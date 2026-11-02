# The Nieh–Yan Twist: draft of the next model (NOT LOCKED; for Road A only)

> **Superseded 2 Nov 15:08 (PATH_DECISION_2026-11-02.md):** the K(φ) < 0 route needs a ghost-sign kinetic term and
> has a strong-coupling point at K = 0. The ghost-free alternative (two fields, kinetic mixing; Toomey et al.,
> arXiv:2511.23463) is now the next model. This draft is kept as a record.

**Status:** draft, 2 Nov 2026. It becomes a pre-registration only if tonight's results take Road A (LU not "NOT
CONFIRMED" and a torsion F at least CONSISTENT).

## Why

- The minimal Twist loses to w0–wa because DESI-type fits want a past phantom phase that crosses w = −1 at
  z ≈ 0.37–0.45 (NEXT_MODELS_DESIGN.md §3).
- A canonical field cannot do this (ρ + p = φ̇² ≥ 0).
- Kang, Li & Yi (EPJC 2026) show that coupling dark energy to the Nieh–Yan density in teleparallel gravity removes the
  perturbation instability at the crossing, and predicts parity-violating gravitational waves.
- The Twist already *is* a Nieh–Yan-coupled field (Mercuri & Taveras), so this is the natural extension.

## Ingredients (each must be fixed before any fit)

1. **Decay constant from torsion:** F = (4/π)√(3/2) M_Pl if TF-P comes out CONSISTENT or SUPPORTED, otherwise
   whichever torsion value passed. No free F.
2. **Kinetic term:** a minimal non-canonical P(X, φ) whose background can cross w = −1, with the fewest new parameters.
   The candidate is a single kinetic-coupling coefficient.
   - **Open:** choose the simplest form that the Nieh–Yan mechanism keeps stable. Kang et al. work at the fluid level;
     a field-level form must be written down and checked for ghosts at the background level.
3. **Perturbations:** removed by the Nieh–Yan coupling (Kang et al.). Implementation: a CLASS dark-energy fluid with
   no perturbations and w(z) taken from the field's background solution.
4. **Shape constraint, so it cannot simply copy w0–wa:**
   - frozen until z_on ≈ 1.5 (the same switch as the minimal Twist);
   - crossing redshift and depth set by the single kinetic coefficient.

   It has two dark-energy parameters (m, the kinetic coefficient), the same count as w0–wa.

## Predictions to lock (if built)

1. Δχ² against w0–wa on DES Y5, Pantheon+ and Union3, with equal parameter counts (a fair head-to-head).
2. **Parity-violating gravitational waves:** velocity birefringence at a scale ~ c·φ̇ ≈ 10⁻⁴³–10⁻⁴² GeV. The current
   LIGO-Virgo bound is 6.5×10⁻⁴² GeV, so the model is consistent today. Future detector sensitivity is to be stated.
3. **CMB birefringence:** the ratio R from the same background (it changes if the field crosses).

## Kinetic term: first pass (2 Nov, ~15:05)

- **Candidate with one new parameter:** P = K(φ)·X − V(φ), with K(φ) = tanh((φ − φ_c)/F).
  - Since ρ + p = 2K·X, **w < −1 exactly where K < 0**.
  - As the field rolls through φ_c, K changes sign, and that is the w = −1 crossing.
  - Dark-energy parameters: m and φ_c, the same count as w0–wa (the initial angle is still set by closure).
- **Toy background integration** (scratch `kinetic_check.py`): not conclusive.
  - While the field is frozen, w ≈ −1 to numerical precision, so the toy registers spurious crossings.
  - A proper solver (CLASS, or a stiff integrator with w computed analytically) is needed before any number is
    quoted.
- **The key theory question:** K < 0 is a ghost-sign kinetic term at the background level. Kang et al. argue that the
  Nieh–Yan coupling removes the field's perturbations, so no ghost mode propagates. Before locking we must check:
  1. that this holds for a *field* with K(φ) (they work with a fluid);
  2. that no ghost appears in the tensor or vector sector;
  3. what happens at the instant K = 0, which is a strong-coupling point.

## Open before it can be locked

- The explicit P(X, φ) and a background ghost check. This is a theory task with no CPU.
- A CLASS implementation of the w(z) fluid from the field solution: about one day of coding plus validation gates
  (null and known mirrors, as for the coupled build).
