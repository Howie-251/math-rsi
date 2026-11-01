"""Fresh r5 integration audit: independent colored domain and nested quota binding.
No DP, producer canonicalization, Profile, pure_quota, or probability engine imports.
"""
from pathlib import Path
from itertools import combinations,permutations,product
from collections import Counter,defaultdict
from fractions import Fraction as Q
from math import comb
from time import process_time
import json,sys
P=Path(__file__).resolve().parent;F=P.parent;B=F.parent
R=next(p for p in P.parents if (p/'proofs/PROBABILITY_LEMMAS.md').exists())
S=R/'context/propertyb34/round01/high-math'
def read(p):return json.loads(p.read_text())
def ns(z):return {int(k):v for k,v in z['counts'].items() if v}
def move(m,p):return sum(1<<p[i] for i in range(9) if m>>i&1)
def serial(x):
 if isinstance(x,Q):return str(x)
 if isinstance(x,dict):return {str(k):serial(v) for k,v in x.items()}
 if isinstance(x,(tuple,list)):return [serial(v) for v in x]
 return x

def canon(big,low):
 # Only initial point invariants, then all color-preserving bijections.
 # This does not use producer refinement or its canonical labels.
 classes=defaultdict(list)
 for i in range(9):
  classes[(int(i not in low),tuple(sum(bool(t>>i&1) and t.bit_count()==j for t in big) for j in (3,4,5)))].append(i)
 cells=[v for _,v in sorted(classes.items())];best=None;bp=None
 for orders in product(*(permutations(c) for c in cells)):
  p=[0]*9;off=0
  for order in orders:
   for i in order:p[i]=off;off+=1
  k=tuple(sorted(move(t,p) for t in big))
  if best is None or k<best:best=k;bp=p
 return best,bp

def domain(profile=False):
 cat=read(S/'UNIT_CATALOGUE_9.json');D=read(B/'DOMAIN.json')['records'];saved={(x['base'],tuple(x['low'])):i for i,x in enumerate(D)}
 assert cat['complete'] and len(cat['orbits'])==374
 pairs=list(combinations(range(9),2));out=[];groups=defaultdict(list);excluded=[0,0];raw=0
 for base,big0 in enumerate(cat['orbits']):
  big=tuple(big0);used=set()
  for t in big:
   assert 3<=t.bit_count()<=5
   for i,j in pairs:
    if t>>i&1 and t>>j&1:assert (i,j) not in used;used.add((i,j))
  blocks=big+tuple((1<<i)|(1<<j) for i,j in pairs if (i,j) not in used)
  # Enumerate high sets, not producer's low sets; recover 35 indexed types directly.
  for high in combinations(range(9),4):
   low=tuple(i for i in range(9) if i not in high);lm=sum(1<<i for i in low);raw+=1
   if any((t&lm).bit_count()>2 for t in blocks):excluded[0]+=1;continue
   count=Counter(blocks)
   for i in range(9):count[1<<i]=(6 if i in low else 7)-sum(bool(t>>i&1) for t in blocks)
   empty=35-sum(count.values())
   if empty<0 or min(count.values())<0:excluded[1]+=1;continue
   count[0]=empty;count=+count
   idx=saved[base,low];z=D[idx];assert dict(count)==ns(z)
   assert sum(count.values())==35
   for i in range(9):assert sum(v for t,v in count.items() if t>>i&1)==(6 if i in low else 7)
   for i,j in pairs:assert sum(v for t,v in count.items() if t>>i&1 and t>>j&1)==1
   key,p=canon(big,low);assert sum(1<<p[i] for i in low)==31
   groups[key].append(idx);out.append(idx)
   if profile and len(out)==30:return dict(profile=True,labels=30),D,groups
 assert raw==47124 and excluded==[34998,9019] and sorted(out)==list(range(3107))
 # Compare partitions by member identities, independently of canonical encodings.
 known=defaultdict(list)
 for i,z in enumerate(D):known[tuple(z['canonical_large']),z['canonical_lowmask']].append(i)
 assert {tuple(sorted(v)) for v in groups.values()}=={tuple(sorted(v)) for v in known.values()}
 assert len(groups)==1689
 return dict(raw_markings=raw,excluded_low_trace=excluded[0],excluded_negative=excluded[1],labels=3107,colored_orbits=1689,families=len({D[i]['base'] for i in out})),D,groups

def choose(n,k):return comb(n,k) if 0<=k<=n else 0

def context(pos,k):
 left=sum(1<<i for i,t in enumerate(pos) if t<k);right=sum(1<<i for i,t in enumerate(pos) if t>k)
 bit=next((1<<i for i,t in enumerate(pos) if t==k),0)
 return left,right,bit,k-1-left.bit_count(),25-k-right.bit_count()

def direction(t,u,left,right,bit,a,b):
 rt=5-t.bit_count();ru=5-u.bit_count()
 if bit:
  if t&u!=bit or (t^bit)&~left or (u^bit)&~right or rt+ru>16:return Q()
  numerator=choose(a,rt)*choose(b,ru)
  return Q(numerator,choose(16,rt)*choose(16-rt,ru)) if numerator else Q()
 if t&u or t&~left or u&~right or min(rt,ru)<1 or rt+ru-1>16:return Q()
 numerator=choose(a,rt-1)*choose(b,ru-1)
 return Q(numerator,16*choose(15,rt-1)*choose(16-rt,ru-1)) if numerator else Q()

def direct_rows(count,pos):
 out=[]
 for k in range(1,26):
  l,r,bit,a,b=context(pos,k);A=Q();BB=Q();C=Q()
  for t,n in count.items():
   free=5-t.bit_count()
   for allowed,slots,name in ((l,a,'A'),(r,b,'B')):
    if bit:
     valid=t&bit and not ((t^bit)&~allowed);num=choose(slots,free);den=choose(16,free)
    else:
     valid=free>=1 and not (t&~allowed);num=free*choose(slots,free-1);den=16*choose(15,free-1)
    val=Q(n*num,den) if valid and num else Q()
    if name=='A':A+=val
    else:BB+=val
   for u,m in count.items():
    cap=n*(m-int(t==u))
    if cap:C+=cap*direction(t,u,l,r,bit,a,b)
  out.append(dict(k=k,A=A,B=BB,C=C))
 return out

def quota(count,pos,i):
 bit=1<<i;k=pos[i];ctx=context(pos,k)
 # Expand distinct original edge stubs and retain every unordered index pair,
 # including zero-weight pairs and equal-type/different-index pairs.
 stubs=[t for t,n in count.items() for _ in range(n) if t&bit]
 degree=len(stubs);qt=max(0,(4*degree-24+2)//3);qp=max(0,(4*count.get(bit,0)-16+2)//3)
 assert degree in (6,7) and qt==(0 if degree==6 else 2) and qp in (0,2) and qp<=qt
 slots=[(direction(t,u,*ctx)+direction(u,t,*ctx),j,k,t==bit and u==bit)
        for j,t in enumerate(stubs) for k,u in enumerate(stubs) if j<k]
 pure=sorted(x for x in slots if x[3])[:qp];assert len(pure)==qp
 used={(x[1],x[2]) for x in pure};rest=sorted(x for x in slots if (x[1],x[2]) not in used)[:qt-qp]
 assert len(rest)==qt-qp
 return dict(degree=degree,q_total=qt,q_pure=qp,loss=sum((x[0] for x in pure+rest),Q()),
             slot_count=len(slots),zero_weight_slots=sum(x[0]==0 for x in slots),
             used_distinct_index_pairs=[[x[1],x[2]] for x in pure+rest])

def coverage(D,groups):
 c=read(F/'COVERAGE_RESULT.json');callers=c['callers'];assert len(callers)==3107
 original={tuple(sorted(ids)) for ids in groups.values()};covered=set();sources=Counter();transport=[]
 for i,x in enumerate(callers):
  assert x['domain_record']==i;tgt=D[i];cert=x['certificate'];src=D[cert['record']];ps=src['old_to_canonical'];pt=tgt['old_to_canonical']
  assert sorted(ps)==sorted(pt)==list(range(9))
  inv={v:k for k,v in enumerate(ps)};p=[inv[pt[j]] for j in range(9)]
  assert {move(t,p):n for t,n in ns(tgt).items()}==ns(src)
  assert {p[j] for j in tgt['low']}==set(src['low'])
  positions=[cert['positions'][p[j]] for j in range(9)]
  assert positions==x['transported_positions'] and len(set(positions))==9 and all(1<=v<=25 for v in positions)
  assert Q(cert['bound'])<1;sources[cert['source']]+=1;covered.add(cert['record'])
  transport.append(dict(target=i,source=cert['record'],target_to_source=p,positions=positions,certificate_layer=cert['source']))
 assert len(covered)==1689 and sources==Counter(old_affine_corrected=736,prior_pilot_raw=12,diverse40_raw=100,full_raw=2259)
 source_layers={}
 for x in callers:source_layers[x['certificate']['record']]=x['certificate']['source']
 assert Counter(source_layers.values())==Counter(old_affine_corrected=325,prior_pilot_raw=2,diverse40_raw=40,full_raw=1322)
 return dict(targets=3107,distinct_sources=1689,by_marking=dict(sources),by_source=dict(Counter(source_layers.values()))),transport

def old_replay(D,profile=False):
 archived=read(F/'OLD325_REPLAY_RESULT.json');rows=[];maxv=Q();qstats=Counter();empty=Counter()
 cases=archived['records'][:5] if profile else archived['records']
 assert archived['orbits']==325 and archived['rows']==8125
 for z in cases:
  i=z['domain_record'];d=D[i];count=ns(d);pos=z['positions'];assert pos==d['positions'];empty[count.get(0,0)]+=1
  actual=direct_rows(count,pos);certs=[quota(count,pos,j) for j in range(9)]
  for a,b in zip(certs,z['certificates']):
   assert all(a[k]==Q(b[k]) for k in ('degree','q_total','q_pure','loss'))
   qstats[a['degree'],a['q_total'],a['q_pure']]+=1
  losses={pos[j]:c['loss'] for j,c in enumerate(certs)};total=Q()
  for row,saved in zip(actual,z['rows']):
   assert all(row[k]==Q(saved[k]) for k in ('A','B','C'))
   loss=losses.get(row['k'],Q());assert loss==Q(saved['deduction']) and 0<=loss<=row['C']
   bound=min(row['A'],row['B'],row['C']-loss);assert bound==Q(saved['bound']);total+=bound
   row.update(deduction=loss,corrected_C=row['C']-loss,bound=bound)
  assert total==Q(z['bound'])==Q(d['old_bound'])<1;maxv=max(maxv,total)
  rows.append(dict(domain_record=i,positions=pos,count=count,certificates=certs,rows=actual,bound=total))
 return dict(cases=len(cases),position_rows=25*len(cases),maximum=maxv,quota_parameter_counts={str(k):v for k,v in qstats.items()},empty_type_multiplicities=dict(empty)),rows

def raw_binding(D):
 # Do not rerun raw DP or all raw ABC. Inspect every explicit witness and
 # its saved independent injection rows, exact count recovery and row sum.
 layers=[]
 pilot=read(B/'PROFILE.json')['records'];layers.append(('prior_pilot',pilot,'raw_witness_bound','rows'))
 layers.append(('diverse40',read(B/'diverse40/RESULT.json')['records'],'raw_bound','raw_rows'))
 layers.append(('full_raw',[json.loads(s) for s in (F/'RECORDS.jsonl').read_text().splitlines() if s.strip()],'raw_bound','raw_rows'))
 count=0;mx=Q();lookup={(z['base'],tuple(z['low'])):i for i,z in enumerate(D)}
 for name,cases,valuekey,rowskey in layers:
  for z in cases:
   i=z.get('domain_record',lookup[(z['base'],tuple(z['low']))]);assert ns(z)==ns(D[i])
   rr=z[rowskey];assert len(rr)==25
   value=sum((min(Q(t[k]) for k in ('A','B','C')) for t in rr),Q())
   assert value==Q(z[valuekey])<1;count+=1;mx=max(mx,value)
 assert count==1365 # 3 old pilot entries, of which only 2 are new orbits
 return dict(stored_raw_cases=1365,unique_raw_orbits=1364,rows_checked=25*count,maximum=mx,ABC_injection_not_reexecuted=True)

def main():
 t0=process_time();profile='--profile' in sys.argv
 dom,D,G=domain(profile)
 if profile:
  q,rows=old_replay(D,True);out=dict(status='PROFILE_PASS',domain=dom,old325=q,cpu_seconds=process_time()-t0)
 else:
  cov,trans=coverage(D,G);q,rows=old_replay(D);raw=raw_binding(D)
  (P/'TRANSPORT.json').write_text(json.dumps(trans,indent=2)+'\n')
  (P/'OLD325_ROWS.json').write_text(json.dumps(serial(rows),indent=2)+'\n')
  out=dict(status='PASS_WITH_DECLARED_IMPORTS',review_independence='same-family',acceptance_status='provisional',
           domain=dom,coverage=cov,old325=q,new_raw_binding=raw,DP_rerun=False,cpu_seconds=process_time()-t0)
 name='PROFILE.json' if profile else 'RESULT.json';(P/name).write_text(json.dumps(serial(out),indent=2)+'\n');print(json.dumps(serial(out),indent=2))
if __name__=='__main__':main()
