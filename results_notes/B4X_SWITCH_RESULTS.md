# B4-X: the switched Twist. Results under the locked rules

**Rule:** PREREGISTRATION_B4X_PHOTON_COUPLING.md, locked 2026-11-02 11:54:34, sha256 9e714bad…c06c (commit 05f4545). Computed after the lock and scored 2026-11-02 11:58:47, mechanically, with nothing tuned.

**Code:**
- R, z_on, b₀: AEGIS nlfix/b4x_switch.py (results/b4x_switch.json).
- X9: b4x_ratio_test.py (b4x_ratio_test.json).

## The numbers

| Rule | DES Y5 best | Pantheon+ best | Verdict |
|---|---|---|---|
| X1 C_γ needed (0.24°) | 14.6 | 35.4 | fit, not evidence |
| X2 cost | +1 parameter | | no win (fits by construction) |
| **X3 R = β_reion / β_rec** | **0.9975** | **0.9974** | predicted band 0.9974–0.9975; **OPEN** until low-ℓ EB is measured |
| **X4 switch-on z_on** (10% of the move) | **1.52** | **1.54** | logged: the switch flipped about 9.4 billion years ago, when H was 2.4 H₀ |
| X5 anisotropy A_CB | ≈ 0 | ≈ 0 | consistent with ACT DR6 / SPT-3G today |
| X6 achromatic | yes | yes | consistent (no ν⁻² rotation reported) |
| **X7 atomic echo b₀** | **3.5 × 10⁻⁴³ GeV** | **1.4 × 10⁻⁴³ GeV** | **PASS (prediction holds)**: about 10¹⁰ below the neutron limit, so labs see nothing |
| **X9 quantum set, silver** | D 0.230 | p 0.32 | **NOT SUPPORTED** |
| **X9 atomic set, golden** | D 0.221 | p 0.044 | **SUGGESTIVE** (it misses SUPPORTED, p < 0.017) |

## Reading (tiers)

- **X3 and X4 (EVIDENCE for the numbers, HYPOTHESIS for the model).**
  - The switch is real and sharp. Both fits, built on different supernova sets, flip at the same moment (z ≈ 1.5).
  - Over 99.7% of the field's move, and so of the rotation, happens after reionisation. R ≈ 1 is the signature of a late-switching, dark-energy-like field.
  - **Limit:** a dark-matter-like axion predicts R ≈ 0, so R separates the Twist from DM-like fields, but not from other late-rolling dark-energy fields.
- **X7.** The same field touches every electron and neutron spin. Today that effect is about 10⁻⁴³ GeV.
  - Best lab limits: neutron |b̃| ≈ 10⁻³³ GeV (Brown, Smullin, Kornack & Romalis, PRL 105, 151604 (2010), abstract checked); electron about 10⁻³¹ GeV (Heckel et al., PRD 78, 092006 (2008); the number comes from a secondary source).
  - The cosmic field's spin effect points along time. Only Earth's 0.1% speed relative to the CMB turns it into the sideways components labs measure, so the real margin is even larger.
  - The Twist survives the atomic scale, but invisibly.
- **X9.**
  - Fermion mass ratios show no silver-ratio pattern: they behave like random numbers.
  - Atomic ionisation energies sit somewhat closer to powers of the golden ratio than 95.6% of random constants do. That is SUGGESTIVE, not SUPPORTED: across all six (set, constant) pairs checked, a p of 0.044 is expected by chance (6 × 0.044 ≈ 0.26).
  - It is worth an independent re-test on a set fixed in advance (for example Z = 21–40), never on the same data.
- **Coincidence flag (MEANING only, found after the fact and not tested).** The switch flips when H = 2.39–2.40 H₀, close to the silver ratio 2.414. But z_on depends on the 10% definition chosen in the lock (5% or 20% would move it). Treat it as a curiosity, not a result.

## The octave ladder (X8, MEANING: arithmetic on known numbers)

n = log₂(Planck energy / rung energy):

| Rung | Energy | Octaves below Planck |
|---|---|---|
| Planck | 1.22 × 10¹⁹ GeV | 0 |
| top quark | 173 GeV | 56.0 |
| bottom / tau / charm | 4.18 / 1.78 / 1.27 GeV | 61.3 / 62.6 / 63.1 |
| muon / strange | 0.106 / 0.093 GeV | 66.6 / 66.8 |
| down / up | 4.7 / 2.2 MeV | 71.1 / 72.3 |
| electron | 0.511 MeV | 74.3 |
| hydrogen binding | 13.6 eV | 89.5 |
| recombination (photons released) | 0.26 eV | 95.2 |
| CMB today | 2.725 K | 105.4 |
| **Twist switch-on** | H = 2.4 H₀ | **201.1** |
| Twist's note (DES Y5 / Pantheon+) | m = 1.26 / 0.50 H₀ | 202.1 / 203.4 |

The bottom of the ladder, about 202 octaves down, is the universe's age in Planck times (10⁶¹). Any field that switches on "now" sits there by construction.
