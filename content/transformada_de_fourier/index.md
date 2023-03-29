---
title: "Transformadas de Fourier discretas"
date: 2023-02-01
summary: "DFT, FFT y por qué en realidad deberían llamarse Series de Fourier discretas."
math: true
draft: true
---

# Introducción
$$
	F(k) = \int_{-\infty}^\infty f(x)~e^{-2\pi i k x}~\text{d}x,\quad f(x) = \int_{-\infty}^\infty f(k)~e^{-2\pi i k x}~\text{d}k,\quad
$$

$$
	F(k_m) = \sum_{x_n=0}^{N-1} f(x_n)\\,e^{-2\pi i x_n k_m}
$$
Si los puntos están equiespaciados una distancia $\Delta x$, entonces $x_n = n \Delta x$. Si el primer dato no está en el origen ($x_0 = 0$) da igual porque una traslación solo agrega una fase en la transformada de Fourier.
Ahora, las frecuencia fundamental, osea, el valor más chico de espacio que podemos diferenciar, es $\frac{1}{N \Delta x}$.
Como los puntos están equiespaciados todas las demás van a ser múltiplo de la fundamental, osea $k_m = \frac{m}{N \Delta x}$ ($k_0 = 0$ nos da el modo traslacional). Reemplazando,
$$
	\boxed{F(k_m) = Y_m = \sum_{n=0}^{N-1} y_n\\,e^{-2\pi i \frac{nm}{N}}},
$$
y realizando el mismo proceso para la antitransformada obtenemos
$$
	\boxed{f(x_n) = y_n = \sum_{m=0}^{N-1} Y_m\\,e^{2\pi i \frac{nm}{N}}}.
$$

{{< fig src="figures/DFT_intro.png" width="100%" >}}

# No olviar

- Por qué FFT es el algortimo más importante de la tecnología moderna.
- Hablar sobre otras aplicaciones.

