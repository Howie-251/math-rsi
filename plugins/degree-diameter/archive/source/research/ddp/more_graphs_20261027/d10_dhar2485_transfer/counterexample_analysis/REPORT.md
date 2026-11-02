# Dhar2485 transfer: kernel overlaps are real; the proposed nonfaithful-capacity obstruction is refuted

P1 was refuted. The original normalized five-pair phase pattern has enough free-voltage forms for both frozen targets: every order5 action in F101 has minimum capacity182>101, and every order7 action in F113 has minimum182>113. Therefore these fields are not excluded by this route-count argument. This does not imply that any translation assignment covers them. The only controlled generator change, Dphase7 to8, splits the named forced overlaps and raises the minimum capacities; P2 was supported. No graph, fixed-polynomial endpoint test, adjacency expansion or BFS was run.

The recommendation is to demote unchanged C35 transfer from priority1 unless a concrete full-coverage argument appears. Underexploration and sufficient form counts do not supply such an argument. The central C25/F101 fixed-action finite projective test is a separately controlled decision chosen by the parent; this report does not add a phase, prime, seed or solver grid. Its outcome should be consumed before another change is proposed.

## Source and closed-scope separation

The known2485 source is C35 semidirect F71, not5*497. The stored convention is

    (i,x)(j,y) = (i+j mod35, x*r^j+y modp),
    (u,b)^(-1) = (-u,-b*r^(-u)).

At p71 the original action is2, of order35, with generators(18,57),(12,66),(29,12),(33,22),(14,27) and their inverses. Relabel phase in units of2 and take the generator ordering oldD^-1,oldC^-1,oldB,oldE,oldA. The normalized phases are[1,3,6,7,9] with actionr=4. Conjugating by translation18 gives voltages[0,15,54,67,1], exactly the recovered polynomial rule[0,r^2-1,-r^2-1,-r,1] at r4 modulo71. This algebraic normalization uses no source graph reproduction.

Before computation, the ledger's relevant metacyclic and closed D8 scopes were read. They cover specified C20/degree8 phase patterns, primitive and nonfaithful p61 actions, the fixedr2 CRT translation scopes, two-involution and parallel-phase patterns. The D5 two-copyC5 cyclotomic transfer is also a different finite scope. None excludes this five-inverse-pair C35 source. SCOPE_READ.json lists the exact separation. No closed D8 run was resumed.

## Four-step forms and the frozen tests

Letters A,B,C,D,E denote phases1,3,6,7,9; lowercase letters are inverses. Enumerate only reduced words of length at most4, forbidding adjacent inverse cancellation. There are1+10+90+810+7290=8201. This loses no reachable endpoint, since an immediate inverse pair cancels in every group instance.

For any word, the fiber endpoint is a linear form in its five generator voltages. A positive letter contributes its voltage times r to the suffix-phase power; an inverse contributes minus its voltage times r to(suffixphase minus its positive generator phase). These forms are reduced exactly in Z[r]/Phi_d(r) for action orders d5,7,35. The retained coefficient vector distinguishes a universal route form, not an evaluated endpoint. Two different forms can still collide after choosing voltages.

The frozen P1 predicted that actionkernel overlaps would force the minimum below101 for order5 or113 for order7. P2 predicted that changing only D's phase7 to8 would split the named overlaps and increase the minimum. Both patterns retain all five free voltages and the same C35 quotient. The finite-field checks cover all four primitive5roots in F101 and all six primitive7roots in F113. They evaluate coefficient forms only; they do not repeat the source agent's fixed quadratic-voltage transfer. No mod127 case or C25 case was evaluated here.

| Pattern | Action order | Minimum universal form count | Tight phases | Minimum in frozen finite field |
|---|---:|---:|---|---:|
|Original[1,3,6,7,9]|5|182|15,20|182 for all4 roots in F101|
|Original[1,3,6,7,9]|7|183|7,28|182 for all6 roots in F113|
|Original[1,3,6,7,9]|35|211|15,20|Not evaluated here|
|Only D7to8|5|197|5,30|197 for all4 roots in F101|
|Only D7to8|7|196|7,28|196 for all6 roots in F113|
|Only D7to8|35|216|17,18|Not evaluated here|

The action7 coefficient evaluations in F113 create one additional minimum-layer coincidence beyond the universal cyclotomic forms. All finite minima still exceed their field size, so P1 is explicitly false. The counts are necessary upper capacities only: they do not establish a complete graph or justify full free-parameter search by themselves. Cyclotomic reductions here apply to the specified primitive roots in prime fields; no unjustified primitive-cyclotomic relation is imposed on mixed CRT actions, a failure already noted in the old D8 ledger.

## Concrete collisions and what the control changes

For an action of order d, elements whose phase is divisible by d form an abelian subgroup: both action multipliers are1, so their fiber coordinates simply add. This gives explicit source-pattern collisions for every voltage choice.

At order5, C*a has phase5 and D*B has phase10, hence

    C a D B = D B C a,

in phase15; inverse words give phase20. This is precisely on the original thin phase pair. Changing offsets cannot split this universal identity. Replacing Dphase7 by8 makes the second block's phase11, so the difference of those two routes becomes

    (1-r^(-1))*(x_C-x_A),

in phase16, a nonzero free-voltage form. Moving D by5, such as7to12, would leave the kernel reason intact and therefore is not a repair of this collision. No such extra case was run.

At order7, D and A*C both have phase7, yielding

    D A C = A C D

in phase14. With only D7to8 the difference is

    (1-r)*(r^(-1)*x_A+x_C),

in phase15. Again the forced identity disappears for generic voltages, though particular parameters can still make the difference zero. WITNESSES.json stores all coefficient differences exactly in the relevant cyclotomic basis.

There is a further direct explanation of the faithful source's nearly tight phase15/20. With action order35 and Dphase7, D has order5 for every voltage: r^7 has order5 and its five-term geometric sum vanishes. Thus D^2=D^-3 and D=D^-4. Among words of length at most4, these account for exactly36 duplicate route forms: four uncontexted pairs, plus32 pairs formed by adding any of the other eight signed letters on either side of D^2 versus D^-3 or its inverse. The exact form enumeration has total excess36, so these known relations account for all universal duplicates. In phase15 specifically the four pairs are ADD/Addd, DDA/dddA, cdd/cDDD, and ddc/DDDc. Hence215 raw reduced words become211 forms; phase20 is the inverse counterpart.

D7to8 removes that forced order5 generator cycle. In the faithful35 universal ring, all8201 reduced words then have different forms within their phase, and the phase minimum rises to216. This is a genuine connecting-rule change, not an offset seed. It also explains why changing quotient order can matter: in the parent's C25 pattern all five phases are units, so Dphase7 no longer has the source's forced five-cycle. That structural observation supports the choice of a controlled quotient change, while making no claim about the parent's as-yet-separate endpoint decision.

## Decision and evidence limits

The analysis produced exact route overlap formulas and one successful capacity control, but no full-coverage construction. The p101/p113 free-voltage families remain open, and faithful p211 at the original phase minimum211 would require a collision-free evaluation on that thin layer. Capacity improvement alone is too weak a signal for priority1. The parent's single fixed C25/101 projective scope should finish its own exact finite decision before the strategy is reconsidered; this analysis does not authorize a new C35 grid or long solver.

The entire computation used1.114836 CPU seconds on one worker. RESULT.json contains every35phase capacity for both patterns and all frozen action-root evaluations; WITNESSES.json gives the concrete form identities; CYCLOTOMIC_FORMS.json records the coefficient conventions and exact moduli. No old baseline BFS, new graph diameter or ordinary bad-pair measurement is claimed. This finite counterexample/control task is terminal, and shared Wiki or central source-analysis files were not changed.
