# Actual715: no fixed-old-induced diameter3 extension at cap11

2026-11-01. **Supported paper deduction with actual local finite premises; STOP this precise scope.** This is not a theorem about all(11,3)graphs or a Lean result. It applies to the exact published715 literal with all old induced adjacencies fixed: no old edge deletions or additional old-old edges. The nonempty finite helper set and its internal graphH are arbitrary, as are allowed helper spokes. No helpergraph search was run.

## Actual input and new finite support

Inherit the actual source and195 eligible target-class certificates from `d3d4_transfer/RESULT.json`:520 vertices are saturated degree11; the other195 form65 P3 classes, each sharing8 core neighbors. Every eligible pin reaches eligible old targets in only its own class within2 old steps. Core owner sets N_i partition the520 core vertices into65 sets of8.

The original degree8 independent-triple guess was refuted by this literal. The P3 center has degree10 and its two leaves degree9; oldsource m3770. The preceding P10 proof did not use the false independent model.

The only new numerical support in this stronger scope reads715 adjacency once and expands CORE reachability for one canonical member of each65 class. No oldD3 BFS or old585/Steiner computation is repeated. The resulting T_i have size72. Their intersections with owner sets satisfy

    |T_i∩N_j| =8 if i=j, and1 if i≠j.

For each core targett let S(t)={i:t∈T_i}. The520 literal sets are distinct9-subsets of65 classes and form3-(65,9,1): each single/pair/triple occurs72/9/1 times. This directly establishes the needed715 premises; no equality to a separately saved585 file is assumed. Because the three members of each actual class have the same core neighbors and their only eligible-old neighbors remain in that class, they have the same two-step CORE set T_i.

The small partition check records22 partitions of8 and29 partitions of9 with at most8 positive entries. It proves the moment maxima5 and6 used below. These are finite integer partitions, not helpergraph samples or a solver run.

## Routes and the minimum helper degree

Suppose an extensionJ exists with maximum degree≤11 and diameter≤3. Old induced graph is exactly the715 source. Choose h of minimum degree r inH. Then0≤r≤11. Its distinct own pin classesA have size

    a=|A|≤11−r.

EveryH-neighbor also hasH-degree≥r and hence at most11−r old pins. LetB be the union of the classes pinned by these r neighbors. Thus

    |B|≤r(11−r).

Core vertices are already saturated, so no helper is adjacent to a core vertex. A≤3 route fromh to a core targett can only enter old immediately at a pin inA and use≤2 old steps, or first traverse oneH-edge and enter old at a neighbor's pin with one old step remaining. A path h–oldpin–helper–t or h–helper–helper–t would require a helper-to-core edge and is impossible. Shared old pins therefore introduce no missing route.

Consequently every core target must satisfy

    S(t)∩A≠∅, or owner(t)∈B.

Call an outside owner class i∉A **bad** if one of its8 core targets has S(t)∩A empty. Every bad class must be inB. We will show that too many bad classes exist for every possible r/a.

## a≤7: every outside owner is bad

Each selected class contributes exactly one hit to another owner's8 targets. Hence, for i∉A,

    sum_{t∈N_i} |S(t)∩A|=a.

If a≤7, at least one of those8 targets is missed. Thus65−a≤|B| would be necessary. But

    a+|B|≤(11−r)(r+1)≤36<65.

This excludes a≤7, in particular every r≥4.

## r0 and r1: third-order design bound

The three-design gives the inherited inclusion-exclusion upper bound

    U(a)=72a−9*C(a,2)+C(a,3)

for own two-step core coverage. U is increasing for0≤a≤11. If r0 then a≤11 and own coverage≤U(11)=462<520. If r1 then a≤10, |B|≤10, and total core coverage≤U(10)+8*10=435+80=515<520. Neither case works.

## Exact outside-class moment

Only r2 with a8 or9, and r3 with a8 remain. Put k_t=|S(t)∩A| and f(k)=C(k,2)−C(k,3). The design gives

    sum_{all core t} f(k_t)=9*C(a,2)−C(a,3).

Inside a selected owner's class i∈A, k_t=1+q_t and sum_{t∈N_i}q_t=a−1. The identity

    f(1+q)=q−C(q,3)

therefore gives selected-owner total2*C(a,2)−Y, where

    Y=sum_{i∈A} sum_{t∈N_i} C(k_t−1,3)≥0.

Subtracting proves the exact identity

    sum_{owner(t)∉A} f(k_t)=7*C(a,2)−C(a,3)+Y.

This uses ordinary binomial counts of the already bound715 design, not a presumed ideal geometry.

### a8

Each outside owner has8 nonnegative hit counts summing8. If fully covered they are all1, so its moment is0. Any such8-count partition has moment at most5, achieved by3+3+2. The total outside moment is at least7*28−56=140. Thus at least ceil(140/5)=28 outside classes are bad.

For r3, |B|≤3*8=24; for r2, |B|≤2*9=18. Both are smaller than28.

### a9

Each of the56 outside owners has8 nonnegative hit counts summing9. A fully covered class has pattern2+1+1+1+1+1+1+1 and moment1. An arbitrary class has moment at most6, achieved by3+3+3. If b classes are bad, the outside total is at most56+5b, while the exact identity bounds it below by7*36−84=168. Therefore

    b≥ceil((168−56)/5)=23.

Here r2 and |B|≤18, again impossible.

All r0..11 and all distinct own-class counts have now been covered, including repeated pins in the same class (which cannot enlargeA or T-unions). Every proposed nonempty helper set has a minimumH-degree vertex, so no finite size or topology ofH escapes this argument.

## Conclusion, cost and exact limit

No nonempty helper extension retaining this715 as its **fixed old induced graph** can have maximum degree≤11 and diameter≤3. This is stronger than the preceding Petersen10 obstruction and the older t≤5 spoke bound, and directly answers the simultaneous helper-to-core necessary cover question for this fixed-induced append rule: it is impossible.

The claim does not allow adding old-old edges or deleting/replacing old edges. Either would change the old two-step sets and invalidate the route/design application. Other715 sources, arbitrary rewiring and generalN(11,3) remain outside the statement. No numerical optimum or global best/priority assertion is made.

New finite support CPU0.053918seconds, plus prior metadata process0.035727 gives measured0.089645/20. Brief local report/code preparation is not individually metered. Exactly one715 adjacency parse,65 canonical two-step CORE expansions, zero full/sourceD3BFS, zero old585 checks, field/solver/Lean/remote calls, and zero new graphs/parameters. All processes are terminal. No alternativeH search or degree/source ladder follows.

Evidence: ARBITRARY_HELPER_PRED.md, check_core_support.py, CORE_SUPPORT_RESULT.json, CORE_SUPPORT_DATA.json, ARBITRARY_HELPER_RESULT.json, RESULT.json, TERMINAL.json. The preceding P10-only analysis is preserved as PETERSEN10_NOTE.md and PETERSEN10_RESULT_HISTORY.json.
