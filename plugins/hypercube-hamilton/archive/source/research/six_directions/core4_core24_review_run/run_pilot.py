"""Bounded experiment; random Q6 coverage is explicitly NOT exhaustive."""
import itertools, json, random, subprocess, time, hashlib, platform
from pathlib import Path
ROOT=Path(__file__).resolve().parent
SEED=20261031
rng=random.Random(SEED)

def edges(n):
    return [(x,x^(1<<i)) for x in range(1<<n) for i in range(n) if not x&(1<<i)]

def matchings_avoiding_zero(n):
    es=[e for e in edges(n) if 0 not in e]
    def rec(i,used,m):
        if i==len(es):yield list(m);return
        yield from rec(i+1,used,m)
        a,b=es[i]
        if not ((1<<a|1<<b)&used):
            yield from rec(i+1,used|1<<a|1<<b,m+[(a,b)])
    yield from rec(0,0,[])

def maximal(n,m):
    covered={z for e in m for z in e}
    return all(a in covered or b in covered for a,b in edges(n) if a and b)

cases=[]; counts={}
for n in (2,3):
    all_m=list(matchings_avoiding_zero(n))
    maximal_m=[m for m in all_m if maximal(n,m)]
    counts[str(n)]={'all_matchings_avoiding_zero':len(all_m),'relative_maximal':len(maximal_m)}
    for m in all_m:
        for v in range(1,1<<n):
            if v.bit_count()%2:cases.append(dict(n=n,u=0,v=v,matching=m,scope='exhaustive_small'))

es=edges(6); seeds=[]
for i in range(24):
    trial=[e for e in es if 0 not in e];rng.shuffle(trial)
    covered=set();m=[]
    for a,b in trial:
        if a not in covered and b not in covered:m.append((a,b));covered.update((a,b))
    seeds.append(('random_relative_maximal',m))
for direction in range(6):
    m=[e for e in es if e[0]^e[1]==1<<direction and 0 not in e]
    seeds.append(('punctured_coordinate_perfect',m))
for i in range(6):
    m=[e for e in es if e[0]^e[1]==1<<i and 0 not in e and (e[0].bit_count()%2)==0]
    trial=[e for e in es if 0 not in e];rng.shuffle(trial);used={z for e in m for z in e}
    for a,b in trial:
        if a not in used and b not in used:m.append((a,b));used.update((a,b))
    seeds.append(('half_layer_seeded_relative_maximal',m))
for label,m in seeds:
    for v in range(1,64):
        if v.bit_count()%2:cases.append(dict(n=6,u=0,v=v,matching=m,scope=label))

inputs=[]
for c in cases:
    mate=[-1]*(1<<c['n'])
    for a,b in c['matching']:mate[a]=b;mate[b]=a
    inputs.append(' '.join(map(str,[c['n'],c['v'],200000,*mate])))
(ROOT/'pilot_cases.txt').write_text('\n'.join(inputs)+'\n')
start=time.monotonic()
proc=subprocess.run([str(ROOT/'path_search.exe')],input='\n'.join(inputs)+'\n',text=True,capture_output=True,timeout=180,check=True)
lines=proc.stdout.splitlines();assert len(lines)==len(cases)
for c,line in zip(cases,lines):
    parts=line.split();c['status']=parts[0];c['nodes']=int(parts[1]);c['path']=list(map(int,parts[2:]))
summary={s:sum(c['status']==s for c in cases) for s in ('FOUND','UNKNOWN','EXHAUSTED')}
output={'seed':SEED,'elapsed_seconds':time.monotonic()-start,'platform':platform.platform(),
        'node_cap_per_case':200000,'small_exhaustion':counts,'q6_matching_samples':len(seeds),
        'summary':summary,'scope':'All Q2/Q3 matchings avoiding zero; sampled Q6 matchings, all odd endpoints.',
        'source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'path_search.cpp',ROOT/'run_pilot.py']},'cases':cases}
(ROOT/'pilot_results.json').write_text(json.dumps(output,indent=2),encoding='utf8')
print(json.dumps({k:v for k,v in output.items() if k!='cases'},indent=2))
