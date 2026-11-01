# Claims index: every claim, its rule, its evidence, its verdict

**Status:** working copy, 1 November 2026. *Pending* rows are filled in when tonight's fits finish.

**Paths:**
- `P/` = `preregistrations/`
- `N/` = `results_notes/`
- `F/` = `fit_results/`
- `C/` = `code/`

Each rule's hash is in `P/<rule>.sha256`. When it was committed is in `LOCK_TIMES.md`. Verdicts are applied by
`C/analysis/rank_models.py` exactly as written.

## Early Twist (Locked Twist)

| # | Claim / test | Verdict | Rule | Write-up | Key files |
|---|---|---|---|---|---|
| E1 | Planck + DESI + Pantheon+ prefer early energy | PASS (Δχ² −4.70) | AEGIS lock files (`F/VERDICT_LOCK.json`) | `N/THESIS.md` §3 | `F/cmp_*` |
| E2 | Planck + ACT DR6 (blind) | PASS (Δχ² −7.23) | `F/N_PACT_LOCK.json` | `N/THESIS.md` §3 | `F/cross_engine_pact.json` |
| E3 | SPT-3G D1 alone | FAIL (best −1.27) | `P/PREREGISTRATION_SPT3G_N9.md`, `_SILVER`, `_TORUS`, `_LETTERS` | `N/SPT3G_RESULTS.md` | `F/width_spt_edelock.json` |
| E4 | All three CMB + DESI + Pantheon+ | PASS (Δχ² −5.63) | `P/PREREGISTRATION_COMBINED_CMB.md` | `N/COMBINED_CMB_RESULTS.md` | `F/cmp_*` |
| E5 | A1: profile in f | PREFERRED (f = 0 costs 5.98) | `P/PREREGISTRATION_PROFILE_F.md` | `N/PROFILE_F_RESULTS.md` | `F/cmp_*` |
| E6 | A2: look-elsewhere | WEAK HINT (1.2–1.4σ global) | `P/PREREGISTRATION_LOOK_ELSEWHERE.md` | `N/LOOK_ELSEWHERE_RESULTS.md` | `N/LOOK_ELSEWHERE_RESULTS.json` |
| E7 | A3: early on top of late | MILD (D −3.65) | `P/PREREGISTRATION_EARLY_LATE.md` | `N/EARLY_LATE_RESULTS.md` | `F/cmp_ax_spa_*` |
| E8 | R1: A3 minimiser stability | STABLE (MILD, −3.96) | `P/PREREGISTRATION_ROBUSTNESS.md` | `N/ROBUSTNESS_RESULTS.md` | `F/cmp_*_b4.json` |
| E9 | A3 with DES-Dovekie | MILD (−2.70) | `P/PREREGISTRATION_DOVEKIE.md` | `N/ROBUSTNESS_RESULTS.md` | `F/cmp_*_dovekie.json` |
| E10 | Potential power n = 3 vs 2 | n = 3 favoured | `P/PREREGISTRATION_POWER_N.md` | `N/THESIS.md` §3 | `F/cmp_*` |
| E11 | Zero predictions (no birefringence, no GW friction) | open / consistent | `P/PREREGISTRATION_NULL_PREDICTIONS.md` | `N/THESIS.md` §5 | — |
| E12 | Lock from the dynamics | NO LOCK | `P/PREREGISTRATION_LOCK_ATTRACTOR.md` | `N/LOCK_ATTRACTOR_RESULTS.md` | `N/LOCK_ATTRACTOR_*.json` |
| E13 | Symbol-derived predictions (P1–P4) | FAIL / INCONCLUSIVE | `P/PREREGISTRATION_SPT3G_*` | `N/SPT3G_RESULTS.md` | `F/width_*.json` |

## Late Twist

| # | Claim / test | Verdict | Rule | Write-up | Key files |
|---|---|---|---|---|---|
| L1 | Late Twist vs ΛCDM (Pantheon+) | FAIL as written (+0.96); ≈ −0.4 offset-corrected; *grid pending* | `P/PREREGISTRATION_LATE_TWIST.md` + deviation 08:58 | `N/LATE_TWIST_RESULTS.md` | `F/cmp_ax_spa_latetwist_gF*.json` |
| L2 | Late Twist vs w0–wa | WORSE; *grid pending* | same | same | same |
| L3 | F, m in natural range | INCONSISTENT (F at prior edge); *pending* | same | same | same |
| L4 | Shared F (one decay constant) | DIFFERENT so far; *pending* | `P/PREREGISTRATION_SHARED_F.md` | same | `F/earlyF_*.json` |
| R2 | L1 with DES Y5 | PASS so far (−5.32, preliminary) | `P/PREREGISTRATION_ROBUSTNESS.md` | `N/ROBUSTNESS_RESULTS.md` | `F/*_desy5.json` |
| ES | Edge scan | *pending* | `P/PREREGISTRATION_EDGE_SCAN.md` | — | `C/axiclass/run_edge.sh` |
| LD | Late Twist on DES-Dovekie | *pending* (expected WEAKENED / NOT CONFIRMED) | `P/PREREGISTRATION_LATE_DOVEKIE_LEE.md` | — | `C/axiclass/pick_late_dovekie.py` |
| LEE-G | Grid look-elsewhere | DES Y5 WEAK HINT so far; Pantheon+ NOT SIGNIFICANT | same | — | `C/analysis/rank_models.py` |
| HC | High-mass corner | *pending* | `P/PREREGISTRATION_HIGH_MASS_CORNER.md` | — | `C/axiclass/run_hc.sh` |
| NM | Null mirror (code check) | +1.35 halofit artefact; cause confirmed | post-hoc check | `N/LATE_TWIST_NULL_MIRROR.md` | `F/null_mirror_*.json` |

## Coupled Twist

| # | Claim / test | Verdict | Rule | Write-up | Key files |
|---|---|---|---|---|---|
| V1–V4 | Code validation gates | PASS | `P/PREREGISTRATION_COUPLED_TWIST.md` | `N/COUPLED_TWIST_GATES.md` | `C/coupled/gates.py` |
| C1–C4 | Coupling needed? phantom crossing? | *pending* | same | — | `C/coupled/coupled_weff.py` |
| C5 | Torsion-natural β = 0.816 | *pending* (expected EXCLUDED) | same + deviation 08:39 | — | — |

## History and art track (not evidence for the physics)

| # | Study | Result | Rule | Write-up |
|---|---|---|---|---|
| H1 | Stars in 1D–6D (correlation dimension) | homogeneous above 3 pc; fractal-like in phase space | `P/PREREGISTRATION_STAR_FRACTAL.md`, `_ND` | `history_track/STAR_FRACTAL_RESULTS.md` |
| H2 | Old books and sources | logged and checked | — | `history_track/OLD_SOURCES_LOG.md` |
