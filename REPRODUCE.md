# Reproducing the work

There are three levels. Each needs more setup than the one before. Most reviewers only need level 1.

| Level | What you get | Needs | Time |
|---|---|---|---|
| **1. Check** | Rules came first; every headline number recomputed; every verdict re-applied | Python 3 only | 10 min |
| **2. Bug** | The AxiCLASS bug reproduced and the fix confirmed | AxiCLASS built (step 2 of level 3) | 10 min more |
| **3. Refit** | Any fit rerun from scratch, on the same code and data | Linux/WSL, conda or micromamba, about 20 GB, hours per fit | half a day to set up |

## Level 1: check (no physics code needed)

```
python verify.py                                        # every rule vs its .sha256; every file vs MANIFEST.txt
python code/analysis/nr_verdicts.py                     # every late-field verdict, as written and on corrected code
python code/analysis/paper_numbers_check.py             # 26 key numbers in the paper recomputed from fit_results/
```

- `LOCK_TIMES.md` shows that each rule entered version control before its result.
- `REVIEWER_QUICK_CHECK.md` has a one-line recomputation of any Δχ² from the files in `fit_results/`.

## Level 3: refit (includes level 2)

**One script rebuilds everything:**

```
bash environment/setup_twist_env.sh
```

It does five things:
1. Creates the conda/micromamba environment `twist` from `environment/environment.yml`: Python 3.11.18, Cobaya 3.6.2
   and the exact versions in `pip_freeze.txt`.
2. Clones **AxiCLASS at commit `ae9609e1f96ddebbb6cc8a46de94512514c68781`** (github.com/PoulinV/AxiCLASS), builds it
   and installs it. This is the "installed" build every original fit used.
3. Makes the three variant builds, which are copies loaded by path and never installed:
   - `AxiCLASS_nlfix`: the two bug fixes (`code/axiclass/nlfix/patch_nlfix.py`);
   - `AxiCLASS_coupled`: the dark-matter coupling β (`code/axiclass/coupled/patch_coupling.py`, 12 exact-anchor edits;
     validate with `coupled/gates.py`, gates V1–V4);
   - `AxiCLASS_coupled_nlfix`: both.
4. Downloads the public likelihood data with `cobaya-install`:
   - Planck 2018 low-ℓ TT/EE;
   - ACT DR6 CMB-only and lensing;
   - DESI DR2 BAO;
   - Pantheon+, DES Y5 and DES-Dovekie;
   - SPT-3G D1 (spt_candl_data at commit `f22611a9`).
5. Checks:
   - the bug reproducer (installed build: MISMATCH; fixed build: MATCH);
   - one likelihood evaluation.

**Settings (all optional):**

| Variable | Meaning | Default |
|---|---|---|
| `TWIST_PY` | Python with Cobaya and classy | set by the setup script |
| `TWIST_BUILDS` | Folder holding the four AxiCLASS builds | `$HOME` |
| `COBAYA_PACKAGES_PATH` | Likelihood data | `packages/` next to the code |
| `TWIST_RESULTS` | Where fits read and write `cmp_<name>.json` | `results/` next to the code |

To reuse our fit outputs (warm starts, or evaluating our best points), set `TWIST_RESULTS=<this repository>/fit_results`.

**Run any fit:**

```
$TWIST_PY code/axiclass/early_late_spa.py <run name>         # writes cmp_<run name>.json (best-fit point and χ²)
```

**The run name encodes the model and the data:**
- **Models:** `ax_spa_lcdm`, `ax_spa_w0wa`, `ax_spa_edelock` (early field), `ax_spa_edelock_w0wa`, `ax_spa_latetwist`
  (late field), `ax_spa_coupledtwist` (late field plus coupling).
- `_gF<log10 F>m<log10 m>` fixes the late field's (F, m) grid point; `_beta<x>` fixes the coupling.
- **Supernovae:** default Pantheon+; `_desy5` uses DES Y5, `_dovekie` uses DES-Dovekie.
- **Non-linear model and code:**
  - `_halofit`: the halofit non-linear model (the reference runs for late fields);
  - `_nlfix`: the corrected-code build.
- **Robustness:** `_nobao` drops DESI; `_b4` or `_r4` use 4 restarts (`_r4` is a cold start).

**Example (the DES Y5 headline):**

```
$TWIST_PY code/axiclass/early_late_spa.py ax_spa_latetwist_gF0m0.102_desy5_nlfix
$TWIST_PY code/axiclass/early_late_spa.py ax_spa_lcdm_halofit_desy5
```

The χ² difference should come out at −6.2. The minimiser (BOBYQA, best of 2 or 4) has no fixed seed, so repeated runs
agree within its tolerance (≲ 1 in χ²), not bit for bit.

**Turn results into verdicts:** `code/analysis/rank_models.py` and `nr_verdicts.py` apply every pre-registered rule
exactly as written.

## Known limits of reproduction

- Fits take 1–4 hours each on 2 cores.
- The grids took days on one 16-core PC.
- Lite ACT/SPT likelihoods are used (as named above), not the full multi-frequency ones.
- Exact χ² values can differ by up to about 1 between runs (no minimiser seed). Every verdict threshold is far larger
  than that, except where the write-ups say otherwise.
