"""Actual AGL(1,8) tower tables and one explicitly bounded HH-coloured profile."""
from pathlib import Path
import json
import resource
import subprocess
import time

HERE = Path(__file__).resolve().parent

def cpu():
    a=resource.getrusage(resource.RUSAGE_SELF); b=resource.getrusage(resource.RUSAGE_CHILDREN)
    return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime

start=cpu()
def mul(a,b):
    z=0
    while b:
        if b&1: z ^= a
        b >>= 1; a <<= 1
        if a&8: a ^= 11
    return z

fm=[[mul(a,b) for b in range(8)] for a in range(8)]
fi=[0]+[next(b for b in range(1,8) if fm[a][b]==1) for a in range(1,8)]
coords=[(a,b) for a in range(1,8) for b in range(8)]
kprod=[[8*(fm[a][c]-1)+(fm[a][d]^b) for c,d in coords] for a,b in coords]
kinv=[8*(fi[a]-1)+fm[fi[a]][b] for a,b in coords]
perms=[[fm[a][t]^b for t in range(8)] for a,b in coords]
masks=[(x<<1)|(x.bit_count()&1) for x in range(128)]
action=[]
for perm in perms:
    row=[]
    for mask in masks:
        moved=sum(1<<perm[t] for t in range(8) if mask>>t&1)
        assert moved.bit_count()%2==0
        row.append(moved>>1)
    action.append(row)

def gp(g,h):
    x,k=g%128,g//128; y,l=h%128,h//128
    return (x^action[k][y])+128*kprod[k][l]

def inv(g):
    x,k=g%128,g//128; ki=kinv[k]
    return action[ki][x]+128*ki

for k in range(56):
    assert kprod[k][kinv[k]]==kprod[kinv[k]][k]==0
    for l in range(56):
        assert all(action[kprod[k][l]][x]==action[k][action[l][x]] for x in range(128))
    for h in range(0,56,8):
        assert coords[kprod[k][h]][1]==coords[k][1]
for g in range(7168):
    assert gp(g,inv(g))==gp(inv(g),g)==0
orbits=[]; orbit_id=[-1]*128
for x in range(128):
    if orbit_id[x]>=0: continue
    orbit=sorted({row[x] for row in action})
    oid=len(orbits)
    for y in orbit: orbit_id[y]=oid
    orbits.append(orbit)

def colour(x):
    w=masks[x].bit_count()
    if w==0: return 'zero'
    if w==8: return 'allones'
    if w==2: return 'weight2'
    if w==6: return 'weight6'
    assert w==4
    syndrome=0
    for t in range(8):
        if masks[x]>>t&1: syndrome ^= t
    return 'plane4' if syndrome==0 else 'nonplane4'

names=['zero','allones','plane4','weight2','weight6','nonplane4']
invol={c:[] for c in names}; pairs={c:[] for c in names}
for g in range(1,7168):
    h=inv(g); c=colour(g%128)
    assert colour(h%128)==c
    if h==g: invol[c].append(g)
    elif g<h: pairs[c].append([g,h])
counts={c:{'orbit_size':sum(colour(x)==c for x in range(128)),
           'involutions':len(invol[c]),'inverse_pairs':len(pairs[c])} for c in names}
expected={'zero':(1,7,24),'allones':(1,8,24),'plane4':(14,56,364),
          'weight2':(28,56,756),'weight6':(28,56,756),'nonplane4':(56,56,1540)}
assert all(tuple(counts[c].values())==expected[c] for c in names)

def describe(g):
    x,k=g%128,g//128; a,b=coords[k]
    return {'code':g,'A_index':x,'mask':masks[x],'k_code':k,'a':a,'b':b,'colour':colour(x)}

def check(S):
    assert len(S)==7 and len(set(S))==7 and 0 not in S
    assert set(map(inv,S))==set(S)
    hh={0}
    for s in S: hh.update(action[k][s%128] for k in range(56))
    assert len(hh)==128

preflight=[255,263,254,1153,inv(1153),1291,inv(1291)]
check(preflight)
samples=[]
seen=set()
for j in range(2000):
    inds=[j%8,(13*j+7)%56,(23*j+19)%56,(17*j+31)%756,(37*j+5)%1540]
    S=[invol['allones'][inds[0]],invol['plane4'][inds[1]],invol['weight6'][inds[2]],
       *pairs['weight2'][inds[3]],*pairs['nonplane4'][inds[4]]]
    check(S)
    key=tuple(sorted(S)); assert key not in seen; seen.add(key)
    samples.append({'cursor':j,'component_indices':inds,'S':S})

structure={'field':'F2[t]/(t^3+t+1)','polynomial_binary':11,
 'A':'even-weight vectors on coordinate points 0..7','A_masks':masks,
 'A_encoding':'index=mask>>1; mask=(index<<1)|parity(index)',
 'K':'AGL(1,8), map t -> a*t xor b','K_encoding':'b+8*(a-1)',
 'K_coordinates':coords,'K_coordinate_permutations':perms,'K_multiplication':kprod,'K_inverse':kinv,
 'K_action_on_A':action,'group_encoding':'A_index+128*K_code',
 'group_multiplication':'(x,k)*(y,l)=(x xor action[k][y],k*l)',
 'group_inverse':'(x,k)^-1=(action[k^-1][x],k^-1)',
 'H_K_codes':list(range(0,56,8)),'H_order':7,'H_normal':False,
 'label_leaf':'A_index+128*K_code',
 'label_block':'7168+A_index+128*b, b=k(0)',
 'label_head':'8192+A_index',
 'leaf_parent':'7168+(leaf%128)+128*K_coordinates[leaf//128][1]',
 'block_parent':'8192+(block-7168)%128',
 'layer_sizes':[7168,1024,128],'n':8320,'degree':8,'edges':33280,
 'A_K_orbits':[{'indices':orb,'colour':colour(orb[0])} for orb in orbits],
 'generator_counts':counts,'nonidentity_involutions':239,'noninvolution_inverse_pairs':3464,
 'checks':{'all_group_inverses':True,'all_K_actions_compose':True,'right_H_coset_labels':True},
 'HH_rule':'union of K-orbits of generator A-components plus zero is all A',
 'normalizations_used':[],'old_normal_H_BB_formula_used':False}
(HERE/'structure.json').write_text(json.dumps(structure,indent=2)+'\n')
(HERE/'generator_lists.json').write_text(json.dumps({'involutions_by_colour':invol,'inverse_pairs_by_colour':pairs},indent=2)+'\n')
(HERE/'preflight.parameters.json').write_text(json.dumps({'S':preflight,'generators':list(map(describe,preflight)),
 'rule':'Two inverse pairs in weight2/nonplane4; one involution in each allones/plane4/weight6 orbit.',
 'HH_checked':True},indent=2)+'\n')
with (HERE/'profile.inputs.jsonl').open('w') as f:
    for row in samples: f.write(json.dumps(row)+'\n')
with (HERE/'engine_tables.hpp').open('w') as f:
    def arr(name,rows):
        f.write('static const int '+name+'['+str(len(rows))+']['+str(len(rows[0]))+'] = {\n')
        for row in rows: f.write('{'+','.join(map(str,row))+'},\n')
        f.write('};\n')
    arr('KACTION',action); arr('KPROD',kprod); arr('KCOORD',coords)
with (HERE/'inputs.txt').open('w') as f:
    f.write('2001\n'+' '.join(map(str,preflight))+'\n')
    for row in samples: f.write(' '.join(map(str,row['S']))+'\n')

before=cpu()
subprocess.run(['g++','-O3','-std=c++17',str(HERE/'profile.cpp'),'-o',str(HERE/'profile')],check=True)
compile_cpu=cpu()-before
elapsed=cpu()-start
(HERE/'prepare.terminal.json').write_text(json.dumps({'status':'PREPARED','cpu_seconds':elapsed,
 'compile_cpu_seconds':compile_cpu,'profile_candidates_prepared':2000,'preflight_candidates':1,
 'HH_checks':2001,'full_production_started':False},indent=2)+'\n')
print(json.dumps({'counts':counts,'preflight_S':preflight,'prepare_CPU':elapsed,'compile_CPU':compile_cpu},indent=2))
