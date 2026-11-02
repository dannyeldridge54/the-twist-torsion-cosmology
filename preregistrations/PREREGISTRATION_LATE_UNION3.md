# LU: does the Late Twist's DES Y5 hint appear in an independent supernova sample (Union3)? Pre-registration

**Locked:** 2026-11-02 14:23:26 (time from Get-Date). Requested by Danny ("attack dark energy with our model"). From DATA_CATALOG.md step 1.

**Written before:** any Union3 fit with the AxiCLASS late-field pipeline exists.

**Why:**
- DATASET_BREAKDOWN.md shows that the Late Twist's DES Y5 gain (−6.23) comes entirely from the DES Y5 supernovae (−8.89).
- DES Y5 has a known calibration offset, and the corrected DES-Dovekie sample halves the pull (LD: −1.33, WEAKENED).
- Union3 is an independent compilation with its own calibration, so it decides whether the hint is a supernova
  systematic.

## Runs (corrected code; same CMB, DESI DR2 and settings as every late fit; only the supernova likelihood changes to `sn.union3`)

| Run | Role |
|---|---|
| ax_spa_latetwist_gF0m0.102_union3_nlfix | Late Twist at the DES Y5 best point (F = 1.00 M_Pl, m = 1.26 H₀), fixed before Union3 is seen |
| ax_spa_lcdm_halofit_union3 | ΛCDM reference (halofit), same data |
| ax_spa_w0wa_halofit_union3 | w0–wa on the same data (context only, no verdict) |

## Rule (the same thresholds as LD)

- **Statistic:** Δ_U = χ²(Late Twist, Union3) − χ²(ΛCDM halofit, Union3).
- **Verdict:**
  - **CONFIRMED** if Δ_U ≤ −4: the hint survives an independent supernova sample.
  - **WEAKENED** if −4 < Δ_U ≤ −1.
  - **NOT CONFIRMED** if Δ_U > −1: the DES Y5 hint does not appear in Union3.
- **Conservative choice:** (F, m) are fixed at the DES Y5 best point and not re-optimised for Union3. This can only
  make Δ_U less negative.
- **A failed or non-finite run** counts as NOT CONFIRMED (code-limited) and is not retried with new settings.
- **Reported beside the verdict:** the per-dataset breakdown (`dataset_breakdown.py`) and the w0–wa context.

## Expectation (logged before running; not a rule)

WEAKENED: about −1 to −3. Union3 is known to prefer evolving dark energy somewhat less strongly than DES Y5, and the
DES Y5 pull partly reflects its calibration.
