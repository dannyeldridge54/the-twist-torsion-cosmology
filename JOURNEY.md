# The journey: how the Twist got here

This is told honestly, failures included, because the record is the point.

## 1. The intuition

Spacetime can bend, and in Einstein–Cartan gravity it can also **twist** (torsion). The starting question was whether
that twist could leave a trace in the universe's expansion: in the Hubble tension, or in DESI's hint that dark
energy changes.

## 2. Version 1: a failure, kept on the record

The first version had **12 bugs**. Once they were fixed, what was left was the standard model with new labels. It was
quarantined, not deleted, and the lesson shaped everything after it: **write the rules down before looking.**

## 3. Version 2: a real field

- The twist was made a real, healthy field: the Barbero–Immirzi parameter γ promoted to φ = √(3/2) M_Pl arsinh(1/γ).
  This is an axion-like field whose natural range is about the Planck mass.
- It was fitted with professional codes (CAMB, then AxiCLASS) to Planck, ACT, DESI and supernova data.
- After a free fit, the extra energy was seen to peak right at **matter–radiation equality**: the "lock". This was
  *disclosed as not blind*, and every later test treated it as an assumption.
- Symbol-derived predictions (width = torsion ÷ 9, starting angle = 1 + √2, a Hebrew-letter Tree, a torus number) were
  each hashed and published on Zenodo **before** being tested on SPT-3G. **They failed or were inconclusive**, and the
  failures are published too.
- UFE v2 paper: 10.5281/zenodo.23847152.

## 4. Version 3: 31 October to 1 November 2026

Each step had a rule hashed first (see `LOCK_TIMES.md`).

| Step | What was asked | What came out |
|---|---|---|
| All three CMB telescopes | Does the early hint hold with Planck + ACT + SPT-3G together? | Yes, Δχ² −5.63 |
| A1 profile | Is zero early energy disfavoured? | f = 0 costs 5.98 |
| A2 look-elsewhere | How significant after counting the free angle? | Only 1.2–1.4σ: **a weak hint** |
| Power n | Is the cos³ shape needed? | n = 3 favoured |
| A3 early + late | Does early energy survive when late dark energy is allowed? | **MILD** (−3.65) |
| Robustness (R1, R2, Dovekie) | Is A3 stable across minimiser restarts and supernova sets? | Stable, but **fragile** across SN sets |
| Lock attractor | Can the dynamics produce the lock? | **NO LOCK**: it stays an assumption |
| Late Twist | Can the natural n = 1 field be all of the dark energy? | Free fits stalled, so a grid was used. Pantheon+ ties ΛCDM (after correction); DES Y5 better (preliminary) |
| Null mirror | Does the code reproduce Λ in the frozen limit? | **No: +1.35.** Traced to halofit reading an inflated Ω_m; it vanishes with halofit off |
| Coupled Twist | Late Twist + dark-matter coupling: build and validate | Patch built; gates V1–V4 pass; fits queued |
| Edge scan, LD, LEE-G, high-mass corner | Probe the edges, correct the supernovae, count the search, test the literature's corner | Locked; running |

**Along the way, the process itself was tightened:**
- **Times:** after hand-typed times were found to be wrong, every time is taken from the system clock, and the house
  check compares header times with commits.
- **Garbled text:** after a shell tool garbled files, a byte-level check was added and the files were repaired.
- **Untracked results:** results that were not committed are now flagged automatically.
- **Scales checkpoints:** at every major step there is a local audit plus online literature rounds, three times over,
  until nothing claim-changing remains.

## 5. What it adds up to so far

- **Early role:** a weak, supernova-dependent hint. The potential shape and the lock are assumed, not derived.
- **Late role:** the natural shape and range fit the data about as well as the standard model, possibly better with
  some supernova sets. Whether that survives is being tested tonight.
- **The method:** rules first, two codes, every loss printed, results that match the big collaborations, and a real
  code artefact found by a null test.

## 6. Where it goes next

1. Fix the halofit artefact, with the deviation logged first.
2. **One field or two?** Look for a single potential for both roles.
3. **The photon coupling:** derive it from the torsion construction, then lock a **birefringence** prediction. This is
   the one test where the twist says something no other model says.
4. **The spin coupling:** check lab bounds.
5. Outside eyes, a versioned archive, and a preprint.

*Offered freely. For balance, not recognition.*
