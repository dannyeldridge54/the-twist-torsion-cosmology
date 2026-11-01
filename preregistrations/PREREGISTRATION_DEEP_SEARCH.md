# Pre-registration: deeper search (12 restarts) for the key fits, as a robustness check

**Written:** 31 October 2026, about 21:10 CT. Before any of the runs below was written as code or run.
**Why:** DEEP_DIVE_2026-10-31.md (section 5) found that the Twist's restarts scatter by up to 2.6 in χ² while ΛCDM's
scatter by under 1. So some Twist Δχ² values may be slightly pessimistic.
**Locking:** SHA-256 hashed and committed when written; never edited afterwards.

## Runs

The same data, model and settings as the originals, except bobyqa is run with **best of 12** restarts. The same
restart count is used for both models in each pair. Runs carry the suffix `_deep`.

| Pair | Data |
|---|---|
| `spa_lcdm_deep`, `spa_edelock_deep` | Planck + ACT + SPT-3G + DESI DR2 + Pantheon+ |
| `spt_lcdm_deep`, `spt_edelock_F9_deep` | SPT-3G D1 + τ prior + DESI DR2 + Pantheon+ |

## Rules

- **The original verdicts stand.** The pre-registered tests were decided on their original runs and are not rewritten.
- For each pair, report Δχ²_deep = χ²(model_deep) − χ²(ΛCDM_deep). For F9, the width constraint's χ² is removed, as
  before.
- **Robustness note:** if Δχ²_deep falls in a different verdict band than the original (bands as in the original
  pre-registration), report it plainly beside the original verdict as "would have been X with a deeper search". The
  original verdict is still not changed.
- Also report the restart spread of each deep run. If the Twist's spread is still above 1, the surface is too rugged
  for bobyqa, and a better optimiser or a profile is needed. That is said plainly too.
