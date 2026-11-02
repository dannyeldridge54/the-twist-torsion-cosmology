# Pre-registration: replication of every n = 1 test on the corrected code (NR)

**Locked:** 2026-11-01 18:37:37 (time from Get-Date).

**Written and locked before:** any replication run. No `_nlfix` fit has been run. The only `_nlfix` evaluations before
the lock are the build gates (null mirror, below), which use fixed ΛCDM parameters and no fitting.

**Why:**
- The installed AxiCLASS has two bugs for an n = 1 axion used as dark energy (LATE_TWIST_NULL_MIRROR.md, "Fix (B0)"):
  1. a forced `include_scf_in_delta_m`, which dilutes δ_m and makes σ8 about 0.25;
  2. halofit and HMcode reading an Ω_m that includes the field as ρ − 3p.
- Together they put about +1.35 on χ² in the Λ limit and make S8 invalid.
- Danny chose (1 Nov) to rerun everything affected overnight. Only n = 1 runs are affected; the early (n = 3) results
  and the ΛCDM and w0–wa references are unchanged (the ΛCDM χ² is identical on the fixed build: 2402.256).

## Builds (separate, not installed)

- **Late Twist:** /home/syndyr/AxiCLASS_nlfix.
- **Coupled Twist:** /home/syndyr/AxiCLASS_coupled_nlfix (copy of the coupled build plus `nlfix/patch_nlfix.py`).
- `early_late_spa.py` loads them for any run name containing `_nlfix`.

**Gate N0 (run before this lock, as a build check):** frozen field (F 100, m 0.015) at the ΛCDM best fit, halofit on,
via the fitter's own switch. Rule: |Δχ²| < 0.15. Results: Late Twist +0.127 PASS; Coupled Twist at β = 0 +0.127 PASS
(`results/nlfix_gate_N0_*.json`).

## What is rerun (all with suffix `_nlfix`; identical settings otherwise)

| Stage | Runs |
|---|---|
| 1 | Late Twist (F, m) grid, Pantheon+ (24) and DES Y5 (24); the 8 locked edge points on both SN sets (16); the 9 high-mass-corner points (Pantheon+) |
| 2 | **LD:** the points chosen by the LD rule applied to the stage 1 `_nlfix` results (DES Y5 best over grid + edge; Pantheon+ best over grid only), on DES-Dovekie |
| 3 | **Coupled Twist** 3×3 grid (β free in ±0.15), centred on the best stage 1 Pantheon+ **grid** point |
| 4 | **C5** (β = ±0.816) and the 5-point **β profile**, at the best stage 3 point |

**References are not rerun** (they contain no scalar field). The existing ΛCDM and w0–wa halofit references for
Pantheon+, DES Y5 and DES-Dovekie are used.

## Verdict rules

**Identical to the original pre-registrations**, applied to the `_nlfix` results with the same references:

| Test | Rule source |
|---|---|
| L1–L3 | PREREGISTRATION_LATE_TWIST.md + deviation 08:58 |
| R2 | PREREGISTRATION_ROBUSTNESS.md |
| Edge | PREREGISTRATION_EDGE_SCAN.md |
| LD and LEE-G | PREREGISTRATION_LATE_DOVEKIE_LEE.md |
| HC | PREREGISTRATION_HIGH_MASS_CORNER.md |
| C1–C5 | PREREGISTRATION_COUPLED_TWIST.md |
| Shared F | PREREGISTRATION_SHARED_F.md |

The non-viable criterion is also the same: penalty or no finite point.

## How the two sets are reported (decided now, before any result)

1. **The original verdicts stay on record exactly as written** (installed code), labelled "as written (code with the
   B0 bugs)".
2. **The replication verdicts are labelled "corrected code (NR)".** Because the original code is known to be wrong
   for n = 1 dark energy, **the paper's headline for the Late Twist and Coupled Twist uses the NR verdicts**, with the
   as-written verdicts shown beside them in the same table.
3. If a verdict differs between the two, both are stated with the reason (the B0 bugs). Nothing is averaged or chosen
   after the fact.
4. **S8 and σ8 for n = 1 models are quoted only from NR runs.**
5. If an NR stage cannot finish (crashes or no finite points), the affected verdicts are reported as "NR incomplete",
   and the as-written verdicts with the −1.35 offset note remain the only numbers.

## Timing

- `nlfix/run_nlfix.sh` starts only after tonight's queue has finished (grid stage 3, LD, HC).
- At most 8 fits run at once.
- Expected: about 8–10 hours, finishing tomorrow morning.
