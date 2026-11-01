"""Compare saved JSON only; does not import either generating implementation."""
from pathlib import Path
import json

HERE=Path(__file__).resolve().parent
OTHER=HERE.parent/'higher_at_least_three_remaining_20261020'/'with_three_blue'
ours=json.loads((HERE/'SUMMARY.json').read_text())
found=json.loads((OTHER/'RESULT.json').read_text())
index={(j['missing'],j['r'],j['n4']):j for j in found['jobs']}
rows=[]
for j in ours['jobs']:
    k=(j['missing'],j['r'],j['n4']);o=index[k]
    a=json.loads((HERE/j['witness_file']).read_text())
    b=json.loads((OTHER/o['witnesses_file']).read_text())
    # Both files use the same explicitly canonical mask representative and
    # the lexicographic 21-pair label ordering. Check full domain identities.
    ka={(tuple(x[0]),tuple(x[1])) for x in a}
    kb={(tuple(x[0]),tuple(x[1])) for x in b}
    assert len(ka)==len(a) and len(kb)==len(b)
    assert ka==kb
    for field in ('n3','n2','n1','aut_size','raw_high_multisets','high_orbits','accepted'):
        assert j[field]==o[field],(k,field)
    pa={tuple(x['high_masks']):x['necessary_J_checked'] for x in j['per_high']}
    pb={tuple(x['high_masks']):x['necessary_J_checked'] for x in o['per_high']}
    assert {h:n for h,n in pa.items() if n}==pb
    rows.append({'missing':k[0],'r':k[1],'n4':k[2],'inputs':len(ka),
                 'full_high_and_J_key_sets_equal':True})
out={'pass':True,'comparison_scope':'all saved actual input keys (canonical high masks, fully labelled J multiset), not merely aggregate counts; no code imports',
     'compared_total':sum(r['inputs'] for r in rows),'rows':rows}
(HERE/'COMPARISON.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',out['compared_total'])
