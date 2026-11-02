# S8 on the corrected code: results under the locked rule

**Rule:** PREREGISTRATION_S8_FIXED_CODE.md, locked 2026-11-02 12:10:03, sha256 f6b1d78e…5ba1 (commit bb5df01). Computed right after and scored mechanically.

**Code:** AEGIS nlfix/s8_check.py, output in results/s8_fixed_code.json.

## Numbers

| Point | σ8 | Ω_m (true) | **S8** |
|---|---|---|---|
| ΛCDM ref, Pantheon+ | 0.8128 | 0.3035 | 0.8175 |
| **Late Twist, Pantheon+** | 0.8114 | 0.3064 | **0.8201** |
| ΛCDM ref, DES Y5 | 0.8139 | 0.3040 | 0.8193 |
| **Late Twist, DES Y5** | 0.7998 | 0.3143 | **0.8186** |
| **Coupled Twist** (ref: ΛCDM Pantheon+) | 0.8240 | 0.3026 | **0.8276** |

## Verdicts

The tension measure is t = (S8 − S8_WL)/σ.

**Primary target, DES Y6 3×2pt: 0.789 ± 0.012**

| Model | t (model) | t (ΛCDM) | Verdict |
|---|---|---|---|
| Late Twist, Pantheon+ | 2.59 | 2.38 | **NEUTRAL** |
| Late Twist, DES Y5 | 2.46 | 2.53 | **NEUTRAL** |
| Coupled Twist | 3.22 | 2.38 | **WORSENS** (+0.84) |

**Cross-check, KiDS-Legacy: 0.815 (+0.016/−0.021)**

| Model | t (model) | t (ΛCDM) | Verdict |
|---|---|---|---|
| Late Twist, Pantheon+ | 0.32 | 0.16 | NEUTRAL |
| Late Twist, DES Y5 | 0.23 | 0.27 | NEUTRAL |
| Coupled Twist | 0.79 | 0.16 | **WORSENS** (+0.63) |

## Reading

- **Late Twist: no growth cost and no growth help.**
  - S8 moves by less than 0.003 against ΛCDM on both supernova sets.
  - With DES Y5, σ8 drops but Ω_m rises, and the two cancel.
  - The Late Twist's DES Y5 gain does not come at the price of structure growth.
- **Coupled Twist: a new cost found.**
  - Its dark-matter coupling (β ≈ −0.04) raises σ8 by about 1.4%, pushing S8 0.84σ further from DES Y6.
  - Its −7.91 χ² gain partly trades against growth data that are **not** in the fit. That is a caveat for the Coupled Twist headline.
  - The expectation logged before computing ("NEUTRAL; about 1% possible for the Coupled Twist") was right for the Late Twist but missed the Coupled verdict by 0.34σ.
- **ΛCDM itself sits 2.4–2.5σ above DES Y6.** This matches DES's own 2.6σ statement, a mirror check that the pipeline's S8 is sane. CLASS's raw Ω_m for the field runs comes out at about 3 (it counts the field wrongly), confirming that the "true Ω_m" rule was needed.
- **Limit:** best-fit values only. Uncertainties need the posteriors (gap 1, MCMC).
