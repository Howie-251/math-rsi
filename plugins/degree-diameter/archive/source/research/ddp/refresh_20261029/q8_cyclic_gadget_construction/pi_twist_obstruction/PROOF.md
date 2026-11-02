# Fixed pi-twist cyclic auxiliary family cannot have diameter three

## Scope and claim

Let vertices be `(a,l)` with a in Z8 and l in F2^3. Retain the three cube edges `(a,l)--(a,l XOR i)` for i=1,2,4. Let

    pi = [3,4,7,0,1,6,5,2],
    sigma(a,l) = (a+delta_l, pi(l)),

and add sigma and its actual inverse as undirected neighbors. Here the eight delta values are arbitrary elements of Z8. The permutation pi preserves label parity, is an involution, and changes two bits: it adds3 at even labels and5 at odd labels.

**Claim:** no choice of the eight delta values gives diameter at most3. This includes every legal degree5 cross-pencil member; zero voltages or duplicate external neighbors do not evade the obstruction. The result concerns this fixed pi, the fixed cube edges, and the Z8 deck only. It does not exclude other pi, arbitrary cross-pencil2-factors, or the q8 fiber-extension method.

The proof uses one exact441-entry sumset table and a paper classification of short words. No delta assignment, graph, or BFS was enumerated.

## 1. Exact finite sumset lemma

There are21 three-element subsets of Z8 containing0. For two such sets A,B,

    A+B=Z8

holds precisely when one set belongs to

    F1 = {{0,1,2}, {0,1,7}, {0,6,7}}

and the other belongs to

    F3 = {{0,2,5}, {0,3,5}, {0,3,6}}.

The two orders are allowed. Thus there are18 ordered full-sumset pairs. F1 comprises the three-term arithmetic progressions containing0 with step±1; F3 similarly has step±3. None of these six sets contains two elements differing by4.

`check_sumsets.py` proves this finite statement by listing every `(0,a,b)` with1<=a<b<=7, evaluating all nine pairwise sums for each of the21² ordered pairs, and recording the exact sumset. It verifies equality with the displayed eighteen pairs, not merely an upper bound. The complete table is `SUMSET_TABLE.jsonl`; `RESULT.json` lists all successful pairs. The table's CPU cost was0.011398719 seconds. This is a finite computational lemma, not a Lean-formalized theorem.

## 2. Antipode coverage forces the lemma at every label

Put

    D_l = {delta_l, -delta_pi(l)},
    A_l = {0} union D_l.

An external step from label l has phase increment in D_l. Since pi is an involution,

    D_pi(l) = -D_l,       A_pi(l) = -A_l.

Write I for a cube step and E for either external orientation. An antipodal target label is `l XOR7`. Let

    r = l XOR2 if l has even parity,
        l XOR4 if l has odd parity.

Equivalently r=pi(l) XOR1. The only possible words of length at most3 ending at that label are:

- III, using each of the three different cube flips: phase0;
- EI: phase in D_l;
- IE, whose first flip reaches r: phase in D_r;
- E I_1 E: phase in D_l+D_r.

E preserves parity and I reverses it. This excludes the other parity types; IEE and EEI change only one bit because pi²=id. In EIE the required middle flip is1. Hence the complete antipode phase set is exactly

    {0} union D_l union D_r union (D_l+D_r) = A_l+A_r.

Diameter at most3 therefore requires A_l+A_r=Z8 for every l. If either set had at most two elements, its sumset with a set of at most three elements would have at most six elements. Thus every A_l has exactly three elements, and the finite lemma applies to every A_l.

Equivalently the eight conditions reduce to the four previously identified conditions

    A0+A2=Z8,   -A0+A1=Z8,   A1+A5=Z8,   A2-A5=Z8.

We do not assume the special parameterization of the single earlier candidate: the argument applies to every delta assignment satisfying these necessary conditions.

Since no A_l contains a pair at difference4, and its elements are0,delta_l,-delta_pi(l), necessarily

    delta_l != 4,
    delta_pi(l) != 4,
    w_l := delta_l+delta_pi(l) != 4        (all modulo8).

The same applies at every label. Negating a residue cannot produce4 unless it was4 already.

## 3. Complete same-label short-word classification

We now seek paths from `(a,l)` to another vertex with the same label l. The possible words of length at most3 are classified as follows.

| Length/type | Possible phase increments |
|---|---|
| Empty |0 |
| One step | none returns to l |
| II |0, using the same cube flip twice |
| EE |0, w_l, -w_l |
| EII |D_l; the two distinct cube flips undo pi(l) XOR l |
| IIE |D_pi(l)=-D_l |
| IEI |D_j union -D_j, for the pi edge between two cube neighbors of l |

Here choose `j=l XOR1`. If l is even, `pi(j)=l XOR4`; if l is odd, `pi(j)=l XOR2`. These are the only two cube neighbors of l that pi pairs. Both orientations are included, yielding D_j and D_pi(j)=-D_j.

This list is exhaustive. At length two, IE and EI change parity and cannot return. At length three, III and all types with two E steps change parity. EEE ends at pi³(l)=pi(l), which differs from l. The remaining three types are precisely EII, IIE, and IEI. Repeated cube flips are included where they can return; no nonbacktracking assumption has removed valid walks.

Therefore the exact same-label phase set is

    {0} union {±w_l}
        union {±delta_l, ±delta_pi(l)}
        union {±delta_j, ±delta_pi(j)}.

By Section2 none of these values is4. Thus `(a,l)` cannot reach `(a+4,l)` in at most3 steps whenever all antipode conditions hold. If an antipode condition fails, diameter at most3 already fails. This dichotomy proves the claim for every delta assignment. ∎

## Consequence and boundary

The earlier explicit candidate covered every antipode phase yet missed `(4,0)` from `(0,0)`. The proof explains that failure as a fixed-pi obstruction, not a poor choice of the eight voltages. This entire pi-twist family stops; orientation reversals, further voltage assignments, or another seed within it cannot repair the halfturn target.

The obstruction does not transfer automatically to a permutation with3-cycles: an EEE word there can return to the original label and can carry an independent cycle-voltage sum. No such new permutation or candidate was evaluated in this task. Theorem1 of the cited Rajiv paper remains the underlying sufficient fiber-extension theorem; this auxiliary obstruction is not a new version of that theorem.
