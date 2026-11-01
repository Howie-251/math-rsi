"""Independent inclusive-pair Mobius domain and original35-index injection certificates; fixed old menu only."""
from pathlib import Path
from itertools import product,permutations,combinations
from collections import Counter,defaultdict
from fractions import Fraction
import json,time,sys
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
st=time.process_time();domain=json.loads((P/'DOMAIN.json').read_text());result=json.loads((P/'RESULT.json').read_text());assert result['status']=='COMPLETE_FIXED_MENU'
# Independently generate actual spectra, not import the scalar spectrum list.
def parts(n,maximum):
 if n==0:yield ();return
 for k in range(min(n,maximum),0,-1):
  for tail in parts(n-k,k):yield (k,)+tail
spectra=[];quads=set()
for e in range(7):
 for part in parts(e,e):
  if len(part)>7-e:continue
  ds=[8]*(14+e)+[9]*(7-e-len(part))+[9+j for j in part]
  assert len(ds)==21 and sum(ds)==175;spectra.append(ds)
  # A degree-count recursion gives all4 point multisets without indexed21choose4.
  counts=Counter(ds);types=sorted(counts)
  for picks in product(range(5),repeat=len(types)):
   if sum(picks)==4 and all(n<=counts[d] for d,n in zip(types,picks)):quads.add(tuple(d for d,n in zip(types,picks) for _ in range(n)))
new={q for q in quads if max(q)>13 or sum(max(d-9,0) for d in q)>4}
assert len(spectra)==15 and len(quads)==38 and new=={tuple(z['quad_degrees']) for z in domain['new_degree_support']}
ordered={p for q in new for p in permutations(q)};cross=(5,6,9,10);triples=(7,11,13,14);keys=set()
for ds in ordered:
 for tri in (0,*triples):
  for cv in product(range(2,5),repeat=4):
   t=sum(cv)-2*int(bool(tri))
   if not 14<=t<=16:continue
   for A,B in product(range(1,5),repeat=2):
    inc={3:A,12:B,**dict(zip(cross,cv))};ns=[0]*16
    if tri:ns[tri]=1
    for pair,c in inc.items():ns[pair]=c-int(bool(tri) and tri&pair==pair)
    if min(ns[3],ns[12])<1 or any(ns[p]<0 for p in cross):continue
    for i in range(4):ns[1<<i]=ds[i]-sum(c for m,c in inc.items() if m>>i&1)+int(bool(tri) and tri>>i&1)
    ns[0]=35-sum(ds)+sum(inc.values())-int(bool(tri))
    if min(ns)<0:continue
    assert sum(ns)==35 and sum(ns[m] for m in cross)==t
    keys.add(tuple(ns))
assert keys==set(map(tuple,domain['labeled_keys'])) and len(keys)==412
perms=set()
for a,b,c in product((0,1),repeat=3):
 L=(1,0) if a else (0,1);R=(3,2) if b else (2,3);perms.add(R+L if c else L+R)
assert len(perms)==8
reps=set()
for ns in keys:
 images=[]
 for p in perms:
  out=[0]*16
  for m,n in enumerate(ns):out[sum(1<<p[i] for i in range(4) if m>>i&1)]=n
  images.append(tuple(out))
 reps.add(min(images))
assert reps==set(map(tuple,domain['representative_keys']))=={tuple(c['counts']) for c in result['cases']} and len(reps)==62
rowsout=[];values=[]
for c in result['cases']:
 ns=c['counts'];pos=tuple(c['best']['positions']);stubs=[frozenset(i+1 for i in range(4) if m>>i&1) for m,n in enumerate(ns) for _ in range(n)]
 assert len(stubs)==35 and tuple(sum(i+1 in x for x in stubs) for i in range(4))==tuple(c['degrees'])
 rows=independent_rows(21,pos,stubs);value=sum((min(r['A'],r['B'],r['C']) for r in rows),Fraction());assert value==Fraction(c['best']['bound'])<1;values.append(value)
 rowsout.append({'counts':ns,'degrees':c['degrees'],'t':c['t'],'positions':pos,'bound':str(value),'zero_quota':True,'original_edge_trace_masks':[sum(1<<(v-1) for v in x) for x in stubs],'rows':[{'k':r['k'],'A':str(r['A']),'B':str(r['B']),'C':str(r['C']),'minimum':str(min(r['A'],r['B'],r['C']))} for r in rows]})
(P/'INDEPENDENT_ROWS.json').write_text(json.dumps({'cases':rowsout},indent=2)+'\n')
out={'status':'PASS','scope':__doc__,'complete_global_degree_spectra':15,'selected_quad_multisets':38,'imported_quad_multisets':33,'new_quad_multisets':5,'new_ordered_degrees':44,'labels':len(keys),'marked_group_order':8,'orbits':len(reps),'labels_by_t':dict(Counter(sum(k[m] for m in cross) for k in keys)),'strict_certificates':len(values),'maximum_bound':str(max(values)),'zero_quota':True,'N':21,'locks':4,'free':17,'original_edge_indices':35,'ordered_distinct_pairs':1190,'rows':21*len(values),'cpu_seconds':time.process_time()-st}
(P/'INDEPENDENT_VERIFY.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
