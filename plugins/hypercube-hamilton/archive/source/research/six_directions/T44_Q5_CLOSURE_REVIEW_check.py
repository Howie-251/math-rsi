"""Independent T44 audit: binary negatives, ALL 2,027,025 forward states,
direct stalled root/completion checks, Hall obstructions, and geometry.
Does not import author code or use its inverse exception lists as input.
"""
import hashlib, itertools as it, json, math
from collections import Counter
from pathlib import Path

R=Path(__file__).resolve().parent
ODD=tuple(x for x in range(16) if x.bit_count()%2)
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def pairs(v):
    if not v:
        yield ()
        return
    x=v[0]
    for i,y in enumerate(v[1:],1):
        for rest in pairs(v[1:i]+v[i+1:]): yield ((x,y),)+rest
def mate(edges):
    m=bytearray([255]*16)
    for x,y in edges:
        assert x!=y and m[x]==m[y]==255
        m[x]=y;m[y]=x
    return bytes(m)
def edges(m): return tuple((x,y) for x,y in enumerate(m) if x<y<16)
def transformed(m,p):
    def tr(x): return sum(((x>>i)&1)<<p[i] for i in range(4))
    return mate((tr(x),tr(y)) for x,y in edges(m))
def load_negative_tables():
    result={};summary=[]
    for weight,z in ((1,1),(3,7)):
        p=R/f'q4_distance{weight}_avoided_table.bin';raw=p.read_bytes()
        assert len(raw)==30*135135
        neg=set();seen=set();positive=0
        for i in range(0,len(raw),30):
            m=raw[i:i+16];cycle=raw[i+16:i+30]
            assert {x for x in range(16) if m[x]==255}=={0,z}
            assert all(m[x]<16 and m[x]!=x and m[m[x]]==x for x in range(16) if x not in (0,z))
            assert m not in seen;seen.add(m)
            if cycle==bytes([255]*14): neg.add(m)
            else:
                assert set(cycle)==set(range(16))-{0,z}
                ce={tuple(sorted((a,b))) for a,b in zip(cycle,cycle[1:]+cycle[:1])}
                required=set(edges(m));assert len(ce)==14 and required<=ce
                assert all((a^b).bit_count()==1 for a,b in ce-required)
                positive+=1
        assert len(seen)==135135
        source=json.loads((R/f'q4_distance{weight}_avoided_table_verification.json').read_text(encoding='utf-8'))
        assert {mate(r['matching']) for r in source['exceptions']}==neg
        # Independent exhaustive short complementary matching check.
        complements=0
        for m in neg:
            even=tuple(x for x in range(16) if x not in (0,z) and x.bit_count()%2==0)
            odd=set(range(16))-{0,z}-set(even)
            def visit(i,left,chosen):
                nonlocal complements
                if i==len(even):
                    complements+=1
                    adj={v:{m[v]} for v in range(16) if v not in (0,z)}
                    for a,b in chosen: adj[a].add(b);adj[b].add(a)
                    reach=set();todo=[next(iter(adj))]
                    while todo:
                        v=todo.pop()
                        if v not in reach: reach.add(v);todo.extend(adj[v]-reach)
                    assert len(reach)<14
                    return
                a=even[i]
                for b in left:
                    if (a^b).bit_count()==1 and m[a]!=b: visit(i+1,left-{b},chosen+((a,b),))
            visit(0,odd,())
        result[weight]=neg
        summary.append({'file':p.name,'sha256':sha(p),'records':len(seen),'positive':positive,'negative':len(neg),'negative_short_completions':complements})
    bad={}
    for z in ODD:
        p=tuple(i for i in range(4) if z>>i&1)+tuple(i for i in range(4) if not z>>i&1)
        bad[z]={transformed(m,p) for m in result[z.bit_count()]}
    return bad,summary
def available(m,d,z,bad):
    if d==z:return False
    k=m[z];assert k<16
    t=bytearray(m);t[z]=255;t[d]=k;t[k]=d
    return bytes(t) not in bad[z]
def geometry():
    even=[x for x in range(32) if x.bit_count()%2==0]
    residual=[p for p in it.combinations([x for x in even if x not in (0,3)],2) if not ((p[0]^p[1])&3)]
    assert len(residual)==18
    group=[p+q for p in it.permutations((0,1)) for q in it.permutations((2,3,4))]
    def image(x,p,t):return sum(((x>>i)&1)<<p[i] for i in range(5))^t
    orbits=[]
    for rep in ((12,20),(5,9),(5,29)):
        orbit={tuple(sorted(image(x,p,t) for x in rep)) for p in group for t in (0,3)}
        assert len(orbit)==6;orbits.append(orbit)
    assert set.union(*orbits)==set(residual) and sum(map(len,orbits))==18
    for p in it.combinations([x for x in even if x not in (0,15)],2):assert (p[0]^p[1])&15
    # Canonical labels and short mirror identification are exactly drop-bit/XOR.
    assert {((x>>1)^1) for x in (0,12,20)}=={1,7,11}
    assert (3>>1)^1==0 and (0>>1)^1==1
    assert {x>>1 for x in (3,5,29)}=={1,2,14}
    assert 0>>1==0 and 3>>1==1
    return {'distance2_pairs':91,'residual_pairs':18,'orbits':[{'representative':rep,'size':len(o)} for rep,o in zip(((12,20),(5,9),(5,29)),orbits)],'distance4_all_separated':True,'canonical_holes_verified':True}
def main():
    bad,tables=load_negative_tables();print('Binary tables and negative exclusions PASS',flush=True)
    families=((7,11),(2,14));failure={fg:[] for fg in families};states=0
    # All roots, all near-perfect complete-graph matchings: forward only.
    for d in range(1,16):
        for es in pairs(tuple(x for x in range(1,16) if x!=d)):
            m=mate(es);states+=1
            status={z:available(m,d,z,bad) for z in (2,7,11,14)}
            for fg in families:
                if not any(status[z] for z in fg):failure[fg].append((d,m))
        print('Forward root',d,'states',states,flush=True)
    assert states==2027025
    probe=json.loads((R/'t44_canonical_completion_probe.json').read_text(encoding='utf-8'));results=[]
    for fi,fg in enumerate(families):
        author=probe['results'][fi];assert tuple(author['free_targets'])==fg
        assert len(failure[fg])==author['near_perfect_failures']
        levels=[]
        for c in (1,3,5,7,9,11,13):
            n=(15-c)//2;troot=math.prod(range(1,c-1,2));total=c*troot
            counts=Counter(tuple(sub) for d,m in failure[fg] for sub in it.combinations(edges(m),n))
            assert max(counts.values(),default=0)<=total
            stalls={f for f,count in counts.items() if count==total}
            alevel=author['levels'][(c-1)//2]
            amap={tuple(tuple(e) for e in item['matching']):item for item in alevel['items']}
            assert set(amap)==stalls
            inspected=0;Ghist=Counter();hall_only=0;port_endpoint_witnesses=0
            for f in sorted(stalls):
                item=amap[f];ports=tuple(sorted(set(range(1,16))-{v for e in f for v in e}));assert len(ports)==c
                bc={z:{} for z in ODD};gr={z:[] for z in ODD}
                for d in ports:
                    rootcounts=Counter();ncompletions=0
                    for D in pairs(tuple(x for x in ports if x!=d)):
                        m=mate(f+D);ncompletions+=1;inspected+=1
                        for z in ODD:
                            if not available(m,d,z,bad):rootcounts[z]+=1
                            elif z in ports and z!=d:port_endpoint_witnesses+=1
                    assert ncompletions==troot
                    for z in ODD:
                        bc[z][d]=rootcounts[z]
                        if rootcounts[z]<troot:gr[z].append(d)
                assert {str(z):v for z,v in gr.items()}==item['good_roots']
                assert {str(z):{str(d):v for d,v in ds.items()} for z,ds in bc.items()}==item['bad_counts']
                G=tuple(z for z in ODD if z!=1 and gr[z]);Ghist[len(G)]+=1
                assert list(G)==item['good_endpoints_excluding_forbidden']
                # Hall's theorem gives an independent alternative to recursive injection DFS.
                badroots={z:set(ports)-set(gr[z]) for z in G}
                deficiency=[]
                for k in range(1,len(G)+1):
                    for S in it.combinations(G,k):
                        N=set().union(*(badroots[z] for z in S))
                        if len(N)<len(S):deficiency.append({'endpoints':S,'badroot_union':sorted(N)})
                injection_exists=not deficiency
                assert (item['bad_injection'] is not None)==injection_exists or len(G)>c
                guaranteed=len(G)>c or (c>=3 and not injection_exists)
                assert guaranteed==item['guaranteed_safe_or_occupied'] and guaranteed
                if len(G)<=c:hall_only+=1
                if c==1:assert len(G)>c
            levels.append({'c':c,'candidate_partials':len(counts),'stalls':len(stalls),'direct_completions':inspected,'endpoint_count_histogram':dict(Ghist),'hall_needed':hall_only,'available_port_endpoint_occurrences':port_endpoint_witnesses,'unresolved':0})
        results.append({'targets':fg,'forward_double_failure_states':len(failure[fg]),'levels':levels})
    dependencies={}
    for name in ('Q4_CORE_REVIEW.json','Q4_TWO_AVOIDED_REVIEW.json','Q4_RICH_GLUING_REVIEW.json','T44_SAMEFACE_ZERO_CROSSING_REVIEW.json'):
        p=R/name;j=json.loads(p.read_text(encoding='utf-8'));assert j['verdict']=='PASS'
        checked={}
        for fn,digest in j['audited_input_hashes'].items():
            assert sha(R/fn)==digest.removeprefix('sha256:');checked[fn]=digest
        dependencies[name]={'sha256':sha(p),'verdict':j['verdict'],'review_independence':j['review_independence'],'acceptance_status':j['acceptance_status'],'audited_inputs_hash_match':checked}
    out={'status':'PASS','geometry':geometry(),'near_perfect_forward_states':states,'binary_tables':tables,'canonical_families':results,'dependencies':dependencies,'input_hashes':{n:sha(R/n) for n in ('T44_Q5_CLOSURE_DRAFT.md','t44_canonical_completion_probe.py','t44_canonical_completion_probe.json','q4_distance1_avoided_table_verification.json','q4_distance3_avoided_table_verification.json')},'checker_sha256':sha(Path(__file__))}
    (R/'T44_Q5_CLOSURE_REVIEW_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
