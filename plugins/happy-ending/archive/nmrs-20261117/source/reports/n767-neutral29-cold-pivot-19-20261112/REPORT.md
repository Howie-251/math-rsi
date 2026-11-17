# Nineteen-point cold-pivot necessary domain: checked UNSAT

Date: 2026-11-12. This is a finite literal computation in one explicitly specified physical order. There was no external review. It is supplementary computational evidence; the later elementary argument in the [ordered-cold-arms research draft](../../.trellis/tasks/10-19-nr7-structure-capacity/research/N7_NEUTRAL29_ORDERED_COLD_ARMS_20261112.md) does not depend on SAT.

The requested model is **UNSAT, with a successfully checked DRAT proof**. The entire formula was independently reconstructed before solving, with zero missing or extra clauses. A 68-input-clause core and its trimmed proof were then extracted and independently checked again.

| Stage | Actual result |
|---|---|
| Independent full clause-set reconstruction | PASS, 1,482 variables and 172,219 distinct clauses |
| Kissat external solve | Exit 20, no timeout, 0.266 seconds |
| Original `drat-trim` check | Exit 0, `s VERIFIED`, no timeout, 0.918 seconds |
| Core extraction/check | Exit 0, `s VERIFIED`, 0.918 seconds |
| Standalone trimmed-core recheck | Exit 0, `s VERIFIED`, 0.166 seconds |

These are wall times recorded by the controlled-process wrapper. The checker also printed its own verification time of 0.872 seconds for the original proof and 0.129 seconds for the core recheck. No SAT witness was produced, and no SAT-coloring audit is claimed to have run.

## Exact finite model

The physical order is `1,...,19`, with `L=1..5`, `A=6..10`, pivot `10`, `B=10..14`, `T=6..14`, and `R=15..19`. The frozen red paths are `1..6`, `14..19`, `6..10`, `10..14`.

The model contains all rank-three packet clauses, forbids red seven and blue six, and forbids all actual same-endpoint weak-seven splits through `R6+B3`, `R5+B4`, `R4+B5`. It also imposes:

- No blue four ends in A; no blue four starts in B.
- No blue five starts or ends in T.
- No blue four has both endpoints in T.
- A red six ending before 10 cannot have its penultimate point in T.
- A red six starting after 10 cannot have its second point in T.
- The redundant red fan units `R(x,5,6)` for `x<5` and `R(14,15,y)` for `y>15`.

All paths range over the full nineteen-point domain. No local dual red-six anchors are required for every T label. No blanket prohibition of blue five is imposed. The ambient blue-five supplies are consumed only via the specified fan units; their full witnesses are not required to lie inside the nineteen points.

See [SCOPE.md](SCOPE.md) for the precise source-to-CNF lifting and reverse projection argument. Every physical triple has one color variable, true meaning red. The 513 extra variables are one-way endpoint flags for the three weak-seven splits, used solely for prohibitions, never for counting. Any coloring satisfying the stated predicates extends by canonical actual red-path-existence values.

## Bindings and retained evidence

| Artifact | SHA-256 |
|---|---|
| [probe.py](probe.py) | `31b2df446c100d221eef1988032b6e3073dfac8102f502802c875078f4c55cf1` |
| [verify.py](verify.py) | `770871da95427bcf7293e7823b5fb4f241568f6453a2c042f143f1da9db8ff7e` |
| [formula.cnf](formula.cnf), 3,819,357 bytes | `8ea8d3f1a358e780d0f4356cab734f80ed7677f7b7ba26e698bbc21d9d271365` |
| [proof.drat](proof.drat), 4,961,060 bytes | `bb114c4faea4b74cdd8c6c59b5fcf1c3e1884dddfbd21c100eb485bf3a5d490a` |
| [core.cnf](core.cnf), 1,184 bytes | `bdc831221a425c938b0997aff36f70c64cd614c33d1736531780e89f7e6e2303` |
| [core.drat](core.drat), 2,584 bytes | `78632f93ca7ff3424b2235aa2ff96d8eae21804d81c35f1210ee10e5b95c833f` |

The authoritative runtime is Linux with Python `/opt/anaconda3/envs/forktqiu3/bin/python3.12`. The actual solver and checker are:

- `/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat`, SHA-256 `c2e44161cd142694f2b612e0be2dcc59cb656df6d42f8713adc4d05b9a22f5fa`.
- `/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim`, SHA-256 `2f01df83916c158d7da43deefde1ea3ea60b19f5d636ae03f31042e88ef179e9`.

[result.json](result.json), [runtime.json](runtime.json), [schema-audit.json](schema-audit.json), [check.stdout](check.stdout), and [core-result.json](core-result.json) retain commands, statuses, timings, and bindings. The completed-file manifest is [final-bindings.json](final-bindings.json). `result.json` captured the wrapper's `run.stdout` before its final status line; the final manifest binds that completed wrapper log. All scientific source/CNF/proof/checker-log bindings were already complete and match their retained bytes.

## Small core and physical translation

[CORE.md](CORE.md) gives every core clause's original CNF clause number and physical triple/endpoint meaning. [core-translation.json](core-translation.json) gives machine-readable predicates and literals. This is a checked core, not a claim of a minimum unsatisfiable subset.

| Predicate in the core | Clauses |
|---|---:|
| Fixed red-path/fan units | 14 |
| No red seven | 14 |
| Packet | 9 |
| Red-six endpoint implication | 8 |
| Weak `R6+B3` | 8 |
| Red-five endpoint implication | 2 |
| Weak `R5+B4` | 2 |
| Early red-six penultimate restriction | 1 |
| Late red-six second restriction | 2 |
| A no incoming blue four | 2 |
| B no outgoing blue four | 3 |
| T no blue-five endpoints | 1 |
| No T-to-T blue four | 2 |

The core uses no no-blue-six clause and no `R4+B5` clause. This does not authorize removing the other clauses from the recorded full probe or changing its proof binding. The separately retained core formula and core proof provide the checked smaller statement.

## Reproduction and scope

Do not invoke `probe.py` in the completed directory: it is deliberately create-only. On Linux, the saved formula and proof can be checked without relaunching a solver:

```bash
/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim formula.cnf proof.drat -t 180
/data/ktqiu_hdd/math_agent/cadical-sc2025/build/drat-trim core.cnf core.drat -t 60
/opt/anaconda3/envs/forktqiu3/bin/python3.12 -B verify.py --schema
```

The bounded conclusion is nonexistence of the specified fixed-order nineteen-point necessary model. Applying it to an ambient input requires the mathematical extraction of those nineteen distinct ordered labels and every asserted constraint. It is not a standalone certificate for every seventy-five-point input, geometric realizability, or a global upper bound of 74. The research draft now supplies a stronger elementary local proof, so the finite result serves as an additional literal cross-check. Sources, formulas, proofs and existing sealed jobs elsewhere were not changed.
