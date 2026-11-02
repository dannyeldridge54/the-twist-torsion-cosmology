# Ratio replication: does the golden/silver pattern hold on data it has never seen? Pre-registration

**Locked:** 2026-11-02 12:01:34 (time from Get-Date). Requested by Danny: "Start the new test with all the new stuff… see about the new equation fitting the silver-golden ratio with everything we found."

**Written after:** B4-X X9 (golden/atomic SUGGESTIVE p = 0.044 on Z = 2–20; silver/quantum NOT SUPPORTED on fermion masses) and the post-hoc note that the switch flips at H ≈ 2.40 H₀. **Written before:** any statistic on the data below.

## Method (identical to B4-X X9)

- **Statistic:** D(c) is the mean, over the set, of the distance from log_c(r) to the nearest integer.
- **Null:** 100,000 constants drawn log-uniform on [1.3, 3.5], with a new seed (20261103). The p-value is the fraction of null constants with D at or below D(candidate).
- **Candidates:** silver 1 + √2, golden (1 + √5)/2, and π. All pairs are reported; only the primaries carry verdicts.

## Tests

**G2. Golden ratio, atomic: the replication (primary).**
- **Set:** the first ionisation energies of Z = 21–60 divided by hydrogen's 13.598 eV, giving 40 values. These atoms were not used before. NIST ASD values in eV, fetched 2 Nov 2026:

  | Z | Elements and energies |
  |---|---|
  | 21–30 | Sc 6.5615, Ti 6.8281, V 6.7462, Cr 6.7665, Mn 7.4340, Fe 7.9025, Co 7.8810, Ni 7.6399, Cu 7.7264, Zn 9.3942 |
  | 31–40 | Ga 5.9993, Ge 7.8994, As 9.7886, Se 9.7524, Br 11.8138, Kr 13.9996, Rb 4.1771, Sr 5.6949, Y 6.2173, Zr 6.6341 |
  | 41–50 | Nb 6.7589, Mo 7.0924, Tc 7.1194, Ru 7.3605, Rh 7.4589, Pd 8.3368, Ag 7.5762, Cd 8.9938, In 5.7864, Sn 7.3439 |
  | 51–60 | Sb 8.6084, Te 9.0098, I 10.4512, Xe 12.1298, Cs 3.8939, Ba 5.2117, La 5.5769, Ce 5.5386, Pr 5.4702, Nd 5.5248 |

- **Verdict:** **REPLICATED** if golden has p < 0.05; **NOT REPLICATED** otherwise.
- **Also reported (descriptive):** the halves Z = 21–40 and 41–60, and Z = 2–60 pooled (the pooled figure reuses old data and carries no verdict).

**S2. Silver ratio, quantum: a new quantum set (primary).**
- **Set:** the successive ratios of 18 well-measured ground-state hadron masses sorted by mass, giving 17 ratios. PDG central values in MeV:

  | Group | Hadrons and masses |
  |---|---|
  | Light mesons | π± 139.57, K± 493.677, η 547.862, ρ 775.26, ω 782.66, K*(892) 891.67, η′ 957.78, φ 1019.461 |
  | Baryons | p 938.272, Λ 1115.683, Σ⁺ 1189.37, Δ 1232, Ξ⁰ 1314.86, Ω⁻ 1672.45 |
  | Heavy mesons | D⁰ 1864.84, J/ψ 3096.90, B⁺ 5279.34, Υ(1S) 9460.30 |

- **Verdict:** **SUPPORTED** if silver has p < 0.05; **NOT SUPPORTED** otherwise.

**S3. The silver-ratio switch: is it robust? (MEANING-tier check.)**
- **Measure:** H(z_on)/H₀ at the NR best fits (DES Y5, Pantheon+), with z_on defined as the redshift where the field has covered f of its move since recombination, for f = 5%, 10%, 20% and 50%.
- **Verdict:** **ROBUST** if all 8 values are within ±2% of 2.41421; **DEFINITION-DEPENDENT** otherwise.
- **Tier:** even a ROBUST result stays MEANING. It is one number from a model fitted to data, and has no physical mechanism.

## Expectations (logged before computing; not rules)

| Test | Expected |
|---|---|
| G2 | NOT REPLICATED. SUGGESTIVE results at p ≈ 0.04 among 6 tries usually fade |
| S2 | NOT SUPPORTED |
| S3 | DEFINITION-DEPENDENT. H(z) changes steadily with z, so different f give different values |

**Surprise threshold:** a REPLICATED G2 would be the first independent support for any ratio pattern here. It would then get a third, fully separate set before anything is claimed.
