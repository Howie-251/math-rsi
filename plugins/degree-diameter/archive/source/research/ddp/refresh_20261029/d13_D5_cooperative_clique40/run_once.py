import array
import itertools
import json
import os
from pathlib import Path
import resource
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
ROOT=Path('/inspire/hdd/global_user/mahaitong-240108120090/ar4math')
SOURCE=ROOT/'research/ddp/more_graphs_20261027/d13_D5_h9_transfer/singlefault_star_probe/continuation/graphs/graph_d13_D5_n51457.edges'
assert sys.byteorder=='little'
assert not (HERE/'TERMINAL.json').exists(), 'This fixed pool has already completed.'
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start,wall=cpu(),time.monotonic()
old=json.loads((HERE.parent/'d13_D5_static_pool_calibration/RESULT.json').read_text())
with (HERE/'S40.txt').open('w') as out:
    out.write('40\n')
    for i,row in enumerate(old['sets']):
        assert row['new_vertex']==51417+i
        out.write(' '.join(map(str,[i,len(row['neighbors'])]+row['neighbors']))+'\n')
subprocess.run(['g++','-std=c++17','-O2',str(HERE/'prepare.cpp'),'-o',str(HERE/'prepare')],check=True)
with (HERE/'PREPARED.json').open('w') as out:
    subprocess.run([str(HERE/'prepare'),str(SOURCE),str(HERE/'S40.txt'),str(HERE/'prepared')],stdout=out,check=True)
data=json.loads((HERE/'PREPARED.json').read_text());n=data['source_n'];W=data['words_per_row'];K=40
def read_masks(name):
    raw=(HERE/name).read_bytes();assert len(raw)==K*W*8
    return [int.from_bytes(raw[i*W*8:(i+1)*W*8],'little') for i in range(K)]
r3=read_masks('prepared.R3.u64.bin');r4=read_masks('prepared.R4.u64.bin');full=(1<<n)-1
def indices(mask):
    while mask:
        bit=mask & -mask;yield bit.bit_length()-1;mask^=bit
result={'scope':'fixed40 P_i from accepted current51457; arbitrary nonempty clique-helper subset', 'source_n':n,'source_m':data['source_m'],'source_reads':1,'multisource_R4_runs':40,'source_diameter_BFS':0,'solver_calls':0,'new_graphs':0}
def finish(status,**fields):
    result.update(status=status,**fields,aggregate_cpu_seconds=cpu()-start,wall_seconds=time.monotonic()-wall,pending=[])
    assert result['aggregate_cpu_seconds']<25
    (HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2),flush=True)
def save_hit(chosen,kind):
    k=len(chosen);usage={}
    for i in chosen:
        assert len(data['sets'][i]['P'])+k-1<=13
        mask=r4[i]
        for j in chosen:
            if j!=i:mask|=r3[j]
        assert mask==full
        for v in data['sets'][i]['P']:usage[v]=usage.get(v,0)+1
    cap={p['vertex']:p['capacity'] for p in data['ports']}
    assert all(u<=cap[v] for v,u in usage.items())
    added=sum(len(data['sets'][i]['P']) for i in chosen)+k*(k-1)//2
    hit={'status':'CONSTRUCTION_PARAMETERS_ONLY_NEEDS_PARENT_GRAPH_AND_ACCEPTANCE','kind':kind,'selected_indices':chosen,'P':[data['sets'][i]['P'] for i in chosen],'new_vertex_labels':list(range(n,n+k)),'all_old_edges_retained':True,'helper_edges':'complete graph on the new labels','n':n+k,'expected_m':data['source_m']+added,'max_degree_bound':13,'diameter_at_most':5}
    (HERE/'HIT_PARAMETERS.json').write_text(json.dumps(hit,indent=2)+'\n')
    finish('HIT_PARAMETERS_CHECKED',hit=hit)

direct=[i for i in range(K) if r4[i]==full]
if direct:
    save_hit([direct[0]],'K1_DIRECT');raise SystemExit

active=(1<<K)-1;chain=[];rounds=[]
while active:
    union=0
    for j in indices(active):union|=r3[j]
    removed=[]
    for i in indices(active):
        unsupported=full & ~(r4[i]|union)
        if unsupported:
            bit=unsupported & -unsupported;t=bit.bit_length()-1
            providers=[j for j in range(K) if r3[j]&bit]
            assert all(not(active>>j&1) for j in providers)
            removed.append(i)
            chain.append({'round':len(rounds),'removed_index':i,'source_added_vertex':51417+i,'witness_old_target':t,'original_R3_provider_indices':providers,'unsupported_targets_at_this_round':unsupported.bit_count()})
    if not removed:break
    rounds.append({'round':len(rounds),'active_before':list(indices(active)),'removed_indices':removed})
    for i in removed:active&=~(1<<i)
(HERE/'PROVIDER_ELIMINATION.json').write_text(json.dumps({'rounds':rounds,'deletion_chain':chain,'surviving_indices':list(indices(active)),'all_targets_unchanged':n},indent=2)+'\n')
result.update(provider_rounds=len(rounds),provider_removed=len(chain),provider_survivors=list(indices(active)))
if not active:
    finish('EXACT_FIXED_POOL_EXCLUDED_BY_PROVIDER_CHAIN');raise SystemExit

# One unified model, not a loop over clique sizes.
p3=array.array('Q');p3.frombytes((HERE/'prepared.providers3.u64.bin').read_bytes())
p4=array.array('Q');p4.frombytes((HERE/'prepared.providers4.u64.bin').read_bytes())
assert len(p3)==len(p4)==n
route_keys=set()
for t in range(n):
    providers=p3[t]&active
    for i in indices(active & ~p4[t]):
        assert providers and not(providers>>i&1)
        route_keys.add((i,providers))
clauses=[]
clauses.append([i+1 for i in indices(active)])
for i in range(K):
    if not(active>>i&1):clauses.append([-(i+1)])
for i,providers in sorted(route_keys):clauses.append([-(i+1)]+[j+1 for j in indices(providers)])
port_clause_count=0
for port in data['ports']:
    users=[i+1 for i in port['pool_indices'] if active>>i&1]
    for forbidden in itertools.combinations(users,port['capacity']+1):
        clauses.append([-v for v in forbidden]);port_clause_count+=1
# Forward prefix counter suffices for negative upper-bound uses.
limit=15
def count(i,j):return K+(i-1)*limit+j
for i in range(1,K+1):
    clauses.append([-i,count(i,1)])
    if i>1:
        for j in range(1,limit+1):clauses.append([-count(i-1,j),count(i,j)])
        for j in range(2,limit+1):clauses.append([-i,-count(i-1,j-1),count(i,j)])
for i in indices(active):
    bound=14-len(data['sets'][i]['P'])
    assert 1<=bound<=14
    clauses.append([-(i+1),-count(K,bound+1)])
cnf=HERE/'clique_pool.cnf'
with cnf.open('w') as out:
    out.write(f'p cnf {K+K*limit} {len(clauses)}\n')
    for c in clauses:out.write(' '.join(map(str,c))+' 0\n')
model={'primary_variables':K,'total_variables':K+K*limit,'clauses':len(clauses),'unique_route_implications':len(route_keys),'port_capacity_clauses':port_clause_count,'active_indices':list(indices(active)),'all_old_targets':n,'all_subset_sizes_in_one_model':True,'solver_wall_limit_seconds':15,'pre_solver_cpu_seconds':cpu()-start}
(HERE/'MODEL.json').write_text(json.dumps(model,indent=2)+'\n')
assert cpu()-start<9
command=[str(ROOT/'.tools/lean-4.24.0-linux/bin/cadical'),'-q','-t','15','-w',str(HERE/'solver.model'),str(cnf)]
with (HERE/'solver.stdout').open('w') as out:
    p=subprocess.Popen(command,stdout=out,stderr=subprocess.STDOUT)
    handle={'status':'RUNNING','pid':p.pid,'command':command,'pre_solver_cpu_seconds':cpu()-start}
    (HERE/'HANDLE.json').write_text(json.dumps(handle,indent=2)+'\n');print(json.dumps(handle),flush=True)
    code=p.wait()
result['solver_calls']=1;result['solver_exit_code']=code
(HERE/'HANDLE.json').write_text(json.dumps({'status':'TERMINAL','pid':p.pid,'exit_code':code})+'\n')
if code==10:
    positives=[]
    for line in (HERE/'solver.model').read_text().splitlines():
        if line.startswith('v '):positives.extend(int(s) for s in line[2:].split() if int(s)>0)
    chosen=sorted(v-1 for v in positives if v<=K);assert chosen
    save_hit(chosen,'SINGLE_UNIFIED_SAT')
else:
    finish('RAW_UNSAT_UNCERTIFIED' if code==20 else 'UNKNOWN',model=model)
