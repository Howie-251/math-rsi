"""One finite, fixed-source two-copy rightmatching question."""
from pathlib import Path
import json
import resource
import time
from collections import deque

START = time.process_time()
resource.setrlimit(resource.RLIMIT_CPU, (8, 8))
HERE = Path(__file__).resolve().parent
BASE = HERE.parents[1]
OLD = BASE/'stale_record_transfer_d8D4/loz1100_split_gate'
N, MOD = 1100, 55
PRIOR = .8

def save(fn, data):
    (HERE/fn).write_text(json.dumps(data, ensure_ascii=False, indent=2)+'\n')

def cpu():
    return time.process_time()-START

if (HERE/'ATTEMPT.json').exists():
    raise RuntimeError('one attempt already recorded; no timer restart')
save('ATTEMPT.json', {'status':'STARTED','CPU_cap':10,'read_plus_prep':PRIOR})
r = json.loads((OLD/'SOURCE_RECIPE_INPUT.json').read_text())
s = [55*a+b for a,b in r['positive_generators']+r['inverse_generators']]
assert s == r['actual_root0_neighbor_labels'] and len(set(s)) == 8
powers = [pow(2,k,55) for k in range(20)]
def mul(u,v):
    a,b = divmod(u,55); c,d = divmod(v,55)
    return 55*((a+c)%20)+(b*powers[c]+d)%55
B = [{0}, {0}|set(s)]
B.append(B[1] | {mul(x,y) for x in B[1] for y in s})
boundary = set(json.loads((OLD/'RESULT.json').read_text())['boundary_targets'])
assert len(boundary) == 674 and all(0<=x<N for x in boundary)
B.append(set(range(N))-boundary)
assert [len(z) for z in B] == [1,9,65,426]
assert all(B[a] <= B[a+1] for a in range(3))
counts = [[sum(x//55 == j for x in b) for j in range(20)] for b in B]
capacity = [sum(counts[a][j]*counts[3-a][(k-j)%20] for a in range(4) for j in range(20)) for k in range(20)]
short = [j for j in range(20) if capacity[j] < 55]
save('PHASE_CAPACITY.json', {'B_sizes':list(map(len,B)), 'B3':'complement of existing source distance4 list; no source R4 rerun','counts':counts,'relative_phase_upper_bounds':capacity,'short_phases':short,'P1_supported':bool(short),'not_sufficient_if_all_pass':True})
checked, hit, timed_out = 0, None, False
maxima = [-1]*20; witnesses = [None]*20; fullcounts = [0]*20
if short:
    status = 'COMPLETE_NO_ALL1100_BY_SINGLE_PHASE_CAPACITY'
else:
    table = [[mul(u,v) for v in range(N)] for u in range(N)]
    full = (1<<N)-1
    with (HERE/'ALL_T_RESULTS.tsv').open('w') as f:
        f.write('t\tphase\tnormal\tcovered\tfirst_missing\trelative_phase_counts\n')
        for t in range(N):
            if cpu()>7:
                timed_out=True; break
            bits=0
            for a in range(4):
                for x in B[a]:
                    xt=table[x][t]
                    for y in B[3-a]:
                        bits |= 1<<table[xt][y]
            checked += 1
            missing=full^bits
            first=(missing & -missing).bit_length()-1 if missing else -1
            q=t//55
            pc=[((bits>>(55*((q+j)%20))) & ((1<<55)-1)).bit_count() for j in range(20)]
            for j,v in enumerate(pc):
                if v>maxima[j]: maxima[j]=v; witnesses[j]=t
                if v==55: fullcounts[j]+=1
            f.write(f'{t}\t{q}\t{t%55}\t{bits.bit_count()}\t{first}\t'+','.join(map(str,pc))+'\n')
            if not missing:
                hit=t; break
    status = 'UNKNOWN_CPU_CAP' if timed_out else ('CANDIDATE_HIT' if hit is not None else 'COMPLETE_NO_ALL1100_RIGHTMATCHINGS')
    save('PHASE_ACTUAL_MAXIMA.json', {'checked':checked,'maxima':maxima,'first_max_witness_t':witnesses,'full55_parameter_counts':fullcounts,'whole_domain':checked==N,'no_second_Ut_or_postprocess_run':True})
if hit is not None:
    es=[(u,table[u][v]) for u in range(N) for v in s if u<table[u][v]]
    assert len(es)==4400
    matching=[table[u][hit] for u in range(N)]
    assert len(set(matching))==N
    es=es+[(u+N,v+N) for u,v in es]+[(u,N+matching[u]) for u in range(N)]
    with (HERE/'candidate_d9_D4_n2200.edges').open('w') as f:
        f.write('2200 9900\n')
        for u,v in es: f.write(f'{u} {v}\n')
    adj=[[] for _ in range(2200)]
    for u,v in es: adj[u].append(v);adj[v].append(u)
    assert all(len(set(row))==len(row)==9 for row in adj)
    roots,valid=0,True
    with (HERE/'PRODUCER_ROOTS.tsv').open('w') as f:
        for root in range(2200):
            if cpu()>7:
                timed_out=True;valid=False;break
            dist=[-1]*2200;dist[root]=0;q=deque([root])
            while q:
                u=q.popleft()
                for v in adj[u]:
                    if dist[v]<0: dist[v]=dist[u]+1;q.append(v)
            roots+=1;ecc=max(dist) if -1 not in dist else 2200
            f.write(f'{root}\t{ecc}\n')
            if ecc>4: valid=False;break
    save('PARAMETERS.json', {'n':2200,'m':9900,'degree':9,'t':hit,'S':s,'inherited_source_D4':True,'producer_roots':roots,'producer_full_pass':valid,'fresh_Lean_ARIS':'PENDING','new_accepted_graphs':0})
    status='CANDIDATE_PRODUCER_PASS_PENDING_FRESH' if valid else 'CANDIDATE_VERIFICATION_PENDING'
result={'status':status,'target':[9,4,2200],'public_main':1768,'checked_t':checked,'full_domain_size':1100,'full_domain_negative':bool(short) or (checked==N and hit is None),'capacity_P1_supported':bool(short),'full_cover_P2_supported':hit is not None,'hit_t':hit,'source_D4':'inherited only; no rerun','source_R3_cache_reused':True,'source_BFS_sourceR4_Lean_ARIS':0,'actual_native_CPU':cpu(),'prior_read_prep_CPU':PRIOR,'case_CPU':PRIOR+cpu(),'case_cap':10,'scope':'fixedLoz1100RIGHTsource allM(h)=h*t; not arbitrarymatching/general9D4','graph_generated':hit is not None,'new_accepted_graph_parameter_Lean':[0,0,0],'terminal':True,'next':'STOP_NO_OTHER_S_SOURCE_TWINDOW'}
save('RESULT.json',result);save('TERMINAL.json',result)
print(json.dumps(result,ensure_ascii=False),flush=True)
