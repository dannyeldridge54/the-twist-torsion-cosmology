# Late Twist results (PREREGISTRATION_LATE_TWIST.md), with a minimiser failure flagged

**Run:** `ax_spa_latetwist`, rerun with the minimiser guard (deviation logged 07:24 CT, commit 8c2c095). It finished on 1 November 2026
at 07:41 CT.

**References:** `ax_spa_lcdm_halofit` and `ax_spa_w0wa_halofit`, as set by the halofit deviation.

## Verdicts, applied exactly as written

| Test | Number | Verdict |
|---|---|---|
| L1 (vs ΛCDM) | Δχ² = +11.64, ΔAIC = +15.64 | **FAIL** |
| L2 (vs w0–wa) | D = +21.60 | **WORSE** |
| L3 (natural range) | F = 0.536 M_Pl, m = 2.04 H₀ | **CONSISTENT** (a weak test; not at a prior edge) |
| Shared F (PREREGISTRATION_SHARED_F.md) | F_late / F_early = 3.69 (R = +0.57) | **DIFFERENT** |

**Reported beside the verdicts:**
- **The fit's own values:** H₀ = 67.00, S8 = 0.779.
- **The field at the best fit:** w today = −0.922, CPL-equivalent w0 = −0.935, wa = −0.103 (fit residual ≤ 0.013).

## Why these verdicts do not test the model: the minimiser did not find the minimum

A post-hoc diagnostic (`axiclass/probe_corner.py`) evaluated χ² with the cosmological and calibration parameters held at
the ΛCDM (halofit) best fit:

| (F, m) | χ² | vs ΛCDM |
|---|---|---|
| Late Twist best fit (0.54 M_Pl, 2.04 H₀) | **2402.66** | +0.40 |
| (3.16 M_Pl, 0.50 H₀), near the ΛCDM-like corner | 2402.64 | +0.38 |
| (3.16 M_Pl, 1.00 H₀) | 2409.62 | +7.36 |
| (3.16, 0.32) and (2.00, 0.32) | ∞ | closure impossible |

**What this shows:**
- At the reported best-fit F and m, simply moving the other parameters to the ΛCDM best fit gives χ² = 2402.66.
  That is **11.24 lower than the minimiser's "best fit"** of 2413.90.
- Both bobyqa restarts reported "converged", but to a poor point. The guarded landscape (flat penalties around the
  region where the closure is impossible) most likely stalled the trust region.
- **So the official L1 and L2 verdicts stand as judged, but they reflect a minimiser failure, not the model.** The
  diagnostic points show the model reaches at least χ² ≈ ΛCDM + 0.4 without any optimisation of the other parameters.
  The true minimum is lower still.
- The probe also shows that the prior's corner (m ≥ 0.32 H₀ with F ≤ 3.16 M_Pl) cannot reach a fully frozen,
  ΛCDM-like field. The nearest viable point (F = 3.16, m = 0.5) costs +0.38 before refitting.

**What a valid test needs (a deviation, which needs the author's OK because the result has been seen):**
- Rerun `ax_spa_latetwist` with the cosmological references centred on the ΛCDM halofit best fit, and best of 4.
- Same priors and rules. The failed run stays on record.
- The same fix would apply to `ax_spa_latetwist_desy5` before robustness batch 2 starts.

**Shared F:** DIFFERENT either way. The two diagnostic points that fit well have F between 0.5 and 3.2 M_Pl, all more
than 3 times F_early = 0.145 M_Pl, unless a refit lands below 0.48 M_Pl.

**Post-hoc observation (not a test):** the construction's natural scale is s = √(3/2) M_Pl = 1.22 M_Pl. I meant to
pre-register "F_late = s", but the fit finished before I could, so it is reported only as a note: the current
(unreliable) best fit F = 0.54 is 0.44 s.

## Rerun (approved; AxiCLASS ΛCDM start, best of 4; finished 1 November 2026)

All 4 restarts reported "converged", at −log posterior 1172.42, 1171.26, 1174.20 and 1170.79: a spread of 6.8 in χ².

**Verdicts, applied exactly as written:**

| Test | Number | Verdict |
|---|---|---|
| L1 (vs ΛCDM) | Δχ² = +3.23 (χ² 2405.49) | **FAIL** |
| L2 (vs w0–wa) | D = +13.18 | **WORSE** |
| L3 (natural range) | F = 1.02 M_Pl, m = 1.20 H₀ | **CONSISTENT** (weak test; not at a prior edge) |
| Shared F | F_late / F_early = 7.0 | **DIFFERENT** |

**Reported beside them:** H₀ = 67.25, S8 = 0.783.

**The minimiser is still stuck** (corner probe, as the loop rules require). At the rerun's own best (F, m), with the other
parameters moved to the ΛCDM halofit best fit, χ² = 2402.94, which is **+0.68** above ΛCDM, against the reported +3.23.
Near the ΛCDM-like corner (F = 3.16, m = 0.5) it is **+0.38**. So:
- the true minimum is at most +0.38, and refitting the other parameters can only lower it;
- whether it falls **below** ΛCDM, which would turn L1 from FAIL into INCONCLUSIVE or better, is not yet known;
- the published thawing-quintessence results suggest a modest gain of order −3 is possible.

**What would settle it** needs the author's OK, because the result has been seen:
- start the minimiser *at* the probe point, with the 13 parameters set there, using smaller initial steps for F and m;
- or switch the Late Twist to a different minimiser (scipy) that copes better with the guarded landscape.

**Meanwhile, the official verdicts stand as written.** Robustness batch 2 (the Late Twist with DES Y5) uses the same
settings, so it may stall the same way.

## Grid results (2026-11-01 17:43; deviation 08:58: lowest grid χ² is the fit; resolution 0.2 dex)

**Status:** the Pantheon+ grid (24/24) and the DES Y5 official fit (24 grid + 8 locked edge points) are complete. Still
pending: the Pantheon+ edge points (post-hoc), LD (DES-Dovekie check) and HC (high-mass corner).

**Non-viable points (10 of 24 in both SN sets; penalty or no finite point, possibly code-limited):**
(log10 F, log10 m) = (−0.4, −0.3), (−0.4, 0), (−0.4, 0.2), (−0.4, 0.4), (−0.2, −0.3), (−0.2, 0), (−0.2, 0.2), (0, −0.3),
(0, 0), (0.2, −0.3). This is consistent with viability needing m²F² ≳ 1.2.

| | Pantheon+ (official: grid only) | DES Y5 (official: grid + edge) |
|---|---|---|
| Best point | F 3.16 M_Pl, m 0.50 H₀ (gF0.5m-0.3) | F 3.16 M_Pl, m 1.00 H₀ (gF0.5m0) |
| Δχ² vs ΛCDM (halofit), as written | **+0.96** | **−5.32** |
| Offset-corrected (−1.35, post-hoc; B0) | about −0.4 (tie) | about −6.7 |
| ΔAIC (2 extra parameters) | +4.96 | −1.32 |
| L1 (vs ΛCDM) | **FAIL** | **PASS** (R2) |
| L2: D vs w0–wa | +10.92, **WORSE** (w0–wa itself −9.96) | +14.44, **WORSE** (w0–wa itself −19.76) |
| L3: natural range | **INCONSISTENT**: F at the prior's upper edge | **INCONSISTENT**: F at the prior's upper edge |
| CPL mapping of the best point | w0 = −0.980, wa = −0.030 (barely thawing) | w0 = −0.879, wa = −0.178 (clear thaw) |
| LEE-G (Šidák over distinct F) | Δχ² > 0 → **NOT SIGNIFICANT** | Z_loc 1.81σ → **Z_glob 1.03σ (N_eff = 5), WEAK HINT** |
| Next best | F 1.58 m 1 (+1.15); F 2.51 m 0.5 (+1.16) | F 2.51 m 1 (−4.28); F 1.58 m 1 (−4.14); edge F 1 m 1.26 (−5.05) |

**DES Y5 edge points (locked blind, 12:34:01):** −0.41, −5.05, +0.14, −2.68, +1.33, +0.23, +1.85, +0.58. None beats the
grid best, so the official DES Y5 best stays −5.32.

**Reading (as pre-registered, stated together as the rules require):**
- With Pantheon+, the natural n = 1 Twist ties ΛCDM at best and is clearly worse than w0–wa.
- With DES Y5, it improves on ΛCDM by 5.3, which is only **1.0σ** after counting the search.
- **The DES Y5 gain must be read together with LD** (the corrected DES-Dovekie sample), which is pending. The
  expectation recorded beforehand (DEEP_DIVE_HINTS H3) is WEAKENED or NOT CONFIRMED.
- Both best points sit at the top of the F range (super-Planckian F), which is why L3 fails. HC tests the opposite
  corner.
- The field never reaches w0–wa's fit: thawing cannot produce DESI's phantom-like wa.
