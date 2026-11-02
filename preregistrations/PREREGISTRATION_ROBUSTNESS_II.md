# Robustness II: is the result driven by DESI, and are the minima stable? Pre-registration

**Locked:** 2026-11-02 12:35:12 (time from Get-Date). Requested by Danny ("do all the work necessary for these people to take it
seriously… make the data speak for itself"). Gaps 3 and 7 of the 2 Nov gap review.

**Written before:** any run below exists. Fitter options added for these runs only (AEGIS early_late_spa.py):
- `_nobao` drops the DESI DR2 BAO likelihood;
- `_r4` is a cold restart: best of 4, started from the ΛCDM halofit reference and never warm-started.

Everything else (likelihoods, priors, settings) is unchanged.

## B2. BAO dissection (does each gain depend on DESI?)

| Model | Run (corrected code) | Reference |
|---|---|---|
| Late Twist, DES Y5 best (F = 1.00, m = 1.26) | ax_spa_latetwist_gF0m0.102_desy5_nobao_nlfix | ax_spa_lcdm_halofit_desy5_nobao |
| w0–wa, DES Y5 (context) | ax_spa_w0wa_halofit_desy5_nobao | same |
| Coupled Twist best (Pantheon+) | ax_spa_coupledtwist_gF0.4m-0.1_nobao_nlfix | ax_spa_lcdm_halofit_nobao |
| w0–wa, Pantheon+ (context) | ax_spa_w0wa_halofit_nobao | same |

- **The measures:**
  - gain_without = χ²(model, no BAO) − χ²(ΛCDM, no BAO);
  - gain_with = the known value with DESI: Late Twist DES Y5 −6.23; Coupled −7.91; w0–wa DES Y5 and Pantheon+ from
    the existing halofit runs;
  - r = gain_without / gain_with.
- **Verdict per model:**
  - **NOT DESI-DRIVEN** if r ≥ 0.5;
  - **PARTLY DESI-DRIVEN** if 0 < r < 0.5;
  - **DESI-DRIVEN** if r ≤ 0.
- The fixed (F, m) are kept at the with-DESI best point, which is a conservative choice: refitting (F, m) without
  DESI could only lower χ².

## R3. Cold restarts (are the reported minima reproducible from scratch?)

| Point | Cold run |
|---|---|
| Late Twist, DES Y5 best | ax_spa_latetwist_gF0m0.102_desy5_nlfix_r4 |
| Coupled Twist best | ax_spa_coupledtwist_gF0.4m-0.1_nlfix_r4 |

- **The measure:** Δ = χ²(cold) − χ²(reported).
- **Verdict:**
  - **STABLE** if |Δ| ≤ 1.0.
  - **IMPROVED** if Δ < −1.0. The reported minimum was not the best; every verdict using that point is recomputed
    with the cold minimum and logged as a deviation, and both are shown.
  - **COLD-START WORSE** if Δ > 1.0. The reported (warm) minimum stands, and minimiser sensitivity is reported.

## Expectations (logged before running; not rules)

| Test | Expected |
|---|---|
| Late Twist DES Y5 | PARTLY or NOT DESI-DRIVEN. The DES Y5 supernovae drive the preference for thawing |
| Coupled Twist | PARTLY DESI-DRIVEN |
| w0–wa | PARTLY DESI-DRIVEN. DESI is a main driver of the w0–wa preference in the literature |
| R3 | STABLE for both (best-of-2 warm results have agreed within about 1 before) |
