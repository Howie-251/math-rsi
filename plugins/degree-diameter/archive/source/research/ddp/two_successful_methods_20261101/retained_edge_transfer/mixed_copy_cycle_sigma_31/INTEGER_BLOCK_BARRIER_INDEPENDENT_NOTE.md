# Independent paper attack: integer block barrier for the fixed G0/K6 rule

2026-11-01. **The integer exclusion is supported.** The proposed eight-block argument is sound for the exact five omissions, copy cycles, saved sigma action, eligible pin pool, degree cap 31 and six-helper clique in this directory. Its necessary pin count is at least 160, while K6 leaves at most 156 helper-to-old pin attachments. This is a paper proof using inherited inputs and the producer's newly completed local relation bindings. It is not a reinterpretation of the solver's UNKNOWN, an independent rerun of those bindings, a Lean proof, an external review, a new graph, or a general exclusion at cap 31.

## Evidence read and what was not repeated

I read the root prediction, the actual local binding result/terminal and its small checker source, the existing fixed-rule parameters, the earlier route-interface note, and the existing LP/stratum/solver receipts. I did not open G0.edges, S8775.edges, G0_INPUT.npz, the old B adjacency/R2/Steiner data, or run any experiment, graph traversal, solver, BFS, field, geometry, Lean, or paid review.

`INTEG_BLOCK_LOCAL_BINDING_RESULT.json` reports all three newly required interfaces actually PASS: the eight saved-R2 groups and sigma pairs, the A-positive-two-support facts, and the current G0 pin-to-target envelopes. It binds all 1750 pool vertices to the 960 original targets A15 times the 64 nonzero B absolute columns. There are no envelope counterexamples. Its terminal reports 0.159323 CPU seconds, within the original batch's 120 CPU budget; cumulative original-batch usage is 96.064628 seconds. This review uses that completed input rather than repeating it.

The history remains separate:

* The only full MILP returned `UNKNOWN_NO_FEASIBLE_INTEGER_PINS_WITHIN_ONE_BUDGET`, with no incumbent and no reported bound/node count. Its wrapper CPU was 95.395974 seconds. That remains UNKNOWN.
* The explicit rational assignment x[h,u]=1/7 on the 120 selected U pins for each helper passes all full LP coverage and capacity rows. The first stronger prediction that every own B2 count was at least seven was false on 960 targets, where the actual own count was three. The full numerator there was 3+5*3=18, so the LP witness survived. The refined saved-data strata match.
* The following integer proof uses new block allocation information. An LP-feasible but integer-infeasible model is consistent with both earlier outcomes.

## 1. The route envelopes include all short paths

For any old target v, the previous paper interface establishes that helper h reaches v in at most three steps exactly when an own pin is in closed B2_G0(v), or another helper's pin is in closed B1_G0(v). A path h-u-g-v with an old intermediate pin u shortens to h-g-v because the helper graph is K6; paths with two subsequent helpers shorten similarly. Therefore no first-helper/mixed route is omitted by using these two old-graph envelopes. This reduction is specific to the complete helper graph.

Write N_a for the literal A-neighbor row of an absolute a, and P_x for the positive support of row x of A squared. For a representative pin based at (a,b), b nonzero absolute and b*=sigma(b), the generous envelopes to original targets A15 times nonzero B absolutes are:

| old suffix after the pin | target column b | target column b* | all other absolute columns |
| --- | --- | --- | --- |
| own helper, closed B2 | P_a | N_a | empty |
| another helper, closed B1 | N_a | {a} | empty |

The ordinary source route contributes only the same-column P_a/N_a terms: different B absolutes have no old relation path of length one or two. A copy-cycle edge changes only the representative index, so cannot introduce another B column. A sigma peer changes b only to b*. Two sigma steps return to b; a sigma step followed by a mandatory/cycle step contributes at most N_a/{a} in b*. This covers cycle-then-sigma as well as sigma-then-cycle, including the cases where the resulting representative is the original source center. The bounds deliberately allow favorable copy positions; using a superset of real reachability makes the exclusion conservative.

Each freed U pin (x,y), y in Y=N_B(0), has closed B2 reach exactly P_x times G_y and closed B1 reach empty in these 960 targets. Its source paths are in the old product relation; two-step paths via a clone of an omitted-column center return only to its original mandatory neighborhood and add no nonzero absolute target. The ten freed U points over column zero, and all twenty representatives over column zero, have no B1/B2 reach to these targets. These zero/exact/subset claims were all bound in the new current-G0 local test, rather than assumed from the old uniformly saturated model.

The eight sets G_y each contain eight absolute columns and four complete sigma transpositions. Thus every useful F pin attachment belongs to exactly one of these eight blocks. Every useful U pin also belongs to exactly one block. Sigma never moves it to another block. The other thirty pool vertices contribute no repair to this target subset. This is why attachments cannot be reused across blocks in the lower bound.

## 2. The small A facts used in the owner cases

The new literal binding gives |P_x|=7 for all fifteen x, |P_x union P_z|=11 for all 105 distinct pairs, and P_a intersect O_A={a} for each of the five absolutes. Hence the union of at most two U supports has at most eleven targets.

For distinct x,z let D be the four points outside P_x union P_z. The bound

    |D intersect (N_a union {c})| <= 3

for absolutes a,c is also actually bound in all 2625 cases. There is a short explanation from the inherited A^3=4A+J: its positive (a,x) entry implies N_a intersects P_x. Thus at most two of the three N_a points can lie outside P_x union P_z; adjoining {c} contributes at most one more. This uses the inherited A-cube fact without rerunning it. Finally N_a is contained in P_a, because a has an absolute loop, and N_a meets O_A only in a. Both are visible in the fixed literal rows; no statement is being made for arbitrary isomorphic-looking factors without an input binding.

## 3. One sigma pair: the integer owner cases

Fix a block y and one of its four pairs {b,b*}. Let f be the total number of actual helper-to-F **attachments** in these two columns. Repeated based classes, repeated representative types and sharing one endpoint among different helpers all count with attachment multiplicity, since each spends one helper degree. An owner is a helper with at least one such attachment. Let u_h be helper h's number of U attachments in this block and U=sum_h u_h. There are only fifteen such U vertices, each of spare degree one, so U<=15. U pins owned by other helpers have empty B1 reach in these columns and cannot substitute for h's own U supports.

### f=0 or f=1

Choose a column with no same-column F attachment. Even an owner has at most a three-point F repair there; nonowners have no more. At most two U supports cover at most eleven targets, so together at most fourteen of the fifteen targets. Every helper would require at least three U pins, giving U>=18>15. Thus these cases are impossible.

### f=2 in one column

In the other column a nonowner gets at most the two absolute points supplied by cross-column B1 reach. Two U supports plus those points cover at most thirteen targets, so every nonowner needs at least three U pins. An owner gets at most the two cross-column N rows; one U support plus their union has at most 7+6=13 points, so each owner needs at least two U pins. There are at most two owners. With r<=2 owners,

    U >= 3*(6-r)+2*r = 18-r >= 16,

again impossible. This already allows the most favorable overlapping/shared pin positions.

### f=2 split between the columns

Say the pins' A labels are a at b and c at b*. A nonowner's F contribution in column b is contained in N_a union {c}. One U pin is too small by cardinality. With two distinct U supports the four missed points cannot all be repaired by N_a union {c}, by the preceding small A fact. Thus every nonowner still needs at least three U pins.

If there are two owners, an owner has, in its own column, at most its P_a and the other pin's single absolute point. Adding one U support gives at most 11+1=12 points. Thus both owners need at least two U pins, yielding U>=4*3+2*2=16.

If the same helper owns both pins, its F contribution in one column is contained in P_a union N_c, hence in P_a union P_c, of size at most eleven. It needs at least one U pin. The five nonowners need at least fifteen more, again U>=16. These cases exhaust f=2. Therefore every sigma pair must have f>=3.

### f=3

There are at most three owners. Choose the column with at most one same-column attachment. A nonowner sees at most one three-point N row and two cross-column absolute points, at most five F-repaired targets. One U support gives at most seven more, still fewer than fifteen. Each nonowner requires at least two U pins.

At most three absolute A labels are present among the pair's F pins. An untouched absolute A target cannot be reached by any of their F envelopes: P_a, N_a and {a} all contain no absolute other than a. Pins outside this sigma pair give no repair in these columns. Therefore **every** helper, including all owners, needs at least one U pin. With r<=3 owners,

    U >= 2*(6-r)+r = 12-r >= 9.

The lower bound does not assume equal pin counts, distinct owners, or distinct touched labels.

### f=4

At most four of the five absolute A labels are touched. The same untouched-absolute argument forces at least one U pin for each helper, so U>=6. For f>=5 no U lower bound is needed here.

## 4. Block accounting and the contradiction

Let f_1,...,f_4 be the four pair attachment counts in one block, F_y their sum, and U_y the common U count for that block. Each f_i>=3. Importantly, U_y is shared across the four pairs: the proof takes a maximum of their U requirements, not their sum.

* If any f_i=3, then U_y>=9 and F_y>=12, so U_y+F_y>=21.
* If no f_i=3 but some f_i=4, then U_y>=6 and F_y>=16, so U_y+F_y>=22.
* Otherwise every f_i>=5, so F_y>=20 by itself.

In every case U_y+F_y>=20. This is a necessary lower bound, not a claim that a 20-pin block assignment exists. Block partitioning now legitimately sums across y:

    total useful helper pins >= sum_y (U_y+F_y) >= 8*20 = 160.

Each of the six helpers already has five K6 neighbors and degree cap 31, so all helper-to-old attachments together are at most 6*(31-5)=156. The missing four attachment slots give a strict contradiction. The thirty pool vertices that do not reach this target subset cannot reduce the 160 useful-pin demand and only consume budget if used.

Only 960 original targets were needed for this contradiction. All original F and clone targets in the full exact model remain required, but dropping them is a relaxation and cannot invalidate this necessary obstruction. No helper-prefix condition or conclusion from deleting vertices from a larger graph was used.

## Disposition and next-rule meaning

The exact G0 plus six-helper K6 integer completion is impossible by this bound, modulo the inherited literal inputs and the new actual local bindings. Keep the numerical MILP UNKNOWN and the valid fractional LP witness as separate historical results. There is no reason to restart its timer or construct a final 10076 graph for this fixed rule.

The obstruction identifies a concrete generation issue: current sigma/cycle transport keeps useful repair channels in eight invariant blocks, and indivisible fifteen-point A support obligations force too many attachments there. A new rule would have to alter that structural budget, for example by genuinely sharing repairs across blocks; this note neither chooses nor tests such a rule. It does not exclude arbitrary cap31 graphs, another hole set, another helper graph, a different peer/copy pattern, cross-block sigma transport, or the whole retained-edge mechanism. The original prediction's reference to an old 235 graph is a harmless typo for the 230 calibration; neither was rerun. Portfolio, parameter and Lean increments are all zero. This paper-only task is terminal.
