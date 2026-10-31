---
title: Fields, Vector Spaces, Inner Products, and Norms
subject: Mathematical foundations
order: 20
description: Linear combinations, bases, Dirac notation, orthonormality, and the resolution of the identity.
source: grupo_corpo_espaco_vetorial_norma.docx
---

## Fields

A **field** $$K$$ is a set equipped with addition and multiplication. Under addition it is an abelian group. Its nonzero elements form an abelian group under multiplication, and multiplication distributes over addition:

$$
a(b+c)=ab+ac.
$$

The real numbers $$\mathbb R$$ and complex numbers $$\mathbb C$$ are the principal fields used here. Elements of the field are called **scalars**.

## Vector spaces

A vector space $$E$$ over $$K$$ has vector addition and scalar multiplication. Vector addition makes $$E$$ an abelian group. For scalars $$\alpha,\beta$$ and vectors $$u,v$$, the additional rules are

$$
\begin{aligned}
\alpha(u+v)&=\alpha u+\alpha v,\\
(\alpha+\beta)u&=\alpha u+\beta u,\\
\alpha(\beta u)&=(\alpha\beta)u,\\
1u&=u.
\end{aligned}
$$

The word *vector* does not necessarily mean an arrow in physical space. Functions, matrices, polynomials, and quantum states can all be vectors.

### Examples and exercises

1. Show that $$E=\{(x,y)\in\mathbb R^2:y=2x\}$$ is a vector space over $$\mathbb R$$.
2. Is $$\{(x,y):y=2x+2\}$$ a vector space? Check whether it contains the zero vector.
3. Show that real polynomials of degree at most three form a vector space. Find a basis and its dimension.
4. Show that real-valued functions on $$\mathbb R$$, with pointwise addition and scalar multiplication, form a vector space:

   $$
   (f+g)(x)=f(x)+g(x),\qquad(cf)(x)=cf(x).
   \]

5. Do real $$2\times2$$ matrices form a vector space?

The complex numbers can be viewed as a vector space over $$\mathbb C$$, of dimension one, or over $$\mathbb R$$, of dimension two. The underlying scalar field matters.

## Bases and linear independence

A basis is a linearly independent set that spans the space. In an $$n$$-dimensional space, every vector has a unique expansion

\[
v=\sum_{i=1}^{n}c_i e_i.
$$

The number of basis vectors is the dimension. Linear independence means that

$$
\sum_{i=1}^{n}c_i e_i=0
\quad\Longrightarrow\quad c_1=\cdots=c_n=0.
$$

For the canonical basis of $$\mathbb R^3$$,

$$
e_1=\begin{pmatrix}1\\0\\0\end{pmatrix},\quad
e_2=\begin{pmatrix}0\\1\\0\end{pmatrix},\quad
e_3=\begin{pmatrix}0\\0\\1\end{pmatrix},
\qquad v=\begin{pmatrix}c_1\\c_2\\c_3\end{pmatrix}.
$$

The vector is abstract; its coordinates depend on the chosen basis. To prove uniqueness, suppose

$$
v=\sum_i c_ie_i=\sum_i a_ie_i.
$$

Subtracting gives $$\sum_i(c_i-a_i)e_i=0$$. Linear independence implies $$c_i=a_i$$ for every $$i$$.

### Exercises

- Can $$\{(1,0,1),(2,0,0)\}$$ be a basis of $$\mathbb R^3$$?
- Is $$\{(1,1),(0,1)\}$$ a basis of $$\mathbb R^2$$?
- Is $$\{(1,0),(0,1),(2,1)\}$$ a basis of $$\mathbb R^2$$?
- Find a basis for real symmetric $$2\times2$$ matrices.

## Inner products

An inner product associates a scalar with two vectors:

$$
\langle\cdot,\cdot\rangle:E\times E\to K.
$$

Using the physics convention, it is linear in the second argument and conjugate linear in the first:

$$
\begin{aligned}
\langle u,u\rangle&\geq0,\quad
\langle u,u\rangle=0\iff u=0,\\
\langle u,v\rangle&=\langle v,u\rangle^*,\\
\langle u,\alpha v+\beta w\rangle
&=\alpha\langle u,v\rangle+\beta\langle u,w\rangle,\\
\langle\alpha u+\beta v,w\rangle
&=\alpha^*\langle u,w\rangle+\beta^*\langle v,w\rangle.
\end{aligned}
$$

Some mathematics texts use the opposite convention for linearity. Either convention is consistent if used throughout.

In the canonical orthonormal basis of $$\mathbb R^n$$,

$$
e_i\cdot e_j=\delta_{ij},\qquad
u\cdot v=\sum_i u_i v_i,
$$

where the **Kronecker delta** is one when $$i=j$$ and zero otherwise.

## Dirac notation

In quantum mechanics an abstract vector is written as a **ket**, $$|a\rangle$$. In an orthonormal basis $$\{|i\rangle\}$$,

$$
|a\rangle=\sum_i a_i|i\rangle,
\qquad a=\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}.
$$

Its associated **bra** is the conjugate transpose:

$$
\langle a|=\sum_i a_i^*\langle i|,
\qquad a^\dagger=(a_1^*,a_2^*,\ldots,a_n^*).
$$

The dagger denotes conjugate transposition. In a complex inner product space, the inner product identifies kets with corresponding conjugate-linear combinations of bras. In finite dimensions this is represented directly by conjugate-transposed coordinate arrays.

The bra–ket product is a scalar:

$$
\langle a|b\rangle=a^\dagger b
=\sum_i a_i^*b_i.
$$

In particular,

$$
\langle a|a\rangle=\sum_i|a_i|^2=\|a\|^2.
$$

For an orthonormal basis, $$\langle i|j\rangle=\delta_{ij}$$. Hence

$$
\langle a|b\rangle
=\sum_{i,j}a_i^*\langle i|j\rangle b_j
=\sum_i a_i^*b_i.
$$

## Completeness and the identity operator

Multiplying the expansion of a ket by a basis bra gives its coordinate:

$$
a_j=\langle j|a\rangle,
\qquad a_j^*=\langle a|j\rangle.
$$

Substitution into the expansion gives

$$
|a\rangle=\sum_i|i\rangle\langle i|a\rangle.
$$

Since this holds for every ket, a complete orthonormal basis satisfies the **resolution of the identity**:

$$
\boxed{\sum_i|i\rangle\langle i|=\hat I.}
$$

Each outer product $$|i\rangle\langle i|$$ is a projector. For the canonical basis in three dimensions, their sum is the $$3\times3$$ identity matrix.

## Norms

A norm is a function $$\|\cdot\|:E\to[0,\infty)$$ satisfying

$$
\begin{aligned}
\|v\|&\geq0,\quad\|v\|=0\iff v=0,\\
\|\alpha v\|&=|\alpha|\|v\|,\\
\|v+w\|&\leq\|v\|+\|w\|.
\end{aligned}
$$

The last property is the triangle inequality. A space equipped with a norm is called a **normed vector space**. Its induced distance is $$d(v,w)=\|v-w\|$$.

Every inner product defines a norm,

$$
\boxed{\|v\|=\sqrt{\langle v,v\rangle},}
$$

but not every norm arises from an inner product. In Euclidean space this is the familiar length obtained from the dot product.
