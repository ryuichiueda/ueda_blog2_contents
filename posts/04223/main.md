---
Copyright: (C) Ryuichi Ueda
---


# dash/src/main.h, main.c
dashのmain.hとmain.cに自分のツッコミコメントを入れたもの。gotoやらロングジャンプやら。

「dash精読sh行」の一環です。いちお、シェルの研究関連の意味ある活動で、何かの原理主義ではございません。。

<a href="http://blog.ueda.asia/?page_id=4219" title="dashのコード解読メモ">「dashのコード解読メモ」に戻る</a>

20141104追記: <a href="http://blog.bsdhack.org/" target="_blank">\@bsdhack氏</a>からコメントのコメントをいただきましたので書き入れてます。

<h2>main.h</h2>

```c
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
 *	\@(#)main.h	8.2 (Berkeley) 5/4/95
 */

#include &lt;errno.h&gt;

/* pid of main shell */
extern int rootpid; 
/* ↑メインのシェルのPIDであるが、メインのシェルってサブシェルじゃないっていうことでOKか？ */
/* shell level: 0 for the main shell, 1 for its children, and so on */
extern int shlvl; 
/* ↑この数字で、自分がメインなのか、メインの子なのか孫なのか、
曽孫か玄孫か分かるようにする。シェルはたくさんのプロセスで動くので、
これはシェル初心者には馴染みにくい概念かもしれない。
余計なお世話だが。*/
#define rootshell (!shlvl) 
/* ↑ rootshellなのかどうかは、shlvlを反転すると分かる。
ちなみに(!shlvl)は、shlvlが1以上のときは0（偽）、
そうでないときは1（真）になる。
ちなみにC言語の真偽とシェルの真偽は逆なので、
頭の悪い私がコードを読むときは、
真偽をフィーリングで読んでしまう。*/

#ifdef __GLIBC__
/* glibc sucks */
extern int *dash_errno;
#undef errno
#define errno (*dash_errno)
#endif
/* ↑ glibc sucksというのは、いちばん綺麗な言葉で翻訳すると
「くたばれglibc」である。汚い言葉で訳すと
「glibc ○○○」（書けない）。
ところで私は研究以外ではC言語でガチな仕事をしたことがない
（コマンドを書く程度）ので、
errnoについて詳しくありません。
というか、いつもこういうものを無視してコーディングしているから、
ダメな人間から脱却できません。*/

void readcmdfile(char *);
int dotcmd(int, char **);
int exitcmd(int, char **);
/* ↑内部コマンドに相当する関数には必ず末尾にcmdとついています。
ただ、ちょっと例外がありそうな予感・・・。 */
```


<h2>main.c</h2>
```c
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
 */

#include &lt;stdio.h&gt;
#include &lt;signal.h&gt;
#include &lt;sys/stat.h&gt;
#include &lt;unistd.h&gt;
#include &lt;fcntl.h&gt;

/* ↓こいつらを一通り読まないと全貌が見えないわけです。
ただ言えるのは、bashより量は少ない。 */
#include &quot;shell.h&quot;
#include &quot;main.h&quot;
#include &quot;mail.h&quot;
#include &quot;options.h&quot;
#include &quot;output.h&quot;
#include &quot;parser.h&quot;
#include &quot;nodes.h&quot;
#include &quot;expand.h&quot;
#include &quot;eval.h&quot;
#include &quot;jobs.h&quot;
#include &quot;input.h&quot;
#include &quot;trap.h&quot;
#include &quot;var.h&quot;
#include &quot;show.h&quot;
#include &quot;memalloc.h&quot;
#include &quot;error.h&quot;
#include &quot;init.h&quot;
#include &quot;mystring.h&quot;
#include &quot;exec.h&quot;
#include &quot;cd.h&quot;

#ifdef HETIO
#include &quot;hetio.h&quot;
#endif

#define PROFILE 0

int rootpid;
int shlvl;
#ifdef __GLIBC__
int *dash_errno;
#endif
#if PROFILE
short profile_buf[16384];
extern int etext();
#endif

STATIC void read_profile(const char *);
STATIC char *find_dot_file(char *);
static int cmdloop(int);
int main(int, char **);

/*
 * Main routine. We initialize things, parse the arguments, execute
 * profiles if we're a login shell, and then call cmdloop to execute
 * commands. The setjmp call sets up the location to jump to when an
 * exception occurs. When an exception occurs the variable &quot;state&quot;
 * is used to figure out how far we had gotten.
 */

/* main関数はややこしいのですが、大半はインタラクティブに使うときの設定で、
シェルスクリプトを読む場合の処理はあまり複雑でないような気がします。
ただ、シグナルがいつくるかわからんとか、そういう不確定要素があるので
順に読んで行っても一筋縄ではいかないようで。 */

int
main(int argc, char **argv)
{
	char *shinit;
	volatile int state;
/* ↑シグナル等で別のスレッドが書き換えそうな変数にはvolatileをつけないといけません。
最適化されてコードが変わってしまうとフラグの役割を果たさなくなるからです。
（などと偉そうに言っているが、最近のコンパイラでもそうなのだろうか？） */
	struct jmploc jmploc;
/* ↑ error.hにいます。ジャンプに使います。ジャンプというのは集英社じゃなくて
C言語の何かなので、わからん人は集英社にお問い合わせしないでください。
私も使ったことがないので分かりませんので聞かないでください。
っていうかジャンプがないと実装できないのか。本当にそうなのか・・・。 */
	struct stackmark smark;
/* ↑コマンドが実行されるときにスタックにプッシュしたりポップしたりするものなのですが、
実際にどう動作してどう機能しているかはまだ私には分かってません。*/
	int login;
/* ↑おそらくログインしているかどうかを判断するフラグ */

#ifdef __GLIBC__
	dash_errno = __errno_location();
#endif
/* ↑glibcがあったらerrnoの前処理をするみたいです。suckだそうです。*/

#if PROFILE
	monitor(4, etext, profile_buf, sizeof profile_buf, 50);
#endif
	state = 0;
	if (unlikely(setjmp(jmploc.loc))) {
/* ↑unlikelyはlikelyと共にShell.hに定義されています。
現在のところフィーリングで理解（つまり理解していない）。
longjmp（飛び降り自殺に近い行為）すると、ここに戻ってきます。
今のところ、setjmpできなかったらこのif文の中身が実行されると解釈。

\@bsdhack氏からコメント:
「setjmp()できなかったら」ではなく「longjump() から飛んできたら」
*/
		int e;
		int s;

		reset();
/* ↑reset関数はinit.cで定義されています。たぶん、
このループにいるときはこれまでの処理がなかったかのように
シェルの機能をユーザに提供する段階なので、
resetが呼ばれているものと。しっかし、関数がどこで定義されているか
ちゃんと調べなければいけないのでC言語大変・・・*/

		e = exception;
/* ↑どこかから妖精のように舞い降りたexception（未調査） */

/* ↓mainは状態（state）で自由奔放にgotoするので死にたい。*/
		s = state;
/* ↓例外がEXITあるいは、状態が0あるいは、
-iが指定されていないあるいは、レベルが1以上なら終わる。*/
		if (e == EXEXIT || s == 0 || iflag == 0 || shlvl)
			exitshell();

/* ↓ATTYなんすか？？なんのことですか？端末か何かですか？*/
		if (e == EXINT
#if ATTY
		&amp;&amp; (! attyset() || equal(termval(), &quot;emacs&quot;))
#endif
		) {
			out2c('\\n');
#ifdef FLUSHERR
			flushout(out2);
#endif
		}
/* ↑とりあえずCtrl+c押されたらバッファに溜まった何かを出すということは理解。
ただし、この解釈は間違っている可能性が大いにあり。 */

		popstackmark(&amp;smark);
/* ↑どこかでpushされているらしい */
		FORCEINTON;				/* enable interrupts */
/* ↑割り込み許可。 */

/* ↓goto地獄。割り込みがかかったときの処理の再開に使われているような気がするが、
まだ分からない。 */
		if (s == 1)
			goto state1;
		else if (s == 2)
			goto state2;
		else if (s == 3)
			goto state3;
		else
			goto state4;
	}
	handler = &amp;jmploc;
/* ↑このhandlerは、少なくともmain.cでは使われていません。*/

#ifdef DEBUG
	opentrace();
	trputs(&quot;Shell args: &quot;); trargs(argv);
#endif

/* ここから初期化が続く */
	rootpid = getpid();
	init();
/* ↓ここでスタックになにか積まれる。何かが。 */
	setstackmark(&amp;smark);

/* ↓ここら辺はシェルをそこそこ使う人ならなんとなくわかるかと。
つまり、私もなんとなくしかわかってません。*/
	login = procargs(argc, argv);
	if (login) {
		state = 1;
		read_profile(&quot;/etc/profile&quot;);
/*↓こういうところにラベルがあるということは、
やはり初期化が中断されたときにさっきのgotoが使われるということか */
state1:
		state = 2;
		read_profile(&quot;$HOME/.profile&quot;);
	}
state2:
	state = 3;
	if (
/* ↓これはlinuxでないと面倒臭いという解釈でよろしい？iflagは-iつまり、
インタラクティブに使うとき。つまり端末から使うとき。 */
#ifndef linux
		getuid() == geteuid() &amp;&amp; getgid() == getegid() &amp;&amp;
#endif
		iflag
	) {
		if ((shinit = lookupvar(&quot;ENV&quot;)) != NULL &amp;&amp; *shinit != '&#92;&#48;') {
			read_profile(shinit);
		}
	}
/* ↓本当に何に使うんだろう？（というコメントを残しておくと、
あとからわかったときに削除して回らなければいけない予感・・・）*/
	popstackmark(&amp;smark);
state3:
	state = 4;
/* ↓このminuscというのは、「マイナスc」、つまり-cオプションのこと。
-cが指定されているとbash -c &quot;引数&quot;とすると引数に書いたコマンドが実行できる。
そういう場合の話。しかし、イレギュラーなのでmain.cにあるのは邪魔だ。邪魔。*/
	if (minusc)
		evalstring(minusc, sflag ? 0 : EV_EXIT);
/* ↑「-cなら引数をそのまま評価してしまえ。以上。」という感じ */

/* ↓このコメントが泣ける・・・。state4でここに来たときには
フラグを見なくてよいからという解釈でよいような気がする。
cmdloopに入るとしばらく出てこない。cmdloopはこの下に定義されています。*/
	if (sflag || minusc == NULL) {
state4:	/* XXX ??? - why isn't this before the &quot;if&quot; statement */
		cmdloop(1);
	}
#if PROFILE
	monitor(0);
#endif
#if GPROF
/* ↓わけわかめ。ただ、重要そうではない。

\@bsdhack氏: プロファイル用
*/
	{
		extern void _mcleanup(void);
		_mcleanup();
	}
#endif

/* ↓おしまいける！*/
	exitshell();
	/* NOTREACHED */
}


/*
 * Read and execute commands. &quot;Top&quot; is nonzero for the top level command
 * loop; it turns on prompting if the shell is interactive.
 */

/* シェルが立ち上がっている間、こいつがグルグルまわる。
トップのループ（topが1とかそれ以上）でインタラクティブだとプロンプトが出るそうです。 */
static int
cmdloop(int top)
{
/* ↓このnodeというやつにパースしたコマンドやらが入っています。*/
	union node *n;
	struct stackmark smark;
	int inter;
	int status = 0;
	int numeof = 0;

	TRACE((&quot;cmdloop(%d) called\\n&quot;, top));

/* ↓HETIOってなんじゃい。たぶん、-iでトップのときに初期化されるので、
インタラクティブな何か。あんまり興味ない。*/
#ifdef HETIO
	if(iflag &amp;&amp; top)
		hetio_init();
#endif
/* ↓回って回って回って回る。 */
	for (;;) {
		int skip;

		setstackmark(&amp;smark);
		if (jobctl)
			showjobs(out2, SHOW_CHANGED);
		inter = 0;

/* ↓インタラクティブなとき。メールがあるとか教えてくれるアレです。
inter変数は今の所なにに使うか不明。*/
		if (iflag &amp;&amp; top) {
			inter++;
			chkmail();
		}
/* ↓interを指定するとコマンドをパースしてくれるようです。*/
		n = parsecmd(inter);
		/* showtree(n); DEBUG */

/* ↓NEOFはperser.hで定義されており、スクリプトの読み終わりに相当。
dashはスクリプトを全部読み込まずに、スクリプトを読みながら処理するので、
NEOFにぶつかるということは処理が全部終わったということに相当。
インタラクティブならプロンプトを出して待つことになる。 */
		if (n == NEOF) {
			if (!top || numeof &gt;= 50)
				break;
			if (!stoppedjobs()) {
/*↓ Iflagは-I（インタラクティブなときにEOFを無視する）に対応。 */
				if (!Iflag)
					break;
				out2str(&quot;\\nUse \\&quot;exit\\&quot; to leave shell.\\n&quot;);
			}
			numeof++;
		} else if (nflag == 0) {
/* ↑nflag（-n）は、「何もしない」。つまりドライランを指定するオプション。
つまりnflag == 0で、「ドライランではない、実行する」という意味になる。 */
			job_warning = (job_warning == 2) ? 1 : 0;
			numeof = 0;
/* ↓実行して終了ステータスをstatusに代入。 */
			evaltree(n, 0);
			status = exitstatus;
		}
		popstackmark(&amp;smark);

/* ↓このevalskipはbreakやreturn、continueのとき等に設定される。
skipのフラグが立っていれば無限ループを出て下のreturn statusでこの関数が終わる。*/
		skip = evalskip;
		if (skip) {
			evalskip &amp;= ~SKIPFUNC;
			break;
		}
	}

	return status;
}

/* ↓ここから下は設定ファイルを読むところ。設定ファイルといっても
シェルスクリプトなので、普通の処理とだいたい同じ手順。 */

/*
 * Read /etc/profile or .profile. Return on error.
 */

STATIC void
read_profile(const char *name)
{
	name = expandstr(name);
/* ↓このsetinputfileに入れたファイルがシェルスクリプトとして解釈されるらしい。 */
	if (setinputfile(name, INPUT_PUSH_FILE | INPUT_NOFILE_OK) &lt; 0)
		return;
/* ↓トップでないループ処理に入って設定ファイルを解釈。 */
	cmdloop(0);
	popfile();
}



/*
 * Read a file containing shell functions.
 */

/* ↓「.」コマンドの横に指定したファイルから関数を読み出す処理。 */

void
readcmdfile(char *name)
{
	setinputfile(name, INPUT_PUSH_FILE);
	cmdloop(0);
	popfile();
}



/*
 * Take commands from a file. To be compatible we should do a path
 * search for the file, which is necessary to find sub-commands.
 */

/* ↓「.」コマンドの横に指定したファイルを見つける処理。
パスの探索はかなり処理が面倒臭く、関数が長めになっています。 */

STATIC char *
find_dot_file(char *basename)
{
	char *fullname;
	const char *path = pathval();
	struct stat statb;

	/* don't try this for absolute or relative paths */
	if (strchr(basename, '/'))
		return basename;

	while ((fullname = padvance(&amp;path, basename)) != NULL) {
		if ((stat(fullname, &amp;statb) == 0) &amp;&amp; S_ISREG(statb.st_mode)) {
			/*
			* Don't bother freeing here, since it will
			* be freed by the caller.
			*/
			return fullname;
		}
		stunalloc(fullname);
	}

	/* not found in the PATH */
	sh_error(&quot;%s: not found&quot;, basename);
	/* NOTREACHED */
}

/* ↓ 「.」コマンドの実装。わたしゃ滅多に使いません。*/

int
dotcmd(int argc, char **argv)
{
	int status = 0;

	if (argc &gt;= 2) {		/* That's what SVR2 does */
		char *fullname;

		fullname = find_dot_file(argv[1]);
		setinputfile(fullname, INPUT_PUSH_FILE);
		commandname = fullname;
		status = cmdloop(0);
		popfile();
	}
	return status;
}

/*↓これはexitコマンドの実装。こちらは.と違ってよく使います。
オプションに指定された終了ステータスを処理して例外を送ってます。
「例外はがんばって実装したよ」とTOURファイルに書いてありました。
C++を使いたいところ。大半の人はそう思わないだろうが。 */

int
exitcmd(int argc, char **argv)
{
	if (stoppedjobs())
		return 0;
	if (argc &gt; 1)
		exitstatus = number(argv[1]);
	exraise(EXEXIT);
	/* NOTREACHED */
}

```
