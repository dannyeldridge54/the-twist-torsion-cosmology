# B4: cosmic birefringence. Results under the locked rule

**Rule:** PREREGISTRATION_B4_BIREFRINGENCE.md, locked 2026-11-02 10:20:30, sha256 4a38898d…490e (commit b24499c). The verdicts below apply it mechanically. Nothing was tuned.

**Target:** |β| = 0.24° ± 0.06°. The score is z = (0.24 − |β|)/0.06:
- **CONSISTENT** if |z| ≤ 2;
- **DISFAVOURED** if 2 < |z| ≤ 3;
- **EXCLUDED** if |z| > 3.

## Headline (primary branch E at the DES Y5 official best fit): **EXCLUDED** (z = 4.0)

Under the standard low-energy reading, the Twist's coupling to light switches off for CMB photons, so it predicts almost no rotation.

## All branches

| Fit | Branch | Predicted abs(β) | z | Verdict |
|---|---|---|---|---|
| DES Y5 best (gF0m0.102) | **E (primary)** | ≈ 0° | 4.0 | **EXCLUDED** |
| DES Y5 best | Nieh–Yan, S=8 | 0.132° | 1.8 | CONSISTENT |
| DES Y5 best | Holst, S=8 | 0.053° | 3.1 | EXCLUDED |
| Pantheon+ best (gF0.4m-0.3) | E (primary) | ≈ 0° | 4.0 | EXCLUDED |
| Pantheon+ best | Nieh–Yan, S=8 | 0.054° | 3.1 | EXCLUDED |
| Pantheon+ best | Holst, S=8 | 0.002° | 4.0 | EXCLUDED |

The predicted sign is negative under our unverified conventions; the rule tests magnitude only.

## What this means (tier: EVIDENCE for the verdicts, HYPOTHESIS for the reading)

- **No explanation without a new parameter.** The Twist with minimally coupled fermions does not explain the measured birefringence. To do so it needs an explicit φ F F̃ term with a free coefficient, and that would be a fit, not a prediction.
- **The one survivor is not the Twist's own field.** One secondary reading survives: the Nieh–Yan coupling, counting all charged fermions, at the DES Y5 fit. That reading uses the Nieh–Yan field, not the Twist's own Holst (arsinh) field, and it ignores the standard decoupling argument.
- **The coupling strength was not the problem.** Under the generous reading, c_γ ≈ 10 F, as guessed. The field moves too little since recombination: 0.08–0.20 M_Pl against the 0.37 M_Pl needed.
- **The verdict depends on the measurement.** If the measured angle falls with better calibration (it is degenerate with instrument polarisation angles), the "≈ 0" prediction becomes the favoured one. The test rule above stays as locked.

## Open caveats (pre-listed in the lock)

1. **Units:** AxiCLASS φ and f_axion are taken as reduced Planck units. This is not yet confirmed. If they are not reduced Planck units, only the secondary-branch numbers scale; branch E is unaffected.
2. **Non-minimal coupling (T3)** is still open.
3. **The Jackiw–Kostelecký Chern–Simons ambiguity** is not resolved.

## Post-lock review (2026-11-02 10:24:15): logged deviations, the rule is unchanged

1. **Citation correction (branch E).**
   - The locked text cites Quevillon & Smith (arXiv:1903.12559) for decoupling. Their abstract does not state it.
   - The correct source is Bauer, Neubert & Thamm, arXiv:1708.00443 (JHEP 12 (2017) 044), eq. 13 and the text after it: B1(τ) ≈ −m_a²/(12 m_f²) for heavy fermions, so "fermions heavier than the ALP decouple".
   - Branch E's physics and verdict are unchanged.
2. **Target value.**
   - On 1 Nov the dive note said to "use the joint value when locking B4". The lock used 0.24° ± 0.06° instead.
   - The joint ACT + Planck value is 0.277° ± 0.057° at 4.8σ (Eskilt, arXiv:2608.06480, checked on the primary page).
   - The locked verdicts stand. This is a sensitivity check only:

   | Fit | Branch | z (0.277 ± 0.057) | Would be |
   |---|---|---|---|
   | DES Y5 | E (primary) | 4.9 | EXCLUDED (same) |
   | DES Y5 | Nieh–Yan, S=8 | 2.5 | DISFAVOURED (was CONSISTENT) |
   | DES Y5 | Holst, S=8 | 3.9 | EXCLUDED (same) |
   | Pantheon+ | E / Nieh–Yan S=8 / Holst S=8 | 4.9 / 3.9 / 4.8 | EXCLUDED (same) |

   The headline does not move. The one consistent secondary reading is target-sensitive, and that is stated wherever it is quoted.
3. **Caveat 1 closed.** AxiCLASS background.c:3540 gives φ in units of the reduced Planck mass, and f_axion is f/M_Pl. The numbers stand.
