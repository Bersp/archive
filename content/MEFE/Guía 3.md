---
title: "Guía 3"
summary: "Guía 3 de MEFE"
math: true
---

{{< toc title="Lista de ejercicios">}}


# Ejercicio 1

## Enunciado
La altura de la población masculina tiene distribución normal $N(175 \\text{cm}, 8 \\text{cm})$.
Sabiendo que los colectivos tienen una altura de 1.95 \\text{m}, ¿qué fracción puede viajar parada sin necesidad de reclinarse? (Rta: $P=0.9938$)

## Resolución
$$
  P = \\int_{-\\infty}^{195} N(x, 175, 8)\\, dx \\simeq 0.9938
$$

# Ejercicio 2
## Enunciado
Se mide una magnitud $A$ con un detector bien calibrado cuya resolución es gaussiana con ancho $\\sigma$, obteniéndose el resultado $x$.
- a) ¿Qué rango $x \\pm a$ debe informarse si se desea que haya $90\\%$ de probabilidad de que éste incluya el verdadero valor de $A$? (Rta: $x \\pm 1.645\\sigma$)
- b) Si el detector tuviera una respuesta no gaussiana y desconocida, pero se sabe que tiene una resolución $\\sigma$, qué rango puede informar en este caso? (Rta: $x \\pm 3.162\\sigma$)
- c) ¿Y si nos dicen que además la distribución que caracteriza la respuesta del detector es unimodal?
_Ayuda: Desigualdad de Vysochanskij–Petunin. (Rta: $x \\pm 1.405\\sigma$)_

### Punto a
La mejor estimación que tenemos de la media es $\\mu = x$.
$$
  \\begin{align*}
    P &= \\int_{x-a}^{x+a} N(x', \\mu, \\sigma) \\, dx' \\\\
      &= \\int_{-\\infty}^{x+a} N(x', \\mu, \\sigma) \\, dx' - \\int_{-\\infty}^{x+a} N(x', \\mu, \\sigma) \\, dx' \\\\
      & \\lesssim 0.9
  \\end{align*}
$$

# Ejercicio 3
## Enunciado
Una fuente radiactiva de actividad $\\lambda$ (decaimientos por unidad de tiempo) se ubica frente a un detector de eficiencia perfecta. Asuma que en cada decaimiento se emite una sola partócula.
- a) Muestre que $X$, el tiempo transcurrido hasta la detección de la primera partócula, tiene distribución exponencial $f_X(t) = λe^{−λt}$.
Proceda de dos maneras alternativas, discutiendo la validez de cada paso:
  - Obtenga primero $F_X(t) = P(X \\leq t)$ como el complemento del suceso "el primer decaimiento ocurre a tiempo mayor que t", y luego por derivación, la densidad de probabilidad $f_X(t)$.
  - Escriba directamente fX(t) como el producto de la probabilidad de que no haya ningón decaimiento entre $0$ y $t$, y que haya un decaimiento justo en el $dt$ siguiente.
- b) Se dice que una distribución no tiene memoria si cumple $P(X > t + s|X > t) = P(X > s)$.
  - ¿Por qué a ésto se lo llama así?
  - Convénzase de que la exponencial es la única distribución de variable contínua que posee esta propiedad (intente usando otras distribuciones).
  Relaciónelo con las hipótesis que llevan a la distribución de Poisson.
  _Nota: para variables aleatorias discretas se define la condición como: $P(X > n+m|X ≥ n) = P(X > m)$_
- c) Se tiene una fuente de 1 Bq (Becquerel = $1$ decaimiento $s^{−1}$).
  - ¿Cuál es la probabilidad de que el primer decaimiento ocurra recién después de $5$ segundos? (Rta: $P = 0.0067$)
  - Calcule la probabilidad de que el primer decaimiento ocurra dentro del primer segundo. Repita el cálculo para el tercer segundo (i.e. el primer decaimiento ocurre entre el 2do y 3er segundo).
  ¿Contradice ésto la "falta de memoria"? (Rta: $P=0.6321$ y $P=0.0855$)
  - ¿Cuánto tiempo debe esperarse para que haya al menos un decaimiento, con una probabilidad del $99\\%$? (Rta: $4.61\\text{s}$)
- d) Si el detector tuviera perfecta eficiencia intrínseca (mide todo lo que le llega) pero cubre un ángulo sólido $\\omega$ visto desde la fuente, ¿como se modifica $f_X(t)$ si las partículas son emitidas en todas direcciones con igual probabilidad?
- e) Mencione otros tres ejemplos de procesos que tengan distribución exponencial.

## Reslución
### Punto c
#### i.
$$
  P(X >5) = 1-\\int_0^{5} EXP(x, \\lambda = 1)\\,dx = e^{-5} \\simeq 0.0067
$$
#### i..
$$
  P(X < 1) = EXP(1, \\lambda=1) \\simeq 0.6321
$$
$$
  P(2 < X < 3) = EXP(3, \\lambda=1) - EXP(2, \\lambda=1) \\simeq 0.0855
$$
#### i.i.
Quiero $t$ tal que $P(X<t) \\gtrsim 0.99$.
$$
  P(X<4.61) = \\int_0^{4.61} EXP(x, \\lambda=1)\\,dx = 0.990048...
$$

# Ejercicio 4
## Enunciado
Si $X$ tiene distribución normal estándar,
- a) ¿Qué distribución tiene $Y = aX + b$?
- b) ¿Cómo implementaría un generador de números al azar $N(\\mu,\\sigma)$ a partir de uno $N(0,1)$?

### Punto a
$$
  F_X(x) = P(X \\leq x),\\quad F_Y(y) = O(Y \\leq y)
$$
$$
  Y\\leq y \\iff aX+b \\leq y \\iff X\\leq \\frac{y-b}{a}
$$
$$
  \\begin{align*}
    \\implies
    P(Y \\leq y) &= P\\left(X\\leq \\frac{y-b}{a}\\right) \\\\
                &= F_X\\left(\\frac{y-b}{a}\\right) \\\\
                &= F_Y(y)
  \\end{align*}
$$
$$
  f_Y(y) = \\frac{d F_Y(y)}{dy} = \\frac{d}{dy}F_X\\left(\\frac{y-b}{a}\\right)
         = \\frac{dx}{dy}\\,\\frac{d F_X}{d x}
$$
$$
  \\implies
  f_X(y) = \\frac{1}{a} f_X\\left(\\frac{y-b}{a}\\right)
  = \\frac{1}{a}\\,N\\left(\\frac{y-b}{a}\\Big| 0, 1\\right)
$$

# Ejercicio 5
## Enunciado
Una barra gira alrededor del punto $(-a, b)$, hasta detenerse al azar formando un ángulo $\\theta$ con el eje $x$, $(\\Theta \\in [−\\pi/2, \\pi/2])$, como muestra la figura.
La recta que contiene a la barra corta al eje de ordenadas en un punto $Y$. Encuentre la función de distribución $F_\\Theta(t)$, y a partir de ésta muestre que $Y$ tiene densidad de probabilidad de Cauchy, $f_Y(t) = \\frac{1}{\\pi} \\frac{a}{a^2 + (t − b)^2}$ . Encuentre su esperanza.\\
Notar que la esperanza de una variable con distribución de Cauchy es cero por simetría (su _valor principal_ está definido), pero la primitiva de $x/(1+x^2)$ es divergente

## Resolución
- $\\Theta \\in [-\\frac{\\pi}{2}, \\frac{\\pi}{2}]$
- $\\theta \\sim U(-\\frac{\\pi}{2}, \\frac{\\pi}{2}) \\implies F_\\Theta(t) = \\frac{1}{\\pi}\\,t$
$$
  \\operatorname{tg}(\\theta) = \\frac{Y-b}{a} \\implies Y = \\operatorname{atg}(\\theta) + b
$$

$$
  f_Y(y) = f_\\theta(t)\\left|\\frac{dt}{dy}\\right|
$$
Tenemos $f_\\theta(t) = 1/\\pi$ y
$$
  tg(t) = \\frac{y-b}{a} \\implies t = atg\\left(\\frac{y-b}{a}\\right)
$$
$$
  \\implies \\frac{dt}{dy} = \\frac{a}{a^2 + (y-b)^2}
$$
$$
  \\implies f_Y(y) = \\frac{1}{\\pi}\\, \\frac{a}{a^2 + (y-b)^2}
$$

