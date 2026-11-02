"""One root-authorized fixed q8 two-source run; no automatic continuation."""
import argparse,json,resource,subprocess
from pathlib import Path
from time import process_time,perf_counter
from prepare_inputs import prepare

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--run',action='store_true');parser.add_argument('--public-gate',type=Path,required=True)
    args=parser.parse_args();assert args.run,'Explicit root-authorized --run is required.'
    D=Path(__file__).resolve().parent;assert not(D/'RESULT.json').exists(),'Single fixed source batch already has a terminal result.'
    assert args.public_gate.is_file();start=process_time();wall=perf_counter();receipts=[]
    specs=prepare(D)
    def child(name,command,limit=None):
        before=resource.getrusage(resource.RUSAGE_CHILDREN);t=perf_counter()
        def cap():
            seconds=max(1,int(limit));resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
        with(D/(name+'.stdout')).open('w')as out,(D/(name+'.stderr')).open('w')as err:
            try:r=subprocess.run(command,cwd=D,stdout=out,stderr=err,preexec_fn=cap if limit else None,timeout=55);code=r.returncode
            except subprocess.TimeoutExpired:code='wall_timeout'
        after=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
        receipts.append({'stage':name,'exit_code':code,'CPU_seconds':cpu,'wall_seconds':perf_counter()-t});return code
    code=child('compile',['g++','-O3','-std=c++17','produce_sources.cpp','-o','produce_sources'])
    cases=[]
    if code==0:
        for s in specs:
            used=sum(r['CPU_seconds']for r in receipts)+process_time()-start;remaining=30-used;assert remaining>1
            case=s['case'];code=child(case,['./produce_sources',case,case+'/TABLES_INPUT.txt',case,str(remaining-0.5)],remaining)
            if code!=0:break
            actual=json.loads((D/(case+'.stdout')).read_text());cases.append(actual)
            for name in ['RESULT.json','TERMINAL.json']:(D/case/name).write_text(json.dumps(dict(actual,running=False,active_processes=[]),indent=2)+'\n')
            print(json.dumps(actual),flush=True)
    result={'status':'PASS_TWO_LITERAL_FILLED_SOURCES_PENDING_FRESH_ACCEPTANCE'if code==0 and len(cases)==2 else'UNKNOWN_SOURCE_PRODUCTION_STOP',
            'public_gate':str(args.public_gate.resolve()),'cases':cases,'receipts':receipts,'classical_unfilled_files_are_reproduction_only':True,
            'candidate_graphs_accepted_here':0,'Lean_instances_accepted_here':0,'BFS_runs':0,'field_geometry_checks_repeated':False,
            'P33_snapshot_or_files_modified':False,'wrapper_CPU_seconds':process_time()-start,
            'accounted_CPU_seconds':sum(r['CPU_seconds']for r in receipts)+process_time()-start,
            'wall_seconds':perf_counter()-wall,'CPU_budget_seconds':30,'workers':1,'running':False,'active_processes':[]}
    for name in ['RESULT.json','TERMINAL.json']:(D/name).write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result),flush=True)

if __name__=='__main__':main()
