#!/usr/bin/env python3
"""One compile and one new-question support/profile run, total case cap20 CPU."""
import json
import math
import os
from pathlib import Path
import resource
import signal
import subprocess
import time

START=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(3,24))
signal.signal(signal.SIGXCPU,lambda signum,frame: (_ for _ in ()).throw(RuntimeError('DRIVER_CPU_STOP')))
HERE=Path(__file__).resolve().parent
REPO=next(p for p in HERE.parents if (p/'AGENTS.md').is_file())
PRIOR=0.8
PREP=0.25
CAP=20

def write(name,data):
    (HERE/name).write_text(json.dumps(data,indent=2)+'\n')

def limits(seconds):
    def apply():
        resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
    return apply

def child(cmd,name,hard,wall):
    before=resource.getrusage(resource.RUSAGE_CHILDREN)
    with (HERE/(name+'.stdout')).open('w') as out,(HERE/(name+'.stderr')).open('w') as err:
        process=subprocess.Popen(cmd,stdout=out,stderr=err,preexec_fn=limits(hard))
        write('PROFILE_HANDLE.json',{'status':'RUNNING_'+name,'driver_pid':os.getpid(),'child_pid':process.pid,
             'command':cmd,'single_worker':True,'child_CPU_hard_seconds':hard,'wholecase_CPU_cap_seconds':CAP})
        timeout=False
        try:
            code=process.wait(timeout=wall)
        except subprocess.TimeoutExpired:
            process.kill();code=process.wait();timeout=True
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    return {'returncode':code,'CPU_seconds':after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,'wall_timeout':timeout}

write('PROFILE_INPUT_BINDING.json',{'source':'actual331387/994161 regular6 Cayley, D9 inherited',
    'RIGHT_law':'(j,n)*(a,c)=(j+a,n*41^a+c), phase49/normal6763,label6763j+n',
    'six_generators':[[25,1254],[24,2125],[18,541],[31,3289],[47,4642],[2,1300]],
    'source_author_C':'research/ddp/more_graphs_20261027/d6_D9_current331387_source/AUTHOR_deg6_D9_CHK.c',
    'LEFT_RIGHT_binding':'inherited inversion isomorphism for inverse-closed source; see source ANALYSIS_GAUGE_PROOF.md',
    'paper_interface':'PAPER_INTERFACE.md','new_source_prime_or_action_order_checks':0,
    'old_single_subdivision_queries_repeated':0,'old_F6959_family_repeated':0,
    'purpose':'new3cut6star support/critical data previously not stored, not oldD9 validation'})
compile_result=child(['c++','-O3','-std=c++17',str(HERE/'profile_once.cpp'),'-o',str(HERE/'profile_once')],'COMPILE',6,20)
native_result=None
if compile_result['returncode']==0:
    available=CAP-PRIOR-PREP-compile_result['CPU_seconds']-(time.process_time()-START)-0.5
    hard=min(15,math.floor(available))
    if hard>=1:
        native_result=child([str(HERE/'profile_once'),str(HERE),str(max(.2,hard-.15))],'NATIVE',hard,25)
raw=json.loads((HERE/'PROFILE_RAW_RESULT.json').read_text()) if (HERE/'PROFILE_RAW_RESULT.json').exists() else None
parent_cpu=time.process_time()-START
total=PRIOR+PREP+parent_cpu+compile_result['CPU_seconds']+(native_result['CPU_seconds'] if native_result else 0)
status='COMPLETE_NEW_QUESTION_SUPPORT_CRITICAL_PHASE_GATE' if raw and raw.get('status')=='COMPLETE_NEW_SUPPORT_AND_PHASE_CRITICAL_PROFILE' and native_result and native_result['returncode']==0 else 'UNKNOWN_PROFILE_BUILD_OR_RUN_STOP'
result={'status':status,'prior_case_CPU_seconds':PRIOR,'new_preparation_charge_CPU_seconds':PREP,
    'compile':compile_result,'native':native_result,'parent_CPU_seconds':parent_cpu,
    'wholecase_CPU_seconds':total,'wholecase_CPU_cap_seconds':CAP,'raw_profile':raw,
    'new_question_identity_R8_support_BFS_roots':1 if raw and raw.get('new_question_support_BFS_roots') else 0,
    'source_D9_validity_BFS_roots':0,'old_single_subdivision_queries_repeated':0,
    'old_field_order_or_F6959_rechecks':0,'candidate_graphs_generated':0,'oldold_BFS_queries':0,
    'scope':'Oneactualsource support export, complete4+1+4critical profiles and fixedphase-projection3edge gate; normaltranslations family remains open if no phaseempty',
    'next':'STOP no normaloffsetscan/extra cut/seed/candidateallroot; rootdispositions actual predictions'}
write('PROFILE_RESULT.json',result)
write('PROFILE_TERMINAL.json',{**result,'terminal':True,'active_processes':0})
write('PROFILE_HANDLE.json',{'status':status,'driver_pid':os.getpid(),'terminal':True,'active_processes':0,
                           'wholecase_CPU_seconds':total})
if raw and raw.get('sphere4_size') is not None:
    write('PROFILE_DATA_SCHEMA.json',{'distance_file':'PROFILE_IDENTITY_DISTANCE.u8','distance_entries':331387,
        'distance_le8':'measured by thisnewquestion supportBFS','distance9':'inheritedsourceD9 for unvisitedsupport',
        'count_file':'PROFILE_IDENTITY_SHORTEST_COUNTS.u32','count_entries':331387,'counts':'shortest-wordDP with measuredle8/inherited9 distances',
        'integer_byte_order':'little-endian host','sphere4_labels_file':'PROFILE_SPHERE4_LABELS.u32',
        'sphere4_entries':raw['sphere4_size'],'sphere4_paths_file':'PROFILE_SPHERE4_PATHS.json',
        'critical_files':'PROFILE_CRITICAL_TYPE{0,1,2}.u64',
        'critical_layout':'rows=sphere4 u index; columns=sphere4 w index; bit1 means criticalpair(u,s_type*w)',
        'critical_u64_words_per_row':raw['critical_u64_stride'],
        'missing_files':'PROFILE_M_TYPE{0,1,2}_LABELS.u32','missing_order':'ascendingactualsourcevertexlabels',
        'group_coordinates':'label=6763*phase+normal','all_arrays_are_newquestiondata_notnewgraph':True})
print(json.dumps({'status':status,'compile':compile_result,'native':native_result,
    'wholecase_CPU_seconds':total,'raw_summary':None if not raw else {k:raw.get(k) for k in ['sphere4_size','phase_domain_count','phase_empty_intersections','phase_prediction_supported','critical_each_type_prediction_supported','selected_sixpin_certificate']}}))
