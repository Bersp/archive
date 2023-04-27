---
title: "Guía 4"
summary: "Guía 4 de MEFE"
math: true
---

{{< toc title="Lista de ejercicios">}}


# Ejercicio 3

## Enunciado
Muestre que el cociente $Z \\equiv X/Y$ de dos variables independientes con distribución normal canónica tiene distribución de Cauchy, $f_Z(t) = 1/[\\pi(1 + t^2 )]$.

## Resolución
Tomo $U, V$ adecuadamente
$$
  U = X/Y, \\quad V = X^2 + Y^2
$$
$$
  f_{XY}(x,y)\\,dx dy = g_{UV}(u,v)\\,du dv
$$
$$
  \\left|\\frac{dxdy}{dudv}\\right| = 2\\,(1 + {\\,x^2\\over y^2}) 
$$
$$
  \\implies
  \\left|\\frac{dxdy}{dudv}\\right| = \\frac{1}{2\\,(1 + {\\,x^2\\over y^2})} 
$$

En este caso la que queremos es $g_U(u)$:
$$
\\begin{align*}
g_U(u)
&= \\int_{-\\infty}^{\\infty} dv~\\frac{1}{2\\pi} e^{-v/2} \\times \\frac{1}{2\\,(1 + {\\,x^2\\over y^2})} \\\\
&= \\int_{0}^{\\infty} dv~\\frac{1}{\\pi} e^{-v/2} \\times \\frac{1}{2\\,(1 + {\\,x^2\\over y^2})} \\\\
&= \\frac{-2}{\\pi} e^{-v/2}\\Big|_0^\\infty \\times \\frac{1}{2\\,(1 + {\\,x^2\\over y^2})} \\\\
&= \\frac{2}{\\pi}  \\times \\frac{1}{2\\,(1 + {\\,x^2\\over y^2})} \\\\
&= \\frac{1}{\\pi\\,(1 + {\\,x^2\\over y^2})} \\\\
\\end{align*}
$$


