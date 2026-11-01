"""Actual7point outsideK avoiding unique singleton Ktrace; complete lift at pair traces/empty only. New pure quota2 only when c0=5; no other quota."""
from pathlib import Path
from itertools import product
from collections import Counter
from fractions import Fraction
import sys,json,time,argparse
P=Path(__file__).resolve().parent;ROOT=P.parents[4];sys.dont_write_bytecode=True;sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'));sys.path.insert(0,str(ROOT/'computations'))
from subset_position_dp import SubsetEngine
from independent_structure_bounds import independent_rows
st=time.process_time();ap=argparse.ArgumentParser();ap.add_argument('--all',action='store_true');arg=ap.parse_args();pairs=(3,5,6,9,10,12);base=(15,0,0,3,0,3,4,0,1,3,3,0,3,0,0,0);menu=[(z,8,9,20,21) for z in (1,10,11,12)];cases=[]
# Actual strict old degree-pair imports (not a blanket global pair assumption).
old=json.loads((ROOT/'context/propertyb35-paper/round01/twentyone-high/DOUBLES.json').read_text());strictpair={}
for d in (9,10):
 for c in range(5,8):
  x=next(z for z in old['cases'] if z.get('degrees')==[7,d] and z.get('codegree')==c);assert x['strict'];strictpair[(d,c)]=x['bound']
inputs=[]
for cs in product(*(range(base[m]+1) for m in pairs)):
 if sum(cs)>7:continue
 c0=7-sum(cs)
 if c0>base[0]:continue
 row=[sum(c for m,c in zip(pairs,cs) if m>>v&1) for v in range(4)]
 if min(row)<1 or max(row)>4:continue
 assert c0<=5
 inputs.append((cs,c0,row))
for cs,c0,row in inputs:
 picked={0:c0,**dict(zip(pairs,cs))};ns=Counter()
 for m,n in enumerate(base):
  c=picked.get(m,0)
  if n-c:ns[2*m]+=n-c
  if c:ns[2*m+1]+=c
 assert sum(ns.values())==35 and ns.get(1,0)==c0 and all(sum(n for m,n in ns.items() if m>>v&1)==d for v,d in enumerate((7,9,10,10,10)))
 e=SubsetEngine(21,5,ns);e.inv={p:(0,0,[]) for p in e.inv};q=2 if c0==5 else 0;vals=[]
 for pos in menu:
  bp={k:1<<i for i,k in enumerate(pos)};left=0;total=0;zero=0;rows=[]
  for k in range(1,22):
   pivot=bp.get(k,0);value=e.value(k,left,pivot);zero+=value;loss=0
   if pivot==1 and q:
    right=e.full^left^pivot;a=k-1-left.bit_count();b=21-k-right.bit_count();W=e.pair(1,1,left,pivot,a,b);loss=2*q*W
    A=sum(e.zeta[pivot][left][r]*e.fl[a][r]*e.fact[e.N-r] for r in range(6))
    B=sum(e.zeta[pivot][right][r]*e.fl[b][r]*e.fact[e.N-r] for r in range(6))
    C=0
    for r in range(6):
     for u in range(6):
      if r+u<=e.N:C+=e.zeta[pivot][left][r]*e.zeta[pivot][right][u]*e.fl[a][r]*e.fl[b][u]*e.fact[e.N-r-u]
    C-=ns.get(pivot,0)*W;assert C-loss>=0
    corrected=min(A,B,C-loss);assert value==min(A,B,C)
   else:corrected=value
   total+=corrected;rows.append({'k':k,'old_min':str(Fraction(value,e.D)),'loss':str(Fraction(loss,e.D)),'corrected_min':str(Fraction(corrected,e.D))});left|=pivot
  vals.append({'positions':pos,'bound':str(Fraction(total,e.D)),'zero_bound':str(Fraction(zero,e.D)),'strict':total<e.D,'rows':rows})
 best=min(vals,key=lambda z:Fraction(z['bound']));z={'pair_lifts':cs,'c0':c0,'Krow':row,'counts':dict(ns),'pure_quota':q,'menu':vals,'best':best};cases.append(z)
 if len(cases)==1:
  # Independent rows, exact extra loss only at z pivot, then recompute each min.
  masks=[m for m,n in ns.items() for _ in range(n)];types=[frozenset(i+1 for i in range(5) if m>>i&1) for m in masks];rr=independent_rows(21,tuple(best['positions']),types);v=Fraction()
  def fall(n,r):
   z=1
   for j in range(r):z*=n-j
   return z
  pos=best['positions'];kz=pos[0];a=kz-1-sum(k<kz for k in pos[1:]);b=21-kz-sum(k>kz for k in pos[1:]);W=Fraction(fall(a,4)*fall(b,4),fall(16,8))
  for r in rr:
   loss=2*q*W if r['k']==kz else 0;assert r['C']>=loss;v+=min(r['A'],r['B'],r['C']-loss)
  assert v==Fraction(best['bound']);(P/'SINGLE_CASE_PILOT.json').write_text(json.dumps({'source':z,'independent_bound':str(v),'free':16,'W':str(W),'cpu_seconds':time.process_time()-st,'domain_size_generated':len(inputs)},indent=2)+'\n');print('PILOT',len(inputs),cs,c0,best['bound'],'zero',best['zero_bound'],'CPU',time.process_time()-st,flush=True)
  if not arg.all:break
 if not best['strict']:
  print('NONSTRICT',cs,c0,best['bound'],flush=True);break
 if time.process_time()-st>12:break
out={'scope':__doc__,'base_counts':base,'pair_order':pairs,'full_input_domain':len(inputs),'inputs':[{'pair_lifts':cs,'c0':c0,'Krow':row} for cs,c0,row in inputs],'old_strict_pair_imports':{str(k):v for k,v in strictpair.items()},'complete':len(cases)==len(inputs),'case_count':len(cases),'strict_count':sum(z['best']['strict'] for z in cases),'cases':cases,'nonstrict':[z for z in cases if not z['best']['strict']],'maximum_best_bound':str(max(Fraction(z['best']['bound']) for z in cases)),'cpu_seconds':time.process_time()-st}
(P/('RESULT.json' if arg.all else 'PILOT_RESULT.json')).write_text(json.dumps(out,indent=2)+'\n');print('FINAL',out['complete'],out['case_count'],out['strict_count'],out['maximum_best_bound'],out['cpu_seconds'])
