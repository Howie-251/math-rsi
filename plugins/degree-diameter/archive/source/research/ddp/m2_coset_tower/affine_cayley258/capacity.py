#!/usr/bin/env python3
from itertools import combinations_with_replacement
from pathlib import Path
from math import comb
import importlib.util
import json
import resource
import time

def main():
    start=time.process_time()
    base=Path(__file__).resolve().parent
    shared=base.parent/'axis_cayley272/symbolic_affine_words.py'
    spec=importlib.util.spec_from_file_location('symbolic_affine_words',shared)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    q=43;r=37;m=6
    scalar=[pow(r,j,q) for j in range(m)]
    assert pow(3,7,q)==r and len(set(scalar))==6 and scalar[3]==42
    phase_product=[[(a+b)%m for b in range(m)] for a in range(m)]
    phase_inverse=[-j%m for j in range(m)]
    records=[];survivors=[];groups=[]
    for p in range(5):
        i=8-2*p;plain_pass=symbolic_pass=bound=0
        for phases in combinations_with_replacement(range(3),p):
            components=[{'phase':j,'kind':'pair'} for j in phases]+[{'phase':3,'kind':'involution'} for _ in range(i)]
            words=module.affine_word_forms(q,phase_product,phase_inverse,scalar,components)
            assert sum(words['raw_counts'])==457
            plain=min(words['raw_counts'])>=q
            symbolic=min(words['form_counts'])>=q
            assert not symbolic or plain
            coordinates=p+i
            projective=(q**(coordinates-1)-1)//(q-1)
            row={'id':len(records),'pairs':p,'involutions':i,'pair_phases':list(phases),'involution_phases':[3]*i,'raw_word_counts':words['raw_counts'],'symbolic_form_counts':words['form_counts'],'plain_capacity_pass':plain,'symbolic_capacity_pass':symbolic,'free_coordinates':coordinates,'projective_input_bound':projective,'coefficient_forms_by_phase':[[list(c) for c in sorted(f)] for f in words['forms']]}
            records.append(row);plain_pass+=plain;symbolic_pass+=symbolic
            if symbolic:
                anchor=next(s for s,c in enumerate(components) if scalar[c['phase']]!=1)
                row['anchor_slot']=anchor
                assert all(len({c[:anchor]+c[anchor+1:] for c in f})==len(f) for f in words['forms'])
                row['anchor_projection_preserves_form_counts']=True
                survivors.append(row);bound+=projective
        groups.append({'pairs':p,'involutions':i,'patterns':comb(p+2,p),'plain_capacity_pass':plain_pass,'symbolic_capacity_pass':symbolic_pass,'projective_input_bound':bound})
    assert len(records)==35
    output={'status':'COMPLETE_PHASE_AND_SYMBOLIC_CAPACITY','group':'F43 semidirect_37 C6','group_order':258,'degree':8,'target_diameter':3,'scalar_powers':scalar,'involutions':43,'inverse_pairs_by_phase_class':[21,43,43],'phase_patterns':35,'plain_capacity_pass':sum(g['plain_capacity_pass'] for g in groups),'symbolic_capacity_pass':len(survivors),'projective_input_bound':sum(g['projective_input_bound'] for g in groups),'by_composition':groups,'survivors':survivors,'shared_symbolic_routine':str(shared),'graphs_generated':0,'field_assignments_tested':0,'CPU_seconds':time.process_time()-start}
    (base/'CAPACITY_RESULTS.json').write_text(json.dumps(output,indent=2)+'\n')
    (base/'capacity_patterns.json').write_text(json.dumps(records,separators=(',',':'))+'\n')
    usage=resource.getrusage(resource.RUSAGE_SELF)
    (base/'capacity_cpu.json').write_text(json.dumps({'process_CPU_seconds':usage.ru_utime+usage.ru_stime,'enumeration_CPU_seconds':output['CPU_seconds']},indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k!='survivors'},indent=2))

if __name__=='__main__':main()
