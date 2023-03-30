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
  \\Omega = \\{ (C_1, C_2) ~/~ C_{1,2} := 1, 2, ..., 40 \\land C_1 \\neq C_2 \\}; \\qquad\\#\\Omega = 40\\times39
$$
$$
  \\omega = \\{ (1, C), (C, 1) ~/~ C := 2, ..., 40 \\}; \\qquad \\#\\omega = 2\\times39
$$
$$
  \\implies P = \\frac{\\#\\omega}{\\#\\Omega} = 1/20 = 0.05
$$

### Punto c
$$
  \\Omega = \\{ (C_1, C_2) ~/~ C_{1,2} := 1, 2, ..., 80 \\land C_1 \\neq C_2 \\}; \\qquad\\#\\Omega = 80\\times79
$$
$$
  \\omega = \\{ (1A, C), (C, 1A), (1R, C), (C, 1R), (1A, 1R), (1R, 1A) ~/~ C = 3, ..., 80\\}, \\quad \\#\\omega = 4\\times78 + 2
$$
$$
  \\implies P = \\frac{\\#\\omega}{\\#\\Omega} \\simeq 0.049683
$$

#### Otra forma de resolverlo
Calculemos la probabilidad de que no ocurra. $\\Omega$ es el mismo.
$$
  \\omega= \\{ (C_1, C_2) ~/~ C_{1,2} = 3, ..., 80 \\}, \\qquad \\#\\omega = 78\\times77
$$
$$
  \\implies \\tilde P = \\frac{78}{80} \\times \\frac{77}{79} \\simeq 0.0950316;\\qquad P = 1-\\tilde P \\simeq 0.049683
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
	\\omega = \\{ (1, 2); (100, 99) \\} \\cup \\{ (M, M+1), (M, M-1) / M:= 2, \\dots, 99 \\} \\quad \\#\\omega = 2\\times98 + 2
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

Usando la fórmula de la [probabilidad condicional](hl8v#probabilidad-condicional).
$$
	P(v_{15}|v_1\\cap v_2 \\dots \\cap v_{14}) = \\frac{P(v_1\\cap v_2 \\dots \\cap v_{15})}{P(v_1\\cap v_2 \\dots \\cap v_{14})} = \\frac{\\left(1/2\\right)^{15}}{\\left(1/2\\right)^{14}} = 1/2
$$
lo cual es evidente porque son independientes.

