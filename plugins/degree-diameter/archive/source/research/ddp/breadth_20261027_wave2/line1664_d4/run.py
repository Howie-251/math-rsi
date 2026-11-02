from pathlib import Path
from collections import deque, Counter
import argparse,json,random,resource,subprocess,time,sys,os

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
parser=argparse.ArgumentParser();parser.add_argument('--source',type=Path,required=True);args=parser.parse_args()
T=time.process_time();CH=resource.getrusage(resource.RUSAGE_CHILDREN);W=time.monotonic()
def used():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-T+r.ru_utime+r.ru_stime-CH.ru_utime-CH.ru_stime
def save(name,x):(OUT/name).write_text(json.dumps(x,indent=2)+'\n')
source=args.source.resolve()
lines=[tuple(map(int,s.split())) for s in source.read_text().splitlines() if s.strip() and not s.startswith('#')]
assert lines[0]==(104,208),'Source must be a normalized edge list with header104208.'
E=sorted(lines[1:]);assert len(E)==len(set(E))==208 and all(0<=u<v<104 for u,v in E)
A=[[] for _ in range(104)]
for e,(u,v) in enumerate(E):A[u].append((v,e));A[v].append((u,e))
assert all(len(x)==4 for x in A)

# A path's endpoint is x + sum b_e (occurrence parity) + sum lambda_e v_e.
# Repeated traversals of a two-point relation retain a free direction parity;
# immediate returns therefore MUST remain in the walk enumeration.
capacity_started=time.process_time();counts=[]
for root in range(104):
    forms=[set() for _ in range(104)]
    stack=[(root,0,0,0)]
    while stack:
        u,depth,bmask,distinct=stack.pop()
        sub=distinct
        while True:
            forms[u].add((bmask,sub))
            if sub==0:break
            sub=(sub-1)&distinct
        if depth<4:
            for v,e in A[u]:stack.append((v,depth+1,bmask^(1<<e),distinct|(1<<e)))
    counts.append([len(x) for x in forms])
fail=[dict(root=u,target=v,formal_affine_forms=counts[u][v]) for u in range(104) for v in range(104) if counts[u][v]<16]
cap=dict(status='PASS_NECESSARY_FORM_CAPACITY' if not fail else 'FAIL_NECESSARY_FORM_CAPACITY',fiber_points_required=16,minimum_form_capacity=min(map(min,counts)),capacity_histogram=dict(Counter(x for row in counts for x in row)),counts=counts,failing_slots=fail,CPU_seconds=time.process_time()-capacity_started,walks='All named controller walks of length0..4, retaining immediate returns',forms='(offset edge-occurrence parity, direction-choice parity); all independent b_e and nonzero v_e in F2^4',not_sufficient_for_diameter=True)
save('capacity.json',cap)
if fail:
    save('terminal.json',dict(status='STOPPED_NECESSARY_CAPACITY_OBSTRUCTION',running=False,scope_exhausted=True,fixed_controller_translation_template_excluded=True,entire_general_line_lift_family_excluded=False,generated_graphs=0,CPU_seconds=used(),witness=fail[0],pending=[]));print(json.dumps({'capacity_failed':fail[0],'CPU_seconds':used()}));sys.exit()

rng=random.Random(20261027401)
starts=[dict(offsets=[rng.randrange(16) for _ in E],directions=[rng.randrange(1,16) for _ in E]) for _ in range(4)]
save('inputs.json',dict(source=str(source),source_edges=E,base_vertices=104,n=1664,degree=8,target_D=4,fiber='F2^4, bit encoding0..15',edge_rule='For controller edge u<v join (u,x) to (v,x XOR b[e]) and (v,x XOR b[e] XOR direction[e])',starts=starts,start_seed=20261027401,mutation_seed=20261027402,updates_per_start=2000,annealing='1000*0.002^phase; four500-update cycles per start',CPU_budget_seconds=90,workers=1))
text=['104 208']+[f'{u} {v}' for u,v in E]
for s in starts:text+=[' '.join(map(str,s['offsets'])),' '.join(map(str,s['directions']))]
(OUT/'inputs.txt').write_text('\n'.join(text)+'\n')
with (OUT/'compile.log').open('w') as log:subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=OUT,stdout=log,stderr=log,check=True)
subprocess.run(['./search','calibrate'],cwd=OUT,check=True)
def expand(s):
    edges=set()
    for e,(u,v) in enumerate(E):
        for x in range(16):
            for h in [s['offsets'][e],s['offsets'][e]^s['directions'][e]]:edges.add((16*u+x,16*v+(x^h)))
    return sorted(edges)
first=expand(starts[0]);adj=[[] for _ in range(1664)]
for u,v in first:adj[u].append(v);adj[v].append(u)
assert len(first)==6656 and all(len(x)==8 for x in adj)
cppsets=[list(map(int,s.split())) for s in (OUT/'first_reachable.txt').read_text().splitlines()]
assert len(cppsets)==104 and all(len(x)==104 for x in cppsets)
miss=[]
for r in range(104):
    dist=[-1]*1664;root=16*r;dist[root]=0;q=deque([root])
    while q:
        u=q.popleft()
        if dist[u]==4:continue
        for v in adj[u]:
            if dist[v]<0:dist[v]=dist[u]+1;q.append(v)
    masks=[0]*104
    for v,d in enumerate(dist):
        if d>=0:masks[v//16]|=1<<(v%16)
    assert masks==cppsets[r],f'First-score reached-set mismatch at orbit{r}'
    miss.append(sum(d<0 for d in dist))
cached=int((OUT/'first_score.txt').read_text());assert cached==8*sum(miss)
save('first_calibration.json',dict(vertices=1664,edges=6656,degree=8,expanded_complete_adjacency=True,ordinary_BFS_roots=104,representatives=[16*r for r in range(104)],BFS_radius=4,all_reachable_sets_match=True,first_score_reused=True,bad_unordered_pairs=cached,orbit_proof='Simultaneous XOR translation in every F2^4 fiber preserves every relation, giving104 proven transitive16-point orbits; bad pairs=16*sum104 deficits/2.',CPU_used_before_production_seconds=used()))
remaining=max(0.,90.-used()-.5)
save('run.json',dict(status='RUNNING_PRODUCTION',running=True,remaining_production_CPU_seconds=remaining,CPU_used_before_production_seconds=used()))
with (OUT/'production.log').open('w') as log:
    proc=subprocess.Popen(['./search','search',str(remaining)],cwd=OUT,stdout=log,stderr=log)
    save('process.json',dict(pid=proc.pid,driver_pid=os.getpid()))
    assert proc.wait()==0
term=json.loads((OUT/'production_terminal.json').read_text());best=json.loads((OUT/'best_parameters.json').read_text());edges=expand(best)
assert len(edges)==6656
(OUT/'best.edges').write_text('1664 6656\n'+''.join(f'{u} {v}\n' for u,v in edges))
best.update(dict(n=1664,m=6656,degree=8,target_D=4,diameter='pending root independent final check',vertex_encoding='16*u+x'))
save('best.json',best)
term.update(dict(total_measured_CPU_seconds=used(),total_wall_seconds=time.monotonic()-W,preparation_and_calibration_CPU_seconds=json.loads((OUT/'first_calibration.json').read_text())['CPU_used_before_production_seconds'],capacity_CPU_seconds=cap['CPU_seconds'],running=False,workers=1,restarts=0,pending=['root independent final saved-edge check']))
save('terminal.json',term);save('run.json',term)
print(json.dumps(term))
