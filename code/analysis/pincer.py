"""PC pincer test (PREREGISTRATION_PINCER.md, locked 2026-11-02 16:22:30): CMB-only best fits predict the late data.
    python pincer.py eval <cmbonly run>   -> pc_<run>.json   (WSL env 'aegis'; late chi2 at the CMB-only point, no refit)
    python pincer.py score                -> pincer.json"""
import json
import os
import sys

AXI = os.environ.get("TWIST_AXI", "/mnt/c/Users/Danny/.copilot/repos/AEGIS/cmb-fit/axiclass")
RES = os.environ.get("TWIST_RESULTS", r"C:\Users\Danny\.copilot\repos\AEGIS\cmb-fit\results")
HERE = os.path.dirname(os.path.abspath(__file__))
LCDM = "ax_spa_lcdm_halofit_cmbonly"
TWISTS = ("ax_spa_latetwist_gF0m0.102_cmbonly_nlfix", "ax_spa_latetwist_gF0.4m-0.3_cmbonly_nlfix")
SAMPLES = {"Pantheon+": "", "DES-Dovekie": "_dovekie", "Union3": "_union3"}


def late_name(cmb_name, suffix):
    base = cmb_name.replace("_cmbonly", "")
    return base.replace("_nlfix", suffix + "_nlfix") if base.endswith("_nlfix") else base + suffix


def evaluate(cmb_name):
    sys.path.insert(0, AXI)
    import early_late_spa as E
    from cobaya.model import get_model
    E._maybe_coupled(cmb_name)
    stored = json.load(open(f"{E.OUT}/cmp_{cmb_name}.json"))["minimum"]
    out = {"cmb_run": cmb_name, "cmb_chi2_stored": stored.get("chi2"), "late": {}}
    for label, suf in SAMPLES.items():
        info = E.make(late_name(cmb_name, suf))
        for k in ("sampler", "output", "resume", "force"):
            info.pop(k, None)
        model = get_model(info)
        point = {p: stored[p] for p in model.parameterization.sampled_params()}
        res = model.logposterior(point)
        lk = {n: -2 * float(v) for n, v in zip(model.likelihood, res.loglikes)}
        late = {n: v for n, v in lk.items() if n.startswith(("bao.", "sn."))}
        cmb = sum(v for n, v in lk.items() if not n.startswith(("bao.", "sn.")))
        out["late"][label] = {"chi2_late": sum(late.values()), "parts": late, "cmb_chi2_rebuilt": cmb}
        print(cmb_name, label, round(sum(late.values()), 3), "cmb rebuilt", round(cmb, 3), flush=True)
    json.dump(out, open(os.path.join(HERE, f"pc_{cmb_name}.json"), "w"), indent=1)


def score():
    ref = json.load(open(os.path.join(HERE, f"pc_{LCDM}.json")))
    stored = json.load(open(os.path.join(RES, f"cmp_{LCDM}.json")))["minimum"]
    cmb_stored = sum(v for k, v in stored.items() if k.startswith("chi2__") and k[6:] not in ("CMB", "BAO", "SN"))
    mirror = abs(ref["late"]["Pantheon+"]["cmb_chi2_rebuilt"] - cmb_stored) <= 0.05
    out = {"mirror_pass": mirror, "cmb_rebuilt": ref["late"]["Pantheon+"]["cmb_chi2_rebuilt"], "cmb_stored": cmb_stored}
    for t in TWISTS:
        g = json.load(open(os.path.join(HERE, f"pc_{t}.json")))
        d = {s: g["late"][s]["chi2_late"] - ref["late"][s]["chi2_late"] for s in SAMPLES}
        sup, dis = sum(v <= -2 for v in d.values()), sum(v >= 2 for v in d.values())
        verdict = ("NO VERDICT (mirror)" if not mirror else "SUPPORTS" if sup >= 2 else
                   "DISFAVOURS" if dis >= 2 else "NEUTRAL")
        out[t] = {"delta": d, "verdict": verdict}
    json.dump(out, open(os.path.join(HERE, "pincer.json"), "w"), indent=1)
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    evaluate(sys.argv[2]) if sys.argv[1] == "eval" else score()
