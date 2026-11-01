"""Full increasing-layout domain for three symmetric local trace profiles."""
from itertools import combinations
from pathlib import Path
import importlib.util
import json
import sys
import time

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("triple_nine_bounded", HERE / "triple_nine_pilot.py")
pilot = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pilot)
old = pilot.old


def main():
    start = time.perf_counter()
    cases = []
    for tau in range(3):
        counts = {0: 14-tau, 1: 5+tau, 2: 5+tau, 4: 5+tau,
                  3: 2-tau, 5: 2-tau, 6: 2-tau, 7: tau}
        best = None
        tested = []
        for positions in combinations(range(1, 19), 3):
            if time.perf_counter()-start > 55:
                raise TimeoutError("Bounded 55-second wall limit exceeded; no completed-domain claim")
            p = old.Profile(18, 5, positions, counts)
            certs = [old.certificate(p, i) for i in range(3)]
            rs = old.rows(p, deductions={positions[i]: certs[i]['loss'] for i in range(3)})
            case = dict(v=18, m=35, degrees=[9]*3,
                tau=tau, counts=counts, positions=positions, certificates=certs,
                rows=rs, bound=old.total_bound(rs))
            tested.append(dict(positions=positions, bound=case['bound']))
            if best is None or case['bound'] < best['bound']:
                best = case
        old.check_independent(best)
        cases.append(dict(tau=tau, tested_count=len(tested), best=best, tested=tested))
        print(tau, len(tested), best['positions'], best['bound'], flush=True)
    out = dict(scope="All C(18,3)=816 increasing-position layouts for each of three symmetric local profiles. "
        "Not a search over hypergraphs. Independent A/B/C row replay on each saved best layout; quota proof reused.",
        complete=True, elapsed_seconds=time.perf_counter()-start, cases=cases)
    (HERE / "TRIPLE_NINE_ALL_POSITIONS.json").write_text(json.dumps(old.json_value(out), indent=2)+"\n")
    print('elapsed', out['elapsed_seconds'], flush=True)


if __name__ == '__main__':
    main()
