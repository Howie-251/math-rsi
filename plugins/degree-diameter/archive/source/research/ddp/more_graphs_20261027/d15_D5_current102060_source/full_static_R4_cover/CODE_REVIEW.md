# Read-only full-static model review

No blocking issue was found in `worker.py`, `run.py` and the frozen prediction. The cache formats and padding were checked separately in `../CACHE_INTERFACE_REVIEW.md/json`. This reviewer did not build the model, call a solver or run BFS.

Every one of the810 cached ball columns is unpacked with little bit order and sliced to all102060 real target IDs. Each column also includes cardinality row102060. The full CSC row counts must equal the saved support for every target, with810 entries in the cardinality row. There is no sampling, active-row subset, constraint-generation loop or repeated deduplication.

The LP uses negative cover coefficients with right-hand side−1 and positive cardinality coefficients with bound15. The integer model then uses all positive coefficients, target lower bounds1 and cardinality upper bound15 over810 binary variables. This is precisely the complete retained-edge R4 cover question.

The eligible-label order and actual102060 CSR header/degrees are checked. The incumbent gate rounds only near-binary values, requires distinct pins and at most15 of them, checks actual free degree in CSR, and tests the complete cached-ball OR across all102060 targets. Only then does it export all old edges plus the new spokes. No old-source BFS or additional ball calculation is needed.

Thread environments are set to1 before numerical imports, and both HiGHS calls pass threads1. The code matches the frozen130 aggregate CPU,25 preparation and95 combined solver allocation: worker soft/hard CPU127/128, one20-second LP, at most one MIP capped by75 and the measured remaining allowances, with one200-second parent wall guard. Actual observed CPU remains a separate terminal measurement. Interrupted/no-incumbent runs remain UNKNOWN; raw solver infeasibility is not promoted to a strict theorem.

This is an implementation review, not a prediction of solver success or a numerical result. Parent owns any independent first-parameter graph acceptance.
