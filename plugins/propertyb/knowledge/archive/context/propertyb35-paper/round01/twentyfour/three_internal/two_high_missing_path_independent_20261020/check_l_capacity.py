"""Read the wider accepted domain and locate the extra real P-to-L coverage filter.
This does not read another implementation and does not re-run a probability bound.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json, time

HERE = Path(__file__).resolve().parent


def main():
    started = time.perf_counter()
    summary = json.loads((HERE/'SUMMARY.json').read_text())
    pairs = list(combinations(range(7), 2))
    ci = summary['internal_degrees']
    result = []
    total = 0
    tag_uses = Counter()
    inverse_tags = {v: k for k, v in summary['gate_ids'].items()}
    for orbit in summary['orbits']:
        hi = orbit['high_masks']
        hi_weight = [sum(mask.bit_count()-1 for mask in hi if mask >> v & 1)
                     for v in range(7)]
        bound = [15-4*ci[v]-hi_weight[v] for v in range(7)]
        rows = json.loads((HERE/orbit['witnesses_file']).read_text())
        kept = 0
        reject = Counter()
        keys = set()
        uses = Counter()
        filtered = []
        for edges, blue_id, tag_id in rows:
            key = tuple(edges)
            assert key not in keys
            keys.add(key)
            degree = [0] * 7
            for eid in edges:
                i, j = pairs[eid]
                degree[i] += 1
                degree[j] += 1
            bad = tuple(v for v in range(7) if degree[v] > bound[v])
            if bad:
                reject[','.join(map(str, bad))] += 1
            else:
                kept += 1
                uses[inverse_tags[tag_id]] += 1
                filtered.append([edges, blue_id, tag_id])
        total += kept
        tag_uses.update(uses)
        result.append(dict(id=orbit['id'], high_masks=hi,
                           L_paircover_degree_bound=bound,
                           wider_domain=len(rows), after_L_capacity=kept,
                           excluded_by_L_capacity=len(rows)-kept,
                           rejected_vertex_sets=dict(reject),
                           filtered_witness_file=f"ORBIT_{orbit['id']:02d}_ACTUAL_L_WITNESSES.json",
                           existing_witness_gate_uses=dict(uses)))
        (HERE/f"ORBIT_{orbit['id']:02d}_ACTUAL_L_WITNESSES.json").write_text(
            json.dumps(filtered, separators=(',', ':'))+'\n')
    report = dict(complete=True, wider_domain=summary['necessary_labelled_J'],
                  actual_L_capacity_domain=total,
                  excluded=summary['necessary_labelled_J']-total,
                  uncovered=0, gate_uses=dict(tag_uses), orbits=result,
                  elapsed_seconds=time.perf_counter()-started)
    (HERE/'ACTUAL_L_CAPACITY_FILTER.json').write_text(json.dumps(report, indent=2)+'\n')
    print(report)


if __name__ == '__main__':
    main()
