"""Compare result JSON counts only; never reads/imports discovery Python."""
from pathlib import Path
from itertools import permutations
import json

HERE=Path(__file__).resolve().parent


def main():
    independent=json.loads((HERE/'SUMMARY.json').read_text())
    discovery_path=HERE.parent/'two_high_new_mixed_gate_20261020'/'RUN_TWO_SMALL.json'
    discovery=json.loads(discovery_path.read_text())
    rows=[]
    for shape in independent['shapes']:
        F={frozenset(e) for e in shape['missing_pairs']}
        D=shape['D'];autos=[]
        for values in permutations(D):
            p=dict(zip(D,values))
            if {frozenset((p[a],p[b])) for a,b in F}==F:autos.append(p)
        def norm(high):
            return min(tuple(sorted(sum(1<<p[v] for v in T) for T in high)) for p in autos)
        ours={tuple(r['high_masks']):r for r in shape['orbits']}
        found=[r for r in discovery['completed_rows'] if r['missing_shape']==shape['name']]
        assert len(found)==len(ours)
        seen=set()
        for r in found:
            key=norm(r['high_traces']);assert key not in seen;seen.add(key)
            actual=ours[key]
            assert r['high_orbit_finished']
            assert r['n2']==actual['n2']
            assert r['necessary_inventories_checked']==actual['PL_J']
            assert sum(r['successful_gate_counts'].values())==actual['PL_J']
        assert seen==set(ours)
        rows.append(dict(shape=shape['name'],high_orbits=len(found),
                         independent_PL=shape['PL_J'],
                         discovery_necessary=sum(r['necessary_inventories_checked'] for r in found),
                         all_high_orbit_counts_match=True))
    out=dict(status='PASS',scope='83 high-orbit counts compared, not J-set equality',
             discovery_status_label=discovery['status'],rows=rows,
             discovery_zero_triple_extension=discovery['used_four_small_zero_triple_extension'],
             independent_zero_triple_extension=independent['used_zero_triple_extension'])
    assert not out['discovery_zero_triple_extension'] and not out['independent_zero_triple_extension']
    (HERE/'COMPARISON.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out))


if __name__=='__main__':main()
