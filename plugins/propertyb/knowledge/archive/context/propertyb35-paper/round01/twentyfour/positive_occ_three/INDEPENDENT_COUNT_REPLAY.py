"""Independent32-term inclusion-exclusion replay for all86 five-positive-set local graph representatives."""
from pathlib import Path
from math import comb
from itertools import combinations
import json,time
HERE=Path(__file__).parent

def choose(n,k):return comb(n,k) if n>=k else 0
def main():
    start=time.time();raw=json.loads((HERE/'five_graph_catalogue.json').read_text());out=[]
    assert raw['status']=='PASS' and raw['orbits']==86 and raw['labeled_graphs']==5307
    for g in raw['graphs']:
        masks=[p['mask'] for p in g['points']];N=len(masks)
        assert all(m.bit_count() in (1,2) for m in masks)
        assert all(sum(bool(m>>i&1) for m in masks)==4 for i in range(5))
        degree=[sum(m.bit_count()==2 and bool(m>>i&1) for m in masks) for i in range(5)]
        E=sum(m.bit_count()==2 for m in masks)
        assert degree==g['degrees'] and N==20-E and 4<=E<=8 and max(degree)<=4
        mult={m:masks.count(m) for m in set(masks) if m.bit_count()==2}
        M2=choose(E,2)-sum(choose(d,2) for d in degree)+sum(choose(n,2) for n in mult.values())
        assert M2==g['M2'] and 1<=M2<=6
        ie={k:sum((-1)**S.bit_count()*choose(sum(not(m&S) for m in masks),k) for S in range(32)) for k in (3,4)}
        assert ie[3]==g['C3'] and ie[4]==g['C4']
        # Separate direct point-subset check, not the catalogue's stored candidates.
        for k in (3,4):
            direct=sum(1 for ids in combinations(range(N),k) if __import__('functools').reduce(int.__or__,(masks[i] for i in ids),0)==31)
            assert direct==ie[k]
        out.append(dict(index=g['index'],edge_vector=g['edge_vector'],N=N,E=E,M2=M2,C3=ie[3],C4=ie[4]))
    minimum=min(x['C4'] for x in out);assert minimum==178 and minimum>168
    result=dict(status='PASS',scope=__doc__,orbits_replayed=len(out),labeled_domain_as_certified_by_two_catalogue_enumerators=raw['labeled_graphs'],minimum_C4=minimum,blocking_upper_bound=168,strict_margin=minimum-168,minimizers=[x for x in out if x['C4']==minimum],all_counts=out,elapsed_seconds=time.time()-start)
    (HERE/'INDEPENDENT_COUNT_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n')
    print({k:v for k,v in result.items() if k not in ('all_counts','minimizers')})
if __name__=='__main__':main()
