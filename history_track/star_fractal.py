"""PREREGISTRATION_STAR_FRACTAL.md and _ND.md: correlation dimension of nearby stars in 1D-6D (positions + velocities).
    venv312 python star_fractal.py extract   -> star_fractal_sample.npz  (all 12,288 AEGIS Gaia tiles)
    venv312 python star_fractal.py measure   -> STAR_FRACTAL_RESULTS.json, star_fractal.png
"""
import glob
import json
import sys
from multiprocessing import Pool

import numpy as np

TILES = r"C:\Users\Danny\.copilot\repos\AEGIS\ufe-v2\cosmos_map\tiles\L5"
COLS = ["ra", "dec", "dist_pc", "x_pc", "y_pc", "z_pc", "g_mag", "ruwe", "pmra", "pmdec", "rv"]
RMAX, RCEN = 200.0, 100.0          # sample radius; centres kept within RCEN so spheres up to r = 100 stay inside


def read_tile(path):
    import pandas as pd
    d = pd.read_csv(path, usecols=COLS)
    mg = d.g_mag + 5 - 5 * np.log10(d.dist_pc)
    d = d[(d.dist_pc < RMAX) & (d.ruwe < 1.4) & (mg <= 10)]
    return d.to_numpy(dtype=float)


def extract():
    files = sorted(glob.glob(TILES + r"\*.csv.gz"))
    print(len(files), "tiles", flush=True)
    out = []
    with Pool(4) as pool:
        for i, a in enumerate(pool.imap_unordered(read_tile, files, chunksize=32)):
            out.append(a)
            if i % 1000 == 0:
                print(i, flush=True)
    a = np.concatenate(out)
    np.savez_compressed("star_fractal_sample.npz", **{c: a[:, k] for k, c in enumerate(COLS)})
    print(len(a), "stars;", int(np.isfinite(a[:, COLS.index("rv")]).sum()), "with radial velocity", flush=True)


def velocities(s):
    import astropy.units as u
    from astropy.coordinates import SkyCoord
    c = SkyCoord(ra=s["ra"] * u.deg, dec=s["dec"] * u.deg, distance=s["dist_pc"] * u.pc,
                 pm_ra_cosdec=s["pmra"] * u.mas / u.yr, pm_dec=s["pmdec"] * u.mas / u.yr,
                 radial_velocity=s["rv"] * u.km / u.s, frame="icrs").galactic
    v = c.velocity
    return np.c_[v.d_x.to_value(u.km / u.s), v.d_y.to_value(u.km / u.s), v.d_z.to_value(u.km / u.s)]


def corr_dim(pts, centres_mask, radii, rng, n_centres=20000):
    from scipy.spatial import cKDTree
    tree = cKDTree(pts)
    idx = np.flatnonzero(centres_mask)
    idx = rng.choice(idx, size=min(n_centres, idx.size), replace=False)
    ctree = cKDTree(pts[idx])
    counts = ctree.count_neighbors(tree, radii).astype(float) - idx.size      # remove self-pairs
    C = counts / idx.size
    lr, lc = np.log(radii), np.log(np.maximum(C, 1e-300))
    D = np.gradient(lc, lr)
    return C, D


def verdicts(radii, D, d):
    lr = np.log10(radii)
    def longest(mask):
        best, start = 0.0, None
        for i, m in enumerate(mask):
            if m and start is None:
                start = i
            if (not m or i == len(mask) - 1) and start is not None:
                end = i if m else i - 1
                best = max(best, lr[end] - lr[start]); start = None
        return best
    frac = longest(D < d - 0.3)
    homo = longest(np.abs(D - d) <= 0.1)
    v = []
    if frac >= 1.0:
        v.append(f"FRACTAL-LIKE over {frac:.2f} dex")
    if homo >= 0.5:
        v.append(f"HOMOGENEOUS over {homo:.2f} dex")
    return v or ["TRANSITION"], frac, homo


def measure():
    s = dict(np.load("star_fractal_sample.npz"))
    rng = np.random.default_rng(1)
    pos = np.c_[s["x_pc"], s["y_pc"], s["z_pc"]]
    rcen = np.linalg.norm(pos, axis=1) < RCEN
    radii = np.logspace(np.log10(0.3), 2, 26)
    res = {"n_stars": int(len(pos)), "radii": radii.tolist(), "spaces": {}}
    # Poisson reference in 3D, same N and volume
    u = rng.normal(size=(len(pos), 3)); u /= np.linalg.norm(u, axis=1)[:, None]
    poi = u * (RMAX * rng.random(len(pos)) ** (1 / 3))[:, None]
    _, Dp = corr_dim(poi, np.linalg.norm(poi, axis=1) < RCEN, radii, rng)
    res["poisson_3d_D"] = Dp.tolist()
    has_rv = np.isfinite(s["rv"])
    vel = np.full((len(pos), 3), np.nan)
    vel[has_rv] = velocities({k: v[has_rv] for k, v in s.items()})
    res["n_with_rv"] = int(has_rv.sum())
    sets = [("1D x", pos[:, :1], np.ones(len(pos), bool)), ("2D x,y", pos[:, :2], np.ones(len(pos), bool)),
            ("3D x,y,z", pos, np.ones(len(pos), bool))]
    full = np.c_[pos, vel]
    for d, name in ((1, "1D x"), (2, "2D x,y"), (3, "3D x,y,z"), (4, "4D +U"), (5, "5D +U,V"), (6, "6D +U,V,W")):
        sets.append((name + " [rv sample]", full[:, :d], has_rv))
    for name, pts, keep in sets:
        d = pts.shape[1]
        P, cm = pts[keep], rcen[keep]
        C, D = corr_dim(P, cm, radii, rng)
        v, frac, homo = verdicts(radii, D, d)
        res["spaces"][name] = {"d": d, "n": int(len(P)), "D": D.tolist(), "C": C.tolist(), "verdict": v}
        print(f"{name:24s} n={len(P):8d}  D(0.3,1,3,10,30,100)=" +
              " ".join(f"{np.interp(np.log(x), np.log(radii), D):.2f}" for x in (0.3, 1, 3, 10, 30, 100)) +
              f"  -> {'; '.join(v)}", flush=True)
    json.dump(res, open("STAR_FRACTAL_RESULTS.json", "w"), indent=1)
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    for name, r in res["spaces"].items():
        (ax[0] if "rv" not in name else ax[1]).plot(radii, r["D"], label=f"{name} (n={r['n']})")
    for a in ax:
        a.plot(radii, Dp, "k:", label="Poisson 3D (random)")
        a.set_xscale("log"); a.set_xlabel("scale r (pc, or km/s ≈ pc/Myr)"); a.set_ylabel("local dimension D(r)")
        a.grid(alpha=0.3); a.legend(fontsize=8)
        for k in range(1, 7):
            a.axhline(k, color="0.85", lw=0.8, zorder=0)
    ax[0].set_title("Positions, full sample: 1D, 2D, 3D")
    ax[1].set_title("Radial-velocity sample: 1D to 6D (phase space)")
    fig.suptitle("Correlation dimension of stars within 200 pc (Gaia DR3, AEGIS store). History/art track, not cosmology.")
    fig.tight_layout(); fig.savefig("star_fractal.png", dpi=130)


if __name__ == "__main__":
    {"extract": extract, "measure": measure}[sys.argv[1]]()
