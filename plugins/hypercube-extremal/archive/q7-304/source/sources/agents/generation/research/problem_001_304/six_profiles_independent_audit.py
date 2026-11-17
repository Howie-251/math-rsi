"""Pure-Python independent audit; never imports or executes the SAT model."""
import itertools as it,json,collections,math,hashlib
from pathlib import Path
H=Path(__file__).resolve().parent
triples=list(it.combinations(range(6),3))
# Full 128-assignment truth table, including the graph degree constraints.
for bits in it.product((False,True),repeat=6):
 for z in (False,True):
  lower=all(any(bits[i] for i in C) for C in it.combinations(range(6),4))
  upper=not all(bits)
  forward=all(not z or any(not bits[i] for i in C) for C in it.combinations(range(6),4))
  reverse=all(z or any(bits[i] for i in C) for C in triples)
  assert (lower and upper and forward and reverse)==(3<=sum(bits)<=5 and z==(sum(bits)==3))
# Reconstruct the action of the complete even-parity-preserving stabilizer
# of the first face (free mask7, base0): S3 x S3 and four even translations.
orbits=json.loads((H/'two_hole_orbits.json').read_text())
faces={(sum(1<<i for i in T),b) for T in triples for b in range(64) if not b&sum(1<<i for i in T)}
perms=[p+q for p in it.permutations(range(3)) for q in it.permutations(range(3,6))]
def perm(x,p):return sum(((x>>i)&1)<<p[i] for i in range(6))
translations=[t for t in range(8) if t.bit_count()%2==0]
seen=set()
for o in orbits:
 mask,base=o['representative']
 orbit={(perm(mask,p),(perm(base,p)^t)&~perm(mask,p)) for p in perms for t in translations}
 assert orbit==set(map(tuple,o['members']))
 assert len(orbit)==o['size'] and not seen&orbit
 seen|=orbit
assert seen==faces-{(7,0)} and len(orbits)==10
profiles=[]
for m,p in [(131,0),(130,0),(129,0),(129,1),(128,0),(128,1)]:
 hist=[]
 for defectp in [0,p]:
  n3=266-2*m-defectp;n5=m-128+n3;n4=32-n3-n5
  assert 3*n3+4*n4+5*n5==m
  assert n3+4*n4+10*n5==158-3*defectp
  hist.append({3:n3,4:n4,5:n5})
 profiles.append({'m':m,'other_p':p,'degree_histograms':hist,'candidate_value':2*(hist[0][3]+hist[1][3])+7*m})
statuses=[];witnesses=[]
for path in sorted(H.glob('six_profiles_sat_m*_p*_case*.json')):
 try:r=json.loads(path.read_text())
 except json.JSONDecodeError:continue # producer may be in the middle of a write
 if 'answer' not in r:continue # Per-certificate checker reports share this glob.
 statuses.append({'file':path.name,'answer':r['answer']})
 if r['answer'] is not True:continue
 E={tuple(sorted(e)) for e in r['edges']}
 assert len(E)==len(r['edges'])==r['m']
 assert all(0<=u<v<64 and (u^v).bit_count()==1 for u,v in E)
 adj=[set() for _ in range(64)]
 for u,v in E:adj[u].add(v);adj[v].add(u)
 degrees=list(map(len,adj));assert min(degrees)>=3 and max(degrees)<=5
 edge=lambda v,i:tuple(sorted((v,v^(1<<i))))
 sq=[];empty=opposite=0
 for i,j in it.combinations(range(6),2):
  for b in range(64):
   if b&((1<<i)|(1<<j)):continue
   selected={edge(b,i),edge(b,j),edge(b^(1<<i),j),edge(b^(1<<j),i)}&E
   assert len(selected)<=3
   if not selected:empty+=1
   if len(selected)==2 and len(set().union(*map(set,selected)))==4:opposite+=1
 totals=[0,0];holes=[[],[]]
 for mask,b in sorted(faces):
  T=[i for i in range(6) if mask>>i&1]
  for parity in [0,1]:
   stars=[v for v in range(64) if v.bit_count()%2==parity and v&~mask==b and all(edge(v,i) in E for i in T)]
   assert len(stars)<=1
   totals[parity]+=len(stars)
   if not stars:holes[parity].append([mask,b])
 assert set(map(tuple,holes[0]))=={(7,0),tuple(orbits[r['case']]['representative'])}
 assert totals==[158,158-3*r['other_p']]
 n3=[sum(degrees[v]==3 for v in range(64) if v.bit_count()%2==p) for p in [0,1]]
 assert n3==[266-2*r['m'],266-2*r['m']-r['other_p']]
 D=empty-opposite;assert D==3*r['m']-400+sum(n3)
 witnesses.append({'file':path.name,'m':len(E),'n3':n3,'stars':totals,'empty':empty,'opposite':opposite,'D':D,'delta':132-len(E),'candidate_value':2*sum(n3)+7*len(E),'candidate_violated':2*D>132-len(E),'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'audit_passed':True})
result={'odd3_truth_table_assignments':128,'odd3_iff_correct':True,'orbit_count':10,'orbit_sizes':[o['size'] for o in orbits],'orbit_partition_verified':True,'profiles':profiles,'available_results':statuses,'audited_SAT_witnesses':witnesses,'scope':'Encoding and witness audit only; UNKNOWN/UNSAT outputs are not treated as certificates.'}
(H/'six_profiles_independent_audit.json').write_text(json.dumps(result,indent=2));print(json.dumps(result))
