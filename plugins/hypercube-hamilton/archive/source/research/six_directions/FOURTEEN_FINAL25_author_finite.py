"""Producer replay/count checks of positive witnesses, not independent review."""
from pathlib import Path
from itertools import permutations
import json,collections,struct,hashlib
P=Path(__file__).resolve().parent
T={7,11,13,19,21,25};units={1,2,4,8,16};E={x for x in range(1,32) if x.bit_count()%2==0}
maps=[tuple(sum(((x>>q[d])&1)<<d for d in range(5)) for x in range(32)) for q in permutations(range(5))]
formal=json.loads((P/'FOURTEEN_FINAL25_FORMAL_options.json').read_text());allopts={};results=[]
# Reuse only the positive forest parser from a producer author script; no old outputs execute.
s=(P/'SIXTEEN_STAR_author_finite.py').read_text();s=s[s.index('labels={}'):s.index("raw=(P/'SIXTEEN_STAR_A_full_certificates.bin')")]
exec(compile(s,'old_positive_forest_parser','exec'))
checked=[]
for z in formal['orbits']:
 orbit=z['orbit'];WA=units|({14} if orbit==0 else set());M={0} if orbit==0 else {0,30};O={x for x in range(1,32) if x.bit_count()%2 and x.bit_count()>=3 and (orbit==1 or x!=14)}
 cl={c['Bclass']:c for c in z['classes']};opts={}
 for a in z['options']:
  J=(T-{a['t']})|(WA-{a['w'],a['b']});U=WA-{a['w'],a['b']};R={a['w'],a['b']};g=cl[a['Bclass']]['geometry'];fixed=set(cl[a['Bclass']]['forced_pairs'][0])
  valid=[i for i,tr in enumerate(maps) if {tr[x] for x in M}==set(g['minority']) and {tr[x] for x in J}==set(g['majority']) and {tr[x] for x in U}==set(g['omitted']) and {tr[x] for x in R}==fixed]
  assert valid;a['B_permutation_index']=valid[0];opts[tuple(a[k] for k in ['q','t','w','b','case','permutation_index'])]=a
 checked.append({'orbit':orbit,'options':list(opts.values())})
 raw=(P/f'FOURTEEN_FINAL25_A_full_{orbit}_certificates.bin').read_bytes();assert len(raw)%32==0
 seen=set();hist=collections.Counter();cls=collections.Counter();flags=collections.Counter()
 for pos in range(0,len(raw),32):
  rec=raw[pos:pos+32];m=rec[22];assert 6<=m<=len(O) and rec[2*m:22]==bytes([255])*(22-2*m)
  es=list(zip(rec[:2*m:2],rec[1:2*m:2]));assert es==sorted(es) and len(set(rec[:2*m]))==2*m;key=rec[:22];assert key not in seen;seen.add(key);used=set(rec[:2*m]);assert T<=used and (orbit==0 or 30 in used)
  for a,b in es:assert a<b and (a^b).bit_count()==1 and ((a in E and b in O) or (b in E and a in O))
  for a in O-used:assert all((a^(1<<d)) in used for d in range(5))
  q,t,w,b,c,pi=(rec[k] for k in [23,24,25,26,27,30]);a=opts[q,t,w,b,c,pi];assert q in E-used and t in T
  tr=maps[pi];seed=(3,4,7) if c==0 else (15,1,7);assert tuple(tr[x] for x in seed)==(q,b,t)
  si=int.from_bytes(rec[28:30],'little');assert si<8031;inverse={tr[x]:x for x in range(32)};lab=labels[c][si]
  hv=next((a if b==31 else b for a,b in es if 31 in (a,b)),None);assert rec[31]==(hv is not None)
  mod=[e for e in es if 31 not in e]+([(w,hv)] if hv is not None else []);par=list(range(14))
  def find(x):
   while par[x]!=x:x=par[x]
   return x
  for x,y in mod:
   xx,yy=find(lab[inverse[x]]),find(lab[inverse[y]]);assert xx!=yy;par[xx]=yy
  hist[m]+=1;cls[a['Bclass']]+=1;flags[rec[31]]+=1
 # Maximal-domain count by unmatched odd subsets, with required even coverage.
 ee=sorted(E);ei={x:i for i,x in enumerate(ee)};free=sorted(O-T);dphist=collections.Counter()
 for mask in range(1<<len(free)):
  U={free[i] for i in range(len(free)) if mask>>i&1};matched=sorted(O-U);required={x^(1<<d) for x in U for d in range(5)}|({30} if orbit==1 else set())
  if len(required)>len(matched):continue
  dp={0:1}
  for x in matched:
   nxt=collections.defaultdict(int)
   for used,n in dp.items():
    for d in range(5):
     bit=1<<ei[x^(1<<d)]
     if not used&bit:nxt[used|bit]+=n
   dp=nxt
  req=sum(1<<ei[x] for x in required);dphist[len(matched)]+=sum(n for used,n in dp.items() if used&req==req)
 assert hist==dphist
 results.append({'orbit':orbit,'maximal_domain':len(seen),'size_histogram':dict(hist),'DP_histogram':dict(dphist),'chosen_B_classes':dict(cls),'target_internal_flag_histogram':dict(flags)})
(P/'FOURTEEN_FINAL25_checked_options.json').write_text(json.dumps({'status':'PRODUCER_EXPLICIT_COMMON_MAPS','orbits':checked},indent=2)+'\n')
Z={39,43,45,51,53,57};Ws=[{1,2,4,8,14,16,32},{1,2,4,8,16,32,62}];witness=bytearray();counts={};hashes={}
for v in [1,7,31]:
 name=f'FOURTEEN_MID_SELECTED_remaining_v{v}_covered.bin';r=(P/name).read_bytes();assert len(r)%13==0;remaining=bytearray();hit=collections.Counter();hashes[name]=hashlib.sha256(r).hexdigest()
 for i in range(len(r)//13):
  z=set(r[i*13:i*13+6]);wset=set(r[i*13+6:(i+1)*13]);chosen=None
  if v==31:
   for orbit,W in enumerate(Ws):
    for pi,tr in enumerate(maps):
     tr6=lambda x:tr[x&31]|(x&32)
     if {tr6(x) for x in z}==Z and {tr6(x) for x in wset}==W:chosen=(orbit,pi);break
    if chosen is not None:break
  if chosen is None:remaining.extend(r[i*13:(i+1)*13])
  else:orbit,pi=chosen;witness.extend(struct.pack('<BIBB',v,i,orbit,pi));hit[orbit]+=1
 (P/f'FOURTEEN_FINAL25_remaining_v{v}_covered.bin').write_bytes(remaining);counts[v]={'input':len(r)//13,'hit':dict(hit),'remaining':len(remaining)//13}
assert sum(sum(c['hit'].values()) for c in counts.values())==25 and sum(c['remaining'] for c in counts.values())==0
(P/'FOURTEEN_FINAL25_actual_witnesses.bin').write_bytes(witness)
out={'status':'PRODUCER_AUTHOR_REPLAY_SUCCESS_NOT_INDEPENDENT_ACCEPTANCE','A_reports':results,'geometries':counts,'input_hashes':hashes,'remaining_covered_target_geometries':0,'full_fourteen_hole_proved':False,'full_P6_proved':False}
(P/'FOURTEEN_FINAL25_author_finite.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
