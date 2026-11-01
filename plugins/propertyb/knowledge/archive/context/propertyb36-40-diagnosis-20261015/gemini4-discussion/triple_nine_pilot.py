"""Bounded parent-proposed triple-lock formula pilot; no whole-H search."""
from pathlib import Path
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
spec = importlib.util.spec_from_file_location(
    "previous_low_diagnostic",
    ROOT / "context/propertyb34-feasibility-20261013/low-vertices/diagnose.py",
)
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)

LAYOUTS = [
    (1, 2, 3), (1, 2, 9), (1, 9, 10), (1, 9, 18),
    (1, 10, 18), (2, 9, 17), (7, 8, 9), (8, 9, 10),
    (9, 10, 11), (7, 9, 11), (8, 10, 12), (1, 2, 18),
]


def main():
    start = time.perf_counter()
    cases = []
    for tau in range(3):
        counts = {0: 14-tau, 1: 5+tau, 2: 5+tau, 4: 5+tau,
                  3: 2-tau, 5: 2-tau, 6: 2-tau, 7: tau}
        assert sum(counts.values()) == 35
        assert all(sum(n for t, n in counts.items() if t & (1 << i)) == 9
                   for i in range(3))
        assert all(sum(n for t, n in counts.items() if t & b == b) == 2
                   for b in (3, 5, 6))
        candidates = []
        for positions in LAYOUTS:
            p = old.Profile(18, 5, positions, counts)
            certs = [old.certificate(p, i) for i in range(3)]
            rs = old.rows(p, deductions={positions[i]: certs[i]['loss'] for i in range(3)})
            candidates.append(dict(v=18, m=35, degrees=[9]*3,
                tau=tau, counts=counts, positions=positions, certificates=certs,
                rows=rs, bound=old.total_bound(rs)))
            print(tau, positions, str(candidates[-1]['bound']), flush=True)
        best = min(candidates, key=lambda c: c['bound'])
        old.check_independent(best)
        cases.append(dict(tau=tau, best=best, tested=[dict(positions=c['positions'],
            bound=c['bound']) for c in candidates]))
    out = dict(scope="Twelve fixed layouts per triple type, not all-position search. "
        "Independent A/B/C row replay on each saved best layout; quota proof reused.",
        attribution="Parent's independent idea, not Gemini's contribution.",
        elapsed_seconds=time.perf_counter()-start, cases=cases)
    (HERE / "TRIPLE_NINE_PILOT.json").write_text(json.dumps(old.json_value(out), indent=2)+"\n")


if __name__ == "__main__":
    main()
