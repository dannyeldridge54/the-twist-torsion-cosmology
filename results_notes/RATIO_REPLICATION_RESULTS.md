# Ratio replication: results under the locked rule

**Rule:** PREREGISTRATION_RATIO_REPLICATION.md, locked 2026-11-02 12:01:34, sha256 4e1caef4…bf04 (commit 10855fb). Scored mechanically right after.

**Code:**
- ratio_replication_test.py (ratio_replication_test.json);
- AEGIS nlfix/b4x_switch_defs.py (results/ratio_s3_switch_defs.json).

## Verdicts

| Test | Data (never used before) | Result | Verdict |
|---|---|---|---|
| **G2** golden ratio, atomic | 40 ionisation energies, Z = 21–60 (NIST) | D 0.256, p 0.56 | **NOT REPLICATED** |
| **S2** silver ratio, quantum | 17 successive ratios of 18 hadron masses (PDG) | D 0.182, p 0.73 | **NOT SUPPORTED** |
| **S3** silver switch | H(z_on)/H₀ for f = 5 / 10 / 20 / 50% | 3.31 / 2.39 / 1.75 / 1.23 (Pantheon+); 3.33 / 2.40 / 1.77 / 1.24 (DES Y5) | **DEFINITION-DEPENDENT** |

All three match the expectations logged before computing.

## Descriptive (no verdicts)

| Set | Silver p | Golden p | π p |
|---|---|---|---|
| Z = 21–40 | 0.52 | 0.71 | 0.89 |
| Z = 41–60 | 0.38 | 0.08 | 0.88 |
| Z = 2–60 pooled | 0.48 | 0.49 | 0.89 |
| Hadrons | 0.73 | 0.68 | 0.24 |

## Reading

- **The golden-ratio hint was chance.**
  - On the 19 atoms it came from, it reached p = 0.044.
  - On 40 new atoms, p = 0.56. Pooled over all 59, p = 0.49.
  - That is the usual fate of a p ≈ 0.04 found among six tries.
- **No silver pattern** shows up in either quantum set: fermions (B4-X) or hadrons (here).
- **The 2.4 ≈ silver match came from our definition.** Moving the "switched on" line from 10% to 5% or 20% moves the number from 2.39 to 3.31 or 1.75.
- **What is robust:**
  - The two fits, built on different supernova data, agree on the switch timing at every definition, to within about 1%.
  - Most of the field's move happens between z ≈ 2.2 and today: 5% done at z ≈ 2.2, half done at z ≈ 0.38.
  - That shape, and R ≈ 0.997, are the Twist's real birefringence predictions (B4-X X3), which stay OPEN for future low-ℓ data.

**Ratio line status: closed as NOT SUPPORTED.** Reopening it needs a physical mechanism that predicts a specific ratio *before* the data is looked at (TODO, not scheduled).
