"""Stage the UFE / Twist v3 Zenodo package (DRAFT). Only our own work; no third-party data, no secrets, no private files.
    python build_zenodo_v3.py        -> zenodo/ufe_v3_upload_DRAFT/ (+ MANIFEST.txt with SHA-256 of every file)
Nothing is uploaded: publishing is Danny's decision, after the running fits finish."""
import glob
import hashlib
import os
import re
import shutil

CM = os.path.dirname(os.path.abspath(__file__))
AE = r"C:\Users\Danny\.copilot\repos\AEGIS"
OUT = os.path.join(CM, "zenodo", "ufe_v3_upload_DRAFT")

GROUPS = {
    "paper": [AE + r"\papers\torsion_born_ede.tex", AE + r"\papers\torsion_born_ede.pdf"]
             + glob.glob(AE + r"\papers\theory_note\spiral_twist_note*.*")
             + glob.glob(AE + r"\papers\theory_note\arxiv\spiral_twist_arxiv.*"),
    "preregistrations": glob.glob(CM + r"\PREREGISTRATION_*.md") + glob.glob(CM + r"\PREREGISTRATION_*.sha256"),
    "results_notes": [CM + "\\" + f for f in (
        "THESIS.md", "PHONE_SUMMARY.md", "ROUTE.md", "SCALES_CHECKPOINT.md", "MODEL_RANKING.md",
        "EARLY_LATE_RESULTS.md", "LATE_TWIST_RESULTS.md", "PROFILE_F_RESULTS.md", "LOOK_ELSEWHERE_RESULTS.md",
        "LOOK_ELSEWHERE_RESULTS.json", "COMBINED_CMB_RESULTS.md", "SPT3G_RESULTS.md", "COUPLED_TWIST_GATES.md",
        "COUPLED_TWIST_NOTES.md", "LOCK_ATTRACTOR_RESULTS.md", "LOCK_ATTRACTOR_RESULTS.json",
        "LOCK_ATTRACTOR_PHASE.json", "STEP2_RESULT.md", "STEP3B_RESULT.md", "DEEP_REVIEW_2026-11-01.md",
        "DEEP_REVIEW_2026-11-01b.md", "DEEP_DIVE_HINTS_2026-11-01.md", "DOUBLE_CHECK_2026-11-01.md",
        "ROBUSTNESS_RESULTS.md", "LATE_TWIST_NULL_MIRROR.md", "PAPER_SCOREBOARD_DRAFT.md",
        "COUPLED_TWIST_RESULTS.md", "T2_PHOTON_COUPLING_LOG.md", "B4_BIREFRINGENCE_RESULTS.md", "B4X_SWITCH_RESULTS.md",
        "RATIO_REPLICATION_RESULTS.md", "S8_FIXED_CODE_RESULTS.md", "ROBUSTNESS_II_RESULTS.md",
        "robustness2_score.json", "THEORY_T1_T3_STABILITY.md", "theory_checks.json", "DATA_CATALOG.md",
        "DATASET_BREAKDOWN.md", "DATASET_BREAKDOWN.json", "RESULTS_LEDGER_2026-11-02.md", "NEXT_MODELS_DESIGN.md",
        "next_model_feasibility.json", "NIEH_YAN_PERIOD.md", "nieh_yan_period.json", "NIEH_YAN_TWIST_DRAFT.md",
        "lu_tf_score.json", "b4x_ratio_test.json", "PATH_DECISION_2026-11-02.md", "LATE_UNION3_RESULTS.md",
        "SOLAR_GATE_RESULTS.md", "solar_gate.json", "LOWZ_SPLIT_RESULTS.md", "lowz_split.json", "lowz_context_ax_spa_w0wa_halofit_desy5.json",
        "bi_kahler_lambda.json", "tau_audit.json", "UFE_CHECKS_RESULTS.md", "ufe_er.json", "ufe_in.json",
        "ufe_lq.json", "SPIRAL_POTENTIAL_LOOP.md", "bi_superpotential.json", "SPIRAL_W_FEASIBILITY.md",
        "spiral_w_scan.json", "spiral_w_benchmark.json", "GROWTH_HZ_RESULTS.md", "growth_hz.json",
        "PREDICTIONS_LOCKED_2026-11-02.md", "forward_predictions.json", "MIRROR_MAP_SPIRAL.md",
        "spiral_class_mirror.json", "spiral_mirror_ramos.json", "spiral_matter_angle.json",
        "spiral_matter_angle_big.json", "spiral_mirror_scan.json", "PATH_REVIEW_FILTERED_2026-11-02.md",
        "QUANTUM_PATH_2026-11-02.md",
        "ratio_replication_test.json")],
    "fit_results": glob.glob(AE + r"\cmb-fit\results\cmp_*.json") + glob.glob(AE + r"\cmb-fit\results\cpl_*.json")
                   + glob.glob(AE + r"\cmb-fit\results\earlyF_*.json") + glob.glob(AE + r"\cmb-fit\results\weff_*.json")
                   + glob.glob(AE + r"\cmb-fit\results\null_mirror*.json")
                   + [AE + r"\cmb-fit\results\\" + f for f in (
                       "VERDICT_LOCK.json", "N_PACT_LOCK.json", "cross_engine_pact.json", "engine_check.json",
                       "validate.json", "width_edelockP.json", "width_edelockP_F9.json", "width_pact_edelock.json",
                       "width_spt_edelock.json", "b4_delta_theta.json", "b4x_switch.json",
                       "ratio_s3_switch_defs.json", "s8_fixed_code.json")],
    "environment": glob.glob(AE + r"\cmb-fit\environment\*.*"),
    "code": glob.glob(AE + r"\cmb-fit\axiclass\*.py") + glob.glob(AE + r"\cmb-fit\axiclass\*.sh")
            + glob.glob(AE + r"\cmb-fit\axiclass\coupled\*.py") + glob.glob(AE + r"\cmb-fit\axiclass\coupled\*.sh")
            + glob.glob(AE + r"\cmb-fit\axiclass\nlfix\*.*")
            + [AE + r"\cmb-fit\cmbfit_compare.py"]
            + [CM + "\\" + f for f in ("rank_models.py", "house_check.py", "audit_all.py", "fix_mojibake.py",
                                       "lock_attractor.py", "look_elsewhere.py", "auto_judge.py",
                                       "step2_potential.py", "step3b_trigger.py", "nr_verdicts.py",
                                       "b4_birefringence_numbers.py", "b4x_ratio_test.py",
                                       "ratio_replication_test.py", "paper_numbers_check.py",
                                       "robustness2_score.py", "theory_checks.py", "dataset_breakdown.py",
                                       "next_model_feasibility.py", "nieh_yan_period.py", "lu_tf_score.py",
                                       "bi_kahler_lambda.py", "solar_lowz.py", "lowz_split.py", "tau_audit.py",
                                       "ufe_checks.py", "bi_superpotential.py", "spiral_w.py", "growth_hz.py",
                                       "verify_sheets.py", "spiral_class_mirror.py", "forward_predictions.py",
                                       "pincer.py")]
            + [AE + r"\cmb-fit\axiclass\spiral_guess.py"]
            + [CM + r"\data\growth_hz_data.json"],
    "history_track": [CM + "\\" + f for f in (
        "OLD_SOURCES_LOG.md", "WELLING_K7.md", "welling_k7.py", "welling_k7.png", "STAR_FRACTAL_RESULTS.md",
        "STAR_FRACTAL_RESULTS.json", "star_fractal.py", "star_fractal.png", "aizawa_check.py", "aizawa_check.png",
        "ODYSSEY_LENSES.md", "GENESIS_SHAPES.md")],
    "licence": [AE + r"\LICENSE", AE + r"\PLEDGE.md", AE + r"\CITATION.cff"],
}

SECRET = re.compile(r"(?i)(api[_-]?key|secret|password|passwd|token|bearer\s+[a-z0-9]|ghp_[A-Za-z0-9]{20,}|"
                    r"sk-[A-Za-z0-9]{20,}|BEGIN (RSA|OPENSSH) PRIVATE KEY|login_token)")
BLOCK_NAMES = re.compile(r"(?i)(token|secret|credential|\.env|private|archive|megamillions|powerball)")


def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    rows, flagged, missing = [], [], []
    for grp, files in GROUPS.items():
        os.makedirs(os.path.join(OUT, grp), exist_ok=True)
        for f in sorted(set(files)):
            if not os.path.exists(f):
                missing.append(f); continue
            name = os.path.basename(f)
            if BLOCK_NAMES.search(name):
                flagged.append((f, "blocked file name")); continue
            data = open(f, "rb").read()
            if not name.endswith((".png", ".pdf")):
                txt = data.decode("utf-8", errors="ignore")
                for m in SECRET.finditer(txt):
                    line = txt[max(0, m.start() - 60): m.end() + 60].replace("\n", " ")
                    flagged.append((f, f"secret-like text: …{line}…"))
            dst = os.path.join(OUT, grp, name)
            shutil.copy2(f, dst)
            rows.append((grp + "/" + name, len(data), hashlib.sha256(data).hexdigest()))
    with open(os.path.join(OUT, "MANIFEST.txt"), "w", encoding="utf-8") as m:
        m.write("UFE / Twist v3 package (DRAFT, not published). SHA-256 of every file.\n\n")
        for p, n, h in rows:
            m.write(f"{h}  {n:>10}  {p}\n")
    total = sum(n for _, n, _ in rows)
    print(f"{len(rows)} files, {total / 1e6:.1f} MB staged in {OUT}")
    print(f"missing (listed but not found): {len(missing)}")
    for f in missing:
        print("  -", f)
    print(f"flagged for review: {len(flagged)}")
    for f, why in flagged:
        print("  !", os.path.basename(f), "-", why[:200])


if __name__ == "__main__":
    main()
