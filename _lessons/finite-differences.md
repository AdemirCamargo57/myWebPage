---
title: The Finite Difference Method
subject: Mathematical foundations
order: 50
description: Taylor expansions, forward and backward differences, central differences, and truncation errors.
source: Metodo_diferencas_finitas.docx
---

## Taylor expansion

Finite differences replace derivatives with combinations of function values at nearby points. They are useful for numerical differentiation and the numerical solution of differential equations.

For a sufficiently smooth function,

$$
f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k+R_n(x),
$$

where the Lagrange remainder is

$$
R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1}
$$

for some $$\xi$$ between $$x_0$$ and $$x$$. Setting $$x=x_0\pm h$$ gives

$$
\begin{aligned}
f(x_0+h)&=f(x_0)+hf'(x_0)+\frac{h^2}{2}f''(x_0)+\frac{h^3}{6}f'''(x_0)+O(h^4),\\
f(x_0-h)&=f(x_0)-hf'(x_0)+\frac{h^2}{2}f''(x_0)-\frac{h^3}{6}f'''(x_0)+O(h^4).
\end{aligned}
$$

## Forward differences

Rearranging the first expansion yields

$$
f'(x_0)=\frac{f(x_0+h)-f(x_0)}{h}+O(h).
$$

Although the Taylor expansion of the numerator has a remainder of order $$h^2$$, dividing by $$h$$ produces a **first-order derivative approximation**.

Applying the forward difference twice gives

$$
f''(x_0)\approx\frac{f(x_0+2h)-2f(x_0+h)+f(x_0)}{h^2}.
$$

For a fixed derivative order $$n$$, repeated forward differences give

$$
f^{(n)}(x_0)\approx
\frac{1}{h^n}\sum_{k=0}^{n}(-1)^k\binom nk f\bigl(x_0+(n-k)h\bigr),
\qquad\binom nk=\frac{n!}{k!(n-k)!}.
$$

These forward formulas generally have first-order truncation error at $$x_0$$.

## Backward differences

The analogous backward formula is

$$
f'(x_0)=\frac{f(x_0)-f(x_0-h)}{h}+O(h).
$$

Applying it twice gives

$$
f''(x_0)\approx\frac{f(x_0)-2f(x_0-h)+f(x_0-2h)}{h^2}.
$$

The general expression is

$$
f^{(n)}(x_0)\approx
\frac{1}{h^n}\sum_{k=0}^{n}(-1)^k\binom nk f(x_0-kh).
$$

## Central differences

Subtracting the Taylor expansions at $$x_0+h$$ and $$x_0-h$$ cancels the even powers of $$h$$:

$$
f(x_0+h)-f(x_0-h)=2hf'(x_0)+\frac{h^3}{3}f'''(x_0)+O(h^5).
$$

Dividing by $$2h$$ gives

$$
\boxed{f'(x_0)=\frac{f(x_0+h)-f(x_0-h)}{2h}+O(h^2).}
$$

If the total spacing is denoted by $$h$$, so the evaluation points are $$x_0\pm h/2$$, the equivalent formula is

$$
f'(x_0)=\frac{f(x_0+h/2)-f(x_0-h/2)}{h}+O(h^2).
$$

Both expressions are second-order approximations. The cubic remainder in the numerator becomes quadratic after division by the spacing.

Adding the expansions instead produces

$$
\boxed{f''(x_0)=\frac{f(x_0+h)-2f(x_0)+f(x_0-h)}{h^2}+O(h^2).}
$$

## A recursive central formula

Define the central difference operator by

$$
\delta_hf(x)=f(x+h/2)-f(x-h/2).
$$

Repeated application gives

$$
\delta_h^nf(x)=\sum_{k=0}^{n}(-1)^k\binom nk
f\!\left(x+\left(\frac n2-k\right)h\right).
$$

Consequently, for fixed $$n$$ and a sufficiently smooth function,

$$
f^{(n)}(x)=\frac{\delta_h^nf(x)}{h^n}+O(h^2).
$$

Notice that applying this definition twice uses the points $$x-h,x,x+h$$, consistent with the second-derivative formula above.

## Choosing a step size

Reducing $$h$$ lowers truncation error, but eventually subtractive cancellation and floating-point roundoff become important. The best step balances these effects. In a calculation, test more than one step size and inspect whether the derivative stabilizes.
