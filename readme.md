
# Rozwiązanie równania różniczkowego drugiego rzędu metodą elementów skończonych
--------
<h2 align="center"> Równanie: </h2>


$$ -\left(E(x) \cdot u^{\prime}(x)\right)^{\prime}=0 $$

$$ \quad \quad \Omega=(0,2) \quad u(2)=3 \quad  u^{\prime}(0)+u(0)=10 $$

``` math
E(x)= \begin{cases}2 & \text { dla } x \in[0,1] \\ 6 & \text { dla } x \in(1,2]\end{cases}
```
<h2 align="center"> Rozwiązanie: </h2>

$$ -E^{\prime}(x) \cdot u^{\prime}(x)-E(x) \cdot u^{\prime \prime}(x)=0 $$

``` math
u=\tilde{u}+w  \quad w \in V= \{f: f \in H^1, f(2)=0 \}
```

$$  w(2)=0 \quad \tilde{u}(2)=3 \Rightarrow \tilde{u} \equiv 3  $$

$$ \Rightarrow u=w+3  $$

$$ u^{\prime}=w^{\prime} \quad $$

$$ u^{\prime \prime}=w^{\prime \prime}  $$

$$ u^{\prime}(0)=10-u(0) \quad \Rightarrow  w^{\prime}(0)=7-w(0) $$

$$ -\int_0^2 E^{\prime} w^{\prime} \varphi d x-\int_0^2 E w^{\prime \prime} \varphi d x=0, \quad \varphi \in V $$

<h6 align="center"> Ponieważ szukamy rozwiązania w przestrzeni, w której nie ma drugiej pochodnej, musimy się jej pozbyć. </h6>

$$ -\int_0^2 E w^{\prime \prime} \varphi d x=\left|\begin{array}{ll}
f=E \varphi & y^{\prime}=w^{\prime \prime} \\
f^{\prime}=E^{\prime} \varphi+E \varphi^{\prime} & y=w^{\prime}
\end{array}\right|=-\left.E \varphi w^{\prime}\right|_0 ^2 +\int_0^2 E^{\prime} \varphi w^{\prime} d x+\int_0^2 E \varphi^{\prime} w^{\prime} d x =$$

$$ =\underbrace{-E(2) \varphi(2) w^{\prime}(2)}_{=0}+E(0) \varphi(0) w^{\prime}(0) +\int_0^2 E^{\prime} \varphi w^{\prime} d x+\int_0^2 E\varphi^{\prime} w^{\prime} d x. $$

<h6 align="center"> Wracamy do głównego równania: </h6>

$$ -\bcancel{\int_0^2 E^{\prime} \varphi w^{\prime} d x} +\bcancel{\int_0^2 E^{\prime} \varphi w^{\prime} d x}+\int_0^2 E \varphi^{\prime} w^{\prime} d x-E(0) \varphi(0) w^{\prime}(0)= -7 E(0) \varphi(0) $$

``` math
\underbrace{\int_0^2 E \varphi^{\prime} w^{\prime} d x-E(0) \varphi(0) w^{\prime}(0)}_{B(w, \varphi)}=\underbrace{-7 E(0) \varphi(0)}_{L(\varphi)} 
```
<h6 align="center"> Będziemy szukali rozwiązania za pomocą następujących funkcji: </h6>

<p align="center">
    <img src="/img/eFunc.jpg" alt="e functions" width="50%">
</p>

<h6 align="center"> Wybieramy takie funkcje e, które zerują się w x=2. Szukana funkcja jest następującą kombinacją liniową:</h6>

$$ w_n=e_0 w_0+e_1 w_1+\ldots+e_{n-1} w_{n-1} $$

<h6 align="center"> Należy rozwiązań następujący układ: </h6>

```math
\left[\begin{array}{cccc}
B\left(e_0, e_0\right) & B\left(e_1, e_0\right) & \ldots & B\left(e_{n-1}, e_0\right) \\
B\left(e_0, e_1\right) &\ddots & & \vdots \\
\vdots & & \\
B\left(e_0, e_{n-1}\right) & \ldots & & B\left(e_{n-1}, e_{n-1}\right)
\end{array}\right]\left[\begin{array}{c}
w_0 \\
w_1 \\
\vdots \\
w_{n-1}
\end{array}\right]=\left[\begin{array}{c}
L\left(e_0\right) \\
L\left(e_1\right) \\
\vdots \\
L\left(e_{n-1}\right)
\end{array}\right]\\
```

<h6 align="center"> Ponieważ użyliśmy shift finalne rozwiązanie to:</h6>

$$ u_n=w_n+3 $$

<h2 align="center"> Wyniki: </h2>
<p align="center">
    <div style="display: flex;">
        <div style="flex: 33.33%; padding: 5px;">
            <img src="/img/solution100.png" alt="Solution 100" width="100%">
            <p align="center">Rys. 1. Rozwiązanie dla n=100</p>
        </div>
        <div style="flex: 33.33%; padding: 5px;">
            <img src="/img/solution250.png" alt="Solution 250" width="100%">
            <p align="center">Rys. 2. Rozwiązanie dla n=250</p>
        </div>
        <div style="flex: 33.33%; padding: 5px;">
            <img src="/img/solution500.png" alt="Solution 500" width="100%">
            <p align="center">Rys. 3. Rozwiązanie dla n=500</p>
        </div>
<p align="center">
    <div style="flex: 33.33%; padding: 5px;">
        <img src="/img/solution1000.png" alt="Solution 1000" width="100%">
        <p align="center">Rys. 4. Rozwiązanie dla n=1000</p>
    </div>
</p>
    </div>
</p>