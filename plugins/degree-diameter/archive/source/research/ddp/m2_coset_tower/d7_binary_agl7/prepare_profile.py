"""Actual F8^2 semidirect-product tower; six balanced, unnormalized samples."""
from pathlib import Path
from itertools import combinations
import json
import random
import resource
import subprocess

HERE=Path(__file__).resolve().parent
SEED=2026102607
def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
def mul(a,b):
    z=0
    while b:
        if b&1:z^=a
        b>>=1;a<<=1
        if a&8:a^=11
    return z
def power(a,n):
    z=1
    for _ in range(n):z=mul(z,a)
    return z
Z=[power(2,j) for j in range(7)]
K=[(a,b,e) for e in range(2) for b in range(3) for a in range(7)]
def encode(k):
    a,b,e=k;return a+7*b+21*e
KP=[];KI=[];ACTION=[]
for a,b,e in K:
    c=(-1 if e else 1)*2**b%7
    KP.append([encode(((a+c*d)%7,(b+f)%3,e^h)) for d,f,h in K])
    ci=pow(c,-1,7)
    KI.append(encode((-ci*a%7,-b%3,e)))
    row=[]
    for x in range(64):
        u,v=x%8,x//8
        if e:u,v=v,u
        row.append(mul(Z[a],power(u,2**b))+8*mul(Z[-a%7],power(v,2**b)))
    ACTION.append(row)
def gp(g,h):
    return (g%64^ACTION[g//64][h%64])+64*KP[g//64][h//64]
def inv(g):
    k=KI[g//64];return ACTION[k][g%64]+64*k
for k in range(42):
    assert KP[k][KI[k]]==KP[KI[k]][k]==0
    for l in range(42):
        assert all(ACTION[KP[k][l]][x]==ACTION[k][ACTION[l][x]] for x in range(64))
for g in range(2688):assert gp(g,inv(g))==gp(inv(g),g)==0
H=[k for k,(a,b,e) in enumerate(K) if a==0]
L=[0]*7
for k,(a,b,e) in enumerate(K):
    if a==0:L[(-1 if e else 1)*2**b%7]=k
for k in range(42):
    for h in H:assert K[KP[k][h]][0]==K[k][0]

names=['product1_7','axes14','product124_21','product356_21','zero']
def colour(x):
    u,v=x%8,x//8
    if not u and not v:return 'zero'
    if not u or not v:return 'axes14'
    p=mul(u,v)
    if p==1:return 'product1_7'
    return 'product124_21' if p in (Z[1],Z[2],Z[4]) else 'product356_21'
invol={c:[] for c in names};pairs={c:[] for c in names}
for g in range(1,2688):
    h=inv(g);c=colour(g%64);assert colour(h%64)==c
    if g==h:invol[c].append(g)
    elif g<h:pairs[c].append([g,h])
independent=json.loads((HERE/'STRUCTURE_CHECK.json').read_text())
for row in independent['horizontal_orbits']:
    c=row['name']
    assert invol[c]==row['nonidentity_involutions_G_encoded']
    assert len(pairs[c])==row['inverse_pair_count']
    assert {x for x in range(64) if colour(x)==c}==set(row['A_members_encoded'])
assert sum(map(len,invol.values()))==119 and sum(map(len,pairs.values()))==1284
def describe(g):
    x=g%64;return {'code':g,'u':x%8,'v':x//8,'K':K[g//64],'colour':colour(x)}

samples=[];branches=[];rng=random.Random(SEED);allsets=set()
for branch,ic in enumerate(combinations(names[:4],2)):
    pc=[c for c in names[:4] if c not in ic]
    lists=[invol[c] for c in ic]+[pairs[c] for c in pc]
    used=set()
    for j in range(200):
        while True:
            idx=tuple(rng.randrange(len(z)) for z in lists)
            if idx not in used:break
        used.add(idx)
        S=[lists[0][idx[0]],lists[1][idx[1]],*lists[2][idx[2]],*lists[3][idx[3]]]
        assert len(set(S))==6 and 0 not in S and set(map(inv,S))==set(S)
        hh={0}
        for s in S:hh.update(ACTION[k][s%64] for k in range(42))
        assert len(hh)==64
        key=tuple(sorted(S));assert key not in allsets;allsets.add(key)
        samples.append({'cursor':len(samples),'branch':branch,'branch_cursor':j,'indices':idx,'S':S})
    branches.append({'branch':branch,'involution_colours':ic,'pair_colours':pc,
                     'component_list_sizes':list(map(len,lists)),'sample_count':200})
structure={'field':'F8=F2[t]/(t^3+t+1)','zeta':2,'zeta_powers':Z,
 'A_encoding':'x=u+8*v','K_encoding':'a+7*b+21*e',
 'group_encoding':'x+64*K_code',
 'K_multiplication':'(a,b,e)*(c,d,f)=(a+(-1)^e*2^b*c mod7,b+d mod3,e+f mod2)',
 'action':'swap u,v if e=1, then (zeta^a*u^(2^b),zeta^(-a)*v^(2^b))',
 'group_multiplication':'(x,k)*(y,l)=(x XOR action[k][y],k*l)',
 'group_inverse':'(action[k^-1][x],k^-1)',
 'K_coordinates':K,'K_multiplication_table':KP,'K_inverse':KI,'K_action':ACTION,
 'H_K_codes':H,'H_normal':False,'multiplicative_L_K_codes':L,
 'layer_sizes':[2688,448,64],'n':3200,'degree':7,'edges':11200,
 'leaf_label':'x+64*K_code','block_label':'2688+x+64*a','head_label':'3136+x',
 'source_individual_element_lists_and_orbits_match':True,
 'no_symmetry_normalization':True}
(HERE/'profile_structure.json').write_text(json.dumps(structure,indent=2)+'\n')
(HERE/'profile_generator_lists.json').write_text(json.dumps({'involutions_by_colour':invol,'inverse_pairs_by_colour':pairs},indent=2)+'\n')
metadata={'seed':SEED,'PRNG':'Python random.Random, MT19937; all actual selected inputs also saved',
 'scope':'Six unnormalized colour allocations; 200 distinct component tuples sampled without replacement per allocation.',
 'component_order':'two involution colours then two inverse-pair colours, each in the displayed orbit order',
 'list_order':'increasing involution code / increasing minimum pair code',
 'branches':branches,'samples':1200,'first_sample_also_profile_cursor':0,
 'all_generator_sets_distinct':True,'all_legal_and_HH_verified':True,
 'no_division_by_six':True,'full_production_started':False,
 'BB_masks_are_calibration_only_not_filter':True}
(HERE/'profile_metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
with (HERE/'profile.inputs.jsonl').open('w') as f:
    for row in samples:f.write(json.dumps(row)+'\n')
with (HERE/'profile.inputs.txt').open('w') as f:
    f.write('1200\n')
    for row in samples:f.write(' '.join(map(str,row['S']))+'\n')
(HERE/'preflight.parameters.json').write_text(json.dumps({'cursor':0,'S':samples[0]['S'],
 'generators':list(map(describe,samples[0]['S'])),'branch':branches[0],'seed':SEED},indent=2)+'\n')
with (HERE/'profile_tables.hpp').open('w') as f:
    def arr(name,rows):
        f.write('static const int '+name+'['+str(len(rows))+']['+str(len(rows[0]))+']={\n')
        for row in rows:f.write('{'+','.join(map(str,row))+'},\n')
        f.write('};\n')
    arr('KACTION',ACTION);arr('KPROD',KP);arr('KCOORD',K)
    f.write('static const int HCODE[6]={'+','.join(map(str,H))+'};\n')
    f.write('static const int LCODE[7]={'+','.join(map(str,L))+'};\n')
before=cpu()
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'profile.cpp'),'-o',str(HERE/'profile')],check=True)
elapsed=cpu()-start
out={'status':'PREPARED','cpu_seconds':elapsed,'compile_cpu_seconds':cpu()-before,
 'samples':1200,'first_sample_is_cursor_zero':True,'source_structure_lists_match':True,'full_production_started':False}
(HERE/'prepare.terminal.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'terminal':out,'first_S':samples[0]['S'],'branches':branches},indent=2))
