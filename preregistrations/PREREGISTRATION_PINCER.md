# Pre-registration: PC, the pincer test (the early universe predicts the late universe)

**Locked:** 2026-11-02 16:22:30
**Idea (Danny):** "start at big bang and set the numbers up middle out … the data can get pincered inside out, outside
in, with correlating data to support it."
**Written** before any of these fits exist.

## Design

- **Early end:** fit each model to the CMB alone (Planck low-ℓ TT/EE, ACT DR6 + Planck high-ℓ cut, ACT DR6 lensing,
  SPT-3G D1); no BAO and no supernovae. Fitter suffix `_cmbonly`.
- **Late end:** at that CMB-only best fit, with no refit, compute the χ² of the late data:
  - DESI DR2 BAO;
  - each supernova sample separately: Pantheon+, DES-Dovekie, Union3. **DES Y5 is excluded** (LZ:
    CALIBRATION-SENSITIVE).
- **Models** (all with their dark-energy parameters fixed, so the CMB fit cannot simply absorb them):
  - ΛCDM (halofit), `ax_spa_lcdm_halofit_cmbonly`;
  - Late Twist at the DES Y5 point (F = 1.00, m = 1.26 H₀), `ax_spa_latetwist_gF0m0.102_cmbonly_nlfix`;
  - Late Twist at the Pantheon+ point (F = 2.51, m = 0.50 H₀), `ax_spa_latetwist_gF0.4m-0.3_cmbonly_nlfix`.
- **Statistic:** Δ_s = χ²_late,s(model) − χ²_late,s(ΛCDM) for each supernova sample s (BAO included in every χ²_late).

## Verdict (per Twist model)

- **SUPPORTS** if Δ_s ≤ −2 for at least two of the three samples: the CMB, which knows nothing about the late data,
  points the late universe the Twist's way.
- **DISFAVOURS** if Δ_s ≥ +2 for at least two of the three samples.
- **NEUTRAL** otherwise.

**Mirror (required first):** at the ΛCDM CMB-only point, the rebuilt CMB χ² must match the stored fit within 0.05;
otherwise no verdict.

## Expectation (not a rule)

NEUTRAL for both. Fixed thawing fields change late distances by less than 1%. The CMB-only fits will mostly track ΛCDM.
