"""Exact geometry and independent Burnside counts; no cycle search."""
import itertools,json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
V=set(range(32));Z={3,5,6,15,23};W={8,25,26,28};H={0}|Z|W;covered=V-H
C={16,17,18,20,24,27,29,30};D=covered-C
assert len(C)==8 and len(D)==14
images=set();stabilizer=[]
for p in itertools.permutations(range(5)):
 t=[sum(((x>>i)&1)<<p[i] for i in range(5)) for x in range(32)]
 image=(tuple(sorted(t[x] for x in Z)),tuple(sorted(t[x] for x in W)));images.add(image)
 if image==(tuple(sorted(Z)),tuple(sorted(W))):stabilizer.append((p,t))
assert len(images)==20 and len(stabilizer)==6
assert all(set(t[x] for x in C)==C and set(t[x] for x in D)==D for p,t in stabilizer)
A={x for x in V if not x&16};B=V-A;M={19,21,22,31}
assert len(({0}|Z)&A)==5 and W&A=={8} and ({0}|Z)&B=={23} and len(W&B)==3
assert M=={x^16 for x in Z&A}=={x for x in B if (x^23).bit_count()==1}
assert M<=covered and (covered&B)-M==C
# Prove all non-16 fixed hole-to-mirror face-circle templates are unusable.
traps=[]
for bit in [1,2,4,8]:
 A={x for x in V if not x&bit};B=V-A
 if bit==8:
  candidates={x^bit for x in Z&A};a=next(iter(({0}|Z)&B));selected=list(itertools.combinations(sorted(candidates),3))
 else:
  selected=[tuple(sorted(x^bit for x in W&A))];a=next(iter(W&B))
 for choice in selected:
  N={x for x in B if (x^a).bit_count()==1};assert len(N-set(choice))==1 and a in H
 traps.append(dict(cut_bit=bit,singleton_free_hole=a,selected_avoided_choices=selected,remaining_short_neighbors_per_choice=1))
def pm(v):
 if not v:yield ();return
 for j in range(1,len(v)):
  for F in pm(v[1:j]+v[j+1:]):yield tuple(sorted(((v[0],v[j]),)+F))
def tr(F,t):return tuple(sorted(tuple(sorted((t[a],t[b]))) for a,b in F))
cm=list(pm(tuple(sorted(C))));dm=list(pm(tuple(sorted(D))));assert len(cm)==105 and len(dm)==135135
burn=[]
for p,t in stabilizer:
 fc=sum(tr(F,t)==F for F in cm);fd=sum(tr(F,t)==F for F in dm)
 burn.append(dict(coordinate_permutation=p,C_fixed=fc,D_fixed=fd,full_fixed=fc*fd))
canonical=sum(row['full_fixed'] for row in burn)//6;assert canonical==2366577
corbits={min(tr(F,t) for p,t in stabilizer) for F in cm};assert len(corbits)==23
counts=json.loads((R/'A10_ORBIT2_canonical_counts.json').read_text());assert counts['canonical_records']==canonical and counts['weighted_matching_cover']==105*135135
binary=R/'A10_ORBIT2_canonical_inputs.bin';assert binary.stat().st_size==canonical*22
out=dict(status='PASS_GEOMETRY_AND_DOMAIN_COUNTS',scope='One A10 marked orbit of size20; reduction to canonical finite inputs; no cycle claim',Z=sorted(Z),W=sorted(W),C=sorted(C),D=sorted(D),orbit_size=len(images),stabilizer_size=6,closed_C_matchings=105,other_D_matchings=135135,full_residual_family=105*135135,C_orbits=len(corbits),canonical_matching_representatives=canonical,record_bytes=22,binary_bytes=binary.stat().st_size,binary_sha256=hashlib.sha256(binary.read_bytes()).hexdigest(),burnside=burn,unusable_fixed_templates=traps,full_orbit_proved=False,fresh_semantic_review_pending=True)
(R/'A10_ORBIT2_geometry_counts_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['burnside','unusable_fixed_templates']}))
