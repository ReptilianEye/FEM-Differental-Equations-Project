
# Rozwiązanie równania różniczkowego drugiego rzędu metodą elementów skończonych
--------
<h2 align="center"> Równanie: </h2>

``` math
\ -\left(E(x) \cdot u^{\prime}(x)\right)^{\prime}=0
```

\[ -\left(E(x) \cdot u^{\prime}(x)\right)^{\prime}=0 \]

\[ \quad \quad \Omega=(0,2) \quad u(2)=3 \quad  u^{\prime}(0)+u(0)=10\]

\[ E(x)= \begin{cases}2 & \text { dla } x \in[0,1] \\ 6 & \text { dla } x \in(1,2]\end{cases} \]

<h2 align="center"> Rozwiązanie: </h2>

\[ -E^{\prime}(x) \cdot u^{\prime}(x)-E(x) \cdot u^{\prime \prime}(x)=0 \]

\[ -E^{\prime}(x) \cdot u^{\prime}(x)-E(x) \cdot u^{\prime \prime}(x)=0  \]

\[ u=\tilde{u}+w \quad w(2)=0 \quad \tilde{u}(2)=3 \Rightarrow \tilde{u} \equiv 3  \]

\[ \Rightarrow u=w+3  \]

\[ u^{\prime}=w^{\prime} \quad \]

\[ u^{\prime \prime}=w^{\prime \prime}  \]

\[ u^{\prime}(0)=10-u(0) \quad \Rightarrow  w^{\prime}(0)=7-w(0) \]

\[ -\int_0^2 E^{\prime} w^{\prime} \varphi d x-\int_0^2 E w^{\prime \prime} \varphi d x=0 \]

<h6 align="center"> Ponieważ szukamy rozwiązania w przestrzeni, w której nie ma drugiej pochodnej, musimy się jej pozbyć. </h6>

\[ -\int_0^2 E w^{\prime \prime} \varphi d x=\left|\begin{array}{ll}
f=E \varphi & y^{\prime}=w^{\prime \prime} \\
f^{\prime}=E^{\prime} \varphi+E \varphi^{\prime} & y=w^{\prime}
\end{array}\right|=-\left.E \varphi w^{\prime}\right|_0 ^2 +\int_0^2 E^{\prime} \varphi w^{\prime} d x+\int_0^2 E \varphi^{\prime} w^{\prime} d x =\]

\[ =\underbrace{-E(2) \varphi(2) w^{\prime}(2)}_{=0}+E(0) \varphi(0) w^{\prime}(0) +\int_0^2 E^{\prime} \varphi w^{\prime} d x+\int_0^2 E\varphi^{\prime} w^{\prime} d x= \]

\[ =7 E(0) \varphi(0)-E(0) \varphi(0) w(0) +\int_0^2 E^{\prime} \varphi w^{\prime} d x+\int_0^2 E\varphi^{\prime} w^{\prime} d x. \]

<h6 align="center"> Wracamy do głównego równania: </h6>

\[ -\int_0^2 E^{\prime} \varphi w^{\prime} d x+\int_0^2 E^{\prime} \varphi w^{\prime} d x+\int_0^2 E \varphi^{\prime} w^{\prime} d x-E(0) \varphi(0) w^{\prime}(0)= -7 E(0) \varphi(0) \]

\[ \underbrace{\int_0^2 E \varphi^{\prime} w^{\prime} d x-E(0) \varphi(0) w^{\prime}(0)}_{B(w, \varphi)}=\underbrace{-7 E(0) \varphi(0)}_{L(\varphi)} \]
