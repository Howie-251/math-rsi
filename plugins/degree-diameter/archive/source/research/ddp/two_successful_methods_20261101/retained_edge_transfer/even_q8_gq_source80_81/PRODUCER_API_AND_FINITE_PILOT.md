# Actual producer API and minimal finite proof proposal

Actual producer call,already completed once by the bounded root-authorized run:

```
produce_sources derived derived/TABLES_INPUT.txt derived CPU_LIMIT
produce_sources balanced balanced/TABLES_INPUT.txt balanced CPU_LIMIT
```

The ten header integers are np,nl,a,b,J,oldn,oldm,filledn,filledm,delta. Then come nl rows of a point labels,np rows of b line labels,J spread-line ids,and np owner indices. `prepare_inputs.py` reads only fresh incidence/spread files and makes the deterministic transpose/owner table;it does not rebuild field,geometry or projections.

Derived labels are the new512/640 ids. Balanced's isotropic `line` ids are0..584,not row numbers among all4745RREF subspaces. Both cases use oldlabel p*nl+l;the output header and exact table dimensions are checked by the writer. All129helper pins are written with explicit helper index;row number is not used as an implicit owner.

## Minimal existing generic interface

Read-only source: `formal/DegreeDiameter/Portfolio/OppositeIncidenceSpreadFamily.lean`,namespace `DegreeDiameter.Portfolio.OppositeIncidenceSpread`. Its `order_degree_and_exact_D3` returns card,degree<=a*b,actualWalkD3 and nonD2. It requires:

1. Explicit e:Old≃Point×Line,with Old=Fin327680 or Fin342225 and label p*nl+l.
2. Literal linePoint:Line→Fin a→Point,pointLine:Point→Fin b→Line,spread:Fin J→Line,and spreadOwner:Point→Fin J.
3. ha:a>0.
4. hline:Inc(p,l) implies some pointLine slot equals l.
5. howner:Inc(p,spread j) implies j=spreadOwner p.
6. project:for all p,l,some q,m satisfy Inc(q,l),Inc(p,m),Inc(q,m).
7. A concrete cardinal inequality1+a*b+(a*b)^2 < np*nl+J.

No new field axioms or full GQ uniqueness formalization is needed by that conditional interface. Each finite premise must nevertheless be kernel-proved for the actual new tables before an unconditional concrete source claim;a fresh external receipt cannot be imported as an axiom/certificate premise.

hline can use per-incidence inverse-slot positions:5120derived and5265balanced checks. howner needs only each spread-line point slot:512derived and585balanced checks. The full projection domain is512*640=327680 and585*585=342225 point/line pairs. Existing CSVs give nonincident q,m;incident pairs use q=p,m=l. A compact certificate records the line-slot of q,connector line m,and the connector slots of p and q,so three literal memberships are kernel-checked. The external uniqueness/field checks need not be repeated.

The generic result proves an upper degree bound,not all-vertex regular equality. Actual artifact counters already establish80/81regularity externally. A future formal regularity theorem would additionally need slot injectivity/exact incidence structure;it should not be claimed as a consequence of this minimal interface alone.

## Two-module cost pilot proposal,not executed

If root chooses formal work later,first allocate only30CPU seconds total to two new modules,each<=15CPU: (A)new literal Definitions with both real carriers/labels and small incidence tables; (B)a finite Pilot proving representative hline/howner entries and fixed-point/first16-line projection chunks for each case. Read the small subset of existing CSV witnesses,not another field or geometry enumeration. Use pinned Lean4.24.0,explicit LEAN_PATH,and only new output modules.

This is a proposed budget,not a measured timing. Its output would be actual definition/import cost and finite-check cost needed to estimate the remaining669905point/line domain. It would not itself close either original source theorem. Any larger chunk plan requires that measurement and a separate root decision;no long proof queue or9000CPU batch is started. No Lean file or olean has been produced by this preparation.
