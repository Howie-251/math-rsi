"""Direct bit-coordinate verification of seven EP0 geometries and marked imports."""
import collections, hashlib, itertools, json
from pathlib import Path
R=Path(__file__).resolve().parent
def tr(x,p):return sum(((x>>j)&1)<<p[j] for j in range(len(p)))
def ed(a,b):return tuple(sorted((a,b)))
def main():
    source=json.loads((R/'eight_ep0_three_neighbor_geometry.json').read_text())
    proj=json.loads((R/'eight_ep0_three_neighbor_projection.json').read_text())
    seeds={1:({1,2},{0,7,11,19}),4:({1,2},{0,7,11,31})}
    images={k:{} for k in seeds}
    for k,(avoid,keep) in seeds.items():
        for p in itertools.permutations(range(5)):
            key=(tuple(sorted(tr(x,p) for x in avoid)),tuple(sorted(tr(x,p) for x in keep)))
            images[k][key]=p
    rows=[];allgeoms=set();orbit_sizes=[];proofs=[]
    for r in source['reports']:
        v=r['target'];Z=set(r['Z']);W=set(r['W']);H={0}|Z|W;good=[]
        # Reconstruct all applicable cuts and sufficient edges without importing producer.
        for i in range(6):
            A={x for x in range(64) if ((x^v)>>i)&1==0}
            if len(Z&A)!=2 or W&A:continue
            S={w^(1<<i) for w in W}
            for q in sorted(A-H-{v}):
                if not q.bit_count()%2 or q^(1<<i) in H:continue
                ns={q^(1<<j) for j in range(6) if j!=i}&S
                if len(ns)>=3:good.append(dict(cut=i,q=q,mirror=q^(1<<i),S_neighbors=sorted(ns)))
        assert good==r['sufficient_crossing_edges']
        forbidden={ed(x['q'],x['mirror']) for x in good}
        hall=r['hall'];U=set(hall['even_set'])
        assert U and all(not a.bit_count()%2 and a not in H for a in U)
        N={a^(1<<i) for a in U for i in range(6) if a^(1<<i) not in H and ed(a,a^(1<<i)) not in forbidden}
        assert sorted(N)==hall['neighbors'] and len(N)<len(U)
        proofs.append(dict(target=v,Z=sorted(Z),Hall_set=sorted(U),Hall_neighbors=sorted(N)))
        for x in good:
            i=x['cut'];ZA={z for z in Z if ((z^v)>>i)&1==0};a=next(iter(Z-ZA))
            def project(y):
                z=y^a;assert not (z>>i&1)
                return sum(((z>>j)&1)<<k for k,j in enumerate(j for j in range(6) if j!=i))
            for s in x['S_neighbors']:
                t=s^(1<<i)
                avoid=tuple(sorted(project(z^(1<<i)) for z in ZA))
                keep=tuple(sorted([0]+[project(w) for w in W-{t}]))
                ks=[k for k in seeds if (avoid,keep) in images[k]];assert len(ks)==1
                k=ks[0]
                rows.append(dict(target=v,Z=sorted(Z),W=sorted(W),cut=i,port=x['q'],selected_edge=[x['q'],s],consumed_odd_hole=t,T15_avoided=list(avoid),T15_included=[y for y in keep if y],core=k))
        orbit={(v,tuple(sorted(tr(z,p) for z in Z)),tuple(sorted(tr(w,p) for w in W)))
               for p in itertools.permutations(range(6)) if tr(v,p)==v}
        assert not (orbit&allgeoms);allgeoms|=orbit;orbit_sizes.append(len(orbit))
    assert rows==proj['rows'] and len(rows)==234
    counts=collections.Counter(x['core'] for x in rows);assert counts=={4:174,1:60}
    assert len(allgeoms)==50
    out=dict(status='PASS',marked_T15_projection_cases=234,core_histogram=dict(counts),orbit_sizes=orbit_sizes,
             Hall_certificates=proofs,closed_geometry_count=50,
             closed_geometries=[dict(root=0,target=v,Z=list(z),W=list(w)) for v,z,w in sorted(allgeoms)])
    (R/'EIGHT_ALL_EP0_CONSEQUENCES_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('closed_geometries','Hall_certificates')}))
if __name__=='__main__':main()
