"""Independent frozen-input binding, marked maps and exact application checks."""
from pathlib import Path
from itertools import permutations
import hashlib,json,struct,collections
R=Path(__file__).resolve().parent
def js(n):return json.loads((R/n).read_bytes())
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
manifest=js('FOURTEEN_FINAL25_MANIFEST.json')
for n,h in manifest['input_hashes'].items():assert sha(n)==h.removeprefix('sha256:'),n
gates={}
for n in ['FOURTEEN_MID_SELECTED_REVIEW.json','HIGHER_FORCED_CHERRY_REVIEW.json']:
 d=js(n);assert d['verdict']=='PASS';gates[n]=sha(n)
 for field in ['audited_input_hashes','imported_dependency_hashes','checker_artifact_hashes']:
  for name,h in d.get(field,{}).items():assert sha(name)==h.removeprefix('sha256:'),(n,name)
rows=js('FOURTEEN_FINAL25_B_summary.json')['reports'];assert {r['index'] for r in rows}=={0,1,7,100,101}
maps=[tuple(sum(((x>>p[d])&1)<<d for d in range(5)) for x in range(32)) for p in permutations(range(5))]
def mask(s):return sum(1<<x for x in set(s))
units={1,2,4,8,16};T={7,11,13,19,21,25};option_reports=[]
for orbit in [0,1]:
 registry=set();M={0} if orbit==0 else {0,30};WA=units|({14} if orbit==0 else set())
 for row in rows:
  if row['orbit']!=orbit:continue
  g=row['geometry']
  for tr in maps:
   if {tr[x] for x in g['minority']}!=M:continue
   registry.add((mask(tr[x] for x in g['majority']),mask(tr[x] for x in g['omitted']),mask(tr[x] for x in row['forced_pairs'][0]),row['index']))
 (R/f'FOURTEEN_FINAL25_REVIEW_registry_{orbit}.txt').write_text(''.join(' '.join(map(str,x))+'\n' for x in sorted(registry)))
 opts=js('FOURTEEN_FINAL25_checked_options.json')['orbits'][orbit];assert opts['orbit']==orbit
 classes={r['Bclass']:r for r in rows if r['orbit']==orbit};seen=set()
 for op in opts['options']:
  q,t,w,b,c,pi,idx,bpi=[op[k] for k in ['q','t','w','b','case','permutation_index','Bclass','B_permutation_index']]
  assert t in T and w in units and b in units-{w} and c in [0,3] and 0<=pi<120 and 0<=bpi<120
  assert q!=0 and q.bit_count()%2==0 and (q^t).bit_count()==1
  tr=maps[pi];seed=(3,4,7) if c==0 else (15,1,7);assert tuple(tr[x] for x in seed)==(q,b,t)
  S=WA-{w,b};J=(T-{t})|S;row=classes[idx];g=row['geometry'];tr=maps[bpi]
  assert row['orbit']==orbit
  assert {tr[x] for x in M}==set(g['minority']) and {tr[x] for x in J}==set(g['majority'])
  assert {tr[x] for x in S}==set(g['omitted']) and {tr[x] for x in [w,b]}==set(row['forced_pairs'][0])
  # Unit mirrors are internally covered and cannot be suppressed/port ends;
  # virtual target port 63 has local label31, distinct from all protected ends.
  assert not {w,b}&(S|T|M|{31}) and 31 not in (S|T|M|{w,b})
  key=(q,t,w,b,c,pi);assert key not in seen;seen.add(key)
 option_reports.append({'orbit':orbit,'options_checked':len(seen),'marked_registry_entries':len(registry)})
Z={39,43,45,51,53,57};Ws=[units|{14,32},units|{32,62}]
raw=(R/'FOURTEEN_FINAL25_actual_witnesses.bin').read_bytes();assert len(raw)==175
wits=list(struct.iter_unpack('<BIBB',raw));byindex={};hits=collections.Counter()
for v,i,orbit,pi in wits:
 assert v==31 and 0<=orbit<2 and 0<=pi<120 and (v,i) not in byindex
 byindex[v,i]=(orbit,pi)
reports=[]
source=js('FOURTEEN_MID_SELECTED_REVIEW.json')
for v in [1,7,31]:
 name=f'FOURTEEN_MID_SELECTED_remaining_v{v}_covered.bin';r=(R/name).read_bytes();assert len(r)%13==0
 assert source['audited_input_hashes'].get(name,source.get('checker_artifact_hashes',{}).get(name)) in (sha(name),'sha256:'+sha(name))
 records=[r[i:i+13] for i in range(0,len(r),13)];assert len(set(records))==len(records)
 remain=[]
 for i,rec in enumerate(records):
  assert list(rec[:6])==sorted(rec[:6]) and list(rec[6:])==sorted(rec[6:])
  candidates=[]
  for orbit,W in enumerate(Ws):
   for pi,tr in enumerate(maps):
    f=lambda x:tr[x&31]|(x&32)
    if v==31 and {f(x) for x in rec[:6]}==Z and {f(x) for x in rec[6:]}==W:candidates.append((orbit,pi))
  if candidates:
   assert byindex[v,i] in candidates;orbit,pi=byindex[v,i];hits[orbit]+=1
  else:assert (v,i) not in byindex;remain.append(rec)
 assert (R/f'FOURTEEN_FINAL25_remaining_v{v}_covered.bin').read_bytes()==b''.join(remain)
 reports.append({'target':v,'source':len(records),'positive':len(records)-len(remain),'remaining':len(remain)})
assert hits=={0:20,1:5} and [r['source'] for r in reports]==[0,0,25] and all(r['remaining']==0 for r in reports)
out={'status':'PASS','all_manifest_input_hashes_verified':len(manifest['input_hashes']),'imported_gate_hashes':gates,'checked_simultaneous_options':option_reports,'application':reports,'orbit_actual_counts':dict(hits),'source_witnesses_checked':len(wits)}
(R/'FOURTEEN_FINAL25_REVIEW_prepare.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
