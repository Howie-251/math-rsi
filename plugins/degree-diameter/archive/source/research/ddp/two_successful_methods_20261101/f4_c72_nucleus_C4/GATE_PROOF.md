# Two72 controllers fail the necessary local conic-permutation gate

The new construction changes the fiber rule by adding nucleus-C4 edges;
old C60/full-pencil controller-size restrictions are not applied. This file
proves the actual new failures, independently of whether the proposed
distance0/1/2 positive coverage lemmas are ultimately accepted. Complementary
mechanism analysis is kept in the separately owned MECHANISM_PROOF.md.

## Actual map domain, including the reverse

Over polynomial F4=F2[w]/(w²+w+1), let N=(0,1,0) and

    L0=(0,0,1), L_(1+t)=(1,t,t²), t∈F4.

The sixty normalized PGL2 matrices h=[[a,b],[c,d]] have nonzero
δ=ad+bc. The actual Sym² matrix is

    [[a²,0,b²],[ac,δ,bd],[c²,0,d²]].

For σ=0 or1, T(x)=s Sym²(h) Frob_σ(x), where s=α/δ, α=2 forσ0 and3 forσ1
on an oriented edge u<v. Actual enumeration gives120 distinct permutations
of the five conic directions, exactly S5; prescribing outgoingport p to
reverseport r leaves exactly24 maps.

The actual inverse has linear matrix B=Frob_σ(A⁻¹), with the same σ. Its
nucleus coefficient is3 for both σ0 andσ1; that is α⁻¹=3 in the linear case,
and Frob(3⁻¹)=3 in the semilinear case. All120 maps were checked on all64
vectors in both composition orders. For both orientations the C4shift union

    {1,2,α,α*Frob_σ(2)}={1,2,3}

also passes. DOMAIN_CHECK.json and SEMILINEAR_MAPS.json retain the exact
finite results. There is no failed field, inverse or shift identity in this
experiment.

## A unique distance3 word forces a forbidden permutation entry

Take a controller pair at distance exactly3 with a unique three-step word

    u → a → b → v.

Any length≤3 path between its fibers must use exactly these three cross
edges; it has no length budget for an internal C4 step. Let i be the port at
a pointing back to u, let p be a's port to b, let r be b's port to a, and let
j be b's port to v. The word is nonbacktracking, so i≠p and j≠r.

Strip the last invertible semilinear map from the three noise columns. Up
to independent nonzero field scalars, the resulting directions are

    T_(a,b)(L_i), L_r, L_j.

They are all on the same five-point conic. The first differs from L_r because
the edge permutation π is injective and π(p)=r. The last differs from L_r
by nonbacktracking. Any three distinct conic points are linearly independent,
so the noise has rank3 exactly when π(i)≠j. If π(i)=j its image has at most16
of64 targets and no other controller route can repair it. This is a necessary
condition for the actual graph, not merely a sufficient-certificate filter.

For a reverse traversal of the stored edge a<b, the equivalent normalized
forbidden entry is π(j)=i rather than π⁻¹(i)=j. prepare.py records that
orientation explicitly. Every exclusion below has an actual unique
controller endpoint pair and its complete three-word as a witness.

## Exoo72: three rows would need only two columns

The saved180-edge source uses sorted local neighbors as its ports. Its new
controller-role shortword enumeration gives3312 ordered distance3 pairs:
2160 have1 word,1104 have2 and48 have4. No old fiber graph or old full-source
D3 BFS is run.

For controller edge0→51, localports p=1,r=0, the unique-route obligations
forbid entries

    (0,1),(0,4),(3,1),(3,4),(4,1),(4,4).

After the fixed assignment π(1)=0, the remaining rows are0,2,3,4 and columns
1,2,3,4. Rows0,3,4 may only use columns2,3. An injective permutation cannot
send three rows into two columns: Hall's condition fails. Therefore none of
this edge's24 possible maps is admissible, independently of the other179
edge choices.

The full gate finds72 of180 edge domains empty. The one local Hall witness
already suffices. Exoo72/HALL_OBSTRUCTION.json gives the six forbidden
entries and actual endpoint witnesses; EMPTY_EDGE_CERTIFICATE.json additionally
identifies an excluding unique pair for each of the24 literal maps.

## Michel72: two rows would need only one column

The second saved72 source gives3420 ordered distance3 pairs:2376 have1
word,792 have2,144 have3 and108 have4.

For its controller edge0→9, p=r=0. The unique-route obligations forbid every
entry(row,column) with row∈{2,3,4} and column∈{2,3,4}. Thus after π(0)=0,
each of rows2,3,4 may only use column1. Already rows2,3 cannot both do so;
Hall's condition fails. Again the24map domain is empty before any global
choice or SAT solve.

The full gate finds108 of180 edge domains empty. Michel72/HALL_OBSTRUCTION.json
and EMPTY_EDGE_CERTIFICATE.json retain the corresponding small proofs and
actual unique-route witnesses.

## Decision and scope

Both specified72 controllers are strictly incompatible with this homogeneous
five-conic, true-inverse, nucleus-C4 construction. The obstruction is a local
permutation incompatibility among required distant routes. Correct local
shift coverage and more intrafiber reach do not alter a controller-distance3
pair's three-cross-edge budget.

The entire preprocessing took0.627833731CPU, one worker, within120CPU.
There is no surviving controller, so no SAT call was made and its60CPU
budget was not used. No4608 graph, candidate edge table, Lean theorem or new
record is claimed. No controller/port-seed/field/C4 continuation is dispatched.

The strict conclusion concerns these two actual controllers and the stated
conic-permutation cross-edge mechanism. It does not exclude other72
controllers, other cross-edge geometries, offsets, different internal moves,
larger degree or arbitrary(22,3) graphs. A relabeling of the ports only
renames the rows and columns of these full-permutation Hall obstructions;
it cannot justify a port-seed search on these same controllers.
