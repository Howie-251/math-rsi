"""Independent witness audit; calls only the stdlib verifier, never construction code."""
import json
from pathlib import Path
from verify_split_transfer import verify,edge,eset,route,short
ROOT=Path(__file__).resolve().parent

def main():
    data=json.loads((ROOT/'auxiliary_reduction_results.json').read_text(encoding='utf8'))
    counts={}
    for c in data:
        assert c['status']=='FOUND'
        n,u,v=c['n'],c['u'],c['v'];m={edge(*e) for e in c['matching']}
        mate={a:b for e in m for a,b in (e,e[::-1])}
        assert len(mate)==2*len(m) and all(map(short,m)) and u not in mate
        assert u.bit_count()%2!=v.bit_count()%2
        l={edge(*e) for e in c['transformed_matching']}
        root,target=c['new_root'],c['new_target']
        d=dict(n=n,u=root,v=target,matching=c['transformed_matching'],**c['split_certificate'],**c['intermediate'])
        verify(d,generalized=True)
        k=c['intermediate']['path'];ke=eset(k)
        if c['kind']=='covered_target_rotation':
            assert len(m)==30 and v in mate and root==mate[v] and target==v
            assert l==(m-{edge(v,mate[v])})|{edge(u,v)}
            assert k[-2:]==[u,v] and c['path']==k[:-1][::-1]+[v]
            expected=(ke-{edge(u,v)})|{edge(v,mate[v])}
        else:
            assert c['kind']=='free_target_cycle' and len(m)==29 and v not in mate
            assert l==m|{edge(u,v)} and short((root,target))
            assert edge(root,target) not in ke
            expected=(ke|{edge(root,target)})-{edge(u,v)}
        final=route(c['path'],range(1<<n),u,v,m,set())
        assert final==expected
        counts[c['kind']]=counts.get(c['kind'],0)+1
    result=dict(status='PASS',certificates=len(data),counts=counts,
                scope='individual certificates only; Z4 and R1/R2 analytic review separate; full P6 open')
    (ROOT/'auxiliary_reduction_verification.json').write_text(json.dumps(result,indent=2),encoding='utf8')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
