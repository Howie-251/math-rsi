# Original twenty-three-point projection without x2 silence: checked UNSAT

This comparison removes exactly the predicate that x2=10 cannot end blue five; all other original twenty-three-point conditions and physical labels are unchanged. It is **checked UNSAT**. Independent clause-set reconstruction passed; the formula has 2530 variables and 620082 clauses, 125 fewer distinct clauses than the original. CNF SHA-256: `cad467e663031fbcd3a1972ab77e4a8f4b488b7b387484c4b2452fd9bf2a7df7`.

Kissat exited 20 in 2.470 seconds. The original DRAT check exited 0 with `s VERIFIED` in 1.317 seconds; no timeout occurred. [result.json](result.json), [check.stdout](check.stdout), [schema-audit.json](schema-audit.json) and [runtime.json](runtime.json) retain the actual commands and bindings. [SCOPE.md](SCOPE.md) records the exact sole-predicate difference.

The separately checked trimmed core contains 174 original clauses. [core.cnf](core.cnf) is 3314 bytes, SHA-256 `6320c902c3fa43f901dda92ca41d2b44ff400651217cb83d04dad1117e4dc47e`; [core.drat](core.drat) is 7720 bytes, SHA-256 `d3f57e2b18b03a7ba47a5c51e930a53bc658c21eba6d76a03672aa10e2f88d71`. Its recheck exited 0 with `s VERIFIED` in 0.065 seconds. [CORE.md](CORE.md) gives each clause's physical literals and original CNF number; [core-translation.json](core-translation.json) is the machine-readable translation.

The 174 groups are: weak R6+B3 17; weak R5+B4 13; no R7 26; red-six endpoint implication 24; red-five implication 12; packet 24; necessary blue fans 9; a4 terminal cut 3; frozen-red units 17; A no-in-B4 8; no B6 4; T no-B5 endpoints 4; no T-to-T B4 11; B no-out-B4 2. The removed private-x2 predicate is not used.

The finite exclusion still retains the other blue-fan and right-arm assumptions. Any claim that every ambient a4 red six must end at c requires a separate proof that a route ending before c extracts this entire predicate without relying on x2 silence. This report makes no unproved transfer, global bound or external-review claim. The [final manifest](final-bindings.json) binds the completed evidence. No new SAT experiment follows this comparison within the sealed four-case package.
