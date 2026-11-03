"""Fresh r1 group tables, actual inverse lists, one sample, and complete quotient-key filter."""
from pathlib import Path
from itertools import combinations
import json
import resource
import subprocess
HERE=Path(__file__).resolve().parent
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
KP=[[(b+d)%7+7*((j+l)%6) for d,l in K] for b,j in K]
KI=[(-b)%7+7*(-j%6) for b,j in K]
ACTION=[[encode(P3[j]*(u+b*v),P3[j]*v,w) for u,v,w in X] for b,j in K]
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

OLD=HERE.parent/'d8_head_triangles'
assert not (HERE/'prepare.terminal.json').exists(), 'No repeated preparation or compilation'
GI=[inv(g) for g in range(6174)]
assert all(len(set(s))==3 and 0 not in s and set(map(inv,s))==set(s) for rows in internal for s in rows)
structure={'parameter':{'q':7,'r':1,'c':3},'A':'F7^2 x C3',
 'A_encoding':'u+7*v+49*w','A_coordinates':X,'A_negative':NEG,
 'A_addition':'component addition modulo 7,7,3; not XOR',
 'K_encoding':'b+7*j','K_coordinates':K,
 'K_multiplication':'(b,j)*(d,l)=(b+d mod7,j+l mod6)',
 'K_inverse':'(-b mod7,-j mod6)',
 'K_action':'(u,v,w)->(3^j*(u+b*v) mod7,3^j*v mod7,w)',
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
 'cross_normalization':'w=1 representatives have field vectors (1,0) and (0,1); both K codes unrestricted.',
 'old_r5_internal_indices_reused':False,'HH_complete_scope':28894320}
(HERE/'structure.json').write_text(json.dumps(structure,indent=2)+'\n')
(HERE/'internal_generator_lists.json').write_text(json.dumps({'involutions':invol,'inverse_pairs':pairs},indent=2)+'\n')
(HERE/'internal_options.json').write_text(json.dumps(internal)+'\n')
with (HERE/'engine_tables.hpp').open('w') as f:
    def arr(name,rows):
        f.write('static const int '+name+'['+str(len(rows))+']['+str(len(rows[0]))+']={\n')
        for row in rows:f.write('{'+','.join(map(str,row))+'},\n')
        f.write('};\n')
    arr('KACTION',ACTION);arr('KPROD',KP);arr('KCOORD',K);arr('AADD',ADD)
(HERE/'production_extra.hpp').write_text('static const int GINV[6174]={'+','.join(map(str,GI))+'};\n')
allowed=json.loads((OLD/'QUOTIENT_BB_ALLOWED.json').read_text())
keys={tuple(x) for x in allowed['allowed_unique_projected_S']};assert len(keys)==16
expected=json.loads((OLD/'HEAD_TRIANGLE_PARAMETER_EXTENSION.json').read_text())['q7_r1']
def project(g):
    x=g%147;return x//7%7+7*(x//49)+21*(g//147//7)
ca=[[project(50+147*7*j),project(GI[50+147*7*j])] for j in range(6)]
cb=[[project(56+147*7*j),project(GI[56+147*7*j])] for j in range(6)]
actual=[];branches=[];offset=0;blocks=0
for branch,options in enumerate(internal):
    passed=0
    for idx,S0 in enumerate(options):
        sp=[project(s) for s in S0]
        for ja in range(6):
            for jb in range(6):
                blocks+=1
                canonical=tuple(sorted(set(ca[ja]+cb[jb]+sp)))
                if canonical not in keys:continue
                scope_base=offset+((idx*6+ja)*6+jb)*49
                actual.append({'branch':branch,'internal_index':idx,'cross_a_index':ja,'cross_b_index':jb,
                               'original_scope_base':scope_base,'internal_S':S0})
                passed+=1
    raw=len(options)*36*49
    row={'branch':branch,'internal_options':len(options),'full_normalized_inputs':raw,
         'quotient_blocks':len(options)*36,'passing_quotient_blocks':passed,
         'original_BB_inputs':passed*49,'quotient_rejected_original_inputs':raw-passed*49,
         'original_cursor_start':offset,'original_cursor_end':offset+raw}
    assert passed==expected['branches'][branch]['passing_projection_keys']
    assert len(options)==expected['branches'][branch]['actual_internal_options']
    branches.append(row);offset+=raw
assert blocks==589680 and len(actual)==4704 and offset==28894320
assert len(actual)*49==expected['passing_full_normalized_inputs']==230496
assert [z['original_BB_inputs'] for z in branches]==[28812,86436,0,115248,0]
with (HERE/'production.selected_keys.jsonl').open('w') as f:
    for row in actual:f.write(json.dumps(row)+'\n')
with (HERE/'production.inputs.txt').open('w') as f:
    f.write(str(len(actual))+'\n')
    for row in actual:f.write(' '.join(map(str,[row['branch'],row['internal_index'],row['cross_a_index'],row['cross_b_index'],row['original_scope_base'],*row['internal_S']]))+'\n')
meta={'parameter':{'q':7,'r':1,'c':3},'full_normalized_scope':offset,
 'actual_internal_sets':sum(map(len,internal)),'completed_projected_blocks':blocks,
 'allowed_unique_projected_S':16,'passing_projected_blocks':4704,'original_BB_inputs':230496,
 'quotient_rejected_original_inputs':offset-230496,'branches':branches,
 'counts_match_independent_r1_extension':True,'old_r5_internal_indices_reused':False,
 'allowed_quotient_sets_source':'../d8_head_triangles/QUOTIENT_BB_ALLOWED.json',
 'scope_proof':'../d8_head_triangles/HEAD_TRIANGLE_PARAMETER_EXTENSION.md',
 'projected_key':'sorted distinct Q codes; Q code=v+7*w+21*j',
 'no_generation_by_24_overlapping_pattern_records':True,
 'order':'branch, new r1 internal option, ja, jb; accepted blocks expand ba then bb',
 'filtered_cursor_start':0,'full_graph_BFS_population':'original BB survivors or one minimum-BB fallback',
 'preflight_is_not_enumeration_prefix':True,'worker_count':1,'cumulative_CPU_limit_seconds':60,
 'independent_math_CPU_accounted_separately':True}
(HERE/'production.metadata.json').write_text(json.dumps(meta,indent=2)+'\n')
# One deterministic, quotient-allowed sample using the new inverse table.
a,b,t,c=1079,5348,2396,3088
S=[a,GI[a],b,GI[b],t,GI[t],c]
assert len(set(S))==7 and 0 not in S and set(map(inv,S))==set(S)
assert tuple(sorted(set(map(project,S)))) in keys
idx=next(i for i,s in enumerate(internal[1]) if set(s)==set(S[4:]))
ki=next(i for i,k in enumerate(actual) if (k['branch'],k['internal_index'],k['cross_a_index'],k['cross_b_index'])==(1,idx,1,5))
k=actual[ki];ba,bb=0,1
HH={0,49,98}
for s in S:HH.update(ACTION[k0][s%147] for k0 in range(42))
assert len(HH)==147
(HERE/'preflight.inputs.txt').write_text(' '.join(map(str,S))+'\n'+' '.join(map(str,[1,idx,1,5,k['original_scope_base'],ki,ba,bb,49*ki+7*ba+bb]))+'\n')
(HERE/'preflight.parameters.json').write_text(json.dumps({'S':S,'generators':[{'code':g,'u_v_w':X[g%147],'b_j':K[g//147]} for g in S],
 'sample_rule':'fixed cross K=(0,1),(1,5), internal pair (2,6,0;2,2) and inverse, involution (1,0,0;0,3)',
 'new_r1_internal_index':idx,'passing_key_index':ki,'actual_HH_covered_heads':147,
 'sample_is_not_prefix':True},indent=2)+'\n')
before=cpu();subprocess.run(['g++','-O3','-std=c++17',str(HERE/'production.cpp'),'-o',str(HERE/'production')],check=True)
compile_cpu=cpu()-before
subprocess.run([str(HERE/'production'),'preflight','2',str(HERE)],check=True)
check=json.loads((HERE/'preflight.check.json').read_text())
assert check['all_BB_targets_match_actual_BFS'] and check['BB_targets_checked']==882
out={'status':'PREPARED_AND_PREFLIGHT_MATCHED','cpu_seconds':cpu()-start,
 'compile_cpu_seconds':compile_cpu,'preflight_cpu_seconds':check['cpu_seconds'],
 'actual_r1_group_and_inverse_rebuilt':True,'old_r5_internal_indices_reused':False,
 'original_scope':28894320,'projection_keys_checked':589680,'allowed_keys':4704,
 'original_BB_inputs':230496,'branch_counts_match_independent_r1_extension':True,
 'full_graphs_expanded':1,'complete_representative_roots':3}
(HERE/'prepare.terminal.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2));print(json.dumps({'preflight_S':S}))
