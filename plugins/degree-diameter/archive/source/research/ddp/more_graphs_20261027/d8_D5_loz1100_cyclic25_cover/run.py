import resource
resource.setrlimit(resource.RLIMIT_CPU,(20,20))
import json
from pathlib import Path
import time
from collections import Counter,deque

HERE=Path(__file__).resolve().parent
N=5500;MOD=275;PHASE=20
def cpu():
    r=resource.getrusage(resource.RUSAGE_SELF);return r.ru_utime+r.ru_stime
def save(name,d):
    (HERE/name).write_text(json.dumps(d,indent=2)+'\n')
assert pow(2,20,275)==1
rows=[];hit=None;status='UNKNOWN_CPU_LIMIT';next_cursor=0
save('RUN_HANDLE.json',{'status':'RUNNING_FIXED25','pid':__import__('os').getpid(),'hard_CPU_seconds':20})
for s in range(5):
    for t in range(5):
        ordinal=5*s+t;next_cursor=ordinal
        if cpu()>=19.0:break
        case_start=cpu()
        positive=[(1,0),(12,33+55*s),(11,1),(16,19+55*t)]
        reverse=[((-j)%20,(-v*pow(2,(-j)%20,275))%275) for j,v in positive]
        assert reverse==[(19,0),(8,(77+220*s)%275),(9,38),(4,(246-55*t)%275)]
        darts=positive+reverse;factors=[pow(2,j,275) for j,v in darts]
        assert len({j for j,v in darts})==8
        for i,(j,v) in enumerate(darts):
            k=(i+4)%8
            assert (j+darts[k][0])%20==0 and (v*factors[k]+darts[k][1])%275==0
        def neighbor(u,d):
            j,x=divmod(u,275);k,v=darts[d]
            return ((j+k)%20)*275+(x*factors[d]+v)%275
        dist=[-1]*N;dist[0]=0;q=deque([0]);hist=[1,0,0,0,0,0]
        while q:
            u=q.popleft()
            if dist[u]==5:continue
            j,x=divmod(u,275);nd=dist[u]+1
            for d,(k,v) in enumerate(darts):
                w=((j+k)%20)*275+(x*factors[d]+v)%275
                if dist[w]<0:dist[w]=nd;hist[nd]+=1;q.append(w)
        assert all(0<=dist[k]<=5 for k in [0,55,110,165,220])
        reached=sum(hist);first_missing=next((i for i,d in enumerate(dist) if d<0),None)
        fibre=[0]*1100;projectionR4=set()
        for u,d in enumerate(dist):
            if d>=0:
                j,x=divmod(u,275);base=55*j+x%55;fibre[base]+=1
                if d<=4:projectionR4.add(base)
        assert len(projectionR4)==1100
        missing_state=None
        if first_missing is not None:
            j,x=divmod(first_missing,275);missing_state={'phase':j,'normal275':x,'projection_mod55':[j,x%55],'deck':x//55}
            assert missing_state['projection_mod55']!=[0,0]
        row={'candidate_ordinal':ordinal,'s':s,'t':t,'positive_generators':positive,'inverse_generators':reverse,'n':5500,'m':22000,'simple':True,'degree':8,'connectivity_paper_guarantee':True,'identity_R5_reached':reached,'identity_R5_missing':N-reached,'identity_histogram_through5':hist,'kernel_distances':{str(k):dist[k] for k in [0,55,110,165,220]},'R4_projection_count':len(projectionR4),'R5_fibre_coverage_histogram':dict(sorted(Counter(fibre).items())),'first_missing_vertex':first_missing,'first_missing_state':missing_state,'actual_global_D':None,'CPU_seconds':cpu()-case_start}
        if first_missing is None:
            row['actual_global_D']=max(i for i,c in enumerate(hist) if c);row['status']='COMPLETE_TARGET_HIT';hit=row;status='PRODUCER_FULL_TARGET_HIT'
        else:row['status']='ACTUAL_IDENTITY_R5_FAILURE'
        rows.append(row)
        with (HERE/'CASES.jsonl').open('a' if ordinal else 'w') as f:f.write(json.dumps(row,separators=(',',':'))+'\n')
        save('RUN_HANDLE.json',{'status':'RUNNING_FIXED25' if not hit else status,'pid':__import__('os').getpid(),'last_completed_ordinal':ordinal,'CPU_seconds':cpu()})
        if hit:
            with (HERE/'graph_d8_D5_n5500.edges').open('w') as f:
                f.write('5500 22000\n');edges=0
                for u in range(N):
                    ns=[neighbor(u,d) for d in range(8)]
                    assert len(set(ns))==8 and u not in ns
                    for v in ns:
                        if u<v:f.write(f'{u} {v}\n');edges+=1
                assert edges==22000
            save('HIT.json',{'status':status,'operation':'RIGHT(j,n)(k,t)=(j+k,n*2^k+t)','phase_modulus':20,'normal_modulus':275,'action':2,'vertex_encoding':'phase*275+normal',**row,'ordinary_unordered_bad_pairs':0})
            break
    if hit or cpu()>=19.0:break
else:status='COMPLETE_ALL25_NO_HIT';next_cursor=25
if hit:next_cursor=len(rows)
result={'status':status,'prediction':'SUPPORTED_COMPLETE_HIT' if hit else 'REFUTED_COMPLETE_ALL25' if len(rows)==25 else 'UNKNOWN_UNTESTED_REMAIN','target_Delta':8,'target_D':5,'savedL':5334,'n':5500,'m':22000,'objects_total':25,'objects_processed':len(rows),'actual_implicit_graphs':len(rows),'identity_R5_checks':len(rows),'hits':int(hit is not None),'actual_global_D':hit['actual_global_D'] if hit else None,'ordinary_bad_unordered_pairs':0 if hit else None,'next_cursor':next_cursor,'untested':25-len(rows),'source_BFS':0,'worker_CPU_seconds':cpu(),'hard_CPU_seconds':20,'compile_CPU_seconds':0}
save('RESULT.json',result)
save('terminal.json',{'status':status,'execution_finished':True,'pending':[],'objects_processed':len(rows),'untested':25-len(rows),'worker_CPU_seconds':cpu()})
save('RUN_HANDLE.json',{'status':status,'execution_finished':True,'worker_CPU_seconds':cpu(),'objects_processed':len(rows),'untested':25-len(rows)})
print(json.dumps(result,indent=2))
