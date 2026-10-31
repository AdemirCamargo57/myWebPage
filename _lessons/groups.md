---
title: Groups and Abelian Groups
subject: Mathematical foundations
order: 10
description: Binary operations, the group axioms, and examples from numbers, matrices, and polynomials.
source: grupo.docx
---

## The group axioms

A **group** $$G$$ is a nonempty set together with a binary operation $$\circ:G\times G\to G$$ satisfying the following properties.

1. **Closure:** if $$x,y\in G$$, then $$x\circ y\in G$$.
2. **Associativity:** $$x\circ(y\circ z)=(x\circ y)\circ z$$ for all $$x,y,z\in G$$.
3. **Identity:** there is an element $$e\in G$$ such that $$x\circ e=e\circ x=x$$ for every $$x\in G$$.
4. **Inverses:** for every $$x\in G$$, there is an element $$x^{-1}\in G$$ satisfying $$x\circ x^{-1}=x^{-1}\circ x=e$$.

If the operation is also **commutative**,

$$
x\circ y=y\circ x\qquad\text{for all }x,y\in G,
$$

the group is called an **abelian group**. Commutativity is not required for a general group.

## Examples

- $$(\mathbb R,+)$$, $$(\mathbb Z,+)$$, and $$(\mathbb C,+)$$ are abelian groups. The identity is zero, and the inverse of $$x$$ is $$-x$$.
- The nonzero real numbers form an abelian group under multiplication. The identity is one, and the inverse of $$x$$ is $$1/x$$.
- Real $$2\times2$$ matrices form an abelian group under matrix addition.
- Polynomials of degree at most $$n$$, including the zero polynomial, form an abelian group under addition.

Subtraction does not make $$\mathbb R$$ a group. For example,

$$
(3-2)-1=0,\qquad 3-(2-1)=2,
$$

so subtraction is not associative.

## Why the operation matters

A set by itself does not determine a group. The operation is essential. All real numbers form a group under addition, but not under multiplication, because zero has no multiplicative inverse.
