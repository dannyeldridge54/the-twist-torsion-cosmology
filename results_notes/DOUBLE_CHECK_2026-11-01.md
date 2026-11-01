# Double check, 1 November 2026 (two audit passes)

**Tool:** `audit_all.py` (read-only), run twice, with the second pass looking for what the first missed.

## Pass 1: what was checked

| Check | Result |
|---|---|
| 11 hashed pre-registrations against their .sha256 | **All match** |
| 3 older SPT-3G pre-registrations (N = 9, Silver, Letters) | No hash files, but **one commit each, never edited**; N = 9 and Silver are also on Zenodo |
| Combined Locked Twist −5.63, w0–wa −10.89 (CAMB) | Recomputed −5.631, −10.889: **match** |
| A3: D −3.65, cross-checks −6.05 and −10.95 | Recomputed −3.653, −6.046, −10.948: **match** |
| A2 look-elsewhere (Z_local 2.38, Z_global 1.24 / 1.37) | Matches the calculator's JSON |
| A1 rise at f = 0, written as 5.98 | Recomputed **5.988 (rounds to 5.99)**; the free-fit gap is 0.357, not 0.35 |
| Paper "[pending]" placeholders | Defined but **never used** in the text; the PDF shows none |

**About the A1 rounding:** the automatic judge used the pre-registered reference χ², rounded to 0.01 (2402.40, 2396.77).
The 0.003 difference does not change the verdict (PREFERRED either way). It is disclosed in PROFILE_F_RESULTS.md rather
than changed, because the numbers match the locked references.

## Pass 1: fixed

- **Paper:**
  - "what is still running" heading → "Significance";
  - Late Twist "is running" → the stall and the rerun, stated;
  - MCMC "are running" → stopped, with ΛCDM converged (H₀ 68.29 ± 0.27) and the early chains not used;
  - agreement with Poulin et al. stated;
  - a new **limitations** paragraph: the weak gravity conjecture (F ≲ 0.008 M_Pl against our 0.145), the SH0ES result
    (Δχ² −30.2, recomputed −30.22), and the published two-role and lock mechanisms;
  - Barbero–Immirzi dark-energy prior art (Pollari 2023).

  Four new references, each checked against the CubeMind library or arXiv. The paper rebuilt with no undefined
  citations.
- **THESIS.md:** the Late Twist row and the P8 status updated; the stale "waiting on A2 and A3" removed.
- **PHONE_SUMMARY.md:** the MCMC row is no longer "running".

## Pass 2: what the first pass missed

1. **Robustness batch 1 had never started.** Its queue waited for the Late Twist result file, which had been archived
   for the approved rerun.
   - The queue was replaced by `run_robustness2.sh`: batch 1 started at 07:51 beside the rerun, and batch 2 follows
     both.
   - The restart is logged; no setting changed.
2. **The staged arXiv bundle (06:46) is out of date.** It lacks A3, the limitations and the fixes. It must be rebuilt
   before any submission.
3. **The same CAMB-vs-CLASS θ mismatch affected the A3 starting points.** The A3 fits agree with CAMB to within 0.42,
   so they did not stall badly. But a stall of about 0.5 could move A3 across its −4 line. The R1 best-of-4 runs (now
   running) are the check.

## State now

- **Running:**
  - the Late Twist rerun (best of 4, AxiCLASS ΛCDM start);
  - robustness batch 1 (5 fits).
- **Queued:** batch 2 (3 fits).
- **The hourly check** judges each when done. Nothing is published, and no rule was changed.

## Pass 3 ("double dive", about 07:55, commit c8c5b3d)

| Check | Result |
|---|---|
| Six running fits (Late Twist rerun + robustness batch 1) | All alive; load about 10 on 16 cores. The one Late Twist warning is the expected closure overflow, which the guard catches |
| auto_judge.py logic for A3 and the Late Twist | Matches the pre-registrations, including the halofit references |
| Old CAMB queue runner and auto-judge tab | Idle (0 CPU over 10 s); harmless |
| Built paper PDF (23 pages) | No "??", "[pending]", "running" leftovers or placeholders; every A3 table value and every new number (68.29, 30.2, 72.2, 0.126, 0.008, 0.145) present |
| Hourly job | Present, next run 08:33 |
| **Git: result files** | **Found and fixed: 51 result JSONs, including the A1, A2 and A3 inputs the paper cites, had never been committed.** Now tracked (AEGIS 651a0cc) |

**Left as is, on purpose:**
- `taurus_gaia.npz` (9 MB, regenerable from the Gaia store);
- runtime `.err` and runner logs;
- `AUTO_RESULTS.md` (rewritten every hour);
- `THEORY_AND_PROOF_DOSSIER.md` in AEGIS: a 255-byte pointer file from 30 October. It is left for you to decide:
  commit it or delete it.