"""Welling's planetary star as K7 on a torus (history and art track; not physics evidence).

Panel 1: the 7 planets in Chaldean order on a circle, joined by the heptagon, {7/2} and {7/3} stars.
Panel 2: the same 21 links laid flat on the torus (triangular lattice, label = a + 3b mod 7).
Panel 3: the flat sheet rolled up into a torus.
Letters follow the Golden Dawn attribution used in build_letters_datasheet.py; other versions differ.
"""
import itertools
import numpy as np
import matplotlib.pyplot as plt

PLANETS = ["Saturn", "Jupiter", "Mars", "Sun", "Venus", "Mercury", "Moon"]  # Chaldean order
SYMS = ["♄", "♃", "♂", "☉", "♀", "☿", "☽"]
LETTER = {"Saturn": "ת Tav", "Jupiter": "כ Kaf", "Mars": "פ Pe", "Sun": "ר Resh",
          "Venus": "ד Dalet", "Mercury": "ב Bet", "Moon": "ג Gimel"}
STEP_COL = {1: "#4c72b0", 2: "#dd8452", 3: "#55a868"}  # heptagon, {7/2}, {7/3}


def step(i, j):
    d = (j - i) % 7
    return min(d, 7 - d)


# ---- panel 1: the star on a circle
ang = np.pi / 2 - 2 * np.pi * np.arange(7) / 7
P = np.c_[np.cos(ang), np.sin(ang)]
edges = list(itertools.combinations(range(7), 2))
assert len(edges) == 21

fig = plt.figure(figsize=(18, 6.4))
ax1 = fig.add_subplot(131)
for i, j in edges:
    ax1.plot(*P[[i, j]].T, color=STEP_COL[step(i, j)], lw=1.8, alpha=0.85)
for k in range(7):
    ax1.scatter(*P[k], s=700, c="white", edgecolors="k", zorder=3)
    ax1.text(*P[k], SYMS[k], ha="center", va="center", fontsize=16, zorder=4)
    ax1.text(*(1.22 * P[k]), f"{PLANETS[k]}\n{LETTER[PLANETS[k]]}", ha="center", va="center", fontsize=9)
ax1.set_title("1. Welling's 7 planets: heptagon + {7/2} + {7/3}\n= all 21 links (complete graph K7)", fontsize=11)
ax1.set_aspect("equal"); ax1.axis("off"); ax1.set_xlim(-1.5, 1.5); ax1.set_ylim(-1.5, 1.5)
for s, lab in [(1, "heptagon (neighbours)"), (2, "{7/2} star"), (3, "{7/3} star = days of the week")]:
    ax1.plot([], [], color=STEP_COL[s], lw=2, label=lab)
ax1.legend(loc="upper center", bbox_to_anchor=(0.5, 0.0), fontsize=8, ncol=3, frameon=False)

# ---- panel 2: flat torus. Lattice point (a, b) carries planet (a + 3b) mod 7.
E1, E2 = np.array([1.0, 0.0]), np.array([0.5, np.sqrt(3) / 2])
NB = [(1, 0), (0, 1), (-1, 1)]  # label steps 1, 3, 2: every nonzero residue, so K7
lab = lambda a, b: (a + 3 * b) % 7
xy = lambda a, b: a * E1 + b * E2
V1, V2 = np.array([1, 2]), np.array([-3, 1])  # period lattice (label 0), det = 7
assert lab(*V1) == 0 and lab(*V2) == 0 and abs(V1[0] * V2[1] - V1[1] * V2[0]) == 7

ax2 = fig.add_subplot(132)
seen = set()
for a in range(-5, 6):
    for b in range(-1, 5):
        for da, db in NB:
            p, q = xy(a, b), xy(a + da, b + db)
            i, j = lab(a, b), lab(a + da, b + db)
            seen.add(frozenset((i, j)))
            ax2.plot([p[0], q[0]], [p[1], q[1]], color=STEP_COL[step(i, j)], lw=1.2, alpha=0.55)
assert len(seen) == 21, len(seen)
corner = xy(0, 0)
cell = np.array([corner, corner + xy(*V1), corner + xy(*V1) + xy(*V2), corner + xy(*V2), corner])
ax2.fill(cell[:, 0], cell[:, 1], color="#f2e6c9", alpha=0.6, zorder=0)
ax2.plot(cell[:, 0], cell[:, 1], "k--", lw=1.2, label="one torus (opposite sides glued)")
for a in range(-5, 6):
    for b in range(-1, 5):
        p = xy(a, b)
        if not (-3.4 < p[0] < 3.0):
            continue
        ax2.text(*p, SYMS[lab(a, b)], ha="center", va="center", fontsize=12,
                 bbox=dict(boxstyle="circle,pad=0.15", fc="white", ec="0.4", lw=0.6))
ax2.set_title("2. The same 21 links on a flat torus:\nevery planet touches all 6 others, no crossings", fontsize=11)
ax2.set_aspect("equal"); ax2.axis("off"); ax2.set_xlim(-3.6, 3.2); ax2.set_ylim(-0.9, 3.9)
ax2.legend(loc="lower center", bbox_to_anchor=(0.5, -0.12), fontsize=8, frameon=False)

# ---- panel 3: roll the sheet into a torus. Coordinates (s, t) in the V1, V2 basis.
M = np.linalg.inv(np.c_[xy(*V1), xy(*V2)])
R, r = 2.0, 0.8


def torus(pt):
    s, t = M @ pt
    u, v = 2 * np.pi * s, 2 * np.pi * t
    return np.array([(R + r * np.cos(v)) * np.cos(u), (R + r * np.cos(v)) * np.sin(u), r * np.sin(v)])


ax3 = fig.add_subplot(133, projection="3d")
uu, vv = np.meshgrid(np.linspace(0, 2 * np.pi, 60), np.linspace(0, 2 * np.pi, 30))
ax3.plot_surface((R + r * np.cos(vv)) * np.cos(uu), (R + r * np.cos(vv)) * np.sin(uu), r * np.sin(vv),
                 color="#f2e6c9", alpha=0.25, linewidth=0)
reps = {}
for a in range(-6, 7):
    for b in range(-3, 6):
        s, t = M @ xy(a, b)
        if 0 <= s < 1 - 1e-9 and 0 <= t < 1 - 1e-9:
            reps[lab(a, b)] = (a, b)
assert len(reps) == 7
for k, (a, b) in reps.items():
    for da, db in NB:
        line = np.array([torus(xy(a, b) + f * xy(da, db)) for f in np.linspace(0, 1, 40)])
        ax3.plot(*line.T, color=STEP_COL[step(k, lab(a + da, b + db))], lw=2)
    p = torus(xy(a, b))
    ax3.scatter(*p, s=120, c="white", edgecolors="k", depthshade=False)
    ax3.text(*(p * 1.12), f"{PLANETS[k]} / {LETTER[PLANETS[k]].split()[1]}", fontsize=8)
ax3.set_title("3. Rolled up: K7 drawn on the torus\n(7 doubles ↔ 7 planets, Golden Dawn attribution)", fontsize=11)
ax3.set_box_aspect((1, 1, 0.4)); ax3.axis("off"); ax3.view_init(elev=35, azim=30)

fig.suptitle("Welling (1719) planetary star = complete graph K7 = the 7-colour torus map. "
             "History and art track: exact geometry, not evidence for the physics.", fontsize=12)
fig.tight_layout(rect=[0, 0.06, 1, 0.92])
fig.savefig("welling_k7.png", dpi=150)
print("edges on flat torus:", len(seen), "| vertices rolled:", len(reps), "| saved welling_k7.png")
