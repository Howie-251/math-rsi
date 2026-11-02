from pathlib import Path
import json
import resource
import subprocess
import time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
START=time.process_time()
CHILD=resource.getrusage(resource.RUSAGE_CHILDREN)
def cpu():
    c=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-START+c.ru_utime+c.ru_stime-CHILD.ru_utime-CHILD.ru_stime
def main():
    p=json.loads((OUT/'PREDICTION.json').read_text())
    assert p['status']=='FROZEN_BEFORE_NEAR_NEIGHBOR_PROXY_COMPUTATION'
    assert not(OUT/'RESULT.json').exists()
    subprocess.run(['g++','-O3','-std=c++17',str(OUT/'probe.cpp'),'-o',str(OUT/'probe')],check=True)
    compile_cpu=cpu();rows=[]
    print(json.dumps({'stage':'COMPILED','CPU_seconds':compile_cpu}),flush=True)
    for spec in p['sources']:
        d=spec['delta'];folder=OUT/f'd{d}';remaining=12-cpu()
        if remaining<.7:
            rows.append({**spec,'status':'UNATTEMPTED_TOTAL_CPU_RESERVE'});continue
        allowance=min(4.5,remaining-.3)
        with(folder/'native.log').open('w')as log:
            answer=subprocess.run([str(OUT/'probe'),str(ROOT/spec['source_graph']),str(folder/'ports.txt'),str(ROOT/spec['R4_cache']),str(folder),str(spec['source_n']),str(spec['source_m']),str(d),str(allowance)],stdout=log,stderr=log,timeout=15)
        native=folder/'NATIVE_RESULT.json'
        r=json.loads(native.read_text())if native.exists()else{'status':'UNKNOWN_NATIVE_TERMINATION','returncode':answer.returncode}
        r.update(returncode=answer.returncode,source_n=spec['source_n'],source_m=spec['source_m'],delta=d)
        (folder/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
        (folder/'terminal.json').write_text(json.dumps({**r,'running':False},indent=2)+'\n')
        rows.append(r)
        print(json.dumps(r),flush=True)
    result={'status':'FIXED_TWO_SOURCE_RULE_TERMINAL','sources':rows,'compile_CPU_seconds':compile_cpu,'total_parent_children_CPU_seconds':cpu(),'CPU_budget_seconds':12,'full_hits':sum(r.get('full_hits',0)for r in rows),'new_graphs':sum(r.get('full_hits',0)for r in rows),'prediction':'SUPPORTED'if any(r.get('full_hits')for r in rows)else'REFUTED_FOR_FIXED_RULE'if all(r['status']=='COMPLETE_FIXED_PROXY_RULE_NO_HIT'for r in rows)else'UNRESOLVED_PARTIAL','new_BFS':0,'new_balls':0,'MIP':0,'greedy':0,'known_D13_retest':False,'shared_family_modified':False,'pending':[]}
    (OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    (OUT/'terminal.json').write_text(json.dumps({**result,'running':False},indent=2)+'\n')
    print('TERMINAL '+json.dumps(result),flush=True)
if __name__=='__main__':main()
