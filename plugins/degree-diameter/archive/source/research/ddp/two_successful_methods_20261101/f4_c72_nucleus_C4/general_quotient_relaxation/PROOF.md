# A fifth quotient direction repairs one Exoo conflict, but not either72 controller

## New relaxation, rather than the old24map domain

The preceding experiment restricted cross maps to conic symmetries. Its
permutation domain fixed sourceport p to target reverseport r and left only
24 possibilities for the other four conic directions. This experiment
releases the conic-symmetry condition. An arbitrary invertible linear or
semilinear map carrying the sourceport line to the targetport line induces
a bijection of the five projective directions of the2-dimensional quotient.
The fifth target direction can be the nucleus/tangent direction, unequal to
all four other outgoing conic directions. It is a genuine extra allowed
column for the unique-route matching problem.

We relax to all120 bijections of the five quotient points and impose no
condition on the image of the source's fifth, omitted quotient point. This
contains all actual invertible linear/semilinear quotient maps. Thus an
empty domain in this relaxation is a necessary obstruction even before
choosing explicit3×3 maps, nucleus scaling or intrafiber shift behavior.

The earlier24domain failure remains valid and unchanged. No360map search,
D0/D2 gate, SAT call or graph generation was run in this follow-up.

## Actual quotient labels

Use polynomial F4, five conic vectors L0=(0,0,1), L_(1+t)=(1,t,t²), and
N=(0,1,0), as in the actual parent INPUT.json. For finiteport p=1+t choose

    H_p=[[1,0,0],[t,1,0],[0,t,1]],

and for p=0 choose

    H_0=[[0,0,1],[1,0,0],[0,1,0]].

Each sends L_p to e0. Project the last two coordinates to PG1(F4), whose
label order is∞,(1,0),(1,1),(1,w),(1,w+1). Actual finite checks give:

- for every i≠p, the image of L_i has quotient label i;
- the image of N has quotient label p, distinct from all four others.

Therefore the four source incoming rows are exactly all labels except p,
and the target's four outgoing conic columns are all labels except r. The
fifth allowed target column, label r, is the nucleus joker. The source's
unused N-row p merely receives the one column unused by the four incoming
rows. A matching of four rows into five columns has120 possibilities.

QUOTIENT_BINDING.json saves all five actual H matrices, their conic
projections and their nucleus projections. The old conic permutation was
not silently reused: in particular this new quotient permutation is **not**
required to send p to r.

## Why the saved unique-route constraints remain necessary

For a controller pair at distance exactly3 with a unique three-cross word,
every possible length≤3 fiber path uses that word and has no room for an
intrafiber step. After stripping its last invertible semilinear cross map,
the noise columns are, up to independent nonzero field scalars,

    T_middle(L_i), L_r, L_j.

Full rank requires the quotient image of incoming row i to differ from
outgoing column j. If they agree, the unique word reaches at most16 of64
fiber targets. Hence each saved forbidden entry(row i,column j) is necessary
for arbitrary invertible portline-transport maps, not just conic symmetries.
For reverse stored-edge traversals the parent certificate already normalized
the inequality using the inverse permutation; those actual normalized
unique-route entries are reused unchanged.

This argument uses only the unique-route rank requirement. The previous
claim that many bad conic routes all miss N is deliberately not used here:
general maps need not preserve that common nucleus obstruction.

## Actual result on Exoo72

Every180 edge was checked against all120 quotient bijections. The old first
empty edge0→51 is repaired: its relaxed domain now has12 possibilities. Its
old three-rows-into-two-columns conflict gains a third allowed column, so
the predicted local benefit of the joker is supported.

But24 other edges remain empty. The first is edge24→61, with localports
p=r=3. Its incoming rows1,2,4 are each forbidden from outgoing columns0,1,2.
They may only use columns3 and4; column3 is the newly allowed nucleus joker.
Three different rows still cannot be injected into these two columns.

Exoo's full relaxed domain-size histogram is

    0:24, 12:48, 28:72, 31:12, 48:24.

Exoo72/MINIMAL_HALL_CERTIFICATE.json lists the nine forbidden entries and
their actual unique controller endpoint/word witnesses. This one3→2 Hall
failure suffices to exclude the general cross-map relaxation on Exoo72.

## Actual result on Michel72

Its first edge0→9 has p=r=0. Rows2,3,4 remain forbidden from columns2,3,4.
The new nucleus joker is column0, so the only allowed columns for those
three rows are0,1. The old conflict gains one column but still fails3→2.

Exactly36 of180 edges remain empty, with relaxed domain-size histogram

    0:36, 8:72, 20:36, 78:36.

Michel72/MINIMAL_HALL_CERTIFICATE.json retains that small obstruction and
actual unique-route witnesses. No global assignment or shift choice can
repair an already impossible local injective quotient map.

## Decision and exact scope

Both specified72 controllers remain excluded for the homogeneous F4³,
full-line cross-edge mechanism with arbitrary invertible linear/semilinear
portline-transport maps and the proposed degree2 intrafiber C4 augmentation.
Changing those intrafiber routes cannot help these controller-distance3
unique pairs, since all three available steps are already cross steps.

This strictly strengthens the previous conic-symmetry exclusion on the same
two controllers. It does not exclude other controllers, other cross-edge
relations, a different graph parameter or arbitrary4608vertex22degree graphs.
No broad statement about all many-word distance3 pairs under general maps is
made. D0/D2 sufficiency for the released maps was neither assumed nor tested.

The actual gate took0.098530715CPU, one worker, within30CPU. It read the saved
unique-route constraints and field INPUT only, without recomputing any
controller shortwords, controller/source BFS or old graph. It generated no
360matrix domain, solver model, candidate graph or Lean output. All local
jobs are terminal. There is no surviving controller interface to pass to
the next planned matrix/D0/D2/SAT stage.
