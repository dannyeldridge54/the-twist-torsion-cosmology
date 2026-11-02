# UFE checks: early role (ER), LQG value (LQ), inflation (IN)

**Rule:** PREREGISTRATION_UFE_CHECKS.md (locked 2026-11-02 15:50:03). **Computed:** `ufe_checks.py` →
`ufe_er.json`, `ufe_in.json`, `ufe_lq.json`. **Tier:** consistency checks of the supergravity embedding (HYPOTHESIS);
none of them is evidence for or against the cosmological fits.

## IN. Inflation from the α = 1 geometry: **TENSION**

| N (e-folds) | n_s = 1 − 2/N | r = 12/N² | Pull vs 0.974 ± 0.003 |
|---|---|---|---|
| 50 | 0.9600 | 0.0048 | 4.7σ |
| 55 | 0.9636 | 0.0040 | 3.5σ |
| **60** | **0.9667** | **0.0033** | **2.4σ** |

- r is far below the BICEP/Keck bound (0.036). The problem is n_s: the α = 1 (Starobinsky-type) value sits below what
  ACT DR6 + Planck + lensing + DESI prefer.
- To reach a 2σ pull it needs N ≥ 62.5 e-folds, which requires an unusually late or efficient reheating.
- This is the known general tension between ACT DR6 and Starobinsky-like inflation, not something specific to the
  Twist. Our own fits with early energy prefer n_s ≈ 0.973–0.975 as well.
- **Expectation logged before computing:** TENSION. It came out as expected.
- **What it means:** the "one geometry for inflation and dark energy" lead is not dead, but its simplest form is under
  pressure. Ways out, each adding something: a different potential shape, more e-folds, or α ≠ 1 (which would break
  the λ = −2√(2/3) link found today).

## ER. Early energy from the dilaton relaxing to its GR point: **TOO SMALL**

| Quantity | Best case over 100 starting values |
|---|---|
| Max Ω_χ at z = 3500 | **0.025** (|ϕ|ᵢ = 2.61); the rule needs ≥ 0.03, the early fits want about 0.07 |
| Ω_χ at z = 500 there | 0.0034 (it does decay) |
| Distance from the GR point today | 1.2×10⁻⁴ (passes Cassini: the attractor works) |
| Change of Newton's constant at BBN | **×13** (the bound is 10%) |

- **Expectation logged before computing:** WRONG SHAPE. It came out as TOO SMALL instead: the relaxation never
  reaches 3% at z = 3500.
- **Worse:** the starting values that come closest need the dilaton far from the GR point early on, and in Reading A
  that changes Newton's constant by a factor of 13 at BBN. Starting values that respect BBN give far less early energy.
- **What it means:** the dilaton cannot be the early field in Reading A. The early role still has no home inside the
  BI supergravity embedding. The early energy needs its own potential (as in the original n = 3 early field), or a
  different mechanism.

## LQ. The BI value today against LQG: **NO VERDICT (mirror failed)**

| Fit | φ_today (CLASS) | \|γ_today\| = √6/(2φ) | Within 10% of 0.2375 / 0.2740? | Mirror (rebuilt − stored log-posterior) |
|---|---|---|---|---|
| Late Twist, Pantheon+ | 4.723 | **0.259** | yes / yes | **0.087: FAIL** (limit 0.05) |
| Late Twist, DES Y5 | 1.808 | 0.677 | no / no | 0.002: pass |

- **By the locked rule there is no verdict:** the Pantheon+ fit did not rebuild within 0.05 of its stored
  log-posterior.
- **Even with a pass it would be PARTIAL, not MATCH:** the Pantheon+ fit lands between the two LQG values (0.259), but
  the DES Y5 fit gives 0.68.
- **Expectation logged before computing:** NO MATCH.
- **Reading (MEANING at most):** the Pantheon+ number is a curiosity. It rests on a mapping with convention freedom
  (where the cosine's origin sits, and 1/γ = a/ϕ), on a dilaton pinned at ½, and on one of two fits. It is not
  evidence. The mirror failure (0.087) is small; why the Pantheon+ rebuild differs from the stored minimum is not yet
  known.
