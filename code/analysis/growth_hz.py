"""GH (PREREGISTRATION_GROWTH_HZ.md, locked 2026-11-02 15:31:34): no-refit predictions of the stored best fits against
cosmic chronometers H(z) (Moresco pipeline covariance) and SDSS RSD-only fsigma8(z). Data: data/growth_hz_data.json.
WSL, micromamba env 'aegis', one model per process (different AxiCLASS builds):
    python growth_hz.py eval <run name>   -> gh_<name>.json (H(z), fsigma8(z), log-posterior mirror)
    python growth_hz.py score             -> growth_hz.json"""
import json
import os
import sys

import numpy as np

AXI = os.environ.get("TWIST_AXI", "/mnt/c/Users/Danny/.copilot/repos/AEGIS/cmb-fit/axiclass")
HERE = os.path.dirname(os.path.abspath(__file__))
D = json.load(open(os.path.join(HERE, "data", "growth_hz_data.json")))
MODELS = {"LT-P": ("ax_spa_latetwist_gF0.4m-0.3_nlfix", "ax_spa_lcdm_halofit"),
          "LT-D": ("ax_spa_latetwist_gF0m0.102_desy5_nlfix", "ax_spa_lcdm_halofit_desy5"),
          "CT": ("ax_spa_coupledtwist_gF0.4m-0.1_nlfix", "ax_spa_lcdm_halofit"),
          "w0wa-P (context)": ("ax_spa_w0wa_halofit", "ax_spa_lcdm_halofit"),
          "w0wa-D (context)": ("ax_spa_w0wa_halofit_desy5", "ax_spa_lcdm_halofit_desy5")}


def predict(_self=None):
    return 0.0


def evaluate(name):
    sys.path.insert(0, AXI)
    import early_late_spa as E
    from cobaya.model import get_model
    E._maybe_coupled(name)
    info = E.make(name)
    for k in ("sampler", "output", "resume", "force"):
        info.pop(k, None)
    zh, zf = np.array(D["cc"]["z"]), np.array(D["fs8"]["z"])
    info["likelihood"]["gh_predict"] = {"external": predict,
                                        "requires": {"Hubble": {"z": np.concatenate([[0.0], zh])},
                                                     "fsigma8": {"z": zf}}}
    model = get_model(info)
    stored = json.load(open(f"{E.OUT}/cmp_{name}.json"))["minimum"]
    point = {p: stored[p] for p in model.parameterization.sampled_params()}
    res = model.logposterior(point)
    pr = model.provider
    out = {"name": name, "H": [float(x) for x in pr.get_Hubble(zh, units="km/s/Mpc")],
           "fs8": [float(x) for x in pr.get_fsigma8(zf)], "H0": float(pr.get_Hubble([0.0], units="km/s/Mpc")[0]),
           "logpost": float(res.logpost), "logpost_stored": -float(stored["minuslogpost"])}
    json.dump(out, open(os.path.join(HERE, f"gh_{name}.json"), "w"), indent=1)
    print(name, "logpost", out["logpost"], "stored", out["logpost_stored"], "H0", out["H0"])


def cc_cov():
    c = D["cc"]
    z, H, e = (np.array(c[k]) for k in ("z", "Hz", "errHz"))
    m = c["mm20"]
    cov = np.diag(e ** 2)
    for key in ("imf", "spsooo"):
        x = np.interp(z, m["z"], m[key]) / 100
        cov += np.outer(H * x, H * x)
    return cov


def chi2s(name):
    g = json.load(open(os.path.join(HERE, f"gh_{name}.json")))
    r = np.array(g["H"]) - np.array(D["cc"]["Hz"])
    ch = float(r @ np.linalg.inv(cc_cov()) @ r)
    f = (np.array(g["fs8"]) - np.array(D["fs8"]["fs8"])) / np.array(D["fs8"]["err"])
    return ch, float(f @ f), abs(g["logpost"] - g["logpost_stored"]) <= 0.05, g


def verdict(d):
    return "SUPPORTS" if d <= -2 else "DISFAVOURS" if d >= 2 else "NEUTRAL"


def score():
    rows = {}
    for label, (m, ref) in MODELS.items():
        hm, fm, okm, gm = chi2s(m)
        hr, fr, okr, gr = chi2s(ref)
        ctx = "context" in label
        dh, df = hm - hr, fm - fr
        rows[label] = {"model": m, "ref": ref, "chi2_H": hm, "chi2_H_ref": hr, "chi2_f": fm, "chi2_f_ref": fr,
                       "dH": dh, "df": df, "dsum": dh + df, "mirror_pass": okm and okr,
                       "H0": gm["H0"], "H0_ref": gr["H0"],
                       "verdict_H": "context" if ctx else (verdict(dh) if okm and okr else "NO VERDICT (mirror)"),
                       "verdict_f": "context" if ctx else (verdict(df) if okm and okr else "NO VERDICT (mirror)")}
    json.dump(rows, open(os.path.join(HERE, "growth_hz.json"), "w"), indent=1)
    for k, v in rows.items():
        print(f"{k:18s} dH {v['dH']:+6.2f} ({v['verdict_H']})  df {v['df']:+6.2f} ({v['verdict_f']})  "
              f"sum {v['dsum']:+6.2f}  chi2_H {v['chi2_H']:.2f}/{v['chi2_H_ref']:.2f}  chi2_f {v['chi2_f']:.2f}/"
              f"{v['chi2_f_ref']:.2f}  H0 {v['H0']:.2f}/{v['H0_ref']:.2f}  mirror {v['mirror_pass']}")


if __name__ == "__main__":
    evaluate(sys.argv[2]) if sys.argv[1] == "eval" else score()
