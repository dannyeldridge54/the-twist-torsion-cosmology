# SSG results: can the BI dilaton exist without breaking solar-system gravity?

**Rule:** PREREGISTRATION_SOLAR_LOWZ.md (locked 2026-11-02 15:17:31). **Computed:** `solar_lowz.py` → `solar_gate.json`
(sympy). **Tier:** EVIDENCE for the algebra; the supergravity embedding of the Twist is a HYPOTHESIS.

## Verdict (Reading A: matter on the supergravity Jordan frame)

**ATTRACTOR-PROTECTED.**

| Quantity | Value |
|---|---|
| Matter coupling | α(χ) = (2e^{√(2/3)χ} − 1)/√3, i.e. α = (2/√3)(\|ϕ\| − ½) |
| GR point (α = 0) | ϕ = −½ (χ = −0.849) |
| Curvature there | d²ln A/dχ² = +1/3 > 0: an **attractor** (Damour–Nordtvedt) |
| Cassini limit | \|α\| < 3.39×10⁻³ |
| Allowed band today | **\|Δχ\| < 0.0072 M_Pl** around the GR point (checked on the exact α) |
| Away from it | α = 0.58 at χ = 0, −0.35 at χ = −2: far beyond Cassini |

**Reading B** (matter on the Einstein frame): α = 0 by construction. Reported as an extra assumption, not a pass.

**Expectation logged before computing:** ATTRACTOR-PROTECTED or FINE-TUNED. It came out as expected.

## What it means

1. **The good news:** the BI dilaton has a built-in GR point. It sits where the supergravity frame function
   Ω = e^{2ϕ}·2ϕ is stationary (ϕ = −½), and matter pushes the field *toward* it during cosmic history. So the theory
   is not excluded by the solar system.
2. **The cost:** today the dilaton must be within 0.0072 M_Pl of that point. In the kinetic-mixing mechanism
   (Toomey et al.) the phantom-looking effect comes from the dilaton *rolling* and energy flowing between the two
   fields. If the dilaton is pinned:
   - the factor e^{λχ} on the angle's kinetic term is a constant (it changes by at most |λ|·0.0072 ≈ 1.2%);
   - the angle then behaves as a single canonical field, which is the **minimal Late Twist** again;
   - **so in Reading A the Spiral Twist cannot produce the phantom illusion today.** It reduces to the model we
     already tested.
3. **The way out costs one assumption:** Reading B (matter couples to the Einstein-frame metric, so the dilaton
   talks only to the dark sector). That is a choice, not a derivation, and it must be stated if used.
4. **For the path:** step 4 (Spiral Twist theory) now has a sharp question. Is Reading B natural for torsion, e.g.
   because matter fermions couple to the tetrad, which is frame-independent at this order? Until that is answered,
   the Spiral Twist with a rolling dilaton is a Reading-B model only.

## Check (mirror)

- The GR point and band were also found by hand before running: ln A = −ϕ − ½ ln(2|ϕ|/3) + const, so
  d ln A/dχ = √(2/3)(|ϕ| − ½), zero at |ϕ| = ½. The sympy result agrees.
- Band edges evaluated on the exact α: −3.381×10⁻³ and +3.401×10⁻³, both within |α| < 3.391×10⁻³.
