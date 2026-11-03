"""Pure C3-coset action: reuse the existing PSL matrices, search new orbit unions."""
from pathlib import Path
from collections import Counter, deque
import json
import pickle
import resource
import runpy
import time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[4]
START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(90,95))
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_candidate_evaluation']
OLD=ROOT/'research/ddp/breadth_20261027/psl2_23_orbits3542_d5'
with (OLD/'prepared.pkl').open('rb') as f: old=pickle.load(f)
math=runpy.run_path(str(OLD/'run.py'))
mul,inv=math['mul'],math['inv']
G,IX,H=old['group_matrices'],old['matrix_index'],old['K']
reps,lookup=old['BR'],old['BL']
N=2024
assert len(G)==6072 and len(reps)==N and len(set(H))==3 and reps[0]==(1,0,0,1)
perms=[[x-1518 for x in p[1518:]] for p in old['perms']]
assert all(sorted(p)==list(range(N)) for p in perms)
bits=[1<<i for i in range(N)]


def save(name,data):
    (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')


def reachable(masks):
    seen=front=1
    for _ in range(5):
        nxt=0
        while front:
            bit=front&-front;front-=bit;nxt|=masks[bit.bit_length()-1]
        front=nxt&~seen;seen|=front
    return seen


def orbital_masks(item):
    # Orbit of unordered rootedge under the alreadyverified two left actions.
    edges={item['representative']};todo=[item['representative']]
    while todo:
        a,b=divmod(todo.pop(),N)
        for p in perms:
            u,v=p[a],p[b]
            if u>v:u,v=v,u
            code=u*N+v
            if code not in edges:edges.add(code);todo.append(code)
    assert len(edges)==N*item['degree']//2
    masks=[0]*N
    for code in edges:
        a,b=divmod(code,N)
        assert a!=b
        masks[a]|=bits[b];masks[b]|=bits[a]
    assert masks[0]==sum(bits[v] for v in item['root_neighbors'])
    return masks


def main():
    assert not (OUT/'RESULT.json').exists(),'This fixedscope already has a result; do not rerun.'
    classes={}
    for v,g in enumerate(reps[1:],1):
        neighbors=tuple(sorted({lookup[IX[mul(h,z)]] for h in H for z in (g,inv(g))}))
        assert 0 not in neighbors
        classes.setdefault(neighbors,v)
    histogram=Counter(map(len,classes))
    assert histogram=={1:5,2:1,3:80,6:296}
    items=[dict(id=i,degree=len(neighbors),representative=v,root_neighbors=list(neighbors),
                representative_matrix=list(reps[v]))
           for i,(neighbors,v) in enumerate(sorted(classes.items(),key=lambda x:x[1]))]
    low=[x for x in items if x['degree']<6]
    choices=[(x['id'],) for x in items if x['degree']==6]
    def compose(pos,left,chosen):
        if not left:
            choices.append(tuple(chosen));return
        for j in range(pos,len(low)):
            degree=low[j]['degree']
            if degree<=left:compose(j+1,left-degree,chosen+[low[j]['id']])
    compose(0,6,[])
    assert len(choices)==len(set(choices))==4661
    by_id={x['id']:x for x in items}
    normalizer={lookup[IX[g]] for g in G if {mul(mul(g,h),inv(g)) for h in H}==set(H)}
    assert len(normalizer)==8
    normalizer_mask=sum(bits[v] for v in normalizer)
    save('SCOPE.json',dict(group='PSL2F23',order=6072,C3_matrices=H,n=N,target_degree=6,
                           subgroup_source='ExistingpreparedK_C3',orbital_histogram=histogram,
                           items=items,choices=choices,normalizer_cosets=sorted(normalizer),
                           complete_scope_count=len(choices),source_search_rerun=False))
    cache={};done=0;hit=None;type_stats={};best_missing=N
    preparation=time.process_time()-START
    for index,choice in enumerate(choices):
        if time.process_time()-START>89:
            break
        partial=[]
        for oid in choice:
            item=by_id[oid]
            if item['degree']==6:
                partial.append(orbital_masks(item))
            else:
                if oid not in cache:cache[oid]=orbital_masks(item)
                partial.append(cache[oid])
        masks=partial[0] if len(partial)==1 else [0]*N
        if len(partial)>1:
            for row in partial:masks=[a|b for a,b in zip(masks,row)]
        assert masks[0].bit_count()==6
        seen=reachable(masks);missing=N-seen.bit_count();done+=1
        profile='+'.join(map(str,sorted((by_id[x]['degree'] for x in choice),reverse=True)))
        stats=type_stats.setdefault(profile,dict(cases=0,min_missing=N,max_missing=0,
                                                normalizer_reachable_min=8,normalizer_reachable_max=0))
        stats['cases']+=1;stats['min_missing']=min(stats['min_missing'],missing)
        stats['max_missing']=max(stats['max_missing'],missing)
        nn=(seen&normalizer_mask).bit_count()
        stats['normalizer_reachable_min']=min(stats['normalizer_reachable_min'],nn)
        stats['normalizer_reachable_max']=max(stats['normalizer_reachable_max'],nn)
        best_missing=min(best_missing,missing)
        if done==1:
            assert all(row.bit_count()==6 for row in masks)
            dist=[-1]*N;dist[0]=0;todo=deque([0])
            while todo:
                a=todo.popleft()
                if dist[a]==5:continue
                row=masks[a]
                while row:
                    bit=row&-row;row-=bit;b=bit.bit_length()-1
                    if dist[b]<0:dist[b]=dist[a]+1;todo.append(b)
            assert sum(bits[i] for i,x in enumerate(dist) if x>=0)==seen
            save('first_calibration.json',dict(choice=choice,degree6_every_vertex=True,
                 one_ordinary_root_R5_matches_bitset=True,root_missing=missing))
        if not missing:
            assert all(row.bit_count()==6 for row in masks)
            edgefile=OUT/'hit2024.edges'
            with edgefile.open('w') as f:
                f.write(f'{N} {N*3}\n')
                for a,row in enumerate(masks):
                    while row:
                        bit=row&-row;row-=bit;b=bit.bit_length()-1
                        if a<b:f.write(f'{a} {b}\n')
            hit=dict(n=N,m=N*3,max_degree=6,target_D=5,choice=choice,
                     orbital_representatives=[by_id[x] for x in choice],C3_matrices=H,
                     coset_representatives=reps,edgefile=edgefile.name,
                     action='LeftPSL2F23 on rightcosetsgH, fullG-orbitsofselectedunorderedpairs.',
                     independent_expanded_edge_check_pending=True,record_claimed=False)
            save('hit_parameters.json',hit);break
        if done==8:
            elapsed=time.process_time()-START-preparation
            forecast=preparation+elapsed*len(choices)/8
            save('profile8.json',dict(completed=8,CPU_seconds=elapsed,
                                    projected_total_CPU_seconds=forecast,budget=90))
            if forecast>88:break
    complete=done==len(choices)
    status='COMPLETE_HIT_AWAIT_ROOT' if hit else 'COMPLETE_NO_HIT' if complete else 'BUDGET_UNKNOWN_NO_HIT'
    result=dict(status=status,n=N,target_Delta=6,target_D=5,savedL=1518,
                evaluated=done,total=4661,unprocessed=4661-done,complete=complete,
                full_hits=int(hit is not None),minimum_root_R5_missing=best_missing,
                type_stats=type_stats,CPU_seconds=time.process_time()-START,
                old_source_BFS=0,old3542_search_rerun=False,full_source_BFS=0,
                scope='OnlythisnaturalPSL2F23/C3actionandallunionsofitsundirecteddegree6orbitals.',
                actual_D=None,ordinary_bad_unordered_pairs=None)
    save('RESULT.json',result);save('terminal.json',result)
    print(json.dumps(result))


if __name__=='__main__':main()
