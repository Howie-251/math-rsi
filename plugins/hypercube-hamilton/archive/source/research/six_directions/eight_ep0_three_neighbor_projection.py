"""Exact T15 geometry of every edge choice in the conditional 3-neighbor route."""
import itertools,json,collections
from pathlib import Path
R=Path(__file__).resolve().parent
def main():
    reps=json.loads((R/'t15_analytic_geometry.json').read_text())['T15']['residual_orbits'];lookup={}
    for p in itertools.permutations(range(5)):
        tr=[sum(((v>>j)&1)<<p[j] for j in range(5)) for v in range(32)]
        for core,row in enumerate(reps):
            key=tuple(sorted(tr[v] for v in row['avoided'])),tuple(sorted(tr[v] for v in row['included']))
            assert key not in lookup or lookup[key]==core;lookup[key]=core
    source=json.loads((R/'eight_ep0_three_neighbor_geometry.json').read_text());rows=[]
    for report in source['reports']:
        v=report['target'];Z=report['Z'];W=report['W']
        assert report['closed_conditional_on_Q5_neighbor_union3']
        for case in report['sufficient_crossing_edges']:
            i,q=case['cut'],case['q'];ZA=[z for z in Z if ((z^v)>>i)&1==0];assert len(ZA)==2
            a=next(z for z in Z if z not in ZA)
            def project(x):
                x^=a;assert (x>>i)&1==0
                return (x&((1<<i)-1))|((x>>(i+1))<<i)
            for s in case['S_neighbors']:
                t=s^(1<<i);assert t in W and (q^s).bit_count()==1
                key=tuple(sorted(project(z^(1<<i)) for z in ZA)),tuple(sorted(project(w) for w in W if w!=t))
                assert key in lookup,key
                rows.append(dict(target=v,Z=Z,W=W,cut=i,port=q,selected_edge=[q,s],consumed_odd_hole=t,T15_avoided=key[0],T15_included=key[1],core=lookup[key]))
    hist=dict(collections.Counter(r['core'] for r in rows))
    out=dict(status='PASS_GEOMETRIC_PROJECTION',scope='Every possible selected q-s edge in all seven three-neighbor EP0 representatives; Q5 neighbor abundance still requires independent review',core_histogram=hist,rows=rows,full_eight_hole_proved=False)
    (R/'eight_ep0_three_neighbor_projection.json').write_text(json.dumps(out,indent=2)+'\n');print(len(rows),hist)
if __name__=='__main__':main()
