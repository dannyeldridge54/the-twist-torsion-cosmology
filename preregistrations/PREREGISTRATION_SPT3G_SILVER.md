# Pre-registration: the zero-setting Locked Twist (starting angle = silver ratio) on SPT-3G

**Written:** 31 October 2026, before any SPT-3G fit of this model was run.
**Authors:** Danny Lee Eldridge, with Claude. Claude chose the mapping below at Danny's request ("do all").
**Locking:** this file is SHA-256 hashed and git-committed when written, and must not be edited afterwards. Any
deviation goes in a separate, dated file.
**Companion records:**
- `PREREGISTRATION_SPT3G_N9.md` (DOI 10.5281/zenodo.23838969), which fixes the width.
- `tree_quantum.py`, which computes the number used here.

## Where the number comes from

Treat the Tree of Life as a quantum graph: 10 sefirot, 22 paths, and a particle hopping along the paths
(tight-binding, H = −A).
- Its ten energy levels include exactly two modes that are antisymmetric between the left and right pillars.
  Their energies are exactly **1 − √2** and **1 + √2**.
- 1 + √2 = 2.41421… is the silver ratio.
- Adding Da'at as an 11th node on the middle pillar leaves both values unchanged, because a middle-pillar node
  cannot couple to pillar-antisymmetric modes.
- All other levels are irregular numbers.

**The mapping (a choice, not a derivation):** the field's starting angle θ_i, a dimensionless number of order 1, is
set to the top balance-mode energy.

  **θ_i = 1 + √2 = 2.41421 rad**

Nothing in the physics derives this link. It is the framework's prediction, written down so that it can fail.

## The model (every setting fixed)

| Setting | Value | Fixed by |
|---|---|---|
| Potential | V = Λ⁴ [1 − cos(d/F)]³ | as in all earlier fits |
| Switch-on | matter–radiation equality, a_c = ω_r / (ω_b + ω_cdm) | PREREGISTRATION_ZEQ.md |
| Width | F = 1.2247 / 9 = 0.13608 M_Pl (1% constraint, as in fwidth.py) | PREREGISTRATION_SPT3G_N9.md |
| Starting angle | **θ_i = 2.41421 rad** | this file |

**Zero extra free settings over ΛCDM.** The energy fraction f_EDE is then set by the width constraint. If the code
cannot fix θ_i and F together while keeping f_EDE determined, the f_EDE value is reported and logged as a deviation
before any result is read.

## What was already known (disclosed)

- **The Planck best-fit start:** Claude had read an AEGIS note (`claims.json`, hold_release) saying the fitted start
  on Planck is ≈ 0.886π ≈ 2.78 rad. This prediction (2.414) therefore lies **below the known Planck best fit** and
  may fail.
- **Fixed-angle runs:** AEGIS also holds fixed-θ_i runs (th2.00 … th3.10) on Planck data. Claude has not opened their
  results.
- **No SPT-3G fit** of any Twist model has been run.

## Data

- **Primary test:** the same as PREREGISTRATION_SPT3G_N9.md. SPT-3G D1 TT/TE/EE, plus:
  - a τ prior from Planck low-ℓ EE;
  - DESI DR2 BAO;
  - Pantheon+.
  
  No SH0ES.
- **Secondary:** P-ACT + DESI DR2 + Pantheon+. Not blind; reported for comparison only.

## Pass / fail (primary test only)

The model has zero extra settings, so ΔAIC = Δχ².

| Outcome | Rule |
|---|---|
| **PASS** | Δχ² < −2 vs ΛCDM |
| **FAIL** | Δχ² ≥ 0 |
| **INCONCLUSIVE** | −2 ≤ Δχ² < 0 |

**Angle check:** a fit on the same primary data with θ_i free (N = 9 and the lock kept).
- **Consistent:** best-fit θ_i within 2.414 ± 0.15 rad.
- **Inconsistent:** further than 0.35 rad away.
- **Not decisive:** anywhere in between.

## Reported beside the verdict

- H₀ and f_EDE for the zero-setting model.
- The S8 penalty against both lensing values (PREREG_S8.md).
- The same zero-setting model at the Planck-preferred angle (≈ 2.78), **labelled as not a prediction**, for contrast.

## What each result would mean

- **PASS:** a parameter-free model, with one number taken from the Tree's quantum pattern, fits independent CMB data
  better than ΛCDM. That would be surprising and worth independent checking. It would still not explain *why* the
  Tree should set the angle.
- **FAIL or angle inconsistent:** the silver-ratio mapping is dropped publicly. The Locked Twist itself is unaffected;
  it never depended on this number.
