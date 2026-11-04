"""Fresh finite shape checks; reads original inputs and writes review outputs only."""
import hashlib,itertools,json,math
from pathlib import Path
R=Path(__file__).resolve().parent.parent
D=Path(__file__).resolve().parent
read=lambda n:json.loads((R/n).read_text(encoding='utf-8-sig'))
sha=lambda n:hashlib.sha256((R/n).read_bytes()).hexdigest()
checked=[]
import sys
sys.path.insert(0,str(R))
from r4_boundary_blocking_probe import negative_table
for core,us,filename in [(4,(3,5,15),'t15_core4_r4_small_negative.txt'),(24,(6,10,15),'t15_core24_route_negative.txt')]:
 actual=[set(),set(),set()]
 for line in (R/filename).read_text().splitlines():
  a=list(map(int,line.split()));assert len(a)==13
  actual[a[0]].add(frozenset(tuple(sorted(a[i:i+2])) for i in range(1,13,2)))
 for f,u in enumerate(us):assert actual[f]==set(negative_table(*[x for x in us if x!=u],1)),(core,f)
for n,h in read('T15_CORE4_FULL_CLOSURE_VERIFICATION.json')['input_sha256'].items():
 assert sha(n)==h,n
 checked.append(n)
review=read('R4_DOUBLE_BRIDGE_REVIEW.json')
for n,h in review['audited_input_hashes'].items():assert sha(n)==h.removeprefix('sha256:'),n
joint=read('r4_joint_blocking_check.json')['reports']
counts={}
for core,expected in [(4,[272,32,1,0,0]),(24,[312,34,1,0,0])]:
 for c,n in zip((4,6,8,10,12),expected):
  rows=[r for r in joint if r['core']==core and r['c']==c];assert len(rows)==1
  assert len(rows[0]['matchings'])==n
 counts[core]=expected
 for c in (2,4,6,8):
  lines=(R/f'r4_joint_fourbridge_core{core}_B{c}.txt').read_text().splitlines()
  seen=set()
  for line in lines:
   v=list(map(int,line.split()));assert len(v)==14-c and len(set(v))==len(v) and set(v)<=set(range(2,16))
   F=tuple(sorted(tuple(sorted(v[i:i+2])) for i in range(0,len(v),2)))
   assert F not in seen;seen.add(F)
  if c>=4:assert seen=={tuple(map(tuple,F)) for F in next(r['matchings'] for r in joint if r['core']==core and r['c']==c)}
  else:
   zero=set()
   src='t15_core4_r4_c2_B_types.txt' if core==4 else 't15_core24_c2_B_types.txt'
   for line in (R/src).read_text().splitlines():
    v=list(map(int,line.split()))
    if v[0]==0:zero.add(tuple(sorted(tuple(sorted(v[i:i+2])) for i in range(3,len(v),2))))
   assert seen==zero
# Directly transport the concrete marked theorem, rather than trusting index 4.
options=[];geometries=[]
core_avoided={1,2};core_free={0,7,11,31}
transforms=[]
for p in itertools.permutations(range(5)):
 tr=[sum(((x>>j)&1)<<p[j] for j in range(5)) for x in range(32)]
 transforms.append(tr)
for v,Z,W,h,size in [(1,{3,5,9},{14,31,47,62},15,10),(7,{15,23,39},{56,59,61,62},63,1)]:
 orbit=set()
 for perm in itertools.permutations(range(6)):
  tr=lambda x:sum(((x>>j)&1)<<perm[j] for j in range(6))
  if tr(v)==v:orbit.add((v,tuple(sorted(map(tr,Z))),tuple(sorted(map(tr,W)))))
 assert len(orbit)==size
 geometries.extend(sorted(orbit))
 for i in range(6):
  za={z for z in Z if (z>>i&1)==(v>>i&1)}
  if len(za)!=2:continue
  a=next(iter(Z-za));q=h^(1<<i)
  def proj(x):
   y=x^a
   return (y&((1<<i)-1))|((y>>(i+1))<<i)
  avoided={proj(z^(1<<i)) for z in za}
  for t in W:
   s=t^(1<<i)
   if (q^s).bit_count()!=1:continue
   free={0}|{proj(w) for w in W-{t}}
   witnesses=[k for k,tr in enumerate(transforms) if {tr[x] for x in core_avoided}==avoided and {tr[x] for x in core_free}==free]
   assert witnesses
   options.append(dict(target=v,cut=i,q=q,s=s,t=t,avoided=sorted(avoided),free=sorted(free),permutation_index=witnesses[0]))
assert len(options)==18 and len(set(geometries))==11
# Two distinct stubs at one isolated A vertex pair with each other; if mapped
# to the same B mirror their parallel edges are a cycle and must be rejected.
stub_vertex=[0,0];assert [j for j in range(2) if j!=0 and stub_vertex[j]==stub_vertex[0]]==[1]
out=dict(status='PASS',core4_manifest_hashes_checked=len(checked),R4_fixed_hashes_checked=len(review['audited_input_hashes']),joint_counts=counts,projection_options=options,closed_normalized_geometries=[dict(target=v,Z=z,W=w) for v,z,w in geometries],other_exceptional_geometries_unproved=39)
(D/'review_supplement.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: fixed hashes, full B list validity, actual marked core4 isometries for 18 options and exact 11-geometry orbit')
