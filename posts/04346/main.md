---
Copyright: (C) Ryuichi Ueda
---


# dash/src/eval.h, eval.c
まだ途中。パイプの繋ぎ換えのところの解読が終わった。evalpipe関数の実装の部分は必見。

<a href="http://blog.ueda.asia/?page_id=4219" title="dashのコード解読メモ">「dashのコード解読メモ」に戻る</a>

<h2>eval.h</h2>
[c]
/*-
 * Copyright (c) 1991, 1993
 *	The Regents of the University of California. All rights reserved.
 * Copyright (c) 1997-2005
 *	Herbert Xu &lt;herbert\@gondor.apana.org.au&gt;. All rights reserved.
 *
 * This code is derived from software contributed to Berkeley by
 * Kenneth Almquist.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the University nor the names of its contributors
 * may be used to endorse or promote products derived from this software
 * without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 *
 *	\@(#)eval.h	8.2 (Berkeley) 5/4/95
 */

extern char *commandname;	/* currently executing command */
/* 終了ステータスが入る変数 */
extern int exitstatus;		/* exit status of last command */
/* バッククォートならびに$( )用 */
extern int back_exitstatus;	/* exit status of backquoted command */

/* $( )に親しんでいる者としては
backback言われると違和感あり。
dashは$( )が使えます。 */
struct backcmd {		/* result of evalbackcmd */
	int fd;			/* file descriptor to read from */
	char *buf;		/* buffer */
	int nleft;		/* number of chars in buffer */
	struct job *jp;		/* job structure for command */
};

/* flags in argument to evaltree */
#define EV_EXIT 01		/* exit after evaluating tree */
#define EV_TESTED 02		/* exit status is checked; ignore -e flag */

int evalstring(char *, int);
/*↓bletch = オエッ, ゲロゲロ */
union node;	/* BLETCH for ansi C */

/* ↓こいつがmain.cから呼ばれている。*/
void evaltree(union node *, int);
void evalbackcmd(union node *, struct backcmd *);

/* ↓break等で処理をスキップするときに使う */
extern int evalskip;

/* reasons for skipping commands (see comment on breakcmd routine) */
#define SKIPBREAK	(1 &lt;&lt; 0)
#define SKIPCONT	(1 &lt;&lt; 1)
#define SKIPFUNC	(1 &lt;&lt; 2)
[/c]


<h2>eval.c</h2>

[c]
/*-
 * Copyright (c) 1993
 *	The Regents of the University of California. All rights reserved.
 * Copyright (c) 1997-2005
 *	Herbert Xu &lt;herbert\@gondor.apana.org.au&gt;. All rights reserved.
 *
 * This code is derived from software contributed to Berkeley by
 * Kenneth Almquist.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 * notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 * notice, this list of conditions and the following disclaimer in the
 * documentation and/or other materials provided with the distribution.
 * 3. Neither the name of the University nor the names of its contributors
 * may be used to endorse or promote products derived from this software
 * without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 * SUCH DAMAGE.
 */

#include &lt;stdlib.h&gt;
#include &lt;signal.h&gt;
#include &lt;unistd.h&gt;
#include &lt;sys/types.h&gt;

/*
 * Evaluate a command.
 */

#include &quot;shell.h&quot;
#include &quot;nodes.h&quot;
#include &quot;syntax.h&quot;
#include &quot;expand.h&quot;
#include &quot;parser.h&quot;
#include &quot;jobs.h&quot;
#include &quot;eval.h&quot;
#include &quot;builtins.h&quot;
#include &quot;options.h&quot;
#include &quot;exec.h&quot;
#include &quot;redir.h&quot;
#include &quot;input.h&quot;
#include &quot;output.h&quot;
#include &quot;trap.h&quot;
#include &quot;var.h&quot;
#include &quot;memalloc.h&quot;
#include &quot;error.h&quot;
#include &quot;show.h&quot;
#include &quot;mystring.h&quot;
#ifndef SMALL
#include &quot;myhistedit.h&quot;
#endif


/* ↓* break等で処理をスキップする場合に使う。多用 */
int evalskip;			/* set if we are skipping commands */
/* ↓たくさんネストしたときにいくつ外に出るか。
そんなにネストしちゃいやん。STATICはstaticに変換されます。*/
STATIC int skipcount;		/* number of levels to skip */
/* ↓だからネストするなっつーの
 * MKINITは空文字に変換されます。(shell.h) */
MKINIT int loopnest;		/* current loop nesting level */
static int funcline;		/* starting line number of current function, or 0 if not in a function */

char *commandname;
int exitstatus;			/* exit status of last command */
int back_exitstatus;		/* exit status of backquoted command */

/* nodeという共用体にパースされたスクリプトが入っているので、
 * これを評価していくのが下のevalなんとかという関数群 */

/* ↓これは今のgccを使っていればstaticがくっつくということでOKか？
 * nrというのはおそらくnot return。*/
#if !defined(__alpha__) || (defined(__GNUC__) &amp;&amp; __GNUC__ &gt;= 3)
STATIC
#endif
void evaltreenr(union node *, int) __attribute__ ((__noreturn__));
/* ↓whileとuntilの評価 */
STATIC void evalloop(union node *, int);
/* ↓forの評価 */
STATIC void evalfor(union node *, int);
/* ↓caseの評価 */
STATIC void evalcase(union node *, int);
/* ↓サブシェルとバックグラウンド起動されたプロセスの評価の評価 */
STATIC void evalsubshell(union node *, int);
/* ↓リダイレクト処理*/
STATIC void expredir(union node *);
/* ↓パイプを連結する処理dupしまくり。 */
STATIC void evalpipe(union node *, int);
/* ↓ notyetやめてくれ。
 * ただ、notyetは定義されていないような気がする。
 * 定かではない。*/
#ifdef notyet
STATIC void evalcommand(union node *, int, struct backcmd *);
#else
STATIC void evalcommand(union node *, int);
#endif
/* ↓組み込みコマンド評価用 */
STATIC int evalbltin(const struct builtincmd *, int, char **, int);
/* ↓関数評価用*/
STATIC int evalfun(struct funcnode *, int, char **, int);
/* ---eval関係はここまで。拝承。--- */

/* ↓コマンドを探す関数 */
STATIC void prehash(union node *);
/* ↓オプションに-xが指定されているときに実行された
 * コマンドを標準エラー出力に吐き出す関数 */
STATIC int eprintlist(struct output *, struct strlist *, int);
/* ↓使われてない。テンプレートか？
 * あるいは次に定義されている構造体のため？ */
STATIC int bltincmd(int, char **);

/* ↓なんすかこの書き方?!?!?!?
 * とりあえず内部コマンドの名前と関数のポインタを
 * 格納するものらしい。 */
STATIC const struct builtincmd bltin = {
	name: nullstr,
	builtin: bltincmd
};


/*
 * Called to reset things after an exception.
 */

/* INCLUDEとRESETが何をするものなのかはTOURに書いてあるが、
 * 正直よくわからん。
 * 理解するにはもうちょっと読む必要が。*/

#ifdef mkinit
INCLUDE &quot;eval.h&quot;

RESET {
	evalskip = 0;
	loopnest = 0;
}
#endif



/*
 * The eval commmand.
 */

/* この関数はプロトタイプ宣言されていない 
 * evalbltinでだけ使われている */
static int evalcmd(int argc, char **argv, int flags)
{
 char *p;
 char *concat;
 char **ap;

 if (argc &gt; 1) {
 p = argv[1];
 if (argc &gt; 2) {
 STARTSTACKSTR(concat);
 ap = argv + 2;
 for (;;) {
 	concat = stputs(p, concat);
 if ((p = *ap++) == NULL)
 break;
 STPUTC(' ', concat);
 }
 STPUTC('&#92;&#48;', concat);
 p = grabstackstr(concat);
 }
 return evalstring(p, flags &amp; EV_TESTED);
 }
 return 0;
}


/*
 * Execute a command or commands contained in a string.
 */

int
evalstring(char *s, int flags)
{
	union node *n;
	struct stackmark smark;
	int status;

	setinputstring(s);
	setstackmark(&amp;smark);

	status = 0;
	while ((n = parsecmd(0)) != NEOF) {
		evaltree(n, flags &amp; ~(parser_eof() ? 0 : EV_EXIT));
		status = exitstatus;
		popstackmark(&amp;smark);
		if (evalskip)
			break;
	}
	popfile();

	return status;
}



/*
 * Evaluate a parse tree. The value is left in the global variable
 * exitstatus.
 */

/* main.cのcmdloopから呼ばれているこのファイルでの最重要関数
 * フラグは最初0で来る。フラグにはEV_TESTD等を渡す。*/
void
evaltree(union node *n, int flags)
{
	/* 終了ステータスのマスク。
	* 終了ステータスを */
	int checkexit = 0;
	void (*evalfn)(union node *, int);
	unsigned isor;
	int status;
	if (n == NULL) {
		TRACE((&quot;evaltree(NULL) called\\n&quot;));
		goto out;
	}
#ifndef SMALL
	displayhist = 1;	/* show history substitutions done with fc */
#endif
	TRACE((&quot;pid %d, evaltree(%p: %d, %d) called\\n&quot;,
	getpid(), n, n-&gt;type, flags));

/* ↓ノードに何が入っているかで場合分け
 * ノードには関数からコマンドまでいろんなものが */
	switch (n-&gt;type) {
/* ↓デバッグ用
 * デバッグでなければ素通り */
	default:
#ifdef DEBUG
		out1fmt(&quot;Node type = %d\\n&quot;, n-&gt;type);
#ifndef USE_GLIBC_STDIO
		flushout(out1);
#endif
		break;
#endif
/* ↓!が頭についているとき */
	case NNOT:
		/* そのまま評価して終了ステータスをひっくり返す */
		evaltree(n-&gt;nnot.com, EV_TESTED);
		status = !exitstatus;
		goto setstatus;
/* ↓リダイレクト付きのコマンド列*/
	case NREDIR:
		/* 行番号を収めるerrlinnoはerror.h,
		* linenoはvar.hで定義されている */
		errlinno = lineno = n-&gt;nredir.linno;
		/* 関数の中だったら関数の中での行数にする */
		if (funcline)
			lineno -= funcline - 1;
		/*ノードの中にリダイレクト先やリダイレクト元の指令がある
		*のでその指示をexpredirに渡す */
		expredir(n-&gt;nredir.redirect);
		/* redir.cにある関数何かの初期化をやっているようだがわからん */
		pushredir(n-&gt;nredir.redirect);
		/* （おそらく）リダイレクトを仕掛けてすぐ帰ってくる */
		status = redirectsafe(n-&gt;nredir.redirect, REDIR_PUSH);
		if (!status) {
			/* 下のノード（リダイレクトされている中身）の実行 */
			evaltree(n-&gt;nredir.n, flags &amp; EV_TESTED);
			status = exitstatus;
		}
		/*わからんちん*/
		if (n-&gt;nredir.redirect)
			popredir(0);
		goto setstatus;
/* ↓ 単純な、リダイレクトされていないコマンド */
	case NCMD:
#ifdef notyet
		if (eflag &amp;&amp; !(flags &amp; EV_TESTED))
			checkexit = ~0;
		evalcommand(n, flags, (struct backcmd *)NULL);
		break;
#else
		evalfn = evalcommand;
checkexit:
		/* -eオプションが指定されていたら
		* checkexitを1111...にセットしてエラーで終わるようにする
		* ただし、EV_TESTEDフラグが立っていたら終わらない。 */
		if (eflag &amp;&amp; !(flags &amp; EV_TESTED))
			checkexit = ~0;
		goto calleval;
#endif
/* for */
	case NFOR:
		evalfn = evalfor;
		goto calleval;
/* while, until */
	case NWHILE:
	case NUNTIL:
		evalfn = evalloop;
		goto calleval;
/* サブシェル、バックグラウンド起動 */
	case NSUBSHELL:
	case NBACKGND:
		evalfn = evalsubshell;
		goto checkexit;
/* パイプにつながったコマンド列 */
	case NPIPE:
		evalfn = evalpipe;
		goto checkexit;
/* case */
	case NCASE:
		evalfn = evalcase;
		goto calleval;
/* &amp;&amp;、||、; */
	case NAND:
	case NOR:
	case NSEMI:
/* NANDとNORが正しいかコンパイル前にチェックしている模様 */
#if NAND + 1 != NOR
#error NAND + 1 != NOR
#endif
#if NOR + 1 != NSEMI
#error NOR + 1 != NSEMI
#endif
		/* 真面目に考えていないが、orだとisorフラグが立つ模様 */
		isor = n-&gt;type - NAND;
		/* 左側を評価 */
		evaltree(
			n-&gt;nbinary.ch1,
			/* わからん。 */
			(flags | ((isor &gt;&gt; 1) - 1)) &amp; EV_TESTED
		);
		/* このif文が真になる場合: isorが1で終了ステータスが0 */
		/* isorが0で終了ステータスが1 */
		if (!exitstatus == isor)
			break;
		/* さっきの条件がOKでcontinue等されていなければ右側を評価 */
		if (!evalskip) {
			n = n-&gt;nbinary.ch2;
evaln:
			evalfn = evaltree;
calleval:
			evalfn(n, flags);
			break;
		}
		break;
/* if */
	case NIF:
		/* ifの右側に書いてあるコマンドの評価 */
		evaltree(n-&gt;nif.test, EV_TESTED);
		/* break等で飛ばすことになっていたら飛ばす。
		* あれ？if文に書いてあるコマンドは評価するんか？？？ */
		if (evalskip)
			break;
		/* if文が真ならifに書いてある処理を実行 */
		if (exitstatus == 0) {
			n = n-&gt;nif.ifpart;
			goto evaln;
		/* そうでなければelseに書いてある処理を実行 */
		/* elifはパースのところでifとelseに分解されていると思われる。
		* （未確認） */
		} else if (n-&gt;nif.elsepart) {
			n = n-&gt;nif.elsepart;
			goto evaln;
		}
		/* elseがない場合、コマンドの成否を終了ステータスに反映させない */
		goto success;
/* 関数を解釈する部分（実行は呼ばれるまでしない） */
/* defun: define of function → わかりにくい */
	case NDEFUN:
		defun(n);
/* このラベルの使い方はどうなんだろう？？？ */
success:
		status = 0;
/* これも */
setstatus:
		exitstatus = status;
		break;
	}
out:
	/* checkexitが11111111...
	* なら終了ステータスをチェックして、
	* 0でなければ出る */
	if (checkexit &amp; exitstatus)
		goto exexit;

	/* pendingsigsはtrap.hで定義されている。
	* シグナル関係の処理 */
	if (pendingsigs)
		dotrap();

	/* EV_EXITフラグが立っていたら出る*/
	if (flags &amp; EV_EXIT) {
exexit:
		/* 例外を出す */
		exraise(EXEXIT);
	}
}


/* treeを評価して帰ってこない関数 */
#if !defined(__alpha__) || (defined(__GNUC__) &amp;&amp; __GNUC__ &gt;= 3)
STATIC
#endif
void evaltreenr(union node *n, int flags)
#ifdef HAVE_ATTRIBUTE_ALIAS
/* __attribute__ ... 使ったことなし。
 * evaltree関数の別名としてevaltreenrを定義するという意味になるらしい。
 * しかし、これではnot returnにならないんじゃないのか？分かりません！*/
	__attribute__ ((alias(&quot;evaltree&quot;)));
#else
{
/* __attribute__が使えなければevaltreenrのなかでevaltree関数を呼び出す*/
	evaltree(n, flags);
	/* 死ぬ */
	abort();
}
#endif


/* while, untilの評価 */
STATIC void
evalloop(union node *n, int flags)
{
	int status;

	/* ネストのカウンタを一個増やす */
	loopnest++;
	status = 0;
	flags &amp;= EV_TESTED;
	for (;;) {
		int i;

		/* これは条件のチェックだろうか */
		evaltree(n-&gt;nbinary.ch1, EV_TESTED);
		/* これはbreakやcontinueの処理 */
		if (evalskip) {
			/*continueの場合、カウントがマイナスになれば
			* 0に戻してスキップ解除。インデントずれてたので修正。 */ 
skipping:	if (evalskip == SKIPCONT &amp;&amp; --skipcount &lt;= 0) {
				evalskip = 0;
				continue;
			}
			/*breakの場合、カウントがマイナスになれば解除。
			* インデントずれてたので修正。 */ 
			if (evalskip == SKIPBREAK &amp;&amp; --skipcount &lt;= 0)
				evalskip = 0;
			/* このbreakがシェルスクリプトに書く
			* breakに対応しているので感慨深い。 */
			break;
		}

		/* 条件判定 */
		i = exitstatus;
		/* untilならひっくり返す */
		if (n-&gt;type != NWHILE)
			i = !i;
		/* 条件に合わなければ出る。 */
		if (i != 0)
			break;

		/* ループの中身の処理 */
		evaltree(n-&gt;nbinary.ch2, flags);
		status = exitstatus;
		if (evalskip)
			goto skipping;
	}
	/* ネストのカウンタを戻して出る */
	loopnest--;
	exitstatus = status;
}


/* forの評価 */
STATIC void
evalfor(union node *n, int flags)
{
	/* forで一個ずつ処理するリスト */
	struct arglist arglist;
	/* argpとspは（シェルではなくこの関数の）for文用。昔のCは読みにくい。 */
	union node *argp;
	struct strlist *sp;
	/* たぶんメモリに関する処理に使う */
	struct stackmark smark;

	/* 行番号のリスト */
	errlinno = lineno = n-&gt;nfor.linno;
	/* 関数なら関数内の行番号に補正 */
	if (funcline)
		lineno -= funcline - 1;

	/* setstackmarkはmemalloc.hで定義されている */
	setstackmark(&amp;smark);
	/* forで一個ずつ処理する変数の文字列を展開する。
 	* 展開のついでにnodeからarglistに変数を移す。*/
	arglist.lastp = &amp;arglist.list;
	for (argp = n-&gt;nfor.args ; argp ; argp = argp-&gt;narg.next) {
		expandarg(argp, &amp;arglist, EXP_FULL | EXP_TILDE);
		/* たぶん、このときにbreakがあるとどうなるのか動作が
		* 未定義でとりあえず出るということにしていると思われる。*/
		/* XXX */
		if (evalskip)
			goto out;
	}
	*arglist.lastp = NULL;

	exitstatus = 0;
	loopnest++;
	flags &amp;= EV_TESTED;
	/* for文でぐるぐる処理を回すパート */
	for (sp = arglist.list ; sp ; sp = sp-&gt;next) {
		/* 変数セット */
		setvar(n-&gt;nfor.var, sp-&gt;text, 0);
		/* 評価 */
		evaltree(n-&gt;nfor.body, flags);
		/* continue, breakの処理 */
		if (evalskip) {
			if (evalskip == SKIPCONT &amp;&amp; --skipcount &lt;= 0) {
				evalskip = 0;
				continue;
			}
			if (evalskip == SKIPBREAK &amp;&amp; --skipcount &lt;= 0)
				evalskip = 0;
			break;
		}
	}
	loopnest--;
out:
	popstackmark(&amp;smark);
}


/* case文 */
STATIC void
evalcase(union node *n, int flags)
{
	union node *cp;/* for文用 */
	union node *patp;/* パターンが入っている */
	struct arglist arglist;/* 場合分け対象の文字列を入れる */
	struct stackmark smark;

	/* 行番号 */
	errlinno = lineno = n-&gt;ncase.linno;
	if (funcline)
		lineno -= funcline - 1;

	/* 場合分け対象の文字列を展開してarglistに入れる */
	setstackmark(&amp;smark);
	arglist.lastp = &amp;arglist.list;
	expandarg(n-&gt;ncase.expr, &amp;arglist, EXP_TILDE);
	exitstatus = 0;
	/* caseを一個ずつ試す */
	for (cp = n-&gt;ncase.cases ; cp &amp;&amp; evalskip == 0 ; cp = cp-&gt;nclist.next) {
		/* パターンは複数持てるのかな？あまりcaseを使わないからよく分からない。 */
		for (patp = cp-&gt;nclist.pattern ; patp ; patp = patp-&gt;narg.next) {
			/* マッチしたら中身を実行 */
			if (casematch(patp, arglist.list-&gt;text)) {
				if (evalskip == 0) {
					evaltree(cp-&gt;nclist.body, flags);
				}
				/* シェルのcase文は下に突き抜けないので素直に出る。*/
				goto out;
			}
		}
	}
out:
	popstackmark(&amp;smark);
}



/*
 * Kick off a subshell to evaluate a tree.
 */

/* サブシェルで処理すべき部分の評価 */
STATIC void
evalsubshell(union node *n, int flags)
{
	/* ジョブ */
	struct job *jp;
	/* バックグラウンド起動かどうか */
	int backgnd = (n-&gt;type == NBACKGND);
	int status;

	/* ここら辺は今のセンスだと関数に括り出してほしいなあ */
	errlinno = lineno = n-&gt;nredir.linno;
	if (funcline)
		lineno -= funcline - 1;

	/* リダイレクトの処理 */
	expredir(n-&gt;nredir.redirect);
	/* バックグラウンドでない、-eがセットされている、トラップがない
 	* というよく分からん条件のときはフォークしない */
	if (!backgnd &amp;&amp; flags &amp; EV_EXIT &amp;&amp; !have_traps())
		goto nofork;
	/* 割り込み受け付けない区間 */
	INTOFF;
	/* ジョブ作り。jobs.cで実装。 */
	jp = makejob(n, 1);
	/* サブシェルプロセスをフォーク */
	if (forkshell(jp, n, backgnd) == 0) {
		/* これは子供（サブシェル内）での処理 */

		INTON; /* 割り込み受け付け */
		/* ここらへんの終了条件の理解についてはサボります・・・*/
		flags |= EV_EXIT;
		if (backgnd)
			flags &amp;=~ EV_TESTED;
nofork:
		/* リダイレクト処理してexec。戻ってこない */
		redirect(n-&gt;nredir.redirect, 0);
		evaltreenr(n-&gt;nredir.n, flags);
		/* never returns */
	}
	/* ここはfork元（親シェル）の処理 */
	status = 0;
	/* バックグラウンド起動でなければジョブ待ち */
	if (! backgnd)
		status = waitforjob(jp);
	exitstatus = status;
	INTON;
	/* 割り込み受け付けない区間おわり */
}



/*
 * Compute the names of the files in a redirection list.
 */

/* リダイレクト先やリダイレクト元のパス等を解決して
 * ノードの中の変数に書き込む。*/
STATIC void
expredir(union node *n)
{
	union node *redir;

	/* 入力元やら出力先やら、複数のファイルをさばくわけです。たぶん。 */
	for (redir = n ; redir ; redir = redir-&gt;nfile.next) {
		struct arglist fn;
		fn.lastp = &amp;fn.list;
		switch (redir-&gt;type) {
		case NFROMTO:
		case NFROM:
		case NTO:
		case NCLOBBER:
		case NAPPEND:
			/* 要はファイルの場合 */
			expandarg(redir-&gt;nfile.fname, &amp;fn, EXP_TILDE | EXP_REDIR);
			redir-&gt;nfile.expfname = fn.list-&gt;text;
			break;
		case NFROMFD:
		case NTOFD:
			/* 要はファイル記述子の場合 */
			if (redir-&gt;ndup.vname) {
				expandarg(redir-&gt;ndup.vname, &amp;fn, EXP_FULL | EXP_TILDE);
				/* parser.cで定義されている。
				* ノードにファイル記述子の情報を書く。*/
				fixredir(redir, fn.list-&gt;text, 1);
			}
			break;
		}
	}
}



/*
 * Evaluate a pipeline. All the processes in the pipeline are children
 * of the process creating the pipeline. (This differs from some versions
 * of the shell, which make the last process in a pipeline the parent
 * of all the rest.)
 */

/* 個人的に非常に興味があるが同時に非常にややこしいパイプの処理 */
STATIC void
evalpipe(union node *n, int flags)
{
	struct job *jp;
	struct nodelist *lp;
	/* パイプの長さ=コマンドの数 */
	int pipelen;
	int prevfd;
	/* ピップエレキバン。ではなくてパイプのファイル記述子が入る。*/
	int pip[2];

	TRACE((&quot;evalpipe(0x%lx) called\\n&quot;, (long)n));
	pipelen = 0;
	/* 数えます*/
	for (lp = n-&gt;npipe.cmdlist ; lp ; lp = lp-&gt;next)
		pipelen++;
	/* これはおそらくパイプ途中のコマンドが死んだらアボートさせる処理。
 	* ただ、コマンド途中のコマンドは-eで止めることができないのとどういう関係が
 	* あるのか、正直なところよく分からない。 */
	flags |= EV_EXIT;
	/* パイプ接続中は割り込みを受け付けない */
	INTOFF;
	/* なぜpipelenを渡すのかは、jobs.cを見ないとわからんか。*/
	jp = makejob(n, pipelen);
	prevfd = -1;
	/* コマンドがつながっているだけ繰り返し */
	for (lp = n-&gt;npipe.cmdlist ; lp ; lp = lp-&gt;next) {
		/* パスの解決や関数のルックアップ処理 */
		prehash(lp-&gt;n);
		pip[1] = -1;
		if (lp-&gt;next) {
			/* ここで次のコマンドと接続するためのパイプを作る*/
			/* pipeができんかったらエラー */
			if (pipe(pip) &lt; 0) {
				close(prevfd);
				sh_error(&quot;Pipe call failed&quot;);
			}
		}
 /*
 * --&gt; prevfd &lt;-- pip[0]
 * 親 |
 * --- pip[1]
 * */
 
		/* 今扱っているコマンドのためのフォーク */
		if (forkshell(jp, lp-&gt;n, n-&gt;npipe.backgnd) == 0) {
			/* 子プロセスの方 */
 /*
 * --&gt; prevfd pip[0] &lt;-----&gt; pip[0] &lt;-- prevfd
 * 子 | 親
 * pip[1] ------- pip[1]
 * 			*/

			/* 割り込み許可 */
			INTON;
			/* 書き出し用があったら読み込み用を閉じる */
			if (pip[1] &gt;= 0) {
				close(pip[0]);
			}
			/*
 * --&gt; prevfd ---&gt; pip[0] &lt;-- prevfd
 * 子 | 親
 * pip[1] ------- pip[1]
 * */

			if (prevfd &gt; 0) {
				dup2(prevfd, 0);
				close(prevfd);
			}
			/*
 * --&gt; 0 ---&gt; pip[0] &lt;-- prevfd
 * 子 | 親
 * pip[1] ------- pip[1]
 * 			*/

			/* 書き出しを標準出力に移す */
			if (pip[1] &gt; 1) {
				dup2(pip[1], 1);
				close(pip[1]);
			}
			/*
 * --&gt; 0 ---&gt; pip[0] &lt;-- prevfd
 * 子 | 親
 * 1 ------- pip[1]
 * 			*/

			evaltreenr(lp-&gt;n, flags);
			/* never returns */
		}
		/* 親の処理 */
		if (prevfd &gt;= 0)
			close(prevfd);
		/*
 * --&gt; 0 ---&gt; pip[0] 
 * 子 | 親
 * 1 ------- pip[1]
 * 		*/

		prevfd = pip[0];
		/*
 * (prevfd)
 * --&gt; 0 ---&gt; pip[0] 
 * 子 | 親
 * 1 ------- pip[1]
 * 		*/

		/* 親は書き込みの方を閉じる */
		close(pip[1]);
		/*
 * (prevfd)
 * --&gt; 0 ---&gt; pip[0] 
 * 子 | 親
 * 1 ----
 * 		*/
	}
	/* バックグラウンドでなければパイプラインの処理を待つ */
	if (n-&gt;npipe.backgnd == 0) {
		exitstatus = waitforjob(jp);
		TRACE((&quot;evalpipe: job done exit status %d\\n&quot;, exitstatus));
	}
	INTON;
}



/*
 * Execute a command inside back quotes. If it's a builtin command, we
 * want to save its output in a block obtained from malloc. Otherwise
 * we fork off a subprocess and get the output of the command via a pipe.
 * Should be called with interrupts off.
 */

/* バッククォート、$( )内のコマンドの実行。
 * 上には内部コマンドのときは出力をバッファ貯め、
 * そうでなければ標準出力に出す（want toということだから
 * そうでないかもしれない）とあるが、
 * 下の処理では何があってもforkしているように見える。
 * forkshellを読まないとなんとも言えない。*/
void
evalbackcmd(union node *n, struct backcmd *result)
{
	int pip[2];
	struct job *jp;

	result-&gt;fd = -1;
	result-&gt;buf = NULL;
	result-&gt;nleft = 0;
	result-&gt;jp = NULL;
	if (n == NULL) {
		goto out;
	}

	/* 内部コマンドでもパイプは開くらしい。*/
	if (pipe(pip) &lt; 0)
		sh_error(&quot;Pipe call failed&quot;);
	jp = makejob(n, 1);
	/* FORK_NOJOBはjobs.cで取り扱われる*/
	if (forkshell(jp, n, FORK_NOJOB) == 0) {
		/* 子プロセス */
		/* パイプ接続の流れはevalpipeを参照のこと */

		FORCEINTON;
		/* 親からの入力口を閉じる */
		close(pip[0]);
		/* 書き込み先を子プロセスの標準出力につなぐ */
		if (pip[1] != 1) {
			dup2(pip[1], 1);
			close(pip[1]);
		}
		ifsfree();
		evaltreenr(n, EV_EXIT);
		/* NOTREACHED */
	}
	/* 子につながっている出力先を閉じる */
	close(pip[1]);
	/* 子からの受け入れ口をresultに入れる */
	result-&gt;fd = pip[0];
	result-&gt;jp = jp;

out:
	TRACE((&quot;evalbackcmd done: fd=%d buf=0x%x nleft=%d jp=0x%x\\n&quot;,
		result-&gt;fd, result-&gt;buf, result-&gt;nleft, result-&gt;jp));
}

static char **
parse_command_args(char **argv, const char **path)
{
	char *cp, c;

	for (;;) {
		cp = *++argv;
		if (!cp)
			return 0;
		if (*cp++ != '-')
			break;
		if (!(c = *cp++))
			break;
		if (c == '-' &amp;&amp; !*cp) {
			if (!*++argv)
				return 0;
			break;
		}
		do {
			switch (c) {
			case 'p':
				*path = defpath;
				break;
			default:
				/* run 'typecmd' for other options */
				return 0;
			}
		} while ((c = *cp++));
	}
	return argv;
}



/*
 * Execute a simple command.
 */

STATIC void
#ifdef notyet
evalcommand(union node *cmd, int flags, struct backcmd *backcmd)
#else
evalcommand(union node *cmd, int flags)
#endif
{
	struct localvar_list *localvar_stop;
	struct redirtab *redir_stop;
	struct stackmark smark;
	union node *argp;
	struct arglist arglist;
	struct arglist varlist;
	char **argv;
	int argc;
	struct strlist *sp;
#ifdef notyet
	int pip[2];
#endif
	struct cmdentry cmdentry;
	struct job *jp;
	char *lastarg;
	const char *path;
	int spclbltin;
	int execcmd;
	int status;
	char **nargv;

	errlinno = lineno = cmd-&gt;ncmd.linno;
	if (funcline)
		lineno -= funcline - 1;

	/* First expand the arguments. */
	TRACE((&quot;evalcommand(0x%lx, %d) called\\n&quot;, (long)cmd, flags));
	setstackmark(&amp;smark);
	localvar_stop = pushlocalvars();
	back_exitstatus = 0;

	cmdentry.cmdtype = CMDBUILTIN;
	cmdentry.u.cmd = &amp;bltin;
	varlist.lastp = &amp;varlist.list;
	*varlist.lastp = NULL;
	arglist.lastp = &amp;arglist.list;
	*arglist.lastp = NULL;

	argc = 0;
	for (argp = cmd-&gt;ncmd.args; argp; argp = argp-&gt;narg.next) {
		struct strlist **spp;

		spp = arglist.lastp;
		expandarg(argp, &amp;arglist, EXP_FULL | EXP_TILDE);
		for (sp = *spp; sp; sp = sp-&gt;next)
			argc++;
	}

	/* Reserve one extra spot at the front for shellexec. */
	nargv = stalloc(sizeof (char *) * (argc + 2));
	argv = ++nargv;
	for (sp = arglist.list ; sp ; sp = sp-&gt;next) {
		TRACE((&quot;evalcommand arg: %s\\n&quot;, sp-&gt;text));
		*nargv++ = sp-&gt;text;
	}
	*nargv = NULL;

	lastarg = NULL;
	if (iflag &amp;&amp; funcline == 0 &amp;&amp; argc &gt; 0)
		lastarg = nargv[-1];

	preverrout.fd = 2;
	expredir(cmd-&gt;ncmd.redirect);
	redir_stop = pushredir(cmd-&gt;ncmd.redirect);
	status = redirectsafe(cmd-&gt;ncmd.redirect, REDIR_PUSH|REDIR_SAVEFD2);

	path = vpath.text;
	for (argp = cmd-&gt;ncmd.assign; argp; argp = argp-&gt;narg.next) {
		struct strlist **spp;
		char *p;

		spp = varlist.lastp;
		expandarg(argp, &amp;varlist, EXP_VARTILDE);

		mklocal((*spp)-&gt;text);

		/*
		* Modify the command lookup path, if a PATH= assignment
		* is present
		*/
		p = (*spp)-&gt;text;
		if (varequal(p, path))
			path = p;
	}

	/* Print the command if xflag is set. */
	if (xflag) {
		struct output *out;
		int sep;

		out = &amp;preverrout;
		outstr(expandstr(ps4val()), out);
		sep = 0;
		sep = eprintlist(out, varlist.list, sep);
		eprintlist(out, arglist.list, sep);
		outcslow('\\n', out);
#ifdef FLUSHERR
		flushout(out);
#endif
	}

	execcmd = 0;
	spclbltin = -1;

	/* Now locate the command. */
	if (argc) {
		const char *oldpath;
		int cmd_flag = DO_ERR;

		path += 5;
		oldpath = path;
		for (;;) {
			find_command(argv[0], &amp;cmdentry, cmd_flag, path);
			if (cmdentry.cmdtype == CMDUNKNOWN) {
				status = 127;
#ifdef FLUSHERR
				flushout(&amp;errout);
#endif
				goto bail;
			}

			/* implement bltin and command here */
			if (cmdentry.cmdtype != CMDBUILTIN)
				break;
			if (spclbltin &lt; 0)
				spclbltin = 
					cmdentry.u.cmd-&gt;flags &amp;
					BUILTIN_SPECIAL
				;
			if (cmdentry.u.cmd == EXECCMD)
				execcmd++;
			if (cmdentry.u.cmd != COMMANDCMD)
				break;

			path = oldpath;
			nargv = parse_command_args(argv, &amp;path);
			if (!nargv)
				break;
			argc -= nargv - argv;
			argv = nargv;
			cmd_flag |= DO_NOFUNC;
		}
	}

	if (status) {
bail:
		exitstatus = status;

		/* We have a redirection error. */
		if (spclbltin &gt; 0)
			exraise(EXERROR);

		goto out;
	}

	/* Execute the command. */
	switch (cmdentry.cmdtype) {
	default:
		/* Fork off a child process if necessary. */
		if (!(flags &amp; EV_EXIT) || have_traps()) {
			INTOFF;
			jp = makejob(cmd, 1);
			if (forkshell(jp, cmd, FORK_FG) != 0) {
				exitstatus = waitforjob(jp);
				INTON;
				break;
			}
			FORCEINTON;
		}
		listsetvar(varlist.list, VEXPORT|VSTACK);
		shellexec(argv, path, cmdentry.u.index);
		/* NOTREACHED */

	case CMDBUILTIN:
		if (spclbltin &gt; 0 || argc == 0) {
			poplocalvars(1);
			if (execcmd &amp;&amp; argc &gt; 1)
				listsetvar(varlist.list, VEXPORT);
		}
		if (evalbltin(cmdentry.u.cmd, argc, argv, flags)) {
			int status;
			int i;

			i = exception;
			if (i == EXEXIT)
				goto raise;

			status = (i == EXINT) ? SIGINT + 128 : 2;
			exitstatus = status;

			if (i == EXINT || spclbltin &gt; 0) {
raise:
				longjmp(handler-&gt;loc, 1);
			}
			FORCEINTON;
		}
		break;

	case CMDFUNCTION:
		poplocalvars(1);
		if (evalfun(cmdentry.u.func, argc, argv, flags))
			goto raise;
		break;
	}

out:
	if (cmd-&gt;ncmd.redirect)
		popredir(execcmd);
	unwindredir(redir_stop);
	unwindlocalvars(localvar_stop);
	if (lastarg)
		/* dsl: I think this is intended to be used to support
		* '_' in 'vi' command mode during line editing...
		* However I implemented that within libedit itself.
		*/
		setvar(&quot;_&quot;, lastarg, 0);
	popstackmark(&amp;smark);
}

/* evalcommandでだけ使われている */
STATIC int
evalbltin(const struct builtincmd *cmd, int argc, char **argv, int flags)
{
	char *volatile savecmdname;
	struct jmploc *volatile savehandler;
	struct jmploc jmploc;
	int status;
	int i;

	savecmdname = commandname;
	savehandler = handler;
	if ((i = setjmp(jmploc.loc)))
		goto cmddone;
	handler = &amp;jmploc;
	commandname = argv[0];
	argptr = argv + 1;
	optptr = NULL;			/* initialize nextopt */
	if (cmd == EVALCMD)
		status = evalcmd(argc, argv, flags);
	else
		status = (*cmd-&gt;builtin)(argc, argv);
	flushall();
	status |= outerr(out1);
	exitstatus = status;
cmddone:
	freestdout();
	commandname = savecmdname;
	handler = savehandler;

	return i;
}

STATIC int
evalfun(struct funcnode *func, int argc, char **argv, int flags)
{
	volatile struct shparam saveparam;
	struct jmploc *volatile savehandler;
	struct jmploc jmploc;
	int e;
	int savefuncline;

	saveparam = shellparam;
	savefuncline = funcline;
	savehandler = handler;
	if ((e = setjmp(jmploc.loc))) {
		goto funcdone;
	}
	INTOFF;
	handler = &amp;jmploc;
	shellparam.malloc = 0;
	func-&gt;count++;
	funcline = func-&gt;n.ndefun.linno;
	INTON;
	shellparam.nparam = argc - 1;
	shellparam.p = argv + 1;
	shellparam.optind = 1;
	shellparam.optoff = -1;
	pushlocalvars();
	evaltree(func-&gt;n.ndefun.body, flags &amp; EV_TESTED);
	poplocalvars(0);
funcdone:
	INTOFF;
	funcline = savefuncline;
	freefunc(func);
	freeparam(&amp;shellparam);
	shellparam = saveparam;
	handler = savehandler;
	INTON;
	evalskip &amp;= ~SKIPFUNC;
	return e;
}


/*
 * Search for a command. This is called before we fork so that the
 * location of the command will be available in the parent as well as
 * the child. The check for &quot;goodname&quot; is an overly conservative
 * check that the name will not be subject to expansion.
 */

STATIC void
prehash(union node *n)
{
	struct cmdentry entry;

	if (n-&gt;type == NCMD &amp;&amp; n-&gt;ncmd.args)
		if (goodname(n-&gt;ncmd.args-&gt;narg.text))
			find_command(n-&gt;ncmd.args-&gt;narg.text, &amp;entry, 0,
				pathval());
}



/*
 * Builtin commands. Builtin commands whose functions are closely
 * tied to evaluation are implemented here.
 */

/*
 * No command given.
 */

STATIC int
bltincmd(int argc, char **argv)
{
	/*
	* Preserve exitstatus of a previous possible redirection
	* as POSIX mandates
	*/
	return back_exitstatus;
}


/*
 * Handle break and continue commands. Break, continue, and return are
 * all handled by setting the evalskip flag. The evaluation routines
 * above all check this flag, and if it is set they start skipping
 * commands rather than executing them. The variable skipcount is
 * the number of loops to break/continue, or the number of function
 * levels to return. (The latter is always 1.) It should probably
 * be an error to break out of more loops than exist, but it isn't
 * in the standard shell so we don't make it one here.
 */

int
breakcmd(int argc, char **argv)
{
	int n = argc &gt; 1 ? number(argv[1]) : 1;

	if (n &lt;= 0)
		badnum(argv[1]);
	if (n &gt; loopnest)
		n = loopnest;
	if (n &gt; 0) {
		evalskip = (**argv == 'c')? SKIPCONT : SKIPBREAK;
		skipcount = n;
	}
	return 0;
}


/*
 * The return command.
 */

int
returncmd(int argc, char **argv)
{
	/*
	* If called outside a function, do what ksh does;
	* skip the rest of the file.
	*/
	evalskip = SKIPFUNC;
	return argv[1] ? number(argv[1]) : exitstatus;
}


int
falsecmd(int argc, char **argv)
{
	return 1;
}


int
truecmd(int argc, char **argv)
{
	return 0;
}


int
execcmd(int argc, char **argv)
{
	if (argc &gt; 1) {
		iflag = 0;		/* exit on error */
		mflag = 0;
		optschanged();
		shellexec(argv + 1, pathval(), 0);
	}
	return 0;
}


STATIC int
eprintlist(struct output *out, struct strlist *sp, int sep)
{
	while (sp) {
		const char *p;

		p = &quot; %s&quot; + (1 - sep);
		sep |= 1;
		outfmt(out, p, sp-&gt;text);
		sp = sp-&gt;next;
	}

	return sep;
}
[/c]
