import collections,json,math,os,resource,subprocess,time
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[5]
# Locate the project from the unambiguous fixed source pathname.
while not (ROOT/'research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.header.edges').is_file():
    ROOT=ROOT.parent
t0=time.process_time();wall=time.monotonic();c0=resource.getrusage(resource.RUSAGE_CHILDREN)
def put(name,x): (HERE/name).write_text(json.dumps(x,indent=2)+'\n')
def total():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-t0+c.ru_utime+c.ru_stime-c0.ru_utime-c0.ru_stime
put('HANDLE.json',{'status':'RUNNING','pid':os.getpid(),'started_utc':time.strftime('%Y-%m-%dT%H:%M:%SZ',time.gmtime())})
pool=json.load(open(HERE.parent/'LABEL_POOL.json'))
ids=list(map(int,(HERE.parent/'source_vertex_ids.txt').read_text().split()))
assert ids==pool['source_vertex_ids']==sorted(set(ids)) and len(ids)==6912
assert len(pool['controllers'])==192 and all(len(x['original_labels36'])==36 for x in pool['controllers'])
relabel={v:i for i,v in enumerate(ids)}
src=ROOT/'research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.header.edges'
edges=[];degrees=[0]*len(ids);source_edge_count=0
with src.open() as f:
    assert tuple(map(int,next(f).split()))==(15552,116316)
    for line in f:
        u,v=map(int,line.split());source_edge_count+=1
        if u in relabel and v in relabel:
            a,b=relabel[u],relabel[v];assert a<b
            edges.append((a,b));degrees[a]+=1;degrees[b]+=1
assert source_edge_count==116316 and len(edges)==len(set(edges))
out=HERE/'graph_induced_n6912.edges'
with out.open('w') as f:
    f.write(f'{len(ids)} {len(edges)}\n')
    f.writelines(f'{a} {b}\n' for a,b in edges)
profile={'n':len(ids),'m':len(edges),'min_degree':min(degrees),'max_degree':max(degrees),'degree_histogram':dict(sorted(collections.Counter(degrees).items())),'simple':True,'actual_induced':True,'source_edges_scanned_once':source_edge_count,'old_source_BFS':0,'label_order':'sorted original IDs, new label=position','labels':'../source_vertex_ids.txt'}
put('DEGREE_PROFILE.json',profile)
put('INPUT.json',{'source':str(src.relative_to(ROOT)),'source_n':15552,'source_m':116316,'label_pool':'../LABEL_POOL.json','actual_graph':out.name,'candidate_count':1,'budget_aggregate_cpu_seconds':30,'worker_count':1})
if max(degrees)>13:
    bad=next(i for i,d in enumerate(degrees) if d>13)
    result={'status':'DEGREE_GATE_REFUTED','actual_graph_count':1,'actual_n':len(ids),'actual_m':len(edges),'actual_max_degree':max(degrees),'first_degree_violation':{'new_label':bad,'source_label':ids[bad],'degree':degrees[bad]},'target_degree':13,'target_D':4,'global_D':None,'new_graph_BFS_roots':0,'old_source_BFS':0,'degree_prediction':'REFUTED','D_prediction':'UNTESTED_AFTER_DEGREE_FAILURE','record_count':0}
else:
    cp=subprocess.run(['g++','-O3','-std=c++17',str(HERE/'radius4.cpp'),'-o',str(HERE/'radius4')],capture_output=True,text=True)
    (HERE/'compile.stderr').write_text(cp.stderr)
    if cp.returncode: raise RuntimeError('compile failed')
    remaining=30-total()
    assert remaining>0
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(max(1,int(remaining)-1),max(2,int(remaining))))
    proc=subprocess.Popen([str(HERE/'radius4'),str(out)],stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True,preexec_fn=limits)
    put('WORKER_HANDLE.json',{'status':'RUNNING','pid':proc.pid,'cpu_budget_seconds':remaining})
    stdout,stderr=proc.communicate(timeout=60)
    (HERE/'worker.stdout').write_text(stdout);(HERE/'worker.stderr').write_text(stderr)
    put('WORKER_HANDLE.json',{'status':'TERMINAL','pid':proc.pid,'exit_code':proc.returncode,'cpu_budget_seconds':remaining})
    if proc.returncode==0:
        result=json.loads(stdout)
        result.update(actual_graph_count=1,actual_max_degree=max(degrees),old_source_BFS=0,degree_prediction='SUPPORTED',record_count=0)
        if result['status']=='FIRST_R4_FAILURE':
            result['first_failure_root_source_label']=ids[result['first_failure_root']]
            result['first_missing_source_label']=ids[result['first_missing_vertex']]
            result['D_prediction']='REFUTED'
        else:result['D_prediction']='SUPPORTED_PENDING_ROOT_INDEPENDENT_ACCEPTANCE'
    else:result={'status':'UNKNOWN_BUDGET_OR_WORKER_FAILURE','worker_exit_code':proc.returncode,'actual_n':len(ids),'actual_m':len(edges),'actual_max_degree':max(degrees),'global_D':None,'old_source_BFS':0,'record_count':0}
result.update(aggregate_cpu_seconds=total(),wall_seconds=time.monotonic()-wall,driver_pid=os.getpid(),budget_aggregate_cpu_seconds=30,other_subsets_or_edge_changes=0)
put('RESULT.json',result);put('TERMINAL.json',{'status':'TERMINAL','result_status':result['status'],'aggregate_cpu_seconds':result['aggregate_cpu_seconds'],'actual_graph_count':1,'pending':[]})
put('HANDLE.json',{'status':'TERMINAL','pid':os.getpid(),'result_status':result['status']})
print(json.dumps(result),flush=True)
