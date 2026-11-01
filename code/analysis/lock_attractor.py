"""PREREGISTRATION_LOCK_ATTRACTOR.md: can the dynamics put the early field's peak at matter-radiation equality?

Units: M_Pl = 1 (reduced), H in units of 100 km/s/Mpc, rho_i = 3 omega_i a^-n, so H^2 = sum(rho)/3.
Field: V = L4 [1 - cos(phi/F)]^n. CDM coupling (case B): rho_c = 3 omega_c a^-3 exp(beta (phi - phi_i)), source -beta rho_c.
In N = ln a:  phi'' + (3 + H'/H) phi' + V_phi/H^2 = -beta rho_c/H^2.
    python lock_attractor.py check     -> validations (energy balance; m_eff ~ H release estimate)
    python lock_attractor.py scan      -> cases A and B, writes LOCK_ATTRACTOR_RESULTS.json
    python lock_attractor.py phase     -> case C fixed points
"""
import json
import sys

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, fsolve

W_B, W_C, W_R = 0.0225, 0.120, 4.18e-5             # Planck-like; omega_r includes neutrinos (N_eff = 3.044)
Z_EQ = (W_B + W_C) / W_R - 1
N_I, N_F = np.log(1e-7), np.log(1e-2)


def background(L4, F, th, beta, n=3):
    phi_i = th * F
    V = lambda p: L4 * (1 - np.cos(p / F)) ** n
    dV = lambda p: L4 * n * (1 - np.cos(p / F)) ** (n - 1) * np.sin(p / F) / F

    def parts(N, s):
        p, dp = s
        a = np.exp(N)
        rr, rb = 3 * W_R / a ** 4, 3 * W_B / a ** 3
        rc = 3 * W_C / a ** 3 * np.exp(beta * (p - phi_i))
        H2 = (rr + rb + rc + V(p)) / (3 - dp ** 2 / 2)
        return a, rr, rb, rc, H2

    def rhs(N, s):
        p, dp = s
        a, rr, rb, rc, H2 = parts(N, s)
        rpp = 4 / 3 * rr + rb + rc + H2 * dp ** 2           # rho + p
        h = -rpp / (2 * H2)                               # H'/H
        return [dp, -(3 + h) * dp - dV(p) / H2 - beta * rc / H2]

    sol = solve_ivp(rhs, (N_I, N_F), [phi_i, 0.0], method="LSODA", rtol=1e-9, atol=1e-12, dense_output=True,
                    max_step=0.01)
    N = np.linspace(N_I, N_F, 6000)
    s = sol.sol(N)
    out = {k: [] for k in ("a", "f", "rphi", "pphi", "rc", "dp")}
    for i, Ni in enumerate(N):
        a, rr, rb, rc, H2 = parts(Ni, s[:, i])
        kin = H2 * s[1, i] ** 2 / 2
        out["a"].append(a); out["f"].append((kin + V(s[0, i])) / (3 * H2))
        out["rphi"].append(kin + V(s[0, i])); out["pphi"].append(kin - V(s[0, i])); out["rc"].append(rc)
        out["dp"].append(s[1, i])
    out = {k: np.array(v) for k, v in out.items()}
    out["N"] = N
    return out


def zpeak(L4, F, th, beta):
    b = background(L4, F, th, beta)
    i = int(np.argmax(b["f"]))
    return 1 / b["a"][i] - 1, float(b["f"][i])


def central_L4(F, th):
    """Lambda^4 putting the uncoupled peak at z_eq (bisection in log L4)."""
    g = lambda lg: np.log(zpeak(10 ** lg, F, th, 0.0)[0] / Z_EQ)
    return 10 ** brentq(g, 3.0, 12.0, xtol=1e-3)


def energy_check(L4, F, th, beta, n=3):
    """Integrate rho_phi separately with d rho_phi/dN = -3 H^2 phi'^2 - beta rho_c phi' and compare it with
    rho_phi rebuilt from (phi, phi'): tests the integrator against energy conservation directly."""
    phi_i = th * F
    V = lambda p: L4 * (1 - np.cos(p / F)) ** n
    dV = lambda p: L4 * n * (1 - np.cos(p / F)) ** (n - 1) * np.sin(p / F) / F

    def rhs(N, s):
        p, dp, rphi = s
        a = np.exp(N)
        rr, rb = 3 * W_R / a ** 4, 3 * W_B / a ** 3
        rc = 3 * W_C / a ** 3 * np.exp(beta * (p - phi_i))
        H2 = (rr + rb + rc + V(p)) / (3 - dp ** 2 / 2)
        h = -(4 / 3 * rr + rb + rc + H2 * dp ** 2) / (2 * H2)
        return [dp, -(3 + h) * dp - dV(p) / H2 - beta * rc / H2, -3 * H2 * dp ** 2 - beta * rc * dp]

    sol = solve_ivp(rhs, (N_I, N_F), [phi_i, 0.0, V(phi_i)], method="LSODA", rtol=1e-11, atol=1e-14,
                    max_step=0.01, dense_output=True)
    worst = 0.0
    for N in np.linspace(N_I, N_F, 4000):
        p, dp, rphi = sol.sol(N)
        a = np.exp(N)
        rr, rb = 3 * W_R / a ** 4, 3 * W_B / a ** 3
        rc = 3 * W_C / a ** 3 * np.exp(beta * (p - phi_i))
        H2 = (rr + rb + rc + V(p)) / (3 - dp ** 2 / 2)
        worst = max(worst, abs(rphi - (H2 * dp ** 2 / 2 + V(p))) / V(phi_i))
    return worst


def check():
    F, th = 0.2, 2.7
    L4 = central_L4(F, th)
    for beta in (0.0, 0.1):
        print(f"beta={beta}: energy conservation, max |rho_phi(integrated) - rho_phi(phi,phi')| / rho_phi,ini = "
              f"{energy_check(L4, F, th, beta):.2e}  (pre-registered: < 1e-6)")
    b = background(L4, F, th, 0.0)
    phi = np.cumsum(np.r_[0, np.diff(b["N"])] * b["dp"]) + th * F
    start = int(np.argmax(np.abs(phi - th * F) > 0.01 * F))   # field has moved 1% of F: roll begins
    # release estimate: m_eff^2 = |V''(phi_i)| ~ H^2 at release; radiation era H^2 = W_R a^-4
    m2 = abs(L4 * (3 * 2 * (1 - np.cos(th)) * np.sin(th) ** 2 + 3 * (1 - np.cos(th)) ** 2 * np.cos(th)) / F ** 2)
    a_rel = (W_R / m2) ** 0.25
    zp, fp = zpeak(L4, F, th, 0.0)
    print(f"central L4={L4:.3e}: z_peak {zp:.0f} (z_eq {Z_EQ:.0f}), f_peak {fp:.3f}")
    print(f"release: m_eff = H estimate z {1 / a_rel - 1:.0f}; field starts rolling (moved 1% of F) at "
          f"z {1 / b['a'][start] - 1:.0f}")
    z1 = zpeak(L4, F, th, 0.0)[0]
    print(f"tolerance check: z_peak {z1:.1f} (rtol 1e-9)")


def scan():
    res = {"z_eq": Z_EQ, "cases": []}
    facs = np.logspace(-1, 1, 9)                         # two decades of L4
    for F in (0.1, 0.2):
        for th in (2.7, 3.1, np.pi - 1e-3):
            L4c = central_L4(F, th)
            for beta in (0.0, 0.01, 0.03, 0.1, 0.3):
                if th > 3.14 and beta == 0.0:
                    pass                                 # the uncoupled hilltop case is kept as a reference
                zs, fs = [], []
                for k in facs:
                    try:
                        zp, fp = zpeak(L4c * k, F, th, beta)
                    except Exception as e:
                        zp, fp = float("nan"), float("nan")
                    zs.append(zp); fs.append(fp)
                zs, fs = np.array(zs), np.array(fs)
                S = float(np.nanmax(zs) / np.nanmin(zs))
                at_eq = bool(np.all((zs > Z_EQ / 1.5) & (zs < 1.5 * Z_EQ)))
                rel = bool(0.03 <= fs[len(fs) // 2] <= 0.12)
                v = ("LOCK DERIVED" if S < 1.5 and at_eq and rel else
                     "PARTIAL" if (S < 1.5) or (at_eq and S < 2.5) else "NO LOCK")
                row = {"case": "A" if beta == 0 else "B", "F": F, "theta_i": round(float(th), 4), "beta": beta,
                       "L4_central": L4c, "S": S, "z_peaks": [round(float(z)) for z in zs],
                       "f_peak_central": float(fs[len(fs) // 2]), "relevant": rel, "verdict": v}
                res["cases"].append(row)
                print(f"F={F} th={th:.4f} beta={beta:<5} S={S:5.2f} z={row['z_peaks'][0]}..{row['z_peaks'][-1]} "
                      f"f_c={row['f_peak_central']:.3f} -> {v}", flush=True)
    json.dump(res, open("LOCK_ATTRACTOR_RESULTS.json", "w"), indent=1)


def phase():
    """Case C: fixed points of (x, y, r) with constant local lambda; Omega_c = f_c (1 - x^2 - y^2 - r)."""
    fc = W_C / (W_B + W_C)

    def f(v, lam, beta):
        x, y, r = v
        h = -(3 + 3 * x * x - 3 * y * y + r) / 2
        oc = fc * (1 - x * x - y * y - r)
        return [-(3 + h) * x + np.sqrt(1.5) * (lam * y * y - beta * oc), y * (-np.sqrt(1.5) * lam * x - h), r * (-4 - 2 * h)]

    out = []
    for lam in (0.1, 1.0, 3.0):
        for beta in (0.0, 0.1):
            pts = set()
            for x0 in np.linspace(-0.9, 0.9, 7):
                for y0 in (0.0, 0.3, 0.7, 0.95):
                    for r0 in (0.0, 0.5, 0.99):
                        sol, info, ok, _ = fsolve(f, [x0, y0, r0], args=(lam, beta), full_output=True)
                        if ok == 1 and np.max(np.abs(f(sol, lam, beta))) < 1e-10:
                            x, y, r = sol
                            if y >= -1e-9 and r >= -1e-9 and x * x + y * y + r <= 1 + 1e-9:
                                pts.add((round(x, 5), round(abs(y), 5), round(r, 5)))
            for p in sorted(pts):
                J = np.zeros((3, 3)); e = 1e-7
                for j in range(3):
                    dpv = np.array(p, float); dpv[j] += e
                    J[:, j] = (np.array(f(dpv, lam, beta)) - np.array(f(np.array(p, float), lam, beta))) / e
                ev = np.linalg.eigvals(J)
                kind = "saddle" if (ev.real > 1e-6).any() and (ev.real < -1e-6).any() else (
                    "attractor" if (ev.real < 1e-6).all() else "repeller")
                at_eq = 0.1 < p[2] < 0.9 and (1 - p[0] ** 2 - p[1] ** 2 - p[2]) > 0.1
                out.append({"lambda": lam, "beta": beta, "x": p[0], "y": p[1], "Omega_r": p[2],
                            "Omega_m": round(1 - p[0] ** 2 - p[1] ** 2 - p[2], 5), "kind": kind,
                            "eig": [round(float(v.real), 3) for v in ev], "saddle_at_equality": bool(at_eq and kind == "saddle")})
                print(out[-1])
    json.dump(out, open("LOCK_ATTRACTOR_PHASE.json", "w"), indent=1)
    print("any saddle at equality:", any(o["saddle_at_equality"] for o in out))


if __name__ == "__main__":
    {"check": check, "scan": scan, "phase": phase}[sys.argv[1]]()
