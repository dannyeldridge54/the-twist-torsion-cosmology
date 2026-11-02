# Where each model gains and loses: per-dataset delta chi2 vs its LCDM reference

Read straight from the stored best fits (`dataset_breakdown.py`); no fitting. Negative means the model fits that dataset better than LCDM does at their respective best fits. Calibration priors are excluded, so the per-dataset entries sum to the total delta chi2 within rounding.

**Caution (tau_audit.py):** the optical depth tau moves by up to +-0.008 between fits along a near-flat direction, and Planck low-l EE moves by +-2-3 with it while the total barely changes. Rows that depend on tau (mainly low-l EE) are not meaningful alone; the totals are.

## Late Twist, Pantheon+ (corrected): total +0.09

| Dataset | delta chi2 |
|---|---|
| Pantheon+ | -1.12 |
| SPT-3G D1 | -0.52 |
| Planck high-l (ACT cut) | -0.15 |
| ACT DR6 lensing | +0.04 |
| Planck low-l TT | +0.12 |
| Planck low-l EE | +0.27 |
| ACT DR6 | +0.37 |
| DESI DR2 BAO | +1.09 |
| *sum* | +0.09 |

## Late Twist, DES Y5 (corrected): total -6.23

| Dataset | delta chi2 |
|---|---|
| DES Y5 | -8.89 |
| Planck low-l EE | -0.29 |
| Planck high-l (ACT cut) | -0.13 |
| Planck low-l TT | +0.13 |
| DESI DR2 BAO | +0.27 |
| ACT DR6 lensing | +0.59 |
| SPT-3G D1 | +0.63 |
| ACT DR6 | +1.47 |
| *sum* | -6.23 |

## Late Twist, DES Y5, no DESI: total -5.33

| Dataset | delta chi2 |
|---|---|
| DES Y5 | -6.07 |
| Planck high-l (ACT cut) | -0.88 |
| ACT DR6 lensing | -0.12 |
| Planck low-l TT | -0.05 |
| SPT-3G D1 | +0.09 |
| Planck low-l EE | +0.76 |
| ACT DR6 | +0.95 |
| *sum* | -5.33 |

## Late Twist, DES-Dovekie (corrected, LD): total -1.33

| Dataset | delta chi2 |
|---|---|
| DES-Dovekie | -4.69 |
| SPT-3G D1 | -0.19 |
| Planck low-l TT | +0.01 |
| Planck high-l (ACT cut) | +0.25 |
| Planck low-l EE | +0.35 |
| DESI DR2 BAO | +0.35 |
| ACT DR6 lensing | +0.69 |
| ACT DR6 | +1.89 |
| *sum* | -1.33 |

## Late Twist, Union3 (corrected, LU): total -1.82

| Dataset | delta chi2 |
|---|---|
| Union3 | -4.10 |
| DESI DR2 BAO | -1.12 |
| ACT DR6 | -0.33 |
| ACT DR6 lensing | +0.05 |
| Planck low-l TT | +0.07 |
| SPT-3G D1 | +0.45 |
| Planck high-l (ACT cut) | +0.52 |
| Planck low-l EE | +2.64 |
| *sum* | -1.82 |

## w0-wa, Union3 (context): total -15.00

| Dataset | delta chi2 |
|---|---|
| Union3 | -6.12 |
| DESI DR2 BAO | -4.72 |
| ACT DR6 | -1.88 |
| Planck low-l EE | -1.78 |
| SPT-3G D1 | -1.05 |
| ACT DR6 lensing | -0.09 |
| Planck low-l TT | +0.19 |
| Planck high-l (ACT cut) | +0.45 |
| *sum* | -15.00 |

## Coupled Twist, Pantheon+ (corrected): total -7.91

| Dataset | delta chi2 |
|---|---|
| DESI DR2 BAO | -4.37 |
| Pantheon+ | -2.16 |
| SPT-3G D1 | -1.20 |
| Planck low-l EE | -1.20 |
| ACT DR6 | -0.42 |
| Planck low-l TT | +0.13 |
| ACT DR6 lensing | +0.29 |
| Planck high-l (ACT cut) | +1.02 |
| *sum* | -7.91 |

## Coupled Twist, no DESI: total +0.74

| Dataset | delta chi2 |
|---|---|
| Planck high-l (ACT cut) | -1.62 |
| Pantheon+ | -1.08 |
| ACT DR6 lensing | -0.69 |
| Planck low-l TT | -0.40 |
| Planck low-l EE | +1.15 |
| SPT-3G D1 | +1.39 |
| ACT DR6 | +1.99 |
| *sum* | +0.74 |

## w0-wa, DES Y5 (context): total -19.76

| Dataset | delta chi2 |
|---|---|
| DES Y5 | -11.23 |
| DESI DR2 BAO | -5.25 |
| Planck low-l EE | -1.91 |
| ACT DR6 | -1.16 |
| SPT-3G D1 | -0.71 |
| ACT DR6 lensing | -0.02 |
| Planck low-l TT | +0.07 |
| Planck high-l (ACT cut) | +0.45 |
| *sum* | -19.76 |

## w0-wa, Pantheon+ (context): total -9.96

| Dataset | delta chi2 |
|---|---|
| DESI DR2 BAO | -3.72 |
| Pantheon+ | -2.52 |
| Planck low-l EE | -1.92 |
| ACT DR6 | -1.39 |
| SPT-3G D1 | -0.62 |
| ACT DR6 lensing | -0.08 |
| Planck low-l TT | +0.12 |
| Planck high-l (ACT cut) | +0.16 |
| *sum* | -9.96 |

## Early field, all CMB + DESI + Pantheon+ (CAMB): total -5.63

| Dataset | delta chi2 |
|---|---|
| Planck high-l (ACT cut) | -2.66 |
| Planck low-l EE | -2.08 |
| ACT DR6 | -1.57 |
| DESI DR2 BAO | -0.76 |
| Planck low-l TT | -0.63 |
| ACT DR6 lensing | +0.19 |
| Pantheon+ | +0.33 |
| SPT-3G D1 | +1.55 |
| *sum* | -5.63 |

