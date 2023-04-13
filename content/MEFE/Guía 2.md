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

### Punto a
Intención de voto de $2\\%$ implica $k=0.02\\times 500 = 10$
$$
  \\implies P = 1-\\sum_{k=0}^9 B(k|n=500, p=0.01) = 0.0311
$$

### Punto b
Si hay $N=5000$ habitantes, el $1\\%$ que tiene planeado votar a $A$ son $K=50$ personas.
$$
  \\implies P = 1-\\sum_{k=0}^9 H(k|N=5000, n=500, K=50) = 0.0239
$$

# Problema 10
## Enunciado
En promedio Messi mete un gol el $18.2\\%$ de las veces que patea al arco.
- a) ¿Cuántas veces por partido debería patear para que la probabilidad de hacer al menos 2 goles sea mayor que el $0\\%$? (Rta: $20$ veces o más)
(Sugerencia: explorá numéricamente la solución de la ecuación trascendente)
- b) ¿Cuál es el número esperado de goles que haría si patea la cantidad de veces del ítem anterior? (Rta: $3.64$ goles)
- c) Si el técnico decide que va a sacarlo justo después de hacer el segundo gol, ¿cuál es el número esperado de veces que pateó? (Rta: $11$ veces)

## Resolución
### Punto a
$$
  1 - B(0, 20, 0.182) - B(1, 20, 0.182) \\simeq 0.902
$$
### Punto b
$$
  n\\times p = 20\\times 0.182 \\simeq 3.64
$$

