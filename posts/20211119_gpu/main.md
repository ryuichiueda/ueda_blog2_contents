---
Keywords: GPU, CUDA
Copyright: (C) 2021 Ryuichi Ueda
---

# CPUとGPUの速度比較

　まだCUDAを触り始めて延べ2日なのですが、GPUの速度が気になったので拙いコードで実験してみました。とりあえずGPUがCPUより速いケースを1つ見つけました。

## 比較するコード

　2次元配列の計算を書いた、次の2つのコードを比較します。

* CPUだけ使ったもの（CPU版）: https://github.com/ryuichiueda/my_cuda_practice/blob/master/array2d.cpp
* GPUを使ったもの（GPU版）: https://github.com/ryuichiueda/my_cuda_practice/blob/master/array2d.cu

　計算はこんなものです。`C`という配列に、`A`と`B`の要素の線型和を何度も足すという、あまり意味のないコードです。

```cpp
// CPU版のコード（array2d.cpp)
for(int j=0;j<N;j++){
    for(int i=0;i<N;i++){
       for(int k=0;k<times;k++)
            C[i + j*N] += A[i + j*N]*3.14 + B[i + j*N]/3.14;
    }
}   
```

あとの実験では、`N=512`で、`times`を`1, 2, 4, 8, ..., 1024`と変化させています。

　上のCPU版のコードと同等なCUDAのコードを下に示します。動作は確認していますが、素人工事で、なんで動くかもさっぱりわかりません。あと、`N>800`でセグメンテーションフォルトを起こします。

```cpp
// GPU版のコード（array2d.cu)
// この関数が各GPUのコアで並列実行される
__global__ void MatAdd(float *A, float *B, float *C, int times)
{
    int block_idx = blockIdx.x*blockDim.x*blockDim.y;
    int i = threadIdx.x + blockDim.x * threadIdx.y + block_idx;
    for(int k=0;k<times;k++)
        C[i] += A[i]*3.14 + B[i]/3.14;
}

int main(int argc, char **argv)
{
（中略）
// ここで実行
    MatAdd<<<N, N>>>(a, b, c, times);
```

　上のコードの例では省略しましたが、GPUで計算するときは、メモリの内容をGPUとDRAMでやりとりする処理が必要です。この処理の時間も計測時間に含めます。このコードの場合、`times`の回数にかかわらずやりとりはDRAM->GPU1回、GPU->DRAM1回の2回だけなので、`times`の回数が増えるほど、GPUの並列処理の効果が見込めます。

## 実験


　先述のように`N=512`、`times`を`1, 2, 4, 8, ..., 1024`と変化させて計算時間を計測しました。

### CPU版

　ざっくり言って、`times`あたり1[ms]ずつ比例して増えていきます。

| `times` | 平均計算時間[ms] | 標準偏差[ms] |
|---:|--------:|-----:|
| 2 | 0.8 | 0.0 |
| 4 | 1.5 | 0.0 |
| 8 | 3.5 | 0.1 |
| 16 | 8.8 | 0.1 |
| 32 | 24.0 | 0.3 |
| 64 | 56.7 | 0.2 |
| 128 | 122.8 | 0.2 |
| 256 | 253.9 | 0.4 |
| 512 | 515.4 | 0.2 |
| 1024 | 1039.9 | 1.1 |

### GPU版

　GPUの場合は、`times=64`あたりまではメモリの内容の転送に時間がかかっているようですが、

| `times` | 平均計算時間[ms] | 標準偏差[ms] |
|---:|--------:|-----:|
| 2 | 55.7 | 4.6 |
| 4 | 54.9 | 3.2 |
| 8 | 56.1 | 9.3 |
| 16 | 54.4 | 2.2 |
| 32 | 55.1 | 1.5 |
| 64 | 57.4 | 2.1 |
| 128 | 62.6 | 3.2 |
| 256 | 71.0 | 5.9 |
| 512 | 89.0 | 8.9 |
| 1024 | 125.7 | 13.8 |

