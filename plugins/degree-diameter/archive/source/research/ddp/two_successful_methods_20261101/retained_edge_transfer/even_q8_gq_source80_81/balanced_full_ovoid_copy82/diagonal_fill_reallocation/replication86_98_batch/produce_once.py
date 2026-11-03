from pathlib import Path
import json,os,resource,subprocess,time
D=Path(__file__).resolve().parent;P=D.parent
start=time.process_time();budget=30.;attempts=[]
def save(path,value):
    tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(value,indent=2)+'\n');os.replace(tmp,path)
def used():
    u=resource.getrusage(resource.RUSAGE_CHILDREN)
    return time.process_time()-start+u.ru_utime+u.ru_stime
cases=[dict(degree=86,r=4,n=363420,m=15573870,directory='multiplicity5_degree86'),
       dict(degree=98,r=16,n=414132,m=19680570,directory='multiplicity17_degree98')]
for c in cases:
    out=P/c['directory'];out.mkdir(exist_ok=True)
    c['output']=str(out/f"graph_d{c['degree']}_D3_n{c['n']}.edges")
    assert not Path(c['output']).exists(),'Fixed batch already ran; inspect receipts, do not rerun.'
    (out/'PREDICTION_AND_SCOPE.md').write_text((D/'PREDICTION_AND_SCOPE.md').read_text()+
        f"\nThis case is degree{c['degree']}, r{c['r']}, n{c['n']}, m{c['m']}. The two-case production budget is shared.\n")
commands=[('compile',['g++','-std=c++17','-O2','-o',str(D/'produce_once'),str(D/'produce_once.cpp')]),
    ('write_both_complete_graphs',[str(D/'produce_once'),str(P/'graph_d82_D3_n346516.edges'),*[c['output']for c in cases]])]
for phase,command in commands:
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    remaining=max(1,int(budget-used()))
    def limits():resource.setrlimit(resource.RLIMIT_CPU,(remaining,remaining))
    with(D/(phase+'.log')).open('w')as log:
        proc=subprocess.Popen(command,stdout=log,stderr=log,preexec_fn=limits)
        save(D/'HANDLE.json',dict(status='RUNNING',driver_pid=os.getpid(),child_pid=proc.pid,phase=phase,command=command,CPU_seconds=used()))
        proc.wait()
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    record=dict(phase=phase,exit_code=proc.returncode,CPU_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime)
    attempts.append(record);save(D/'CHECKPOINT.json',dict(attempts=attempts,CPU_seconds=used(),running=False))
    if proc.returncode:
        save(D/'TERMINAL.json',dict(status='FAILED_STOP',running=False,attempts=attempts,CPU_seconds=used()))
        raise SystemExit(proc.returncode)
report=json.loads((D/'write_both_complete_graphs.log').read_text());assert used()<budget
for expected,actual in zip(cases,report['cases']):
    for key in('degree','r','n','m'):assert expected[key]==actual[key]
    out=P/expected['directory']
    parameters=dict(source='../graph_d82_D3_n346516.edges',source_n=346516,source_m=14204970,
        original_H_n=342290,role_count=4226,original_role_center_label='342290+h,h0..4225',
        copy_index='j=4226*b+h',new_label='346516+j',r=actual['r'],degree=actual['degree'],
        n=actual['n'],m=actual['m'],new_new_edges=0,all_source_edges_retained=True,
        frozen_fullN='actual complete G1 center neighborhood, all pins <342290',
        public_guarantee=4225*actual['degree'],located_margin=actual['degree']-16,
        priority='UNKNOWN',independent_fresh_acceptance='PENDING')
    save(out/'PARAMETERS.json',parameters)
    save(out/'RESULT.json',dict(status=report['status'],**actual,source_parse_in_shared_batch=1,
        all_role_N_sizes_actual_source_bound=True,source_fullN_frozen=True,strictlex_header_simple=True,
        BFS_runs=0,batch_receipt='../replication86_98_batch/RESULT.json',fresh_acceptance='PENDING'))
    save(out/'TERMINAL.json',dict(status='PRODUCER_TERMINAL_PASS_PENDING_FRESH_ACCEPTANCE',running=False,
        complete_graph=Path(expected['output']).name,BFS_runs=0,no_automatic_next_parameter=True))
report.update(CPU_seconds=used(),CPU_budget_seconds=budget,attempts=attempts,
    complete_outputs=[c['output']for c in cases],root_counts_modified=False,field_geometry_Lean_solver_runs=0)
save(D/'RESULT.json',report)
save(D/'TERMINAL.json',dict(status='BOTH_PRODUCERS_TERMINAL_PASS_PENDING_FRESH_ACCEPTANCE',running=False,
    all_children_terminal=True,CPU_seconds=used(),CPU_budget_seconds=budget,BFS_runs=0,
    complete_outputs=report['complete_outputs'],no_other_parameter_generated=True))
save(D/'HANDLE.json',dict(status='TERMINAL',running=False,active_children=[],CPU_seconds=used()))
print(json.dumps(dict(status=report['status'],CPU_seconds=used(),cases=report['cases'])))
