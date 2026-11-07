#!/usr/bin/env python3
"""Draw the exact final five-cut recipe; unshown source edges stay in place."""
import json
import math
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

CASE = Path(__file__).resolve().parents[1]
recipe = json.loads((CASE / "data/d10_d4_recipe.json").read_text())
cuts = recipe["cut_edges"]
assert len(cuts) == 5 and len({v for e in cuts for v in e}) == 10
assert recipe["source_n"] == 2566 and recipe["new_label"] == 2566
paper, ink, blue, red = "#fdfcf7", "#1a1a1a", "#1a4a8c", "#b8390e"
plt.rcParams.update({"font.family": "DejaVu Serif", "svg.fonttype": "none"})
fig, (left, right) = plt.subplots(1, 2, figsize=(13.6, 5.6),
                               gridspec_kw={"width_ratios": [1, 1.6]})
fig.patch.set_facecolor(paper)
fig.subplots_adjust(left=.05, right=.97, bottom=.18, top=.78, wspace=.23)
fig.text(.045, .94, "Five edge replacements add one vertex", fontsize=20,
         weight="bold", color=ink)
fig.text(.045, .87, "(10,4): 2,566 vertices  →  2,567 vertices", fontsize=13,
         color="#6b6b6b")
for ax in (left, right):
    ax.set_facecolor(paper)
    ax.axis("off")
left.set(xlim=(0, 4), ylim=(-.6, 4.8))
for i, (u, v) in enumerate(cuts):
    y = 4 - i
    left.plot([1, 3], [y, y], "--", color=red, linewidth=2)
    left.scatter([1, 3], [y, y], s=85, color=blue, zorder=3)
    left.text(.8, y, str(u), ha="right", va="center", fontsize=11, color=ink)
    left.text(3.2, y, str(v), ha="left", va="center", fontsize=11, color=ink)
left.set_title("Remove five disjoint source edges", fontsize=12, loc="left",
               color=ink, pad=12)
fig.text(.435, .48, "→", fontsize=31, color=red, ha="center")
right.set(xlim=(-3.4, 3.4), ylim=(-2.6, 2.6), aspect="equal")
ends = [v for edge in cuts for v in edge]
for i, v in enumerate(ends):
    angle = math.pi / 2 + i * 2 * math.pi / 10
    x, y = 2 * math.cos(angle), 2 * math.sin(angle)
    right.plot([0, x], [0, y], color=blue, linewidth=1.5, zorder=1)
    right.scatter([x], [y], s=85, color=blue, zorder=3)
    right.text(1.17*x, 1.17*y, str(v), ha="center", va="center",
               fontsize=10, color=ink)
right.scatter([0], [0], s=900, color=red, zorder=4)
right.text(0, 0, str(recipe["new_label"]), ha="center", va="center",
           color="white", fontsize=11, weight="bold", zorder=5)
right.set_title("Connect the new vertex to all ten endpoints", fontsize=12,
                loc="left", color=ink, pad=12)
fig.text(.045, .10, "Each old endpoint: degree 10 → 9 → 10.    New vertex: degree 10.",
         fontsize=11, color=ink)
fig.text(.045, .045, "Exact endpoint labels; other source edges omitted. The complete graph has 12,835 edges and diameter 4.",
         fontsize=9, color="#6b6b6b")
for extension in ("png", "svg"):
    fig.savefig(CASE / f"assets/construction_d10_d4.{extension}", dpi=180,
                facecolor=paper)
svg = CASE / "assets/construction_d10_d4.svg"
svg.write_text("\n".join(line.rstrip() for line in svg.read_text().splitlines()) + "\n")
plt.close(fig)
print("Wrote the exact five-cut construction figure.")
