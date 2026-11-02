#!/usr/bin/env python3
"""Prepare only; one explicitly authorized cache-vs-literal root calibration.
Does not enumerate voltage assignments or recompute the provider gate.
"""
import argparse, json, os, resource, subprocess, time
from pathlib import Path

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
BASE=HERE.parent/'k5_q16_NB4_quotient_gate'/'BASE_INPUT.json'
CACHE=HERE.parent/'k5_actual_route_provider_gate'/'REAL_ROUTE_CACHE.json'
PASS=HERE.parent/'k5_actual_route_provider_gate'/'PASS_ASSIGNMENTS.json'

def write(name,obj):
    (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--prepare-only',action='store_true',required=True)
    parser.parse_args();wall=time.monotonic()
    write('PREPARE_HANDLE.json',dict(pid=os.getpid(),mode='prepare_only_with_one_authorized_calibration'))
    base=json.loads(BASE.read_text());cache=json.loads(CACHE.read_text());passed=json.loads(PASS.read_text())
    assert len(passed)==30 and len(cache['roots'])==5
    rows=cache['roots'][0];assert len(rows)==161
    prefix={():0};nodes=[(-1,-1)];groups=[]
    for row in rows:
        w=tuple(row['freeword']);current=()
        for s in w:
            new=current+(s,)
            if new not in prefix:
                prefix[new]=len(nodes);nodes.append((prefix[current],2*(abs(s)-1)+(s<0)))
            current=new
        image=row['field_image'];assert 0<=image<1<<81
        groups.append((row['target'],prefix[w],image&((1<<64)-1),image>>64))
    vectors=[[x//(3**i)%3 for i in range(4)]for x in range(81)]
    field=[]
    for M,v in zip(base['matrices'],base['noise_vectors']):
        tab=[]
        for x in vectors:
            y=[sum(M[i][j]*x[j]for j in range(4))%3 for i in range(4)]
            tab.append([sum(((y[i]+t*v[i])%3)*3**i for i in range(4))for t in range(3)])
        field.append(tab)
    with (HERE/'search_input.txt').open('w')as f:
        f.write('1\n'+str(len(nodes))+'\n')
        for line in nodes:f.write(' '.join(map(str,line))+'\n')
        f.write(str(len(groups))+'\n')
        for line in groups:f.write(' '.join(map(str,line))+'\n')
        for line in base['port_neighbors']:f.write(' '.join(map(str,line))+'\n')
        for p in field:
            for line in p:f.write(' '.join(map(str,line))+'\n')
        f.write(str(len(passed))+'\n')
        for p in passed:f.write(' '.join(map(str,p['chord_V4_values']))+'\n')
    write('INPUT_SCOPE.json',dict(base_input=str(BASE.relative_to(ROOT)),route_cache=str(CACHE.relative_to(ROOT)),
        provider_pass_input=str(PASS.relative_to(ROOT)),source_base=0,source_field=0,raw_words=341,merged_keys=len(groups),
        prefix_nodes=len(nodes),total_tree_gauge_assignments=16**6,provider_surviving_projections=len(passed),
        actual_lift_assignments=len(passed)*4**6,projection_order='PASS_ASSIGNMENTS literal list',
        lift_order='six base4 digits lexicographic; chord0 most significant',
        lift_formula='(V4&1)+2*digit+8*(V4>>1)',
        vertex_label='81*(16*base+deck)+field_little_endian_base3',
        inverse_ports=base['inverse_ports'],chords=base['chords_low_to_high'],
        orbit_roots='(base,deck identity,field), all 5*81; explicit deck left action',
        old_full_NB4_gate_used=False,search_started=False))
    command=['g++','-O3','-std=c++17','-Wall','-Wextra',str(HERE/'search.cpp'),'-o',str(HERE/'search')]
    cp0=resource.getrusage(resource.RUSAGE_CHILDREN)
    with (HERE/'compile.log').open('w')as log:
        process=subprocess.Popen(command,stdout=log,stderr=subprocess.STDOUT)
        write('COMPILE_HANDLE.json',dict(pid=process.pid,command=command));rc=process.wait()
    assert rc==0
    cp1=resource.getrusage(resource.RUSAGE_CHILDREN)
    command=[str(HERE/'search'),'--calibrate',str(HERE/'search_input.txt'),'10']
    with (HERE/'calibration.log').open('w')as log:
        process=subprocess.Popen(command,cwd=HERE,stdout=log,stderr=subprocess.STDOUT)
        write('CALIBRATION_HANDLE.json',dict(pid=process.pid,command=command));rc=process.wait()
    assert rc==0 and json.loads((HERE/'CALIBRATION.json').read_text())['status']=='PASS'
    cp2=resource.getrusage(resource.RUSAGE_CHILDREN)
    self_cpu=time.process_time();child_cpu=cp2.ru_utime+cp2.ru_stime
    write('PREPARE_RESULT.json',dict(status='PREPARED_NOT_SEARCHED',driver_pid=os.getpid(),returncode=0,
        driver_CPU_seconds=self_cpu,compile_CPU_seconds=cp1.ru_utime+cp1.ru_stime-cp0.ru_utime-cp0.ru_stime,
        calibration_child_CPU_seconds=cp2.ru_utime+cp2.ru_stime-cp1.ru_utime-cp1.ru_stime,
        total_CPU_seconds=self_cpu+child_cpu,wall_seconds=time.monotonic()-wall,
        provider_gate_recomputed=False,voltage_enumeration_started=False,
        explicitly_calibrated_assignments=1,actual_search_scope=122880))
    print(json.dumps(json.loads((HERE/'PREPARE_RESULT.json').read_text())))

if __name__=='__main__':main()
