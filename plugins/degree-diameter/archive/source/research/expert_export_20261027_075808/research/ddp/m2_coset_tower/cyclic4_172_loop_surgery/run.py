"""Complete fixed-source two-cross-matchings to two-cycles surgery, no random starts."""
from pathlib import Path
from collections import Counter, defaultdict, deque
from itertools import combinations, product
import json, os, time

HERE=Path(__file__).resolve().parent
assert not (HERE/'terminal.json').exists(), 'No automatic restart'
start=time.process_time()
source=json.loads((HERE.parent/'cyclic4_172_balanced/best.json').read_text())
q=43; n=172
eu,ev,vs=source['edge_u'],source['edge_v'],source['voltages']
classes=defaultdict(list)
for i,pair in enumerate(zip(eu,ev)): classes[pair].append(i)
slots=sum(len(list(combinations(es,2))) for es in classes.values())*21**2
assert slots==4410
metadata={'source':'../cyclic4_172_balanced/best.json','source_bad_pairs':258,'raw_scope':slots,
          'loops_voltage_representatives':list(range(1,22)),'worker_count':1,'CPU_budget_seconds':30,
          'scope':'one fixed source;remove any two parallel cross-matchings;add one nonzero cycle in each endpoint orbit',
          'old_states_rescored':0,'BFS_roots_per_candidate':4,'no_common_scalar_normalization':True}
(HERE/'metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
(HERE/'run.json').write_text(json.dumps({'running':True,'pid':os.getpid(),'worker_count':1})+'\n')
done=0;best=None;per_pair={};hist=Counter();cursor=None;stop=False

def score(edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    assert len(edges)==602 and all(len(row)==7 for row in adj)
    rows=[];miss=[];ecc=[]
    for root in range(0,n,q):
        d=[-1]*n;d[root]=0;que=deque([root])
        while que:
            u=que.popleft()
            for v in adj[u]:
                if d[v]<0:d[v]=d[u]+1;que.append(v)
        rows.append(dict(sorted(Counter(d).items())))
        miss.append(sum(x<0 or x>3 for x in d))
        ecc.append(-1 if -1 in d else max(d))
    assert sum(miss)%2==0
    return {'root_misses':miss,'score_sum':sum(miss),'bad_unordered_pairs':q*sum(miss)//2,
            'diameter':-1 if -1 in ecc else max(ecc),'eccentricities':ecc},rows

for (a,b),es in sorted(classes.items()):
    for removed in combinations(es,2):
        keep=[i for i in range(14) if i not in removed]
        u=[eu[i] for i in keep]+[a,b];v=[ev[i] for i in keep]+[a,b]
        fixed=[vs[i] for i in keep]
        fixed_edges=set()
        for aa,bb,z in zip(u[:12],v[:12],fixed):
            for x in range(q):fixed_edges.add(tuple(sorted((q*aa+x,q*bb+(x+z)%q))))
        for alpha,beta in product(range(1,22),repeat=2):
            cursor={'pair':[a,b],'removed_edge_indices':list(removed),'loop_voltages':[alpha,beta]}
            if time.process_time()-start>=30:stop=True;break
            edges=set(fixed_edges)
            for orbit,z in [(a,alpha),(b,beta)]:
                for x in range(q):edges.add(tuple(sorted((q*orbit+x,q*orbit+(x+z)%q))))
            sc,rows=score(edges);done+=1;hist[sc['bad_unordered_pairs']]+=1
            state={'n':n,'m':602,'degree':7,'q':43,'edge_u':u,'edge_v':v,'voltages':fixed+[alpha,beta],
                   'score':sc,'root_distance_histograms':rows,'position':cursor,'evaluation_index':done}
            key=f'{a}{b}'
            if key not in per_pair or sc['score_sum']<per_pair[key]['score']['score_sum']:per_pair[key]=state
            if best is None or sc['score_sum']<best['score']['score_sum']:
                best=state
                (HERE/'best.json').write_text(json.dumps(best,indent=2)+'\n')
                (HERE/'best.edges').write_text('172 602\n'+''.join(f'{x} {y}\n' for x,y in sorted(edges)))
            if sc['score_sum']==0:stop=True;break
        if stop:break
    if stop:break

status='FOUND_D3' if best['score']['score_sum']==0 else 'CPU_LIMIT_PREFIX_SAVED' if done<slots else 'COMPLETE_FIXED_SOURCE_SURGERY_NO_SOLUTION'
out={'status':status,'running':False,'scope':slots,'processed_candidates':done,'complete_root_BFS_runs':4*done,
     'best_score':best['score'],'strict_improvement_over_source':best['score']['bad_unordered_pairs']<258,
     'last_position':cursor,'next_position':cursor if done<slots and status!='FOUND_D3' else None,
     'bad_pair_histogram':dict(sorted(hist.items())),'CPU_seconds':time.process_time()-start,
     'family_exhausted':False,'pending':['root final saved graph independent check']}
(HERE/'best_per_endpoint_pair.json').write_text(json.dumps(per_pair,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps(out,indent=2)+'\n')
(HERE/'run.json').write_text(json.dumps({'running':False,'pid':os.getpid(),'status':status,'CPU_seconds':out['CPU_seconds']})+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='bad_pair_histogram'},indent=2))
