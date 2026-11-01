# Pre-registration: the torus number sets the field width (N = 7) on SPT-3G

**Written:** 31 October 2026, before either target result below existed:
- the N = 7 SPT-3G fit (`spt_edelock_F7`) had not been run or queued;
- the free-width SPT-3G fit (`spt_edelock`) was still running, and its result file did not exist.

**Authors:** Danny Lee Eldridge, with Claude. Danny asked for the torus to be pre-registered; Claude chose the mapping
and the rule.

**Locking:** this file is SHA-256 hashed and git-committed when written, and must not be edited afterwards. Any
deviation goes in PREREGISTRATION_SPT3G_DEVIATIONS.md with a date.

**Companion records:**
- `TORUS_TAURUS_NOTES.md` and `torus_taurus.py`: the torus facts.
- `PREREGISTRATION_SPT3G_N9.md`: the same model and data with N = 9 (it failed).

## Where the number comes from (exact facts)

- **The Tree fits a torus.** The Tree of Life with 22 paths is planar. With Da'at (linked to Keter, Chokhmah, Binah
  and Tiferet) it is not planar, and it has genus exactly 1. A torus map with 15 faces is checked in
  `torus_taurus.py`.
- **The torus's own number is 7.**
  - Every map on a torus can be coloured with 7 colours, and some need all 7 (Heawood number; Ringel–Youngs 1968).
  - K7 is the largest complete graph that fits on a torus.
  - The 7 double letters fill it exactly.

**The mapping (a choice, not a derivation):** the width divisor N in F = √(3/2) M_Pl / N is the torus number. So
**N = 7** and **F = 1.2247 / 7 = 0.17496 M_Pl**.

Nothing in the physics derives this link. It is written down so that it can fail.

## The model

| Setting | Value | Fixed by |
|---|---|---|
| Potential | V = Λ⁴ [1 − cos(φ/F)]³ | as in all earlier fits |
| Switch-on | matter–radiation equality (the lock) | PREREGISTRATION_ZEQ.md |
| Width | **N = 7**: F = √1.5 / 7, with a 1% constraint (`fwidth.FWidth7`) | this file |
| Starting angle θ_i, f_EDE | free, as in `spt_edelock_F9` | PREREGISTRATION_SPT3G_N9.md |

**Data and fitter:** the same as the N = 9 test, with its logged deviations (PREREGISTRATION_SPT3G_DEVIATIONS.md):
- SPT-3G D1 TT/TE/EE lite;
- τ ~ N(0.051, 0.006);
- DESI DR2 + Pantheon+;
- no SH0ES;
- bobyqa, the same starting point.

Run name: `spt_edelock_F7`.

## Pass / fail

### Test A (primary): the N = 7 fit

- Δχ² = χ²(`spt_edelock_F7`) − χ²__fwidth_7 − χ²(`spt_lcdm`).
- ΔAIC = Δχ² + 2, as for N = 9.

| Outcome | Rule |
|---|---|
| **PASS** | Δχ² < −2 and ΔAIC < 0 |
| **FAIL** | Δχ² ≥ 0 |
| **INCONCLUSIVE** | anything in between |

### Test B (width check): the free-width fit

Read the implied N = √1.5 / F from the `spt_edelock` minimum with `width_readback.py spt_edelock`.

| Outcome | Rule |
|---|---|
| **Consistent** | implied N in 6–8 |
| **Inconsistent** | implied N outside 5–9 |
| **Not decisive** | anything in between |

These bands are the N = 9 bands (8–10 and 7–11) moved to 7.

## Disclosed in advance (what was already known)

- **On P-ACT** (PHASE1_RESULTS.md, step 1.2), the N profile has its minimum at N = 8. N = 7 sits 0.77 above it.
- **On Planck,** the minimum is at N = 9.
- **Best-fit N values already read back:**
  - P-ACT free fit: 8.29.
  - Planck free fit: 8.81.
  - These lie between 7 and 9, and closer to 9. So Test B is expected to be "not decisive" or "inconsistent" unless
    SPT-3G prefers a wider field.
- **On SPT-3G,** the N = 9 fit (Δχ² +0.52) and the zero-setting silver fit (+0.43) both FAILED. The N = 7 Twist also
  contains ΛCDM as a limit, so a PASS needs SPT-3G to show a real early-energy minimum, which neither earlier fit
  showed.
- **Expected outcome:** FAIL is the expected result of Test A. It is registered anyway, so the torus mapping is tested
  in public rather than kept as a story.
- **Look-elsewhere:** the torus offers other numbers (15 faces, 26 links, 11 points, 16 independent loops). 7 was
  chosen because it is the torus's own invariant (Heawood), not a property of this particular map. It is stated here
  so that no second number is tried afterwards.
- **The letters prediction is unaffected.** PREREGISTRATION_SPT3G_LETTERS.md uses the same `spt_edelock` result for
  f_EDE.

## What each result would mean

- **A PASS** (with Test B consistent): a width set by the torus number fits independent CMB data better than ΛCDM. That
  would be surprising and worth checking independently. It still would not explain *why*.
- **A FAIL:** the torus → width mapping is dropped publicly. The torus facts stay true as mathematics.
