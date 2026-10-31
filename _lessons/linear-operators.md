---
title: Linear Operators and Matrix Representations
subject: Mathematical foundations
order: 40
description: Operators in Dirac notation, adjoints, unitary changes of basis, and eigenvalue properties.
source: Operador_linear.docx
---

## Operators and linearity

An operator $$\hat O:E\to E$$ maps a vector to another vector in the same space:

$$
\hat O|a\rangle=|b\rangle.
$$

In a chosen finite-dimensional basis, kets are column vectors, bras are row vectors, and operators are matrices. Matrix multiplication therefore determines the order of the factors. Expressions such as $$|a\rangle\hat O$$ or $$\hat O\langle a|$$ are not ordinary matrix products with these dimensions. Similarly, multiplying two columns is not an inner product. The valid products include the scalar $$\langle a|b\rangle$$ and the operator $$|a\rangle\langle b|$$.

A linear operator satisfies

$$
\hat O(\alpha|a\rangle+\beta|b\rangle)
=\alpha\hat O|a\rangle+\beta\hat O|b\rangle.
$$

Differentiation is linear:

$$
\frac{d}{dx}[\alpha f(x)+\beta g(x)]
=\alpha f'(x)+\beta g'(x).
$$

Integration over fixed limits is also linear. By contrast, taking the square root is not a linear operation: in general $$\sqrt{\alpha f+\beta g}\ne\alpha\sqrt f+\beta\sqrt g$$.

## Building an operator matrix

The action on a basis determines a linear operator. For example, let

$$
|a\rangle=\begin{pmatrix}1\\0\end{pmatrix},\qquad
|b\rangle=\begin{pmatrix}0\\1\end{pmatrix},
$$

and suppose $$\hat O|a\rangle=|b\rangle$$ and $$\hat O|b\rangle=|a\rangle$$. The columns of the matrix are the images of the basis vectors, so

$$
O=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

More generally, insert the identity $$\hat I=\sum_i|i\rangle\langle i|$$ on both sides of the operator:

$$
\boxed{\hat O=\sum_{i,j}|i\rangle O_{ij}\langle j|,
\qquad O_{ij}=\langle i|\hat O|j\rangle.}
$$

For $$|a\rangle=\sum_j a_j|j\rangle$$, the resulting vector has components

$$
b_i=\sum_j O_{ij}a_j.
$$

The outer product $$|i\rangle\langle j|$$ is a matrix with one unit entry in row $$i$$, column $$j$$. Summing these matrices with coefficients $$O_{ij}$$ reconstructs the usual operator matrix.

A bra can also multiply an operator on the right. However, if $$\hat O|a\rangle=|b\rangle$$, taking the adjoint gives $$\langle a|\hat O^\dagger=\langle b|$$, not generally $$\langle a|\hat O=\langle b|$$.

## Transpose, complex conjugate, and adjoint

In a fixed orthonormal basis,

$$
\begin{aligned}
O^{\mathsf T}_{ij}&=O_{ji},\\
(O^*)_{ij}&=O_{ij}^*,\\
(O^\dagger)_{ij}&=O_{ji}^*.
\end{aligned}
$$

Thus,

$$
O^{\mathsf T}=\sum_{ij}O_{ji}|i\rangle\langle j|
=\sum_{ij}O_{ij}|j\rangle\langle i|.
$$

Exchange either the coefficient indices or the outer-product indices when writing the transpose, not both simultaneously.

The adjoint satisfies

$$
\langle a|\hat O b\rangle=\langle\hat O^\dagger a|b\rangle.
$$

Useful identities include

$$
(AB)^\dagger=B^\dagger A^\dagger,\qquad
(cA)^\dagger=c^*A^\dagger,\qquad
(A^\dagger)^\dagger=A.
$$

## Hermitian and anti-Hermitian operators

An operator is **Hermitian** if $$O=O^\dagger$$, and **anti-Hermitian** if $$O=-O^\dagger$$. In finite-dimensional spaces, Hermitian and self-adjoint mean the same thing. In infinite-dimensional spaces, domains must also be specified before identifying symmetry with self-adjointness.

The Pauli matrices are Hermitian:

$$
\sigma_x=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
\sigma_y=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad
\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

Multiplying any Hermitian matrix by $$i$$ gives an anti-Hermitian matrix.

For wavefunctions, Hermiticity is tested through the inner product. The familiar Hamiltonian

$$
\hat H=-\frac{\hbar^2}{2m}\frac{d^2}{dx^2}+V(x)
$$

with real $$V$$ has the expected symmetry when integration by parts produces no boundary terms. The boundary conditions and operator domain are essential parts of this statement.

## Changing an orthonormal basis

Let $$\{|i\rangle\}$$ and $$\{|\alpha\rangle\}$$ be complete orthonormal bases. Define

$$
U_{i\alpha}=\langle i|\alpha\rangle,
\qquad |\alpha\rangle=\sum_i|i\rangle U_{i\alpha}.
$$

Orthonormality and completeness imply

$$
U^\dagger U=UU^\dagger=I,
\qquad U^{-1}=U^\dagger.
$$

If $$O$$ represents the operator in the first basis and $$\Omega$$ represents it in the second,

$$
\begin{aligned}
\Omega_{\alpha\beta}
&=\langle\alpha|\hat O|\beta\rangle
=\sum_{ij}U_{i\alpha}^*O_{ij}U_{j\beta},\\
\Omega&=U^\dagger O U,\qquad O=U\Omega U^\dagger.
\end{aligned}
$$

This is a unitary change of basis. Every finite-dimensional Hermitian matrix can be diagonalized in an orthonormal eigenbasis.

## Eigenvalues and eigenvectors

An eigenvector is a nonzero vector satisfying

$$
\hat O|\alpha\rangle=\omega_\alpha|\alpha\rangle.
$$

The operator changes its magnitude or phase but not its direction. Taking the adjoint gives

$$
\langle\alpha|\hat O^\dagger
=\omega_\alpha^*\langle\alpha|.
$$

### Real expectation values

For a Hermitian operator and a normalized state,

$$
\langle\psi|\hat O|\psi\rangle^*
=\langle\psi|\hat O^\dagger|\psi\rangle
=\langle\psi|\hat O|\psi\rangle.
$$

Therefore its expectation value is real. For an unnormalized state, divide the numerator by $$\langle\psi|\psi\rangle$$.

### Real eigenvalues

For a nonzero eigenvector of a Hermitian operator,

$$
(\omega_\alpha-\omega_\alpha^*)
\langle\alpha|\alpha\rangle=0.
$$

Positive definiteness gives $$\langle\alpha|\alpha\rangle>0$$, hence $$\omega_\alpha=\omega_\alpha^*$$.

### Orthogonality of distinct eigenvalues

For two eigenvectors of a Hermitian operator,

$$
(\omega_\alpha-\omega_\beta)
\langle\beta|\alpha\rangle=0.
$$

If the eigenvalues differ, the eigenvectors are orthogonal. Within a degenerate eigenspace, eigenvectors can be chosen orthonormal, but two arbitrary eigenvectors with the same eigenvalue need not already be orthogonal.
