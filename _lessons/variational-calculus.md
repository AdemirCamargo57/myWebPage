---
title: Variational Calculus
subject: Mathematical foundations
order: 60
description: Stationary functionals, the Euler–Lagrange equation, holonomic constraints, and functional derivatives.
source: CÁLCULO VARIACIONAL.docx
---

## From functions to functionals

Ordinary calculus finds stationary values of functions. Variational calculus asks which **function** makes a **functional** stationary. A functional assigns a number to an entire function or curve. A common form is

$$
I[y]=\int_{x_i}^{x_f}F(x,y(x),y'(x))\,dx.
$$

A stationary value can be a minimum, a maximum, or a saddle point. The first-variation condition alone does not distinguish them.

### Shortest path between two points

For a curve $$y=y(x)$$ in a plane, its arc length is

$$
I[y]=\int ds=\int_{x_i}^{x_f}\sqrt{1+y'^2}\,dx,
\qquad ds=\sqrt{dx^2+dy^2}.
$$

Finding the shortest path becomes a minimization problem for this functional, with the endpoint values fixed.

### The brachistochrone problem

Consider a particle released from rest at height $$h$$, sliding without friction under gravity. If $$y$$ measures height upward, conservation of energy gives

$$
\tfrac12mv^2=m g(h-y),\qquad v=\sqrt{2g(h-y)}.
$$

Since $$dt=ds/v$$, the travel time is

$$
T[y]=\int_{x_i}^{x_f}\sqrt{\frac{1+y'^2}{2g(h-y)}}\,dx.
$$

The desired path minimizes travel time, which is a different objective from minimizing distance. Related variational questions ask for shortest paths on spheres, curves enclosing the largest area for a fixed perimeter, or surfaces enclosing the largest volume under appropriate constraints.

## Deriving the Euler–Lagrange equation

Let $$y(x)$$ be a candidate stationary curve. Construct nearby curves

$$
Y(x,\epsilon)=y(x)+\epsilon\eta(x),
\qquad\eta(x_i)=\eta(x_f)=0.
$$

The function $$\eta$$ is arbitrary apart from smoothness and endpoint conditions. With $$\eta$$ fixed, the functional becomes an ordinary function of $$\epsilon$$:

$$
I(\epsilon)=\int_{x_i}^{x_f}F(x,Y,Y')\,dx.
$$

Stationarity requires

$$
\left.\frac{dI}{d\epsilon}\right|_{\epsilon=0}=0.
$$

Assuming sufficient smoothness to differentiate under the integral,

$$
\left.\frac{dI}{d\epsilon}\right|_0
=\int_{x_i}^{x_f}\left(
\frac{\partial F}{\partial y}\eta
+\frac{\partial F}{\partial y'}\eta'\right)dx.
$$

The independent variable $$x$$ does not vary with $$\epsilon$$. Integration by parts gives

$$
\int_{x_i}^{x_f}\frac{\partial F}{\partial y'}\eta'\,dx
=\left[\frac{\partial F}{\partial y'}\eta\right]_{x_i}^{x_f}
-\int_{x_i}^{x_f}\frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right)\eta\,dx.
$$

The boundary term vanishes because $$\eta$$ vanishes at both endpoints. Therefore

$$
\int_{x_i}^{x_f}\left[
\frac{\partial F}{\partial y}
-\frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right)
\right]\eta(x)\,dx=0.
$$

By the fundamental lemma of variational calculus, the coefficient must vanish when this holds for all admissible test functions:

$$
\boxed{\frac{\partial F}{\partial y}
-\frac{d}{dx}\left(\frac{\partial F}{\partial y'}\right)=0.}
$$

This is the **Euler–Lagrange equation**. The conclusion follows from the arbitrariness of $$\eta$$, not from a general claim that a zero integral has an identically zero integrand.

## First variations and the symbol δ

The variation of the curve is

$$
\delta y=Y(x,\epsilon)-y(x)=\epsilon\eta(x).
$$

The independent variable remains fixed: $$\delta x=0$$. Expanding the integrand gives

$$
F(x,y+\delta y,y'+\delta y')
=F(x,y,y')+F_y\delta y+F_{y'}\delta y'+O(\delta^2).
$$

The linear term is the first variation:

$$
\delta I=\int_{x_i}^{x_f}(F_y\delta y+F_{y'}\delta y')\,dx.
$$

Here $$\delta y'=d(\delta y)/dx$$. Thus variation and differentiation commute for the smooth families under consideration:

$$
\delta\left(\frac{dy}{dx}\right)=\frac{d}{dx}(\delta y).
$$

After integration by parts,

$$
\delta I=\int_{x_i}^{x_f}
\left[F_y-\frac{d}{dx}F_{y'}\right]\delta y\,dx.
$$

Also,

$$
\delta I=\epsilon\left.\frac{dI}{d\epsilon}\right|_0.
$$

This explains the equivalence of the stationary conditions in the two notations.

The distinction between $$d$$ and $$\delta$$ is useful: $$dy$$ describes a change along a given curve as $$x$$ changes, while $$\delta y$$ describes a change from one curve to a neighboring curve at the same $$x$$.

## Application to the shortest path

For $$F=\sqrt{1+y'^2}$$, the integrand does not depend explicitly on $$y$$. The Euler–Lagrange equation becomes

$$
\frac{d}{dx}\left(\frac{y'}{\sqrt{1+y'^2}}\right)=0.
$$

Hence $$y'$$ is constant and the stationary curve is a straight line. With fixed endpoints in the Euclidean plane, this gives the shortest path.

## Several dependent variables

For

$$
I[y_1,\ldots,y_n]
=\int F(x,y_1,\ldots,y_n,y_1',\ldots,y_n')\,dx,
$$

independent variations give one equation for each dependent variable:

$$
\frac{\partial F}{\partial y_i}
-\frac{d}{dx}\left(\frac{\partial F}{\partial y_i'}\right)=0,
\qquad i=1,\ldots,n.
$$

In analytical mechanics, replace $$x$$ by time $$t$$, the $$y_i$$ by generalized coordinates $$q_i$$, and $$F$$ by the Lagrangian $$L$$. Stationarity of the action then gives Lagrange's equations.

## Holonomic constraints

A holonomic constraint can be written as an equation involving generalized coordinates and possibly time:

$$
f(q_1,\ldots,q_n,t)=0.
$$

If it does not explicitly depend on time, it is called **scleronomic**. With $$m$$ independent regular constraints, the number of independent coordinates is reduced from $$n$$ to $$n-m$$.

Directly eliminating coordinates can be inconvenient. Lagrange multipliers allow all coordinates to be retained. For an ordinary constrained optimization problem, stationary points satisfy

$$
\delta\left(F+\sum_{a=1}^{m}\lambda_a f_a\right)=0,
\qquad f_a=0,
$$

or

$$
\frac{\partial F}{\partial y_i}
+\sum_a\lambda_a\frac{\partial f_a}{\partial y_i}=0.
$$

For a functional with pointwise constraints $$f_a(x,y_1,\ldots,y_n)=0$$, use the augmented integrand

$$
\widetilde F=F+\sum_a\lambda_a(x)f_a.
$$

The equations become

$$
\frac{\partial F}{\partial y_i}
-\frac{d}{dx}\frac{\partial F}{\partial y_i'}
+\sum_a\lambda_a(x)\frac{\partial f_a}{\partial y_i}=0,
$$

together with the constraints. Multipliers for pointwise constraints are generally functions of the independent variable.

### Worked example: a plane over a circle

Find the extrema of $$\Theta(x,y)=x+y$$ subject to

$$
(x-2)^2+(y-2)^2=1.
$$

With $$f=(x-2)^2+(y-2)^2-1$$, stationarity of $$\Theta+\lambda f$$ gives

$$
1+2\lambda(x-2)=0,\qquad
1+2\lambda(y-2)=0.
$$

Thus $$x=y$$. Substituting in the constraint gives

$$
x=y=2\pm\frac{1}{\sqrt2}.
$$

The maximum value is $$4+\sqrt2$$, and the minimum is $$4-\sqrt2$$.

### Exercise

Find the maximum of $$f(x,y)=x^2y$$ subject to $$x^2+y^2=3$$. Set up the multiplier equations and compare all stationary candidates. The number of equations matching the number of unknowns does not guarantee a unique solution.

## Functional derivatives

The directional derivative of a functional is defined by

$$
DI[u](\eta)=
\left.\frac{d}{d\epsilon}I[u+\epsilon\eta]\right|_0.
$$

When it can be written as

$$
DI[u](\eta)=\int\frac{\delta I}{\delta u(x)}\eta(x)\,dx,
$$

the coefficient is called the **functional derivative**. It is important to distinguish the directional derivative, a number for a chosen $$\eta$$, from the function $$\delta I/\delta u(x)$$.

For

$$
I[u]=\int_{x_0}^{x_1}F(x,u,u')\,dx,
$$

Taylor expansion and integration by parts, with fixed endpoint values, give

$$
\boxed{\frac{\delta I}{\delta u(x)}
=\frac{\partial F}{\partial u}
-\frac{d}{dx}\left(\frac{\partial F}{\partial u'}\right).}
$$

### Example: an integral of a square

Let $$J[y]=\int y(x)^2\,dx$$. Then

$$
J[y+\epsilon\eta]-J[y]
=\int(2\epsilon y\eta+\epsilon^2\eta^2)\,dx.
$$

Dividing by $$\epsilon$$ and taking the limit gives

$$
DJ[y](\eta)=\int2y\eta\,dx,
\qquad\frac{\delta J}{\delta y(x)}=2y(x).
$$

### Example: an integral of a square root

For $$J[\phi]=\int\sqrt{\phi(t)}\,dt$$, with $$\phi$$ strictly positive where varied, the binomial expansion gives

$$
\sqrt{\phi+\epsilon\eta}
=\sqrt\phi+\frac{\epsilon\eta}{2\sqrt\phi}
-\frac{\epsilon^2\eta^2}{8\phi^{3/2}}+\cdots.
$$

Therefore

$$
\frac{\delta J}{\delta\phi(t)}=\frac{1}{2\sqrt{\phi(t)}}.
$$

## Sum and product rules

The variation follows familiar algebraic rules:

$$
\delta(F+G)=\delta F+\delta G,
\qquad\delta(FG)=F\,\delta G+G\,\delta F.
$$

For constant $$c_1,c_2$$,

$$
\frac{\delta(c_1F+c_2G)}{\delta u(x)}
=c_1\frac{\delta F}{\delta u(x)}
+c_2\frac{\delta G}{\delta u(x)}.
$$

For a product of scalar-valued functionals,

$$
\frac{\delta(FG)}{\delta u(x)}
=G\frac{\delta F}{\delta u(x)}
+F\frac{\delta G}{\delta u(x)}.
$$

To see the product rule, add and subtract $$F[u+\epsilon\eta]G[u]$$ in the increment of $$FG$$, divide by $$\epsilon$$, and take the limit. Each resulting term has the form of a directional derivative.

## Further reading

R. G. Parr and W. Yang, *Density-Functional Theory of Atoms and Molecules* (1989), discussion of functional differentiation.
