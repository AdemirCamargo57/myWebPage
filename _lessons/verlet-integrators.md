---
title: Verlet, Velocity Verlet, and Leapfrog Integration
subject: Molecular dynamics
order: 20
description: Time-stepping equations of motion, force evaluation, velocities, and kinetic energy.
source: verlet_velocity_verlet_leap_frog.docx
---

## The position Verlet algorithm

Molecular dynamics requires the numerical integration of equations of motion. The Verlet family of algorithms advances atomic positions in discrete time steps. These methods are also used in extended dynamical formulations such as Car–Parrinello dynamics.

Let $$\mathbf r(t)$$, $$\mathbf v(t)$$, and $$\mathbf a(t)$$ denote position, velocity, and acceleration, and let $$h=\Delta t$$. Taylor expansion gives

$$
\begin{aligned}
\mathbf r(t+h)&=\mathbf r(t)+\mathbf v(t)h+\tfrac12\mathbf a(t)h^2
+\tfrac16\dot{\mathbf a}(t)h^3+O(h^4),\\
\mathbf r(t-h)&=\mathbf r(t)-\mathbf v(t)h+\tfrac12\mathbf a(t)h^2
-\tfrac16\dot{\mathbf a}(t)h^3+O(h^4).
\end{aligned}
$$

Adding the expressions and using $$\mathbf a(t)=\mathbf F(t)/m$$ yields

$$
\boxed{\mathbf r(t+h)=2\mathbf r(t)-\mathbf r(t-h)
+\frac{\mathbf F(t)}m h^2+O(h^4).}
$$

For conservative interactions, the force is

$$
\mathbf F=-\nabla V
=-\left(\frac{\partial V}{\partial x},
\frac{\partial V}{\partial y},\frac{\partial V}{\partial z}\right).
$$

The next position requires the current and previous positions and the current force. Position Verlet is simple and time reversible for the usual position-dependent force problem. The local position relation has an $$O(h^4)$$ remainder; the integration method has second-order global accuracy.

## Recovering velocities

Subtracting the Taylor expansions gives

$$
\mathbf r(t+h)-\mathbf r(t-h)=2h\mathbf v(t)+O(h^3),
$$

so

$$
\mathbf v(t)=\frac{\mathbf r(t+h)-\mathbf r(t-h)}{2h}+O(h^2).
$$

Velocities are not needed to update positions in this formulation, but are needed for kinetic energy and temperature. The central velocity estimate becomes available only after the next position has been calculated.

## Velocity Verlet

Velocity Verlet advances positions and velocities together. For forces depending only on position, it can be written as

$$
\begin{aligned}
\mathbf r_{n+1}&=\mathbf r_n+\mathbf v_nh+\tfrac12\mathbf a_nh^2,\\
\mathbf a_{n+1}&=\mathbf F(\mathbf r_{n+1})/m,\\
\mathbf v_{n+1}&=\mathbf v_n+\tfrac12(\mathbf a_n+\mathbf a_{n+1})h.
\end{aligned}
$$

The position update follows from a Taylor expansion. For the velocity, start with

$$
\mathbf v(t+h)=\mathbf v(t)+\mathbf a(t)h
+\tfrac12\dot{\mathbf a}(t)h^2+O(h^3).
$$

Approximating $$\dot{\mathbf a}(t)$$ by

$$
\dot{\mathbf a}(t)\approx\frac{\mathbf a(t+h)-\mathbf a(t)}h
$$

gives the average-acceleration velocity update above.

An equivalent implementation uses two half-step velocity updates:

1. Compute $$\mathbf v_{n+1/2}=\mathbf v_n+\tfrac12h\mathbf a_n$$.
2. Advance $$\mathbf r_{n+1}=\mathbf r_n+h\mathbf v_{n+1/2}$$.
3. Evaluate the new force and acceleration.
4. Complete $$\mathbf v_{n+1}=\mathbf v_{n+1/2}+\tfrac12h\mathbf a_{n+1}$$.

After initialization, only one new force evaluation is required per step. Velocity-dependent forces, thermostats, or constraints may require modified integration schemes.

## Leapfrog

Leapfrog stores positions at integer times and velocities at half-integer times:

$$
\begin{aligned}
\mathbf v_{n+1/2}&=\mathbf v_{n-1/2}+h\mathbf a_n,\\
\mathbf r_{n+1}&=\mathbf r_n+h\mathbf v_{n+1/2}.
\end{aligned}
$$

The position and velocity sequences leap over one another. A velocity at the integer time can be reconstructed as

$$
\mathbf v_n=\tfrac12(\mathbf v_{n-1/2}+\mathbf v_{n+1/2}).
$$

To initialize from a known $$\mathbf v_0$$, use a consistent half-step estimate, such as $$\mathbf v_{-1/2}=\mathbf v_0-\tfrac12h\mathbf a_0$$.

## Kinetic energy and temperature

For atomic masses $$m_\alpha$$,

$$
K=\frac12\sum_\alpha m_\alpha|\mathbf v_\alpha|^2.
$$

Under the usual classical equipartition assumptions, an instantaneous kinetic temperature is

$$
T=\frac{2K}{f k_\mathrm B},
$$

where $$f$$ is the number of active degrees of freedom. Constraints and removed center-of-mass motion affect $$f$$. With leapfrog, care is needed because half-step and reconstructed full-step velocities lead to different finite-step kinetic-energy estimates.

## Accuracy and stability

These integrators are second order. Their good long-time behavior does not imply exact energy conservation at a finite time step. Choose a step small enough to resolve the fastest relevant motion, and check energy behavior and convergence as the time step is reduced.
