#!/usr/bin/env python3
"""One complete edge-mask old-obligation gate from already cached support."""
import json
import math
import os
from pathlib import Path
import resource
import signal
import struct
import subprocess
import time

START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(3,24))
signal.signal(signal.SIGXCPU,lambda signum,frame: (_ for _ in ()).throw(RuntimeError('DRIVER_CPU_STOP')))
HERE=Path(__file__).resolve().parent
PRIOR=2.511387697
PREP=0.25
CAP=20

def write(name,obj):
    (HERE/name).write_text(json.dumps(obj,indent=2)+'\n')

def limit(seconds):
    def apply():resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
    return apply

def child(cmd,name,hard,wall):
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    with (HERE/(name+'.stdout')).open('w') as out,(HERE/(name+'.stderr')).open('w') as err:
        p=subprocess.Popen(cmd,stdout=out,stderr=err,preexec_fn=limit(hard))
        write('OLD_HANDLE.json',{'status':'RUNNING_'+name,'driver_pid':os.getpid(),'child_pid':p.pid,
            'command':cmd,'single_worker':True,'child_hard_CPU_seconds':hard,'wholecase_CPU_cap_seconds':CAP})
        timedout=False
        try:code=p.wait(timeout=wall)
        except subprocess.TimeoutExpired:p.kill();code=p.wait();timedout=True
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    return {'returncode':code,'CPU_seconds':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,'wall_timeout':timedout}

paths=json.loads((HERE/'PROFILE_SPHERE4_PATHS.json').read_text())['paths_from_identity']
assert len(paths)==750 and all(len(r['path'])==5 and r['path'][0]==0 and r['path'][-1]==r['target'] for r in paths)
with (HERE/'OLD_CACHED_SPHERE4_PATHS.u32').open('wb') as stream:
    for row in paths:stream.write(struct.pack('<5I',*row['path']))
write('OLD_INPUT_BINDING.json',{'data_source':'PROFILE_RESULT.json/PROFILE_DATA_SCHEMA.json actualcached support',
    'distance_count_sphere_critical_M_reused':True,'new_BFS':0,'new_DP':0,'new_source_D9_or_field_checks':0,
    'sphere4_paths_repacked_only':'750saved5vertexpaths flattened, no newroute search',
    'mask_representative_domain_proof':'PAPER_OLD_OBLIGATION_GATE.md; firstcut endpointfilter happens beforeclassgrouping',
    'postfilter_scope':'One firstrealtriple/type only; its laterfailure never excludes wholemaskclass',
    'prior_case_CPU_seconds':PRIOR,'new_preparation_charge_CPU_seconds':PREP})
compile_result=child(['c++','-O3','-std=c++17',str(HERE/'old_obligation_once.cpp'),'-o',str(HERE/'old_obligation_once')],'OLD_COMPILE',6,20)
native=None
if compile_result['returncode']==0:
    available=CAP-PRIOR-PREP-compile_result['CPU_seconds']-(time.process_time()-START)-.5
    hard=min(14,math.floor(available))
    if hard>=1:native=child([str(HERE/'old_obligation_once'),str(HERE),str(max(.2,hard-.15))],'OLD_NATIVE',hard,25)
raw=json.loads((HERE/'OLD_RAW_RESULT.json').read_text()) if (HERE/'OLD_RAW_RESULT.json').exists() else None
parent=time.process_time()-START
total=PRIOR+PREP+parent+compile_result['CPU_seconds']+(native['CPU_seconds'] if native else 0)
success=bool(raw and native and native['returncode']==0 and raw.get('status')!='UNKNOWN_OLD_OBLIGATION_GATE_STOP')
result={'status':raw['status'] if success else 'UNKNOWN_OLD_OBLIGATION_BUILD_OR_RUN_STOP',
    'raw':raw,'compile':compile_result,'native':native,'prior_case_CPU_seconds':PRIOR,
    'new_preparation_charge_CPU_seconds':PREP,'parent_CPU_seconds':parent,'wholecase_CPU_seconds':total,
    'wholecase_CPU_cap_seconds':CAP,'new_BFS_DP_or_sourceD9_fieldchecks':0,'new_candidate_graphs':0,
    'scope':'Fixedactual331387source/minimal3vertexdisjointoldcuts/one6star; fullNOonlyifall3firstcanonicaltypeobligationgatesNO',
    'next':'STOP nosecondtriple/normaloptimization/newfield/fullseam; rootdispositionsactualfirsttripleorcompleteNO'}
write('OLD_RESULT.json',result)
write('OLD_TERMINAL.json',{**result,'terminal':True,'active_processes':0})
write('OLD_HANDLE.json',{'status':result['status'],'driver_pid':os.getpid(),'terminal':True,'active_processes':0,'wholecase_CPU_seconds':total})
print(json.dumps({'status':result['status'],'compile':compile_result,'native':native,
    'wholecase_CPU_seconds':total,'types':None if not success else [
        {k:r[k] for k in ['first_type','critical_pair_count','mask_classes','maximum_single_edge_obligations_hit','strict_two_edge_cardinality_bound_excludes','found_real_disjoint_pair','first_triple']} for r in raw['firsttypes']]}))
