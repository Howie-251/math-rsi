<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# 2026-11-20: retained near64 proof recovery and shared-extender boundary

This branch began with the shared-extender obligation in
[the structural audit §5](NMRS_STRUCTURAL_AUDIT_20261120.md). The caller redirected
it to recovering the already complete ordinary858 near64 proof after a new
ordinary866≤56 checker result appeared. All execution below is on the authoritative
Linux server. No solver, external review or sealed-input edit was launched by
this branch. The initial phase used one recovered DRAT checker. The caller later
explicitly authorized the distinct parallel GRAT route recorded in §6.

## 1. The recovered obligation

The retained `near64-v1` is a necessary formula for a hypothetical 64-point
ordinary $N(8,5,8)$ input. Its original solver returned20. Its original checker
returned−11, so the original result remains `INCOMPLETE`. The proof and CNF were
retained unchanged:

| Artifact | Bytes | SHA256 |
|---|---:|---|
| CNF |170803254|`3754079cd7a76f18d12bfce74d00fa6fdb39ba145c91308337a9356c83e737a6`|
| DRAT |9327117152|`15bf2b1ee800eab71daba8916a53c21cf022102c6712022df56829dc9eafdbde`|

The other completed near64 rank-fan proof also has original checker−11. It is
untouched and was not selected for recovery: the base formula needs fewer
semantic imports.

The original checker source still declares32-bit `RATset` entries and sorts
them with `sizeof(int)`. This is the exact class of database-offset bug recorded
in [the project large-input contract](../SOURCE_MAP.md#excluded-sources).
The September14 repaired checker is already present on Linux and matches its
historical18-test receipt, including sparse offsets above `INT_MAX`, ASan, valid
and invalid proof fixtures, and timeout-option rejection. The current crash
has no debugger backtrace; matching the known defect is a diagnosis, not a
claim that this crash's precise instruction was independently observed.

The existing repaired binary SHA is
`0e0b9f7e0aa78ce2f4f970676407d95eae6908dff2b48af212f885d137374787`;
source SHA is
`ada55215f76b5ffe3af03be7e7259c75c855a3ee61603e80c260df4144b032de`.
Both were copied to the fresh replay directory, with the old failed receipt
and historical repair validation. Existing binaries, original CNFs/proofs,
and jobs were not replaced.

## 2. Independent full reconstruction: completed

[The new source](../SOURCE_MAP.md#excluded-sources) adapts the existing
independent near65 equation-level rebuilder. It imports no primary builder and
has no solver or checker invocation. The exact hole count changes19→20;
all source/target bindings and the expected CNF hash change accordingly.

The Linux run completed in13.405851654seconds and reproduced all298511variables
and5187264clauses byte for byte. It checked215369semantic variable IDs, including
their interleaving with the numeric cardinality counters. It independently
enumerated1048576six-point masks,908legal packets and843no-blue5templates, and
regenerated all563hole supports and24horizontal maps. Its resulting CNF SHA
is exactly the retained primary SHA above. The source SHA is
[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]

Raw successful stdout and command are in
[the reconstruction transport receipt](../SOURCE_MAP.md#excluded-sources).
The [standalone reconstruction receipt](../SOURCE_MAP.md#excluded-sources),
[actual launch binding](../SOURCE_MAP.md#excluded-sources), and
[historical checker validation](../SOURCE_MAP.md#excluded-sources)
have also been fetched locally.
The fresh Linux output directory is
`<private-artifact-root>`.

The [existing near65 semantic bridge](evidence/n8-d122-common-bridges-20261119/NEAR65_SEMANTIC_BRIDGE.md)
applies to the same necessary source schemas: actual trueP injects into84states;
all missing-angle and row-entry charges use the same actual labels; prefix-six
coverage is complete. For64points there are20holes, and the nine coordinate
charges give total missing angles≤6 rather than≤3. This is the only population
change in the base necessary formula. No frozen66 assumptions, `u=l`, rank-fan,
or extra Hall variants enter this recovery.

## 3. The one actual checker: pending

The controller is
[recover_near64.py](../SOURCE_MAP.md#excluded-sources). It checks the input
hashes before launch, runs one process, and after termination requires exit0,
exactly one `s VERIFIED`, and unchanged CNF/proof/checker/source hashes.
Its fresh output root is
`<private-artifact-root>`.

Actual controller PID3833686; actual checker PID/PGID3833744, launched
2026-11-20 03:18:39.869091UTC. Command:

```text
stdbuf -oL <fresh-root>/checker <original-near64>/model/formula.cnf <original-near64>/proof.drat -t 0 -b
```

To resume monitoring, invoke only
`<private-python-runtime> -B <shared-chords-root>/checkpoint_recovery.py <fresh-label>`.
The helper reads the existing PID, descriptors and log, writes one small fresh
receipt, and includes the terminal `result.json`when present. Do not relaunch
`launch_recovery.py`or `recover_near64.py`while this bound run exists.

The first observed checker log reports binary-mode checking and parses the
298511-variable/5187264-clause input. No verdict or ETA is inferred from that.
At03:22:48.815284UTC the checker was actually R with11044864kB resident memory;
its proof descriptor position was7960072192of9327117152bytes,85.34%of the
serialized input. This measures parsing, not verified proof progress. The
[raw checkpoint](../SOURCE_MAP.md#excluded-sources) includes
all process-file descriptor positions and the actual command.
At the later [03:32:32UTC checkpoint](../SOURCE_MAP.md#excluded-sources)
the same checker remained R, fully parsed, with12862048kBresident memory and
no verdict. It had run13minutes52seconds. No second checker was started.
The [03:35:58UTC checkpoint](../SOURCE_MAP.md#excluded-sources)
then records actual verification progress0.29%and the checker's own remaining
time estimate53407.41seconds (about14.84hours). This is an early, unstable
internal estimate, not a completion promise. The checker remained R with
12867168kBresident memory. The `-b`option does emit a progress display during
verification, in addition to its initial binary-mode banner. The bound process
is preserved, without a deadline or resubmission.
[Operational connection details omitted from this publication excerpt.]
process listings before a successful create-only Python detacher was used;
they launched nothing.

If and only if this actual replay succeeds, its mathematical scope is a single
successful DRAT over a separately fully reconstructed necessary formula,
yielding ordinary858≤63. It is not two DRAT runs, a new solver result, or an
external proof audit. With an independently established ordinary866≤56 and
the caller's stated C8≤187 bridge, this would yield D8≤119 and F8≤307. Until
the actual checker succeeds, no such additional numerical conclusion is claimed
by this file.

## 4. A precise extender fact retained from the original branch

For the real R7selector $p$, let $u<z=p(u)$ and $w=p(z)$. Then

$$u\le w<z.$$

Indeed $w<z$ is the established R7sign rule. If $w<u$, the fan at $u$ makes
$(w,u,z)$ blue. Its pair order gives $uz\prec wz$, contradicting the minimality
of $wz$ at $z$. Thus every source in the positive fibre of $z$ lies at or left
of its actual opposite selector $p(z)$; equality is exactly a mutual pair.
This is stronger than treating $p$ as arbitrary laminar arcs, but does not say
every fibre contains the opposite selector.

For $u<v$ in the real residual, if $p(u)=z<p(v)=y$, the established noncrossing
fan rule gives the strict separated order $u<z<v<y$. Shared roots and nested
arcs remain possible. In particular the existing single-extender construction
still allows all of a legal residual in one fibre; no universal fibre cap below
the residual capacity follows from the selector fact alone.

The proposed five-chord obstruction is valid as a necessary condition, but this
branch has not converted21/22matched bridges into such an ordered chord pattern,
nor proved the required shared matching upper bound. No central upper bound
is attributed to that unfinished argument. The new useful action is recovering
the already completed64-point exclusion with the correct large-input checker.

## 5. The improved short-cap import changes the frozen frontier

This subsection is conditional on the caller independently completing its new
ordinary866≤56 import. It uses the already proved general potential lemma in
[C188 §5](N8_C188_311_20261119.md), not the pending near64 replay.

For $k=4$, both private70-state faces then have at least $t=14$holes. If
$H=252-|Cpart|$, its budget is now

$$B_0=5H-210-8\cdot14=5H-322.$$

Thus the actual two-end ideals obey

$$4L_{\rm internal}+L_{\rm private}+L_{\rm cross}
\le16B_0-5L_{\rm cross}.$$

In the new $|Cpart|=187$frontier, $H=65$and $B_0=3$. The exact row identity
$Z+4\eta=3$forces $\eta=0$in **both** actual endpoint charts. Consequently
each private face has exactly14holes, $Z=3$, and
$L_{\rm cross}\le\eta_P+\eta_E=0$. No physical point changes among the three
classes (first private face, second private face, internal) during its actual
$P\subseteq E$movement. Each private face contains56physical points, and the
internal class contains75.

The remaining inequality is

$$4L_{\rm internal}+L_{\rm private}\le48.$$

At most48of187points move at all, so **at least139points are frozen**.
At most12of the75internal points move, so **at least63internal points are
frozen**. These conclusions concern the same physical actualP/Echarts.
They strengthen the older188-point/t13specialization (only92frozen points)
and are valid even if the858≤63checker has not completed.

There is also an exact four-role consequence. Under unit ideal moves the two
internal word classes (containing both extreme coordinates1,10and containing
neither) cannot exchange without passing through a private class. Therefore
$L_{\rm cross}=0$preserves **all four** extreme-coordinate classes for every
physical point, not just their three-class grouping.

For clarity this has the following direct true-rank interpretation. Let
$S_B,S_R,E_B,E_R$be the actual starts/ends of six-point blue/red paths in this
same187-point $H$. Incoming $P$contains $(5,1)$exactly on $E_B$, and contains
$(1,5)$exactly on $E_R$. Since
$E(v)=G\setminus\uparrow\{(6-f_B(v,w),6-f_R(v,w)):w>v\}$for actual outgoing edge ranks,
it excludes $(5,1)$exactly on $S_R$, and excludes $(1,5)$exactly on $S_B$.
Thus agreement of the extreme-coordinate classes says that every point is in
exactly one of

$$L=S_B\cap S_R,\quad T_R=S_R\cap E_R,\quad
T_B=S_B\cap E_B,\quad R=E_B\cap E_R.$$

The actual first private class is $L$and the last private class is $R$.
Consequently

$$|L|=|R|=56,\qquad |T_R|+|T_B|=75.$$

In particular **a187-point C8input with any point outside these four roles
is excluded**, once ordinary866≤56is established. This is a quantified
conditional exclusion of actual inputs, not a claim that the remaining class
is realizable or that its common bridges have the required upper bound.

For the same imported bound the ordinary four-by-five capacity is
$N(8,6,7)\le\lfloor9\cdot56/5\rfloor=100$by the established coordinate
deletion transport. Both $S_R$and $S_B$have that capacity (the common-seam
argument excludes a blue6inside $S_R$and a red6inside $S_B$). Hence
$56+|T_R|\le100$and $56+|T_B|\le100$, giving

$$31\le |T_R|,|T_B|\le44.$$

Their populations are therefore14complementary possibilities, while all actual
path supports and selectors still have to be retained. This restriction does
not prove that any of those14possibilities is impossible.

For the adjacent $|Cpart|=186$frontier, $H=66$, $B_0=8$, and the same formula
gives total area≤128and at least58frozen physical points. It does not force
$\eta=0$there. Neither specialization supplies the still missing shared-chord
or matching upper bound by itself.

## 6. Explicitly authorized faster independent GRAT route

The continuing numerical caller asked to finish F8≤307/ES8≤308and explicitly
authorized a distinct installed parallel GRATgenerator plus independent checker,
while retaining the one fixed DRAT run. No duplicate drat-trim or new dependency
was launched. Exact census, signed32integer admission, memory/disk admission and
actual small binary inference/rejection gates all passed. A fresh detached
16-thread controller PID3848781was then launched. Its output root is
`<private-artifact-root>`.

The [dedicated physical64proof entry](shared-chords-20261120/ORDINARY858_63_PROOF.md)
gives every imported mathematical premise and the original-input→exact-CNF bridge,
all raw proof/input/tool bindings, separate reconstruction and checker acceptance,
and the conditional final numerical chain. It now also records the distinct GRAT
route's actual admission and launch. A generator verdict without the independent
GRATchkverdict remains incomplete. Neither running route contributes858≤63yet.

## 7. Primary-source check of the actual one-point exchange

This is a conditional paper consistency check requested by the caller, not an
external review. Assume the genuineR7partition of aQ8input has$|H|=187$and
ordinary866≤56has been established. Then §5gives universal zero neutrality
for every actual187-point C8input:

$$H=S_{B6}(H)\sqcup E_{R6}(H).$$

**Ambient H-source closure.** R20§§5.2–5.4specializes from$n=7$to$n=8$using
R7§3.1without changing its logic. First an ambient red7with both endpoints in
$H$is excluded by the originalR7proof, regardless of its interior. If an ambient
red7ends at$v\in R$and starts in$H$, choose its earliest possible$H$source$a$.
A$P_-$source extends to red8, so$a\in G$. If$a$starts a blue6inside$H$, its second
point differs from$v$, and the$G$incoming red6plus three-chain lemma contradicts
the path. If$a$ends a red6inside$H$, take that actual prefix$F'$and any$G$ambient
blue6from$a$. Three-chain forces that blue6's second vertex to be$v$.
Writing$f$for the last predecessor in$F'$, a blue$(f,a,v)$prefixes the blue6to
blue7; a red$(f,a,v)$extends$F'$to the same$v$from an earlier$H$source. Both are
impossible. Zero neutrality covers both cases, proving that **no ambient red7
starts in$H$**, for any endpoint.

Now let$s\in R$have all three actual properties:

1. an ambient red6ending at$s$;
2. an ambient blue6starting at$s$;
3. a red7from$s$whose other six vertices lie in$H$.

The third property is automatically supplied by$H\cup\{s\}$and C8≤187once the
ambient H-source closure above is known. Conditions1and2remain the substantive
existence requirements for choosing$s$.

Fix one such red7tail$P$, ending at$q\in H$. The three-chain lemma applied to
the fixed incoming red6,$P$, and **each** ambient blue6from$s$forces the second
vertex of every such blue6to be$q$. Conversely fix any one such blue6$J$;
applying the same lemma to **every** ambient red7from$s$forces its endpoint to
be$q$. The conclusion quantifies over all actual alternatives, not one chosen
representative.

Put$H'=(H\setminus\{q\})\cup\{s\}$. It has187actual points and inherits no
blue7/weak8. It has no red7: a path starting at an old$H$point is impossible by
the ambient closure, and a path starting at$s$would have to end at the deleted$q$.
Hence$H'$is a genuineC8input and has universal zero neutrality after its ranks
and paths are recomputed.

Yet$s$cannot start a blue6in$H'$, since every ambient one has second vertex$q$.
If a red6$F'$inside$H'$ended at$s$, its last predecessor$f$is an old$H$point.
Since$J$starts$(s,q)$, a blue$(f,s,q)$gives blue7by prefixing$f$to$J$; a red
$(f,s,q)$extends$F'$by$q$to an ambient red7starting in$H$. Both are impossible.
Thus$s$also cannot end a red6in$H'$, contradicting its universal zero neutrality.

Therefore no such$s$exists. The exchange is logically sound with the stated
actual-path premises. To turn it into a global numerical proof, its caller must
still supply an actual$s\in R$with conditions1and2, or otherwise exclude the
remaining domain. This check does not invent that existence premise.

## 8. Final branch handoff

The caller reports that its separate analytic macro proof now reaches the
requested F8≤307/ES8≤308without ordinary858≤63. The pending near64routes are
therefore a separate stronger ordinary-capacity result, not a prerequisite for
that already assembled numerical chain. No further computation was expanded
after the caller's instruction; both authorized processes remain unchanged.

At the [actual04:02:21UTC handoff](../SOURCE_MAP.md#excluded-sources),
[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]
complete in311860msand forward pass active. Both detached controllers have PPID1.
Neither terminal verdict existed. The [durable runbook](shared-chords-20261120/RUNBOOK.md)
lists exact monitor commands, automatic terminal receipt paths and fail-closed
collection steps. The original and reconstructed CNFs, proof, tool snapshots,
before/after hash gates and all prior receipts remain bound and preserved.

## 9. Resumed target on2026-11-20

The user now requests F8≤306/ES8≤307. The caller resumes monitoring the two
unchanged bound near64proof routes until successful completion or explicit
release. At the [fresh04:07:39UTC snapshot](../SOURCE_MAP.md#excluded-sources),
[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]
pass; no terminal result. No duplicate solve/checker or external review is added.

The exact new caller connection is in the [dedicated proof entry §10](shared-chords-20261120/ORDINARY858_63_PROOF.md):
ordinary63would give D≤119, while the new [macro paper](N8_F307_ES308_20261120.md)
already bounds the R7H187branch by187+104=291. The remainingH≤186branch would
then have at most186+119=305points, provingQ305/F306/ES307once the actual ordinary
checker result is available. This does not replace the macro's stated paper
guarantee or pretend that ordinary63has already been checked.

## 10. Internal check of the new common-budget macro

**2026-11-20 successor:** the stronger all-lock deletion argument is now in
[N8_F306_ES307_20261120.md](N8_F306_ES307_20261120.md), appended with the
Q8≤298/F8≤299/ES8≤300proof. With all distinct locks$L$, the actual set
$Z=(H\cup(D\setminus S)\cup M)\setminus L$isC8and retains every lock owner.
The earliest-owner exception argument gives
$5e+4m\le3+5h+w$, hence
$50d\le5538+30h+21t(h)$with$t(h)=\lfloor(3+5h)/4\rfloor$.
This strengthens the Q299/F300/ES301step recorded below; no new computation or
external review is involved.

The caller subsequently supplied a stronger paper argument givingQ8≤299,
F8≤300andES8≤301without ordinary63. This subsection records the requested
primary-source/internal check; it is not external review or formal acceptance.

Use the caller's notation on one actualQ8input: $|H|=187-h$, $|D|=d$,
$S$the ambient red7starters, $G_*=S\cap H$of size$g$, and$W\subset D$the
red7endpoints supplied by thoseHsources, $|W|=w$. R20§5.2applies without a
population equality, so allH-source red7endpoints are outsideH. Each$G_*$point
belongs to the original$G$, hence has actual incoming red6and ambient blue6.
R7§3.1therefore locks all its red7ends and all blue6second points to one member
of$W$.

Let$M=D\cap S\cap S_{B6}(X)\cap E_{R6}(D)$with$|M|=m$. Its actual incoming
red6plus ambient blue6and red7also supply a unique lock. Let$Q_H\subset H$be
the distinctMlocks insideH, and put$\delta=m-|Q_H|\ge0$,

$$Y=(H\setminus Q_H)\cup M,\qquad |Y|=187-(h-\delta).$$

No lock is an owner: a red7endpoint cannot start a blue6, since the common seam
extends one path to red8or blue7. Hence no point of$W\cup Q_H$is in$G_*\cup M$.
Every ambient red7starting inYstarts at$G_*\cup M$, and its lock lies outsideY.
ThusYis a realC8input. C8≤187first yields$\delta\le h$.

For each distinct$q\in W\cup Q_H$choose the earliest owner$s\in G_*\cup M$
with that lock. It remains inY. It cannot end an ambient blue6because it starts
a red7; it cannot start a blue6inYbecause every ambient blue6second is the
absent$q$. If a red6insideYended at$s$, let$f$be its predecessor. A blue
$(f,s,q)$prefixes the owner's blue6to blue7. A red$(f,s,q)$creates an ambient
red7from the red6's earlier source$t\in Y$. That$t$is in$G_*\cup M$and its
unique lock is$q$, contrary to the chosen earliest owner. Thus$s$also cannot
end a red6inY.

These$w+|Q_H|$different owners are therefore in the initial privatePface ofY
and outside its initial privateEface. For actual$P\subseteq E$, the physical
Eface is a subset of the physicalPface. ThePface has at most56points, while
theEface has at least$56-\eta_E$points. The same t14ordinary-row identity gives

$$4\eta_E+Z_E=3+5(h-\delta),\qquad Z_E\ge0.$$

Consequently

$$w+|Q_H|\le\eta_E\le\left\lfloor\frac{3+5(h-\delta)}4\right\rfloor,$$
$$m+w=\delta+w+|Q_H|
\le\left\lfloor\frac{3+5h-\delta}4\right\rfloor
\le\left\lfloor\frac{3+5h}4\right\rfloor.$$

This is the common budget; counting eachMowner and eachWlock independently
would lose precisely the$\delta$correction.

The remaining caller budgets also follow from actual subsets:

- $D-W+G_*\subset P_+$. OldDpoints cannot acquire a new residual junction,
  since originalGwas defined by all paths in the full$P_+$. Each added$G_*$point
  cannot start a blue5inside this set: append the last vertex's actual$p$to get
  an ambient blue6whose required second lock lies in deletedW. Thus the set
  satisfies the realDconditions, yielding$g\le120-d+w$.
- $H\cup(D\setminus(W\cup S))$has no red7and isC8, so
  $e=|D\setminus S|\le h+w$.
- Splitting actual$S\cap S_{B6}$intoH, M, and
  $D\setminus E_{R6}(D)$gives$b\le g+m+56$.

On the common5-by6outgoing chart, total holes are$462-n$, double-extreme holes
are$84-|S|+b$, and no-extreme holes are at most$226-n+|S|$using the same126-state
face capacity100. The126ordinary eleven-state rows give

$$504\le(462-n)+5(84-|S|+b)+4(226-n+|S|),$$
$$5b\ge5n+|S|-1282.$$

Since$n=187-h+d$and$|S|=g+d-e\ge g+d-h-w$, combining the three budgets gives

$$10d\le1107+6h+5\left\lfloor\frac{3+5h}4\right\rfloor.$$

For$h=1,2,3,4,5,6,7$the resulting population bounds are respectively
$298,298,298,298,299,299,299$. For$h\ge8$, the already established$d\le120$
gives$n\le307-h\le299$. The$h=0$case is covered by the earlier stronger macro;
even the weaker displayed inequality gives$n\le297$. Thus the claimed new
Q299/F300/ES301chain follows from these stated imports. This internal check
finds no lost actual-path premise or duplicated cost in the common-budget step.

## 11. Preserved independent ordinary-capacity work after caller release

The caller released this branch from waiting for ordinary63because its stronger
macro independently achieves the requested numerical goal. At the actual
[04:15:41UTC snapshot](../SOURCE_MAP.md#excluded-sources),
[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]
16actual threads and177134508kBRSS. Its parsing took311860msand forward pass
706326ms. No terminal verdict or independentGRATchkexisted yet. Both detached
controllers and automatic terminal receipts remain unchanged and preserved.
