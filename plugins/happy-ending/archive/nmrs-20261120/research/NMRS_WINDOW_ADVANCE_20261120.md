<!-- Publication excerpt: mathematical content retained; local paths/control-plane metadata redacted, links relocated. Original SHA256 in INVENTORY.json. Historical snapshots are superseded by HANDOFF.md. -->
# Fixed-width window advance: a stronger global coefficient

Latest strengthening: §6 uses the integer number of marked faces in every
nested window. It improves the finite values in §4 and yields a still stronger
uniform coefficient; the raw-seed coefficient below remains valid.

2026-11-20. This continues the endpoint-request proof in
[the integer-lift manuscript §§8–9](NMRS_WINDOW_INTEGER_LIFT_20261119.md).
The original signotope domain and its red/private-hole interfaces are unchanged.
All scientific execution below ran on authoritative Linux; no external review
was requested or performed. These are exact certificates for necessary
inequalities, not a capacity optimum or an external acceptance verdict.

## 1. New result and its original caller

For every original input of the fixed-width family with five columns and
height universe `[v]`, the existing ordinary-row and actual endpoint-face
bridges define the same nonblue-hole count `p` and private-hole count `q`.
The new certificate gives, for **every v >= 64**,

\[
\boxed{p\ge\left\lceil c_{64}\binom v4\right\rceil,
\qquad c_{64}=\frac{1462410989664619}{15884400011119080}
\simeq0.09206586264768775.}
\]

The previous coefficient was
`c_old = 62043237111/678755000000`. The exact positive difference is

\[
c_{64}-c_{\rm old}
=\frac{3622028078559363494297}
{5500824453850577115000000}>0.
\]

The existing ordinary-row inequality is

\[
(v+1)H\ge\binom{v+4}4+(v-4)p+4q.
\]

Thus, already with `q >= 0`, the new global formula is

\[
\boxed{N(v+6,7,v+3)\le\binom{v+6}5-
\left\lceil\frac{\binom{v+4}4+(v-4)
\left\lceil c_{64}\binom v4\right\rceil}{v+1}\right\rceil,
\quad v\ge64.}
\]

Equivalently `H >= c_64 binom(v,4) + O(v^3)`. This improves the quartic
deficit coefficient throughout the same infinite family; it is not merely a
new finite population value. It does not change the separate finite best
value at `v=44`, `N(50,7,47) <= 2103267`.

## 2. Exact seed predicate and all-face checks

For seed height `t`, put `B=t-4`. A nonnegative weight `w(i,j)` is permitted
when `i,j >= 0` and `i+j < B`. All legal four-face profiles are
`I,J >= 0`, `I+J <= B`. Define

\[
E(I,J)=\sum_{i<I}w(i,J)+\sum_{j<J}w(I,j),\qquad
P(I,J)=E(I,J)+(B-I-J)w(I,J).
\]

The normalized seed predicate is **E <= 1 and P <= 5 for every face**.
The total request weight is

\[
W_t=\sum_{i+j<B}\binom{t-2-i-j}{3}w(i,j),
\qquad c_t=\frac{W_t}{5\binom t4}.
\]

The existing [discovery code](../SOURCE_MAP.md#excluded-sources) was copied into
a fresh directory and run at heights `44,45,48,56,64`, with denominator
`10^10`. Existing sealed candidates and runtimes were preserved.

| t | Positive weights | All legal faces | W numerator | Final denominator | c_t |
|---:|---:|---:|---:|---:|---:|
|44|194|861|620434232504191|10000000000|0.09140768502687877|
|45|203|903|681166541880787|10000000000|0.09143481887053753|
|48|250|1035|890903386657064|10000000000|0.09157193819067366|
|56|365|1431|1686358484077567|10000000000|0.09182708399779830|
|64|468|1891|2924821979329238|10000000007|0.09206586264768775|

All final rows pass both the original integer checker and a separate
[independent accumulation checker](../SOURCE_MAP.md#excluded-sources).
The latter does not import discovery or the old checker: it distributes each
weight to every served face, accumulates integer costs, recomputes the
objective and all rational comparisons. Its
[primary output](../SOURCE_MAP.md#excluded-sources) binds each
certificate's SHA256. In particular the accepted 64-height certificate is
[normalized-a5-v64-repaired.json](../inputs/window/normalized-a5-v64-repaired.json),
[Process-control details omitted; historical mathematical status and receipts retain their separate scope.]
Its [old-checker output](../SOURCE_MAP.md#excluded-sources)
has `max E numerator = 10000000007` and
`max P numerator = 49999999993`, with denominator `10000000007`.

The unmodified 64-height floor **failed** exact feasibility: maximum `5E`
numerator was `50000000035`, exceeding `5*10^10` by 35. Its
[raw candidate](../inputs/window/rejected-v64.json) and
[FAIL report](../SOURCE_MAP.md#excluded-sources) remain
preserved. [repair64.py](../SOURCE_MAP.md#excluded-sources) keeps every integer
numerator and increases the denominator by seven, an exact uniform scaling by
`10000000000/10000000007`. This makes every red bound feasible; the private
bound had already been feasible and is weakened by scaling. All final
constraints were then rechecked. No floating objective enters the result.

Even the re-rounded height-44 certificate strictly improves the old
coefficient by `43288237/157850000000000`. For `44 <= v < 64`, the strongest
applicable row of the table can be used according to `t <= v`; each of these
five coefficients is larger than the former `c_old`.

## 3. Transfer to every larger actual input

Fix the **same** original input of height `v >= t`. On each naturally ordered
`t`-subset `U` of its heights, embed the seed weights. Let `R_U` and `Q_U`
count its actual distinct red and private marked four-faces contained in U.
The original endpoint-covering bridge and the all-face predicate give

\[
R_U+5Q_U\ge W_t.
\]

This uses each face's normalized bound; it does not import the finite union
certificate's red-hole cost. Every actual four-face is contained in exactly
`binom(v-4,t-4)` such U. Summing gives

\[
R+5Q\ge\frac{W_t}{\binom t4}\binom v4.
\]

By the unchanged original hole-to-face bridge, the same input satisfies
`R+5Q <= 5(p-q)+5q = 5p`. Thus
`p >= ceil(c_t binom(v,4))`. All quantifiers are over restrictions of one
actual input; no unrelated extremal realization is combined. The argument
requires no sampled larger-height enumeration.

## 4. Same-parameter gain against the old named row/union envelope

The comparison below is to the strongest integer consequence of the **named
existing normalized, row and correctly transported union inequalities**,
plus `0 <= q <= p`. It is not a claim of best capacity, of best literature
bound, or of optimality over every known structural inequality.

Write `V=binom(v,4)` and

\[
R_r=\frac{501410212499\,V}{10^6\cdot135751},\quad
R_u=\frac{502561846116\,V}{10^6\cdot135751},\quad
A=\frac{40}{v-4}\,40+
\left(1-\frac{40}{v-4}\right)\frac{41027820}{10^6}.
\]

The old seed constraints on the same p,q are

\[
40p+4q\ge R_r,\qquad Ap+(44-A)q\ge R_u.
\]

The factor A is exactly the existing complete-hole/partial-face mixture from
[§9.4](NMRS_WINDOW_INTEGER_LIFT_20261119.md); using a uniform cost 40 here
would be invalid. For an integer p define

\[
q_*(p)=\max\left(0,
\left\lceil\frac{R_r-40p}{4}\right\rceil,
\left\lceil\frac{R_u-Ap}{44-A}\right\rceil\right).
\]

We minimize the ordinary-row term `(v-4)p+4q` over integer p,q. At each of
`v=64,100,128`, its minimum is attained at
`p0=ceil(c V)`, `q=q_*(p0)`: indeed increasing p by one can decrease `q_*`
by at most `M=max(10,ceil(A/(44-A)))`, and the exact checker verifies
`v-4 >= 4M` and `q_*(p0) <= p0`. Hence the row term is nondecreasing
throughout the feasible integer domain. This is an exact integer
optimization of the stated envelope, not just substitution of an arbitrary
q or a favorable p. The independent checker also recomputes the existing
fractional eliminated formulas; their final H values agree here.

Use `c=c_old` for the old column and `c=c_64` for the new column:

| Original parameter | Old p0,q* | New p0,q* | Old H | New H | Old N bound | New N bound | Gain |
|---|---:|---:|---:|---:|---:|---:|---:|
|N(70,7,67)|58079,5917|58497,1737|66505|66634|12036509|12036380|129|
|N(106,7,103)|358430,36562|361011,10752|387660|389091|100953216|100951785|1431|
|N(134,7,131)|975135,99488|982159,29248|1034089|1038663|332825437|332820863|4574|

The new inequality uses the same original input and retains all old envelope
constraints. Consequently each displayed gain comes from the improved
normalized coefficient; it is not a sum of separate finite improvements.

## 5. Reproduction and execution receipts

Work directory on Linux:
`<private-artifact-root>`.
Interpreter: `<private-python-runtime>`; discovery SciPy
`1.15.3`. Run the exact replays there with:

```bash
<private-python-runtime> verify.py normalized-a5-v44.json normalized-a5-v45.json normalized-a5-v48.json normalized-a5-v56.json normalized-a5-v64-repaired.json
<private-python-runtime> independent.py
```

Successful discovery/check receipts:
[44/45](../SOURCE_MAP.md#excluded-sources),
[48/56 plus preserved raw 64 FAIL](../SOURCE_MAP.md#excluded-sources),
[repair and independent exact replay](../SOURCE_MAP.md#excluded-sources).
[Operational connection details omitted from this publication excerpt.]
[Operational connection details omitted from this publication excerpt.]
succeeded and the complete primary data were unpacked locally. See
[archive fetch](../SOURCE_MAP.md#excluded-sources) and
[the archive](../SOURCE_MAP.md#excluded-sources). No secret was copied to
this research directory.

The assigned mathematical advance and exact recomputation are complete.
External acceptance, a low-rank closed weight formula and capacity optimality
remain separate unproved obligations. No unrelated run was started.

## 6. Integer nested-window lift: additional finite and global gain

For every fixed actual h-window U, let `T(U)=R_U+5Q_U`. This is an integer,
although the request certificate W_h is rational. Therefore a checked seed
gives **T(U) >= ceil(W_h)**. Take `A_44=62044`, and for `h>44` define

\[
A_h=\max\left\{
\left\lceil\frac{h A_{h-1}}{h-4}\right\rceil,
\ \lceil W_h\rceil\ \text{if a retained seed at h is available}\right\}.
\]

The retained seed heights are exactly 44,45,48,56,64. To prove the recurrence,
delete each of the h heights in turn. Every actual marked four-face survives
in exactly h-4 deletions, with its red/private weight unchanged. Hence
`(h-4)T(U) = sum_{x in U} T(U\{x}) >= h A_(h-1)`; integrality gives the
ceiling. Thus for every actual input of height v>=44,

\[
\boxed{p\ge\left\lceil A_v/5\right\rceil.}
\]

This argument counts faces marked in the original input and then restricts
their support. It does not recompute incompatible roles after each deletion.

The h=64 direct seed gives `A_64=292483`. In particular the uniform coefficient
for every v>=64 can immediately be strengthened to

\[
c^*_{64}=\frac{292483}{5\binom{64}4}
=\frac{292483}{3176880}\simeq0.09206611518219134>c_{64}.
\]

The recurrence gives increasing normalized values
`c*_h=A_h/(5 binom(h,4))`. For any fixed h, transport its integer face bound
on every h-subset to obtain the uniform coefficient c*_h for all v>=h.
For h>=64 there are no further retained seeds, so each rounding step adds
strictly less than `1/(5 binom(h+1,4))`. The reciprocal-binomial identity

\[
\sum_{k=h+1}^{\infty}\frac1{\binom k4}
=\frac4{3\binom h3}
\]

proves a fixed-seed recurrence limit satisfying

\[
c^*_h\le c^*_{\infty}<c^*_h+\frac4{15\binom h3}.
\]

This is a ceiling-loss bound for this fixed seed family, not an upper bound
on the best possible coefficient or on future new seeds.

All steps h=44,...,1024 and the same integer row/union envelope from §4 were
computed with exact standard-library arithmetic on Linux. Fraction-based
ceilings were checked again by direct integer quotient formulas. Primary
[output](../SOURCE_MAP.md#excluded-sources),
[source](../SOURCE_MAP.md#excluded-sources), and
[actual exit0 receipt](../SOURCE_MAP.md#excluded-sources) retain
all integers, seed hashes and comparisons. The local output file is decoded
[Operational connection details omitted from this publication excerpt.]
transport, not a local scientific rerun.

| v | A_v | p lower bound | New H | New N bound | Gain against old published named envelope | Further gain over §4 c64-only method |
|---:|---:|---:|---:|---:|---:|---:|
|64|292483|58497|66634|12036380|129|0|
|100|1805108|361022|389098|100951778|1438|7|
|128|4910964|982193|1038685|332820841|4596|22|
|256|80465298|16093060|16511233|9883903109|95455|515|
|1024|20966536167|4193307234|4218466562|9562924688644|28830189|157580|

The old published named envelope here is precisely §4's old c plus existing
row/union inequalities and integer p,q. The **same integrality insight also
improves the old 44 seed**, so the checker separately applies this recurrence
using only its historical W44. Against that strengthened old-seed comparator,
the final H gains are 127,1411,4508,93573,28259503 respectively. This separates
new-seed gain from a new use of integrality; it is still not a best-capacity
claim.

At h=1024 the universal coefficient for all v>=1024 is

\[
c^*_{1024}=\frac{20966536167}{227725146880}
\simeq0.09206948136495588,
\]

and the fixed-seed recurrence limit is strictly below
`1014509831/11018958720 ~= 0.09206948285944754`. No new LP or SAT was run
for this strengthening.
