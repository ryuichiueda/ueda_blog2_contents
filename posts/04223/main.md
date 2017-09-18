---
Copyright: (C) Ryuichi Ueda
---

# dash/src/main.h, main.c
dashのmain.hとmain.cに自分のツッコミコメントを入れたもの。gotoやらロングジャンプやら。<br />
<br />
「dash精読sh行」の一環です。いちお、シェルの研究関連の意味ある活動で、何かの原理主義ではございません。。<br />
<br />
<a href="http://blog.ueda.asia/?page_id=4219" title="dashのコード解読メモ">「dashのコード解読メモ」に戻る</a><br />
<br />
20141104追記: <a href="http://blog.bsdhack.org/" target="_blank">\@bsdhack氏</a>からコメントのコメントをいただきましたので書き入れてます。<br />
<br />
<h2>main.h</h2><br />
<br />
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
 *	\@(#)main.h	8.2 (Berkeley) 5/4/95<br />
 */<br />
<br />
#include &lt;errno.h&gt;<br />
<br />
/* pid of main shell */<br />
extern int rootpid; <br />
/* ↑メインのシェルのPIDであるが、メインのシェルってサブシェルじゃないっていうことでOKか？ */<br />
/* shell level: 0 for the main shell, 1 for its children, and so on */<br />
extern int shlvl; <br />
/* ↑この数字で、自分がメインなのか、メインの子なのか孫なのか、<br />
曽孫か玄孫か分かるようにする。シェルはたくさんのプロセスで動くので、<br />
これはシェル初心者には馴染みにくい概念かもしれない。<br />
余計なお世話だが。*/<br />
#define rootshell (!shlvl) <br />
/* ↑ rootshellなのかどうかは、shlvlを反転すると分かる。<br />
ちなみに(!shlvl)は、shlvlが1以上のときは0（偽）、<br />
そうでないときは1（真）になる。<br />
ちなみにC言語の真偽とシェルの真偽は逆なので、<br />
頭の悪い私がコードを読むときは、<br />
真偽をフィーリングで読んでしまう。*/<br />
<br />
#ifdef __GLIBC__<br />
/* glibc sucks */<br />
extern int *dash_errno;<br />
#undef errno<br />
#define errno (*dash_errno)<br />
#endif<br />
/* ↑ glibc sucksというのは、いちばん綺麗な言葉で翻訳すると<br />
「くたばれglibc」である。汚い言葉で訳すと<br />
「glibc ○○○」（書けない）。<br />
ところで私は研究以外ではC言語でガチな仕事をしたことがない<br />
（コマンドを書く程度）ので、<br />
errnoについて詳しくありません。<br />
というか、いつもこういうものを無視してコーディングしているから、<br />
ダメな人間から脱却できません。*/<br />
<br />
void readcmdfile(char *);<br />
int dotcmd(int, char **);<br />
int exitcmd(int, char **);<br />
/* ↑内部コマンドに相当する関数には必ず末尾にcmdとついています。<br />
ただ、ちょっと例外がありそうな予感・・・。 */<br />
[/c]<br />
<br />
<br />
<h2>main.c</h2><br />
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
 */<br />
<br />
#include &lt;stdio.h&gt;<br />
#include &lt;signal.h&gt;<br />
#include &lt;sys/stat.h&gt;<br />
#include &lt;unistd.h&gt;<br />
#include &lt;fcntl.h&gt;<br />
<br />
/* ↓こいつらを一通り読まないと全貌が見えないわけです。<br />
ただ言えるのは、bashより量は少ない。 */<br />
#include &quot;shell.h&quot;<br />
#include &quot;main.h&quot;<br />
#include &quot;mail.h&quot;<br />
#include &quot;options.h&quot;<br />
#include &quot;output.h&quot;<br />
#include &quot;parser.h&quot;<br />
#include &quot;nodes.h&quot;<br />
#include &quot;expand.h&quot;<br />
#include &quot;eval.h&quot;<br />
#include &quot;jobs.h&quot;<br />
#include &quot;input.h&quot;<br />
#include &quot;trap.h&quot;<br />
#include &quot;var.h&quot;<br />
#include &quot;show.h&quot;<br />
#include &quot;memalloc.h&quot;<br />
#include &quot;error.h&quot;<br />
#include &quot;init.h&quot;<br />
#include &quot;mystring.h&quot;<br />
#include &quot;exec.h&quot;<br />
#include &quot;cd.h&quot;<br />
<br />
#ifdef HETIO<br />
#include &quot;hetio.h&quot;<br />
#endif<br />
<br />
#define PROFILE 0<br />
<br />
int rootpid;<br />
int shlvl;<br />
#ifdef __GLIBC__<br />
int *dash_errno;<br />
#endif<br />
#if PROFILE<br />
short profile_buf[16384];<br />
extern int etext();<br />
#endif<br />
<br />
STATIC void read_profile(const char *);<br />
STATIC char *find_dot_file(char *);<br />
static int cmdloop(int);<br />
int main(int, char **);<br />
<br />
/*<br />
 * Main routine. We initialize things, parse the arguments, execute<br />
 * profiles if we're a login shell, and then call cmdloop to execute<br />
 * commands. The setjmp call sets up the location to jump to when an<br />
 * exception occurs. When an exception occurs the variable &quot;state&quot;<br />
 * is used to figure out how far we had gotten.<br />
 */<br />
<br />
/* main関数はややこしいのですが、大半はインタラクティブに使うときの設定で、<br />
シェルスクリプトを読む場合の処理はあまり複雑でないような気がします。<br />
ただ、シグナルがいつくるかわからんとか、そういう不確定要素があるので<br />
順に読んで行っても一筋縄ではいかないようで。 */<br />
<br />
int<br />
main(int argc, char **argv)<br />
{<br />
	char *shinit;<br />
	volatile int state;<br />
/* ↑シグナル等で別のスレッドが書き換えそうな変数にはvolatileをつけないといけません。<br />
最適化されてコードが変わってしまうとフラグの役割を果たさなくなるからです。<br />
（などと偉そうに言っているが、最近のコンパイラでもそうなのだろうか？） */<br />
	struct jmploc jmploc;<br />
/* ↑ error.hにいます。ジャンプに使います。ジャンプというのは集英社じゃなくて<br />
C言語の何かなので、わからん人は集英社にお問い合わせしないでください。<br />
私も使ったことがないので分かりませんので聞かないでください。<br />
っていうかジャンプがないと実装できないのか。本当にそうなのか・・・。 */<br />
	struct stackmark smark;<br />
/* ↑コマンドが実行されるときにスタックにプッシュしたりポップしたりするものなのですが、<br />
実際にどう動作してどう機能しているかはまだ私には分かってません。*/<br />
	int login;<br />
/* ↑おそらくログインしているかどうかを判断するフラグ */<br />
<br />
#ifdef __GLIBC__<br />
	dash_errno = __errno_location();<br />
#endif<br />
/* ↑glibcがあったらerrnoの前処理をするみたいです。suckだそうです。*/<br />
<br />
#if PROFILE<br />
	monitor(4, etext, profile_buf, sizeof profile_buf, 50);<br />
#endif<br />
	state = 0;<br />
	if (unlikely(setjmp(jmploc.loc))) {<br />
/* ↑unlikelyはlikelyと共にShell.hに定義されています。<br />
現在のところフィーリングで理解（つまり理解していない）。<br />
longjmp（飛び降り自殺に近い行為）すると、ここに戻ってきます。<br />
今のところ、setjmpできなかったらこのif文の中身が実行されると解釈。<br />
<br />
\@bsdhack氏からコメント:<br />
「setjmp()できなかったら」ではなく「longjump() から飛んできたら」<br />
*/<br />
		int e;<br />
		int s;<br />
<br />
		reset();<br />
/* ↑reset関数はinit.cで定義されています。たぶん、<br />
このループにいるときはこれまでの処理がなかったかのように<br />
シェルの機能をユーザに提供する段階なので、<br />
resetが呼ばれているものと。しっかし、関数がどこで定義されているか<br />
ちゃんと調べなければいけないのでC言語大変・・・*/<br />
<br />
		e = exception;<br />
/* ↑どこかから妖精のように舞い降りたexception（未調査） */<br />
<br />
/* ↓mainは状態（state）で自由奔放にgotoするので死にたい。*/<br />
		s = state;<br />
/* ↓例外がEXITあるいは、状態が0あるいは、<br />
-iが指定されていないあるいは、レベルが1以上なら終わる。*/<br />
		if (e == EXEXIT || s == 0 || iflag == 0 || shlvl)<br />
			exitshell();<br />
<br />
/* ↓ATTYなんすか？？なんのことですか？端末か何かですか？*/<br />
		if (e == EXINT<br />
#if ATTY<br />
		&amp;&amp; (! attyset() || equal(termval(), &quot;emacs&quot;))<br />
#endif<br />
		) {<br />
			out2c('\\n');<br />
#ifdef FLUSHERR<br />
			flushout(out2);<br />
#endif<br />
		}<br />
/* ↑とりあえずCtrl+c押されたらバッファに溜まった何かを出すということは理解。<br />
ただし、この解釈は間違っている可能性が大いにあり。 */<br />
<br />
		popstackmark(&amp;smark);<br />
/* ↑どこかでpushされているらしい */<br />
		FORCEINTON;				/* enable interrupts */<br />
/* ↑割り込み許可。 */<br />
<br />
/* ↓goto地獄。割り込みがかかったときの処理の再開に使われているような気がするが、<br />
まだ分からない。 */<br />
		if (s == 1)<br />
			goto state1;<br />
		else if (s == 2)<br />
			goto state2;<br />
		else if (s == 3)<br />
			goto state3;<br />
		else<br />
			goto state4;<br />
	}<br />
	handler = &amp;jmploc;<br />
/* ↑このhandlerは、少なくともmain.cでは使われていません。*/<br />
<br />
#ifdef DEBUG<br />
	opentrace();<br />
	trputs(&quot;Shell args: &quot;); trargs(argv);<br />
#endif<br />
<br />
/* ここから初期化が続く */<br />
	rootpid = getpid();<br />
	init();<br />
/* ↓ここでスタックになにか積まれる。何かが。 */<br />
	setstackmark(&amp;smark);<br />
<br />
/* ↓ここら辺はシェルをそこそこ使う人ならなんとなくわかるかと。<br />
つまり、私もなんとなくしかわかってません。*/<br />
	login = procargs(argc, argv);<br />
	if (login) {<br />
		state = 1;<br />
		read_profile(&quot;/etc/profile&quot;);<br />
/*↓こういうところにラベルがあるということは、<br />
やはり初期化が中断されたときにさっきのgotoが使われるということか */<br />
state1:<br />
		state = 2;<br />
		read_profile(&quot;$HOME/.profile&quot;);<br />
	}<br />
state2:<br />
	state = 3;<br />
	if (<br />
/* ↓これはlinuxでないと面倒臭いという解釈でよろしい？iflagは-iつまり、<br />
インタラクティブに使うとき。つまり端末から使うとき。 */<br />
#ifndef linux<br />
		getuid() == geteuid() &amp;&amp; getgid() == getegid() &amp;&amp;<br />
#endif<br />
		iflag<br />
	) {<br />
		if ((shinit = lookupvar(&quot;ENV&quot;)) != NULL &amp;&amp; *shinit != '&#92;&#48;') {<br />
			read_profile(shinit);<br />
		}<br />
	}<br />
/* ↓本当に何に使うんだろう？（というコメントを残しておくと、<br />
あとからわかったときに削除して回らなければいけない予感・・・）*/<br />
	popstackmark(&amp;smark);<br />
state3:<br />
	state = 4;<br />
/* ↓このminuscというのは、「マイナスc」、つまり-cオプションのこと。<br />
-cが指定されているとbash -c &quot;引数&quot;とすると引数に書いたコマンドが実行できる。<br />
そういう場合の話。しかし、イレギュラーなのでmain.cにあるのは邪魔だ。邪魔。*/<br />
	if (minusc)<br />
		evalstring(minusc, sflag ? 0 : EV_EXIT);<br />
/* ↑「-cなら引数をそのまま評価してしまえ。以上。」という感じ */<br />
<br />
/* ↓このコメントが泣ける・・・。state4でここに来たときには<br />
フラグを見なくてよいからという解釈でよいような気がする。<br />
cmdloopに入るとしばらく出てこない。cmdloopはこの下に定義されています。*/<br />
	if (sflag || minusc == NULL) {<br />
state4:	/* XXX ??? - why isn't this before the &quot;if&quot; statement */<br />
		cmdloop(1);<br />
	}<br />
#if PROFILE<br />
	monitor(0);<br />
#endif<br />
#if GPROF<br />
/* ↓わけわかめ。ただ、重要そうではない。<br />
<br />
\@bsdhack氏: プロファイル用<br />
*/<br />
	{<br />
		extern void _mcleanup(void);<br />
		_mcleanup();<br />
	}<br />
#endif<br />
<br />
/* ↓おしまいける！*/<br />
	exitshell();<br />
	/* NOTREACHED */<br />
}<br />
<br />
<br />
/*<br />
 * Read and execute commands. &quot;Top&quot; is nonzero for the top level command<br />
 * loop; it turns on prompting if the shell is interactive.<br />
 */<br />
<br />
/* シェルが立ち上がっている間、こいつがグルグルまわる。<br />
トップのループ（topが1とかそれ以上）でインタラクティブだとプロンプトが出るそうです。 */<br />
static int<br />
cmdloop(int top)<br />
{<br />
/* ↓このnodeというやつにパースしたコマンドやらが入っています。*/<br />
	union node *n;<br />
	struct stackmark smark;<br />
	int inter;<br />
	int status = 0;<br />
	int numeof = 0;<br />
<br />
	TRACE((&quot;cmdloop(%d) called\\n&quot;, top));<br />
<br />
/* ↓HETIOってなんじゃい。たぶん、-iでトップのときに初期化されるので、<br />
インタラクティブな何か。あんまり興味ない。*/<br />
#ifdef HETIO<br />
	if(iflag &amp;&amp; top)<br />
		hetio_init();<br />
#endif<br />
/* ↓回って回って回って回る。 */<br />
	for (;;) {<br />
		int skip;<br />
<br />
		setstackmark(&amp;smark);<br />
		if (jobctl)<br />
			showjobs(out2, SHOW_CHANGED);<br />
		inter = 0;<br />
<br />
/* ↓インタラクティブなとき。メールがあるとか教えてくれるアレです。<br />
inter変数は今の所なにに使うか不明。*/<br />
		if (iflag &amp;&amp; top) {<br />
			inter++;<br />
			chkmail();<br />
		}<br />
/* ↓interを指定するとコマンドをパースしてくれるようです。*/<br />
		n = parsecmd(inter);<br />
		/* showtree(n); DEBUG */<br />
<br />
/* ↓NEOFはperser.hで定義されており、スクリプトの読み終わりに相当。<br />
dashはスクリプトを全部読み込まずに、スクリプトを読みながら処理するので、<br />
NEOFにぶつかるということは処理が全部終わったということに相当。<br />
インタラクティブならプロンプトを出して待つことになる。 */<br />
		if (n == NEOF) {<br />
			if (!top || numeof &gt;= 50)<br />
				break;<br />
			if (!stoppedjobs()) {<br />
/*↓ Iflagは-I（インタラクティブなときにEOFを無視する）に対応。 */<br />
				if (!Iflag)<br />
					break;<br />
				out2str(&quot;\\nUse \\&quot;exit\\&quot; to leave shell.\\n&quot;);<br />
			}<br />
			numeof++;<br />
		} else if (nflag == 0) {<br />
/* ↑nflag（-n）は、「何もしない」。つまりドライランを指定するオプション。<br />
つまりnflag == 0で、「ドライランではない、実行する」という意味になる。 */<br />
			job_warning = (job_warning == 2) ? 1 : 0;<br />
			numeof = 0;<br />
/* ↓実行して終了ステータスをstatusに代入。 */<br />
			evaltree(n, 0);<br />
			status = exitstatus;<br />
		}<br />
		popstackmark(&amp;smark);<br />
<br />
/* ↓このevalskipはbreakやreturn、continueのとき等に設定される。<br />
skipのフラグが立っていれば無限ループを出て下のreturn statusでこの関数が終わる。*/<br />
		skip = evalskip;<br />
		if (skip) {<br />
			evalskip &amp;= ~SKIPFUNC;<br />
			break;<br />
		}<br />
	}<br />
<br />
	return status;<br />
}<br />
<br />
/* ↓ここから下は設定ファイルを読むところ。設定ファイルといっても<br />
シェルスクリプトなので、普通の処理とだいたい同じ手順。 */<br />
<br />
/*<br />
 * Read /etc/profile or .profile. Return on error.<br />
 */<br />
<br />
STATIC void<br />
read_profile(const char *name)<br />
{<br />
	name = expandstr(name);<br />
/* ↓このsetinputfileに入れたファイルがシェルスクリプトとして解釈されるらしい。 */<br />
	if (setinputfile(name, INPUT_PUSH_FILE | INPUT_NOFILE_OK) &lt; 0)<br />
		return;<br />
/* ↓トップでないループ処理に入って設定ファイルを解釈。 */<br />
	cmdloop(0);<br />
	popfile();<br />
}<br />
<br />
<br />
<br />
/*<br />
 * Read a file containing shell functions.<br />
 */<br />
<br />
/* ↓「.」コマンドの横に指定したファイルから関数を読み出す処理。 */<br />
<br />
void<br />
readcmdfile(char *name)<br />
{<br />
	setinputfile(name, INPUT_PUSH_FILE);<br />
	cmdloop(0);<br />
	popfile();<br />
}<br />
<br />
<br />
<br />
/*<br />
 * Take commands from a file. To be compatible we should do a path<br />
 * search for the file, which is necessary to find sub-commands.<br />
 */<br />
<br />
/* ↓「.」コマンドの横に指定したファイルを見つける処理。<br />
パスの探索はかなり処理が面倒臭く、関数が長めになっています。 */<br />
<br />
STATIC char *<br />
find_dot_file(char *basename)<br />
{<br />
	char *fullname;<br />
	const char *path = pathval();<br />
	struct stat statb;<br />
<br />
	/* don't try this for absolute or relative paths */<br />
	if (strchr(basename, '/'))<br />
		return basename;<br />
<br />
	while ((fullname = padvance(&amp;path, basename)) != NULL) {<br />
		if ((stat(fullname, &amp;statb) == 0) &amp;&amp; S_ISREG(statb.st_mode)) {<br />
			/*<br />
			* Don't bother freeing here, since it will<br />
			* be freed by the caller.<br />
			*/<br />
			return fullname;<br />
		}<br />
		stunalloc(fullname);<br />
	}<br />
<br />
	/* not found in the PATH */<br />
	sh_error(&quot;%s: not found&quot;, basename);<br />
	/* NOTREACHED */<br />
}<br />
<br />
/* ↓ 「.」コマンドの実装。わたしゃ滅多に使いません。*/<br />
<br />
int<br />
dotcmd(int argc, char **argv)<br />
{<br />
	int status = 0;<br />
<br />
	if (argc &gt;= 2) {		/* That's what SVR2 does */<br />
		char *fullname;<br />
<br />
		fullname = find_dot_file(argv[1]);<br />
		setinputfile(fullname, INPUT_PUSH_FILE);<br />
		commandname = fullname;<br />
		status = cmdloop(0);<br />
		popfile();<br />
	}<br />
	return status;<br />
}<br />
<br />
/*↓これはexitコマンドの実装。こちらは.と違ってよく使います。<br />
オプションに指定された終了ステータスを処理して例外を送ってます。<br />
「例外はがんばって実装したよ」とTOURファイルに書いてありました。<br />
C++を使いたいところ。大半の人はそう思わないだろうが。 */<br />
<br />
int<br />
exitcmd(int argc, char **argv)<br />
{<br />
	if (stoppedjobs())<br />
		return 0;<br />
	if (argc &gt; 1)<br />
		exitstatus = number(argv[1]);<br />
	exraise(EXEXIT);<br />
	/* NOTREACHED */<br />
}<br />
<br />
[/c]
