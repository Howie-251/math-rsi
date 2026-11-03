from pathlib import Path
from collections import deque
import json,random,resource,subprocess,time

OUT=Path(__file__).resolve().parent
P=OUT.parents[3]
T=time.process_time();CH=resource.getrusage(resource.RUSAGE_CHILDREN);W=time.monotonic()
def used():
    x=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-T+x.ru_utime+x.ru_stime-CH.ru_utime-CH.ru_stime
def save(name,x):(OUT/name).write_text(json.dumps(x,indent=2)+'\n')
source=P/'research/ddp/m1_sources/graph_6_3_n120.txt'
E=sorted(tuple(map(int,line.split())) for line in source.read_text().splitlines() if line and not line.startswith('#'))
A=[set() for _ in range(120)]
for u,v in E:A[u].add(v);A[v].add(u)
assert len(E)==360 and all(len(x)==6 for x in A)
single=[int(u//60==v//60) for u,v in E]
assert sum(single)==60
assert all(sum(single[e] for e,(u,v) in enumerate(E) if x in (u,v))==1 for x in range(120))
rng=random.Random(20261027304)
starts=[{'offsets':[rng.randrange(8) for _ in E],'directions':[0 if s else rng.randrange(1,8) for s in single],'internal_shifts':[rng.randrange(1,8) for _ in A]} for _ in range(4)]
save('inputs.json',{'source':str(source),'n':960,'degree':12,'target_D':3,'source_edges':E,'single_matching_flags':single,'source_perfect_matching':[E[i] for i,s in enumerate(single) if s],'fiber':'F2^3 encoded by x0+2x1+4x2','construction':'For each source edge u<v, join (u,x) to (v,x XOR b[e]), and also to (v,x XOR b[e] XOR v[e]) unless selected single matching. In each source block add x--x XOR s[u].','starts':starts,'start_seed':20261027304,'mutation_seed':20261027305,'updates_per_start':5000,'start_count':4,'annealing':'150*0.004^phase, phase=(step mod1250)/1249','CPU_budget_seconds':60,'workers':1})
lines=['120 360']+[f'{u} {v} {s}' for (u,v),s in zip(E,single)]
for st in starts:
    for name in ['offsets','directions','internal_shifts']:lines.append(' '.join(map(str,st[name])))
(OUT/'inputs.txt').write_text('\n'.join(lines)+'\n')
with (OUT/'compile.log').open('w') as log:
    subprocess.run(['g++','-O3','-std=c++17','search.cpp','-o','search'],cwd=OUT,stdout=log,stderr=log,check=True)
subprocess.run(['./search','calibrate'],cwd=OUT,check=True)
def expand(st):
    edges=set()
    for e,(u,v) in enumerate(E):
        shifts=[st['offsets'][e]]
        if not single[e]:shifts.append(st['offsets'][e]^st['directions'][e])
        for x in range(8):
            for h in shifts:edges.add(tuple(sorted((8*u+x,8*v+(x^h)))))
    for u,s in enumerate(st['internal_shifts']):
        for x in range(8):edges.add(tuple(sorted((8*u+x,8*u+(x^s)))))
    return sorted(edges)
def adjacent(edges):
    a=[[] for _ in range(960)]
    for u,v in edges:a[u].append(v);a[v].append(u)
    return a
firstedges=expand(starts[0]);adj=adjacent(firstedges)
assert len(firstedges)==5760 and all(len(a)==12 for a in adj) and all(u!=v for u,v in firstedges)
data=list(map(int,(OUT/'first_score.txt').read_text().split()));cpp=data[0];cppmiss=data[1:];assert len(cppmiss)==120
miss=[]
for root in range(960):
    dist=[-1]*960;dist[root]=0;q=deque([root]);reached=1
    while q:
        u=q.popleft()
        if dist[u]==3:continue
        for v in adj[u]:
            if dist[v]<0:dist[v]=dist[u]+1;q.append(v);reached+=1
    miss.append(960-reached)
assert all(miss[8*u+x]==cppmiss[u] for u in range(120) for x in range(8))
assert sum(miss)//2==cpp
save('first_calibration.json',{'all_960_adjacencies_expanded':True,'vertices':960,'edges':5760,'minimum_degree':12,'maximum_degree':12,'ordinary_BFS_roots':960,'BFS_radius':3,'all_root_deficits_match_proven_translation_orbits':True,'bad_unordered_pairs':cpp,'cpp_score_equal':True,'formal_first_score_reused':True,'CPU_used_before_production_seconds':used()})
remaining=max(0.,60.-used()-0.5)
save('run.json',{'status':'RUNNING_PRODUCTION','remaining_production_CPU_seconds':remaining,'CPU_used_before_production_seconds':used(),'wall_started':W,'running':True})
with (OUT/'production.log').open('w') as log:
    proc=subprocess.Popen(['./search','search',str(remaining)],cwd=OUT,stdout=log,stderr=log)
    save('process.json',{'pid':proc.pid,'driver_pid':__import__('os').getpid()})
    assert proc.wait()==0
term=json.loads((OUT/'production_terminal.json').read_text());best=json.loads((OUT/'best_parameters.json').read_text());edges=expand(best)
(OUT/'best.edges').write_text('960 5760\n'+''.join(f'{u} {v}\n' for u,v in edges))
assert len(edges)==5760
best.update({'n':960,'edges':5760,'minimum_degree':12,'maximum_degree':12,'target_D':3,'vertex_encoding':'8*u+x','diameter':'pending root independent final check'})
save('best.json',best)
term.update({'running':False,'workers':1,'restarts':0,'total_measured_CPU_seconds':used(),'total_wall_seconds':time.monotonic()-W,'preparation_and_calibration_CPU_seconds':json.loads((OUT/'first_calibration.json').read_text())['CPU_used_before_production_seconds'],'full_graph_generated':True,'new_full_source_calibration_BFS_roots':960,'best_final_independent_BFS_roots':0,'pending':['root-independent-final-check'],'source_perfect_matching_size':60})
save('terminal.json',term);save('run.json',term)
print(json.dumps(term))
