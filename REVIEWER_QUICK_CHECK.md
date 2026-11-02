# For reviewers: check this work in 10 minutes

You do not have to trust anything here. Every claim can be checked from public files. Here is how.

## 1. What is claimed, and what is NOT

| Claimed (with its strength) | NOT claimed |
|---|---|
| Early dark energy: a weak hint, 1.2–1.4σ after look-elsewhere | That the Hubble tension is solved |
| Late field on corrected code: ties ΛCDM (Pantheon+); −6.2 with DES Y5, 1.3σ global, weakened on DES-Dovekie | That it beats w0–wa (it never does) |
| Coupled field: −7.9 with β ≈ ±0.05, but S8 worsens | That torsion fixes the coupling (β = 0.816 is excluded) |
| The minimal field cannot make the measured birefringence | That it explains birefringence |
| One clean open prediction: R = 0.997 (switch-on z ≈ 1.5) | A detection of anything |
| Two AxiCLASS bugs, reproducible in 10 s (`code/nlfix/BUG_REPORT.md`) | — |

## 2. Were the rules written before the results? (2 minutes)

```
python verify.py
```

- `verify.py` checks every rule file against its `.sha256`, and every file against `MANIFEST.txt`.
- `LOCK_TIMES.md` then lists, for each rule and its result, the commit time each first entered version control. Each
  rule's time is before its result's.

## 3. Is a headline number what the files say? (3 minutes)

Take any Δχ²: it is χ²(model) − χ²(ΛCDM reference), read straight from the `minimum.chi2` field of two files in
`fit_results/`. Example, the Late Twist with DES Y5 on corrected code:

```
python -c "import json;f=lambda n:json.load(open(f'fit_results/cmp_{n}.json'))['minimum']['chi2'];print(f('ax_spa_latetwist_gF0m0.102_desy5_nlfix')-f('ax_spa_lcdm_halofit_desy5'))"
```

This should print −6.23. `code/analysis/nr_verdicts.py` applies every rule and prints the full side-by-side table.

## 4. Are the code bugs real? (1 minute with AxiCLASS installed)

```
python code/nlfix/bug_reproducer.py <AxiCLASS>/python/build
```

For a frozen field that must equal Λ, the installed AxiCLASS gives σ8 = 0.25 instead of 0.81.

## 5. Where to push hardest (our own list of weak points)

1. Best fits and profile likelihoods only: no MCMC posteriors or Bayesian evidence for the Twist models.
2. Lite ACT/SPT likelihoods, not the full multi-frequency ones.
3. The (F, m) plane is profiled on a coarse grid (24 points + 8 edge points).
4. Early and late roles use two potentials (n = 3 and n = 1); one field doing both is not shown.
5. The birefringence test depends on the photon-coupling reading (decoupling vs anomaly). Both are reported, and the
   primary reading was fixed before comparison.
6. AI assistants did much of the coding and drafting under the author's direction. Every number is reproducible from
   the public files, which is why this guide exists.

Corrections are welcome and credited: dannyeldridge54@gmail.com, or open an issue on the repository.
