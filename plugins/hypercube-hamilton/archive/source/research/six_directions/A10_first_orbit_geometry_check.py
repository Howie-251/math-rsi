"""Exact bit geometry and four-candidate choice coverage for one A10 orbit.
Only ten abstract partial matchings on four labels are checked; no Q5
matching instances or Hamilton cycles are enumerated.
"""
import itertools,json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
V=set(range(32));Z={3,5,6,15,23};W={8,16,25,26};major={0}|Z;H=major|W;covered=V-H
assert len(major)==6 and len(W)==4 and all(x.bit_count()%2==0 for x in major) and all(x.bit_count()%2==1 for x in W)
assert all((z^w).bit_count()!=1 for z in Z for w in W)
images=set()
for p in itertools.permutations(range(5)):
 tr=lambda x:sum(((x>>i)&1)<<p[i] for i in range(5))
 images.add((tuple(sorted(map(tr,Z))),tuple(sorted(map(tr,W)))))
assert len(images)==30
# Exhaust all possible restrictions of the arbitrary matching to four candidates.
abstract=[frozenset()]
edges=list(itertools.combinations(range(4),2))
abstract += [frozenset([e]) for e in edges]
abstract += [frozenset([e,f]) for e,f in itertools.combinations(edges,2) if not set(e)&set(f)]
assert len(abstract)==10
cover_rows=[]
for fixed in abstract:
 good=[set(pair) for pair in edges if tuple(sorted(set(range(4))-set(pair))) not in fixed]
 assert len(good)>=4 and set().union(*good)==set(range(4))
 assert all(sum(x in pair for pair in good)>=2 for x in range(4))
 cover_rows.append(dict(fixed_edges=sorted(fixed),nonfixed_choices=len(good),minimum_selected_occurrences=min(sum(x in pair for pair in good) for x in range(4))))
rows=[]
for bit,a,M,C in [(8,15,{11,13,14,31},{9,10,12,24,27,28,29,30}),(16,23,{19,21,22,31},{17,18,20,24,27,28,29,30})]:
 A={x for x in V if not x&bit};B=V-A
 assert len(major&A)==5 and len(W&A)==1 and major&B=={a} and len(W&B)==3
 assert {x^bit for x in (major&A)-{0}}==M
 assert M<=covered&B and M=={x for x in B if (x^a).bit_count()==1}
 assert ((covered&B)-M)==C and len(C)==8
 assert (16-len(H&A))%2==0 # crossing count is even.
 choices=[]
 for pair in itertools.combinations(sorted(M),2):
  selected=set(pair);other=M-selected
  assert len(other)==2
  assert (len(major&A)-len(selected))-len(W&A)==2
  assert len(W&B)+len(selected)==5
  choices.append(dict(selected_bridges=sorted(selected),selected_A_holes=sorted(x^bit for x in selected),T15_obstruction_edge=sorted(other)))
 rows.append(dict(cut_bit=bit,A_majority_holes=sorted(major&A),A_minority_holes=sorted(W&A),singleton_majority_B=a,candidates=sorted(M),closed_outside=sorted(C),choices=choices))
I=set(rows[0]['closed_outside'])&set(rows[1]['closed_outside'])
assert I=={24,27,28,29,30} and len(I)%2==1 and I<=covered
out=dict(status='PASS',scope='One marked 4:6-hole Q5 orbit, exact bit geometry and four-candidate choice coverage; analytic closure is in the proof document',forbidden=0,Z=sorted(Z),W=sorted(W),orbit_size=len(images),original_Q5_matching_instances_enumerated=0,abstract_four_candidate_matchings_checked=len(abstract),candidate_choice_cover=cover_rows,cuts=rows,odd_closed_intersection=sorted(I),fresh_proof_checker_review_pending=True,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(R/'A10_first_orbit_geometry_check.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['candidate_choice_cover','cuts']}))

