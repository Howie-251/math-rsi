"""Frozen actual core15 source, only the new signed low-star interface and tau boundary.
No q3 DP, new H or negative-layout search.
"""
import json,itertools,time
from pathlib import Path
D=Path(__file__).resolve().parent
S=D.parent/'MIXED_THREE_SIX_UNIT8_REALIZATION.json'
h=json.loads(S.read_text()); E=list(map(frozenset,h['edges']));V=frozenset(range(25))
deg={v:sum(v in e for e in E) for v in V};lows=[v for v in V if deg[v]==6]
assert lows==[0,1,2]
B=frozenset([5,6,7,10,13,15,19,20])
rows=[];t0=time.process_time()
for z in lows:
    H0=[(j,e) for j,e in enumerate(E) if z not in e]
    assert len(H0)==29 and all(e&B and e-B for j,e in H0)
    blocks=[e-{z} for e in E if z in e]
    assert len(blocks)==6 and sum(map(len,blocks))==24 and frozenset.union(*blocks)==V-{z}
    assert all(len(A&C)==0 for A,C in itertools.combinations(blocks,2))
    for color in ['blue','red']:
        original=B if color=='blue' else V-B-{z}
        A=[C for C in blocks if C<=original];U=frozenset.union(*A) if A else frozenset()
        N=[(j,e&original) for j,e in H0]
        assert all(F for j,F in N)
        for x in U:assert sum(x in C for C in A)+sum(x in F for j,F in N)==deg[x]
        active=[(j,F) for j,F in N if F<=U]
        small=[F for j,F in active if len(F)<=2]
        tau=0 if not small else None;witness=[]
        for q in range(1,len(U)+1):
            if tau is not None:break
            for T in itertools.combinations(sorted(U),q):
                if all(set(T)&F for F in small):tau=q;witness=list(T);break
        repair=None
        for q in range(len(U)+1):
            for T in itertools.combinations(sorted(U),q):
                R=frozenset(T)
                if all(R&C for C in A) and all(not F<=R for j,F in active):repair=list(T);break
            if repair is not None:break
        is_min=len(A)==min(sum(C<=B for C in blocks),sum(C<=V-B-{z} for C in blocks))
        rows.append(dict(z=z,color=color,is_minimum_monoblock_direction=is_min,
            positive_blocks=[sorted(C) for C in A],active_negative=[dict(edge_index=j,points=sorted(F)) for j,F in active],
            unfiltered_negative_count=29,maximum_unfiltered_signed_occ=max([deg[x] for x in U],default=0),
            tau_small=tau,minimum_hitting_set=witness,repair=repair))
        if is_min and tau<=3:assert repair is not None
out=dict(scope=__doc__,source=str(S.relative_to(D.parent.parent.parent.parent.parent)),
    source_coloring_blue=sorted(B),rows=rows,
    gate_scalar_checks={'delete_at_most_two_points':{'candidate_min':32,'negative_max':29},
       'deficits300':{'candidates':16,'blockers_at_singleton_max':11},
       'deficits210':{'candidates':24,'blockers_at_two_points_max':22},
       'deficits111':{'candidates':27,'remaining_negative_max':26}},
    cpu_seconds=time.process_time()-t0,status='PASS')
(D/'CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':'PASS','cpu_seconds':out['cpu_seconds'],'rows':[{k:r[k] for k in ('z','color','is_minimum_monoblock_direction','tau_small','repair')} for r in rows]},indent=2))
