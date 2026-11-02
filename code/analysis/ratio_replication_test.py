"""Ratio replication (PREREGISTRATION_RATIO_REPLICATION.md, locked 2026-11-02 12:01:34): G2 golden on Z = 21-60 ionisation
energies, S2 silver on 18 hadron masses. Same D statistic and null as B4-X X9 (b4x_ratio_test.py), new seed 20261103."""
import json
import math

import numpy as np

from b4x_ratio_test import CAND, D, IE as IE_2_20

IE_21_60 = [6.5615, 6.8281, 6.7462, 6.7665, 7.4340, 7.9025, 7.8810, 7.6399, 7.7264, 9.3942,
            5.9993, 7.8994, 9.7886, 9.7524, 11.8138, 13.9996, 4.1771, 5.6949, 6.2173, 6.6341,
            6.7589, 7.0924, 7.1194, 7.3605, 7.4589, 8.3368, 7.5762, 8.9938, 5.7864, 7.3439,
            8.6084, 9.0098, 10.4512, 12.1298, 3.8939, 5.2117, 5.5769, 5.5386, 5.4702, 5.5248]
HADRONS = [139.57, 493.677, 547.862, 775.26, 782.66, 891.67, 957.78, 1019.461, 938.272, 1115.683, 1189.37, 1232,
           1314.86, 1672.45, 1864.84, 3096.90, 5279.34, 9460.30]
H = 13.598
SETS = {"G2 atomic Z=21-60": (np.log(np.array(IE_21_60) / H), "golden"),
        "S2 hadron mass ratios": (np.diff(np.log(sorted(HADRONS))), "silver"),
        "(desc) Z=21-40": (np.log(np.array(IE_21_60[:20]) / H), None),
        "(desc) Z=41-60": (np.log(np.array(IE_21_60[20:]) / H), None),
        "(desc) Z=2-60 pooled": (np.log(np.array(IE_2_20[1:] + IE_21_60) / H), None)}
rng = np.random.default_rng(20261103)
rand = np.exp(rng.uniform(math.log(1.3), math.log(3.5), 100_000))
res = {}
for name, (logr, primary) in SETS.items():
    Dr = D(logr, rand)
    for cn, c in CAND.items():
        d = float(D(logr, c)[0]); p = float(np.mean(Dr <= d))
        if cn == primary:
            verdict = ("REPLICATED" if p < 0.05 else "NOT REPLICATED") if primary == "golden" else \
                      ("SUPPORTED" if p < 0.05 else "NOT SUPPORTED")
        else:
            verdict = "(reported)"
        res[f"{name} | {cn}"] = {"n": int(len(logr)), "D": d, "p": p, "verdict": verdict}
        print(f"{name:24s} n={len(logr):2d} {cn:7s} D = {d:.3f}  p = {p:.3f}  {verdict}")
json.dump(res, open("ratio_replication_test.json", "w"), indent=1)
