"""Save two fixed stratified samples using the source's actual ordered small-cell tables."""
from pathlib import Path
import json, random, resource, subprocess
HERE=Path(__file__).resolve().parent
BASE=HERE.parent
def cpu():
 a=resource.getrusage(resource.RUSAGE_SELF);b=resource.getrusage(resource.RUSAGE_CHILDREN)
 return a.ru_utime+a.ru_stime+b.ru_utime+b.ru_stime
start=cpu()
assert (HERE/'STRUCTURE.md').exists(), 'Read completed source structure before running this preparation'
assert not (HERE/'profile.prepare.json').exists(), 'No repeated sampling or compilation'
source=json.loads((HERE/'STRUCTURE.json').read_text())
completed=[]
for p,ns,seed,name in [(31,100,2026102631,'d7_head_triangles_c31'),(43,50,2026102643,'d8_head_triangles_c43')]:
 case=next(c for c in source['cases'] if c['p']==p)
 folder=BASE/name;folder.mkdir(exist_ok=True)
 K=p-1;A=3*p;L=A*K;D=case['degree'];M=case['K_over_H_index'];P=case['primitive_powers']
 assert P==[pow(3,i,p) for i in range(K)] and len(set(P))==K
 def inv(g):
  x=g%p;w=g//p%3;i=g//A
  return (-P[-i%K]*x)%p+p*(-w%3)+A*(-i%K)
 def gp(g,h):
  return (g%p+P[g//A]*(h%p))%p+p*((g//p%3+h//p%3)%3)+A*((g//A+h//A)%K)
 GI=[inv(g) for g in range(L)]
 assert all(gp(g,GI[g])==gp(GI[g],g)==0 for g in range(L))
 iv=[[],[]];pairs=[[],[]];cross=[[],[]]
 for g in range(1,L):
  x,w=g%p,g//p%3
  if w==0:
   if GI[g]==g:iv[bool(x)].append(g)
   elif g<GI[g]:pairs[bool(x)].append([g,GI[g]])
  elif w==1:cross[bool(x)].append(g)
 assert list(map(len,iv))==[case['G0_zero_field_involutions'],case['G0_nonzero_field_involutions']]
 assert list(map(len,pairs))==[case['G0_zero_field_inverse_pairs'],case['G0_nonzero_field_inverse_pairs']]
 assert list(map(len,cross))==[case['cross_zero_field_pairs'],case['cross_nonzero_field_pairs']]
 rng=random.Random(seed);seen=set();samples=[];strata=[];rejections=0
 for idx,cell in enumerate(case['profile_strata']):
  nz=cell['internal_zero_field_involutions'];nn=cell['internal_involutions']-nz
  pz=cell['internal_zero_field_pairs'];pn=cell['internal_inverse_pairs']-pz
  cz=cell['additional_cross_zero_field_pairs'];cn=cell['additional_cross_nonzero_field_pairs']
  for local in range(ns):
   while True:
    anchor_i=rng.randrange(K);anchor=1+p+A*anchor_i
    extras=rng.sample(cross[0],cz)+rng.sample([g for g in cross[1] if g!=anchor],cn)
    invols=rng.sample(iv[0],nz)+rng.sample(iv[1],nn)
    ips=rng.sample(pairs[0],pz)+rng.sample(pairs[1],pn)
    S=sorted([anchor,GI[anchor],*[h for g in extras for h in (g,GI[g])],*invols,*[g for pair in ips for g in pair]])
    assert len(S)==D-1 and len(set(S))==D-1 and 0 not in S and set(map(inv,S))==set(S)
    assert any(g%p and g//p%3==0 for g in S) and any(g%p and g//p%3 for g in S)
    key=tuple(S)
    if key not in seen:seen.add(key);break
    rejections+=1
   samples.append({'cursor':len(samples),'stratum':idx,'stratum_cursor':local,'S':S,
                   'marked_cross_anchor':anchor,'marked_cross_anchor_K_index':anchor_i,
                   'additional_w1_cross_representatives':extras,'internal_involutions':invols,'internal_inverse_pairs':ips})
  strata.append({'index':idx,'sampling_cell':cell,'planned_samples':ns})
 assert len(samples)==case['profile_strata_count']*ns
 with (folder/'profile.inputs.jsonl').open('w') as f:
  for row in samples:f.write(json.dumps(row)+'\n')
 with (folder/'profile.inputs.txt').open('w') as f:
  f.write(' '.join(map(str,[p,K,M,D,len(strata),len(samples)]))+'\n')
  for s in samples:f.write(' '.join(map(str,[s['stratum'],s['stratum_cursor'],*s['S']]))+'\n')
 metadata={'parameter':{'p':p,'r':3,'K':K,'H_order':K//M,'block_index_count':M},
  'source_structure':'../d8_head_triangles_c43/STRUCTURE.md',
  'source_small_cell_table':'../d8_head_triangles_c43/STRUCTURE.json cases[p].profile_strata',
  'seed':seed,'PRNG':'Python random.Random / MT19937','sample_count':len(samples),'strata':strata,
  'stratum_order':'exact source JSON order','every_saved_S_is_distinct':True,'duplicate_proposals_rejected':rejections,
  'scope':'fixed stratified sample only; not complete family enumeration or uniform graph sampling',
  'marked_nonzero_w1_cross_anchor':'x=1, K index drawn from all 0..p-2',
  't_greater_than_one_nonuniform_anchor_distribution_acknowledged':True,
  'all_internal_and_cross_field_nonzero_requirements_checked':True,
  'three_root_weights':case['layer_sizes'],'three_roots':[0,case['layer_sizes'][0],sum(case['layer_sizes'][:2])],
  'layer_sizes':case['layer_sizes'],'n':case['n'],'degree':D,'edges':case['edges'],
  'group_encoding':'x+p*w+3*p*i','group_product':'(x+r^i*y,w+v,i+j) mod p,3,p-1',
  'group_inverse':'(-r^-i*x,-w,-i)','leaf_parent':'L+(g mod3p)+3p*((g div3p) modm)',
  'block_parent':'L+B+(block-L) mod3p','head_edges':'For every x join w=0,1,2 in a K3',
  'BB_orbit_bits':case['BB_compressed_bits_per_quotient_layer'],'BB_missing_multiple':K//M,
  'BB_diagnostic_only_no_filtering':True,'CPU_limit_shared_across_two_parameters':60,'worker_count':1,
  'independent_final_only_parent_owned':True}
 (folder/'profile.metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
 (folder/'generator_lists.json').write_text(json.dumps({'involutions_zero_nonzero':iv,'pairs_zero_nonzero':pairs,'cross_w1_zero_nonzero':cross},indent=2)+'\n')
 completed.append({'p':p,'directory':name,'samples':len(samples),'strata':len(strata),'seed':seed})
before=cpu();subprocess.run(['g++','-O3','-std=c++17',str(HERE/'profile.cpp'),'-o',str(HERE/'profile')],check=True)
compile_cpu=cpu()-before
out={'status':'TWO_PROFILES_PREPARED','CPU_seconds':cpu()-start,'compile_CPU_seconds':compile_cpu,'parameters':completed,
     'total_planned_samples':2600,'single_generic_binary':True,'production_full_enumeration_authorized':False}
(HERE/'profile.prepare.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
