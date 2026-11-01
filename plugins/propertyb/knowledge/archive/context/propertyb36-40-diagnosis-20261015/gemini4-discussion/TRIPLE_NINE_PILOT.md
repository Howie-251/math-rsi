# Three degree-nine locks: bounded exact pilot

2026-10-15. This is the parent's independent proposal, not Gemini's contribution. No Lean, whole-hypergraph search, or Goal change.

## Actual selection and type formulas

For an 18-vertex, 35-edge five-uniform hypergraph of minimum degree nine, let r be the number of degree-nine vertices. All others have degree at least ten, so 175>=9r+10(18-r)=180-r, hence r>=5. If every pair of degree-nine vertices must have codegree two in the residual double-lock branch, any three distinct degree-nine vertices are eligible locks.

Let tau be their common triple multiplicity. Since all pair codegrees are two, tau belongs to {0,1,2}. The exact trace counts by lock bitmask are

| Mask | Multiplicity |
|---|---:|
| 7 | tau |
| 3,5,6, each | 2-tau |
| 1,2,4, each | 5+tau |
| 0 | 14-tau |

Inclusion-exclusion proves these identities: a pure singleton has 9-2-2+tau edges, and the union of the three links has 27-6+tau=21+tau edges. The script asserts total edge count 35, all three degrees nine, and all three pair codegrees two. The reduction to pair codegree two uses the parent's existing full double-lock table; this pilot did not re-audit that table.

## The twelve tested layouts

Positions are one-based:

```
(1,2,3), (1,2,9), (1,9,10), (1,9,18),
(1,10,18), (2,9,17), (7,8,9), (8,9,10),
(9,10,11), (7,9,11), (8,10,12), (1,2,18).
```

These are twelve fixed layouts per type, **not all-position search**. The existing Profile, nested total/pure certificate, rows, and total_bound API was reused. All three types were evaluated at all twelve layouts, and each saved best layout was independently replayed through independent_structure_bounds.independent_rows for its A/B/C endpoint and pair formulas. The total/pure quota proof itself was reused, not independently reproved.

| tau | Best tested bound | Saved layout | Total link quota per lock | Pure quota per lock |
|---:|---:|---|---:|---:|
| 0 | 40/39 | (1,9,10) | 7 | 2 |
| 1 | 40/39 | (1,9,10) | 7 | 3 |
| 2 | 101/99 | (1,9,10) | 7 | 5 |

None is strict below one. This small pilot therefore supplies no triple-lock closure. It does not show all other layouts fail, that stronger shared deductions fail, or that any corresponding hypergraph is non-colourable. For tau=2, layout (1,2,18) yields 40/39, showing the retained 101/99 is a genuine improvement within the tested list.

The complete 36-layout arithmetic, saved best rows/certificates, and independent-replay flags are in TRIPLE_NINE_PILOT.json; reproduction is `python3 context/propertyb36-40-diagnosis-20261015/gemini4-discussion/triple_nine_pilot.py`. The measured formula-evaluation plus replay time was approximately 0.067 seconds. No further search was necessary for this bounded task.

## Addendum: complete local position domain

On the parent's subsequent request, the measured small cost justified scanning every increasing position triple, namely all binom(18,3)=816 layouts for each of the same three trace types (2448 evaluations total). This is only a finite local-formula domain, not a hypergraph search. Because each trace profile is invariant under permuting the three lock labels, increasing positions cover every assignment up to this exact symmetry.

The complete scan took 3.302 seconds and produced:

| tau | Minimum over all 816 increasing layouts | Saved first minimizer |
|---:|---:|---|
| 0 | 40/39 | (1,2,10) |
| 1 | 40/39 | (1,2,10) |
| 2 | 101/99 | (1,9,10) |

Independent A/B/C replay passed on all three saved minima. Hence changing positions alone cannot close any of these three types under the tested total/pure quota estimate; a stronger deduction, another lock, or another method is needed. This is a precise failure boundary for this formula, not a counterexample to the original colouring statement.

The original twelve-layout script and JSON remain unchanged. Full-domain evidence is separately retained in TRIPLE_NINE_ALL_POSITIONS.json, including every tested position and bound, saved best rows/certificates, and replay flags. Reproduce with `python3 context/propertyb36-40-diagnosis-20261015/gemini4-discussion/triple_nine_all_positions.py`.
