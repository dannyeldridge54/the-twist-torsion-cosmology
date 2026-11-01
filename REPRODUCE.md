# Reproducing the fits

## Environment

- Linux, or WSL on Windows, with micromamba.
- Python 3.11 with: Cobaya, CAMB, classy (AxiCLASS), numpy, scipy.
- **Likelihoods** (public, installed through Cobaya and candl; not included here), exactly as in
  `code/axiclass/early_late_spa.py`:
  - `planck_2018_lowl.TT`, `planck_2018_lowl.EE`;
  - `act_dr6_cmbonly` (PlanckActCut + ACTDR6CMBonly) and `act_dr6_lenslike` (actplanck_baseline);
  - `spt3g_d1_tne_lite` (candl);
  - `bao.desi_dr2.desi_bao_all`;
  - one of `sn.pantheonplus`, `sn.desy5` or `sn.desdovekie`.
- **AxiCLASS:** the public repository by Poulin, Smith et al.

## Runs

- Each fit is one command: `python code/axiclass/early_late_spa.py <run name>`.
- **The run name encodes the model and data:**
  - `ax_spa_lcdm`, `ax_spa_w0wa`, `ax_spa_edelock`, `ax_spa_edelock_w0wa` and `ax_spa_latetwist`;
  - `_halofit`: the halofit non-linear model;
  - `_desy5` and `_dovekie`: the supernova sample;
  - `_b4`: best of 4 restarts;
  - `_gF<log10 F>m<log10 m>`: a fixed (F, m) grid point;
  - `coupledtwist` with `_beta<x>`: the Coupled Twist.
- Runs write `cmp_<name>.json` with the best-fit point and χ². `code/analysis/rank_models.py` turns them into verdicts.
- Queue scripts: `run_grid.sh`, `run_grid_helper.sh`, `run_edge.sh`, `run_late_dovekie.sh`, `run_hc.sh`.

## The Coupled Twist build

1. Clone AxiCLASS.
2. Run `python code/coupled/patch_coupling.py <path to the AxiCLASS clone>`. It makes 12 exact-anchor edits to `background.h`,
   `input.c`, `background.c` and `perturbations.c` (parameter `scf_coupling_beta`).
3. Build with `code/coupled/build_coupled.sh`.
4. Validate with `code/coupled/gates.py` (gates V1–V4 must pass before any fit).

## Known artefact

- In AxiCLASS, a scalar field enters halofit's Ω_m as ρ − 3p. For a frozen field that is +4 Ω_field.
- It adds about +1.35 to Late Twist χ² against Λ-based references (`results_notes/LATE_TWIST_NULL_MIRROR.md`).
- **Reproduce the diagnosis** with `code/axiclass/null_mirror.py` and `null_mirror_nl.py`.
- A fix is planned as a logged deviation, after the current runs.
