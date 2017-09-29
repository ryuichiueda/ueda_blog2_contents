---
Copyright: (C) Ryuichi Ueda
---


# dash/src/shell.h
気ままにコメントしております。正確さは・・・周囲の評価に委ねます。

このファイルにはC言語らしいテクニックがいくつか。


<a href="http://blog.ueda.asia/?page_id=4219" title="dashのコード解読メモ">「dashのコード解読メモ」に戻る</a>

```c
/*-
 * Copyright (c) 1991, 1993
 *	The Regents of the University of California. All rights reserved.
 * Copyright (c) 1997-2005
 *	Herbert Xu <herbert\@gondor.apana.org.au>. All rights reserved.
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
 *	\@(#)shell.h	8.2 (Berkeley) 5/4/95
 */

/*
 * The follow should be set to reflect the type of system you have:
 *	JOBS -> 1 if you have Berkeley job control, 0 otherwise.
 *	SHORTNAMES -> 1 if your linker cannot handle long names.
 *	define BSD if you are running 4.2 BSD or later.
 *	define SYSV if you are running under System V.
 *	define DEBUG=1 to compile in debugging ('set -o debug' to turn on)
 *	define DEBUG=2 to compile in and turn on debugging.
 *	define DO_SHAREDVFORK to indicate that vfork(2) shares its address
 *	with its parent.
 *
 * When debugging is on, debugging info will be written to ./trace and
 * a quit signal will generate a core dump.
 */

#include <sys/param.h>

/* ↓JOBSとBSDはmakeのときに変わるのかなあ？
とか思ってLinuxでもmakeしてみたけど変わりませんでした。 */
#ifndef JOBS
#define JOBS 1
#endif
#ifndef BSD
#define BSD 1
#endif

/* ↓C++屋でほとんどマクロ使わないから分からんが、
インデントはしないのだろうか？できないんだっけか？ */
#ifndef DO_SHAREDVFORK
#if __NetBSD_Version__ >= 104000000
#define DO_SHAREDVFORK
#endif
#endif

/* ↓void *をpointerと表す。そんなこと必要なほどvoid *使うのかな。 */
typedef void *pointer;

/* ↓ヌルってない環境のためにヌルを定義 */
#ifndef NULL
#define NULL (void *)0
#endif

/* ↓なんでこんなことするの？ */
#define STATIC static

/* ↓これは互換性の何かなんだろう。おそらく。
別のファイルで関数の頭にMKINIT int hogehoge()と付いている。
MKタクシーではない。 */
#define MKINIT	/* empty */

/* ↓これを文字列の初期化のときに代入するみたい。
初期化されたままの文字列を検出するときに使うようである。
nullstr[0]は初期化されていないので適当なアドレスが
入っている模様。こういうテクニックを使う
文化があるのかどうかはよくわからん。 */
extern char nullstr[1];		/* null string */

/* ↓トレースの準備。しっかし、大文字のTRACEってWindowsでもあったなあ。
使い方はdash/TOURに解説あり。
trace paramとコマンドみたいになっているが、
使うときにTRACE((aaa))と書くとtrace(aaa)という関数になる。 */
#ifdef DEBUG
#define TRACE(param)	trace param
#define TRACEV(param)	tracev param
#else
#define TRACE(param)
#define TRACEV(param)
#endif

/* ↓可変長の引数を扱うためにva_*というマクロがあるらしい。*/
#if defined(__GNUC__) && __GNUC__ < 3
#define va_copy __va_copy
#endif

/* ↓分岐予測のためのものだそうです。expected_valueに
xがとる確率が高い値を入れておくと速くなる。へえ。 */
#if !defined(__GNUC__) || (__GNUC__ == 2 && __GNUC_MINOR__ < 96)
#define __builtin_expect(x, expected_value) (x)
#endif

/* ↓これは__builtin_expectを使うときの定石らしい。!!が二つあるのは、
not notという意味で、おそらく真値（0以外の数）を1に正規化するためだろう。
おそらく。 */
*/
#define likely(x)	__builtin_expect(!!(x),1)
#define unlikely(x)	__builtin_expect(!!(x),0)

/* ↓シェルで数字を計算するときに使う最大値みたいだが、
あまりいい感じではない。 */
/*
 * Hack to calculate maximum length.
 * (length * 8 - 1) * log10(2) + 1 + 1 + 12
 * The second 1 is for the minus sign and the 12 is a safety margin.
 */
static inline int max_int_length(int bytes)
{
	return (bytes * 8 - 1) * 0.30102999566398119521 + 14;
}
```
