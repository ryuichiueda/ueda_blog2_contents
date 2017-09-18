---
Copyright: (C) Ryuichi Ueda
---

# dash/src/eval.h, eval.c
まだ途中。パイプの繋ぎ換えのところの解読が終わった。evalpipe関数の実装の部分は必見。<br />
<br />
<a href="http://blog.ueda.asia/?page_id=4219" title="dashのコード解読メモ">「dashのコード解読メモ」に戻る</a><br />
<br />
<h2>eval.h</h2><br />
[c]<br />
/*-<br />
 * Copyright (c) 1991, 1993<br />
 *	The Regents of the University of California. All rights reserved.<br />
 * Copyright (c) 1997-2005<br />
 *	Herbert Xu &lt;herbert\@gondor.apana.org.au&gt;. All rights reserved.<br />
 *<br />
 * This code is derived from software contributed to Berkeley by<br />
 * Kenneth Almquist.<br />
 *<br />
 * Redistribution and use in source and binary forms, with or without<br />
 * modification, are permitted provided that the following conditions<br />
 * are met:<br />
 * 1. Redistributions of source code must retain the above copyright<br />
 * notice, this list of conditions and the following disclaimer.<br />
 * 2. Redistributions in binary form must reproduce the above copyright<br />
 * notice, this list of conditions and the following disclaimer in the<br />
 * documentation and/or other materials provided with the distribution.<br />
 * 3. Neither the name of the University nor the names of its contributors<br />
 * may be used to endorse or promote products derived from this software<br />
 * without specific prior written permission.<br />
 *<br />
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND<br />
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE<br />
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE<br />
 * ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE<br />
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL<br />
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS<br />
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)<br />
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT<br />
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY<br />
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF<br />
 * SUCH DAMAGE.<br />
 *<br />
 *	\@(#)eval.h	8.2 (Berkeley) 5/4/95<br />
 */<br />
<br />
extern char *commandname;	/* currently executing command */<br />
/* 終了ステータスが入る変数 */<br />
extern int exitstatus;		/* exit status of last command */<br />
/* バッククォートならびに$( )用 */<br />
extern int back_exitstatus;	/* exit status of backquoted command */<br />
<br />
/* $( )に親しんでいる者としては<br />
backback言われると違和感あり。<br />
dashは$( )が使えます。 */<br />
struct backcmd {		/* result of evalbackcmd */<br />
	int fd;			/* file descriptor to read from */<br />
	char *buf;		/* buffer */<br />
	int nleft;		/* number of chars in buffer */<br />
	struct job *jp;		/* job structure for command */<br />
};<br />
<br />
/* flags in argument to evaltree */<br />
#define EV_EXIT 01		/* exit after evaluating tree */<br />
#define EV_TESTED 02		/* exit status is checked; ignore -e flag */<br />
<br />
int evalstring(char *, int);<br />
/*↓bletch = オエッ, ゲロゲロ */<br />
union node;	/* BLETCH for ansi C */<br />
<br />
/* ↓こいつがmain.cから呼ばれている。*/<br />
void evaltree(union node *, int);<br />
void evalbackcmd(union node *, struct backcmd *);<br />
<br />
/* ↓break等で処理をスキップするときに使う */<br />
extern int evalskip;<br />
<br />
/* reasons for skipping commands (see comment on breakcmd routine) */<br />
#define SKIPBREAK	(1 &lt;&lt; 0)<br />
#define SKIPCONT	(1 &lt;&lt; 1)<br />
#define SKIPFUNC	(1 &lt;&lt; 2)<br />
[/c]<br />
<br />
<br />
<h2>eval.c</h2><br />
<br />
[c]<br />
/*-<br />
 * Copyright (c) 1993<br />
 *	The Regents of the University of California. All rights reserved.<br />
 * Copyright (c) 1997-2005<br />
 *	Herbert Xu &lt;herbert\@gondor.apana.org.au&gt;. All rights reserved.<br />
 *<br />
 * This code is derived from software contributed to Berkeley by<br />
 * Kenneth Almquist.<br />
 *<br />
 * Redistribution and use in source and binary forms, with or without<br />
 * modification, are permitted provided that the following conditions<br />
 * are met:<br />
 * 1. Redistributions of source code must retain the above copyright<br />
 * notice, this list of conditions and the following disclaimer.<br />
 * 2. Redistributions in binary form must reproduce the above copyright<br />
 * notice, this list of conditions and the following disclaimer in the<br />
 * documentation and/or other materials provided with the distribution.<br />
 * 3. Neither the name of the University nor the names of its contributors<br />
 * may be used to endorse or promote products derived from this software<br />
 * without specific prior written permission.<br />
 *<br />
 * THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS'' AND<br />
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE<br />
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE<br />
 * ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS BE LIABLE<br />
 * FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL<br />
 * DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS<br />
 * OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)<br />
 * HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT<br />
 * LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY<br />
 * OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF<br />
 * SUCH DAMAGE.<br />
 */<br />
<br />
#include &lt;stdlib.h&gt;<br />
#include &lt;signal.h&gt;<br />
#include &lt;unistd.h&gt;<br />
#include &lt;sys/types.h&gt;<br />
<br />
/*<br />
 * Evaluate a command.<br />
 */<br />
<br />
#include &quot;shell.h&quot;<br />
#include &quot;nodes.h&quot;<br />
#include &quot;syntax.h&quot;<br />
#include &quot;expand.h&quot;<br />
#include &quot;parser.h&quot;<br />
#include &quot;jobs.h&quot;<br />
#include &quot;eval.h&quot;<br />
#include &quot;builtins.h&quot;<br />
#include &quot;options.h&quot;<br />
#include &quot;exec.h&quot;<br />
#include &quot;redir.h&quot;<br />
#include &quot;input.h&quot;<br />
#include &quot;output.h&quot;<br />
#include &quot;trap.h&quot;<br />
#include &quot;var.h&quot;<br />
#include &quot;memalloc.h&quot;<br />
#include &quot;error.h&quot;<br />
#include &quot;show.h&quot;<br />
#include &quot;mystring.h&quot;<br />
#ifndef SMALL<br />
#include &quot;myhistedit.h&quot;<br />
#endif<br />
<br />
<br />
/* ↓* break等で処理をスキップする場合に使う。多用 */<br />
int evalskip;			/* set if we are skipping commands */<br />
/* ↓たくさんネストしたときにいくつ外に出るか。<br />
そんなにネストしちゃいやん。STATICはstaticに変換されます。*/<br />
STATIC int skipcount;		/* number of levels to skip */<br />
/* ↓だからネストするなっつーの<br />
 * MKINITは空文字に変換されます。(shell.h) */<br />
MKINIT int loopnest;		/* current loop nesting level */<br />
static int funcline;		/* starting line number of current function, or 0 if not in a function */<br />
<br />
char *commandname;<br />
int exitstatus;			/* exit status of last command */<br />
int back_exitstatus;		/* exit status of backquoted command */<br />
<br />
/* nodeという共用体にパースされたスクリプトが入っているので、<br />
 * これを評価していくのが下のevalなんとかという関数群 */<br />
<br />
/* ↓これは今のgccを使っていればstaticがくっつくということでOKか？<br />
 * nrというのはおそらくnot return。*/<br />
#if !defined(__alpha__) || (defined(__GNUC__) &amp;&amp; __GNUC__ &gt;= 3)<br />
STATIC<br />
#endif<br />
void evaltreenr(union node *, int) __attribute__ ((__noreturn__));<br />
/* ↓whileとuntilの評価 */<br />
STATIC void evalloop(union node *, int);<br />
/* ↓forの評価 */<br />
STATIC void evalfor(union node *, int);<br />
/* ↓caseの評価 */<br />
STATIC void evalcase(union node *, int);<br />
/* ↓サブシェルとバックグラウンド起動されたプロセスの評価の評価 */<br />
STATIC void evalsubshell(union node *, int);<br />
/* ↓リダイレクト処理*/<br />
STATIC void expredir(union node *);<br />
/* ↓パイプを連結する処理dupしまくり。 */<br />
STATIC void evalpipe(union node *, int);<br />
/* ↓ notyetやめてくれ。<br />
 * ただ、notyetは定義されていないような気がする。<br />
 * 定かではない。*/<br />
#ifdef notyet<br />
STATIC void evalcommand(union node *, int, struct backcmd *);<br />
#else<br />
STATIC void evalcommand(union node *, int);<br />
#endif<br />
/* ↓組み込みコマンド評価用 */<br />
STATIC int evalbltin(const struct builtincmd *, int, char **, int);<br />
/* ↓関数評価用*/<br />
STATIC int evalfun(struct funcnode *, int, char **, int);<br />
/* ---eval関係はここまで。拝承。--- */<br />
<br />
/* ↓コマンドを探す関数 */<br />
STATIC void prehash(union node *);<br />
/* ↓オプションに-xが指定されているときに実行された<br />
 * コマンドを標準エラー出力に吐き出す関数 */<br />
STATIC int eprintlist(struct output *, struct strlist *, int);<br />
/* ↓使われてない。テンプレートか？<br />
 * あるいは次に定義されている構造体のため？ */<br />
STATIC int bltincmd(int, char **);<br />
<br />
/* ↓なんすかこの書き方?!?!?!?<br />
 * とりあえず内部コマンドの名前と関数のポインタを<br />
 * 格納するものらしい。 */<br />
STATIC const struct builtincmd bltin = {<br />
	name: nullstr,<br />
	builtin: bltincmd<br />
};<br />
<br />
<br />
/*<br />
 * Called to reset things after an exception.<br />
 */<br />
<br />
/* INCLUDEとRESETが何をするものなのかはTOURに書いてあるが、<br />
 * 正直よくわからん。<br />
 * 理解するにはもうちょっと読む必要が。*/<br />
<br />
#ifdef mkinit<br />
INCLUDE &quot;eval.h&quot;<br />
<br />
RESET {<br />
	evalskip = 0;<br />
	loopnest = 0;<br />
}<br />
#endif<br />
<br />
<br />
<br />
/*<br />
 * The eval commmand.<br />
 */<br />
<br />
/* この関数はプロトタイプ宣言されていない <br />
 * evalbltinでだけ使われている */<br />
static int evalcmd(int argc, char **argv, int flags)<br />
{<br />
 char *p;<br />
 char *concat;<br />
 char **ap;<br />
<br />
 if (argc &gt; 1) {<br />
 p = argv[1];<br />
 if (argc &gt; 2) {<br />
 STARTSTACKSTR(concat);<br />
 ap = argv + 2;<br />
 for (;;) {<br />
 	concat = stputs(p, concat);<br />
 if ((p = *ap++) == NULL)<br />
 break;<br />
 STPUTC(' ', concat);<br />
 }<br />
 STPUTC('&#92;&#48;', concat);<br />
 p = grabstackstr(concat);<br />
 }<br />
 return evalstring(p, flags &amp; EV_TESTED);<br />
 }<br />
 return 0;<br />
}<br />
<br />
<br />
/*<br />
 * Execute a command or commands contained in a string.<br />
 */<br />
<br />
int<br />
evalstring(char *s, int flags)<br />
{<br />
	union node *n;<br />
	struct stackmark smark;<br />
	int status;<br />
<br />
	setinputstring(s);<br />
	setstackmark(&amp;smark);<br />
<br />
	status = 0;<br />
	while ((n = parsecmd(0)) != NEOF) {<br />
		evaltree(n, flags &amp; ~(parser_eof() ? 0 : EV_EXIT));<br />
		status = exitstatus;<br />
		popstackmark(&amp;smark);<br />
		if (evalskip)<br />
			break;<br />
	}<br />
	popfile();<br />
<br />
	return status;<br />
}<br />
<br />
<br />
<br />
/*<br />
 * Evaluate a parse tree. The value is left in the global variable<br />
 * exitstatus.<br />
 */<br />
<br />
/* main.cのcmdloopから呼ばれているこのファイルでの最重要関数<br />
 * フラグは最初0で来る。フラグにはEV_TESTD等を渡す。*/<br />
void<br />
evaltree(union node *n, int flags)<br />
{<br />
	/* 終了ステータスのマスク。<br />
	* 終了ステータスを */<br />
	int checkexit = 0;<br />
	void (*evalfn)(union node *, int);<br />
	unsigned isor;<br />
	int status;<br />
	if (n == NULL) {<br />
		TRACE((&quot;evaltree(NULL) called\\n&quot;));<br />
		goto out;<br />
	}<br />
#ifndef SMALL<br />
	displayhist = 1;	/* show history substitutions done with fc */<br />
#endif<br />
	TRACE((&quot;pid %d, evaltree(%p: %d, %d) called\\n&quot;,<br />
	getpid(), n, n-&gt;type, flags));<br />
<br />
/* ↓ノードに何が入っているかで場合分け<br />
 * ノードには関数からコマンドまでいろんなものが */<br />
	switch (n-&gt;type) {<br />
/* ↓デバッグ用<br />
 * デバッグでなければ素通り */<br />
	default:<br />
#ifdef DEBUG<br />
		out1fmt(&quot;Node type = %d\\n&quot;, n-&gt;type);<br />
#ifndef USE_GLIBC_STDIO<br />
		flushout(out1);<br />
#endif<br />
		break;<br />
#endif<br />
/* ↓!が頭についているとき */<br />
	case NNOT:<br />
		/* そのまま評価して終了ステータスをひっくり返す */<br />
		evaltree(n-&gt;nnot.com, EV_TESTED);<br />
		status = !exitstatus;<br />
		goto setstatus;<br />
/* ↓リダイレクト付きのコマンド列*/<br />
	case NREDIR:<br />
		/* 行番号を収めるerrlinnoはerror.h,<br />
		* linenoはvar.hで定義されている */<br />
		errlinno = lineno = n-&gt;nredir.linno;<br />
		/* 関数の中だったら関数の中での行数にする */<br />
		if (funcline)<br />
			lineno -= funcline - 1;<br />
		/*ノードの中にリダイレクト先やリダイレクト元の指令がある<br />
		*のでその指示をexpredirに渡す */<br />
		expredir(n-&gt;nredir.redirect);<br />
		/* redir.cにある関数何かの初期化をやっているようだがわからん */<br />
		pushredir(n-&gt;nredir.redirect);<br />
		/* （おそらく）リダイレクトを仕掛けてすぐ帰ってくる */<br />
		status = redirectsafe(n-&gt;nredir.redirect, REDIR_PUSH);<br />
		if (!status) {<br />
			/* 下のノード（リダイレクトされている中身）の実行 */<br />
			evaltree(n-&gt;nredir.n, flags &amp; EV_TESTED);<br />
			status = exitstatus;<br />
		}<br />
		/*わからんちん*/<br />
		if (n-&gt;nredir.redirect)<br />
			popredir(0);<br />
		goto setstatus;<br />
/* ↓ 単純な、リダイレクトされていないコマンド */<br />
	case NCMD:<br />
#ifdef notyet<br />
		if (eflag &amp;&amp; !(flags &amp; EV_TESTED))<br />
			checkexit = ~0;<br />
		evalcommand(n, flags, (struct backcmd *)NULL);<br />
		break;<br />
#else<br />
		evalfn = evalcommand;<br />
checkexit:<br />
		/* -eオプションが指定されていたら<br />
		* checkexitを1111...にセットしてエラーで終わるようにする<br />
		* ただし、EV_TESTEDフラグが立っていたら終わらない。 */<br />
		if (eflag &amp;&amp; !(flags &amp; EV_TESTED))<br />
			checkexit = ~0;<br />
		goto calleval;<br />
#endif<br />
/* for */<br />
	case NFOR:<br />
		evalfn = evalfor;<br />
		goto calleval;<br />
/* while, until */<br />
	case NWHILE:<br />
	case NUNTIL:<br />
		evalfn = evalloop;<br />
		goto calleval;<br />
/* サブシェル、バックグラウンド起動 */<br />
	case NSUBSHELL:<br />
	case NBACKGND:<br />
		evalfn = evalsubshell;<br />
		goto checkexit;<br />
/* パイプにつながったコマンド列 */<br />
	case NPIPE:<br />
		evalfn = evalpipe;<br />
		goto checkexit;<br />
/* case */<br />
	case NCASE:<br />
		evalfn = evalcase;<br />
		goto calleval;<br />
/* &amp;&amp;、||、; */<br />
	case NAND:<br />
	case NOR:<br />
	case NSEMI:<br />
/* NANDとNORが正しいかコンパイル前にチェックしている模様 */<br />
#if NAND + 1 != NOR<br />
#error NAND + 1 != NOR<br />
#endif<br />
#if NOR + 1 != NSEMI<br />
#error NOR + 1 != NSEMI<br />
#endif<br />
		/* 真面目に考えていないが、orだとisorフラグが立つ模様 */<br />
		isor = n-&gt;type - NAND;<br />
		/* 左側を評価 */<br />
		evaltree(<br />
			n-&gt;nbinary.ch1,<br />
			/* わからん。 */<br />
			(flags | ((isor &gt;&gt; 1) - 1)) &amp; EV_TESTED<br />
		);<br />
		/* このif文が真になる場合: isorが1で終了ステータスが0 */<br />
		/* isorが0で終了ステータスが1 */<br />
		if (!exitstatus == isor)<br />
			break;<br />
		/* さっきの条件がOKでcontinue等されていなければ右側を評価 */<br />
		if (!evalskip) {<br />
			n = n-&gt;nbinary.ch2;<br />
evaln:<br />
			evalfn = evaltree;<br />
calleval:<br />
			evalfn(n, flags);<br />
			break;<br />
		}<br />
		break;<br />
/* if */<br />
	case NIF:<br />
		/* ifの右側に書いてあるコマンドの評価 */<br />
		evaltree(n-&gt;nif.test, EV_TESTED);<br />
		/* break等で飛ばすことになっていたら飛ばす。<br />
		* あれ？if文に書いてあるコマンドは評価するんか？？？ */<br />
		if (evalskip)<br />
			break;<br />
		/* if文が真ならifに書いてある処理を実行 */<br />
		if (exitstatus == 0) {<br />
			n = n-&gt;nif.ifpart;<br />
			goto evaln;<br />
		/* そうでなければelseに書いてある処理を実行 */<br />
		/* elifはパースのところでifとelseに分解されていると思われる。<br />
		* （未確認） */<br />
		} else if (n-&gt;nif.elsepart) {<br />
			n = n-&gt;nif.elsepart;<br />
			goto evaln;<br />
		}<br />
		/* elseがない場合、コマンドの成否を終了ステータスに反映させない */<br />
		goto success;<br />
/* 関数を解釈する部分（実行は呼ばれるまでしない） */<br />
/* defun: define of function → わかりにくい */<br />
	case NDEFUN:<br />
		defun(n);<br />
/* このラベルの使い方はどうなんだろう？？？ */<br />
success:<br />
		status = 0;<br />
/* これも */<br />
setstatus:<br />
		exitstatus = status;<br />
		break;<br />
	}<br />
out:<br />
	/* checkexitが11111111...<br />
	* なら終了ステータスをチェックして、<br />
	* 0でなければ出る */<br />
	if (checkexit &amp; exitstatus)<br />
		goto exexit;<br />
<br />
	/* pendingsigsはtrap.hで定義されている。<br />
	* シグナル関係の処理 */<br />
	if (pendingsigs)<br />
		dotrap();<br />
<br />
	/* EV_EXITフラグが立っていたら出る*/<br />
	if (flags &amp; EV_EXIT) {<br />
exexit:<br />
		/* 例外を出す */<br />
		exraise(EXEXIT);<br />
	}<br />
}<br />
<br />
<br />
/* treeを評価して帰ってこない関数 */<br />
#if !defined(__alpha__) || (defined(__GNUC__) &amp;&amp; __GNUC__ &gt;= 3)<br />
STATIC<br />
#endif<br />
void evaltreenr(union node *n, int flags)<br />
#ifdef HAVE_ATTRIBUTE_ALIAS<br />
/* __attribute__ ... 使ったことなし。<br />
 * evaltree関数の別名としてevaltreenrを定義するという意味になるらしい。<br />
 * しかし、これではnot returnにならないんじゃないのか？分かりません！*/<br />
	__attribute__ ((alias(&quot;evaltree&quot;)));<br />
#else<br />
{<br />
/* __attribute__が使えなければevaltreenrのなかでevaltree関数を呼び出す*/<br />
	evaltree(n, flags);<br />
	/* 死ぬ */<br />
	abort();<br />
}<br />
#endif<br />
<br />
<br />
/* while, untilの評価 */<br />
STATIC void<br />
evalloop(union node *n, int flags)<br />
{<br />
	int status;<br />
<br />
	/* ネストのカウンタを一個増やす */<br />
	loopnest++;<br />
	status = 0;<br />
	flags &amp;= EV_TESTED;<br />
	for (;;) {<br />
		int i;<br />
<br />
		/* これは条件のチェックだろうか */<br />
		evaltree(n-&gt;nbinary.ch1, EV_TESTED);<br />
		/* これはbreakやcontinueの処理 */<br />
		if (evalskip) {<br />
			/*continueの場合、カウントがマイナスになれば<br />
			* 0に戻してスキップ解除。インデントずれてたので修正。 */ <br />
skipping:	if (evalskip == SKIPCONT &amp;&amp; --skipcount &lt;= 0) {<br />
				evalskip = 0;<br />
				continue;<br />
			}<br />
			/*breakの場合、カウントがマイナスになれば解除。<br />
			* インデントずれてたので修正。 */ <br />
			if (evalskip == SKIPBREAK &amp;&amp; --skipcount &lt;= 0)<br />
				evalskip = 0;<br />
			/* このbreakがシェルスクリプトに書く<br />
			* breakに対応しているので感慨深い。 */<br />
			break;<br />
		}<br />
<br />
		/* 条件判定 */<br />
		i = exitstatus;<br />
		/* untilならひっくり返す */<br />
		if (n-&gt;type != NWHILE)<br />
			i = !i;<br />
		/* 条件に合わなければ出る。 */<br />
		if (i != 0)<br />
			break;<br />
<br />
		/* ループの中身の処理 */<br />
		evaltree(n-&gt;nbinary.ch2, flags);<br />
		status = exitstatus;<br />
		if (evalskip)<br />
			goto skipping;<br />
	}<br />
	/* ネストのカウンタを戻して出る */<br />
	loopnest--;<br />
	exitstatus = status;<br />
}<br />
<br />
<br />
/* forの評価 */<br />
STATIC void<br />
evalfor(union node *n, int flags)<br />
{<br />
	/* forで一個ずつ処理するリスト */<br />
	struct arglist arglist;<br />
	/* argpとspは（シェルではなくこの関数の）for文用。昔のCは読みにくい。 */<br />
	union node *argp;<br />
	struct strlist *sp;<br />
	/* たぶんメモリに関する処理に使う */<br />
	struct stackmark smark;<br />
<br />
	/* 行番号のリスト */<br />
	errlinno = lineno = n-&gt;nfor.linno;<br />
	/* 関数なら関数内の行番号に補正 */<br />
	if (funcline)<br />
		lineno -= funcline - 1;<br />
<br />
	/* setstackmarkはmemalloc.hで定義されている */<br />
	setstackmark(&amp;smark);<br />
	/* forで一個ずつ処理する変数の文字列を展開する。<br />
 	* 展開のついでにnodeからarglistに変数を移す。*/<br />
	arglist.lastp = &amp;arglist.list;<br />
	for (argp = n-&gt;nfor.args ; argp ; argp = argp-&gt;narg.next) {<br />
		expandarg(argp, &amp;arglist, EXP_FULL | EXP_TILDE);<br />
		/* たぶん、このときにbreakがあるとどうなるのか動作が<br />
		* 未定義でとりあえず出るということにしていると思われる。*/<br />
		/* XXX */<br />
		if (evalskip)<br />
			goto out;<br />
	}<br />
	*arglist.lastp = NULL;<br />
<br />
	exitstatus = 0;<br />
	loopnest++;<br />
	flags &amp;= EV_TESTED;<br />
	/* for文でぐるぐる処理を回すパート */<br />
	for (sp = arglist.list ; sp ; sp = sp-&gt;next) {<br />
		/* 変数セット */<br />
		setvar(n-&gt;nfor.var, sp-&gt;text, 0);<br />
		/* 評価 */<br />
		evaltree(n-&gt;nfor.body, flags);<br />
		/* continue, breakの処理 */<br />
		if (evalskip) {<br />
			if (evalskip == SKIPCONT &amp;&amp; --skipcount &lt;= 0) {<br />
				evalskip = 0;<br />
				continue;<br />
			}<br />
			if (evalskip == SKIPBREAK &amp;&amp; --skipcount &lt;= 0)<br />
				evalskip = 0;<br />
			break;<br />
		}<br />
	}<br />
	loopnest--;<br />
out:<br />
	popstackmark(&amp;smark);<br />
}<br />
<br />
<br />
/* case文 */<br />
STATIC void<br />
evalcase(union node *n, int flags)<br />
{<br />
	union node *cp;/* for文用 */<br />
	union node *patp;/* パターンが入っている */<br />
	struct arglist arglist;/* 場合分け対象の文字列を入れる */<br />
	struct stackmark smark;<br />
<br />
	/* 行番号 */<br />
	errlinno = lineno = n-&gt;ncase.linno;<br />
	if (funcline)<br />
		lineno -= funcline - 1;<br />
<br />
	/* 場合分け対象の文字列を展開してarglistに入れる */<br />
	setstackmark(&amp;smark);<br />
	arglist.lastp = &amp;arglist.list;<br />
	expandarg(n-&gt;ncase.expr, &amp;arglist, EXP_TILDE);<br />
	exitstatus = 0;<br />
	/* caseを一個ずつ試す */<br />
	for (cp = n-&gt;ncase.cases ; cp &amp;&amp; evalskip == 0 ; cp = cp-&gt;nclist.next) {<br />
		/* パターンは複数持てるのかな？あまりcaseを使わないからよく分からない。 */<br />
		for (patp = cp-&gt;nclist.pattern ; patp ; patp = patp-&gt;narg.next) {<br />
			/* マッチしたら中身を実行 */<br />
			if (casematch(patp, arglist.list-&gt;text)) {<br />
				if (evalskip == 0) {<br />
					evaltree(cp-&gt;nclist.body, flags);<br />
				}<br />
				/* シェルのcase文は下に突き抜けないので素直に出る。*/<br />
				goto out;<br />
			}<br />
		}<br />
	}<br />
out:<br />
	popstackmark(&amp;smark);<br />
}<br />
<br />
<br />
<br />
/*<br />
 * Kick off a subshell to evaluate a tree.<br />
 */<br />
<br />
/* サブシェルで処理すべき部分の評価 */<br />
STATIC void<br />
evalsubshell(union node *n, int flags)<br />
{<br />
	/* ジョブ */<br />
	struct job *jp;<br />
	/* バックグラウンド起動かどうか */<br />
	int backgnd = (n-&gt;type == NBACKGND);<br />
	int status;<br />
<br />
	/* ここら辺は今のセンスだと関数に括り出してほしいなあ */<br />
	errlinno = lineno = n-&gt;nredir.linno;<br />
	if (funcline)<br />
		lineno -= funcline - 1;<br />
<br />
	/* リダイレクトの処理 */<br />
	expredir(n-&gt;nredir.redirect);<br />
	/* バックグラウンドでない、-eがセットされている、トラップがない<br />
 	* というよく分からん条件のときはフォークしない */<br />
	if (!backgnd &amp;&amp; flags &amp; EV_EXIT &amp;&amp; !have_traps())<br />
		goto nofork;<br />
	/* 割り込み受け付けない区間 */<br />
	INTOFF;<br />
	/* ジョブ作り。jobs.cで実装。 */<br />
	jp = makejob(n, 1);<br />
	/* サブシェルプロセスをフォーク */<br />
	if (forkshell(jp, n, backgnd) == 0) {<br />
		/* これは子供（サブシェル内）での処理 */<br />
<br />
		INTON; /* 割り込み受け付け */<br />
		/* ここらへんの終了条件の理解についてはサボります・・・*/<br />
		flags |= EV_EXIT;<br />
		if (backgnd)<br />
			flags &amp;=~ EV_TESTED;<br />
nofork:<br />
		/* リダイレクト処理してexec。戻ってこない */<br />
		redirect(n-&gt;nredir.redirect, 0);<br />
		evaltreenr(n-&gt;nredir.n, flags);<br />
		/* never returns */<br />
	}<br />
	/* ここはfork元（親シェル）の処理 */<br />
	status = 0;<br />
	/* バックグラウンド起動でなければジョブ待ち */<br />
	if (! backgnd)<br />
		status = waitforjob(jp);<br />
	exitstatus = status;<br />
	INTON;<br />
	/* 割り込み受け付けない区間おわり */<br />
}<br />
<br />
<br />
<br />
/*<br />
 * Compute the names of the files in a redirection list.<br />
 */<br />
<br />
/* リダイレクト先やリダイレクト元のパス等を解決して<br />
 * ノードの中の変数に書き込む。*/<br />
STATIC void<br />
expredir(union node *n)<br />
{<br />
	union node *redir;<br />
<br />
	/* 入力元やら出力先やら、複数のファイルをさばくわけです。たぶん。 */<br />
	for (redir = n ; redir ; redir = redir-&gt;nfile.next) {<br />
		struct arglist fn;<br />
		fn.lastp = &amp;fn.list;<br />
		switch (redir-&gt;type) {<br />
		case NFROMTO:<br />
		case NFROM:<br />
		case NTO:<br />
		case NCLOBBER:<br />
		case NAPPEND:<br />
			/* 要はファイルの場合 */<br />
			expandarg(redir-&gt;nfile.fname, &amp;fn, EXP_TILDE | EXP_REDIR);<br />
			redir-&gt;nfile.expfname = fn.list-&gt;text;<br />
			break;<br />
		case NFROMFD:<br />
		case NTOFD:<br />
			/* 要はファイル記述子の場合 */<br />
			if (redir-&gt;ndup.vname) {<br />
				expandarg(redir-&gt;ndup.vname, &amp;fn, EXP_FULL | EXP_TILDE);<br />
				/* parser.cで定義されている。<br />
				* ノードにファイル記述子の情報を書く。*/<br />
				fixredir(redir, fn.list-&gt;text, 1);<br />
			}<br />
			break;<br />
		}<br />
	}<br />
}<br />
<br />
<br />
<br />
/*<br />
 * Evaluate a pipeline. All the processes in the pipeline are children<br />
 * of the process creating the pipeline. (This differs from some versions<br />
 * of the shell, which make the last process in a pipeline the parent<br />
 * of all the rest.)<br />
 */<br />
<br />
/* 個人的に非常に興味があるが同時に非常にややこしいパイプの処理 */<br />
STATIC void<br />
evalpipe(union node *n, int flags)<br />
{<br />
	struct job *jp;<br />
	struct nodelist *lp;<br />
	/* パイプの長さ=コマンドの数 */<br />
	int pipelen;<br />
	int prevfd;<br />
	/* ピップエレキバン。ではなくてパイプのファイル記述子が入る。*/<br />
	int pip[2];<br />
<br />
	TRACE((&quot;evalpipe(0x%lx) called\\n&quot;, (long)n));<br />
	pipelen = 0;<br />
	/* 数えます*/<br />
	for (lp = n-&gt;npipe.cmdlist ; lp ; lp = lp-&gt;next)<br />
		pipelen++;<br />
	/* これはおそらくパイプ途中のコマンドが死んだらアボートさせる処理。<br />
 	* ただ、コマンド途中のコマンドは-eで止めることができないのとどういう関係が<br />
 	* あるのか、正直なところよく分からない。 */<br />
	flags |= EV_EXIT;<br />
	/* パイプ接続中は割り込みを受け付けない */<br />
	INTOFF;<br />
	/* なぜpipelenを渡すのかは、jobs.cを見ないとわからんか。*/<br />
	jp = makejob(n, pipelen);<br />
	prevfd = -1;<br />
	/* コマンドがつながっているだけ繰り返し */<br />
	for (lp = n-&gt;npipe.cmdlist ; lp ; lp = lp-&gt;next) {<br />
		/* パスの解決や関数のルックアップ処理 */<br />
		prehash(lp-&gt;n);<br />
		pip[1] = -1;<br />
		if (lp-&gt;next) {<br />
			/* ここで次のコマンドと接続するためのパイプを作る*/<br />
			/* pipeができんかったらエラー */<br />
			if (pipe(pip) &lt; 0) {<br />
				close(prevfd);<br />
				sh_error(&quot;Pipe call failed&quot;);<br />
			}<br />
		}<br />
 /*<br />
 * --&gt; prevfd &lt;-- pip[0]<br />
 * 親 |<br />
 * --- pip[1]<br />
 * */<br />
 <br />
		/* 今扱っているコマンドのためのフォーク */<br />
		if (forkshell(jp, lp-&gt;n, n-&gt;npipe.backgnd) == 0) {<br />
			/* 子プロセスの方 */<br />
 /*<br />
 * --&gt; prevfd pip[0] &lt;-----&gt; pip[0] &lt;-- prevfd<br />
 * 子 | 親<br />
 * pip[1] ------- pip[1]<br />
 * 			*/<br />
<br />
			/* 割り込み許可 */<br />
			INTON;<br />
			/* 書き出し用があったら読み込み用を閉じる */<br />
			if (pip[1] &gt;= 0) {<br />
				close(pip[0]);<br />
			}<br />
			/*<br />
 * --&gt; prevfd ---&gt; pip[0] &lt;-- prevfd<br />
 * 子 | 親<br />
 * pip[1] ------- pip[1]<br />
 * */<br />
<br />
			if (prevfd &gt; 0) {<br />
				dup2(prevfd, 0);<br />
				close(prevfd);<br />
			}<br />
			/*<br />
 * --&gt; 0 ---&gt; pip[0] &lt;-- prevfd<br />
 * 子 | 親<br />
 * pip[1] ------- pip[1]<br />
 * 			*/<br />
<br />
			/* 書き出しを標準出力に移す */<br />
			if (pip[1] &gt; 1) {<br />
				dup2(pip[1], 1);<br />
				close(pip[1]);<br />
			}<br />
			/*<br />
 * --&gt; 0 ---&gt; pip[0] &lt;-- prevfd<br />
 * 子 | 親<br />
 * 1 ------- pip[1]<br />
 * 			*/<br />
<br />
			evaltreenr(lp-&gt;n, flags);<br />
			/* never returns */<br />
		}<br />
		/* 親の処理 */<br />
		if (prevfd &gt;= 0)<br />
			close(prevfd);<br />
		/*<br />
 * --&gt; 0 ---&gt; pip[0] <br />
 * 子 | 親<br />
 * 1 ------- pip[1]<br />
 * 		*/<br />
<br />
		prevfd = pip[0];<br />
		/*<br />
 * (prevfd)<br />
 * --&gt; 0 ---&gt; pip[0] <br />
 * 子 | 親<br />
 * 1 ------- pip[1]<br />
 * 		*/<br />
<br />
		/* 親は書き込みの方を閉じる */<br />
		close(pip[1]);<br />
		/*<br />
 * (prevfd)<br />
 * --&gt; 0 ---&gt; pip[0] <br />
 * 子 | 親<br />
 * 1 ----<br />
 * 		*/<br />
	}<br />
	/* バックグラウンドでなければパイプラインの処理を待つ */<br />
	if (n-&gt;npipe.backgnd == 0) {<br />
		exitstatus = waitforjob(jp);<br />
		TRACE((&quot;evalpipe: job done exit status %d\\n&quot;, exitstatus));<br />
	}<br />
	INTON;<br />
}<br />
<br />
<br />
<br />
/*<br />
 * Execute a command inside back quotes. If it's a builtin command, we<br />
 * want to save its output in a block obtained from malloc. Otherwise<br />
 * we fork off a subprocess and get the output of the command via a pipe.<br />
 * Should be called with interrupts off.<br />
 */<br />
<br />
/* バッククォート、$( )内のコマンドの実行。<br />
 * 上には内部コマンドのときは出力をバッファ貯め、<br />
 * そうでなければ標準出力に出す（want toということだから<br />
 * そうでないかもしれない）とあるが、<br />
 * 下の処理では何があってもforkしているように見える。<br />
 * forkshellを読まないとなんとも言えない。*/<br />
void<br />
evalbackcmd(union node *n, struct backcmd *result)<br />
{<br />
	int pip[2];<br />
	struct job *jp;<br />
<br />
	result-&gt;fd = -1;<br />
	result-&gt;buf = NULL;<br />
	result-&gt;nleft = 0;<br />
	result-&gt;jp = NULL;<br />
	if (n == NULL) {<br />
		goto out;<br />
	}<br />
<br />
	/* 内部コマンドでもパイプは開くらしい。*/<br />
	if (pipe(pip) &lt; 0)<br />
		sh_error(&quot;Pipe call failed&quot;);<br />
	jp = makejob(n, 1);<br />
	/* FORK_NOJOBはjobs.cで取り扱われる*/<br />
	if (forkshell(jp, n, FORK_NOJOB) == 0) {<br />
		/* 子プロセス */<br />
		/* パイプ接続の流れはevalpipeを参照のこと */<br />
<br />
		FORCEINTON;<br />
		/* 親からの入力口を閉じる */<br />
		close(pip[0]);<br />
		/* 書き込み先を子プロセスの標準出力につなぐ */<br />
		if (pip[1] != 1) {<br />
			dup2(pip[1], 1);<br />
			close(pip[1]);<br />
		}<br />
		ifsfree();<br />
		evaltreenr(n, EV_EXIT);<br />
		/* NOTREACHED */<br />
	}<br />
	/* 子につながっている出力先を閉じる */<br />
	close(pip[1]);<br />
	/* 子からの受け入れ口をresultに入れる */<br />
	result-&gt;fd = pip[0];<br />
	result-&gt;jp = jp;<br />
<br />
out:<br />
	TRACE((&quot;evalbackcmd done: fd=%d buf=0x%x nleft=%d jp=0x%x\\n&quot;,<br />
		result-&gt;fd, result-&gt;buf, result-&gt;nleft, result-&gt;jp));<br />
}<br />
<br />
static char **<br />
parse_command_args(char **argv, const char **path)<br />
{<br />
	char *cp, c;<br />
<br />
	for (;;) {<br />
		cp = *++argv;<br />
		if (!cp)<br />
			return 0;<br />
		if (*cp++ != '-')<br />
			break;<br />
		if (!(c = *cp++))<br />
			break;<br />
		if (c == '-' &amp;&amp; !*cp) {<br />
			if (!*++argv)<br />
				return 0;<br />
			break;<br />
		}<br />
		do {<br />
			switch (c) {<br />
			case 'p':<br />
				*path = defpath;<br />
				break;<br />
			default:<br />
				/* run 'typecmd' for other options */<br />
				return 0;<br />
			}<br />
		} while ((c = *cp++));<br />
	}<br />
	return argv;<br />
}<br />
<br />
<br />
<br />
/*<br />
 * Execute a simple command.<br />
 */<br />
<br />
STATIC void<br />
#ifdef notyet<br />
evalcommand(union node *cmd, int flags, struct backcmd *backcmd)<br />
#else<br />
evalcommand(union node *cmd, int flags)<br />
#endif<br />
{<br />
	struct localvar_list *localvar_stop;<br />
	struct redirtab *redir_stop;<br />
	struct stackmark smark;<br />
	union node *argp;<br />
	struct arglist arglist;<br />
	struct arglist varlist;<br />
	char **argv;<br />
	int argc;<br />
	struct strlist *sp;<br />
#ifdef notyet<br />
	int pip[2];<br />
#endif<br />
	struct cmdentry cmdentry;<br />
	struct job *jp;<br />
	char *lastarg;<br />
	const char *path;<br />
	int spclbltin;<br />
	int execcmd;<br />
	int status;<br />
	char **nargv;<br />
<br />
	errlinno = lineno = cmd-&gt;ncmd.linno;<br />
	if (funcline)<br />
		lineno -= funcline - 1;<br />
<br />
	/* First expand the arguments. */<br />
	TRACE((&quot;evalcommand(0x%lx, %d) called\\n&quot;, (long)cmd, flags));<br />
	setstackmark(&amp;smark);<br />
	localvar_stop = pushlocalvars();<br />
	back_exitstatus = 0;<br />
<br />
	cmdentry.cmdtype = CMDBUILTIN;<br />
	cmdentry.u.cmd = &amp;bltin;<br />
	varlist.lastp = &amp;varlist.list;<br />
	*varlist.lastp = NULL;<br />
	arglist.lastp = &amp;arglist.list;<br />
	*arglist.lastp = NULL;<br />
<br />
	argc = 0;<br />
	for (argp = cmd-&gt;ncmd.args; argp; argp = argp-&gt;narg.next) {<br />
		struct strlist **spp;<br />
<br />
		spp = arglist.lastp;<br />
		expandarg(argp, &amp;arglist, EXP_FULL | EXP_TILDE);<br />
		for (sp = *spp; sp; sp = sp-&gt;next)<br />
			argc++;<br />
	}<br />
<br />
	/* Reserve one extra spot at the front for shellexec. */<br />
	nargv = stalloc(sizeof (char *) * (argc + 2));<br />
	argv = ++nargv;<br />
	for (sp = arglist.list ; sp ; sp = sp-&gt;next) {<br />
		TRACE((&quot;evalcommand arg: %s\\n&quot;, sp-&gt;text));<br />
		*nargv++ = sp-&gt;text;<br />
	}<br />
	*nargv = NULL;<br />
<br />
	lastarg = NULL;<br />
	if (iflag &amp;&amp; funcline == 0 &amp;&amp; argc &gt; 0)<br />
		lastarg = nargv[-1];<br />
<br />
	preverrout.fd = 2;<br />
	expredir(cmd-&gt;ncmd.redirect);<br />
	redir_stop = pushredir(cmd-&gt;ncmd.redirect);<br />
	status = redirectsafe(cmd-&gt;ncmd.redirect, REDIR_PUSH|REDIR_SAVEFD2);<br />
<br />
	path = vpath.text;<br />
	for (argp = cmd-&gt;ncmd.assign; argp; argp = argp-&gt;narg.next) {<br />
		struct strlist **spp;<br />
		char *p;<br />
<br />
		spp = varlist.lastp;<br />
		expandarg(argp, &amp;varlist, EXP_VARTILDE);<br />
<br />
		mklocal((*spp)-&gt;text);<br />
<br />
		/*<br />
		* Modify the command lookup path, if a PATH= assignment<br />
		* is present<br />
		*/<br />
		p = (*spp)-&gt;text;<br />
		if (varequal(p, path))<br />
			path = p;<br />
	}<br />
<br />
	/* Print the command if xflag is set. */<br />
	if (xflag) {<br />
		struct output *out;<br />
		int sep;<br />
<br />
		out = &amp;preverrout;<br />
		outstr(expandstr(ps4val()), out);<br />
		sep = 0;<br />
		sep = eprintlist(out, varlist.list, sep);<br />
		eprintlist(out, arglist.list, sep);<br />
		outcslow('\\n', out);<br />
#ifdef FLUSHERR<br />
		flushout(out);<br />
#endif<br />
	}<br />
<br />
	execcmd = 0;<br />
	spclbltin = -1;<br />
<br />
	/* Now locate the command. */<br />
	if (argc) {<br />
		const char *oldpath;<br />
		int cmd_flag = DO_ERR;<br />
<br />
		path += 5;<br />
		oldpath = path;<br />
		for (;;) {<br />
			find_command(argv[0], &amp;cmdentry, cmd_flag, path);<br />
			if (cmdentry.cmdtype == CMDUNKNOWN) {<br />
				status = 127;<br />
#ifdef FLUSHERR<br />
				flushout(&amp;errout);<br />
#endif<br />
				goto bail;<br />
			}<br />
<br />
			/* implement bltin and command here */<br />
			if (cmdentry.cmdtype != CMDBUILTIN)<br />
				break;<br />
			if (spclbltin &lt; 0)<br />
				spclbltin = <br />
					cmdentry.u.cmd-&gt;flags &amp;<br />
					BUILTIN_SPECIAL<br />
				;<br />
			if (cmdentry.u.cmd == EXECCMD)<br />
				execcmd++;<br />
			if (cmdentry.u.cmd != COMMANDCMD)<br />
				break;<br />
<br />
			path = oldpath;<br />
			nargv = parse_command_args(argv, &amp;path);<br />
			if (!nargv)<br />
				break;<br />
			argc -= nargv - argv;<br />
			argv = nargv;<br />
			cmd_flag |= DO_NOFUNC;<br />
		}<br />
	}<br />
<br />
	if (status) {<br />
bail:<br />
		exitstatus = status;<br />
<br />
		/* We have a redirection error. */<br />
		if (spclbltin &gt; 0)<br />
			exraise(EXERROR);<br />
<br />
		goto out;<br />
	}<br />
<br />
	/* Execute the command. */<br />
	switch (cmdentry.cmdtype) {<br />
	default:<br />
		/* Fork off a child process if necessary. */<br />
		if (!(flags &amp; EV_EXIT) || have_traps()) {<br />
			INTOFF;<br />
			jp = makejob(cmd, 1);<br />
			if (forkshell(jp, cmd, FORK_FG) != 0) {<br />
				exitstatus = waitforjob(jp);<br />
				INTON;<br />
				break;<br />
			}<br />
			FORCEINTON;<br />
		}<br />
		listsetvar(varlist.list, VEXPORT|VSTACK);<br />
		shellexec(argv, path, cmdentry.u.index);<br />
		/* NOTREACHED */<br />
<br />
	case CMDBUILTIN:<br />
		if (spclbltin &gt; 0 || argc == 0) {<br />
			poplocalvars(1);<br />
			if (execcmd &amp;&amp; argc &gt; 1)<br />
				listsetvar(varlist.list, VEXPORT);<br />
		}<br />
		if (evalbltin(cmdentry.u.cmd, argc, argv, flags)) {<br />
			int status;<br />
			int i;<br />
<br />
			i = exception;<br />
			if (i == EXEXIT)<br />
				goto raise;<br />
<br />
			status = (i == EXINT) ? SIGINT + 128 : 2;<br />
			exitstatus = status;<br />
<br />
			if (i == EXINT || spclbltin &gt; 0) {<br />
raise:<br />
				longjmp(handler-&gt;loc, 1);<br />
			}<br />
			FORCEINTON;<br />
		}<br />
		break;<br />
<br />
	case CMDFUNCTION:<br />
		poplocalvars(1);<br />
		if (evalfun(cmdentry.u.func, argc, argv, flags))<br />
			goto raise;<br />
		break;<br />
	}<br />
<br />
out:<br />
	if (cmd-&gt;ncmd.redirect)<br />
		popredir(execcmd);<br />
	unwindredir(redir_stop);<br />
	unwindlocalvars(localvar_stop);<br />
	if (lastarg)<br />
		/* dsl: I think this is intended to be used to support<br />
		* '_' in 'vi' command mode during line editing...<br />
		* However I implemented that within libedit itself.<br />
		*/<br />
		setvar(&quot;_&quot;, lastarg, 0);<br />
	popstackmark(&amp;smark);<br />
}<br />
<br />
/* evalcommandでだけ使われている */<br />
STATIC int<br />
evalbltin(const struct builtincmd *cmd, int argc, char **argv, int flags)<br />
{<br />
	char *volatile savecmdname;<br />
	struct jmploc *volatile savehandler;<br />
	struct jmploc jmploc;<br />
	int status;<br />
	int i;<br />
<br />
	savecmdname = commandname;<br />
	savehandler = handler;<br />
	if ((i = setjmp(jmploc.loc)))<br />
		goto cmddone;<br />
	handler = &amp;jmploc;<br />
	commandname = argv[0];<br />
	argptr = argv + 1;<br />
	optptr = NULL;			/* initialize nextopt */<br />
	if (cmd == EVALCMD)<br />
		status = evalcmd(argc, argv, flags);<br />
	else<br />
		status = (*cmd-&gt;builtin)(argc, argv);<br />
	flushall();<br />
	status |= outerr(out1);<br />
	exitstatus = status;<br />
cmddone:<br />
	freestdout();<br />
	commandname = savecmdname;<br />
	handler = savehandler;<br />
<br />
	return i;<br />
}<br />
<br />
STATIC int<br />
evalfun(struct funcnode *func, int argc, char **argv, int flags)<br />
{<br />
	volatile struct shparam saveparam;<br />
	struct jmploc *volatile savehandler;<br />
	struct jmploc jmploc;<br />
	int e;<br />
	int savefuncline;<br />
<br />
	saveparam = shellparam;<br />
	savefuncline = funcline;<br />
	savehandler = handler;<br />
	if ((e = setjmp(jmploc.loc))) {<br />
		goto funcdone;<br />
	}<br />
	INTOFF;<br />
	handler = &amp;jmploc;<br />
	shellparam.malloc = 0;<br />
	func-&gt;count++;<br />
	funcline = func-&gt;n.ndefun.linno;<br />
	INTON;<br />
	shellparam.nparam = argc - 1;<br />
	shellparam.p = argv + 1;<br />
	shellparam.optind = 1;<br />
	shellparam.optoff = -1;<br />
	pushlocalvars();<br />
	evaltree(func-&gt;n.ndefun.body, flags &amp; EV_TESTED);<br />
	poplocalvars(0);<br />
funcdone:<br />
	INTOFF;<br />
	funcline = savefuncline;<br />
	freefunc(func);<br />
	freeparam(&amp;shellparam);<br />
	shellparam = saveparam;<br />
	handler = savehandler;<br />
	INTON;<br />
	evalskip &amp;= ~SKIPFUNC;<br />
	return e;<br />
}<br />
<br />
<br />
/*<br />
 * Search for a command. This is called before we fork so that the<br />
 * location of the command will be available in the parent as well as<br />
 * the child. The check for &quot;goodname&quot; is an overly conservative<br />
 * check that the name will not be subject to expansion.<br />
 */<br />
<br />
STATIC void<br />
prehash(union node *n)<br />
{<br />
	struct cmdentry entry;<br />
<br />
	if (n-&gt;type == NCMD &amp;&amp; n-&gt;ncmd.args)<br />
		if (goodname(n-&gt;ncmd.args-&gt;narg.text))<br />
			find_command(n-&gt;ncmd.args-&gt;narg.text, &amp;entry, 0,<br />
				pathval());<br />
}<br />
<br />
<br />
<br />
/*<br />
 * Builtin commands. Builtin commands whose functions are closely<br />
 * tied to evaluation are implemented here.<br />
 */<br />
<br />
/*<br />
 * No command given.<br />
 */<br />
<br />
STATIC int<br />
bltincmd(int argc, char **argv)<br />
{<br />
	/*<br />
	* Preserve exitstatus of a previous possible redirection<br />
	* as POSIX mandates<br />
	*/<br />
	return back_exitstatus;<br />
}<br />
<br />
<br />
/*<br />
 * Handle break and continue commands. Break, continue, and return are<br />
 * all handled by setting the evalskip flag. The evaluation routines<br />
 * above all check this flag, and if it is set they start skipping<br />
 * commands rather than executing them. The variable skipcount is<br />
 * the number of loops to break/continue, or the number of function<br />
 * levels to return. (The latter is always 1.) It should probably<br />
 * be an error to break out of more loops than exist, but it isn't<br />
 * in the standard shell so we don't make it one here.<br />
 */<br />
<br />
int<br />
breakcmd(int argc, char **argv)<br />
{<br />
	int n = argc &gt; 1 ? number(argv[1]) : 1;<br />
<br />
	if (n &lt;= 0)<br />
		badnum(argv[1]);<br />
	if (n &gt; loopnest)<br />
		n = loopnest;<br />
	if (n &gt; 0) {<br />
		evalskip = (**argv == 'c')? SKIPCONT : SKIPBREAK;<br />
		skipcount = n;<br />
	}<br />
	return 0;<br />
}<br />
<br />
<br />
/*<br />
 * The return command.<br />
 */<br />
<br />
int<br />
returncmd(int argc, char **argv)<br />
{<br />
	/*<br />
	* If called outside a function, do what ksh does;<br />
	* skip the rest of the file.<br />
	*/<br />
	evalskip = SKIPFUNC;<br />
	return argv[1] ? number(argv[1]) : exitstatus;<br />
}<br />
<br />
<br />
int<br />
falsecmd(int argc, char **argv)<br />
{<br />
	return 1;<br />
}<br />
<br />
<br />
int<br />
truecmd(int argc, char **argv)<br />
{<br />
	return 0;<br />
}<br />
<br />
<br />
int<br />
execcmd(int argc, char **argv)<br />
{<br />
	if (argc &gt; 1) {<br />
		iflag = 0;		/* exit on error */<br />
		mflag = 0;<br />
		optschanged();<br />
		shellexec(argv + 1, pathval(), 0);<br />
	}<br />
	return 0;<br />
}<br />
<br />
<br />
STATIC int<br />
eprintlist(struct output *out, struct strlist *sp, int sep)<br />
{<br />
	while (sp) {<br />
		const char *p;<br />
<br />
		p = &quot; %s&quot; + (1 - sep);<br />
		sep |= 1;<br />
		outfmt(out, p, sp-&gt;text);<br />
		sp = sp-&gt;next;<br />
	}<br />
<br />
	return sep;<br />
}<br />
[/c]
