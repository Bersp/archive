---
title: "Guía 2"
summary: "Guía 2 de MEFE"
math: true
---

{{< toc title="Lista de ejercicios">}}


# Ejercicio 6

## Enunciado
Al lanzarse un par de dados se espera que en promedio salga un doble seis cada 36 tiradas. Si se hacen sólo 25 tiradas, ¿conviene apostar a favor o en contra de la aparición de al menos un doble seis? (Rta: a favor, $P=0.5055$)

## Resolución
La probabilidad de que no aparezca nunca un doble $6$ es:
$$
  P = 1 - B(0\\,|\\,n=25, p=1/36) = 0.5055
$$

# Ejercicio 7
## Enunciado
Para determinar si un autroproclamado adivino es un trucho se lo somete a un test que consiste en disponer boca abajo sobre la mesa diez cartas de truco, 5 oros y 5 bastos, y pedirle que adivine cuáles son los cinco bastos. Encuentre la probabilidad de que acierte tres o más bastos por pura casualidad. (Rta: $P=0.5$).

## Resolución
$$
  P = \\sum_{k=3}^6 H(k|N=10,n=5,K=5) = 0.5
$$

# Ejercicio 8
## Enunciado
El $1\\%$ de una población tiene planeado votar un cierto candidato $A$.
Se realiza una encuesta tomando $n = 500$ habitantes al azar. ¿Cuál es la probabilidad de que el resultado de intención de voto para $A$ sea mayor o igual que el $2\\%$? Dicho de otra manera, ¿cuál es la probabilidad de que la encuesta se equivoque por más del 100%?
- a) Si el número de habitantes de la población es muchísimo mayor que $n$. (Rta: $P=0.0311$)
- b) Si hay $N = 5000$ habitantes en la población. (Rta: $P=0.0239$)
- c) ¿Cuántos habitantes $N$ debería haber en la población para que los resultados entre (a) y (b) tuvieran una diferencia relativa menor al 0.1%? (Rta: $N≃1.15 \\times 106$)

## Resolución

$$
  P(A) = 0.01
$$

## Punto a
Intención de voto de $2\\%$ implica $k=0.02\\times 500 = 10$
$$
  \\implies P = 1-\\sum_{k=0}^9 B(k|n=500, p=0.01) = 0.0311
$$

## Punto b
Si hay $N=5000$ habitantes, el $1\\%$ que tiene planeado votar a $A$ son $K=50$ personas.
$$
  \\implies P = 1-\\sum_{k=0}^9 H(k|N=5000, n=500, K=50) = 0.0239
$$

# Ejercicio 10
## Enunciado
En promedio Messi mete un gol el $18.2\\%$ de las veces que patea al arco.
- a) ¿Cuántas veces por partido debería patear para que la probabilidad de hacer al menos 2 goles sea mayor que el $0\\%$? (Rta: $20$ veces o más)
(Sugerencia: explorá numéricamente la solución de la ecuación trascendente)
- b) ¿Cuál es el número esperado de goles que haría si patea la cantidad de veces del ítem anterior? (Rta: $3.64$ goles)
- c) Si el técnico decide que va a sacarlo justo después de hacer el segundo gol, ¿cuál es el número esperado de veces que pateó? (Rta: $11$ veces)

## Resolución

## Punto a
$$
  1 - B(0, 20, 0.182) - B(1, 20, 0.182) \\simeq 0.902
$$
## Punto b
$$
  n\\times p = 20\\times 0.182 \\simeq 3.64
$$
### Punto c
La esperanza de la binomial negativa es $k/p =  2/0.182 \\simeq 11$.

# Ejercicio 11
## Enunciado
Una fuente radiactiva tiene una actividad de $4$ Bq (Becquerel = $1$ decaimiento $s^{-1}$).
Calcule la probabilidad de observar al menos un decaimiento en
- a) 1 segundo (Rta: $P=0.9817$)
- b) 2 segundos (Rta: $P=0.9997$)

## Resolución

$\\lambda = 4/s^{-1}$

## Punto a
$\\mu = \\lambda \\times 1s$
$$
	P(1, 4) \\simeq 0.9817
$$

## Punto a
$\\mu = \\lambda \\times 2s$
$$
	P(1, 8) \\simeq 0.9997
$$

# Ejercicio 12
## Enunciado
Para determinar la concentración $c$ de glóbulos blancos en sangre de un paciente, se toma una muestra de $1$ mm$^3$ de sangre y se cuentan los glóbulos presentes.
- a) Si se nos informa que $c = 4.05 \\text{nL}^{−1}$, ¿Cuál fue el error estadístico porcentual en la determinación de ese valor?
¿Qué hipótesis emplea? (Rta: $1.6\\%$)
- b) Resulta ser que la muestra que fue observada en el microscopio no era directamente la muestra extraída del paciente, sino que esta fue diluida $10$ veces para hacerla translúcida, y de esa nueva solución se extrajo $1$ mm$^3$ para examinar bajo el microscopio. ¿Cuál es entonces el error estadístico porcentual correcto para $c$? ¿Siguen
siendo válidas las hipótesis del inciso previo? (Rta: $4.9\\%$)

## Resolución

El error estadístico porcentual es $\\varepsilon = \\sigma/\\lang c\\rang$

## Punto a
$$
	c = 4.05\\,\\text{nL}^{-1} = 4050\\,\\text{mm}^{-3}
$$
- V.A.:  de glóbulos en la muestra
- En principio la dist es Binomial, pero como la probabilidad de agarrar un glóbulo es muy baja pero la probabilidad de intento $n \\propto V$ es muy alta, entonces $p\\to 0$ y $n\\to \\infty$. Lo que permite utilizar Poisson para este problema.
$$
	\\mu = c\\times 1\\text{mm}^3 = 4050
$$
$$
	\\sigma = \\sqrt{\\mu} = 63.64
$$
$$
	\\varepsilon = \\frac{\\sigma}{\\mu} = 0.0157 \\simeq 1.6\\%
$$

## Punto b
Al diluir $10$ veces la muestra, tenés, en promedio $10$ veces menos glóbulos:
$$
	\\varepsilon = \\frac{\\sqrt{405}}{405} \\simeq 4.9\\%
$$

# Ejercicio 14
## Enunciado
Una fuente de luz emite en promedio 100 fotones s$^{−1}$. Durante cuánto tiempo debería contarse fotones si se desea conocer la intensidad del haz con una precisión de $1/1000$. (Rta: 2.77 hs)
Nota: use como "precisión" el cociente $\\varepsilon = \\sigma/\\mu$.

## Resolución

$$
	\\lambda = 100/\\text{sec}
$$
$$
	\\implies \\mu = 100/\\text{sec} \\times t
$$
$$
	\\frac{\\sqrt{100\\times t}}{100\\times t} = \\frac{1}{10\\sqrt{t}} = \\frac{1}{1000}
$$
$$
	\\implies t = 1000 \\sec \\simeq 2.77\\text{hs}
$$

# Ejercicio 15
## Enunciado
Una astrónoma quiere mejorar una antigua determinación del período de un pulsar $\\tau \\pm \\sigma \\tau /\\sqrt{n}$ , hecha a partir de $n = 25$ mediciones exitosas.
Se sabe que por fluctuaciones en la polución de la atmósfera el $20\\%$ de las pulsaciones deberán ser descartadas luego de evaluar su calidad.
Si la astrónoma quiere que la nueva determinación de $\\tau$ sea el doble de precisa que la anterior,
- a) ¿Cuántas observaciones exitosas (no afectadas por la atmósfera) son necesarias? (Rta: $n = 100$)
- b) ¿Cuál es la probabilidad de que necesite realizar 130 o más observaciones en total (tanto exitosas como afectadas)
- ara alcanzar el grado de precisi´on deseada? (Rta: p = 0.206)
- c) ¿Cuántas observaciones totales debería planificar si quiere que la probabilidad de obtener la precisión deseada (o una incluso mejor) sea mayor al $99\\%$? (Rta: por lo menos $139$ mediciones)

## Resolución

$$
	n_e = 25 \\text{ existosas}
$$
## Punto a
Quiere tomar $m_e$ mediciones de modo tal que el error sea la mitad que antes:
$$\\frac{\\sigma_\\tau}{\\sqrt{m_e}} = \\frac{1}{2} \\frac{\\sigma_\\tau}{\\sqrt{n_e}} \\implies m_e 2^2 n_e = 4n_e$$
$$
	\\implies m_e = 100
$$

## Punto b
- V. A.: # de observaciones totales $n$
- Distribución Binomial Negativa con $k=100$ mediciones exitosas y probabilidad de mediciones exitosas $p = 1-0.2 = 0.8$
$$
	\\begin{align*}
		P &= B_n(n\\geq 130|k=100, p=0.8) = 1-B_n(n < 130|k=100, p=0.8) \\\\
		&= 1 - \\sum_{n=0}^{121} B_n(n|k=100, p=0.8)
	\\end{align*}
$$
$$
	\\implies P(n \\geq 130) = 0.205
$$

### Punto c
Quiero $n$ tal que haya una probabilidad mayor al $99\\%$ de tener $k\\geq 100$ observaciones existosas.
$$
	B(k \\geq 100 | n, p) = 1- \\sum_{k=0}^{99} B(k|n, p=0.8) \\geq 0.99
$$
$$
	\\implies n = 139
$$

