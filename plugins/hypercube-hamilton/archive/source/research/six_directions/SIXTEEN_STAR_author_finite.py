"""Producer replay and count checks. Independent review is still required."""
from pathlib import Path
from itertools import permutations
import json,collections,struct,hashlib
P=Path(__file__).resolve().parent
T={7,11,13,19,21,25,31};WA={1,2,4,8,14,16,22};units={1,2,4,8,16}
E={x for x in range(1,32) if x.bit_count()%2==0};O={x for x in range(1,32) if x.bit_count()%2 and x.bit_count()>=3 and x not in {14,22}}
maps=[tuple(sum(((x>>q[d])&1)<<d for d in range(5)) for x in range(32)) for q in permutations(range(5))]
o=json.loads((P/'SIXTEEN_STAR_FORMAL_options.json').read_text());cl={c['index']:c for c in o['classes']};opts={}
for z in o['options']:
 J=(T-{z['t']})|(WA-{z['w'],z['b']});U=WA-{z['w'],z['b']};R={z['w'],z['b']};g=cl[z['Bclass']]['geometry'];fixed=set(cl[z['Bclass']]['forced_pairs'][0])
 valid=[i for i,tr in enumerate(maps) if {tr[x] for x in J}==set(g['majority']) and {tr[x] for x in U}==set(g['omitted']) and {tr[x] for x in R}==fixed]
 assert valid;z['B_permutation_index']=valid[0]
 opts[tuple(z[k] for k in ['q','t','w','b','case','permutation_index'])]=z
(P/'SIXTEEN_STAR_checked_options.json').write_text(json.dumps({'status':'PRODUCER_EXPLICIT_COMMON_MAPS','options':list(opts.values())},indent=2)+'\n')
labels={}
for case,seed in [(0,(3,4,7)),(3,(15,1,7))]:
 raw=(P/f'TWELVE_ROOT_STAR_OPENING_case_{case:02d}_forests.bin').read_bytes();assert len(raw)==8031*32;out=[]
 for i in range(8031):
  par=list(range(32));deg=[0]*32
  def find(x):
   while par[x]!=x:x=par[x]
   return x
  es=list(zip(raw[i*32:(i+1)*32:2],raw[i*32+1:(i+1)*32:2]));assert tuple(sorted((seed[0],seed[2]))) in es
  for a,b in es:
   assert a<b and (a^b).bit_count()==1;aa,bb=find(a),find(b);assert aa!=bb;par[aa]=bb;deg[a]+=1;deg[b]+=1
  assert deg==[0 if x in {0,31} else 2 if x in seed[:2] else 1 for x in range(32)]
  ids={};lab={}
  for x in range(1,31):
   r=find(x)
   if r not in ids:ids[r]=len(ids)
   lab[x]=ids[r]
  assert len(ids)==14;out.append(lab)
 labels[case]=out
raw=(P/'SIXTEEN_STAR_A_full_certificates.bin').read_bytes();assert len(raw)%32==0
seen=set();hist=collections.Counter();cls=collections.Counter()
for pos in range(0,len(raw),32):
 rec=raw[pos:pos+32];m=rec[22];assert 7<=m<=9 and rec[2*m:22]==bytes([255])*(22-2*m)
 es=list(zip(rec[:2*m:2],rec[1:2*m:2]));assert es==sorted(es) and len(set(rec[:2*m]))==2*m;key=rec[:22];assert key not in seen;seen.add(key)
 used=set(rec[:2*m]);assert T<=used
 for a,b in es:assert a<b and (a^b).bit_count()==1 and ((a in E and b in O) or (b in E and a in O))
 for a in O-used:assert all((a^(1<<d)) in used for d in range(5))
 q,t,w,b,c,pi=(rec[k] for k in [23,24,25,26,27,30]);z=opts[q,t,w,b,c,pi];assert q in E-used and t in T-{31}
 tr=maps[pi];seed=(3,4,7) if c==0 else (15,1,7);assert tuple(tr[x] for x in seed)==(q,b,t)
 si=int.from_bytes(rec[28:30],'little');assert si<8031;inverse={tr[x]:x for x in range(32)};lab=labels[c][si]
 hv=next((a if b==31 else b for a,b in es if 31 in (a,b)),None);assert rec[31]==(hv is not None)
 mod=[e for e in es if 31 not in e]+([(w,hv)] if hv is not None else [])
 par=list(range(14))
 def find(x):
  while par[x]!=x:x=par[x]
  return x
 for a,b in mod:
  aa,bb=find(lab[inverse[a]]),find(lab[inverse[b]]);assert aa!=bb;par[aa]=bb
 hist[m]+=1;cls[z['Bclass']]+=1
# Count by unmatched-odd subsets, independent of producer DFS ordering.
ee=sorted(E);ei={x:i for i,x in enumerate(ee)};free=sorted(O-T);dphist=collections.Counter()
for mask in range(1<<len(free)):
 U={free[i] for i in range(len(free)) if mask>>i&1};matched=sorted(O-U);required={x^(1<<d) for x in U for d in range(5)}
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
assert hist==dphist and sum(hist.values())==120463
# Exact source subset and complementary raw files, actual -> canonical maps.
Z={39,43,45,51,53,57,63};W={1,2,4,8,14,16,22,32};witness=bytearray();counts={};hashes={}
for v in [1,7,31]:
 name=f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin';r=(P/name).read_bytes();assert len(r)%15==0;remaining=bytearray();hit=0
 hashes[name]=hashlib.sha256(r).hexdigest()
 for i in range(len(r)//15):
  z=set(r[i*15:i*15+7]);wset=set(r[i*15+7:(i+1)*15]);chosen=None
  if v==31:
   for pi,tr in enumerate(maps):
    tr6=lambda x:tr[x&31]|(x&32)
    if {tr6(x) for x in z}==Z and {tr6(x) for x in wset}==W:chosen=pi;break
  if chosen is None:remaining.extend(r[i*15:(i+1)*15])
  else:witness.extend(struct.pack('<BIB',v,i,chosen));hit+=1
 (P/f'SIXTEEN_STAR_remaining_v{v}_covered.bin').write_bytes(remaining);counts[v]={'input':len(r)//15,'hit':hit,'remaining':len(remaining)//15}
assert sum(c['hit'] for c in counts.values())==30 and sum(c['remaining'] for c in counts.values())==118
(P/'SIXTEEN_STAR_actual_witnesses.bin').write_bytes(witness)
out={'status':'PRODUCER_AUTHOR_REPLAY_SUCCESS_NOT_INDEPENDENT_ACCEPTANCE','maximal_domain':120463,'unique':len(seen),'size_histogram':dict(hist),'DP_histogram':dict(dphist),'chosen_B_classes':dict(cls),'geometries':counts,'input_hashes':hashes,'remaining_covered_target_geometries':118,'full_sixteen_hole_proved':False,'full_P6_proved':False}
(P/'SIXTEEN_STAR_author_finite.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
