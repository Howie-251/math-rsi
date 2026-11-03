# SAT produced a complete3840-point20-regularD3 graph

> 2026-11-01最新验收补记：本图全部3840字面根独验已PASS；固定公式图完整Lean及独立import/type/axioms已PASS（标准3axioms），最终fresh Gemini C实际SUCCESS/PASS。详见[完整编译证据](formalization/FINAL_COMPILE_RESULT.json)与[真实最终审阅](../reviews/F4_FINAL_C_DISPOSITION.md)。以下“pending root”等是生成批次当时的历史，不构成当前在途任务。全球纪录状态仍未认证。


One finite edge-dependent projectivity model produced a complete graph:
**n3840, m38400, simple undirected20-regular, diameter exactly3 by the full
route certificate**. This is90 vertices more than the existing local3750
instance at the same degree and diameter. Independent graph validation is
pending root; latest global record and Lean status are not claimed.

The global five-matrix F4 domain had failed. Here each of150 undirected
controller edges chooses its own map, with the actual inverse on the
reverse dart. This releases a real compatibility constraint, especially on
the self-inverse controller port4. The controller and common conic directions
remain fixed. No new controller, field or random seed was tried.

Preparation PID2258128 produced7200 selectors,14250 total variables and24450
clauses. After a static semantic review, the only solver call was driver
PID2267162 / CaDiCaL PID2267165, return10/SAT. Solver CPU was0.233523 seconds;
recorded preparation+driver+solver CPU was1.609514885 seconds, within the
whole60CPU budget. There were zero observation timeouts and no restart.

SAT acceptance rechecked the literal complete CNF, all300 dart inverses and
line mappings, all300 five-plane pencils, and one full-rank three-word for
each of3300 nonadjacent/equal controller pairs. It then generated all3840
adjacency sets and checked degree20, no loops and reverse adjacency. No
producer graph BFS or old-source BFS was run.

Artifacts:

- `graph_d20_D3_n3840.edges`: full headered edge list.
- `PARAMETERS.json`: controller, five directions and all300 dart matrices.
- `generate.py`: standalone deterministic reproduction from those parameters;
  source only, not run a second time.
- `ROUTE_CERTIFICATE.json` and `PROOF.md`: full finite and mathematical
  all-pair route proof.
- `model.cnf`, `SELECTOR_MAP.json`, `PAIR_COVERAGE.json`, `INPUT.json`,
  `MODEL.json`, `MODEL_CODE.md`: exact finite synthesis scope and encoding.
- `solver_solution.txt`, `solver.log`, `SOLVER_HANDLE.json`, `TERMINAL.json`:
  actual single-call result and CPU/return data.

The batch is terminal. Root has been notified to arrange the sole independent
graph verification and current public comparison. No continuation is started.
