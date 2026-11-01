# Independent selection/coverage review of the other 23-point branches

Reviewer: Codex subagent t34_20_21_math, same-family/provisional. This review reads the mathematical selection and coverage arguments; it does not rerun the other workers' numerical tables or certify their Lean implementation.

Read in full:

- `../middle-math/CANDIDATE_FOUR_FIVE_LOW_23.md`;
- `../middle-math/CANDIDATE_ONE_TWO_LOW_23.md`;
- `../middle-math/CANDIDATE_LOW_BRANCHES.md`;
- `../high-math/CANDIDATE_THREE_LOW_23.md`;
- `../middle-math/ONE_LOW_23_RESIDUAL_GRAPHS.json`.

No gap found in the actual selection and universal graph arguments checked below.

For r=4/5 lows, external degree totals146/140 give at least13/11 vertices of degree7 or8. Any four lows have at most8 nonunit partners in total, so their fixed common-unit set U has at least5/3 members. The one-high residual conclusion can be applied to every four-low subset, since every such subset has a nonempty U. Thus every low-low pair is unit, including r=5: each pair extends to a four-low subset. All pair/triple restrictions then apply to the same fixed U. If every three members of U have exactly one seven and two eights, four selected members give3k=4 by counting seven-vertex appearances. The unique seven-lock residual has exactly34 edges and the stated degree vector:6 low-low pairs,12 low-high pairs,4 high-high pair copies,3 high singleton copies,9 empty copies. Adding the fifth low uses only its actual total excess2 and the already-established low-low unit codegrees; it does not silently assume unit high codegrees.

For r=1/2, t+2r>=14 and removal of at most2r exceptional high neighbors give |U|>=14-4r, hence10/6. The strong-codegree argument concerns only the selected seven-degree vertices and still applies in the presence of lows. The three seven-degree points needed for the maximum-codegree4 table exist. The complete extension domains start without a high-high unit assumption, and the global graph restriction is deduced from all five-high residuals.

The r=1 graph contradiction is valid. Since every five-set is one of2K2+K1, K3+2K1, K3+K2, every induced P3 extends to a forbidden five-set. P3-free connected components are cliques by the shortest-path argument. Every K4 extends to a forbidden five-set, so every clique has size at most3. If four components exist, four representatives plus any distinct fifth vertex induce at least four components. This too is forbidden. Thus |U|<=9, contradicting |U|>=10. The argument requires no assertion about where a fifth vertex lies beyond being distinct; edges across full components cannot appear.

For r=3, the external twenty vertices have degree total152, giving at least14 degree7/8 vertices and at least8 sevens. Removing at most6 nonunit partners leaves |U|>=8 and at least2 sevens. Four distinct members can therefore be chosen containing two sevens. Sorting their degrees ensures the first three contain at least two sevens, so the restricted three-to-four-high extension does cover the actual choice. High-high codegree<=2 is established by the full two-high residual classification before being used as a cap.

For r>=6, the six-low residual has all low-low codegrees1, and the stated type counts sum to34 with all six degrees6. At r=6 the seventeen external vertices have degree total134; at least10 have degree7 or8. The six lows have total external excess12, so one of those at least10 vertices consumes at most1 unit. Its explicit mixed extension is justified. At r>=7 the seven-low promotion/projection exclusion must remain a proved complete local classification in formalization; it is not replaced by rechecking stored examples.

The remaining common obligation is unchanged: formally connect actual trace multiplicities and every complete promotion/projection inventory to the saved exact certificates. The independently checked arithmetic reported in these drafts does not by itself discharge that Lean coverage obligation.
