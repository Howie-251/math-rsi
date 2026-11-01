# C.2 two-point chart synchronization — 2026-10-21

Added the existing C.2 exact evaluations at k=12 and k=13 as purple diamonds, separate from the uniform theorem's blue curve and the red individual results. Both purple points read the left linear axis and share the same reference envelope L_ref. Points retain their true k coordinates; leader labels alone move.

| k | Reference | Uniform lower bound (gain) | C.2 accepted budget | C.2 lower bound (gain) | Lock candidate |
|---:|---:|---:|---:|---:|---:|
|12|4633|4635 (2)|4646|4647 (14)|4661 (28)|
|13|9539|9542 (3)|9563|9564 (25)|No complete improvement over C.2|

The script reads numeric_bridge.json and INDEPENDENT_NUMERIC_CHECK.json without modifying them. It asserts strict acceptance (upper log gap < 0), saved independent acceptance PASS, next-budget rejection PASS, and agreement with the unchanged uniform reference data. Derived data: plot_c2_data.json. Parent also saved a fresh deterministic two-point replay in C2_12_13_READBACK.json; this chart task did not modify it.

Ran `.tools/math-python/bin/python figures/propertyb_bounds/plot_bounds.py` successfully. Updated delta/small/overview SVG, PNG and PDF, plus the three-page propertyb_bounds.pdf; gain exports regenerate from the same unchanged uniform values. Inspected actual delta.png and small.png with view_image after layout adjustments: both purple values and red k12 lock label are visible, C.2 k13 label stays inside the canvas, legends separate left-axis numerical points from the right-axis Lean theorem, and blue uniform values remain unchanged. Minor tick 13 identifies the new actual k=13 coordinate. Labels are English throughout the figures.

RESULTS_FIGURE.md now puts m(13)≥9564 and both C.2 values in a first-screen summary card, explains all three result types, and includes the non-collapsed k12/13 comparison table immediately below the main figure. C.2 is a numeric application of the paper's sufficient criterion, not a literature baseline or a claim of Lean verification for those evaluations. The k12 lock candidate remains stronger than C.2. No new mathematics, search, model review, Lean run, Goal, wiki or v2 operation was performed here.
