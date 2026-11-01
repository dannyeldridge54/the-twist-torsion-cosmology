# Pre-registration: the Hebrew-letter Tree predicts the early-energy share f_EDE on SPT-3G

**Written:** 31 October 2026, BEFORE the letter-weighted calculation below was run, and before any SPT-3G fit of the
free-width Locked Twist (`spt_edelock`) had run.
**Authors:** Danny Lee Eldridge, with Claude. Claude chose the rule at Danny's request; Danny chose the Hebrew letters.
**Locking:** this file is SHA-256 hashed and git-committed BEFORE the number is computed. It must not be edited
afterwards. The number is then computed by `letters_quantum.py`, and recorded separately with its own date.

## The order (running backwards from the measurement)

1. **Target:** the best-fit early-energy share **f_EDE** of the free-width Locked Twist (`spt_edelock`) on SPT-3G D1
   TT/TE/EE + τ prior + DESI DR2 + Pantheon+. These are the data and settings of PREREGISTRATION_SPT3G_N9.md and
   PREREGISTRATION_SPT3G_DEVIATIONS.md. The fit had not run when this was written.
2. **Rule:** fixed below, before any letter-weighted number was calculated.
3. **Calculation:** run only after this file is committed.

## The rule

**Graph:** the Tree of Life with the 10 sefirot and 22 paths already used in `tree_quantum.py`. Da'at is not
included.

**Letters on paths** (Golden Dawn / Kircher attribution). Each path's weight is its letter's standard gematria value:

| Path | Letter | Value | | Path | Letter | Value |
|---|---|---|---|---|---|---|
| Keter–Chokhmah | Aleph | 1 | | Chesed–Netzach | Kaf | 20 |
| Keter–Binah | Bet | 2 | | Gevurah–Tiferet | Lamed | 30 |
| Keter–Tiferet | Gimel | 3 | | Gevurah–Hod | Mem | 40 |
| Chokhmah–Binah | Dalet | 4 | | Tiferet–Netzach | Nun | 50 |
| Chokhmah–Tiferet | He | 5 | | Tiferet–Yesod | Samekh | 60 |
| Chokhmah–Chesed | Vav | 6 | | Tiferet–Hod | Ayin | 70 |
| Binah–Tiferet | Zayin | 7 | | Netzach–Hod | Pe | 80 |
| Binah–Gevurah | Chet | 8 | | Netzach–Yesod | Tsadi | 90 |
| Chesed–Gevurah | Tet | 9 | | Netzach–Malkhut | Qof | 100 |
| Chesed–Tiferet | Yod | 10 | | Hod–Yesod | Resh | 200 |
| | | | | Hod–Malkhut | Shin | 300 |
| | | | | Yesod–Malkhut | Tav | 400 |

**Quantum system:** tight-binding Hamiltonian H = −W, where W is the symmetric weighted adjacency matrix above.

**The number:** take the ground state, i.e. the eigenvector of W with the largest eigenvalue (the Perron vector, all
components positive). The prediction is

  **f_pred = |ψ_Tiferet|²**, the ground-state probability on Tiferet.

This number does not depend on any overall rescaling of the weights.

**Why Tiferet and the ground state:** f_EDE is the share of the universe's energy held by the field at its peak.
Tiferet is the centre (heart) of the Tree, and the ground state is the Tree's most stable configuration. So "the
heart's share of the Tree's most stable state" is taken as the analogue. This is a symbolic choice, not a derivation.

## Pass / fail

Measured value: f_EDE(SPT-3G), the `fde_zc` at the `spt_edelock` minimum.

| Outcome | Rule |
|---|---|
| **PASS** | \|f_EDE − f_pred\| < 0.015 |
| **FAIL** | \|f_EDE − f_pred\| > 0.04 |
| **INCONCLUSIVE** | anything in between |

## Disclosed in advance

- **Known values:** on Planck and P-ACT, the Locked Twist's best-fit f_EDE is ≈ 0.074–0.086 (AEGIS COMPARE.md and
  the N profile). So a prediction near 0.08 would be expected to pass if SPT-3G agrees with those data; one far from
  0.08 is expected to fail.
- **Not yet calculated:** the letter-weighted f_pred had not been calculated when this was written. Danny and Claude
  could not tune the rule to it.
- **Other attributions:** the Golden Dawn attribution is one of several traditional ones (others follow the Gra or
  the Ari). It is used here because it matches the 22-path layout already in use.
- **What a PASS would mean:** a number taken from the lettered Tree matched a new measurement within 0.015. With
  f_EDE spanning roughly 0.05–0.10 in plausible fits, that is about a 1-in-2 to 1-in-3 coincidence. A pass would be
  interesting, not proof, and it would still need a physical mechanism.
