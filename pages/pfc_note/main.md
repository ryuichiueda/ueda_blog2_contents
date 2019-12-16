---
Keywords: 研究
Copyright: (C) 2019 Ryuichi Ueda
---

# 固定障害物回避のためのPFC法の拡張

## このドキュメント

　書いている途中の日本語プレプリントです。支障のないものはすべて手の内をオープンにして研究することにしました。

## 背景

　移動ロボットはいまだにセンシングできない角を安全に曲がれない。どんなにセンサが良くなろうとも、どんな環境条件でも正確な値を返してくるセンサなど存在しない。センシング条件が悪い場合に、移動ロボットが事故を予測して適切に回避するアルゴリズムを考えることは有用である。

　　このニッチながら重要な問題に数理モデルで取り組んでいる研究は（あんまり調査していないものの）見られない。

## 従来研究

　移動ロボットの自己位置推定は本質的に曖昧で、推定結果は確率的に表現されることが多い[[Thrun 2005]](https://mitpress.mit.edu/books/probabilistic-robotics)。この場合、自己位置推定結果は、環境中でロボットが到達する可能性のある全位置・向き（以後、まとめて「姿勢」と表記）


## 以下ガラクタ



\section{PROBLEM DEFINITION}\label{sec:problem}


We handle a POMDP (partially observable Markov decision process)
problem\cite{cassandra96}. We assume a system in which
a robot chooses and executes an action at every time step
$t=0,1,2,\dots,T-1$. 
$T$ denotes the time step at which the task is finished. 
The value of $T$ is not fixed.


\subsection{State transition}

The state transition by an action is defined stochastically as
\begin{align}
	\V{x}_t \sim p(\V{x} | \V{x}_{t-1}, a_t) \quad (\V{x}_t, \V{x}, \V{x}_{t-1} \in \mathcal{X}, a_t \in \mathcal{A} ),  \label{eq:state_transition_model}
\end{align}
where $\V{x}$ is a state in the state space $\mathcal{X}$.
$\V{x}_t$ is the state at time $t$.
The probability density function (pdf) $p(\V{x} | \V{x}_{t-1}, a_t)$ 
represents the state transition model of the system.
The symbol $\sim$ denotes a choice of
a random variable based on the pdf at its right side. 
$a_t$ is the action of the robot between time $t-1$ and $t$.
An action is chosen from the set of actions $\mathcal{A}$
once in a time step.


\subsection{State Estimation}

At each time $t$, the robot obtains an observation $\V{z}_t$,
which is generated with the following observation model:
\begin{align}
	\V{z}_t \sim p(\V{z} | \V{x}_t). \label{eq:observation_model}
\end{align}
The robot cannot perceive the actual state $\V{x}_t^*$.
Therefore, it must estimate $\V{x}^*$ from the observations.

By using the pdfs in
Equations (\ref{eq:state_transition_model}) and (\ref{eq:observation_model}), 
the robot calculates the following pdf
\begin{align}
b_t(\V{x}) = p(\V{x}_t | a_{1:t}, \V{z}_{1:t}),
\end{align}
where $a_{1:t} = \{a_1, a_2, \dots, a_t\}$ and
$z_{1:t} = \{z_1, z_2, \dots, z_t\}$.
$b_t$ is referred to as a belief\cite{thrun2005}. 

while it knows the state transition model
$p(\V{x} | \V{x}_{t-1}, a_t)$ and
the observation model $p(\V{z} | \V{x}_t)$.


The robot calculates the belief with a Bayes filter, 
which is composed of the following two equations:
\begin{align}
	\hat{b}_t(\V{x}) &=  \big\langle p(\V{x} | \V{x}', a_t) \big\rangle_{b_{t-1}(\V{x}')}, \ \text{and}\\
	b_t(\V{x}) &= \eta p(\V{z} | \V{x}_t)\hat{b}_t(\V{x}),
\end{align}
where $\langle \cdot \rangle_p$ denotes the expectation operator
and $\eta$ is the normalizing constant. 
They are applied to the belief just after $a_t$ and
$\V{z}_t$ are determined respectively. 

\subsection{Task}

Task is given through the following evaluation:
\begin{align}
	J(a_{1:T}, \V{x}_{0,T}) = \sum_{t=1}^T r(a_t, x_t) + V_\text{f}(\V{x}_T). \label{eq:j}
\end{align}
This $J$ corresponds to a functional of optimal control on a discrete space. 

The solution of this problem is given as the optimal policy:
\begin{align}
	\Pi^*: \mathcal{X} \to \mathcal{A}.
\end{align}
This function gives the action required to maximize the value $J$ for every state $\V{x}$.
When we can solve the expected value of $J$ when the robot starts from a state $\V{x}$, 
the function of the expected value 

\section{PFC WITH ATTENTION}\label{sec:method}

\subsection{Q-MDP and PFC}

When the state is unknown, the robot cannot evaluate 

PFC is a method biases 

In \cite{ueda2018robio}, 

\begin{align}
	\hat{Q}(a,b_t) &= \Big\langle \dfrac{1}{[V_\text{max} - V(\V{x})]^m}
        Q(a, \V{x})
	\Big\rangle_{b_t(\V{x})}, \label{eq:pfc}
\end{align}
where $V_{\max} = \max_{\V{x} \in \mathcal{X}} V(\V{x})$.

When $m=0$, Equation (\ref{eq:pfc}) corresponds to the equation used in the Q-MDP value method \cite{littman1995}.


\subsection{Attention function}

We propose an attentionn function 
\begin{align}
	Y: \mathcal{X} \to \Re,
\end{align}
which quantifies how much a state should be 

We introduce an attention function 


\begin{align}
	\hat{Q}(a,b_t, Y_{t-1}) &= \Big\langle Y_t(\V{x})
        Q(a, \V{x})
	\Big\rangle_{b_t(\V{x})}, \label{eq:pfc}
\end{align}
where
\begin{align}
	Y(\V{x} | a_{t:1}, b_{t:0}) &= \max_{a_{t+1} \in \mathcal{A}} y(\V{x}, a_{t+1:1}, b_{t:0}).
\end{align}

\subsection{Implementation of PFC with attention weight}

Add a variable of attention weight.

\begin{align}
	\xi^{(i)} = (\V{x},w, \alpha)
\end{align}


\begin{align}
	\alpha = 
\end{align}
