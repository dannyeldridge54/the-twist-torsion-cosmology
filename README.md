# The Twist: a pre-registered test of a torsion-motivated scalar field

**Author:** Danny Lee Eldridge · **Version:** 3 (working copy, 1 November 2026) · **Licence:** Hippocratic License 3.0
(HL3-MIL-SV, see `licence/`)

> *Offered freely to everyone, especially the people who will build the technologies and crafts to come.*

This repository holds the whole programme in one place: the idea, every rule written before its test, every fit
result, the code that produced them, the honest verdicts (including every loss), and the paper. Nothing in it is
third-party data; the public likelihoods and codes it uses are listed in `REPRODUCE.md`.

**Status:** some fits are still running tonight. Rows marked *pending* in `CLAIMS_INDEX.md` are filled in when they
finish, and this package is rebuilt. It has **not been published**. Publishing (Zenodo, arXiv) is the author's
decision.

---

## 1. The idea in plain words

**The question.** The universe's expansion rate (H₀) comes out about 67–68 when it is inferred from the early universe,
and about 70–73 when it is measured today. Separately, the newest galaxy maps (DESI) hint that dark energy may be
changing.

**The proposal.** In Einstein–Cartan gravity, spacetime can twist (torsion) as well as curve. Its Barbero–Immirzi
parameter γ can become a field:

  φ = √(3/2) M_Pl · arsinh(1/γ)

This is a healthy, axion-like field with a natural range of about the Planck mass. It is *motivated* by torsion, not
derived from it. It is tested in three roles:

| Role | What it does | Potential |
|---|---|---|
| **Early Twist** (Locked Twist) | A few percent of extra energy peaking at matter–radiation equality | Λ⁴[1 − cos(φ/F)]³ (assumed) |
| **Late Twist** | The same kind of field thawing today, as all the dark energy | Λ⁴[1 − cos(φ/F)] (natural) |
| **Coupled Twist** | The Late Twist plus a coupling β to dark matter | as Late Twist, with m_c ∝ e^{βφ/M_Pl} |

## 2. The honest headline (so far)

- **Early energy:** Planck, ACT and all CMB data combined prefer about 7–8% early energy. That is 2.4σ at the best
  angle, but **only about 1.2–1.4σ** once the look-elsewhere effect is counted. SPT-3G alone does not see it. Allowed
  alongside late dark energy, the hint is **mild**, and it is fragile across supernova samples.
- **Late Twist:**
  - With Pantheon+ it fits about as well as ΛCDM, a tie once a code artefact is corrected (see below).
  - With DES Y5 supernovae it improves on ΛCDM (preliminary). Whether that survives the corrected DES-Dovekie sample
    is pre-registered and running.
- **A code artefact, found and explained:** AxiCLASS's halofit reads a matter density inflated by the field, which
  adds about +1.35 to every Late Twist χ². It was found by a null test and confirmed (+0.03 with halofit off).
- **What would make it strong:** a prediction only the twist makes, locked before the data. The planned one is the
  CMB polarisation rotation (birefringence) from the field's photon coupling.

The full scoreboard of every pre-registered test, wins and losses alike, is in
`results_notes/PAPER_SCOREBOARD_DRAFT.md`.

## 3. How the work was done (the method is the contribution)

1. **Rules first.** Every test's rule (data, statistic, thresholds, verdict wording) was written, SHA-256 hashed and
   committed *before* its result existed. Deviations are logged, dated and append-only
   (`preregistrations/PREREGISTRATION_SPT3G_DEVIATIONS.md`).
2. **Two codes.** CAMB and AxiCLASS agree within 0.4 in χ².
3. **Pipeline check.** Our late-dark-energy gains reproduce DESI DR2's published numbers within 0.33.
4. **Every loss printed.** Failed predictions stay in the record.
5. **Null tests.** These include the null mirror that exposed the halofit artefact.
6. **Scales checkpoints.** At every major step there is a local consistency check (hashes, numbers, run health,
   untracked results, garbled text) plus online literature rounds, recorded in
   `results_notes/SCALES_CHECKPOINT.md`.

## 4. What is where

| Folder | Contents |
|---|---|
| `CLAIMS_INDEX.md` | **Start here:** every claim → its rule (with hash) → result file → script → verdict |
| `LOCK_TIMES.md` | When each rule and result first entered version control (proof of "rule before result") |
| `REPRODUCE.md` | How to rebuild the environment and rerun any fit |
| `verify.py` | Recomputes every hash: rules against their `.sha256` files and all files against `MANIFEST.txt` |
| `MANIFEST.txt` | SHA-256 and size of every file in this repository |
| `paper/` | Paper v3 (LaTeX and PDF) |
| `preregistrations/` | Every rule, with its `.sha256` |
| `results_notes/` | Verdict write-ups, the thesis, the route, reviews, the scoreboard |
| `fit_results/` | Every fit's best-fit point and χ² (`cmp_*.json`) plus derived results |
| `code/axiclass/` | Fit drivers, grid, edge, LD and HC runners, null mirror |
| `code/coupled/` | The Coupled Twist patch to AxiCLASS, its build script and validation gates |
| `code/analysis/` | Ranking (all verdicts), house check, look-elsewhere, lock attractor and others |
| `history_track/` | History and art studies (old books, stars in 1D–6D), kept separate: **not evidence for the physics** |
| `licence/` | Licence, pledge, citation file |

## 5. Check it yourself

```
python verify.py
```

This confirms that no rule or result changed after it was hashed. `LOCK_TIMES.md` then shows that each rule's
commit came before its result's commit. The original commit history lives in the two working repositories (AEGIS and
CubeMind) and is available on request.

## 6. Earlier records

- Zenodo: N = 9 prediction 10.5281/zenodo.23838969
- Zenodo: Silver 10.5281/zenodo.23839507
- Zenodo: UFE v2 paper 10.5281/zenodo.23847152

## 7. Thanks

To everyone whose public data and open codes made this possible: Planck, ACT, SPT-3G, DESI, Pantheon+, DES, CAMB,
CLASS and AxiCLASS, Cobaya. And to everyone who came before.
