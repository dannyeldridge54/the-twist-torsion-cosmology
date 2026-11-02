# LZ results: where in redshift does the Late Twist's DES Y5 supernova gain come from?

**Rule:** PREREGISTRATION_SOLAR_LOWZ.md (locked 2026-11-02 15:17:31). **Computed:** `lowz_split.py` (evaluation
15:22:36–15:26:20) → `lowz_split.json`. **Tier:** EVIDENCE.

## Mirror (must pass first): PASS

| Point | χ²_SN recomputed | χ²_SN from the likelihood | χ²_SN stored |
|---|---|---|---|
| Late Twist, DES Y5 | 1639.83993 | 1639.83993 | 1639.8399 |
| ΛCDM, DES Y5 | 1648.72915 | 1648.72915 | 1648.7291 |

The rebuilt models also reproduce the stored log-posteriors within 0.003.

## Verdict: **CALIBRATION-SENSITIVE** (r = −0.06)

| Δχ²_SN (Late Twist − ΛCDM) | Value |
|---|---|
| All 1829 supernovae (Δ_full) | **−8.89** |
| z > 0.1 only (1632 SNe, own absolute magnitude) (Δ_high) | **+0.53** |
| z ≤ 0.1 only (197 SNe, own absolute magnitude) (Δ_low) | −0.29 |
| r = Δ_high / Δ_full | **−0.06** |

**Expectation logged before computing:** CALIBRATION-SENSITIVE. It came out as expected, and more strongly than
expected.

## What it means

- **Neither half prefers the Twist on its own.** The −8.89 exists only when the nearby (mostly external, low-z)
  supernovae and the DES supernovae are tied together through **one shared absolute magnitude.** All of the gain is
  the relative offset between the two groups: the same low-z intercept offset identified by Efstathiou (2025),
  Huang et al. (arXiv:2502.04212) and Zhang (MNRAS 552, 2026).
- **The same holds for w0–wa** (post-hoc context, `lowz_context_ax_spa_w0wa_halofit_desy5.json`; no rule):
  Δ_full −11.23, Δ_high +1.94, Δ_low −0.55, r = −0.17. So this is a property of the DES Y5 data, not of our model.
  Any evolving-dark-energy model's DES Y5 supernova gain comes from that offset.
- **Combined with LD and LU:** the Late Twist's best result (DES Y5, −6.23) rests on a low-z/high-z calibration offset.
  It weakens on the recalibrated DES-Dovekie (−1.33) and on Union3 (−1.82). **The Late Twist hint should now be
  described as a DES Y5 calibration effect, not evidence for the field.**
- **Caveat (fixed in advance):** no refit. Zhang (2026) refits after truncation and still finds about 2σ residual for
  w0–wa on DES Y5. A refit could recover part of a gain for the Twist too, but the split shows it cannot come from either
  half alone at these parameters.

## Files

`lowz_split.py`, `lowz_split.json`, `lowz_context_ax_spa_w0wa_halofit_desy5.json`; the `lowz_*.npz` evaluation
files (data vectors and distances) are kept locally and are not part of the release (large, and regenerable).
