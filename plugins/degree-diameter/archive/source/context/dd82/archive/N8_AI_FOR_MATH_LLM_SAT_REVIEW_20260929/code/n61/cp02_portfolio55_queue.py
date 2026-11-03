#!/usr/bin/env python3
"""Existing queue: replicas of one formula; stop on the first decisive result."""
from cp02_common import VERSION
from cp02_queue import CP02Queue, queue

queue.STATE_VERSION = VERSION + '_portfolio55_queue_v1'


class CP02PortfolioQueue(CP02Queue):
    def _new_state(self):
        # A single UNSAT closes the formula only because every worker gets
        # the identical CNF, map and constraint set, not a subproblem/cube.
        signatures = {(r['_cnf_path'], r['_variable_map_path'],
                       queue.canonical_json(r['case_key']),
                       tuple(r['theory_flags'])) for r in self.records}
        if len(self.records) != 55 or len(signatures) != 1:
            raise ValueError('requires 55 configurations of one identical CP02 input')
        if {r['seed'] for r in self.records} != set(range(55)):
            raise ValueError('expected seeds 0 through 54')
        state = super()._new_state()
        state.update(parallelism='independent_seed_portfolio_no_clause_sharing',
                     logical_jobs_total=1, solver_configurations=55,
                     stop_on='first raw_unsat or SAT_validated for the same formula')
        return state

    def _apply_result_locked(self, job_id, result):
        super()._apply_result_locked(job_id, result)
        if result['result_status'] == 'raw_unsat' and self.sat_result is None:
            self.state.setdefault('portfolio_raw_unsat_winner', job_id)
            queue.STOP_REASON = 'same_formula_portfolio_raw_unsat'
            queue.STOP_EVENT.set()
            self._save_state_locked()

    def build_progress(self):
        p = super().build_progress()
        statuses = [j['result_status'] for j in self.jobs.values()]
        sat = 'SAT_validated' in statuses
        raw = 'raw_unsat' in statuses
        logical_status = ('SAT_validated' if sat else 'raw_unsat' if raw else
                          'timeout' if all(s == 'timeout' for s in statuses) else 'unknown')
        cancelled = sum(bool(j['attempts']) and
                        j['attempts'][-1].get('reason') in
                        ('same_formula_portfolio_raw_unsat','SAT_validated_found')
                        for j in self.jobs.values())
        p.update(parallelism='independent_seed_portfolio_no_clause_sharing',
            logical_jobs_total=1, logical_jobs_remaining=int(not (sat or raw)),
            logical_result_status=logical_status, solver_configurations=55,
            portfolio_cancelled_replicas=cancelled,
            portfolio_raw_unsat_winner=self.state.get('portfolio_raw_unsat_winner'),
            B_INSIDE_to_O_raw=raw, B_to_O_closed=False, global_N61_closed=sat,
            mathematical_status=('SAT_validated' if sat else
                'B_INSIDE_to_O_at_raw_solver_level_only' if raw else 'unresolved'))
        if raw and not sat:
            p['run_status']='same_formula_raw_unsat_found'
        return p


queue.Iteration2Queue = CP02PortfolioQueue
if __name__ == '__main__':
    queue.main()
