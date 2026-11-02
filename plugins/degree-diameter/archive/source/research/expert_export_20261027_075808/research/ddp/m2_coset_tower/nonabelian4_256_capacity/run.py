#!/usr/bin/env python3
import json
import resource
import subprocess
import time
from pathlib import Path

OUT=Path(__file__).resolve().parent

def used():
    me=resource.getrusage(resource.RUSAGE_SELF)
    child=resource.getrusage(resource.RUSAGE_CHILDREN)
    return me.ru_utime+me.ru_stime+child.ru_utime+child.ru_stime

def main():
    start=used();wall=time.monotonic()
    subprocess.run(['g++','-O3','-std=c++17',str(OUT/'capacity.cpp'),'-o',str(OUT/'capacity')],check=True)
    prep=used()-start
    topology={'n':256,'degree':8,'diameter_target':3,'group_order':64,
        'edge_u':[0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2],
        'edge_v':[1,1,1,2,2,2,3,3,2,2,3,3,3,3,3,3],
        'tree_edge_indices':[0,3,6],
        'free_edge_indices':[1,2,4,5,7,8,9,10,11,12,13,14,15],
        'phase_mask_convention':'bit k is the phase of free_edge_indices[k]',
        'coefficient_order':'same as free_edge_indices; signed coefficients interpreted modulo 32',
        'dart_convention':'2*edge is edge_u to edge_v; 2*edge+1 is its inverse',
        'expected_reduced_walks_per_root_by_length':[1,8,56,392]}
    (OUT/'topology.json').write_text(json.dumps(topology,indent=2)+'\n')
    summaries=[]
    for name in ['D64','Q64']:
        remaining=120-(used()-start)-1
        if remaining<=0:break
        dest=OUT/name.lower()
        dest.mkdir(exist_ok=True)
        with (dest/'run.log').open('w') as log:
            proc=subprocess.run([str(OUT/'capacity'),str(dest),name,str(remaining)],stdout=log,stderr=subprocess.STDOUT)
        assert proc.returncode==0
        result=json.loads((dest/'results.json').read_text())
        summaries.append(result)
        (dest/'progress.json').write_text(json.dumps({k:result[k] for k in ['status','running','group','completed_phase_masks','next_phase_mask','capacity_pass_count','CPU_seconds']},indent=2)+'\n')
        print({k:result[k] for k in ['group','status','completed_phase_masks','capacity_pass_count','surviving_tight_fibers','CPU_seconds']},flush=True)
        if result['status']!='COMPLETE':break
    terminal={'status':'COMPLETE' if len(summaries)==2 and all(r['status']=='COMPLETE' for r in summaries) else 'CPU_LIMIT_PREFIX_SAVED',
        'running':False,'preparation_CPU_seconds':prep,
        'total_measured_CPU_seconds':used()-start,'wall_seconds':time.monotonic()-wall,
        'groups':[{k:r[k] for k in ['group','status','completed_phase_masks','next_phase_mask','capacity_pass_count','surviving_tight_fibers','CPU_seconds']} for r in summaries],
        'translation_assignments':0,'generated_graphs':0,'BFS_roots':0}
    (OUT/'terminal.json').write_text(json.dumps(terminal,indent=2)+'\n')
    print(json.dumps(terminal,indent=2))

if __name__=='__main__':main()
