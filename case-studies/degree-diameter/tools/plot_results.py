#!/usr/bin/env python3
"""Render the case-study comparison from the included, dated CSV."""
from pathlib import Path
import csv

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

CASE = Path(__file__).resolve().parents[1]
with (CASE / "data/chart_data.csv").open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))

plt.rcParams.update({
    "font.family": "DejaVu Serif", "font.size": 10,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.spines.left": False, "axes.edgecolor": "#d6d0c0",
    "axes.labelcolor": "#4a4a4a", "text.color": "#1a1a1a",
    "xtick.color": "#6b6b6b", "ytick.color": "#1a1a1a",
    "svg.fonttype": "none",
})
fig, (left, right) = plt.subplots(
    1, 2, figsize=(13.6, 6.2), gridspec_kw={"width_ratios": [1, 1.45]}
)
fig.patch.set_facecolor("#fdfcf7")
left.set_facecolor("#fdfcf7")
right.set_facecolor("#fdfcf7")
fig.subplots_adjust(left=.08, right=.93, bottom=.22, top=.70, wspace=.50)
fig.text(.045, .94, "Larger graphs under the same degree and diameter limits",
         fontsize=20, weight="bold")
fig.text(.045, .885, "Three main-table improvements and a seven-parameter D3 series",
         fontsize=12, color="#6b6b6b")

table_rows = [r for r in rows if r["diameter"] != "3"]
for i, r in enumerate(table_rows):
    gain = int(r["gain"])
    left.barh(i, gain, height=.42, color="#b8390e", zorder=3)
    left.text(gain + 1.4, i, f"+{gain:,}", va="center", fontsize=12,
              weight="bold", color="#b8390e")
    left.text(0, i - .32, f'{int(r["reference"]):,}  →  {int(r["ours"]):,}',
              fontsize=10, color="#6b6b6b")
left.set_yticks(range(3), [f'({r["degree"]}, {r["diameter"]})' for r in table_rows])
left.set_ylim(2.6, -.65)
left.set_xlim(0, 75)
left.set_xticks([0, 20, 40, 60])
left.set_xlabel("Additional vertices", labelpad=10)
left.set_title("A   Gains over Comellas table entries", loc="left", pad=25,
               fontsize=12, weight="bold")
left.grid(axis="x", color="#e8e3d5", zorder=0)
left.tick_params(axis="y", length=0, pad=9)

d3_rows = [r for r in rows if r["diameter"] == "3"]
for i, r in enumerate(d3_rows):
    ref, ours, gain = (int(r[k]) for k in ("reference", "ours", "gain"))
    right.barh(i + .15, ref, height=.26, color="#b5bdc9", zorder=3,
               label="Published-method reference" if i == 0 else None)
    right.barh(i - .15, ours, height=.26, color="#1a4a8c", zorder=3,
               label="Our construction" if i == 0 else None)
    right.text(ours + 95, i - .15, f"{ours:,}", va="center", fontsize=9,
               color="#1a4a8c", weight="bold")
    right.text(ref + 95, i + .15, f"{ref:,}", va="center", fontsize=8,
               color="#6b6b6b")
    right.text(1.015, i, f"+{gain:,}", transform=right.get_yaxis_transform(),
               va="center", fontsize=10, color="#b8390e", weight="bold")
right.set_yticks(range(7), [r["degree"] for r in d3_rows])
right.set_ylim(6.6, -.65)
right.set_xlim(0, 8900)
right.set_xticks([0, 2000, 4000, 6000, 8000])
right.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x):,}"))
right.set_xlabel("Vertices (axis starts at zero)", labelpad=10)
right.set_ylabel("Maximum degree", labelpad=11)
right.set_title("B   D3: comparison with public methods", loc="left", pad=25,
                fontsize=12, weight="bold")
right.text(1.015, 1.025, "GAIN", transform=right.transAxes, fontsize=8,
           color="#6b6b6b", weight="bold")
right.grid(axis="x", color="#e8e3d5", zorder=0)
right.tick_params(axis="y", length=0, pad=6)
right.legend(loc="upper left", bbox_to_anchor=(-.02, -.18), frameon=False,
             ncol=2, fontsize=9)

fig.text(.045, .075,
         "A: Comellas table, 3 November 2026.   B: published constructions and formula instances, 1 November 2026.",
         fontsize=9, color="#6b6b6b")
fig.text(.045, .038,
         "Each comparison uses the same maximum degree and diameter. Reference formulas and sources accompany the case study.",
         fontsize=9, color="#6b6b6b")
(CASE / "assets").mkdir(exist_ok=True)
fig.savefig(CASE / "assets/results.png", dpi=180, facecolor="#fdfcf7")
fig.savefig(CASE / "assets/results.svg", facecolor="#fdfcf7")
plt.close(fig)
print("Wrote assets/results.png and assets/results.svg")
