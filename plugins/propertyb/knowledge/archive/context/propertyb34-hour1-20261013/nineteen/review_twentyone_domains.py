"""Independent local-domain/selected-witness binding audit; no numeric-bound rerun."""
from pathlib import Path
from itertools import combinations,product
from fractions import Fraction
import json
ROOT=Path(__file__).resolve().parents[3]
BASE=ROOT/'context/propertyb34-hour1-20261013/low-math'
PAIRS=[3,5,9,6,10,12];TRIPLES=[7,11,13,14]
def quad(ds,ls):
    pair=dict(zip(PAIRS,ls))
    # Common triple counts, not the generator's exact-triple parameters.
    caps=[min(n for p,n in pair.items() if p&t==p) for t in TRIPLES]
    for ts in product(*(range(c+1) for c in caps)):
      common=dict(zip(TRIPLES,ts))
      for q in range(min(ts)+1):
        mu={15:q};mu.update({t:n-q for t,n in common.items()})
        for p,l in pair.items():mu[p]=l-sum(n for t,n in common.items() if t&p==p)+q
        for i,d in enumerate(ds):
          b=1<<i
          mu[b]=d-sum(n for p,n in pair.items() if p&b)+sum(n for t,n in common.items() if t&b)-q
        mu[0]=34-sum(ds)+sum(ls)-sum(ts)+q
        if min(mu.values())>=0:yield mu,common,q

def key(ds,mu):return (tuple(ds),tuple(mu.get(i,0) for i in range(1<<len(ds))))
def stored(name):return json.loads((BASE/name).read_text())['cases']
def keys(rows):return {key(r['ds'],{int(m):n for m,n in r['counts'].items()}) for r in rows}
low_expected=set()
for dy in (5,6,7):
 for dz in range(dy,9):
  for l in ((1,) if dy==5 else range(1,dy+1)):
   for t in (0,1):
    mu={7:t,3:1-t,5:1-t,6:l-t,1:5-2+t,2:dy-1-l+t,4:dz-1-l+t,0:34-5-dy-dz+2+l-t}
    if min(mu.values())>=0:low_expected.add(key((5,dy,dz),mu))
low=stored('TWENTYONE_FIVE_LOW.json');assert keys(low)==low_expected
quad_expected={key((5,8,8,8),mu) for ls in product((1,2),repeat=3) for mu,_,_ in quad((5,8,8,8),(1,1,1)+ls)}
quads=stored('TWENTYONE_FIVE_QUAD.json');assert keys(quads)==quad_expected
sevens_expected=set()
for ds,ls in [((5,7,7,7),(1,1,1,2,2,2))]+[((5,7,7,8),(1,1,1,2,a,b)) for a in (1,2) for b in (1,2)]+[((5,7,8,8),(1,1,1,a,b,c)) for a in (1,2) for b in (1,2) for c in range(1,9)]:
 for mu,common,q in quad(ds,ls):
  if ds==(5,7,7,7) and q!=1:continue
  if ds==(5,7,7,8) and not (common[7]==1 and common[11]==0 and common[13]==0):continue
  if ds==(5,7,8,8) and not (common[7]==0 and common[11]==0):continue
  sevens_expected.add(key(ds,mu))
sevens=stored('TWENTYONE_FIVE_SEVENS.json');assert keys(sevens)==sevens_expected
V=json.loads((BASE/'TWENTYONE_FIVE_VERIFIED.json').read_text())
def witness_key(r):return (r['v'],tuple(r['ds']),tuple(r['pos']),key(r['ds'],{int(m):n for m,n in r['counts'].items()}),Fraction(r['bound']))
witnesses={witness_key(r) for r in V['witnesses']}
needed=[r for r in low+quads+sevens if not (r['ds']==[5,7,8,8] and r['ls'][-1]>2)]
for r in needed:
 if Fraction(r['bound'])<1:assert witness_key(r) in witnesses
# All local high-codegree (5,8,8) triple objects have an accepted witness.
extra=set()
for l in range(3,9):
 for t in (0,1):
  mu={7:t,3:1-t,5:1-t,6:l-t,1:3+t,2:7-l+t,4:7-l+t,0:15+l-t}
  if min(mu.values())>=0:extra.add(key((5,8,8),mu))
actual_extra={key(r['ds'],{int(m):n for m,n in r['counts'].items()}) for r in V['witnesses'] if r['ds']==[5,8,8]}
assert actual_extra==extra
residual=[r for r in sevens if r['ds']==[5,7,8,8] and r['ls'][-1]<=2 and Fraction(r['bound'])>=1]
assert len(residual)==1
rr=residual[0];assert rr['ls']==[1,1,1,1,1,2] and rr['q']==0 and rr['t3']==[0]*4
residual_quad=[r for r in quads if Fraction(r['bound'])>=1]
assert len(residual_quad)==5 and all(r['q']==0 for r in residual_quad)
out={'status':'PASS','scope':'Independent complete local count domains and stored accepted-witness binding; numerical probability formulas and dual certificates NOT re-executed','counts':{'low_triples':len(low_expected),'5888_quadruples':len(quad_expected),'seven_quadruples':len(sevens_expected),'extra_588_triples':len(extra),'stored_verified_witnesses':len(V['witnesses'])},'residual_5788':1,'residual_5888':5}
Path(__file__).with_name('TWENTYONE_DOMAIN_REVIEW.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
