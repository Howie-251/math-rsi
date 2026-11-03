from pathlib import Path
from collections import deque
import json, random, resource, subprocess, time, sys

P=Path(__file__).resolve().parent
assert not (P/'terminal.json').exists(), 'Do not restart this completed profile.'
start_self=time.process_time()
def child_cpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return r.ru_utime+r.ru_stime
start_children=child_cpu();wall=time.monotonic()
scout=P.parent/'two_orbit128_scout'
capacity=json.loads((scout/'RESULT.json').read_text())
tight=json.loads((scout/'TIGHT_SUM.json').read_text())
conditions={r['phase_mask']:r for r in tight['records']}
rng=random.Random(20261027214)
rules=[]

def mul(g,h):
    x,s=g;y,t=h
    return ((x+(-1)**s*y+16*s*t)%32,s^t)

def code(g):return g[0]+32*g[1]

def tuple_of(c):return c%32,c//32

def legal(xx,bits):
    c=[x+32*s for x,s in zip(xx,bits)]
    return c[0] not in (0,16) and c[1] not in (0,16) and len({0,c[2],c[3],c[4]})==4

for survivor in capacity['survivors']:
    phase=survivor['phase_mask'];bits=survivor['phases_a_b_h1_h2_h3']
    assert sum(bits[:2])==1
    odd=bits[:2].index(1)
    eqs=conditions[phase]['equations']
    assert conditions[phase]['consistent']
    nontrivial=[e for e in eqs if any(e['coefficient_sum']) or e['rhs']]
    dependent=bool(nontrivial)
    if dependent:
        first=next(e for e in nontrivial if e['coefficient_sum'][odd]%4==2)
        eqs=[first]+[e for e in eqs if e is not first]
        # Every other tight equation is an exact scalar multiple mod16
        # after dividing its even coefficients/rhs by2.
        a=[v//2 for v in first['coefficient_sum']];b=first['rhs']//2
        ai=pow(a[odd],-1,16)
        for e in eqs:
            aa=e['coefficient_sum'];bb=e['rhs']
            assert all(v%2==0 for v in aa) and bb%2==0
            aa=[v//2 for v in aa];bb//=2
            scalar=aa[odd]*ai%16
            assert all((x-scalar*y)%16==0 for x,y in zip(aa,a)) and (bb-scalar*b)%16==0
    for draw in range(10000):
        xx=[rng.randrange(32) for _ in range(5)]
        if dependent:
            e=eqs[0];residue=(e['rhs']-sum(e['coefficient_sum'][j]*xx[j] for j in range(5) if j!=odd))//2
            xx[odd]=(residue*pow(e['coefficient_sum'][odd]//2,-1,16))%16+16*rng.randrange(2)
        if not legal(xx,bits):continue
        assert all((sum(a*x for a,x in zip(e['coefficient_sum'],xx))-e['rhs'])%32==0 for e in eqs)
        break
    else:raise AssertionError('No legal initial parameter found.')
    rules.append(dict(phase=phase,bits=bits,odd=odd,dependent=dependent,equations=eqs,x=xx,group_codes=[x+32*s for x,s in zip(xx,bits)],draws=draw+1))
assert len(rules)==14 and sum(r['dependent'] for r in rules)==8
(P/'inputs.json').write_text(json.dumps(dict(group='Q64',n=128,degree=6,target_D=3,variables=['a','b','h1','h2','h3'],cross_anchor=0,start_seed=20261027214,kick_seed=20261027215,starts=rules,segments_per_start=3,max_strict_steps_per_segment=12,constrained_neighbor_count=125,direct_neighbor_count=155,kick='Two distinct free-parameter positions changed to legal alternatives, one scored final state.',CPU_budget_seconds=60,workers=1),indent=2)+'\n')
with (P/'rules.txt').open('w') as f:
    f.write(str(len(rules))+'\n')
    for r in rules:
        f.write(f"{r['phase']} {r['odd']} {int(r['dependent'])} {len(r['equations'])}\n")
        for e in r['equations']:f.write(' '.join(map(str,e['coefficient_sum']+[e['rhs']]))+'\n')
        f.write(' '.join(map(str,r['x']))+'\n')

# Independent direct tuple expansion of the first formal production state.
r=rules[0];a,b,h1,h2,h3=map(tuple_of,r['group_codes']);hh=[(0,0),h1,h2,h3]
es=set()
for x in range(32):
    for s in range(2):
        g=(x,s);u=code(g)
        es.add(tuple(sorted((u,code(mul(g,a))))))
        es.add(tuple(sorted((64+u,64+code(mul(g,b))))))
        for h in hh:es.add((u,64+code(mul(g,h))))
assert len(es)==384 and all(u<v for u,v in es)
adj=[[] for _ in range(128)]
for u,v in es:adj[u].append(v);adj[v].append(u)
assert [len(x) for x in adj]==[6]*128
rows=[]
for root in [0,64]:
    d=[-1]*128;d[root]=0;q=deque([root])
    while q:
        u=q.popleft()
        for v in adj[u]:
            if d[v]<0:d[v]=d[u]+1;q.append(v)
    rows.append([z if 0<=z<=3 else -1 for z in d])
miss=[row.count(-1) for row in rows]
with (P/'first_expected.txt').open('w') as f:
    f.write('384\n')
    for u,v in sorted(es):f.write(f'{u} {v}\n')
    for row in rows:f.write(' '.join(map(str,row))+'\n')
(P/'first.python_calibration.json').write_text(json.dumps(dict(status='INDEPENDENT_FIRST_FORMAL_STATE',edges=384,vertices=128,degree=6,roots=[0,64],radius3_distance_entries=256,root_misses=miss,bad_unordered_pairs=32*sum(miss),method='Direct Python pair-coordinate group product; build all edges; ordinary two-root BFS; truncate distances beyond target radius.'),indent=2)+'\n')

compile_start=time.monotonic()
with (P/'compile.log').open('w') as log:
    subprocess.run(['g++','-std=c++17','-O3','search.cpp','-o','search'],cwd=P,stdout=log,stderr=subprocess.STDOUT,check=True)
prep=(time.process_time()-start_self)+(child_cpu()-start_children)
limit=60-prep-0.25
assert limit>0, 'Preparation exhausted budget; do not restart.'
run=dict(status='RUNNING',driver_pid=__import__('os').getpid(),worker_count=1,preparation_CPU_seconds=prep,production_CPU_limit=limit,restarts=0)
(P/'run.json').write_text(json.dumps(run,indent=2)+'\n')
with (P/'search.log').open('w') as log:
    completed=subprocess.run([str(P/'search'),'rules.txt','first_expected.txt',str(limit),'20261027215'],cwd=P,stdout=log,stderr=subprocess.STDOUT)
assert completed.returncode==0, (P/'search.log').read_text()
terminal=json.loads((P/'search.terminal.json').read_text())
calibration=json.loads((P/'first.cpp_calibration.json').read_text())
assert calibration['bad_unordered_pairs']==32*sum(miss) and calibration['first_score_reused']
total=(time.process_time()-start_self)+(child_cpu()-start_children)
terminal.update(preparation_CPU_seconds=prep,total_measured_CPU_seconds=total,wall_seconds=time.monotonic()-wall,CPU_budget_seconds=60,workers=1,constrained_phase_starts=8,direct_phase_starts=6,phase_patterns=14,first_calibration_edges=384,first_calibration_BFS_roots=2,first_calibration_entries=256,first_score_reused=True)
(P/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n');(P/'run.json').write_text(json.dumps(terminal,indent=2)+'\n')
assert total<=60
print(json.dumps({k:terminal[k] for k in ['status','starts_completed','segments_entered','legal_score_evaluations','complete_neighborhoods','strict_moves','best_bad_unordered_pairs','total_measured_CPU_seconds','wall_seconds']}))
