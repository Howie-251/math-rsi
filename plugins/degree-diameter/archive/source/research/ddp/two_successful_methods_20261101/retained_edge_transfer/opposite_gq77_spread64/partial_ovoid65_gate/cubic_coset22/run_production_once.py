#!/usr/bin/env python3
"""Prepare exact table bridge, compile once, run once; total budget60CPU."""
import datetime
import json
import math
from pathlib import Path
import resource
import subprocess
import time

OUT=Path(__file__).resolve().parent
SOURCE=OUT.parent.parent


def read(path):
    return json.loads(path.read_text())


def write(name,value):
    (OUT/name).write_text(json.dumps(value,indent=2)+'\n')


def child_cpu():
    x=resource.getrusage(resource.RUSAGE_CHILDREN)
    return x.ru_utime+x.ru_stime


def limit(seconds):
    def apply():
        resource.setrlimit(resource.RLIMIT_CPU,(seconds,seconds))
    return apply


def main():
    start=time.process_time()
    wall=time.monotonic()
    before=child_cpu()
    pred=read(OUT/'PRED_PRODUCTION.json')
    assert not (OUT/'BUILD_RUN.json').exists(),'one fixed production batch only'
    assert not (OUT/pred['output']).exists()
    data=read(SOURCE/'PARAMETERS.json')
    rows=read(OUT/'CENTERS.json')
    finite=read(OUT/'PRECHECK_RESULT.json')
    rule=read(OUT/'PRED.json')
    points=[tuple(p) for p in data['points']]
    ids=[points.index(tuple(p)) for p in rule['candidate_points_mod7']]
    assert ids==finite['point_ids'] and len(rows)==1100
    spread=data['spread_line_labels']
    lines=[r['points'] for r in data['lines']]
    through=data['point_incident_lines']
    owners=data['point_spread_owner']
    assert (SOURCE/'TABLES_INPUT.txt').read_text().split()==list(map(str,
        [400,8,50]+[p for r in lines for p in r]+[l for r in through for l in r]+spread+owners))
    for i,r in enumerate(rows):
        pi,j=divmod(i,50)
        assert r['index']==i and r['point_index']==pi and r['point_id']==ids[pi]
        assert r['spread_index']==j and r['spread_line']==spread[j]
        assert r['center']==400*ids[pi]+spread[j] and r['source_degree']==64
        assert r['flag']==(ids[pi] in lines[spread[j]])
    with (OUT/'PRODUCTION_INPUT.txt').open('w') as f:
        f.write('400 8 50 1100\n')
        for r in lines+through:
            f.write(' '.join(map(str,r))+'\n')
        f.write(' '.join(map(str,spread))+'\n')
        f.write(' '.join(map(str,owners))+'\n')
        for r in rows:
            f.write(' '.join(str(r[k]) for k in ['index','point_index','point_id','spread_index','spread_line','center'])+'\n')
    write('PARAMETERS.json',{
        'stage':'FIXED_PRODUCTION_PARAMETERS_FROZEN',
        'source_edgefile':'../../graph_d64_D3_n160050.edges',
        'source_geometry_parameters':'../../PARAMETERS.json',
        'source_n':160050,'source_m':5121600,'source_degree':64,
        'field':'GF7 ordinary modular arithmetic',
        'source_coordinates':'u0,u1,v0,v1',
        'alternating_form_without_nonzero_factor2':'x0*y2+3*x1*y3-x2*y0-3*x3*y1 mod7',
        'partial_ovoid_rule':'(1,t,t^3+k,-t^2) for k0,2,4/t0..6, followed by(0,0,1,0)',
        'partial_ovoid_points':rule['candidate_points_mod7'],
        'partial_ovoid_point_ids':ids,
        'spread_line_ids_original_order':spread,
        'source_center_labels_original_order':[r['center'] for r in rows],
        'saved_center_table':'CENTERS.json',
        'saved_centers_all1100_fields_bound_to_frozen_geometry':True,
        'clone_label':'160050+savedcenter.index',
        'clone_neighbors':'Exactly the64literal neighbors of itscenter in immutable160050source;formula equality checked before writing.',
        'new_to_new_edges':0,
        'old_edges':'All5121600source edges retained exactly, streamed in original order',
        'target_n':161150,'target_m':5192000,
        'degree_histogram':{'64':90750,'65':70400},
        'output':'graph_d65_D3_n161150.edges',
        'output_order':'Strict ascending lexicographic pairs u<v',
        'public_comparison':'Rootlocated160750;globalrecord/priority notcertified',
        'independent_acceptance':'SEPARATE_ROOT_TASK'})
    prep=time.process_time()-start
    run={'started_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
         'budget_CPU_seconds':60,'workers':1,'preparation_CPU_seconds':prep,
         'source_edges_generated':False,'compile_runs':1,'production_runs':1}
    compile_start=child_cpu()
    cmd=['g++','-std=c++17','-O2','-DNDEBUG','produce.cpp','-o','produce']
    with (OUT/'BUILD.log').open('w') as log:
        compilation=subprocess.run(cmd,cwd=OUT,stdout=log,stderr=subprocess.STDOUT,
                                   preexec_fn=limit(max(1,math.floor(60-prep))),timeout=180)
    compile_cpu=child_cpu()-compile_start
    run['compile']={'command':cmd,'exit_code':compilation.returncode,'CPU_seconds':compile_cpu}
    if compilation.returncode!=0:
        run['status']='COMPILE_FAILED_NO_PRODUCTION';write('BUILD_RUN.json',run)
        raise SystemExit(compilation.returncode)
    used=time.process_time()-start+child_cpu()-before
    remaining=math.floor(60-used)
    assert remaining>0,'compile exhausted total budget'
    production_start=child_cpu()
    with (OUT/'PRODUCTION.log').open('w') as log:
        production=subprocess.run(['./produce'],cwd=OUT,stdout=log,stderr=subprocess.STDOUT,
                                  preexec_fn=limit(remaining),timeout=180)
    production_cpu=child_cpu()-production_start
    run['production']={'command':['./produce'],'exit_code':production.returncode,
                       'child_CPU_seconds':production_cpu,'RLIMIT_CPU_seconds':remaining}
    run['total_measured_CPU_seconds']=time.process_time()-start+child_cpu()-before
    run['wall_seconds']=time.monotonic()-wall
    run['finished_utc']=datetime.datetime.now(datetime.timezone.utc).isoformat()
    run['status']='PRODUCER_PASS_AWAIT_FRESH_INDEPENDENT_ACCEPTANCE' if production.returncode==0 else 'PRODUCTION_FAILED'
    write('BUILD_RUN.json',run)
    assert run['total_measured_CPU_seconds']<60
    if production.returncode!=0:
        raise SystemExit(production.returncode)
    result=read(OUT/'PRODUCER_RESULT.json')
    result['compile_CPU_seconds']=compile_cpu
    result['total_measured_CPU_seconds_including_compile_and_preparation']=run['total_measured_CPU_seconds']
    result['total_CPU_budget_seconds']=60
    result['concrete_Lean']='NOT_STARTED_SEPARATE_TASK'
    result['accepted_counts_changed']=False
    write('RESULT.json',result)
    write('TERMINAL.json',{'status':'FIXED161150_PRODUCTION_COMPLETE_RETURN_TO_ROOT',
          'running':False,'graph_file_complete':True,'independent_acceptance':'PENDING_FRESH_ROOT_READBACK',
          'candidate_graphs_generated':1,'BFS':0,'Lean':0,'solver':0,'install':0,'hash':0,
          'total_measured_CPU_seconds':run['total_measured_CPU_seconds'],
          'next':'Fresh independent acceptance;no producer continuation,no accepted counts changed.'})
    print(json.dumps({'status':run['status'],'n':161150,'m':5192000,
          'total_CPU_seconds':run['total_measured_CPU_seconds'],
          'compile_CPU_seconds':compile_cpu,'production_child_CPU_seconds':production_cpu,
          'edgefile':str(OUT/'graph_d65_D3_n161150.edges')}))


if __name__=='__main__':
    main()
