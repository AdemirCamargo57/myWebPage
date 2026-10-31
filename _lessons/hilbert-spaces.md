---
title: Hilbert Spaces
subject: Mathematical foundations
order: 30
description: Completeness, separability, square-integrable functions, and the quantum mechanical state space.
source: Espaco_Hilbert.docx
---

## What is a Hilbert space?

A Hilbert space is a vector space equipped with an inner product that is complete with respect to the norm induced by that inner product. It therefore has all the properties of a vector space, together with a notion of length, angle, and convergence.

If the inner product is denoted by $$\langle u,v\rangle$$, the induced norm is

$$
\|u\|=\sqrt{\langle u,u\rangle}.
$$

Completeness means that limits suggested by the geometry of the space remain inside the space: every Cauchy sequence converges to an element of the same space.

## Separability

A space is **separable** if it contains a countable dense subset. A set is countable if it is finite or can be put into one-to-one correspondence with a subset of the natural numbers. A countably infinite set has the same cardinality as $$\mathbb N$$.

A subset $$A$$ is dense in a space $$M$$ when its closure is the whole space:

$$
\overline A=M.
$$

The closure contains both the points of $$A$$ and all its limit points. Thus, every point in $$M$$ can be approximated arbitrarily closely by points in $$A$$.

Many Hilbert spaces used in quantum mechanics are separable. Separability is an additional property; it is not part of the general definition of a Hilbert space.

## Cauchy sequences and completeness

A sequence $$(a_n)$$ is Cauchy if

$$
\forall\epsilon>0,\quad\exists N\in\mathbb N
\quad\text{such that}\quad m,n\geq N
\Longrightarrow\|a_m-a_n\|<\epsilon.
$$

The condition involves **any two sufficiently late terms**, not only consecutive terms. In a complete space, there is an element $$a$$ such that $$\|a_n-a\|\to0$$.

## Finite- and infinite-dimensional examples

The spaces $$\mathbb R^n$$ and $$\mathbb C^n$$, with their usual inner products, are finite-dimensional Hilbert spaces.

An important infinite-dimensional example is $$L^2(\mathbb R)$$, the space of square-integrable complex-valued functions, understood up to equality almost everywhere. Its inner product is

$$
\langle\varphi,\phi\rangle
=\int_{-\infty}^{\infty}\varphi^*(x)\phi(x)\,dx.
$$

Membership requires

$$
\int_{-\infty}^{\infty}|\phi(x)|^2\,dx<\infty.
$$

## Connection with quantum mechanics

Normalizable wavefunctions belong to an appropriate Hilbert space. For a normalized state,

$$
\langle\psi,\psi\rangle=1.
$$

For example, $$e^x$$ and $$e^{2x}$$ are not square integrable over the entire real line. The expression

$$
\int_{-\infty}^{\infty}e^xe^{2x}\,dx
=\int_{-\infty}^{\infty}e^{3x}\,dx
$$

diverges. These functions therefore cannot serve as normalizable states in $$L^2(\mathbb R)$$. This restriction depends on the domain: a function that is not square integrable on the whole real line may be square integrable on a finite interval.
