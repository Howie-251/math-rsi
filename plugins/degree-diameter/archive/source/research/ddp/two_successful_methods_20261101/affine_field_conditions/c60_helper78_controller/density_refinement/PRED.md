# Authorized density refinement of the same fixed H18 case

The previous one-shot solve ended UNKNOWN after 59.218354853 tracked
worker CPU seconds. Its CNF, STARTED record, and UNKNOWN remain untouched.
This is the root-authorized necessary-constraint refinement, not a
continuation of the previous solver state. There is exactly one new solver
call, at most 27 CPU / 45 wall seconds; new preparation at most 2 CPU
seconds; combined scope including the old worker must stay below 90 CPU
seconds. No third timer or different helper count is authorized.

## Density prediction and proof before the new solve

A size-three class S_i in a K4 helper component must send an old edge to
each of the 14 helper classes outside its own component. Its total old
edge incidence is 3*5=15. An internal edge would consume two incidences,
leaving at most 13 for the 14 required classes, so S_i is independent.
The 14 distinct outside classes require 14 distinct old endpoints, hence
|N_G(S_i)|>=14. At most one incidence can reach the other classes of its
own K4 component. A separate paper review agreed with all these necessary
conclusions. No sufficiency claim is made.

The exact enumeration of all C(60,3)=34,220 source triples found:

* 8,120 rejected because they are not independent.
* 26,100 independent triples: neighbor union 12 for 460, union 13 for
  6,380, union 14 for 11,900, and union 15 for 7,360.
* Thus 6,840 independent triples fail union>=14 and 19,260 pass both
  necessary conditions. Enumeration used 0.020359557 CPU seconds.

All candidates and rejected independent triples are saved in
`TRIPLE_FILTER.json`. This concrete candidate set is the refinement
prediction; a declining count of bad pairs is not used as progress.

Use two explicit types of necessary clauses, only for the twelve
size-three helpers 6..17:

1. For every old edge uv, add not x[u,i] OR not x[v,i]. This adds 1,800
   binary clauses and enforces independence.
2. For each of the 6,840 independent triples with neighbor union below
   14, add the three negative color literals. Exact load three then
   excludes that entire class. This adds 82,080 ternary clauses.

The refined CNF preserves the old 145,047 clauses verbatim and appends
83,880 necessary clauses, for 228,927 clauses and the same 44,460
variables. The own-component incidence condition is proved above but is
not separately encoded. No additional matching or block constraints are
added. Source attribution remains Bhakar.

SAT still requires a literal 78-controller and independent enumeration
of all 78*216 walks covering all 6,084 ordered pairs. UNKNOWN leaves this
fixed H18 case open and ends all authorized continuation. UNSAT, if
obtained, applies only to the same fixed source/H18 case.
