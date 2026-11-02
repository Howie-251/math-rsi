from pathlib import Path
from itertools import product
from collections import Counter,defaultdict
import json,time

P=Path(__file__).resolve().parent
t=time.process_time()
by_shifts=defaultdict(set)
direction2=defaultdict(set)
length_hist=Counter()
witness={}
phase0_words=[]
total=0
for length in range(6):
    for word in product(['t','T','a','b'],repeat=length):
        phase=0;delta=u=v=0;shifts=0;visited=[0]
        for letter in word:
            if letter=='t':
                delta^=1<<(phase%6);phase+=1;shifts+=1
            elif letter=='T':
                phase-=1;delta^=1<<(phase%6);shifts+=1
            elif letter=='a':u^=1<<(phase%6)
            else:v^=1<<(phase%6)
            visited.append(phase)
        total+=1
        if phase%6:continue
        assert phase==0 and delta==0 and shifts in [0,2,4]
        form=u|(v<<6)
        by_shifts[shifts].add(form)
        if shifts==2:direction2[1 if max(visited)>0 else -1].add(form)
        witness.setdefault(form,list(word))
        phase0_words.append(dict(word=list(word),length=length,shift_letters=shifts,
                                 integer_net_shift=phase,delta_coefficient_polynomial=delta,
                                 u_shift_polynomial=u,v_shift_polynomial=v,form=form))
        length_hist[length]+=1
assert total==1365 and len(phase0_words)==351
forms=set(witness)
assert len(forms)==30
assert len(by_shifts[0])==4 and len(by_shifts[2])==26 and len(by_shifts[4])==11
assert len(direction2[1])==len(direction2[-1])==15 and len(direction2[1]&direction2[-1])==4
new4=sorted(by_shifts[4]-(by_shifts[0]|by_shifts[2]))
assert new4==[4,16,256,1024]
records=[]
for form in sorted(forms):
    u=form&63;v=form>>6
    rows=[]
    for bit in range(6):
        row=0
        for shift in range(6):
            if u>>shift&1:row^=1<<((bit-shift)%6)
            if v>>shift&1:row^=1<<(6+(bit-shift)%6)
        rows.append(row)
    records.append(dict(form=form,u_shift_exponents=[s for s in range(6) if u>>s&1],
                        v_shift_exponents=[s for s in range(6) if v>>s&1],
                        output_bit_linear_form_rows=rows,shortest_witness_word=witness[form]))
assert len({tuple(row['output_bit_linear_form_rows']) for row in records})==30
out=dict(status='ALL_DELTA_U_V_PARAMETERS_PHASE0_CAPACITY_OBSTRUCTED',group='F2^6 semidirect C6 by cyclic coordinate shift',
         group_order=384,generators=['t=(delta,1)','t_inverse=(T_inverse delta,-1)','a=(u,0)','b=(v,0)'],
         formal_input_variables=[f'u{i}' for i in range(6)]+[f'v{i}' for i in range(6)],
         shift_convention='T moves lamp bit i to i+1 modulo6; output bit r of T^s u is u_(r-s mod6)',
         all_words_length_at_most5=total,phase0_words=len(phase0_words),phase0_word_count_by_length=dict(length_hist),
         all_phase0_integer_net_shifts_zero=True,all_phase0_delta_coefficients_zero=True,
         phase0_capacity=30,required_phase0_lamps=64,minimum_missing_phase0_lamps=34,
         forms_by_shift_letter_count={k:sorted(v) for k,v in by_shifts.items()},
         two_shift_forms_by_excursion_direction={k:sorted(v) for k,v in direction2.items()},
         two_shift_direction_capacities={k:len(v) for k,v in direction2.items()},
         two_shift_direction_intersection_count=4,four_shift_new_forms=new4,forms=records,
         CPU_seconds=time.process_time()-t,parameter_masks_tested=0,graphs_generated=0,BFS_performed=False,
         other_ring_lengths_or_generating_sets_tested=False,pending=[])
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
(P/'phase0_words.json').write_text(json.dumps(phase0_words,indent=2)+'\n')
print(out['status'],'CPU',out['CPU_seconds'])
print('all words',total,'phase0',len(phase0_words),'capacities',{k:len(v) for k,v in by_shifts.items()},'union',len(forms))
print('two directions',{k:len(v) for k,v in direction2.items()},'intersection',4,'new4',new4)
