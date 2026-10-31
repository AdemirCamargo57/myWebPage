---
title: Numerical Calculation of Atomic Forces
subject: Molecular dynamics
order: 10
description: Deriving atomic forces from central differences of the potential energy.
source: calculo_numerico_focas.docx
---

## Forces as energy derivatives

The force on an atom is the negative gradient of the potential energy. If $$\mathbf R$$ contains all atomic coordinates,

$$
F_{\alpha x}=-\frac{\partial E(\mathbf R)}{\partial x_\alpha}.
$$

To obtain a Cartesian force component numerically, displace only the corresponding coordinate, keeping all others fixed. Let $$\mathbf e_{\alpha x}$$ be the unit vector for that coordinate.

## Central difference derivation

Expanding the energy around $$\mathbf R$$,

$$
E(\mathbf R+h\mathbf e_{\alpha x})
=E(\mathbf R)+h\frac{\partial E}{\partial x_\alpha}
+\frac{h^2}{2}\frac{\partial^2E}{\partial x_\alpha^2}
+\frac{h^3}{6}\frac{\partial^3E}{\partial x_\alpha^3}+O(h^4),
$$

$$
E(\mathbf R-h\mathbf e_{\alpha x})
=E(\mathbf R)-h\frac{\partial E}{\partial x_\alpha}
+\frac{h^2}{2}\frac{\partial^2E}{\partial x_\alpha^2}
-\frac{h^3}{6}\frac{\partial^3E}{\partial x_\alpha^3}+O(h^4).
$$

Subtracting cancels the even-order terms:

$$
E(\mathbf R+h\mathbf e_{\alpha x})-E(\mathbf R-h\mathbf e_{\alpha x})
=2h\frac{\partial E}{\partial x_\alpha}+O(h^3).
$$

Thus,

$$
\boxed{
F_{\alpha x}\approx-
\frac{E(\mathbf R+h\mathbf e_{\alpha x})-E(\mathbf R-h\mathbf e_{\alpha x})}{2h}.
}
$$

The force approximation has an error of order $$h^2$$, because the cubic energy-difference remainder is divided by $$h$$. Repeat the calculation for the $$y$$ and $$z$$ components and for each atom.

## Practical interpretation

The finite difference is taken component by component; a quotient by a displacement vector is not a definition of a vector derivative. Energies at displaced geometries must be evaluated with consistent settings and sufficiently tight numerical convergence. Checking more than one displacement helps distinguish truncation error from numerical noise.
