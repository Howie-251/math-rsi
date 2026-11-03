"""Actual F7^2 x C3 group and one bounded five-allocation sample, with head triangles."""
from pathlib import Path
from itertools import combinations
import json
import random
import resource
import subprocess
HERE=Path(__file__).resolve().parent
SEED=2026102608
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
X=[(x%7,x//7%7,x//49) for x in range(147)]
K=[(k%7,k//7) for k in range(42)]
def encode(u,v,w):return u%7+7*(v%7)+49*(w%3)
ADD=[[encode(u+a,v+b,w+c) for a,b,c in X] for u,v,w in X]
NEG=[encode(-u,-v,-w) for u,v,w in X]
P3=[pow(3,j,7) for j in range(6)];P4=[pow(4,j,7) for j in range(6)]
KP=[[(b+P4[j]*d)%7+7*((j+l)%6) for d,l in K] for b,j in K]
KI=[(-pow(4,-j,7)*b)%7+7*(-j%6) for b,j in K]
ACTION=[[encode(P3[5*j%6]*u+b*P3[j]*v,P3[j]*v,w) for u,v,w in X] for b,j in K]
def gp(g,h):return ADD[g%147][ACTION[g//147][h%147]]+147*KP[g//147][h//147]
def inv(g):
    k=KI[g//147];return NEG[ACTION[k][g%147]]+147*k
for k in range(42):
    assert KP[k][KI[k]]==KP[KI[k]][k]==0
    for l in range(42):assert all(ACTION[KP[k][l]][x]==ACTION[k][ACTION[l][x]] for x in range(147))
    for h in range(7):assert K[KP[k][h]][1]==K[k][1]
for g in range(6174):assert gp(g,inv(g))==gp(inv(g),g)==0
def colour(x):
    u,v,w=X[x]
    return 'offaxis' if v else ('axis' if u else 'zero')
invol={c:[] for c in ['zero','axis','offaxis']};pairs={c:[] for c in invol}
for g in range(1,6174):
    if X[g%147][2]:continue
    h=inv(g);assert X[h%147][2]==0 and colour(h%147)==colour(g%147)
    if g==h:invol[colour(g%147)].append(g)
    elif g<h:pairs[colour(g%147)].append([g,h])
assert [len(invol[c]) for c in invol]==[1,6,42]
assert [len(pairs[c]) for c in pairs]==[20,123,861]
internal=[[],[],[],[],[]]
for a,b in pairs['axis']:
    for c in invol['offaxis']:internal[0].append([a,b,c])
for a,b in pairs['offaxis']:
    for c in invol['axis']:internal[1].append([a,b,c])
for a,b in combinations(invol['axis'],2):
    for c in invol['offaxis']:internal[2].append([a,b,c])
for a in invol['axis']:
    for b,c in combinations(invol['offaxis'],2):internal[3].append([a,b,c])
for a in invol['axis']:
    for b in invol['offaxis']:
        for c in invol['zero']:internal[4].append([a,b,c])
assert list(map(len,internal))==[5166,5166,630,5166,252]
assert sum(map(len,internal))*42**2==28894320
names=['axis_pair+offaxis_involution','offaxis_pair+axis_involution',
       'two_axis_involutions+one_offaxis','one_axis_involution+two_offaxis',
       'axis_involution+offaxis_involution+zero_involution']
samples=[];branches=[];rng=random.Random(SEED);seen_all=set()
for branch,options in enumerate(internal):
    target=300 if branch<2 else 200;seen=set()
    for j in range(target):
        while True:
            k1,k2,idx=rng.randrange(42),rng.randrange(42),rng.randrange(len(options))
            if (k1,k2,idx) not in seen:break
        seen.add((k1,k2,idx));g=50+147*k1;h=56+147*k2
        S=[g,inv(g),h,inv(h),*options[idx]]
        assert len(set(S))==7 and 0 not in S and set(map(inv,S))==set(S)
        hh={0,49,98}
        for s in S:hh.update(ACTION[k][s%147] for k in range(42))
        assert len(hh)==147
        key=tuple(sorted(S));assert key not in seen_all;seen_all.add(key)
        samples.append({'cursor':len(samples),'branch':branch,'branch_cursor':j,
                        'cross_K_codes':[k1,k2],'internal_option_index':idx,'S':S})
    branches.append({'branch':branch,'name':names[branch],'internal_options':len(options),
                     'full_normalized_inputs':len(options)*42**2,'profile_samples':target})
def desc(g):return {'code':g,'u_v_w':X[g%147],'b_j':K[g//147]}
structure={'A':'F7^2 x C3','A_encoding':'u+7*v+49*w','A_coordinates':X,
 'A_addition':'component addition modulo 7,7,3; not XOR','A_negative':NEG,
 'K_encoding':'b+7*j','K_coordinates':K,
 'K_multiplication':'(b,j)*(d,l)=(b+4^j*d mod7,j+l mod6)',
 'K_inverse':'(-4^(-j)*b mod7,-j mod6)',
 'K_action':'(u,v,w)->(3^(5j)*u+b*3^j*v mod7,3^j*v mod7,w)',
 'K_multiplication_table':KP,'K_inverse_table':KI,'K_action_table':ACTION,
 'group_encoding':'x+147*K_code','group_multiplication':'(x,k)*(y,l)=(x+k(y),k*l)',
 'group_inverse':'(-k^-1(x),k^-1)','H_K_codes':list(range(7)),
 'leaf_label':'x+147*K_code','block_label':'6174+x+147*j','head_label':'7056+x',
 'leaf_parent':'6174+(leaf%147)+147*((leaf//147)//7)',
 'block_parent':'7056+(block-6174)%147',
 'head_edges':'For each u,v, join the three heads w=0,1,2 as K3.',
 'layer_sizes':[6174,882,147],'n':7203,'degree':8,'edges':28812,
 'all_group_inverse_checks':6174,'all_K_action_composition_checks':42*42*147,
 'right_H_coset_labels_checked':True,
 'internal_involution_counts':{c:len(v) for c,v in invol.items()},
 'internal_inverse_pair_counts':{c:len(v) for c,v in pairs.items()},
 'cross_normalization':'w=1 representatives have field vectors (1,0) and (0,1); their two K codes are unrestricted.',
 'old_BB_formula_used':False,'all_candidates_scored_by_actual_three_root_BFS':True}
(HERE/'structure.json').write_text(json.dumps(structure,indent=2)+'\n')
(HERE/'internal_generator_lists.json').write_text(json.dumps({'involutions':invol,'inverse_pairs':pairs},indent=2)+'\n')
(HERE/'internal_options.json').write_text(json.dumps(internal)+'\n')
metadata={'seed':SEED,'PRNG':'Python random.Random / MT19937','branches':branches,
 'scope':'1200 balanced sampled tuples only; no complete production',
 'all_inputs_saved':True,'all_generator_sets_distinct':True,'full_normalized_scope_not_executed':28894320,
 'first_sample_is_profile_cursor_zero':True,'profile_cursor_zero_cached_not_rescored':True,
 'three_root_weights':[6174,882,147],'three_roots':[0,6174,7056],
 'no_route_formula_filter':True,'new_head_edges_present':True}
(HERE/'profile_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
with (HERE/'profile.inputs.jsonl').open('w') as f:
    for row in samples:f.write(json.dumps(row)+'\n')
with (HERE/'profile.inputs.txt').open('w') as f:
    f.write('1200\n')
    for row in samples:f.write(' '.join(map(str,row['S']))+'\n')
(HERE/'preflight.parameters.json').write_text(json.dumps({'cursor':0,'S':samples[0]['S'],
 'generators':list(map(desc,samples[0]['S'])),'input':samples[0],'seed':SEED},indent=2)+'\n')
with (HERE/'engine_tables.hpp').open('w') as f:
    def arr(name,rows):
        f.write('static const int '+name+'['+str(len(rows))+']['+str(len(rows[0]))+']={\n')
        for row in rows:f.write('{'+','.join(map(str,row))+'},\n')
        f.write('};\n')
    arr('KACTION',ACTION);arr('KPROD',KP);arr('KCOORD',K);arr('AADD',ADD)
before=cpu();subprocess.run(['g++','-O3','-std=c++17',str(HERE/'profile.cpp'),'-o',str(HERE/'profile')],check=True)
out={'status':'PREPARED','cpu_seconds':cpu()-start,'compile_cpu_seconds':cpu()-before,
 'profile_samples':1200,'full_production_started':False,'counts_match':True}
(HERE/'prepare.terminal.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'terminal':out,'first_S':samples[0]['S'],'branches':branches},indent=2))
