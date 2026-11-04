"""Independent deterministic audit. No producer imports or search-count assumptions.

Q4 negative tables are declared previously audited exact inputs. Their complete
negative sets, not their status/count fields, are used. Every one of 2,027,025
near-perfect rooted states is forward-tested against those sets at all 8 odd
targets, and compared with independently inverted failure sets.
"""
from pathlib import Path
import json, hashlib, itertools as it, collections, datetime, time
R = Path(__file__).resolve().parent
ROWS = {13:(1,0,1,(7,11,13)),14:(1,0,1,(7,11,14)),19:(2,3,2,(4,8,14)),31:(3,6,7,(1,11,13)),32:(3,6,7,(1,8,13)),35:(3,6,7,(8,11,13)),37:(0,0,7,(11,13,14)),38:(4,15,14,(2,4,8))}
H = {13:14,14:13,31:8,35:1}
V = set(range(16)); O = [v for v in V if v.bit_count()%2]
def read(n): return json.loads((R/n).read_text(encoding='utf-8'))
def edge(a,b): return (min(a,b),max(a,b))
def canon(es): return frozenset(edge(*e) for e in es)
def covered(f): return {v for e in f for v in e}
def pairs(vs):
    if not vs:
        yield frozenset(); return
    a,*tail = vs
    for b in tail:
        for f in pairs([v for v in tail if v!=b]): yield f | {edge(a,b)}
def df(n):
    v=1
    for k in range(n,0,-2): v*=k
    return v
def cycle_edges(p,cyclic=True):
    return canon(zip(p,p[1:]+(p[:1] if cyclic else [])))
def validate_cycle(es, support, required):
    assert required<=es and covered(es)==support and len(es)==len(support)
    adj={v:[] for v in support}
    for a,b in es: adj[a].append(b);adj[b].append(a)
    assert all(len(ns)==2 for ns in adj.values())
    seen=set();todo=[next(iter(support))]
    while todo:
        u=todo.pop()
        if u not in seen: seen.add(u);todo.extend(adj[u])
    assert seen==support
    assert all((a^b).bit_count()==1 for a,b in es-required)
def run():
    start=time.time();out={}; neg={};bad={}
    for z in O:
        # Explicit coordinate map sends canonical 1 or 7 to z.
        positions=[i for i in range(4) if z>>i&1]+[i for i in range(4) if not z>>i&1]
        trans=lambda v:sum(((v>>i)&1)<<positions[i] for i in range(4))
        neg[z]={canon((trans(a),trans(b)) for a,b in row['matching']) for row in read(f'q4_distance{z.bit_count()}_avoided_table_verification.json')['exceptions']}
        assert len(neg[z]) in (51,53)
        assert all(len(f)==7 and covered(f)==V-{0,z} for f in neg[z])
        inv=set()
        for f in neg[z]:
            for a,b in f:
                for d,k in ((a,b),(b,a)):
                    l=(f-{edge(d,k)})|{edge(z,k)}
                    assert covered(l)==V-{0,d}
                    inv.add((d,l))
        bad[z]=inv
    out['negative_inverse_sizes']={z:len(bad[z]) for z in O}
    # Exhaustive forward audit, including all d=z unavailable boundaries.
    full_failed={i:set() for i in ROWS};states=checks=0
    for d in range(1,16):
        for l in pairs(sorted(V-{0,d})):
            states+=1;mate={a:b for a,b in l}|{b:a for a,b in l};failed={d}
            for z in O:
                if z==d: continue
                k=mate[z];t=(l-{edge(z,k)})|{edge(d,k)}
                no=t in neg[z]
                assert no==((d,l) in bad[z]);checks+=1
                if no:failed.add(z)
            for i,(_,a,x,targets) in ROWS.items():
                if set(targets)<=failed: full_failed[i].add((d,l))
    assert states==15*df(13)
    out['forward_root_states']=states;out['forward_target_tests']=checks
    print('forward root-state audit complete',states,flush=True)
    source=read('t15_analytic_geometry.json')['T15']['residual_orbits']
    expected_A={};summary=[]
    for i,(cut,a,x,targets) in ROWS.items():
        g=source[i];holes=g['avoided']+g['included']
        only=[v for v in holes if v>>cut&1];assert len(only)==1 and only[0] in g['avoided']
        drop=lambda v:(v&((1<<cut)-1))|((v>>(cut+1))<<cut)
        tr=lambda v:drop(v)^drop(only[0])
        assert tr(0)==a and tr(next(v for v in g['avoided'] if v!=only[0]))==x
        assert set(map(tr,g['included']))==set(targets)
        assert a.bit_count()%2==0 and all(t.bit_count()%2 for t in (x,*targets))
        safe={z for z in O if z!=x and ((a^x).bit_count()!=1 or (a^z).bit_count()!=1)}
        assert set(targets)<=safe
        failures=full_failed[i];levels=[]
        for c in range(1,12,2):
            m=(15-c)//2
            # All stalled partials occur as submatchings of a failing state.
            # Generate that superset, then independently enumerate completions.
            multiplicity=collections.Counter(frozenset(s) for d,l in failures for s in it.combinations(l,m))
            stalls={f for f,n in multiplicity.items() if n==c*df(c-2)}
            candidates=0
            for f,n in multiplicity.items():
                assert n<=c*df(c-2)
            hall_log=[];safe_count=hall_count=0
            for f in stalls:
                ports=sorted((V-{0})-covered(f));assert len(ports)==c
                good={z:set() for z in safe};completion_count=0
                for d in ports:
                    for pairing in pairs([v for v in ports if v!=d]):
                        l=f|pairing;completion_count+=1
                        assert (d,l) in failures
                        for z in safe:
                            if z!=d:
                                k=next(b if aa==z else aa for aa,b in l if z in (aa,b))
                                if ((l-{edge(z,k)})|{edge(d,k)}) not in neg[z]:good[z].add(d)
                assert completion_count==c*df(c-2)
                usable={z for z in safe if good[z]}
                if len(usable)>c: safe_count+=1
                elif c>=3:
                    # Independent bipartite maximum matching instead of trusting
                    # producer Hall witnesses. Also record an explicit deficient set.
                    badroots={z:set(ports)-good[z] for z in usable}
                    matched={}
                    def augment(z,seen):
                        for d in badroots[z]-seen:
                            seen.add(d)
                            if d not in matched or augment(matched[d],seen):matched[d]=z;return True
                        return False
                    cardinality=sum(augment(z,set()) for z in usable)
                    assert cardinality<len(usable)
                    deficient=next(s for n in range(1,len(usable)+1) for s in it.combinations(sorted(usable),n) if len(set().union(*(badroots[z] for z in s)))<n)
                    hall_log.append({'partial':sorted(f),'subset':deficient,'bad_union':sorted(set().union(*(badroots[z] for z in deficient)))})
                    hall_count+=1
                else:
                    assert i in H and usable=={H[i]}
                if c==1 and i in H:
                    assert usable=={H[i]};d=ports[0];assert d!=H[i]
            levels.append({'c':c,'stalls':len(stalls),'safe_count':safe_count,'hall_count':hall_count,'hall_certificates':hall_log})
            if c==1 and i in H:expected_A[i]=stalls
        summary.append({'orbit':i,'failed_states':len(failures),'levels':levels})
    out['root_and_partial_accounting']=summary
    print('partial, completion, Hall audit complete',flush=True)
    inputs=read('t15_single_crossing_spectrum_inputs.json');certs=read('t15_single_crossing_spectra.json')
    assert len(inputs)==len(certs)==4200
    byid={r['id']:r for r in certs};assert len(byid)==len(certs)
    short=sorted(edge(a,b) for a in V for b in V if a<b and (a^b).bit_count()==1)
    groups=collections.defaultdict(lambda:collections.defaultdict(dict));witnesses=0
    for inp in inputs:
        i=inp['orbit'];face=inp['face'];assert i in H and face in ('A','B')
        f=canon(inp['matching']);assert len(f)*2==len(covered(f))
        cut,a,x,targets=ROWS[i];h=H[i]
        support=V-{0} if face=='A' else V-{x,h}
        assert inp['support']==sum(1<<v for v in support)
        assert inp['cyclic']==(face=='B')
        if face=='A':
            assert f in expected_A[i];root=next(iter((V-{0})-covered(f)))
            assert inp['root']==root and inp['target']==h
        else:
            assert covered(f)==V-{a,x,h,*targets} and inp['root']==a and inp['target']==-1
        assert f not in groups[i][face]
        cert=byid.pop(inp['id']);assert cert['witnesses'];union=set();edge_witness={}
        for p in cert['witnesses']:
            witnesses+=1;assert len(p)==len(set(p))==len(support) and set(p)==support
            assert p[0]==inp['root']
            if face=='A':assert p[-1]==h
            es=cycle_edges(p,face=='B');assert f<=es
            opt=es-f;assert all((aa^bb).bit_count()==1 for aa,bb in opt)
            union|=opt
            for e in opt:edge_witness[e]=p
        assert sum(1<<j for j,e in enumerate(short) if e in union)==cert['spectrum']
        groups[i][face][f]=(union,edge_witness,inp)
    assert not byid
    pair_stats=[];joins=0
    for i in H:
        cut,a,x,targets=ROWS[i];h=H[i];aa=groups[i]['A'];bb=groups[i]['B']
        assert set(aa)==expected_A[i]
        assert set(bb)==set(pairs(sorted(V-{a,x,h,*targets})))
        assert len(aa)==105 and len(bb)==945
        hist=collections.Counter()
        for fa,(ua,wa,ia) in aa.items():
            d=ia['root']
            for fb,(ub,wb,ib) in bb.items():
                common=ua&ub;assert common;hist[len(common)]+=1
                s,t=min(common);p=wa[(s,t)];q=wb[(s,t)]
                assert not {s,t}&{0,x,h}
                ca=cycle_edges(p+[16+h]);cb=cycle_edges([16+v for v in q])
                joined=(ca-{(s,t)})|(cb-{(16+s,16+t)})|{(s,16+s),(t,16+t)}
                req=fa|canon((16+u,16+v) for u,v in fb)|{(d,16+h)}
                validate_cycle(joined,set(range(32))-{0,16+x},req);joins+=1
        pair_stats.append({'orbit':i,'A':len(aa),'B':len(bb),'pairs':sum(hist.values()),'min_intersection':min(hist),'histogram':dict(sorted(hist.items()))})
    assert joins==396900
    out.update({'positive_witnesses_checked':witnesses,'input_count':len(inputs),'pair_statistics':pair_stats,'actual_30cycle_joins_checked':joins,'status':'PASS','full_T15_proved':False,'full_P6_proved':False,'review_independence':'same-family','acceptance_status':'provisional','seconds':time.time()-start})
    names=['T15_SINGLE_AVOIDED_FACE_CLOSURE.md','t15_analytic_geometry.json','q4_distance1_avoided_table_verification.json','q4_distance3_avoided_table_verification.json','Q4_CORE_AND_A4_SPLIT.md','Q4_T15_CLASSIFICATION.md','t15_single_crossing_spectrum_inputs.json','t15_single_crossing_spectra.json',Path(__file__).name]
    out['sha256']={n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in names}
    out['declared_imports']=['Previously independently audited exact Q4 two-opposite-hole negative tables (positive complement included)','Previously proved Q4 A4_4','Previously proved exact Q4 T15 classification']
    out['generated_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    dest=R/'t15_single_avoided_face_independent_check.json';dest.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('status','forward_root_states','forward_target_tests','positive_witnesses_checked','actual_30cycle_joins_checked','seconds')},indent=2),flush=True)
if __name__=='__main__':run()
