"""Prepare and independently validate diagnostic A4 edge prescriptions.

Not an exhaustive enumeration of Q5 matchings. A bounded negative is UNKNOWN.
"""
import json,sys,collections,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
edge=lambda a,b:tuple(sorted((a,b)))
def prepare():
    source=json.loads((R/'q5_t15_probe_inputs.json').read_text())
    cases=[]
    for row in source:
        for y in row['avoid']:
            x=next(v for v in row['avoid'] if v!=y)
            for z in sorted(set(row['holes'])-{0,*row['avoid']}):
                if (y^z).bit_count()!=2:continue
                for p in range(32):
                    if (p^y).bit_count()!=(p^z).bit_count() or (p^y).bit_count()!=1:continue
                    cases.append(dict(id=len(cases),source_id=row['id'],x=x,y=y,z=z,p=p,
                        matching=row['matching'],required=row['matching']+[[y,z],[y,p]]))
    (R/'q5_prescription_inputs.json').write_text(json.dumps(cases)+'\n')
    (R/'q5_prescription_inputs.txt').write_text('\n'.join(' '.join(map(str,[c['id'],c['x'],len(c['required']),*[v for e in c['required'] for v in e]])) for c in cases)+'\n')
    print('prepared',len(cases),'prescriptions on',len(source),'T15 inputs')
def verify():
    cases=json.loads((R/'q5_prescription_inputs.json').read_text())
    results=json.loads((R/'q5_prescription_results.json').read_text())
    assert len(cases)==len(results)
    source_status=collections.defaultdict(list);pair_status=collections.defaultdict(list)
    for c,r in zip(cases,results):
        assert c['id']==r['id']
        source_status[c['source_id']].append(r['status'])
        pair_status[c['source_id'],c['y'],c['z']].append(r['status'])
        if r['status']!='FOUND':continue
        cyc=r['cycle'];assert len(cyc)==len(set(cyc))==31
        assert set(cyc)==set(range(32))-{c['x']}
        edges={edge(a,b) for a,b in zip(cyc,cyc[1:]+cyc[:1])}
        required={edge(a,b) for a,b in c['required']}
        assert required<=edges
        assert all((a^b).bit_count()==1 for a,b in edges-required)
        # Remove the forbidden y from its required p-y-z segment.
        final=[v for v in cyc if v!=c['y']]
        e2={edge(a,b) for a,b in zip(final,final[1:]+final[:1])}
        original={edge(a,b) for a,b in c['matching']}
        assert len(final)==30 and set(final)==set(range(32))-{c['x'],c['y']}
        assert original<=e2 and all((a^b).bit_count()==1 for a,b in e2-original)
    badpairs=[list(k) for k,v in pair_status.items() if all(s=='EXHAUSTED_NO_CYCLE' for s in v)]
    failures=[k for k,v in source_status.items() if 'FOUND' not in v]
    out=dict(scope='DIAGNOSTIC_ONLY_NOT_EXHAUSTIVE_Q5',full_t15_proved=False,
        prescriptions=len(cases),statuses=dict(collections.Counter(r['status'] for r in results)),
        source_inputs=len(source_status),sources_without_positive=failures,
        ordered_pairs_without_either_common_neighbor=badpairs,
        max_nodes=max(r['nodes'] for r in results),positive_witness_check='PASS',
        hashes={n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in ['q5_prescribed_component_probe.cpp','q5_prescription_inputs.json','q5_prescription_results.json']})
    (R/'q5_prescription_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':
    (prepare if len(sys.argv)>1 and sys.argv[1]=='prepare' else verify)()
