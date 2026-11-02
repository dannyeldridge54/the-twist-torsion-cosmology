# GH results: stored best fits vs cosmic chronometers H(z) and SDSS fσ8 (no refit)

**Rule:** PREREGISTRATION_GROWTH_HZ.md (locked 2026-11-02 15:31:34). **Data:** `data/growth_hz_data.json` (frozen from
Moresco's pipeline and Alam et al. 2021 Table III before the lock). **Computed:** `growth_hz.py` (scored 16:10:38) →
`growth_hz.json`. **Tier:** EVIDENCE.

| Model | Δχ²_H vs ΛCDM | Verdict H | Δχ²_f vs ΛCDM | Verdict f | χ²_H / χ²_f (model; ΛCDM) | H0 (model; ΛCDM) |
|---|---|---|---|---|---|---|
| Late Twist, Pantheon+ | −0.01 | **NO VERDICT** (mirror) | +0.03 | **NO VERDICT** (mirror) | 6.25 / 6.28; 6.25 / 6.25 | 67.87; 68.17 |
| Late Twist, DES Y5 | +0.03 | **NEUTRAL** | +0.42 | **NEUTRAL** | 6.28 / 6.65; 6.25 / 6.23 | 66.94; 68.13 |
| Coupled Twist | +0.10 | **NEUTRAL** | −0.31 | **NEUTRAL** | 6.35 / 5.94; 6.25 / 6.25 | 68.21; 68.17 |
| w0–wa, Pantheon+ (context) | +0.25 | — | −0.16 | — | 6.51 / 6.09 | 67.76 |
| w0–wa, DES Y5 (context) | +0.27 | — | −0.03 | — | 6.52 / 6.20 | 66.94 |

**Expectation logged before computing:** Late Twist NEUTRAL everywhere; Coupled NEUTRAL or DISFAVOURS on fσ8. It came
out NEUTRAL everywhere. The Coupled Twist's fσ8 is slightly better (−0.31), not worse.

## Reading

- **These datasets cannot separate the models.** Every Δ is below 0.5, with χ² ≈ 6 for 15 H(z) points and ≈ 6 for six
  fσ8 points in all models. Both datasets agree well with all of them; their errors are too large to tell them apart.
- So the Twist passes two independent, unseen datasets, but so does ΛCDM. This is a consistency check, not support.
- **Open item:** the Pantheon+ Late Twist fit (`gF0.4m-0.3_nlfix`) rebuilds 0.087 away from its stored log-posterior.
  This is the second time (LQ also). The rule gives no verdict for it. The cause (likely the closure shooting or the
  stored point's precision) is not yet found. The DES Y5 fit rebuilds within 0.002.

## Files

`growth_hz.py`, `growth_hz.json`, `gh_*.json` (predictions per model), `data/growth_hz_data.json`.
