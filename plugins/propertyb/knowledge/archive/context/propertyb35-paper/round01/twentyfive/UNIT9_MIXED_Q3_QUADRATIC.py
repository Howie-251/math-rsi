"""q3 nine-unit residuals: fixed nonconsecutive layout + fixed ABC choices.
Every saved polynomial is an exact degree<=2 Boolean expression for that
fixed-branch sum; it upper-bounds the true per-row min. No false affine claim.
"""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import sys,json,time
P=Path(__file__).resolve().parent;R=P.parents[3];S=R/'context/propertyb34/round01/high-math'
sys.dont_write_bytecode=True
sys.path[:0]=[str(S),str(R/'computations'),str(R/'computations/propertyb33/round01')]
from bare_layout import BareLayout
from subset_position_dp import SubsetEngine
from multilock import Profile,rows,total_bound,json_value
from pure_quota import certificate

def counts(f,c,mask):
 return {t:a for t,a in {**{int(t):1 for t in f['full']},**{1<<i:a-int(bool(mask>>i&1)) for i,a in enumerate(f['single_high'])},0:c['empty']}.items() if a}

class FixedBranch:
 def __init__(self,f,c,positions,choices):
  self.f=f;self.c=c;self.choices=choices;self.engine=BareLayout(25,positions)
  self.eligible=f['eligible'];self.loss=[]
  for mask in (0,sum(1<<i for i in self.eligible)):
   p=Profile(25,5,positions,counts(f,c,mask))
   self.loss.append({positions[i]:certificate(p,i)['loss'] for i in range(9)})
  self.position_label={p:i for i,p in enumerate(positions)}
 def evaluate(self,mask,both=False):
  _,abc=self.engine.bound(counts(self.f,self.c,mask),True)
  fixed=minimum=Q()
  for k,raw in enumerate(abc,1):
   vals=list(raw)
   if k in self.position_label:
    i=self.position_label[k];vals[2]-=self.loss[int(bool(mask>>i&1))][k]
   fixed+=vals[self.choices[k-1]];minimum+=min(vals)
  return (fixed,minimum) if both else fixed
 def polynomial(self):
  c=self.evaluate(0);singles={i:self.evaluate(1<<i) for i in self.eligible}
  linear=[singles[i]-c if i in singles else Q() for i in range(9)]
  quad=[]
  for i,j in combinations(self.eligible,2):
   val=self.evaluate((1<<i)|(1<<j))-singles[i]-singles[j]+c
   if val:quad.append([i,j,val])
  return dict(constant=c,linear=linear,quadratic=quad)

def poly_value(poly,mask):
 return Q(poly['constant'])+sum((Q(a) for i,a in enumerate(poly['linear']) if mask>>i&1),Q())+sum((Q(a) for i,j,a in poly['quadratic'] if mask>>i&1 and mask>>j&1),Q())

def affine_value(f,c,mask):
 return min(Q(a)+sum((Q(lay['slopes'][i]) for i in range(9) if mask>>i&1),Q()) for a,lay in zip(c['layout_constants'],f['layouts']))

def independent_fixed(f,c,mask,positions,choices):
 p=Profile(25,5,positions,counts(f,c,mask));dd={positions[i]:certificate(p,i)['loss'] for i in range(9)}
 rr=rows(p,deductions=dd)
 return sum(((r['A'],r['B'],r['corrected_C'])[ch] for r,ch in zip(rr,choices)),Q())

def run(pilot=False):
 st=time.perf_counter();src=json.loads((P/'UNIT9_MIXED_AFFINE.json').read_text())
 targets=[(f,c) for f in src['families'] if f['feasible'] for c in f['cases'] if c['q']==3 and c.get('residual_colors')]
 prev={}
 if not pilot and (P/'UNIT9_MIXED_Q3_QUADRATIC_PILOT.json').exists():
  previous=json.loads((P/'UNIT9_MIXED_Q3_QUADRATIC_PILOT.json').read_text());prev={f['base']:f for f in previous['families']}
 limit=5 if pilot else len(targets);budget=120;out=[];dp_calls=0;exactchecks=independentchecks=0;processed=0
 for f,c in targets[:limit]:
  original=c['residual_colors'];remain={mask:affine_value(f,c,mask) for mask in original}
  polys=[];flags=[];family_start=time.perf_counter()
  if f['base'] in prev:
   old=prev[f['base']];polys=old['polynomials'];flags=old['flags']
   for poly in polys:
    for mask in list(remain):
     value=poly_value(poly,mask)
     if value<1:del remain[mask]
     else:remain[mask]=min(remain[mask],value)
  else:
   while remain and len(polys)<8 and time.perf_counter()-st<budget:
    seed=max(remain,key=remain.get);ns=counts(f,c,seed)
    eng=SubsetEngine(25,9,ns);z=eng.verify(eng.solve());dp_calls+=1
    if z['bound']>=1:
     flags.append(dict(kind='non_strict_optimal_dp_seed',mask=seed,bound=z['bound']));break
    choices=[min(range(3),key=lambda j:(row['A'],row['B'],row['corrected_C'])[j]) for row in z['rows']]
    fixed=FixedBranch(f,c,z['positions'],choices);poly=fixed.polynomial()
    assert poly_value(poly,seed)==z['bound'];exactchecks+=1
    allmasks=[sum(1<<i for i in low) for low in combinations(f['eligible'],3)] if pilot else [seed]+list(remain)[:2]
    for mask in set(allmasks):
     fv,mv=fixed.evaluate(mask,True);pv=poly_value(poly,mask)
     assert pv==fv and pv>=mv,(f['base'],mask,pv,fv,mv);exactchecks+=1
    checkmask=max(remain,key=lambda mask:poly_value(poly,mask))
    assert independent_fixed(f,c,checkmask,z['positions'],choices)==poly_value(poly,checkmask);independentchecks+=1
    covered=[]
    for mask in list(remain):
     value=poly_value(poly,mask)
     if value<1:covered.append(mask);del remain[mask]
     else:remain[mask]=min(remain[mask],value)
    poly.update(positions=z['positions'],choices=choices,seed_mask=seed,seed_bound=z['bound'],covered_masks=covered,independent_replay_mask=checkmask)
    polys.append(poly)
    assert seed in covered
   if remain and len(polys)>=8:flags.append(dict(kind='eight_layout_cap'))
  out.append(dict(base=f['base'],initial_residual=len(original),covered=len(original)-len(remain),residual_masks=sorted(remain),polynomials=polys,flags=flags,elapsed_seconds=time.perf_counter()-family_start))
  processed+=1
  print('family',f['base'],'initial',len(original),'covered',len(original)-len(remain),'layouts',len(polys),'flags',flags,'sec',time.perf_counter()-family_start,'total',time.perf_counter()-st,flush=True)
  if time.perf_counter()-st>=budget:break
 initial=sum(len(c['residual_colors']) for f,c in targets);covered=sum(f['covered'] for f in out)
 summary=dict(scope=__doc__,pilot=pilot,complete_processed=processed==len(targets),target_families=len(targets),target_colors=initial,processed_families=processed,processed_initial_colors=sum(f['initial_residual'] for f in out),covered_colors=covered,total_remaining_colors=initial-covered,dp_calls_this_run=dp_calls,total_saved_polynomials=sum(len(f['polynomials']) for f in out),fixed_branch_identity_checks=exactchecks,independent_formula_checks=independentchecks,elapsed_seconds=time.perf_counter()-st)
 target='UNIT9_MIXED_Q3_QUADRATIC_PILOT.json' if pilot else 'UNIT9_MIXED_Q3_QUADRATIC.json'
 (P/target).write_text(json.dumps(json_value(dict(summary=summary,families=out)),separators=(',',':'))+'\n')
 print(json.dumps(json_value(summary),indent=2))
if __name__=='__main__':run(len(sys.argv)>1 and sys.argv[1]=='pilot')
