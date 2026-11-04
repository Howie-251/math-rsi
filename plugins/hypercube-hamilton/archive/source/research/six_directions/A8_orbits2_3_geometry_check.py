"""Bit geometry only: two analytic A8 closures, no matching enumeration."""
import itertools,json,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
V=set(range(32));W={25,26,28};I={24,27,29,30};D8={8,9,10,12};D16={16,17,18,20};C8=I|D8;C16=I|D16;U=I|D8|D16
configs=[dict(Z={3,5,6,15},orbit=20,delta0bits=[1,2,4],cuts=[(8,2,{11,13,14},15,{11,13,14,31}),(16,3,{19,21,22,31},23,{19,21,22,23,31})]),dict(Z={3,5,15,23},orbit=30,delta0bits=[2,4],cuts=[(8,2,{11,13,31},15,{11,13,14,31}),(16,2,{19,21,31},23,{19,21,22,31})])]
rows=[]
for config in configs:
 Z=config['Z'];H={0}|Z|W;covered=V-H;major={0}|Z
 assert all((z^w).bit_count()!=1 for z in Z for w in W)
 orbit=set()
 for p in itertools.permutations(range(5)):
  tr=lambda x:sum(((x>>i)&1)<<p[i] for i in range(5))
  orbit.add((tuple(sorted(map(tr,Z))),tuple(sorted(map(tr,W)))))
 assert len(orbit)==config['orbit']
 cutrows=[]
 for bit,k,M,a,S in config['cuts']:
  A={x for x in V if not x&bit};B=V-A
  assert M<=covered&B and S<=covered&B and len(S-M)==1
  minorityA=len(W&A);majorityA=len(major&A)
  assert majorityA-k-minorityA==2 and all((y^bit) in Z&A for y in M)
  if k==2:assert {x for x in major&B}=={a} and {x for x in B if (x^a).bit_count()==1}==S
  if k==3:assert major&B==set() and {x for x in B if (x^a).bit_count()==1}==M and a in S-M
  choices=list(itertools.combinations(sorted(M),k));ob=[]
  for Ytuple in choices:
   Y=set(Ytuple)
   if k==2:pair=tuple(sorted(S-Y))
   else:pair=tuple(sorted({a}|(M-Y)))
   assert len(pair)==2;ob.append(pair)
  common=set(ob[0])
  for edge in ob:common&=set(edge)
  assert len(common)==1 # Thus at most one obstruction edge can belong to F.
  for fixed in [None]+list(range(len(choices))):
   usable=[set(Y) for j,Y in enumerate(choices) if j!=fixed]
   assert set().union(*usable)==M
  C=(covered&B)-S;assert C==(C8 if bit==8 else C16)
  assert (len(S)-(16-len(H&A))%2)%2==0 # |S|-c even for every possible c.
  cutrows.append(dict(bit=bit,bridges_per_choice=k,candidates=sorted(M),special=sorted(S),obstruction_edges=ob,closed_outside=sorted(C),A_hole_counts=[minorityA,majorityA]))
 assert C8&C16==I and C8-C16==D8 and C16-C8==D16
 rem=covered-U;assert len(rem)==12 and 1 in rem
 delta0=[]
 for bit in config['delta0bits']:
  A={x for x in V if not x&bit};B=V-A
  assert len(major&A)==len(W&A)==2
  Y={x^bit for x in W&A};singleton=next(iter(W&B));N={x for x in B if (x^singleton).bit_count()==1};assert Y<=N
  pair=N-Y;assert len(pair)==2 and len(pair&D8)==len(pair&D16)==1
  assert N<=U
  delta0.append(dict(bit=bit,bridge_vertices=sorted(Y),singleton=singleton,special=sorted(N),obstruction_edge=sorted(pair)))
 lowmask=sum(config['delta0bits']);same=[x for x in rem if x&lowmask==1&lowmask];assert same==[1]
 rows.append(dict(Z=sorted(Z),W=sorted(W),orbit_size=len(orbit),cuts=cutrows,delta0=delta0,remaining_closed_set=sorted(rem),preserved_bitmask=lowmask,vertex1_possible_mates=[]))
output=dict(status='PASS',scope='Exact bit geometry, bridge choice cover, obstruction edges, set identities and isolated residual parity-class vertex; analytic matching argument in separate proof',rows=rows,matching_instances_enumerated=0,fresh_proof_checker_review_pending=True,checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
(R/'A8_orbits2_3_geometry_check.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps({k:v for k,v in output.items() if k!='rows'}))
