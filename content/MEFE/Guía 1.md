---
title: "Guía 1"
summary: "Guía 1 de MEFE"
math: true
---


# Ejercicios
- [Ejercicio 7](#ejercicio-7)
- [Ejercicio 8](#ejercicio-8)
- [Ejercicio 9](#ejercicio-9)
- [Ejercicio 11](#ejercicio-11)
- [Ejercicio 12](#ejercicio-12)

# Ejercicio 7

## Enunciado
¿Cuándo es más probable obtener al menos un as de espadas?
- a) al extraer dos cartas de un mismo mazo de truco (que consta de 40 cartas) (Rta: $P = 0.05$),
- b) al extraerlas de dos mazos, una carta de cada mazo (Rta: $P = 0.049375$),
- c) Se mezclan dos mazos y se extraen dos cartas (Rta: $P = 0.049683$),
- d) Encuentre el espacio muestral e identifique los sucesos mencionados.

## Resolución
### Punto a
$$
  \\Omega = \\{ (C_1, C_2) ~/~ C_{1,2} := 1, 2, ..., 40 \\land C_1 \\neq C_2 \\}\\\\
	\\#\\Omega = 40\\times39
$$
$$
  \\omega = \\{ (1, C), (C, 1) ~/~ C := 2, ..., 40 \\}\\\\
	\\#\\omega = 2\\times39
$$
$$
  \\implies P = \\frac{\\#\\omega}{\\#\\Omega} = 1/20 = 0.05
$$

### Punto c
$$
  \\Omega = \\{ (C_1, C_2) ~/~ C_{1,2} := 1, 2, ..., 80 \\land C_1 \\neq C_2 \\}\\\\
	\\#\\Omega = 80\\times79
$$
$$
  \\omega = \\{ (1A, C), (C, 1A), (1R, C), (C, 1R), (1A, 1R), (1R, 1A) ~/~ C = 3, ..., 80\\}\\\\ \\#\\omega = 4\\times78 + 2
$$
$$
  \\implies P = \\frac{\\#\\omega}{\\#\\Omega} \\simeq 0.049683
$$

#### Otra forma de resolverlo
Calculemos la probabilidad de que no ocurra. $\\Omega$ es el mismo.
$$
  \\omega= \\{ (C_1, C_2) ~/~ C_{1,2} = 3, ..., 80 \\}\\\\
	\\#\\omega = 78\\times77
$$
$$
	\\begin{align*}
  \\implies
		\\tilde P &= \\frac{78}{80} \\times \\frac{77}{79} \\simeq 0.0950316\\\\
					 P &= 1-\\tilde P \\simeq 0.049683
	\\end{align*}
$$

# Ejercicio 8

## Enunciado
Entre los números del 1 al 100 se eligen dos al azar. Encuentre la probabilidad de que sean consecutivos si se los elige,
- a) sin reposición (Rta: $P = 0.02$),
- b) con reposición (Rta: $P = 0.0198$),
- c) Encuentre el espacio muestral en cada caso e identifique los sucesos mencionados.

## Resolución
### Punto a
$$
	\\#\\Omega = 100\\times99\\\\
	\\omega = \\{ (1, 2); (100, 99) \\} \\cup \\{ (M, M+1), (M, M-1) / M:= 2, \\dots, 99 \\}\\\\ \\#\\omega = 2\\times98 + 2
$$
$$
	P = \\frac{\\#\\Omega}{\\#\\omega} = 0.02
$$
### Punto b
$$
	\\#\\Omega = 100\\times100
$$
el $\\omega$ es el mismo que en el punto anterior
$$
	P = \\frac{\\#\\Omega}{\\#\\omega} = 0.0198
$$


# Ejercicio 9

## Enunciado
Se tiran dos dados. Calcule la probabilidad de que:
- a) no salga ningún as (Rta: $P = 25/36$),
- b) no salga ningún as y ningún seis. (Rta: $P = 16/36$)

## Resolución
### Punto a
$$
	P = \\frac{5}{6}\\times\\frac{5}{6} = \\frac{25}{36}
$$

### Punto b
$$
	P = \\frac{4}{6}\\times\\frac{4}{6} = \\frac{16}{36}
$$

# Ejercicio 11
## Enunciado
Considere un partido de truco entre cuatro jugadores que dura 15 manos. Encuentre la probabilidad de que:
- a) a un dado jugador nunca le toque el ancho de espadas (Rta: $P = 0.31$),
- b) el as de espadas no salga en todo el partido (Rta: $P = 0.0047$).

### Punto a
$$
	P = \\left(\\frac{40-3}{40}\\right)^{15} = 0.310546...
$$

### Punto b
$$
	P = \\left(\\frac{40-3\\times4}{40}\\right)^{15} = 0.004747...
$$

# Ejercicio 12
## Enunciado
Una moneda no cargada se lanza 15 veces. ¿Cuál es la probabilidad de que en la última tirada se obtenga cara, sabiendo que en las primeras catorce tiradas salió ceca?

## Resolución
- $v_n$: salió cara (verso) en la tirada $n$-ésima
- $r_n$: salió ceca (reverso) en la tirada $n$-ésima

Usando la fórmula de la probabilidad condicional.
$$
	P(v_{15}|v_1\\cap v_2 \\dots \\cap v_{14}) = \\frac{P(v_1\\cap v_2 \\dots \\cap v_{15})}{P(v_1\\cap v_2 \\dots \\cap v_{14})} = \\frac{\\left(1/2\\right)^{15}}{\\left(1/2\\right)^{14}} = 1/2
$$
lo cual es evidente porque son independientes.

# Ejercicio 13

## Enunciado
Una urna $U_a$ tiene $7$ bolas blancas y $3$ negras, y otra urna $U_b$, $5$ blancas y $5$ negras. Se extrae al azar una bola de $U_a$ y se la coloca en $U_b$. A continuación se extrae al azar una bola de $U_b$. Encuentre la probabilidad de que:
- a) ambas bolas extraídas sean negras (Rta: $P = 9/55$),
- b) al menos una bola extraída sea negra (Rta: $P = 34/55$),
- c) exactamente una bola extraída sea negra (Rta: $P = 5/11$),
- d) Verifique que se cumple: $P(b) = P(a)+P(c)$ y discuta cuál sería el error conceptual en pensar que $P(c) = 2P(a)$ y por lo tanto $P(b) = P(c) + P(c) − P(a)$. Recuerde que $P(A \\cup B) = P(A) + P(B) − P(A \\cap B)$.

## Resolución
- $A_n$: extraigo una bola negra de $U_a$ y la pongo en $U_b$
- $A_n$: extraigo una bola negra de $U_b$
- $A_b$: extraigo una bola blanca de $U_a$ y la pongo en $U_b$
- $A_b$: extraigo una bola blanca de $U_b$

### Punto a
$$
	P(\\text{punto a}) = P(A_n) \\times P(B_n | A_n) = \\frac{3}{10} \\times\\frac{6}{11} = \\frac{9}{55}
$$

### Punto b
$$
\\begin{align*}
	P(\\text{punto b})
	&= P(A_n) \\times P(B_n | A_n) + P(A_b)\\times P(B_n | A_b) + P(A_n)\\times P(B_b | A_n) \\\\
	&=
	\\frac{3}{10} \\times\\frac{6}{11} +
	\\frac{7}{10} \\times\\frac{5}{11} +
	\\frac{3}{10} \\times\\frac{5}{11} = \\frac{34}{55}
\\end{align*}
$$

### Punto c
$$
\\begin{align*}
	P(\\text{punto c})
	&= P(A_b)\\times P(B_n | A_b) + P(A_n)\\times P(B_b | A_n)\\\\
	&=\\frac{7}{10} \\times\\frac{5}{11} +
	\\frac{3}{10} \\times\\frac{5}{11} = \\frac{5}{11}
\\end{align*}
$$

### Punto d
Comparando con los resultados de arriba es evidente que
$$
	P(\\text{punto b}) = P(\\text{punto a}) + P(\\text{punto c})
$$

# Ejercicio 14

## Enunciado
Un dado se fabrica de modo que la probabilidad de sacar un numéro es proporcional al mismo. Calcule:
- a) la probabilidad de obtener un 2 (Rta: $P=2/21$)
- b) la probabilidad de haber obtenido un 2 dado que se obtuvo un número par (Rta: $P=1/6$)

## Resolución

$$
\\begin{align*}
	P(1) &= \\alpha \\\\
	P(2) &= 2\\alpha \\\\
	&~~\\vdots \\\\
	P(6) &= 6\\alpha \\\\
\\end{align*}
$$
### Punto a

$$
1 = \\sum_{i=1}^6 P(i) = (6+5+\\dots+1)\\,\\alpha = 21\\alpha \\\\
\\implies \\alpha = \\frac{1}{21}
$$
$$
	\\implies P(2) = 2\\alpha = \\frac{2}{21}
$$

### Punto b
Si ya sabemos que el resultado es par, la probabilidad de sacar un $2, 4$ o $6$ tiene que sumar $1$, porque completan el espacio muestral. Esto es
$$
	1 = P(2|\\text{par}) + P(4|\\text{par}) + P(6|\\text{par}) = 12\\alpha\\\\\\implies \\alpha = \\frac{1}{12} \\\\
$$
$$
	\\implies P(2|\\text{par}) = 2\\alpha = \\frac{1}{6}
$$

# Ejercicio 15

## Enunciado
Se tira un par de dados, obteniéndose $a$ y $b$ como resultado. Considere los siguientes sucesos:
- $A = \\{a \\text{ es impar}\\}$,
- $B = \\{b \\text{ es impar}\\}$,
- $C = \\{a+b \\text{ es impar}\\}$
- $D = \\{\\text{al menos } a \\text{ o } b \\text{ es múltiplo de } 3\\}$.

Consignas:
- a) Muestre que $A, B$ y $C$ no son independientes, aunque sí son independientes de a pares.
- b) ¿Son independientes $C$ y $D$?

## Resolución
Dos eventos son independientes si $P(\\beta|\\alpha) = P(\\beta)$ y $P(\\alpha|\\beta) = P(\\alpha) \\iff P(\\beta|\\alpha) = P(\\beta)$.

$$A = \\{a \\text{ es impar}\\} = \\{(1, b); (3, b); (5, b)\\}$$
$$B = \\{b \\text{ es impar}\\} = \\{(a, 1); (a, 3); (a, 5)\\}$$
$$
	C = \\{a+b \\text{ es impar}\\} = \\text{muchas combinaciones}
$$
$$
	D = \\{\\text{al menos } a \\text{ o } b \\text{ es múltiplo de } 3\\}
	= \\{ (3, b); (6, b); (a, 3); (a, 6) \\}
$$
$$
	\\Omega = \\{ (a, b) / a,b = 1, 2, \\dots, 6 \\},~~\\#\\Omega=6^2=36
$$

### Punto a
$$
	\\#A = \\#B = 3\\times 6 = 18\\\\
	P(A) = P(B) = 18/36 = 1/2
$$
$$
	A \\cap B = \\{ (1,1); (1,3); (1,5); (3,1); (3,3); (3,5); (5,1); (5,3); (5,5)\\} \\\\
	\\# (A \\cap B) = 9 \\implies P(A \\cap B) = 9/36
$$

$$
	P(A|B) = \\frac{P(A\\cap B)}{P(B)} = 9/18 = 1/2 = P(A)
$$

Y así con todos...

