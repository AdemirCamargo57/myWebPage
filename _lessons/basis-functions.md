---
title: Basis Functions in Quantum Chemistry
subject: Quantum chemistry
order: 20
description: Slater and Gaussian functions, contractions, split-valence bases, polarization, and diffuse functions.
source: funcoes_base.docx
---

## Expanding molecular orbitals

In a finite-basis electronic structure calculation, a molecular orbital is expanded as a linear combination of basis functions:

$$
\psi_p(\mathbf r)=\sum_\mu C_{\mu p}\chi_\mu(\mathbf r).
$$

The basis functions are mathematical building blocks. Atom-centered Slater-type and Gaussian-type functions are common in molecular calculations; plane waves are another important choice, especially for periodic systems.

## Slater-type functions

A Cartesian Slater-type function centered at the origin can be written in the form

$$
\chi^{\mathrm{STO}}_{pqs}(\zeta,x,y,z)
=Nx^py^qz^s e^{-\zeta r},\qquad r=\sqrt{x^2+y^2+z^2}.
$$

Here $$N$$ normalizes the function, $$p,q,s$$ are nonnegative integers, and $$\zeta>0$$ controls its radial extent. Larger exponents produce more compact functions; smaller exponents give more diffuse functions. More general Slater functions include additional radial powers and spherical harmonics.

The total Cartesian angular degree is $$l=p+q+s$$. Examples of polynomial factors are:

| Shell | Cartesian factors |
| --- | --- |
| s | $$1$$ |
| p | $$x,y,z$$ |
| d | $$xy,xz,yz,x^2,y^2,z^2$$ |

Five pure spherical d functions can be formed from suitable combinations, such as $$xy,xz,yz,x^2-y^2,2z^2-x^2-y^2$$. Six Cartesian d functions contain the five-dimensional d space plus an additional component. Therefore software options using five or six d functions change the basis and its function count.

Slater functions have physically useful radial behavior, but multicenter molecular integrals are more difficult to evaluate than the corresponding Gaussian integrals.

## Gaussian-type functions

A Cartesian Gaussian centered at atom $$A$$ is

$$
\chi^{\mathrm{GTO}}_{pqs}(\alpha,\mathbf r)
=N(x-X_A)^p(y-Y_A)^q(z-Z_A)^s
e^{-\alpha|\mathbf r-\mathbf R_A|^2}.
$$

The exponent $$\alpha>0$$ controls the width. Gaussian functions make molecular integrals computationally efficient, but a single Gaussian does not reproduce the near-nucleus cusp or the long-range decay of a Slater function.

## Contracted Gaussians and STO-nG

A contracted Gaussian is a fixed linear combination of primitives:

$$
\chi_\mu^{\mathrm{CGTO}}(\mathbf r)
=\sum_{k=1}^{K}d_{\mu k}\,
\chi_{\mu k}^{\mathrm{GTO}}(\alpha_{\mu k},\mathbf r).
$$

The contraction coefficients and exponents are usually supplied by the chosen basis set. The electronic structure calculation determines coefficients multiplying the contracted functions, rather than independently optimizing each primitive coefficient.

In an STO-nG basis, $$n$$ Gaussian primitives approximate each Slater-like function. For example,

$$
\chi^{\mathrm{STO\text{-}3G}}\approx\sum_{k=1}^{3}d_k\chi_k^{\mathrm{GTO}},
\qquad
\chi^{\mathrm{STO\text{-}6G}}\approx\sum_{k=1}^{6}d_k\chi_k^{\mathrm{GTO}}.
$$

These are finite Gaussian approximations, not exact equalities to Slater functions.

## Basis-set size

- A **minimal basis** provides one basis function for each atomic orbital needed in the conventional minimal atomic description.
- A **double-zeta** basis provides two radial functions per represented orbital.
- **Triple-, quadruple-, and quintuple-zeta** bases provide three, four, and five radial functions, respectively.
- A **split-valence** basis uses more radial flexibility in the valence shell than in the core.

For hydrogen, a minimal basis has one s function. For carbon, the conventional minimal set contains $$1s,2s,2p_x,2p_y,2p_z$$: five functions. An individual molecular orbital can be expanded in these five functions; the many-electron wavefunction is constructed from occupied orbitals and is not itself just this one-electron expansion.

For carbon, an all-electron double-zeta set with two radial functions for each of those five orbitals has ten functions. A double-zeta split-valence set has one core s function and two functions for each of the four valence orbitals, giving

$$
1+2(1+3)=9
$$

basis functions.

## Pople split-valence notation

The notation $$N\text{-}n_1n_2\mathrm G$$ describes a core contraction of $$N$$ primitives and a valence shell split into contractions of $$n_1$$ and $$n_2$$ primitives.

For example, carbon in **6-31G** has:

- one core s contraction containing six primitives;
- one valence s contraction and three valence p contractions, each containing three primitives;
- a second valence s function and three valence p functions, each containing one primitive.

There are nine contracted spatial functions. Counting primitives separately for every Cartesian component gives

$$
6+4(3)+4(1)=22.
$$

Schematically, a molecular orbital expressed in this carbon-centered basis is

$$
\psi=C_c\chi_{1s}^{(6)}
+\sum_{\mu\in\{s,p_x,p_y,p_z\}}
\left[C_{\mu,1}\chi_\mu^{(3)}
+C_{\mu,2}\chi_\mu^{(1)}\right].
$$

In **6-311G**, the valence space is split into three radial parts: contractions of three, one, and one primitive. Carbon then has

$$
1+3(4)=13
$$

contracted functions, and $$6+4(3)+4+4=26$$ primitives when counted by Cartesian component.

## Polarization functions

Polarization functions add angular flexibility. For hydrogen, adding p functions allows the electron density to depart from a purely s-like shape. For carbon, adding d functions provides angular flexibility beyond the occupied atomic p shell.

For example, **6-31G(d)** adds a d shell on heavy atoms. **6-31G(d,p)** adds d functions on heavy atoms and p functions on hydrogen. The five-versus-six d-function convention must be stated when counting the functions.

## Diffuse functions

Diffuse functions have small exponents and extend farther from the nuclei. They are useful when the density is spatially extended, as in many anions, weakly bound states, and some excited states.

In Pople notation:

- **+** adds diffuse functions to heavy atoms.
- **++** also adds diffuse functions to hydrogen.
- Parenthetical angular labels, such as **(d,p)**, specify polarization functions separately.

For carbon in **6-31+G(d)**, the nine 6-31G functions are supplemented by four diffuse functions (one s and three p) and a d shell. With six Cartesian d functions, the total is

$$
9+4+6=19
$$

contracted functions. With five spherical d functions, it is eighteen. If each added diffuse and Cartesian polarization function is uncontracted, the primitive count by Cartesian component is $$22+4+6=32$$.

## Interpreting a calculation

When reporting a basis, include the complete name and relevant angular-function conventions. Increasing basis size gives more variational flexibility, but the physical result also depends on the electronic structure method. Check convergence for the property of interest rather than relying only on the name or nominal size of a basis.
