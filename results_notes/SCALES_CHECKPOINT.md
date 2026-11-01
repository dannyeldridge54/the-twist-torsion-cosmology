# Scales levelling: the checkpoint run at every major intersection

**Asked for by Danny on 1 November 2026:** "a scales leveling part of the schedule that does the online local checks 3
time at every major intersection; make sure your house is kept well."

## What counts as a major intersection

1. A pre-registered result lands: the Late Twist rerun, robustness batch 1, robustness batch 2, or any future test.
2. Before the paper is rebuilt for release, or before the arXiv or Zenodo bundle is staged.
3. When a new pre-registration is written.

## The checkpoint (both pans of the scale)

**Local pan (the house), up to 3 passes:**
1. Run `python house_check.py`. It covers:
   - hashes, including the older ones kept under other names;
   - key numbers recomputed from the result files;
   - run health;
   - result files tracked in git;
   - the paper PDF built after its source, with no "??", "[pending]" or "running" left;
   - main write-ups committed.
2. Fix every FAIL line (commit, rebuild, record), then run it again.
3. **Level means HITS: 0.** If pass 3 still has hits, stop and report them to Danny instead of forcing them.

**Online pan, a deep dive until a round has no new hits (added 1 Nov 2026 at Danny's request: "add deep dive to
scales check"):**
1. Each round, search for anything new since the last checkpoint that bears on the result just landed:
   - new papers on the same model or data;
   - new data releases (DESI, ACT, SPT, Simons Observatory, SH0ES, CCHP);
   - verification of any citation added since the last checkpoint.
2. **Each round follows up on the previous round's leads.** Read the abstract or primary source of anything
   claim-relevant; do not rely on search snippets.
3. **A hit is something that would change a claim, a number or a required citation.** Papers that are only interesting
   go into DEEP_DIVE_HINTS_*.md, not the paper.
4. **Stop only after a round with no new hits** (normally 3–5 rounds; at most 6, then report what is still open).
5. Log every round in the hints file as a table (round, found, use), plus the citations to add.

**Then:** commit, and send Danny a short line with local hits fixed, online hits found, and level or not.

## Rules that do not bend

- Nothing is published.
- No pre-registration or rule is edited.
- Corrections go in the deviation log.
- Every new citation is checked against arXiv, the journal page or the CubeMind library before it goes in.

## Record

| Date | Intersection | Local passes → hits | Online rounds → hits | Level? |
|---|---|---|---|---|
| 2026-11-01 ~08:00 | Review after the Late Twist stall | 3 → 4, 0, 0 | 5 → prior art (fixed onset, torsion + DESI), H₀ range, then none | Yes |
| 2026-11-01 08:08 | Coupled Twist pre-registered | 1 → 0 | 3 → φMDE convention (checked: 2β²/3 holds in ours, V4 sign wording fixed), β bounds confirmed, torsion DM portal and γ bounds (no effect), then none | Yes |
| 2026-11-01 08:13 | Re-check ("Again") | 2 → 2, 0, 0 (new header-time check found hand-typed times: 2 log headers, Late Twist results, 2 notes; all corrected) | 1 → none (Pollari sole author confirmed; SPT-3G f < 0.070 matches the published version we cite) | Yes |

## Bouncing back and forth with the CubeMind council (asked for on 1 November 2026)

**The aim:** our checkpoint and the council check each other, in turns, until they agree or we run out of bounces.
The council uses the **"Scales"** preset on its 13-point dial (`agent/settings.py`), which Danny applies from the Dial
tab with the helm on.

**At each intersection:**

1. **Our side (bounce 1).** Run the checkpoint above: house check until 0 hits, then online rounds. Write a one-page
   brief: the result, the verdicts by rule, what the pans found, and our confidence.
2. **Council side (bounce 2).** The council reviews that brief under Scales:
   - 3 rounds;
   - Advocate, strict Skeptic and 3 Rivals;
   - 3 independent sources;
   - null mirror ×3, subtle known mirror, swapped-model repeat mirror;
   - the mind check blocking.

   Its verdict, its mirror results (in `data/mirror_runs.jsonl`) and every objection are saved.
3. **Compare.**
   - **AGREE:** same verdict per rule, and no objection we cannot answer from the files. We are level; record it.
   - **DISAGREE**, or an open objection: our side checks that specific point (bounce 3: recompute, re-search, or
     re-read the file). The council then re-reviews with our answer (bounce 4).
4. **Stop rules:**
   - Stop at agreement, or after **3 full back-and-forths**, whichever comes first.
   - Anything still disputed goes to Danny as "open: ours says X, council says Y, because …". Neither side overrides
     the other.
   - If a council mirror fails (the null mirror finds an effect, the known mirror misses one, or the repeat
     disagrees), the council's verdict is set aside as unreliable for that intersection. It is recorded, not argued.

**What never bounces:**
- the pre-registered rules and verdict bands;
- the deviation log (append-only);
- publication, which is Danny's.

The council can raise a concern, but it cannot change a verdict that a rule decided.

**When it starts:** only after Danny restarts CubeMind (it stays stopped until the current fits finish) and applies
the Scales preset. Until then, bounce 1 runs alone, as now.| 2026-11-01 08:42 | Coupled Twist built, gates passed, loops set | 3 → 1, 1, 1 (uncommitted ranking file; passes run without fixing in between, then fixed) → 0, 0 | 2 → synchronous-gauge δ_m for coupled CDM (checked: CLASS's gauge-invariant transform plus the added θ_cdm already handles it), then none (CDM-only coupling standard; adiabatic instability noted to watch) | Mirrors: null = V1 (β = 0 gives an identical χ²), known = V3 (planted φMDE found), repeat = V2/V4 in two configurations (identical). Council off (CubeMind stopped). Level: yes |
| 2026-11-01 08:53 | Late Twist rerun landed; Zahn pages logged | 2 → 1 (ranking file uncommitted), 0 | 2 → Zahn identified (Oculus Artificialis structure confirmed); Panscopium source still open | Mirrors: corner probe = known-point mirror (the fit is 2.5+ above a point needing no fit), so the fit is flagged stuck. Council off. Level: yes |
| 2026-11-01 08:57 | Deep review (b) | 4 → 1, 1, 0, 0 | 2 → DESI DR2 numbers confirmed (we match −10.7 and −21.0 within 0.33); thawing-axion benchmark | Known-answer mirror passed (DESI reproduced); corner-probe mirror flags the stalled Late Twist. Council off. Level: yes |
| 2026-11-01 09:03 | (F, m) grid approved, logged, launched | 2 → 0, 0 | none needed: the grid range was set from the literature benchmark (F ≈ 0.6, m ≈ 1.75 H₀) in the previous round | Mirrors: the free fits stay on record beside the grid (a repeat comparison once the grid lands). Council off. Level: yes |
| 2026-11-01 09:05 | Quick review (grid running, 0 points done) | 1 → 0 | 1 → fixed-grid profiling confirmed as standard (Procoli, Herold et al.); adopt: report the restart spread per grid point when judging | All 7 fits healthy, no log errors. Council off. Level: yes |
| 2026-11-01 09:16 | Lock-attractor study: NO LOCK | 1 → 0 | 1 → chameleon EDE (Karwal et al. 2021) is a different potential, recorded as scope, not a contradiction | Mirrors: energy conservation 1e-12 (known-answer); the m_eff = H estimate agrees within 25%; the φMDE point matches gate V3 (repeat across two codes). Council off. Level: yes |
| 2026-11-01 09:53 | Star fractal 1D–6D done; R2 A3 with DES Y5 landed (D −4.70: SURVIVES, so A3 is fragile across SN sets) | 2 → 3 (new result JSONs), 0 | none needed (no new claims for the paper; the star study is the history track) | Mirrors: Poisson reference 3.0 ± 0.3; the rv subsample matches the full sample within 0.07. Council off. Level: yes |
| 2026-11-01 09:55 | Plan review; ROUTE.md revised | 1 → 0 | 1 → DES Y5 has a known 0.04 mag calibration offset (Efstathiou), corrected in DES-Dovekie, so the A3 'SURVIVES' with DES Y5 needs a Dovekie bracket (added as B1). Claim-relevant: noted, no rule changed | Grid non-viability matches the physics: m²F² ≤ 1.0 fails, ≥ 1.45 works. Council off. Level: yes |
| 2026-11-01 10:00 | Dovekie bracket pre-registered (09:56:48) and launched | 1 → 0 | covered by the previous round (Efstathiou offset; Dovekie correction) | Smoke test: Dovekie loads and existing runs are unchanged. Council off. Level: yes |
| 2026-11-01 10:04 | Checks and updates: thesis and phone brought up to date; garbled text found and repaired | 6 → 3 (garble, list rule), 3 (more garble), 2 (uncommitted), 0, 0 | none needed (no new claims) | New house-check rule: a UTF-8 byte-pattern scan for garbled text. Cause: PowerShell Get-Content without -Encoding UTF8 when rewriting files; that route is no longer used. Council off. Level: yes |
| 2026-11-01 10:07 | Grid speed-up (helper worker with atomic claims) | 1 → 0 | none needed (scheduling only) | Claim test: a duplicate attempt exits in 0.06 s. No rule or setting changed. Council off. Level: yes |
| 2026-11-01 11:57 | DV + B1: Dovekie MILD (D −2.70); R1 STABLE (D −3.96); A3 fragile by the filter rule | 2 → 2 (new JSONs), 0, 0 | 1 → DES's own Dovekie+CMB+DESI result (w0 −0.803 ± 0.054, wa −0.72 ± 0.21) matches our late-only fit (−0.824, −0.643): a validation, not a correction | Mirrors: restart spreads of 2.6–2.8 noted in both early+late fits. Council off. Level: yes |
| 2026-11-01 12:16 | Review (grid mid-way) | 2 → 1 (new grid JSON), 0, 0 | none needed (no new claims) | Both workers running 8 fits, no duplicate points (claims working). Council off. Level: yes |
| 2026-11-01 12:42 | Gaps closed: edge scan locked (12:34:01, 0 DES Y5 results at lock); null mirror run; trial-count scoreboard queued for the paper | 2 → 0, 0 | none needed (internal checks) | **Null mirror found a +1.35 offset** in the Late Twist code's Λ limit; recorded, verdicts as written stand. Council off. Level: yes |
| 2026-11-01 13:07 | Null-mirror cause found (halofit reads an Ω_m inflated by the field; frozen offset +0.03 without halofit); paper scoreboard drafted; 4 grid points committed (Pantheon+ best +0.96 at gF0.5m-0.3) | 4 → 0, 0 | none needed (source reading plus a local test) | Verdicts as written unchanged. CLASS's derived Ω_m and S8 are invalid for scf runs (use the true Ω_m). Council off. Level: yes |
| 2026-11-01 13:20 | Deep-dive review on request: grid ahead of the timetable (Pantheon+ 12 of 24 fits plus the non-viable points; DES Y5 at 4); edge runner alive and waiting for slots | 3 → 0, 0 | 2 rounds: thawing literature agrees (Pantheon+ mild, DES Y5 strongest); new prior art arXiv:2609.03062 (interacting thawing, −10.0 vs −3.9) logged in COUPLED_TWIST_NOTES; no claim-changing hit | **Preliminary:** DES Y5 Late Twist best −5.32 vs ΛCDM as written (4 of 24 points). Council off. Level: yes |
| 2026-11-01 13:26 | Gaps closed: LD (Late Twist on DES-Dovekie) and LEE-G (grid look-elsewhere) pre-registered and locked 13:25:13 (DES Y5 grid at 4 of 24, 0 LD results); runner queued after the edge scan; ranking wired (Dovekie runs kept out of the grid) | 0 | none needed | LEE-G now: DES Y5 Z_loc 1.81σ, Z_glob 1.81σ (N_eff 1 so far), WEAK HINT, preliminary. Council off. Level: yes |
| 2026-11-01 13:30 | Web deep dive (5 angles plus follow-ups) | 0 | Prior art arXiv:2608.09487 (dynamical BI field plus quintessence, GW friction) to cite; the literature-preferred axion corner (sub-Planckian F, large m) is outside our grid (H2, user decision); LD expectation recorded before results (likely WEAKENED or NOT CONFIRMED); B0/B4 design notes | No claim change. Council off. Level: yes |
| 2026-11-01 13:32 | HC (high-mass corner, 9 Pantheon+ points) pre-registered and locked 13:31:40 with 0 results; runner queued after LD; ranking keeps HC out of the grid, edge and LEE-G (tested); hourly loop updated | 0 | none needed | Queue tonight: grid, edge, LD, HC, then Coupled Twist. Council off. Level: yes |
| 2026-11-01 14:20 | **The Twist published on GitHub** (dannyeldridge54/the-twist-torsion-cosmology, public, pushed by the user's sign-in); CubeMind packaged separately (local only, licence draft); arXiv and Zenodo v3 bundles rebuilt and staged, NOT submitted (arXiv tar compiles standalone, 24 pages) | 2 → 0 | none needed | Results still pending in the public README by design. Council off. Level: yes |
| 2026-11-01 14:58 | B0 done early: two code bugs (forced delta_m for n_axion = 1; halofit/HMcode Omega_m) fixed in a separate build; first fix FAILED its pre-written rule, the second PASSED (+0.13); deviations 14:34:07 and 14:41:32. Outreach drafted and ON HOLD per Danny; TODO.md lists it all | 0 | none needed (source and local tests) | Running fits untouched (installed AxiCLASS); verdicts as written. Council off. Level: yes, steering straight |
| 2026-11-01 15:02 | Book kit made (BOOK_BRIEF.md, BOOK_SOURCES.md with 1,040 PC paths); outreach parked on TODO.md; back on task | 1 → 0, 0 (garble came from fix_mojibake's own docstring example; inventory now skips it) | none needed | Fits: Pantheon+ grid 14 fits, DES Y5 9; edge scan running (DES Y5 first); LEE-G DES Y5 Z_glob 1.29σ, WEAK HINT. Council off. Level: yes, steering straight |
| 2026-11-01 15:05 | Review on request (local + web) | 0, 0 | 3 rounds: NEW prior art Babu & Amendola arXiv:2610.23497 (coupled cosine thawing, abs(beta) < 0.073; C5 = 0.816 about 11x above), logged; birefringence numbers updated for B4; Dovekie literature agrees with H3; the bug is not publicly known | No claim changes. Early results checked as unaffected by the B0 bugs (n = 3). Council off. Level: yes, on track |
| 2026-11-01 15:08 | Dive to exhaustion (5 web rounds) | 0, 0 | Round 5 had no new claim-relevant hits. Found: independent profile agreement (Poulin 2505.08051), T3 coupling-choice caveat, B4 novelty limited to the torsion-fixed coefficient, a citation list for the final update | No claim changes; on track. Council off. Level: yes |
