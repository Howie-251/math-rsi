<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Shared locks: actual fan, separated blocks, and the free penultimate

2026-11-20. This branch owns only this directory. It uses actual ordered complete
rank-3signotopes in the Q8domain (no blue7, no red8, no weak8). No external review.
All scientific execution is on Linux. Existing near64jobs are never restarted.
The caller's supplied free-penultimate construction is checked below; it avoids
any claim that one lock has only one owner.

The caller's existing definitions and imports are in
[the current common-budget proof](../N8_F306_ES307_20261120.md): ordinary866≤56,
ordinary867≤100by coordinate transport, C8≤187, D8≤120, the common t(h)budget,
and the actual462-state ordinary-row inequality. The path-lock input itself is
[R7§3.1](../../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R7_DEFICIT_STABILITY_AND_JOINT_WITNESSES.md); ambient H-endpoint
closure uses[R20§5.2](../../../nmrs-20261117/source/.trellis/tasks/10-19-nr7-structure-capacity/research/RESET_R20_GLOBAL_PROOF_ARCHITECTURE_AND_JOINT_REALIZABILITY.md).

## 1. A mixed owner gives a genuinely frozen extreme pair

Let$a$have an actual incoming red6, an ambient red7starting at$a$, and an
ambient blue6starting at$a$. R7§3.1locks all its red7ends and all its blue6second
vertices to the same$q>a$. Fix a blue6$J=(a,q,j_3,j_4,j_5,j_6)$.

For$x<a$, a blue$(x,a,q)$would prefix$x$toJand give blue7, so it is red.
For$a<x<q$, a blue$(a,x,q)$would join the red7$a\to q$at the same ends to make
weak8, so it is red. The last predecessor$f$of the incoming red6therefore has
red$(f,a,q)$, giving a red7whose last pair is$(a,q)$. For$t>q$, red$(a,q,t)$
would extend this path to red8; hence it is blue.

Thus, on the entire actual mother,

$$\chi(\operatorname{sort}(x,a,q))=R\quad(x<q, x\ne a),$$
$$\chi(a,q,t)=B\quad(t>q).$$

The actual pair ranks, with coordinates orderedB,Rand lengths counted in edges,
are exactly

$$l(a,q)=(1,6),\quad f(a,q)=(5,1),\quad
u(a,q)=(6-f_B,7-f_R)=(1,6).$$

This is an actual frozen pair, not merely a frozen point ideal. In the common
pair linear order, $aq$is the strict maximal incident pair at$a$. This maximal
selector is different from the originalR7minimal selector$p$.

## 2. The entire physical interval has the same maximal fan

For$a<v<q$, red$(a,v,q)$gives$aq\prec vq$. Each$j_i>q$has
$qj_i\prec aq$from the fixed blue6. Therefore$vq\succ qj_3$, forcing
blue$(v,q,j_3)$; the rest ofJremains blue. Every$v\in[a,q)$starts an actual
blue6through$q$.

Now for$x<v<q$, blue$(x,v,q)$would prefix$x$to that blue6and give blue7.
Applying this observation to the later of any two vertices below$q$shows that
all$(x,v,q)$in the block are red. For$t>q$, the original owner's full fan gives
$qt\prec aq\prec vq$, hence blue$(v,q,t)$. Thus$q$is the strict maximal incident
selector for every actual$v\in[a,q)$, including nonowners.

Every red7starting at such$v$ends at$q$: an earlier end$y<q$would itself start
blue6, forbidden at a red7end by the common seam; a later end$y>q$would share its
ends with blue3$(v,q,y)$and produce weak8. This does **not** by itself say every
blue6from every nonowner uses$q$as second; that stronger fact below needs its
actual red6prefix.

For distinct locks, the owner intervals are strictly separated. If an owner$t$
of another lock$r$lay in$[a,q)$, its blue6through$q$would force$r=q$. The endpoint
$q$itself cannot own, because a red7end cannot start blue6. Consequently distinct
owner blocks have order$a<q<t<r$.

The last five physical points before$q$are in this block, start blue6, and do
not start red7: all red7from them would have to end at$q$, but there are fewer
than five intervening vertices. This gives five distinct(nonS,B6)points per
lock, **not automatically five points ofD**.

## 3. The caller's free-penultimate point is valid

Use$O=X\setminus(S\cup B)$, where$S$are actual red7starters and$B$actual blue6
starters, and write$p=|O|$. The old owner set is$A=G_*\cup M$, of size$g+m$,
and its distinct locks form$\mathcal L$, of size$\ell$.

For each$q\in\mathcal L$choose its latest owner$a$, and an actual red7from$a$
to$q$. Let$v$be its penultimate vertex and$f$the preceding vertex. The prefix
$a\to v$is an actual red6. By §2$v$starts blue6through$q$.

Consider **any** blue6from$v$with second vertex$y$. If$(f,v,y)$were blue, prepend
$f$to get blue7. Thus it is red, and the fixed red6$a\to v$followed by$y$gives
red7$a\to y$. The owner's unique endpoint forces$y=q$. Every red7from$v$also
ends at$q$by §2.

The point$v$is outsideOand outside every lock, since it starts blue6. It is not
an old owner: otherwise its blue6through$q$would force its own lock to$q$,
contrary to the latest choice of$a<v$. This argument does not need$v\notin S$,
or the stronger assertion that$v$ends a red6insideD. The separated blocks make
the chosen$v_q$distinct for different locks.

Hence the actual induced set

$$K=(O\cup A\cup\{v_q:q\in\mathcal L\})\setminus\mathcal L$$

has no blue6and no red7: every possible source is an owner or added$v_q$, whose
blue6second and red7end have both been removed; Ocontains neither type of ambient
source. Weak8is inherited. Ordinary867≤100therefore gives

$$100\ge|K|=p+g+m+\ell-|O\cap\mathcal L|\ge p+g+m,$$
$$\boxed{p\le100-g-m,\qquad p+b\le156},$$

using the already established$b\le56+g+m$. This is a common actual-set capacity
argument; no grid realizability or disjoint interiors of witness paths is used.

## 4. Exact algebra returned to the caller

Retain the ambient ordinary-row identity in its exact four-sector form:

$$882\ge5n+|S|-5b-4p.$$

The new inequalities give$5b+4p\le680+g+m$. Substituting
$n=187-h+d$and$|S|=d-e+g$therefore yields

$$\boxed{6d\le627+5h+e+m}.$$

The existing common budgets$5e+4m\le3+5h+w$and$w+m\le t(h)$imply

$$e+m\le\left\lfloor\frac{3+5h+t(h)}5\right\rfloor,$$
$$6d\le627+5h+\left\lfloor\frac{3+5h+t(h)}5\right\rfloor,
\quad t(h)=\left\lfloor\frac{3+5h}4\right\rfloor.$$

This exact consequence was returned to the caller for its main global assembly;
it is stronger than merely inserting$p+b\le156$as a standalone population cap.
It uses the old common budgets on their original physical sets, not new budgets
on the867setK.

## 5. Actual17-point counterexample to owner-fibre uniqueness

The [complete actual witness](../../inputs/signotopes/shared-lock17.json) is a complete
17-point Q8signotope with two genuineG_*owners5,6sharing$q=12$. Both use incoming
red6prefix$[0,1,2,3,4]$, red7tail$[7,8,9,10,11,12]$, and blue6tail
$[12,13,14,15,16]$. All680original triple colors are supplied.

The controlled Linux solve returnedSATin2.033013295seconds. A separate audit
recomputed all2380packets, true incoming/outgoing ranks, all actual fixed-end
maximal paths and weak8conditions, a complete strict pair-order extension,
its actual minimal selector and the trueP+/P-/G/H/Dpartition. Maximal blue/red
path lengths are at most6/7and the maximum opposite-color same-end sum is9.
Both owner's actual pair ranks are$l=(1,6)$and$f=(5,1)$.

The last five physical points before$q$are7,8,9,10inDand11inH. Thus neither
owner uniqueness nor an unconditional fiveDpoints-per-lock assertion can be
used. The caller's free point is11, beyond the latest owner6, and is inHbut
outside the old owners, matching §3.

[Raw result/bindings](../../SOURCE_MAP.md#excluded-sources):680variables,
1424184clauses; CNF SHA
`e9446f8646622effec8b836678470097f13e299584863b2501d3c4c15dbfaf4a`;
witness SHA`d1c7515ee4171e668c519efb4f451624f94bafb3a80b1a8611b8737ef9e1d0b8`.
Source is[probe_two_owners.py](../../SOURCE_MAP.md#excluded-sources). This is an actual abstract
signotope example; no geometric realization or critical298-point extension is
claimed.

One second tiny probe, launched before the caller's completion message, forces
the **same five-point incoming prefix** to give red6to every terminal vertex,
and makes all triples through the last vertex16blue. These extra restrictions
would put all five terminal vertices inHunder the actual minimal selector.
This specific stronger arm template is UNSAT: solver20in2.017458988seconds,
fixed checker0in2.014929599seconds, exactly oneVERIFIED. It does not prove a
universal prohibition on all-five-inH, because shared-prefix/all-blue-last
constraints are stronger than that membership assertion.

The [raw result and checker binding](../../SOURCE_MAP.md#excluded-sources) record
CNF SHA`9b4c8aca0383eae3d12e4881d984b1f175a9162cbe1f7ad792e922dd1ad81fc4`,
680variables/1424324clauses and a963-byte DRAT SHA
`31a1c0279006b8f17cd07970cd3ab8c334a1c959ee570a4ccb4547898557d25c`.
Full original artifacts remain in the fresh Linux
`two-owner-all-tail-H17-02/`directory. No additional solver is needed or launched
for the valid free-point upper-bound argument.

## 6. Preserved ordinary63work

At the actual05:02:21UTCsnapshot, the retained GRATgenerator had completed
[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]
05:02:27UTCand by05:12:30UTCwas actually verifying the split certificate,
RSS113477840kB. No terminal checker result was yet available. The original fixed
DRAT3833744remainedR,9.75%at05:02:21UTC. All processes and seals remain unchanged.
Generator-only success is not ordinary858≤63; the original-input bridge and
fail-closed terminal capture remain in the prior shared-chords directory.

## 7. Optional geometric enhancement: exact fixed-x exclusions only

The [fixed-abscissa test](GEOMETRY_FIXED_X.md) tries$x_i=i,i^2,i^3$and
$256-(16-i)^2$for the same actual17-point coloring. All four are infeasible,
each with an exact nonnegative rational Farkas certificate, verified against
all17determinant coefficient columns. No coordinates were recovered; general
geometric realizability with other abscissas remains unknown. All tests and
exact checks ran on Linux in0.122seconds, with no dependency installation,
external review or effect on the global proof. The optional branch stops at
the user-requested scope.
