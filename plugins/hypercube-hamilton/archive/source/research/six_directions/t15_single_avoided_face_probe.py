"""Completion accounting for T15 cuts with exactly one avoided hole in A.

Uses previously certified Q4 endpoint exception tables. This is a candidate
finite lemma, not by itself a proof of the global gluing theorem.
"""
import itertools,json,math
from collections import Counter
from pathlib import Path
R=Path(__file__).resolve().parent
edge=lambda a,b:tuple(sorted((a,b)))
def main():
    sources={k:json.loads((R/f'q4_distance{k}_avoided_table_verification.json').read_text()) for k in (1,3)}
    odd=[x for x in range(16) if x.bit_count()%2];bad={}
    for y in odd:
        p=[i for i in range(4) if y>>i&1]+[i for i in range(4) if not y>>i&1]
        def tr(x):return sum(((x>>i)&1)<<p[i] for i in range(4))
        vals=set()
        for row in sources[y.bit_count()]['exceptions']:
            f=frozenset(edge(tr(a),tr(b)) for a,b in row['matching'])
            for a,b in f:
                for d,k in ((a,b),(b,a)):
                    vals.add((d,frozenset(f-{edge(d,k)}|{edge(y,k)})))
        bad[y]=vals
    orbits=json.loads((R/'t15_analytic_geometry.json').read_text())['T15']['residual_orbits']
    output=[]
    for idx,r in enumerate(orbits):
        O=r['avoided']+r['included']
        for cut in range(5):
            if sum(x>>cut&1 for x in O)!=1:continue
            only=next(x for x in O if x>>cut&1)
            if only not in r['avoided']:continue
            def drop(x):return (x&((1<<cut)-1))|((x>>(cut+1))<<cut)
            def local(x):return drop(x)^drop(only)
            a=local(0);x=local(next(v for v in r['avoided'] if v!=only))
            B=sorted(local(v) for v in r['included'])
            allowed=[z for z in odd if z!=x and ((a^x).bit_count()!=1 or (a^z).bit_count()!=1)]
            assert all(z in allowed for z in B)
            candidates=set().union(*(bad[z] for z in B))
            failures={(d,f) for d,f in candidates if all(d==z or (d,f) in bad[z] for z in B)}
            levels=[]
            for c in (1,3,5,7,9,11):
                m=(15-c)//2;perroot=math.prod(range(1,c-1,2));total=c*perroot
                counts=Counter(tuple(sorted(sub)) for d,f in failures for sub in itertools.combinations(sorted(f),m))
                stalls=[frozenset(f) for f,n in counts.items() if n==total]
                rows=[]
                for f in stalls:
                    ports=sorted(set(range(1,16))-{v for e in f for v in e})
                    good={}
                    for z in allowed:
                        bc=Counter(d for d,L in bad[z] if f<=L)
                        good[z]=[d for d in ports if d!=z and bc[d]<perroot]
                    G=[z for z in allowed if good[z]]
                    # Failure requires all usable endpoints to be occupied in B,
                    # with their distinct actual A roots chosen among bad roots.
                    badroot={z:set(ports)-set(good[z]) for z in G}
                    hall_witness=None
                    for size in range(1,len(G)+1):
                        for sub in itertools.combinations(G,size):
                            neighbors=set().union(*(badroot[z] for z in sub))
                            if len(neighbors)<len(sub):hall_witness=list(sub);break
                        if hall_witness:break
                    ok=len(G)>c or (c>=3 and hall_witness is not None)
                    rows.append(dict(matching=sorted(f),ports=ports,good_roots=good,
                        usable=G,hall_deficient_subset=hall_witness,closed_by_safe_or_occupied=ok))
                levels.append(dict(crossings=c,stalls=len(stalls),unresolved=sum(not t['closed_by_safe_or_occupied'] for t in rows),items=rows))
            output.append(dict(orbit=idx,cut=cut,minority=a,forbidden=x,free_targets=B,allowed_targets=allowed,near_perfect_failures=len(failures),levels=levels))
    result=dict(scope='FINITE_CANDIDATE_LEMMA_GLUING_AND_INDEPENDENT_AUDIT_PENDING',full_t15_proved=False,results=output)
    (R/'t15_single_avoided_face_probe.json').write_text(json.dumps(result,indent=2)+'\n')
    for r in output:print({k:r[k] for k in ('orbit','cut','minority','forbidden','free_targets','allowed_targets','near_perfect_failures')},[(l['crossings'],l['stalls'],l['unresolved']) for l in r['levels']])
if __name__=='__main__':main()
