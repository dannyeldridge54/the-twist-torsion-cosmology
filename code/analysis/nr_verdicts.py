"""NR verdicts (PREREGISTRATION_NLFIX_REPLICATION.md): the identical rules (rank_models.py's own functions), applied to
the "_nlfix" runs, with the same ΛCDM / w0–wa references. Prints a side-by-side table: as written vs corrected code.
    python nr_verdicts.py            (safe at any time; missing runs show as pending)"""
import json
import math
import os

import rank_models as r

R = r.RES
GRID = [f"gF{a:g}m{b:g}" for a in r.GRID_LF for b in r.GRID_LM]
EDGE = list(r.EDGE_PTS)
HC = ["gF-0.6m0.751", "gF-0.6m1.052", "gF-0.6m1.353", "gF-0.4m0.551", "gF-0.4m0.852", "gF-0.4m1.153", "gF-0.2m0.351",
      "gF-0.2m0.652", "gF-0.2m0.953"]


def c(n):
    p = os.path.join(R, f"cmp_{n}.json")
    return json.load(open(p))["minimum"] if os.path.exists(p) else None


def best(names):
    rows = [(c(n)["chi2"], n) for n in names if c(n)]
    return min(rows) if rows else (None, None)


def accounted(names):
    done = 0
    for n in names:
        log = os.path.join(R, "lanes", f"{n}.log")
        if c(n) or (os.path.exists(log) and any(s in open(log, errors="ignore").read()
                                                 for s in ("-100000", "Cannot reproduce log minimum"))):
            done += 1
    return done


def tag(n):
    import re
    g = re.search(r"_gF(-?[0-9.]+)m(-?[0-9.]+)", n)
    return {"log10_F": float(g.group(1)), "log10_m": float(g.group(2))}


def lee(d, names):
    if d is None or d >= 0:
        return "NOT SIGNIFICANT" if d is not None else "pending"
    n_eff = len({round(tag(n)["log10_F"], 6) for n in names if c(n)})
    from statistics import NormalDist
    pl = math.exp(d / 2)
    pg = 1 - (1 - pl) ** n_eff
    z = lambda p: NormalDist().inv_cdf(1 - p / 2) if p < 1 else 0.0
    zg = z(pg)
    return f"Z_loc {z(pl):.2f}σ → Z_glob {zg:.2f}σ (N_eff {n_eff}) → " + (
        "HOLDS" if zg >= 2 else "WEAK HINT" if zg >= 1 else "NOT SIGNIFICANT")


ref = {k: (c(f"ax_spa_lcdm_halofit{k}") or {}).get("chi2") for k in ("", "_desy5", "_dovekie")}
w0wa = {k: (c(f"ax_spa_w0wa_halofit{k}") or {}).get("chi2") for k in ("", "_desy5", "_dovekie")}
out = ["| Test | As written | Corrected code (NR) |", "|---|---|---|"]
for sfx, lab, pts in (("", "Pantheon+", GRID), ("_desy5", "DES Y5", GRID + EDGE)):
    row = {}
    for ver, suf in (("as", ""), ("nr", "_nlfix")):
        names = [f"ax_spa_latetwist_{p}{sfx}{suf}" for p in pts]
        b, n = best(names)
        d = None if b is None else b - ref[sfx]
        done = accounted(names)
        v3 = r.l3(tag(n))[0] if n else "pending"
        row[ver] = (d, n, done, len(names), b, v3, lee(d, names))
    for key, f in (("L1", lambda x: f"{r.fmt(x[0])} → {r.l1(x[0])}"),
                   ("L2", lambda x: f"D {r.fmt(None if x[4] is None else x[4] - w0wa[sfx])} → "
                                    f"{r.l2(None if x[4] is None else x[4] - w0wa[sfx])}"),
                   ("L3", lambda x: x[5]), ("LEE-G", lambda x: x[6]),
                   ("best point", lambda x: f"{(x[1] or '—').replace('ax_spa_latetwist_', '')} ({x[2]}/{x[3]} accounted)")):
        out.append(f"| {lab} {key} | {f(row['as'])} | {f(row['nr'])} |")
for ver, suf in (("as", ""), ("nr", "_nlfix")):
    pass
ld = {}
for ver, suf in (("as", ""), ("nr", "_nlfix")):
    b, n = best([os.path.basename(p)[4:-5] for p in __import__("glob").glob(
        os.path.join(R, f"cmp_ax_spa_latetwist_gF*_dovekie{suf}.json")) if (suf or not p.endswith("_nlfix.json"))])
    d = None if b is None or ref["_dovekie"] is None else b - ref["_dovekie"]
    ld[ver] = "pending" if d is None else f"{r.fmt(d)} → " + (
        "CONFIRMED" if d <= -4 else "WEAKENED" if d <= -1 else "NOT CONFIRMED")
out.append(f"| LD (Dovekie) | {ld['as']} | {ld['nr']} |")
hc = {}
for ver, suf in (("as", ""), ("nr", "_nlfix")):
    b, n = best([f"ax_spa_latetwist_{p}{suf}" for p in HC])
    g, _ = best([f"ax_spa_latetwist_{p}{suf}" for p in GRID])
    hc[ver] = "pending" if b is None or g is None else f"Δ_HC {r.fmt(b - g)} → " + (
        "BETTER CORNER" if b - g <= -1 else "SIMILAR" if b - g < 1 else "WORSE")
out.append(f"| HC | {hc['as']} | {hc['nr']} |")
import glob as _g
for ver, suf in (("as", ""), ("nr", "_nlfix")):
    pass
cp = {}
for ver, suf in (("as", ""), ("nr", "_nlfix")):
    files = [os.path.basename(p)[4:-5] for p in _g.glob(os.path.join(R, f"cmp_ax_spa_coupledtwist_gF*{suf}.json"))
             if suf or not p.endswith("_nlfix.json")]
    b, n = best(files)
    lt, _ = best([f"ax_spa_latetwist_{p}{suf}" for p in GRID])
    c5 = [x for x in (best([os.path.basename(p)[4:-5] for p in _g.glob(os.path.join(
        R, f"cmp_ax_spa_coupledtwist_beta{s}0.816_gF*{suf}.json")) if suf or not p.endswith("_nlfix.json")])[0]
        for s in ("", "-")) if x is not None]
    if b is None:
        cp[ver] = ("pending",) * 4
        continue
    d1, d2, d3 = b - ref[""], (b - lt) if lt else None, b - w0wa[""] + 2
    cp[ver] = (f"{r.fmt(d1)} → " + ("PASS" if d1 < -6 else "FAIL" if d1 >= 0 else "INCONCLUSIVE"),
               "pending" if d2 is None else f"{r.fmt(d2)} → " + ("NEEDED" if d2 < -4 else "NOT NEEDED" if d2 >= -1 else "MILD"),
               f"{r.fmt(d3)} → " + ("PREFERRED" if d3 < -2 else "AS GOOD AS" if abs(d3) <= 2 else "WORSE"),
               "pending" if not c5 else ("SURVIVES" if min(c5) - ref[""] < 0 else "EXCLUDED"))
for i, k in enumerate(("C1 vs ΛCDM", "C2 coupling needed", "C3 vs w0–wa (ΔAIC)", "C5 β = 0.816")):
    out.append(f"| Coupled {k} | {cp['as'][i]} | {cp['nr'][i]} |")
print("\n".join(out))
