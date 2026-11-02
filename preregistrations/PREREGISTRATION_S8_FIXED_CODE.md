# S8 on the corrected code: does the Twist ease or worsen the growth tension? Pre-registration

**Locked:** 2026-11-02 12:10:03 (time from Get-Date). Gap 2 from the 2 Nov gap review; Danny: "Start where u think best".

**Written before:** any σ8 or S8 is computed on the fixed build. (On the original code these values were invalid: the B0 bug pulled the field into δ_m.)

## Points evaluated (no new fits; each best fit is evaluated once)

| Model | Run | Matching ΛCDM reference |
|---|---|---|
| Late Twist, Pantheon+ (NR best) | ax_spa_latetwist_gF0.4m-0.3_nlfix | ax_spa_lcdm_halofit |
| Late Twist, DES Y5 (NR best) | ax_spa_latetwist_gF0m0.102_desy5_nlfix | ax_spa_lcdm_halofit_desy5 |
| Coupled Twist (NR best) | ax_spa_coupledtwist_gF0.4m-0.1_nlfix | ax_spa_lcdm_halofit |

- **Builds:**
  - Late Twist and the ΛCDM references run on AxiCLASS_nlfix. ΛCDM has no scalar field, so the fix does not touch it.
  - The Coupled Twist runs on AxiCLASS_coupled_nlfix.
- **Computed:**
  - S8 = σ8 √(Ω_m/0.3), with σ8 from CLASS;
  - Ω_m = (ρ_cdm + ρ_b + ρ_ncdm)/ρ_crit today, from the background table, never CLASS's derived Ω_m (which counts the field).

## Weak-lensing targets (fetched before the lock)

- **Primary:** DES Y6 3×2pt (Abbott et al., arXiv:2601.14559, ΛCDM): **S8 = 0.789 ± 0.012**.
- **Cross-check:** KiDS-Legacy cosmic shear (arXiv:2503.19442): S8 = 0.815, with σ = 0.016 if the model is above and 0.021 if below.

## Rule

- **Tension measure:** t = (S8_model − S8_WL)/σ, for each model and for its ΛCDM reference.
- **Verdict per model (primary target):**
  - **EASES** if |t_model| < |t_ΛCDM| − 0.5;
  - **WORSENS** if |t_model| > |t_ΛCDM| + 0.5;
  - **NEUTRAL** otherwise.
- The KiDS-Legacy verdicts are reported alongside.
- **Limit:** best-fit values only; no S8 uncertainty from posteriors (that is gap 1, MCMC).

## Expectation (logged before computing; not a rule)

NEUTRAL for all three on DES Y6.
- The late field adds a few percent of dark energy that moves only at z < 2, and changes growth only slightly.
- The Coupled Twist with β ≈ −0.04 could shift σ8 by about 1%.
