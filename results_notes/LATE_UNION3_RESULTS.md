# LU results: the Late Twist's DES Y5 point on Union3

**Rule:** PREREGISTRATION_LATE_UNION3.md (locked 2026-11-02 14:23:26). **Fits:** the last finished 15:20:40.
**Scored by:** `lu_tf_score.py` (written before any result). **Tier:** EVIDENCE.

## Verdict

| Statistic | Value | Verdict |
|---|---|---|
| Δ_U = χ²(Late Twist) − χ²(ΛCDM), Union3, (F, m) fixed at the DES Y5 best point | **−1.82** | **WEAKENED** (−4 < Δ_U ≤ −1) |
| w0–wa vs ΛCDM on the same data (context only) | −15.00 | — |

**Expectation logged before running:** WEAKENED, about −1 to −3. It came out as expected.

## Per-dataset breakdown (`dataset_breakdown.py`)

| Dataset | Late Twist − ΛCDM |
|---|---|
| Union3 supernovae | −4.10 |
| DESI DR2 BAO | −1.12 |
| ACT DR6 | −0.33 |
| ACT DR6 lensing | +0.05 |
| Planck low-ℓ TT | +0.07 |
| SPT-3G D1 | +0.45 |
| Planck high-ℓ (ACT cut) | +0.52 |
| Planck low-ℓ EE | +2.64 |
| **Sum** | **−1.82** |

## Reading

- **The Union3 supernovae do prefer the late field (−4.10), less than DES Y5 (−8.89) but more than Pantheon+
  (−1.12).** The CMB then takes most of it back.
- **The +2.64 on Planck low-ℓ EE** is the reionisation multipoles. With (F, m) fixed, the minimiser settled on a
  different optical depth than in the ΛCDM fit (τ = 0.0675 against 0.0613, with ln(10¹⁰A_s) 3.067 against 3.057).
  **The total is not distorted by this** (`tau_audit.py`, post-hoc): τ trades against the other datasets along a
  nearly flat direction. The Late Twist DES Y5 cold restart lands at τ = 0.0714 with low-ℓ EE +3.15, yet its total is
  within 0.13 of the warm fit (τ = 0.0642, EE −0.29). So single-dataset rows that depend on τ (mainly low-ℓ EE, by
  ±2–3) are not meaningful alone; the totals are.
  *(An earlier version of this note said a fuller minimisation "could only make Δ_U more negative, by at most
  about 2.6". The τ audit does not support that, so it was withdrawn before any use.)*
- **The three supernova samples now give one picture:** DES Y5 −6.23 (PASS), DES-Dovekie −1.33 (WEAKENED),
  Union3 −1.82 (WEAKENED), Pantheon+ +0.09 (tie). The strong hint is specific to the original DES Y5 calibration.
  This matches the outside work on DES Y5's low-redshift supernovae (PATH_DECISION_2026-11-02.md).
- **w0–wa gains −15.00 on Union3.** That is close to Babu & Amendola's independent −13.53 for the same kind of data
  combination (arXiv:2610.23497), a cross-check of our pipeline. The minimal Late Twist trails w0–wa by about 13 here
  too.
- `Omega_m` ≈ 2.90 in the Late Twist file is the known CLASS bookkeeping for field runs (the field is counted inside
  Ω_m); the true Ω_m rule (S8_FIXED_CODE_RESULTS.md) applies.

## Files

- `fit_results/cmp_ax_spa_latetwist_gF0m0.102_union3_nlfix.json`, `cmp_ax_spa_lcdm_halofit_union3.json`,
  `cmp_ax_spa_w0wa_halofit_union3.json`
- `lu_tf_score.json`, `DATASET_BREAKDOWN.md`
