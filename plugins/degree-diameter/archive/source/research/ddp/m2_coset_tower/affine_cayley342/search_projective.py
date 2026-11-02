#!/usr/bin/env python3
"""One complete 381-class actual Cayley search, after saved upstream exclusions."""
from collections import Counter, deque
from pathlib import Path
import json
import os
import resource
import time

Q=19
K=18
N=342
BASE=Path(__file__).resolve().parent
POWERS=[pow(2,j,Q) for j in range(K)]

def multiply(a,b):
    x,j=a%Q,a//Q
    y,k=b%Q,b//Q
    return (x+POWERS[j]*y)%Q+Q*((j+k)%K)

def inverse(a):
    x,j=a%Q,a//Q
    return (-POWERS[-j%K]*x)%Q+Q*(-j%K)

def evaluate(generators):
    adjacency=[[multiply(u,s) for s in generators] for u in range(N)]
    distance=[-1]*N;distance[0]=0;queue=deque([0])
    while queue:
        u=queue.popleft()
        for v in adjacency[u]:
            if distance[v]<0:
                distance[v]=distance[u]+1;queue.append(v)
    connected=-1 not in distance
    return adjacency,{'n':N,'m':4*N,'degree':8,'connected':connected,
                      'diameter':max(distance) if connected else None,
                      'root_deficit_gt3_or_unreachable':sum(d<0 or d>3 for d in distance),
                      'root_distance_histogram':dict(sorted(Counter(distance).items()))}

def save_best(parameters,adjacency,result):
    edges=[(u,v) for u,row in enumerate(adjacency) for v in row if u<v]
    assert len(edges)==1368
    with (BASE/'production.best.edges').open('w') as stream:
        stream.write('342 1368\n')
        for u,v in edges:stream.write(f'{u} {v}\n')
    result['bad_unordered_pairs']=171*result['root_deficit_gt3_or_unreachable']
    (BASE/'production.best.json').write_text(json.dumps(dict(parameters,graph=result),indent=2)+'\n')

def main():
    start=time.process_time()
    assert not (BASE/'production.terminal.json').exists(), 'No restart of completed batch.'
    assert len(set(POWERS))==18 and POWERS[9]==18
    for a in range(N):assert multiply(a,inverse(a))==multiply(inverse(a),a)==0
    input_file=BASE.parent/'axis_parameter_capacity/agl19_d8.symbolic_survivors.json'
    upstream=json.loads(input_file.read_text())
    assert len(upstream)==1
    row=upstream[0];phases=row['pair_phases']
    assert row['id']==543 and phases==[2,3,4,8] and row['pairs']==4 and row['involutions']==0
    assert row['symbolic_pass'] and row['projective_marked_input_bound']==381
    anchor=next(i for i,j in enumerate(phases) if j!=0)
    free=[i for i in range(4) if i!=anchor]
    run={'status':'RUNNING','pid':os.getpid(),'worker_count':1,'running':True,'CPU_budget_seconds':30,'scope':381,'source':str(input_file)}
    (BASE/'production.run.json').write_text(json.dumps(run,indent=2)+'\n')
    done=legal=illegal=0;best_missing=N+1;hist=Counter();found=False;timed_out=False
    with (BASE/'production.cases.tsv').open('w') as cases:
        cases.write('cursor\tx0\tx1\tx2\tx3\tlegal\tmissing\tdiameter\n')
        for lead in range(3):
            for code in range(Q**(2-lead)):
                if time.process_time()-start>=29:
                    timed_out=True;break
                fields=[0]*4;fields[free[lead]]=1
                tail=code
                for slot in free[lead+1:]:fields[slot]=tail%Q;tail//=Q
                generators=[]
                for x,j in zip(fields,phases):
                    s=x+Q*j;generators.extend((s,inverse(s)))
                valid=len(set(generators))==8 and 0 not in generators
                cursor=done;done+=1
                if not valid:
                    illegal+=1;cases.write('\t'.join(map(str,[cursor]+fields+[0,-1,-1]))+'\n');continue
                legal+=1
                adjacency,result=evaluate(generators)
                missing=result['root_deficit_gt3_or_unreachable'];hist[missing]+=1
                cases.write('\t'.join(map(str,[cursor]+fields+[1,missing,result['diameter']]))+'\n')
                if missing<best_missing:
                    best_missing=missing
                    parameters={'encoding':'x+19*j','source_pattern_id':543,'projective_index':cursor,'anchor_slot':anchor,'phases':phases,'fields':fields,'S':generators}
                    save_best(parameters,adjacency,result)
                if missing==0:
                    found=True;print(f'FOUND_D3 cursor={cursor}',flush=True);break
            if found or timed_out:break
    status='FOUND_D3' if found else 'CPU_LIMIT_INCOMPLETE' if timed_out else 'COMPLETE_NO_SOLUTION'
    if not found and not timed_out:assert done==381 and legal==381 and illegal==0
    usage=resource.getrusage(resource.RUSAGE_SELF)
    terminal={'status':status,'raw_scope':381,'raw_representatives_checked':done,'legal_graphs_checked':legal,'illegal_representatives':illegal,'root_BFS_runs':legal,'minimum_root_deficit':best_missing,'root_deficit_histogram':dict(sorted(hist.items())),'next_cursor':done,'running':False,'CPU_seconds':time.process_time()-start,'recorded_process_CPU_seconds':usage.ru_utime+usage.ru_stime,'source_pattern_id':543,'upstream_plain_patterns':715,'upstream_plain_survivors':100,'upstream_symbolic_survivors':1,'scope_claim_requires_upstream_exclusions':True}
    (BASE/'production.terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
    run.update(status=status,running=False,exit_code=0,next_cursor=done,recorded_process_CPU_seconds=terminal['recorded_process_CPU_seconds'])
    (BASE/'production.run.json').write_text(json.dumps(run,indent=2)+'\n')
    print(json.dumps(terminal,indent=2))

if __name__=='__main__':main()
