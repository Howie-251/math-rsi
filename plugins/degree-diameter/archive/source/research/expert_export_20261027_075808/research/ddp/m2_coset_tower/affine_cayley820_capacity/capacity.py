#!/usr/bin/env python3
"""One bounded complete phase/symbolic capacity pass; no field search or BFS."""
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
import importlib.util
import json
import os
import resource
import time

Q=41
M=20
D=12
PRIMITIVE=6
R=36
CPU_LIMIT=60.0

def convolution(a,b):
    out=[0]*M
    for j,x in enumerate(a):
        if x:
            for k,y in enumerate(b):
                if y:out[(j+k)%M]+=x*y
    return out

def main():
    start=time.process_time();base=Path(__file__).resolve().parent
    assert not (base/'terminal.json').exists(), 'Do not restart a completed or stopped capacity pass.'
    assert pow(PRIMITIVE,20,Q)!=1 and pow(PRIMITIVE,8,Q)!=1
    assert PRIMITIVE*PRIMITIVE%Q==R
    scalar=[pow(R,j,Q) for j in range(M)]
    assert len(set(scalar))==M and scalar[10]==40
    shared=base.parent/'axis_cayley272/symbolic_affine_words.py'
    spec=importlib.util.spec_from_file_location('symbolic_affine_words',shared)
    helper=importlib.util.module_from_spec(spec);spec.loader.exec_module(helper)
    product=[[(j+k)%M for k in range(M)] for j in range(M)]
    inverse=[-j%M for j in range(M)]
    count=plain_pass=symbolic_pass=0
    survivors=[]
    grouped=[{'pairs':p,'involutions':D-2*p,'scope':comb(p+9,p),'completed':0,'plain_pass':0,'symbolic_pass':0,'free_coordinates':D-p,'projective_classes_per_pattern':(Q**(D-p-1)-1)//(Q-1),'surviving_projective_input_bound':0} for p in range(7)]
    assert sum(g['scope'] for g in grouped)==8008
    timed_out=False;plain_cpu=symbolic_cpu=0.0
    run={'status':'RUNNING','running':True,'pid':os.getpid(),'worker_count':1,'CPU_budget_seconds':CPU_LIMIT,'patterns_scope':8008,'group_order':820,'degree':D,'target_diameter':3,'primitive':PRIMITIVE,'action_root':R,'actual_graphs_generated':0,'field_assignments_tested':0,'BFS_runs':0}
    (base/'run.json').write_text(json.dumps(run,indent=2)+'\n')
    with (base/'patterns.jsonl').open('w') as stream:
        for p in range(7):
            i=D-2*p
            for phases in combinations_with_replacement(range(10),p):
                if time.process_time()-start>=58.5:
                    timed_out=True;break
                before=time.process_time()
                a=[0]*M
                for j in phases:a[j]+=1;a[-j%M]+=1
                a[10]+=i
                square=convolution(a,a);cube=convolution(square,a)
                raw=[cube[j]+square[j]+(2-2*D)*a[j]+((1-D) if j==0 else 0) for j in range(M)]
                assert min(raw)>=0 and sum(raw)==1597 and all(raw[j]==raw[-j%M] for j in range(M))
                plain=min(raw)>=Q
                plain_cpu+=time.process_time()-before
                row={'id':count,'pairs':p,'involutions':i,'pair_phases':list(phases),'involution_phase':10,'raw_word_counts':raw,'plain_capacity_pass':plain,'symbolic_capacity_evaluated':False,'free_coordinates':D-p,'projective_input_bound':grouped[p]['projective_classes_per_pattern']}
                if plain:
                    before=time.process_time()
                    components=[{'phase':j,'kind':'pair'} for j in phases]+[{'phase':10,'kind':'involution'} for _ in range(i)]
                    result=helper.affine_word_forms(Q,product,inverse,scalar,components)
                    assert result['raw_counts']==raw
                    symbolic=min(result['form_counts'])>=Q
                    row.update(symbolic_capacity_evaluated=True,symbolic_form_counts=result['form_counts'],symbolic_capacity_pass=symbolic,symbolic_deficient_phases=[j for j,n in enumerate(result['form_counts']) if n<Q])
                    plain_pass+=1;grouped[p]['plain_pass']+=1
                    if symbolic:
                        anchor=next(s for s,c in enumerate(components) if scalar[c['phase']]!=1)
                        dropped_counts=[len({c[:anchor]+c[anchor+1:] for c in f}) for f in result['forms']]
                        assert dropped_counts==result['form_counts']
                        row.update(anchor_slot=anchor,anchor_projection_preserves_form_counts=True)
                        survivors.append(row.copy());symbolic_pass+=1;grouped[p]['symbolic_pass']+=1
                        grouped[p]['surviving_projective_input_bound']+=row['projective_input_bound']
                    symbolic_cpu+=time.process_time()-before
                stream.write(json.dumps(row,separators=(',',':'))+'\n')
                count+=1;grouped[p]['completed']+=1
                if count%128==0:
                    stream.flush()
                    (base/'progress.json').write_text(json.dumps({'completed_patterns':count,'scope':8008,'plain_pass':plain_pass,'symbolic_pass':symbolic_pass,'CPU_seconds':time.process_time()-start,'by_composition':grouped},indent=2)+'\n')
            if timed_out:break
    status='CPU_LIMIT_INCOMPLETE' if timed_out else 'COMPLETE_CAPACITY_ONLY'
    if not timed_out:assert count==8008
    bound=sum(g['surviving_projective_input_bound'] for g in grouped)
    result={'status':status,'group':'F41 semidirect_36 C20','primitive':PRIMITIVE,'action_root':R,'scalar_powers':scalar,'group_order':820,'degree':12,'target_diameter':3,'involutions':41,'noninvolution_pairs_by_phase_class':[20]+[41]*9,'scope':8008,'completed_patterns':count,'next_cursor':count,'plain_capacity_pass':plain_pass,'symbolic_capacity_pass':symbolic_pass,'by_composition':grouped,'surviving_marked_projective_input_bound':bound,'survivors_file':'symbolic_survivors.json','pattern_file':'patterns.jsonl','CPU_seconds':time.process_time()-start,'plain_CPU_seconds':plain_cpu,'symbolic_CPU_seconds':symbolic_cpu,'CPU_budget_seconds':CPU_LIMIT,'worker_count':1,'running':False,'field_assignments_tested':0,'actual_graphs_generated':0,'BFS_runs':0,'bound_is_before_actual_generator_legality_filter':True}
    (base/'symbolic_survivors.json').write_text(json.dumps(survivors,indent=2)+'\n')
    usage=resource.getrusage(resource.RUSAGE_SELF)
    result['recorded_process_CPU_seconds']=usage.ru_utime+usage.ru_stime
    (base/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
    run.update(status=status,running=False,exit_code=0,next_cursor=count,recorded_process_CPU_seconds=result['recorded_process_CPU_seconds'])
    (base/'run.json').write_text(json.dumps(run,indent=2)+'\n')
    (base/'progress.json').write_text(json.dumps({'status':status,'completed_patterns':count,'scope':8008,'plain_pass':plain_pass,'symbolic_pass':symbolic_pass,'CPU_seconds':result['CPU_seconds'],'by_composition':grouped},indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
