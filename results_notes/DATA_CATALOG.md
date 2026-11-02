# Data catalog: every public dataset that can test the Twist

Written 2 Nov 2026.
- **Status:** *used* = in the published fits; *not yet* = public but not used; *future* = not released yet.
- **Rule:** before any *not yet* or *future* dataset is fitted, its prediction and verdict rule are written and locked
  (as for every test so far).

## What the stored fits already say (`dataset_breakdown.py` → DATASET_BREAKDOWN.md)

Per-dataset Δχ² against ΛCDM at the best fits. Negative means the model fits that dataset better.

| Model | Gains from | Loses on | Reading |
|---|---|---|---|
| **Late Twist, DES Y5** (−6.23) | DES Y5 supernovae −8.89 | ACT DR6 +1.47, SPT-3G +0.63, DESI +0.27 | **A single-dataset hint.** It lives in the one supernova sample that has a known calibration offset |
| Late Twist, DES-Dovekie (−1.33) | Dovekie supernovae −4.69 | ACT DR6 +1.89 | Recalibration halves the supernova pull |
| Late Twist, Pantheon+ (+0.09) | Pantheon+ −1.12, SPT −0.52 | DESI +1.09 | A tie |
| **w0–wa, DES Y5** (−19.76) | supernovae −11.2, DESI −5.2, ACT −1.2, SPT −0.7 | none | **Broad support from every probe** |
| Coupled Twist (−7.91) | DESI −4.37, Pantheon+ −2.16 | Planck high-ℓ +1.02 | DESI-driven: without DESI the CMB turns against it |
| Early field (−5.63) | ACT −1.57, Planck high-ℓ −2.66 | SPT-3G +1.55 | Planck/ACT hint, not seen by SPT |

**Why the Twist loses to w0–wa:**
- DESI's distances favour an equation of state that crosses w = −1 (the "phantom" direction). A canonical thawing
  field like the Twist cannot cross it, so it cannot follow DESI's preferred path, and w0–wa gains on every probe.
- This is the physical limit of the minimal model, now quantified dataset by dataset.

## Datasets

| Dataset | Measures | Twist prediction there | Status |
|---|---|---|---|
| Planck 2018 low-ℓ TT/EE | CMB, reionisation | early field: small gain | used |
| ACT DR6 (CMB-only, with Planck cut) | CMB damping tail | early field gains; late field slightly against | used |
| ACT DR6 lensing | matter clumping | neutral | used |
| SPT-3G D1 (TnE lite) | CMB | early field against (+1.55) | used |
| DESI DR2 BAO | distances, z 0.3–2.3 | late field neutral; coupled field gains | used |
| Pantheon+ | supernovae z < 2.3 | tie | used |
| DES Y5 / DES-Dovekie | supernovae | late field gains (Y5); halved (Dovekie) | used |
| **Union3 supernovae** | supernovae, independent calibration | the third supernova test of the late hint: the decisive cheap test | **used** (LU: WEAKENED, −1.82; TF/TF-P Union3 fits running) |
| **Growth (fσ8)**: BOSS/eBOSS RSD, DESI full-shape | structure growth | late field: same as ΛCDM; coupled: about 1% faster | **not yet** |
| **Cosmic chronometers** H(z) | expansion, no ruler | late field: H(z) within about 1% of ΛCDM, thawing below z ≈ 1.5 | **not yet** |
| SPT-3G lensing (installed) | clumping | neutral | **not yet** (gap B3) |
| KiDS-Legacy / DES Y6 shear likelihoods | S8 | late neutral; coupled worse | not yet (only S8 compared) |
| Planck / BICEP-Keck multipole-dependent EB | rotation vs scale | R = 0.997 (if photon-coupled) | not yet (context only) |
| GWTC dark sirens | GW propagation, H0 | BI field: GR-like propagation | not yet |
| DESI DR3, Euclid DR1, Rubin/LSST supernovae | expansion and growth, much tighter | thawing shape: switch-on at z ≈ 1.5, half by z ≈ 0.38 | future: lock predictions first |
| Simons Observatory, LiteBIRD | low-ℓ EB rotation | R = 0.997 | future |

## Next steps (in order of value per effort)

1. **Union3 supernovae** with the late field at the DES Y5 best point: one fit plus a ΛCDM reference, with the rule
   locked first. This decides whether the single-dataset hint is a DES Y5 calibration artefact.
2. **Prediction checks with no refitting:** compute fσ8(z) and H(z) from the stored best fits and compare with the
   published RSD and chronometer tables (values taken from the primary papers).
3. **MCMC posteriors and evidence** for the late field with all supernova samples (days of PC time).
