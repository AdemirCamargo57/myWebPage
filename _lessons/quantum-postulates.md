---
title: Postulates of Quantum Mechanics
subject: Quantum chemistry
order: 10
description: States, observables, measurement, time evolution, canonical quantization, and position and momentum representations.
source: CAP-II_v10.docx
---

## States and superposition

The state of a closed quantum system at an initial time is specified by a vector $$|\psi(t_0)\rangle$$ in the Hilbert space associated with the system. For a pure state, physically equivalent nonzero vectors that differ only by an overall complex factor represent the same ray. We normally choose a normalized representative.

A linear combination of state vectors is another vector in the state space. For example,

$$
|\Psi\rangle=c_1|\psi_1\rangle+c_2|\psi_2\rangle.
$$

The complex coefficients are probability amplitudes. When the component states are orthonormal and $$\Psi$$ is normalized, $$|c_1|^2+|c_2|^2=1$$. Superposition describes a quantum state; it does not mean that a measurement yields several eigenvalues at once.

## Observables

Measurable physical quantities are represented by self-adjoint operators. In finite-dimensional treatments these are Hermitian matrices:

$$
\hat A^\dagger=\hat A.
$$

Examples are position $$\hat x$$, linear momentum $$\hat p$$, angular momentum $$\hat L$$, and energy $$\hat H$$. Self-adjointness ensures a real spectrum. In a finite-dimensional space, a Hermitian operator has a complete orthonormal eigenbasis. For differential operators, domains and boundary conditions also matter.

## Possible measurement outcomes

An ideal measurement of an observable yields a value in its spectrum. For a discrete energy eigenstate,

$$
\hat H|n\rangle=E_n|n\rangle.
$$

A state can be expanded in a complete energy eigenbasis:

$$
|\psi\rangle=\sum_n c_n|n\rangle.
$$

Some operators have continuous spectra. Position and momentum on the full real line are familiar examples; an energy spectrum can be discrete, continuous, or mixed, depending on the system.

## Continuous bases and the Dirac delta

Formally, a position expansion is

$$
|\psi\rangle=\int_{-\infty}^{\infty}\psi(x)|x\rangle\,dx,
\qquad\psi(x)=\langle x|\psi\rangle.
$$

The discrete orthonormality relation $$\langle n|m\rangle=\delta_{nm}$$ is replaced by

$$
\langle x|x'\rangle=\delta(x-x').
$$

The Dirac delta is a distribution, not an ordinary function with a conventional value of infinity at zero. Its defining sampling property is

$$
\int f(x')\delta(x-x')\,dx'=f(x),
\qquad\int\delta(x-x')\,dx'=1.
$$

The continuous completeness relations are

$$
\int|x\rangle\langle x|\,dx=\hat I,
\qquad\int|p\rangle\langle p|\,dp=\hat I.
$$

The generalized kets $$|x\rangle$$ and $$|p\rangle$$ are not normalizable Hilbert-space vectors in the same sense as a bound-state wavefunction; these relations are understood in the distributional framework.

## Measurement probabilities

For a normalized state and a nondegenerate discrete eigenstate $$|a\rangle$$, the probability of obtaining eigenvalue $$a$$ is the Born rule:

$$
P(a)=|\langle a|\psi\rangle|^2.
$$

If the state has not been normalized,

$$
P(a)=\frac{|\langle a|\psi\rangle|^2}{\langle\psi|\psi\rangle}.
$$

For a degenerate eigenspace, use its projector $$P_a$$:

$$
P(a)=\langle\psi|P_a|\psi\rangle.
$$

For a continuous position measurement, $$|\psi(x)|^2$$ is a probability density:

$$
P(x\in[a,b])=\int_a^b|\psi(x)|^2\,dx.
$$

## State after an ideal measurement

If a projective measurement gives outcome $$a$$, the state immediately afterward is

$$
|\psi'\rangle=\frac{P_a|\psi\rangle}
{\sqrt{\langle\psi|P_a|\psi\rangle}}.
$$

In the nondegenerate case it is proportional to $$|a\rangle$$. An immediate repetition of the same ideal measurement then gives the same value with certainty, provided no intervening evolution changes the state.

## Time evolution

Between measurements, the state of a closed system evolves according to the Schrödinger equation:

$$
i\hbar\frac{d}{dt}|\psi(t)\rangle=\hat H|\psi(t)\rangle.
$$

For a time-independent Hamiltonian,

$$
|\psi(t)\rangle=e^{-i\hat Ht/\hbar}|\psi(0)\rangle
=\sum_n c_ne^{-iE_nt/\hbar}|n\rangle.
$$

### Global and relative phases

Multiplying the entire state by a phase $$e^{i\theta}$$ does not change its measurement probabilities:

$$
|\langle a|e^{i\theta}\psi\rangle|^2
=|\langle a|\psi\rangle|^2.
$$

Changing the phase of only one component generally changes the state. For example,

$$
|\psi(t)\rangle
=\alpha e^{-iE_1t/\hbar}|1\rangle
+\beta e^{-iE_2t/\hbar}|2\rangle
$$

has the same ray as

$$
\alpha|1\rangle+\beta e^{-i(E_2-E_1)t/\hbar}|2\rangle.
$$

Removing a common energy offset removes only a global phase. Relative energy differences control the phase evolution between components.

## Canonical quantization and ordering

Canonical quantization associates classical coordinates and momenta with operators obeying

$$
[\hat q_i,\hat p_j]=i\hbar\delta_{ij}\hat I,
\quad[\hat q_i,\hat q_j]=[\hat p_i,\hat p_j]=0.
$$

Products require care because the operators need not commute. A common symmetric prescription maps a classical product $$px$$ to

$$
px\longmapsto\tfrac12(\hat p\hat x+\hat x\hat p).
$$

A fully symmetrized product of three factors averages over their six orderings. Symmetrization is a useful prescription, not a universal theorem that uniquely quantizes every classical observable.

## Poisson brackets

For classical functions $$f(q_i,p_i,t)$$ and $$g(q_i,p_i,t)$$, define

$$
\{f,g\}=\sum_i\left(
\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}
-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right).
$$

Using Hamilton's equations,

$$
\dot q_i=\frac{\partial H}{\partial p_i},
\qquad\dot p_i=-\frac{\partial H}{\partial q_i},
$$

the total time derivative is

$$
\frac{df}{dt}=\{f,H\}+\frac{\partial f}{\partial t}.
$$

For a function with no explicit time dependence, $$\{f,H\}=0$$ implies that it is a constant of motion. In particular,

$$
\{q_k,p_l\}=\delta_{kl},\qquad
\{f,q_k\}=-\frac{\partial f}{\partial p_k},\qquad
\{f,p_k\}=\frac{\partial f}{\partial q_k}.
$$

Poisson brackets are antisymmetric, bilinear, obey the product rule, and satisfy the Jacobi identity:

$$
\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0.
$$

If $$f$$ and $$g$$ are constants of motion, their Poisson bracket is also a constant of motion under the usual regularity assumptions. This follows by combining the time-derivative rule and the Jacobi identity.

The correspondence with the commutator is expressed schematically as

$$
\{f,g\}\longleftrightarrow\frac{1}{i\hbar}[\hat f,\hat g].
$$

It correctly motivates the canonical commutation relations. It is not an exact operator identity for arbitrary classical functions.

## Expectation values

For a normalized state,

$$
\langle A\rangle=\langle\psi|\hat A|\psi\rangle.
$$

If $$|\psi\rangle=\alpha|1\rangle+\beta|2\rangle$$, with orthonormal eigenstates satisfying $$\hat A|j\rangle=a_j|j\rangle$$, then

$$
\langle A\rangle=|\alpha|^2a_1+|\beta|^2a_2.
$$

This is the usual statistical mean weighted by measurement probabilities. If the two probabilities are equal, the mean is $$(a_1+a_2)/2$$. A mean need not itself be a possible individual measurement result.

## Ehrenfest's theorem

Differentiating the expectation value and using the Schrödinger equation gives

$$
\boxed{\frac{d}{dt}\langle A\rangle
=\frac{1}{i\hbar}\langle[\hat A,\hat H]\rangle
+\left\langle\frac{\partial\hat A}{\partial t}\right\rangle.}
$$

For the harmonic oscillator,

$$
\hat H=\frac{\hat p^2}{2m}+\frac{k\hat x^2}{2},
$$

the commutator $$[\hat p,\hat x^2]=-2i\hbar\hat x$$ yields

$$
\frac{d\langle p\rangle}{dt}=-k\langle x\rangle,
\qquad\frac{d\langle x\rangle}{dt}=\frac{\langle p\rangle}{m}.
$$

For this potential, the mean values obey the classical oscillator equations. For a general potential, $$d\langle p\rangle/dt=-\langle V'(x)\rangle$$, which need not equal $$-V'(\langle x\rangle)$$.

## Position and momentum representations

The position wavefunction is the projection

$$
\psi(x,t)=\langle x|\psi(t)\rangle.
$$

In this representation the position operator multiplies by $$x$$:

$$
\langle x|\hat x|\psi\rangle=x\psi(x).
$$

With the continuum normalization used here,

$$
\langle x|p\rangle=\frac{1}{\sqrt{2\pi\hbar}}e^{ipx/\hbar}.
$$

Position and momentum wavefunctions are Fourier transforms:

$$
\psi(x)=\frac{1}{\sqrt{2\pi\hbar}}
\int e^{ipx/\hbar}\widetilde\psi(p)\,dp,
$$

$$
\widetilde\psi(p)=\frac{1}{\sqrt{2\pi\hbar}}
\int e^{-ipx/\hbar}\psi(x)\,dx.
$$

Differentiating the first expression gives

$$
-i\hbar\frac{\partial\psi(x)}{\partial x}
=\frac{1}{\sqrt{2\pi\hbar}}\int p\,e^{ipx/\hbar}\widetilde\psi(p)\,dp.
$$

Therefore the momentum operator in the position representation is

$$
\boxed{\hat p=-i\hbar\frac{\partial}{\partial x}.}
$$

For a particle with $$\hat H=\hat p^2/(2m)+V(\hat x)$$, projecting the abstract Schrödinger equation onto $$\langle x|$$ gives

$$
i\hbar\frac{\partial\psi(x,t)}{\partial t}
=\left[-\frac{\hbar^2}{2m}\frac{\partial^2}{\partial x^2}+V(x)\right]\psi(x,t).
$$

The abstract state is a time-dependent vector; its position representation depends on both $$x$$ and $$t$$, hence the partial derivative in the wave equation.
