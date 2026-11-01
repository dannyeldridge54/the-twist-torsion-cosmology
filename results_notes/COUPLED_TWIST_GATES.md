# Coupled Twist: validation gates (PREREGISTRATION_COUPLED_TWIST.md)

**When:** 1 November 2026.

**What was tested:** the AxiCLASS copy at `/home/syndyr/AxiCLASS_coupled`, branch `coupled-twist`.
- The patch is `AEGIS/cmb-fit/axiclass/coupled/patch_coupling.py`: 12 exact-anchor edits.
- The build is `build_coupled.sh`, into its own folder; the installed classy is untouched.
- The gates are run by `gates.py` and `run_v1.sh`.

| Gate | Requirement | Result | Pass? |
|---|---|---|---|
| V1 | β = 0 reproduces the original χ² at the same point to within 0.05 | original 2422.893160603244, coupled 2422.893160603244: **difference 0** (the second run confirmed it loaded the coupled build) | **PASS** |
| V2 | Energy exchange: Σρ continuity to 10⁻⁴ | field energy equation with the exchange term balances to **1.1 × 10⁻⁷** (β = 0.1) | **PASS** |
| V3 | φMDE reaches Ω_φ = 2β²/3 to within 5% (β = 0.1), with "field kinetic, V negligible" | as written (all matter coupled, baryons set negligible): kinetic x² = 0.00546, 0.00597, 0.00627, 0.00647, **0.00660** at a = 0.005, 0.01, 0.02, 0.05, 0.1, against 0.00667. Within 5% from a ≈ 0.02, within 1% at a = 0.1 | **PASS** |
| V4 | Sign: d ln(ρ_c a³)/dlna = β dφ/dlna | residual **1.4 × 10⁻¹¹**, sign correct throughout | **PASS** |

**Note on V3 (written after seeing the first number):**
- With the real baryon fraction the model couples dark matter only, as pre-registered. The φMDE value is then
  2β²f_c²/3, with f_c = ω_c/(ω_b + ω_c) = 0.84, which gives 0.0047; the code gave 0.00478 at a = 0.05.
- I derived that dependence only after seeing 0.0048, so it is **not** what passed the gate. The gate passed as written,
  using the all-matter-coupled run.

**Pipeline check:** a full likelihood evaluation with β = 0.05 at an un-fitted point runs and is finite (χ² 2407.6).
This is not a result.

**Status:** all four gates pass, so coupled fits may count once run.
