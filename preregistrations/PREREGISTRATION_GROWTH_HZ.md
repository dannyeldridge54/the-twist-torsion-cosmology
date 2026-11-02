# Pre-registration: GH, a no-refit prediction check of the stored best fits against cosmic chronometers H(z) and growth fσ8(z)

**Locked:** 2026-11-02 15:31:34
**Written** before any prediction was computed. The data were fetched from primary sources first and frozen in
`data/growth_hz_data.json` (provenance inside). Requested by Danny ("attack data"); DATA_CATALOG.md step 2.

## Data (fixed)

- **H(z):** the 15 cosmic-chronometer points (BC03) from Moresco's public pipeline, with the full covariance built
  exactly as in its `CC_covariance.ipynb`: statistical diagonal + IMF + stellar-population-model (`spsooo`) terms,
  fully correlated. This dataset is independent of everything in our fits.
- **fσ8(z):** the six SDSS final RSD-only values (Alam et al. 2021, Table III), diagonal errors. Caveat: same galaxies
  as some BAO we do not use; DESI DR2 BAO is a different survey.

## Models (stored best fits, no refit)

| Label | Model | ΛCDM reference |
|---|---|---|
| LT-P | Late Twist, Pantheon+ (`ax_spa_latetwist_gF0.4m-0.3_nlfix`) | `ax_spa_lcdm_halofit` |
| LT-D | Late Twist, DES Y5 (`ax_spa_latetwist_gF0m0.102_desy5_nlfix`) | `ax_spa_lcdm_halofit_desy5` |
| CT | Coupled Twist (`ax_spa_coupledtwist_gF0.4m-0.1_nlfix`) | `ax_spa_lcdm_halofit` |
| context | w0–wa, Pantheon+ and DES Y5 (`ax_spa_w0wa_halofit`, `_desy5`) | same as above |

Each model is rebuilt with `early_late_spa.make()` and evaluated at its stored minimum (as in LZ). The mirror is the
same: the rebuilt log-posterior must match the stored one within 0.05, or no verdict.

## Statistic and verdict

- χ²_H = rᵀC⁻¹r with r = H_model(z) − H_obs, using the model's own H0 (no free parameter); χ²_f = Σ(fσ8_model −
  fσ8_obs)²/σ², with CLASS's `effective_f_sigma8`.
- For each Twist model and each dataset, Δ = χ²(model) − χ²(ΛCDM reference). Also reported: Δ_H + Δ_f.
- **Verdict per model and dataset:** **SUPPORTS** if Δ ≤ −2; **NEUTRAL** if −2 < Δ < +2; **DISFAVOURS** if Δ ≥ +2.
- w0–wa rows are context only (no verdict).

## Expectation (not a rule)

NEUTRAL everywhere for the Late Twist (H(z) within about 1% of ΛCDM; growth unchanged). The Coupled Twist is NEUTRAL
or DISFAVOURS on fσ8 (about 1% faster growth; it already WORSENS S8).
