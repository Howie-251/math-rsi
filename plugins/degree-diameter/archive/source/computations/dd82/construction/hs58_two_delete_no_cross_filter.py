#!/usr/bin/env python3
"""Derive a no-cross-D subdomain from saved a5 representatives; no graph generation."""
from pathlib import Path
import json
import time

HERE = Path(__file__).resolve().parent
OUT = HERE / 'hs58_two_delete_five_add_auxiliary_run'

def main():
    start_cpu, start_wall = time.process_time(), time.monotonic()
    ids = set(json.loads((OUT/'survivor_ids.json').read_text())['remaining_type_ids'])
    reps = json.loads((OUT/'representatives.json').read_text())['representatives']
    admitted, excluded = [], []
    for r in reps:
        if r['type_id'] not in ids:
            continue
        witnesses = [dict(bad_pair=[a,b], degrees=[r['degrees'][a],r['degrees'][b]],
                          degree_sum=r['degrees'][a]+r['degrees'][b])
                     for a,b in r['bad_pairs'] if r['degrees'][a]+r['degrees'][b] < 5]
        if witnesses:
            excluded.append(dict(type_id=r['type_id'],witnesses=witnesses))
        else:
            admitted.append(r['type_id'])
    report = dict(
        complete=True, input_type_ids=sorted(ids), checked_types=len(admitted)+len(excluded),
        scope='Exactly two disjoint original HS deletions inducing no Q cross-edge; all five additions and all ports free.',
        condition='Every pair at H-distance greater than two has d_H(u)+d_H(v)>=5.',
        proof='proofs/dd82/construction/HS58_NO_CROSS_ENDPOINT_COVERAGE.md',
        remaining_type_ids=admitted, excluded=excluded,
        excluded_type_count=len(excluded),remaining_type_count=len(admitted),
        graph_generation=False,solver_invoked=False,raw_catalog_modified=False,
        cpu_seconds=time.process_time()-start_cpu,wall_seconds=time.monotonic()-start_wall)
    (OUT/'no_cross_filter.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k not in ['input_type_ids','excluded']},indent=2))

if __name__ == '__main__':
    main()
