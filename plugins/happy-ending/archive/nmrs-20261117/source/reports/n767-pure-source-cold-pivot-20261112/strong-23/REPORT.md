# Pure red-six source against a cold pivot: branch (i) checked UNSAT

Date: 2026-11-12. The weaker branch (i) is **UNSAT with a successful bound DRAT check**, after independent full clause-set reconstruction. No red six from p to c is assumed. The conditional branch (ii) therefore was not solved. No external review was invoked.

## Physical predicate

The physical order is 1..23. Freeze actual red paths `(1..6)`, `(6,7,8,9,15)`, `(9..14)`, `(15,16,17,18)`, `(18..23)`. The middle red six witnesses a strict early terminal for p=9, before the pivot c=15.

A0={6,7,8,15} consists of cold-in through labels; B={15,16,17,18} consists of cold-out through labels; T is their union and **does not contain 9**. Point p=9 is only a pure red-six source: the frozen gap path witnesses its source role, no R6 may end at p, and no B5 may end at p. It may end B4 or start B5. All packets, no R7, no B6, all actual same-endpoint weak-seven splits, the A0/B/T restrictions and the vacuous outer extrema are retained.

All former p-as-T/cold-in rules, the private-x2 no-in-B5 condition, both gap blue fans and the out-p terminal cut are removed. No complete R6(p,c) is required inside or outside the selected domain. See [SCOPE.md](SCOPE.md).

## Actual checks

| Stage | Result |
|---|---|
| Independent full normalized clause reconstruction | PASS; 2530 variables, 617089 clauses; zero missing/extra |
| External Kissat | Exit 20, no timeout, 3.924 seconds |
| Original bound DRAT check | Exit 0, `s VERIFIED`, no timeout, 1.468 seconds |
| Trimmed-core extraction/check | Exit 0, `s VERIFIED`, 2.120 seconds |
| Standalone core proof recheck | Exit 0, `s VERIFIED`, 0.065 seconds |

[formula.cnf](formula.cnf) is 15913449 bytes, SHA-256 `acac6b101e4eddef23a36b5e205deb938de807f6f05858fb4fe152c28ce9d2f9`. [proof.drat](proof.drat) is 24396002 bytes, SHA-256 `25818e3392e12f209f1b48ff8efc97dfe4e117e25fbbfb8bf0bb3fa25ab94443`. Commands, hashes and logs are in [result.json](result.json), [runtime.json](runtime.json), [schema-audit.json](schema-audit.json) and [check.stdout](check.stdout). The completed-file [manifest](final-bindings.json) records final controller log bytes; early receipts captured that log before its trailing status line.

## Core and purity dependence

The separately checked core has 205 original clauses. [CORE.md](CORE.md) gives original clause numbers and physical literal translation; [core-translation.json](core-translation.json) is machine-readable. [core.cnf](core.cnf) is 4282 bytes, [core.drat](core.drat) 12527 bytes. This is not a minimum-core claim.

The groups are: weak R6+B3 17; weak R5+B4 11; weak R4+B5 1; no R7 37; R6 endpoint implication 30; R5 implication 11; R4 implication 1; packet 45; pure-p no-in-R6 3; frozen red units 17; A0 no-in-B4 10; no B6 6; T no-B5 endpoints 8; no T-to-T B4 6; B no-out-B4 2. No gap fan, terminal cut or x2 restriction is present.

The three purity clauses forbid exactly these actual red sixes:

- `(2,3,4,5,6,9)`, core 139, original CNF 477374.
- `(1,2,3,4,7,9)`, core 140, original CNF 483548.
- `(1,2,3,4,5,9)`, core 144, original CNF 484520.

The core does not use the pure-source no-in-B5 clauses. It **does use** no-in-R6, so this evidence cannot be relabeled as a theorem for arbitrary red-six sources that may also be red-six terminals.

## Transfer boundary and branch (ii)

Any ambient configuration with the stated left red five `(a1,a2,a3,p,c)`, the three cold-in through points a1..a3, dual-cold through c, right cold-out red four, and actual external arms, extracts this physical order whenever a pure source p has an actual R6 ending strictly before c. Its four internal points and terminal lie strictly between p and c and are distinct from the marked arms. Thus the checked finite model excludes that strict early-terminal branch under the displayed complete assumptions.

The left virtual-fan lemma separately gives `chi(p,c,y)=B` for y>c, hence an R6 from p cannot end after c, by same-endpoint R6+B3. Together these facts leave only terminal c for the nonempty pure-source family in this configuration. The required mathematical lifting still includes the actual arm/role assumptions above; it is not a theorem about an arbitrary isolated pure source.

For a more general source p that is also allowed to be in E, branch (ii) may only consume an ambient R6(p,c) as the necessary red fan `chi(p,y,c)=R`, 10<=y<=14. It must not force its four internal points into the selected 23 points. No such overstrong local path-existence constraint was added here. Since (i) already excludes the pure-source early branch, no additional conditional solve was launched.

All scientific execution occurred on the authoritative Linux host using the existing controlled workspace Kissat and bound drat-trim; all sources are fresh snapshots. Recheck with `drat-trim formula.cnf proof.drat -t 180`, `drat-trim core.cnf core.drat -t 60` and `python3 -B verify.py --schema` on Linux. No global bound, geometric realization or external acceptance is claimed.
