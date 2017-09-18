---
Copyright: (C) Ryuichi Ueda
---


# dash/src/shell.h
気ままにコメントしております。正確さは・・・周囲の評価に委ねます。<br />
<br />
このファイルにはC言語らしいテクニックがいくつか。<br />
<br />
<br />
<a href="http://blog.ueda.asia/?page_id=4219" title="dashのコード解読メモ">「dashのコード解読メモ」に戻る</a><br />
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
 *	\@(#)shell.h	8.2 (Berkeley) 5/4/95<br />
 */<br />
<br />
/*<br />
 * The follow should be set to reflect the type of system you have:<br />
 *	JOBS -&gt; 1 if you have Berkeley job control, 0 otherwise.<br />
 *	SHORTNAMES -&gt; 1 if your linker cannot handle long names.<br />
 *	define BSD if you are running 4.2 BSD or later.<br />
 *	define SYSV if you are running under System V.<br />
 *	define DEBUG=1 to compile in debugging ('set -o debug' to turn on)<br />
 *	define DEBUG=2 to compile in and turn on debugging.<br />
 *	define DO_SHAREDVFORK to indicate that vfork(2) shares its address<br />
 *	with its parent.<br />
 *<br />
 * When debugging is on, debugging info will be written to ./trace and<br />
 * a quit signal will generate a core dump.<br />
 */<br />
<br />
#include &lt;sys/param.h&gt;<br />
<br />
/* ↓JOBSとBSDはmakeのときに変わるのかなあ？<br />
とか思ってLinuxでもmakeしてみたけど変わりませんでした。 */<br />
#ifndef JOBS<br />
#define JOBS 1<br />
#endif<br />
#ifndef BSD<br />
#define BSD 1<br />
#endif<br />
<br />
/* ↓C++屋でほとんどマクロ使わないから分からんが、<br />
インデントはしないのだろうか？できないんだっけか？ */<br />
#ifndef DO_SHAREDVFORK<br />
#if __NetBSD_Version__ &gt;= 104000000<br />
#define DO_SHAREDVFORK<br />
#endif<br />
#endif<br />
<br />
/* ↓void *をpointerと表す。そんなこと必要なほどvoid *使うのかな。 */<br />
typedef void *pointer;<br />
<br />
/* ↓ヌルってない環境のためにヌルを定義 */<br />
#ifndef NULL<br />
#define NULL (void *)0<br />
#endif<br />
<br />
/* ↓なんでこんなことするの？ */<br />
#define STATIC static<br />
<br />
/* ↓これは互換性の何かなんだろう。おそらく。<br />
別のファイルで関数の頭にMKINIT int hogehoge()と付いている。<br />
MKタクシーではない。 */<br />
#define MKINIT	/* empty */<br />
<br />
/* ↓これを文字列の初期化のときに代入するみたい。<br />
初期化されたままの文字列を検出するときに使うようである。<br />
nullstr[0]は初期化されていないので適当なアドレスが<br />
入っている模様。こういうテクニックを使う<br />
文化があるのかどうかはよくわからん。 */<br />
extern char nullstr[1];		/* null string */<br />
<br />
/* ↓トレースの準備。しっかし、大文字のTRACEってWindowsでもあったなあ。<br />
使い方はdash/TOURに解説あり。<br />
trace paramとコマンドみたいになっているが、<br />
使うときにTRACE((aaa))と書くとtrace(aaa)という関数になる。 */<br />
#ifdef DEBUG<br />
#define TRACE(param)	trace param<br />
#define TRACEV(param)	tracev param<br />
#else<br />
#define TRACE(param)<br />
#define TRACEV(param)<br />
#endif<br />
<br />
/* ↓可変長の引数を扱うためにva_*というマクロがあるらしい。*/<br />
#if defined(__GNUC__) &amp;&amp; __GNUC__ &lt; 3<br />
#define va_copy __va_copy<br />
#endif<br />
<br />
/* ↓分岐予測のためのものだそうです。expected_valueに<br />
xがとる確率が高い値を入れておくと速くなる。へえ。 */<br />
#if !defined(__GNUC__) || (__GNUC__ == 2 &amp;&amp; __GNUC_MINOR__ &lt; 96)<br />
#define __builtin_expect(x, expected_value) (x)<br />
#endif<br />
<br />
/* ↓これは__builtin_expectを使うときの定石らしい。!!が二つあるのは、<br />
not notという意味で、おそらく真値（0以外の数）を1に正規化するためだろう。<br />
おそらく。 */<br />
*/<br />
#define likely(x)	__builtin_expect(!!(x),1)<br />
#define unlikely(x)	__builtin_expect(!!(x),0)<br />
<br />
/* ↓シェルで数字を計算するときに使う最大値みたいだが、<br />
あまりいい感じではない。 */<br />
/*<br />
 * Hack to calculate maximum length.<br />
 * (length * 8 - 1) * log10(2) + 1 + 1 + 12<br />
 * The second 1 is for the minus sign and the 12 is a safety margin.<br />
 */<br />
static inline int max_int_length(int bytes)<br />
{<br />
	return (bytes * 8 - 1) * 0.30102999566398119521 + 14;<br />
}<br />
[/c]
