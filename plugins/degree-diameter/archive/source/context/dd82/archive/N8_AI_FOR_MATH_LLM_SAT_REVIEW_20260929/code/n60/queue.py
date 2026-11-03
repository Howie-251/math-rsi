"""Use the existing queue, telemetry and coverage without changing old runs."""
from __future__ import annotations
import os
import sys
from sat58.jobs import run_branch_queue as base
from sat60.round11 import queue as previous
from sat60.round13.queue import Round13Queue
from sat60.round13.progress import coverage, export
from .contract import VERSION, REVISION


class Round13R02Queue(Round13Queue):
    def _start_session(self):
        if self.manifest_payload.get("encoding_version") != VERSION:
            raise ValueError("not a frozen r02 input; do not resume an r01 run with r02 code")
        previous.Round11Queue._start_session(self)
        tasks = self.manifest_payload["tasks"]
        self.session.update(research_round="Round13", encoding_version=VERSION, package_revision=REVISION,
            computation_question=self.manifest_payload["computation_question"],
            purpose=self.manifest_payload["purpose"], command=[sys.executable, *sys.argv],
            solvers=[str(p) for p in self.args.solvers], solver_args=self.args.solver_args,
            verifier=str(self.args.verifier), results_dir=str(self.args.results_dir),
            manifest=str(self.args.manifest), scratch_dir=str(self.args.scratch_dir),
            enabled_constraints={t["quotient_job_id"]: t["enabled_constraints"] for t in tasks},
            feedback_modules={t["quotient_job_id"]: t["feedback_modules"] for t in tasks},
            baseline_constraints={t["quotient_job_id"]: t.get("baseline_constraints", {}) for t in tasks},
            memory_reserve_mib=self.reserve_mib,
            memory_per_worker_estimate_mib=os.environ.get("N60_R13_R02_MEMORY_PER_WORKER_MIB", "2500"))


def main():
    previous.coverage, previous.export = coverage, export  # process-local adapter only
    base.RESULT_STATUSES = (*base.RESULT_STATUSES, "COVERED_BY_OTHER_ROUTE")
    base.BranchQueue = Round13R02Queue
    return base.main()


if __name__ == "__main__":
    raise SystemExit(main())
