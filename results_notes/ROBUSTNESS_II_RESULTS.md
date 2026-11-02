# Robustness II: results under the locked rule

**Rule:** PREREGISTRATION_ROBUSTNESS_II.md, locked 2026-11-02 12:35:12, sha256 25480e62…5f06 (commit 8d43c34).

**Scoring:** applied mechanically by `robustness2_score.py`, with the output in `robustness2_score.json`.

**Fits:** run under the new names `_nobao` (DESI DR2 dropped) and `_r4` (cold restart, best of 4). Launch incidents
are logged in SCALES_CHECKPOINT.md (12:52); no data was affected.

## B2: BAO dissection (does each gain depend on DESI?)

The measure is r = gain without DESI / gain with DESI. Verdicts: **NOT DESI-DRIVEN** if r ≥ 0.5, **PARTLY** if
0 < r < 0.5, **DESI-DRIVEN** if r ≤ 0.

| Model | Gain with DESI | Gain without DESI | r | Verdict |
|---|---|---|---|---|
| **Late Twist, DES Y5** (F = 1.00, m = 1.26 fixed) | −6.23 | −5.33 | 0.86 | **NOT DESI-DRIVEN** |
| w0–wa, DES Y5 (context) | −19.76 | −9.77 | 0.49 | PARTLY DESI-DRIVEN |
| **Coupled Twist** (Pantheon+) | −7.91 | +0.74 | −0.09 | **DESI-DRIVEN** |
| w0–wa, Pantheon+ (context) | −9.96 | −3.36 | 0.34 | PARTLY DESI-DRIVEN |

## R3: cold restarts

Scored by `robustness2_score.py` (the last `_r4` fit finished 15:11:11, 2 Nov). Δ = χ²(cold, best of 4) − χ²(reported).

| Point | reported | cold (best of 4) | Δ | Verdict |
|---|---|---|---|---|
| Late Twist, DES Y5 | 2639.79 | 2639.91 | +0.13 | **STABLE** |
| Coupled Twist | 2394.35 | 2396.72 | +2.37 | **COLD-START WORSE** |

- **Late Twist:** four cold starts land within 0.13 of the reported minimum. The −6.23 is a reproducible minimum.
- **Coupled Twist:** per the locked rule, the reported (warm) minimum stands. The minimiser is sensitive here: four
  random cold starts do not reach it, and their best is 2.37 higher. From cold starts alone the gain over ΛCDM would read
  −5.54 instead of −7.91.
  - This fits the known shape of the β profile (two narrow modes at ±0.05 with a solver failure near the edges).
  - The expectation logged before the run (STABLE for both) was wrong for the Coupled Twist.
  - It is a third caution on the coupled result, after DESI-DRIVEN and the S8 cost.

## Reading

- **The Late Twist's DES Y5 hint is not a DESI effect.** It keeps 86% of its gain without DESI, so it comes from the
  supernovae and the CMB. The (F, m) values were fixed at the with-DESI best point, so refitting could only make the
  no-DESI gain larger.
  - The hint is still weak (1.27σ global) and weakens on DES-Dovekie. Robustness to DESI does not make it stronger.
  - Without DESI the gap to w0–wa narrows (−5.33 against −9.77, versus −6.23 against −19.76 with DESI), but w0–wa
    still fits better.
- **The Coupled Twist's gain is entirely DESI-driven.** Without DESI it is slightly worse than ΛCDM. This joins its
  S8 cost (WORSENS) as a second reason to treat the coupled result with caution.
- **w0–wa itself leans on DESI** for half to two-thirds of its preference. That matches the literature.

The expectations logged before the run were: Late Twist PARTLY or NOT; Coupled PARTLY; w0–wa PARTLY. The Late Twist
and w0–wa came out as expected. The Coupled Twist came out stronger than expected (DESI-DRIVEN).
