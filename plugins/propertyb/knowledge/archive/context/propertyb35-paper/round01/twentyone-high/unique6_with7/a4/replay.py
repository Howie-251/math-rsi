"""Independent full-inclusive recovery, label transports and 35-stub exact replay for a7=4."""
from pathlib import Path
from itertools import combinations, product
from fractions import Fraction as Q
import importlib.util, json, time
HERE=Path(__file__).parent; ROOT=HERE.parents[5]
spec=importlib.util.spec_from_file_location('old_replay',ROOT/'context/propertyb35-paper/round01/twentyone-delta5/replay.py'); old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)

def key(ns):return tuple(ns.get(str(m),ns.get(m,0)) for m in range(64))
def invert(inc):
    ns={}
    for A in sorted(range(64),key=int.bit_count,reverse=True):
        ns[A]=inc[A]-sum(v for B,v in ns.items() if B&A==A)
    return ns if min(ns.values())>=0 else None

def main():
    st=time.time(); dom=json.loads((HERE/'DOMAIN.json').read_text()); rows=json.loads((HERE/'DP.json').read_text())['cases']; found={8:set(),9:set()}
    # Construct the three four-seven residuals directly, without reading their
    # discovery-domain inventories: four singletons with zero/one triple, or 22.
    pairs=list(combinations(range(4),2));triples=list(combinations(range(4),3)); bases=[]
    for nonzero in (None,*range(4)):
        bases.append(((1,2,4,8),{sum(1<<i for i in T):int(j==nonzero) for j,T in enumerate(triples)}))
    for j in (1,2,3):
        B=1|(1<<j);bases.append((tuple(sorted((B,15^B))),{sum(1<<i for i in T):0 for T in triples}))
    for d in (8,9):
        for P4,old_triples in bases:
            parts=[tuple(sorted((*P4,16)))]+[tuple(sorted((B|16) if j==k else B for j,B in enumerate(P4))) for k in range(len(P4))]
            for P in parts:
                same=lambda A:int(any(B&A==A for B in P))
                # Independent explicit description of the verified (6,7,d)
                # gate: 8 admits c1/2; 9 also c3 iff same central block.
                coptions=[(1,2,3) if d==9 and same((1<<i)|16) else (1,2) for i in range(4)]
                for cs in product(*coptions):
                    for ts in product((0,1),repeat=6):
                        tsmap={sum(1<<i for i in T)|16:v for T,v in zip(pairs,ts)}
                        qopts=[range(min(old_triples[A],*(tsmap[sum(1<<i for i in S)|16] for S in combinations(T,2)))+1) for T in triples for A in [sum(1<<i for i in T)]]
                        for qs in product(*qopts):
                            inc={0:35}
                            for A in range(1,64):
                                H=A>>1
                                if A&1:inc[A]=6 if not H else same(H)
                                elif H.bit_count()==1:inc[A]=d if H==16 else 7
                                elif H.bit_count()==2:inc[A]=cs[(H^16).bit_length()-1] if H&16 else 1
                                elif H.bit_count()==3:inc[A]=tsmap[H] if H&16 else old_triples[H]
                                elif H.bit_count()==4:inc[A]=qs[triples.index(tuple(i for i in range(4) if H>>i&1))] if H&16 else 0
                                else:inc[A]=0
                            ns=invert(inc)
                            if ns is not None:found[d].add(key(ns))
    assert len(dom['labelled'])==sum(len(x) for x in found.values())
    for d in (8,9):assert found[d]=={key(r['counts']) for r in dom['labelled'] if r['outsider_degree']==d}
    for r in dom['labelled']:
        rep=dom['orbits'][r['orbit']];p=r['from_representative_seven_permutation']
        assert rep['degrees']==[6,7,7,7,7,r['outsider_degree']]
        def move(m):return (m&33)|sum(1<<(p[i]+1) for i in range(4) if m>>(i+1)&1)
        assert key({move(int(m)):v for m,v in rep['counts'].items()})==key(r['counts'])
    out=[]
    for d in (8,9):
        rr=[r for r in rows if r['degrees'][-1]==d]; vals=[]
        for r in rr:
            assert key(r['counts'])==key(dom['orbits'][r['id']]['counts'])
            assert all(sum(v for m,v in r['counts'].items() if int(m)>>i&1)==di for i,di in enumerate(r['degrees']))
            vals.append(old.verify(r))
        assert all(v<1 for v in vals)
        out.append(dict(outsider_degree=d,labelled=len(found[d]),orbits=len(rr),max_bound=str(max(vals))))
    result=dict(status='PASS',scope=__doc__,independent_full_inclusion_domain=True,actual_transports=len(dom['labelled']),fixed_profiles=len(rows),expanded_stubs_per_profile=35,ordered_distinct_pairs_per_profile=1190,independent_rows=21*len(rows),results=out,elapsed_seconds=time.time()-st)
    (HERE/'REPLAY.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
if __name__=='__main__':main()
