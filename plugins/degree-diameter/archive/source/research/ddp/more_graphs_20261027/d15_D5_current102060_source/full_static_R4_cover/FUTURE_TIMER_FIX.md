# Future-only solver-stage CPU timer correction

The only executed model run used `worker.executed.py`, preserved before editing. `worker.py` now contains a future-only timer correction; it has not been run or tested, and no further solve is authorized by this edit.

The recorded first run set the whole-worker soft/hard CPU limits127/128 and passed internal time limits to the two solver calls. Those internal limits did not return the MIP call before the intended95CPU sub-budget. Total observed aggregate CPU128.11086108799998 remained below130, but the solver-stage sub-budget was not separately enforced. See BUDGET_COMPLIANCE.json.

The future change records CPU at the start of the combined LP/MIP stage and sets an OS soft deadline no later than that start+95CPU. During native calls SIGXCPU uses the OS default termination action, rather than a Python handler that can be delayed until the native call returns. Core output is disabled. The global hard limit remains128; after solver return the normal127/128 limit and Python handler are restored for literal checking/export. Driver fallback preserves UNKNOWN on a phase termination. This code change adds no actual run, solver call, calibration or changed outcome to the first model receipt.

The existing CODE_REVIEW predates this timer edit and applies to the executed model logic preserved in worker.executed.py. No additional review, solve or calibration was requested or performed for the future timer change.
