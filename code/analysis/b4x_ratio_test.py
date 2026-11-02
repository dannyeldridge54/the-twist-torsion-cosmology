"""B4-X rule X9 (PREREGISTRATION_B4X_PHOTON_COUPLING.md, locked 2026-11-02 11:54:34): do the quantum and atomic sets sit
closer to whole powers of the silver ratio, golden ratio or pi than to powers of a random constant?
D(c) = mean over the set of |log_c(r) - nearest integer|; p = fraction of 100,000 log-uniform random constants on
[1.3, 3.5] with D <= D(candidate). SUPPORTED p < 0.05/3, SUGGESTIVE p < 0.05, else NOT SUPPORTED (primaries only)."""
import json
import math

import numpy as np

MASS = {"e": 0.51099895, "u": 2.16, "d": 4.67, "s": 93.4, "mu": 105.6583755, "c": 1270, "tau": 1776.86, "b": 4180,
        "t": 172690}
IE = [13.598, 24.587, 5.392, 9.323, 8.298, 11.260, 14.534, 13.618, 17.423, 21.565, 5.139, 7.646, 5.986, 8.152,
      10.487, 10.360, 12.968, 15.760, 4.341, 6.113]
CAND = {"silver": 1 + math.sqrt(2), "golden": (1 + math.sqrt(5)) / 2, "pi": math.pi}
SETS = {"Q (fermion mass ratios)": (np.diff(np.log(sorted(MASS.values()))), "silver"),
        "A (ionisation / hydrogen)": (np.log(np.array(IE[1:]) / IE[0]), "golden")}


def D(logr, c):
    x = logr[:, None] / np.log(np.atleast_1d(c))[None, :]
    return np.mean(np.abs(x - np.round(x)), axis=0)


rng = np.random.default_rng(20261102)
rand = np.exp(rng.uniform(math.log(1.3), math.log(3.5), 100_000))
res = {}
for name, (logr, primary) in (SETS.items() if __name__ == "__main__" else ()):
    Dr = D(logr, rand)
    for cn, c in CAND.items():
        d = float(D(logr, c)[0]); p = float(np.mean(Dr <= d))
        verdict = ("SUPPORTED" if p < 0.05 / 3 else "SUGGESTIVE" if p < 0.05 else "NOT SUPPORTED") if cn == primary else "(reported)"
        res[f"{name} | {cn}"] = {"D": d, "p": p, "verdict": verdict}
        print(f"{name:28s} {cn:7s} D = {d:.3f}  p = {p:.3f}  {verdict}")
    print(f"{name:28s} null D: median {np.median(Dr):.3f}, 5% {np.percentile(Dr, 5):.3f}")
if __name__ == "__main__":
    json.dump(res, open("b4x_ratio_test.json", "w"), indent=1)
