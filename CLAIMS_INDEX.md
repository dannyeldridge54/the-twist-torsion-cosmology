# Claims index: every claim, its rule, its evidence, its verdict

**Status:** final, 2 November 2026. Every pre-registered test has a verdict. Late-field verdicts are given as written
and on corrected code (NR); the corrected-code verdict is the headline.

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
| L1 | Late Twist vs ΛCDM (Pantheon+) | **NR: FAIL (+0.09, a tie)**; as written FAIL (+0.96) | `P/PREREGISTRATION_LATE_TWIST.md` + deviation 08:58 | `N/LATE_TWIST_RESULTS.md` | `F/cmp_ax_spa_latetwist_gF*.json` |
| L2 | Late Twist vs w0–wa | **NR: WORSE** (D +10.05 / +13.53); as written WORSE | same | same | same |
| L3 | F, m in natural range | **NR: CONSISTENT**; as written INCONSISTENT | same | same | same |
| L4 | Shared F (one decay constant) | DIFFERENT | `P/PREREGISTRATION_SHARED_F.md` | same | `F/earlyF_*.json` |
| R2 | L1 with DES Y5 | **NR: PASS (−6.23)**; as written PASS (−5.32) | `P/PREREGISTRATION_ROBUSTNESS.md` | `N/ROBUSTNESS_RESULTS.md` | `F/*_desy5.json` |
| ES | Edge scan | done (32/32 DES Y5 points accounted) | `P/PREREGISTRATION_EDGE_SCAN.md` | `N/LATE_TWIST_RESULTS.md` | `C/axiclass/run_edge.sh` |
| LD | Late Twist on DES-Dovekie | **NR: WEAKENED (−1.33)**; as written NOT CONFIRMED (+0.18) | `P/PREREGISTRATION_LATE_DOVEKIE_LEE.md` | `N/LATE_TWIST_RESULTS.md` | `C/axiclass/pick_late_dovekie.py` |
| LEE-G | Grid look-elsewhere | **NR: DES Y5 WEAK HINT (1.27σ global)**; Pantheon+ NOT SIGNIFICANT | same | same | `C/analysis/rank_models.py` |
| HC | High-mass corner | **NR: WORSE (+37.0)**; as written WORSE (+38.0) | `P/PREREGISTRATION_HIGH_MASS_CORNER.md` | `N/LATE_TWIST_RESULTS.md` | `C/axiclass/run_hc.sh` |
| NM | Null mirror (code check) | two AxiCLASS bugs found and fixed; fixed build +0.13 PASS | post-hoc check + deviations 14:34:07, 14:41:32 | `N/LATE_TWIST_NULL_MIRROR.md` | `F/null_mirror_*.json` |
| NR | Replication of every n = 1 test on corrected code | done; side-by-side table | `P/PREREGISTRATION_NLFIX_REPLICATION.md` | `N/LATE_TWIST_RESULTS.md` | `F/*_nlfix.json` |
| B2 | Does each gain depend on DESI? | Late Twist DES Y5 **NOT DESI-DRIVEN** (−5.33 without, 86% kept); Coupled **DESI-DRIVEN** (+0.74 without); w0–wa PARTLY | `P/PREREGISTRATION_ROBUSTNESS_II.md` | `N/ROBUSTNESS_II_RESULTS.md` | `F/*_nobao*.json` |
| R3 | Cold restarts of the two best points | Late DES Y5 **STABLE** (+0.13); Coupled **COLD-START WORSE** (+2.37; the warm minimum stands, minimiser-sensitive) | same | same | `F/*_r4.json` |
| LU | Late Twist DES Y5 point on Union3 (independent SNe) | **WEAKENED (−1.82)**; Union3 SNe −4.10; w0–wa −15.00 (context) | `P/PREREGISTRATION_LATE_UNION3.md` | `N/LATE_UNION3_RESULTS.md` | `F/*_union3*.json` |
| TF | F fixed at √(3/2) and √6 M_Pl (m free) | *pending* | `P/PREREGISTRATION_TORSION_F.md` | — | `F/*_fF*.json` |
| TF-P | F fixed at (4/π)√(3/2) M_Pl, derived from the Nieh–Yan period | *pending* | `P/PREREGISTRATION_TORSION_F_PLANCK.md` | `N/NIEH_YAN_PERIOD.md` | `F/*_fF0.1930*.json` |
| LZ | Low-z split of the DES Y5 supernova gain | **CALIBRATION-SENSITIVE** (r = −0.06): neither half alone prefers the Twist; the gain is the low/high-z offset (w0–wa the same, r = −0.17) | `P/PREREGISTRATION_SOLAR_LOWZ.md` | `N/LOWZ_SPLIT_RESULTS.md` | `N/lowz_split.json` |
| SSG | BI dilaton vs Cassini (Spiral Twist gate) | **ATTRACTOR-PROTECTED** (Reading A): GR point at ϕ = −½, band \|Δχ\| < 0.0072; a pinned dilaton gives no phantom illusion today | `P/PREREGISTRATION_SOLAR_LOWZ.md` | `N/SOLAR_GATE_RESULTS.md` | `N/solar_gate.json` |
| S8 | S8 on corrected code | Late Twist NEUTRAL; Coupled Twist WORSENS (+0.84σ vs DES Y6) | `P/PREREGISTRATION_S8_FIXED_CODE.md` | `N/S8_FIXED_CODE_RESULTS.md` | `F/s8_fixed_code.json` |

## Coupled Twist

| # | Claim / test | Verdict | Rule | Write-up | Key files |
|---|---|---|---|---|---|
| V1–V4 | Code validation gates | PASS | `P/PREREGISTRATION_COUPLED_TWIST.md` | `N/COUPLED_TWIST_GATES.md` | `C/coupled/gates.py` |
| C1 | Coupled vs ΛCDM | **NR: PASS (−7.91)**; as written PASS (−6.80) | same | `N/COUPLED_TWIST_RESULTS.md` | `F/cmp_ax_spa_coupledtwist_*.json` |
| C2 | Coupling needed | **NR: NEEDED (−8.00)**; as written NEEDED | same | same | same |
| C3 | Coupled vs w0–wa (ΔAIC) | **NR: WORSE (+4.05)**; as written WORSE (+5.16) | same | same | same |
| C5 | Torsion-natural β = 0.816 | **EXCLUDED** (both codes; NR +71,655 for either sign) | same + deviation 08:39 | same | `F/cmp_*beta*0.816*.json` |
| βP | β profile (NR) | bimodal: ±0.05 → −7.37 / −7.34; 0 → −0.63; −0.1 / +0.1 → +128 / +94 | same | same | `F/cmp_*beta*_nlfix.json` |

## Birefringence and spin (photon and fermion couplings)

| # | Claim / test | Verdict | Rule | Write-up | Key files |
|---|---|---|---|---|---|
| B4 | Minimal field explains the measured CMB rotation | **EXCLUDED** (primary, 4.0σ); the generous S = 8 reading is CONSISTENT only at the DES Y5 fit and target-sensitive | `P/PREREGISTRATION_B4_BIREFRINGENCE.md` | `N/B4_BIREFRINGENCE_RESULTS.md` | `F/b4_delta_theta.json` |
| B4-X | One added photon coupling: switch ratio R | fits by construction; **R = 0.997, OPEN** (LiteBIRD) | `P/PREREGISTRATION_B4X_PHOTON_COUPLING.md` | `N/B4X_SWITCH_RESULTS.md` | `F/b4x_switch.json` |
| X7 | Atomic spin echo below lab limits | **PASS** (b₀ ≈ 10⁻⁴³ GeV, 10¹⁰ below the neutron bound) | same | same | same |
| X9 | Silver (quantum) / golden (atomic) ratio spacings | NOT SUPPORTED / SUGGESTIVE (p 0.044) | same | same | `b4x_ratio_test.json` |
| G2/S2/S3 | Ratio replication on new data | golden NOT REPLICATED (p 0.56); silver NOT SUPPORTED; switch value DEFINITION-DEPENDENT | `P/PREREGISTRATION_RATIO_REPLICATION.md` | `N/RATIO_REPLICATION_RESULTS.md` | `ratio_replication_test.json` |

## Unification (UFE) consistency checks (supergravity embedding of the BI field; HYPOTHESIS tier)

| # | Claim / test | Verdict | Rule | Write-up | Key files |
|---|---|---|---|---|---|
| IN | α = 1 geometry gives acceptable inflation | **TENSION** (n_s 0.9667 at N = 60, 2.4σ low) | `P/PREREGISTRATION_UFE_CHECKS.md` | `N/UFE_CHECKS_RESULTS.md` | `N/ufe_in.json` |
| ER | Dilaton relaxation supplies the early energy | **TOO SMALL** (≤ 2.5%; G ×13 at BBN) | same | same | `N/ufe_er.json` |
| LQ | BI value today matches LQG γ | **NO VERDICT** (mirror 0.087) | same | same | `N/ufe_lq.json` |
| GH | Stored fits vs H(z) chronometers and fσ8 | **NEUTRAL** (all \|Δ\| < 0.5; LT-P NO VERDICT, mirror) | `P/PREREGISTRATION_GROWTH_HZ.md` | `N/GROWTH_HZ_RESULTS.md` | `N/growth_hz.json`, `data/growth_hz_data.json` |

## History and art track (not evidence for the physics)

| # | Study | Result | Rule | Write-up |
|---|---|---|---|---|
| H1 | Stars in 1D–6D (correlation dimension) | homogeneous above 3 pc; fractal-like in phase space | `P/PREREGISTRATION_STAR_FRACTAL.md`, `_ND` | `history_track/STAR_FRACTAL_RESULTS.md` |
| H2 | Old books and sources | logged and checked | — | `history_track/OLD_SOURCES_LOG.md` |
