# Prediction: sigma's eight invariant blocks force160 pins, above156

2026-11-01, after the actual one-shot MILP timed out and after the explicit
fractional witness and refined route strata were checked. This is a new
integer-allocation obstruction for this ONE G0, not a claim from UNKNOWN.
All proposed checks below fit in the unused original120CPU budget
(95.905302CPU used so far); no second solver or graph pattern is authorized.

Let Y=N_B(0), the eight saved nonabsolute neighbors of the fixed port0.
For every other B absolute b, its old R2 support contains exactly one y in Y;
define G_y as those b. The saved point-to-line projection data should give
eight disjoint groups of size8. The saved sigma fixes0 and all y in Y, so
each of its32 absolute transpositions lies inside one G_y. Bind this mapping
from the already saved PORT_R2.json and actual sigma pairs; do not rerun
old585 R2/Steiner or sigma-edge checks.

In each block y there are15 available U pins(585*x+y), x0..14, each with
spare1; let u_h be the number assigned to helper h and U=sum_h u_h<=15.
Other freed U pins cannot reach old targets(585*x+b), b in G_y, in one/two
G0 steps. All free F pins that can repair those targets have B coordinate
in the same block; sigma never transports repairs to another block.

For the literal A relation, let P_x be the positive support of row x of A²
and N_a the three-entry adjacency row of an absolute a. Predict:

* every P_x has7 points; two distinct supports have union11;
* P_a intersects the absolute set only in a;
* for any two distinct x,z and absolutes a,c, their four missed points
  are not all contained in N_a union{c} (at most three are contained).

These are small new local support obligations. Check all105 pairs and
2625 pair/absolute/absolute combinations, not A³ or the old230 graphs.

The specific G0 rule implies the following generous upper envelopes for
an F pin based(a,b) and its sigma partner b*:

|pin's G0 reach to original targets A×B-absolute|same b|partner b*|other columns|
|---|---|---|---|
|closed B2 (own helper)|P_a|N_a|empty|
|closed B1 (other helper)|N_a|{a}|empty|

They are upper bounds, allowing favorable copy positions even when a
particular copy lacks a listed target. Each U pin(x,y) has old-target B2
exactly P_x×G_y and B1 empty there. The other ten freed U pins and the20
F representatives over b0 do not reach these64-column old targets in
B1/B2. A targeted check of these current-G0 envelopes can bind the paper
proof; no helper BFS, old585 neighborhood or new integer search is needed.

Fix one of the four sigma pairs{b,b*} in a block. Let f count all actual
helper-to-F pin attachments in these two columns, including repeated pins.
All six helpers must cover all15 original A targets in each column.

## Predict that f<=2 is impossible

If f0 or1, choose a column without its own F attachment. Every helper has
at most a three-point repair there; with at most two U pins it reaches at
most11+3<15. All six helpers would need at least3 U pins, exceeding15.

If f2 are in the same column, at the other column nonowners see at most
two absolute points and need3 U pins. Each owner needs at least2 U pins:
one U support7 plus at most two cross-column N rows6 still gives<15.
With at most two owners, total U>=16.

If f2 are in different columns, a nonowner's repair is contained in
N_a union{c}. The predicted four-missed-point fact implies it needs3 U
pins. With two owners, each owner needs at least2 U pins: one U support
and its own same-column P_a cover at most11, and the other pin adds at
most one absolute point there. Thus U>=4*3+2*2=16. With one shared owner,
the other five need3 each; that owner still needs a U pin because its two
F-derived contributions are inside two P supports, whose union<=11.
Again U>=16. Hence every sigma pair requires f>=3.

## Predict the stronger bounds at f3 and f4

At f3, at most three helpers own an F pin. In the column with at most one
same-column attachment, a nonowner sees at most3+2=5 repaired A targets.
One U support7 is insufficient, so each nonowner needs at least2 U pins.
At most three absolute A labels occur among those F pins. Any untouched
absolute target can only be reached using a U pin, since same-column P_a
and cross-column N_a contain no other absolutes. Thus every helper needs
at least1 U pin, and U>=2*(6-3)+3=9.

At f4, at most four A absolute labels are touched. The same untouched-
absolute argument gives U>=6. These claims allow arbitrary pin owners,
copy indices, repeated classes, and all permitted endpoint sharing.

## The per-block and global contradiction

Each block has four sigma pairs, all with f>=3. If a pair has f3 then
U>=9 and total F attachments>=12, costing at least21 pins in this block.
Otherwise, if a pair has f4, U>=6 and F attachments>=16, costing at least22.
If every pair has f>=5, the F attachments alone cost at least20.
Thus EVERY block requires U+F_attachments>=20. Eight disjoint blocks require
at least160 helper pins, but K6 at cap31 permits only6*26=156. The extra
ten freed-U pins and twenty F points over b0 cannot reduce this target
obligation and only spend more budget. Predict that this proves the exact
G0/K6 rule impossible despite its rational LP witness.

An independent paper attack must check all route envelopes, the f2 owner
cases and the per-block accounting. If supported with the local bindings,
stop this fixed model as a mathematical exclusion separate from the solver's
UNKNOWN. It does not exclude another sigma/peer action that transports
repairs between blocks, another omission pattern, helper graph or cap31.
In particular the old uniformly saturated exclusions are not being reused.
The next effective rule change would need genuine cross-block repair reuse,
not a longer run of this model.
