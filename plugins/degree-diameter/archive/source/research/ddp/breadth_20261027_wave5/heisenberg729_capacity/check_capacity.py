from pathlib import Path
from itertools import product
from collections import defaultdict,Counter
import json,time

P=Path(__file__).resolve().parent
t=time.process_time()
letters=[(i,sign) for i in range(5) for sign in [1,-1]]
pairs=[(i,j) for i in range(5) for j in range(i+1,5)]
pair_index={p:5+k for k,p in enumerate(pairs)}
by_exponent=defaultdict(list)
total=0
for length in range(4):
    for word in product(letters,repeat=length):
        exponent=[0]*5
        form=[0]*15
        for i,sign in word:exponent[i]=(exponent[i]+sign)%3;form[i]=(form[i]+sign)%3
        for pos,(i,sign) in enumerate(word):
            for j,other in word[pos+1:]:
                if i==j:continue
                a,b=sorted((i,j));orientation=1 if i<j else -1
                q=pair_index[a,b]
                form[q]=(form[q]+2*sign*other*orientation)%3
        by_exponent[tuple(exponent)].append(dict(word=[list(letter) for letter in word],center_form=form))
        total+=1
assert total==1111 and len(by_exponent)==131
def add(a,b,sign):return tuple((x+sign*y)%3 for x,y in zip(a,b))
def weight(v):return sum(x!=0 for x in v)
def witness(c):
    support=[i for i,x in enumerate(c) if x]
    outside=[i for i,x in enumerate(c) if not x]
    w=len(support);x=[0]*5
    if w in [1,2]:
        for i in outside[:3]:x[i]=1
    elif w==3:
        x[support[0]]=c[support[0]]
        for i in outside:x[i]=1
    return tuple(x)
records=[];canonical=[]
for c in product(range(3),repeat=5):
    if not any(c) or next(x for x in c if x)!=1:continue
    w=weight(c);x=witness(c)
    coset=[x,add(x,c,1),add(x,c,-1)]
    reached=[v for v in coset if v in by_exponent]
    assert len(reached)==1 and reached[0]==x
    words=[row for v in reached for row in by_exponent[v]]
    forms=sorted({tuple(row['center_form']) for row in words})
    if w<=3:assert weight(x)==3 and len(words)==6 and len(forms)<=6
    else:assert x==(0,)*5 and len(forms)==1 and forms[0]==(0,)*15
    row=dict(relation=c,relation_weight=w,witness_exponent=x,
             projection_coset_representatives=coset,coset_weight_list=[weight(v) for v in coset],
             only_representative_reachable_within3=x,words_at_most3=len(words),
             distinct_generic_center_form_upper_bound=len(forms),required_center_values=9)
    records.append(row)
    if c==tuple([1]*w+[0]*(5-w)):
        canonical.append(dict(**row,complete_words=words,distinct_generic_center_forms=forms))
assert len(records)==121 and len(canonical)==5
counts=dict(Counter(row['relation_weight'] for row in records))
assert counts=={1:5,2:20,3:40,4:40,5:16}
out=dict(status='ALL_FIVE_RELATION_WEIGHTS_OBSTRUCTED',group='UT3(F9)',group_order=729,
         inverse_generator_pairs=5,target_degree=10,target_diameter=3,
         center_size=9,projection_F3_dimension=4,full_rank_kernel_dimension=1,
         rank_below4_status='disconnected: all word projections remain in a proper subspace of F3^4',
         normalized_relation_lines_checked=121,nonzero_relation_vectors_represented=242,
         relation_lines_by_weight=counts,all_words_of_length_at_most3=total,
         distinct_mod3_exponent_vectors=131,
         generic_center_variables=[f't{i}' for i in range(5)]+[f'B{i}{j}' for i,j in pairs],
         generic_center_formula='Symmetric center t=z-xy/2; a word has sum(sign*t_i) + (1/2)*sum_{p<q} sign_p sign_q B(v_i,v_j), with 1/2=2 in F3. Treating B_ij as independent gives an upper bound; actual F9 substitutions and relation constraints can only identify values.',
         canonical_weight_cases=canonical,all_relation_line_witnesses=records,
         largest_witness_center_capacity=6,parameters_searched=0,graphs_generated=0,BFS_performed=False,
         CPU_seconds=time.process_time()-t,pending=[])
(P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['status'],'CPU',out['CPU_seconds'])
for row in canonical:print('weight',row['relation_weight'],'coset_weights',row['coset_weight_list'],'words',row['words_at_most3'],'formal_capacity',row['distinct_generic_center_form_upper_bound'])
