"""Controlled quotient change of the source-derived quadratic rule."""
from pathlib import Path
import json
import subprocess
import time
from literal_transfer import endpoints, ROOT

OUT = Path(__file__).resolve().parent
START = time.process_time()


def main():
    prediction = json.loads((OUT / 'QUOTIENT25_PREDICTION.json').read_text())
    assert prediction['frozen_before_experiment']
    p, m = 101, 25
    roots = [r for r in range(2, p) if pow(r, m, p) == 1 and pow(r, 5, p) != 1]
    assert len(roots) == 20
    cases = []
    for r in roots:
        positive = list(zip([1, 3, 6, 7, 9], [0, (r*r-1) % p, (-r*r-1) % p, -r % p, 1]))
        case = endpoints(p, r, m=m, positive=positive)
        case['positive_generators'] = positive
        if case['all_phases_full']:
            arcs = []
            for phase, b in positive:
                arcs.extend([(phase, b), (-phase % m, -b * pow(r, -phase, p) % p)])
            edges = set()
            for phase in range(m):
                for x in range(p):
                    u = phase*p + x
                    for dp, b in arcs:
                        v = ((phase+dp) % m)*p + (x*pow(r, dp, p)+b) % p
                        edges.add(tuple(sorted((u, v))))
            assert len(edges) == 5*m*p and all(u != v for u, v in edges)
            path = OUT / f'graph_d10_D4_n2525_r{r}.edges'
            with path.open('w') as f:
                f.write(f'{m*p} {len(edges)}\n')
                for u, v in sorted(edges):
                    f.write(f'{u} {v}\n')
            case.update(graph_generated=True, edge_file=path.name)
            if not any(c['graph_generated'] for c in cases):
                check = subprocess.run([str(ROOT/'computations/ddp/verify_graph'), str(path), '10', '4'], capture_output=True, text=True)
                (OUT/'QUOTIENT25_FIRST_INDEPENDENT.json').write_text(check.stdout)
                assert check.returncode == 0, (check.stdout, check.stderr)
                case['independent_check'] = json.loads(check.stdout)
        cases.append(case)
    raw = cases[0]['raw_words_by_phase']
    result = dict(status='COMPLETE', frozen_rule=prediction, cases=cases,
                  actual_min_raw_words_per_phase=min(raw),
                  route_count_prediction_supported=min(raw)>215,
                  complete_hits=sum(c['graph_generated'] for c in cases),
                  CPU_seconds=time.process_time()-START, old_source_BFS=0)
    (OUT/'QUOTIENT25_RESULT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n')
    print(json.dumps(dict(min_raw_words=min(raw), prediction_supported=result['route_count_prediction_supported'],
                         complete_hits=result['complete_hits'], CPU_seconds=result['CPU_seconds'],
                         cases=[dict(r=c['action'], root_missing=c['representative_root_missing'], min_coverage=min(c['distinct_endpoints_by_phase'])) for c in cases]), ensure_ascii=False))


if __name__ == '__main__':
    main()
