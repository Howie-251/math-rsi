"""One actual sample for each of the 192 approved HH color cells, fixed documented seed."""
from pathlib import Path
import json, random, resource, subprocess
HERE=Path(__file__).resolve().parent
DESIGN=HERE.parent/'d8_head_triangles/HEAD_TRIANGLE_Q11_PROFILE_DESIGN.json'
def cpu():
 a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
 return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu();assert not (HERE/'prepare.terminal.json').exists(), 'Do not repeat fixed preparation or compilation'
design=json.loads(DESIGN.read_text());assert design['HH_color_cell_count']==192
Q=11;J=10;A=363;K=110;L=39930
pw=[pow(2,j,Q) for j in range(J)];assert len(set(pw))==J
X=[(x%Q,x//Q%Q,x//(Q*Q)) for x in range(A)];KC=[(k%Q,k//Q) for k in range(K)]
def enc(u,v,w):return u%Q+Q*(v%Q)+Q*Q*(w%3)
ADD=[[enc(u+a,v+b,w+c) for a,b,c in X] for u,v,w in X]
NEG=[enc(-u,-v,-w) for u,v,w in X]
KP=[[(b+pw[2*j%J]*d)%Q+Q*((j+l)%J) for d,l in KC] for b,j in KC]
KI=[(-pw[-2*j%J]*b)%Q+Q*(-j%J) for b,j in KC]
ACT=[[enc(pw[3*j%J]*u+b*pw[j]*v,pw[j]*v,w) for u,v,w in X] for b,j in KC]
def gp(g,h):return ADD[g%A][ACT[g//A][h%A]]+A*KP[g//A][h//A]
def inv(g):
 k=KI[g//A];return NEG[ACT[k][g%A]]+A*k
GI=[inv(g) for g in range(L)]
assert all(gp(g,GI[g])==gp(GI[g],g)==0 for g in range(L))
for k in range(K):
 assert KP[k][KI[k]]==KP[KI[k]][k]==0
 for l in range(K):assert all(ACT[KP[k][l]][x]==ACT[k][ACT[l][x]] for x in range(A))
def colour(g):
 u,v,w=X[g%A];return 2 if v else (1 if u else 0)
pairs=[[],[],[]];iv=[[],[],[]];cross=[[],[],[]]
for g in range(1,L):
 w=X[g%A][2];c=colour(g);assert colour(GI[g])==c
 if w==0:
  if g==GI[g]:iv[c].append(g)
  elif g<GI[g]:pairs[c].append([g,GI[g]])
 elif w==1:cross[c].append(g)
assert list(map(len,pairs))==[54,545,5995]
assert list(map(len,iv))==[1,10,110]
assert list(map(len,cross))==[110,1100,12100]
rng=random.Random(2026102611);samples=[];seen=set();counts={2:0,3:0,4:0}
for cell in design['cells']:
 assert cell['cell_id']==len(samples) and cell['planned_representatives']==1
 ka,kb=rng.randrange(K),rng.randrange(K)
 anchorA=122+A*ka;anchorB=132+A*kb
 extra=[]
 for c in range(3):extra.extend(rng.sample([g for g in cross[c] if g not in (anchorA,anchorB)],cell['extra_cross_colors_after_anchors'][c]))
 chosen_pairs=[];chosen_iv=[]
 # Within each O/A/B color, draw inverse pairs then involutions from ascending pools.
 for c in range(3):
  chosen_pairs.extend(rng.sample(pairs[c],cell['internal_pair_colors_zero_axis_offaxis'][c]))
  chosen_iv.extend(rng.sample(iv[c],cell['internal_involution_colors_zero_axis_offaxis'][c]))
 cross_reps=[anchorA,anchorB,*extra]
 S=sorted([h for g in cross_reps for h in (g,GI[g])]+[h for pair in chosen_pairs for h in pair]+chosen_iv)
 assert len(S)==len(set(S))==11 and 0 not in S and sorted(map(inv,S))==S
 assert [sum(colour(g)==c for g in cross_reps) for c in range(3)]==cell['cross_colors_zero_axis_offaxis']
 assert [sum(colour(pair[0])==c for pair in chosen_pairs) for c in range(3)]==cell['internal_pair_colors_zero_axis_offaxis']
 assert [sum(colour(g)==c for g in chosen_iv) for c in range(3)]==cell['internal_involution_colors_zero_axis_offaxis']
 hh={0,121,242}
 for s in S:hh.update(ACT[k][s%A] for k in range(K))
 assert len(hh)==363
 assert tuple(S) not in seen;seen.add(tuple(S))
 t=cell['cross_inverse_pairs'];counts[t]+=1
 samples.append({'cell_id':cell['cell_id'],'cell':cell,'S':S,'anchor_K_codes':[ka,kb],
  'marked_cross_A_B':[anchorA,anchorB],'extra_cross_w1':extra,'internal_pairs':chosen_pairs,'internal_involutions':chosen_iv,
  'HH_actual_head_targets':len(hh),
  'S_coordinates_u_v_w_b_j':[[*X[g%A],*KC[g//A]] for g in S]})
assert counts=={2:81,3:81,4:30}
with (HERE/'profile.inputs.jsonl').open('w') as f:
 for row in samples:f.write(json.dumps(row)+'\n')
with (HERE/'profile.inputs.txt').open('w') as f:
 f.write('192\n')
 for row in samples:f.write(' '.join(map(str,[row['cell_id'],row['cell']['cross_inverse_pairs'],*row['S']]))+'\n')
(HERE/'generator_lists.json').write_text(json.dumps({'internal_pairs_O_A_B':pairs,'internal_involutions_O_A_B':iv,'cross_w1_O_A_B':cross})+'\n')
meta={'q':11,'r':3,'c':2,'degree':12,'n':43923,'edges':263538,
 'layer_sizes':[39930,3630,363],'roots':[0,39930,43560],
 'group_encoding':'u+11*v+121*w+363*(b+11*j)',
 'group_product':'((u,v,w)+U_bD_j(u1,v1,w1), b+2^(2j)*d, j+l), mod11/mod3/mod10',
 'K_product':'(b,j)(d,l)=(b+2^(2j)*d mod11,j+l mod10)',
 'K_action':'(2^(3j)*u+b*2^j*v,2^j*v,w)',
 'group_inverse':'(-k^-1(x),k^-1), with K inverse=(-2^(-2j)*b,-j)',
 'leaf_parent':'39930+x+363*j','block_parent':'43560+x','head_triangles':121,
 'head_triangle_edges':363,'field_arithmetic':'F11 modular addition and multiplication, never XOR',
 'seed':2026102611,'PRNG':'Python random.Random / MT19937',
 'sampling_order':'design cell_id order; two K anchors; O/A/B extras; then in each O/A/B color internal inverse pairs followed by involutions',
 'scope':'Exactly one representative for each of 192 approved HH color cells, not a complete family enumeration',
 'design_source':'../d8_head_triangles/HEAD_TRIANGLE_Q11_PROFILE_DESIGN.md',
 'actual_samples':192,'actual_counts_by_t':counts,'all_actual_S_saved_and_distinct':True,
 'internal_pair_counts_O_A_B':list(map(len,pairs)),'internal_involution_counts_O_A_B':list(map(len,iv)),
 'cross_counts_O_A_B':list(map(len,cross)),
 'all_element_inverse_checks':39930,'all_K_action_composition_checks':K*K*A,
 'all_candidates_actual_HH_check':True,'complete_three_root_BFS_for_every_sample':True,
 'original_BB_masks':10,'original_BB_targets_per_mask':363,
 'quotient_BB_targets_per_mask':33,'BB_diagnostic_only_no_filtering':True,
 'safe_marked_normalization_is_not_uniform_unmarked_sampling':True,
 'CPU_limit_seconds':60,'worker_count':1,'independent_final_check_parent_owned':True}
(HERE/'profile.metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
(HERE/'structure_tables.json').write_text(json.dumps({'A_coordinates':X,'K_coordinates':KC,'K_product':KP,'K_inverse':KI,'K_action':ACT,'A_negative':NEG})+'\n')
before=cpu();subprocess.run(['g++','-O3','-std=c++17',str(HERE/'profile.cpp'),'-o',str(HERE/'profile')],check=True)
out={'status':'PREPARED','CPU_seconds':cpu()-start,'compile_CPU_seconds':cpu()-before,
 'actual_samples':192,'actual_counts_by_t':counts,'no_graph_or_BFS_yet':True}
(HERE/'prepare.terminal.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
