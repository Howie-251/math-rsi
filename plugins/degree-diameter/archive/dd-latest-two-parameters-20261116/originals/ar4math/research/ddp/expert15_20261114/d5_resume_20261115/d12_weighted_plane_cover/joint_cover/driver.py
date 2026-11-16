from pathlib import Path
import json,math,os,resource,subprocess,sys,time
P=Path(__file__).resolve().parent;D=P.parent/'current_graph_data';LIB='/tmp/n62_sms_install/lib/libsmscadical.a'
def childcpu():
    r=resource.getrusage(resource.RUSAGE_CHILDREN);return r.ru_utime+r.ru_stime
def lim(seconds):
    def limits():
        s=max(1,math.ceil(seconds));resource.setrlimit(resource.RLIMIT_CPU,(s,s));resource.setrlimit(resource.RLIMIT_AS,(2*1024**3,2*1024**3));resource.setrlimit(resource.RLIMIT_CORE,(0,0))
    return limits
def run(command,name,seconds):
    with(P/name).open('w')as f:r=subprocess.run(command,stdout=f,stderr=subprocess.STDOUT,preexec_fn=lim(seconds),env={**os.environ,'OMP_NUM_THREADS':'1','OPENBLAS_NUM_THREADS':'1','MKL_NUM_THREADS':'1'})
    if r.returncode:raise RuntimeError(f'{name}: exit{r.returncode}')
def main():
    mode=sys.argv[1]if len(sys.argv)>1 else'prepare';start=time.process_time();c0=childcpu()
    if mode=='prepare':
        assert not(P/'PREP_RESULT.json').exists(),'Already prepared; do not silently repeat.'
        budget=lambda:8-(time.process_time()-start+childcpu()-c0)
        run([sys.executable,str(P/'convert.py')],'CONVERT.log',budget())
        run(['g++','-O2','-std=c++17',str(P/'cover.cpp'),LIB,'-lpthread','-o',str(P/'cover')],'COMPILE.log',budget())
        run([str(P/'cover'),'--selftest'],'SELFTEST.log',budget())
        run([str(P/'cover'),'--prepare',str(P),str(D)],'PREP_NATIVE.log',budget())
        used=time.process_time()-start+childcpu()-c0;assert used<=8,used
        model=json.loads((P/'MODEL.json').read_text());assert not model['solve_entered']
        out={'status':'READY_NOT_SOLVED','prepare_compile_controls_CPU':used,'budget_CPU':8,'single_thread':True,'memory_GiB':2,
             'encoding_control_solver_calls':6,'mathematical_solver_calls':0,'solve_entered':False,'SAT_models':0,'fullchecks':0,
             'model':model,'solver_CPU_limit_when_authorized':180,'command_after_Root_authorization':'python3 '+str(P/'driver.py')+' run'}
        (P/'PREP_RESULT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out),flush=True)
    elif mode=='run':
        assert(P/'PREP_RESULT.json').exists()and not(P/'RUN_HANDLE.json').exists(),'One authorized solver run only.'
        (P/'RUN_HANDLE.json').write_text(json.dumps({'status':'STARTING_AUTHORIZED_SINGLE_SOLVER','driver_pid':os.getpid(),'solver_CPU_limit':180})+'\n')
        with(P/'SOLVER.log').open('w')as f:
            proc=subprocess.Popen([str(P/'cover'),'--solve',str(P),str(D),'180'],stdout=f,stderr=subprocess.STDOUT,preexec_fn=lim(190))
            (P/'RUN_HANDLE.json').write_text(json.dumps({'status':'NATIVE_RUNNING','driver_pid':os.getpid(),'native_pid':proc.pid,'solver_CPU_limit':180})+'\n');proc.wait()
        if proc.returncode:raise RuntimeError(f'native exit{proc.returncode}; keep raw logs')
        result=json.loads((P/'NATIVE_RESULT.json').read_text())
        if result['solver_return_code']==10:
            run([sys.executable,str(P/'verify.py')],'VERIFY.log',8)
            verification=json.loads((P/'VERIFICATION.json').read_text());result['verification']=verification;result['fullchecks']=1;result['status']=verification['status']
        result['whole_run_CPU']=time.process_time()-start+childcpu()-c0
        (P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');(P/'RUN_HANDLE.json').write_text(json.dumps({'status':'TERMINAL','running':False,'result':'RESULT.json'})+'\n');print(json.dumps(result),flush=True)
    else:raise ValueError('prepare or run')
if __name__=='__main__':main()
