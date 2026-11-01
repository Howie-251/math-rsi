"""Independent injection replay and complete trace-domain reconstruction, v36–38."""
import ast,json,time,itertools
from functools import lru_cache
from fractions import Fraction as Q
from math import comb,factorial
from pathlib import Path
OUT=Path(__file__).resolve().parent;BASE=OUT.parent;ROOT=BASE.parents[1];MID=BASE/'mid34_38'
SOURCE=ROOT/'context/propertyb-m6-66-20261029/independent/check.py'
ns=dict(Q=Q,lru_cache=lru_cache,factorial=factorial,comb=comb)
ff=[n for n in ast.parse(SOURCE.read_text()).body if isinstance(n,ast.FunctionDef) and n.name in {'ceildiv','fall','probs'}]
exec(compile(ast.Module(body=ff,type_ignores=[]),str(SOURCE),'exec'),ns);prob=ns['probs']
# This graph quota is a declared import; its author is this reviewer.
import importlib.util
spec=importlib.util.spec_from_file_location('linkquota',BASE/'small31_33/diagnose.py');linkquota=importlib.util.module_from_spec(spec);spec.loader.exec_module(linkquota)

def deduct(v,pos,ell,j,use_component):
 cells=[];typ=[T for T in ell if T>>j&1]
 for i,T in enumerate(typ):
  for U in typ[i:]:
   cap=comb(ell[T],2) if T==U else ell[T]*ell[U]
   if cap:cells.append((prob(v,pos,pos[j],T,U)+prob(v,pos,pos[j],U,T),cap,T|U))
 out=Q(0)
 for R in range(1<<len(pos)):
  if R>>j&1:continue
  f=sum(n for T,n in ell.items() if T>>j&1 and not T&R);N=v-1-R.bit_count()
  q=linkquota.quota(N+1,f) if use_component else max(0,-(-(5*f-N)//4));cost=Q(0)
  for w,cap,U in sorted(cells):
   if U&R:continue
   z=min(q,cap);q-=z;cost+=z*w
  assert q==0
  out=max(out,cost)
 return out

def joint_deduct(v,pos,ell,j):
 typ=[T for T in ell if T>>j&1];cells=[]
 for i,T in enumerate(typ):
  for U in typ[i:]:
   cap=comb(ell[T],2) if T==U else ell[T]*ell[U]
   if cap:cells.append((prob(v,pos,pos[j],T,U)+prob(v,pos,pos[j],U,T),cap,T|U))
 Rs=[R for R in range(1<<len(pos)) if not R>>j&1]
 needs=[linkquota.quota(v-R.bit_count(),sum(n for T,n in ell.items()if T>>j&1 and not T&R))for R in Rs]
 positive=[]
 for w,cap,U in cells:
  eligible=tuple(not U&R for R in Rs)
  if w==0:needs=[max(0,q-cap*hit)for q,hit in zip(needs,eligible)]
  else:positive.append((w,cap,eligible))
 positive.sort(reverse=True)
 @lru_cache(None)
 def rec(i,state):
  if not any(state):return Q(0)
  if i==len(positive):return None
  w,cap,hits=positive[i];upper=min(cap,max([q for q,h in zip(state,hits)if h]or[0]));best=None
  for z in range(upper+1):
   rest=tuple(max(0,q-z*h)for q,h in zip(state,hits));val=rec(i+1,rest)
   if val is not None:
    val+=z*w
    if best is None or val<best:best=val
  return best
 result=rec(0,tuple(needs));assert result is not None
 return result

def bound(v,pos,ell,use_component=False,joint=False):
 pos=tuple(pos);assert len(set(pos))==len(pos) and all(1<=h<=v for h in pos);D={pos[j]:(joint_deduct(v,pos,ell,j) if joint else deduct(v,pos,ell,j,use_component)) for j in range(len(pos))};total=Q(0)
 for h in range(1,v+1):
  A=sum(n*prob(v,pos,h,T)[0] for T,n in ell.items());B=sum(n*prob(v,pos,h,T)[1] for T,n in ell.items())
  C=sum(n*(m-(T==U))*prob(v,pos,h,T,U) for T,n in ell.items() for U,m in ell.items())
  assert C>=D.get(h,0);total+=min(A,B,C-D.get(h,0))
 return total

def ell_for(ds,blocks):
 ell={}
 for b in blocks:ell[b]=ell.get(b,0)+1
 for j,d in enumerate(ds):ell[1<<j]=d-sum(n for b,n in ell.items() if b>>j&1)
 ell[0]=66-sum(ell.values());assert min(ell.values())>=0
 return{t:n for t,n in ell.items() if n}

def pairmult(ds,blocks):
 return tuple(sum(bool(b>>i&1 and b>>j&1) for b in blocks) for i,j in itertools.combinations(range(len(ds)),2))

@lru_cache(None)
def clique_decompositions(target,s=4):
 pairs=list(itertools.combinations(range(s),2));cliques=[]
 for mask in range(1,1<<s):
  if mask.bit_count()<2:continue
  used=tuple(k for k,(i,j) in enumerate(pairs) if mask>>i&1 and mask>>j&1);cliques.append((mask,used))
 @lru_cache(None)
 def rec(state):
  if not any(state):return frozenset({()})
  pivot=next(i for i,n in enumerate(state) if n)
  out=set()
  for b,used in cliques:
   if pivot not in used or any(state[k]==0 for k in used):continue
   nxt=list(state)
   for k in used:nxt[k]-=1
   out.update(tuple(sorted((b,*tail))) for tail in rec(tuple(nxt)))
  return frozenset(out)
 return rec(tuple(target))

def four_domain(ds,known,d4s,parent_pair=None):
 oldpairs=list(itertools.combinations(range(3),2));p4=list(itertools.combinations(range(4),2));out=set()
 for d4 in d4s:
  for double in (-1,0,1,2):
   target=[1]*6
   if parent_pair is not None:target[p4.index(oldpairs[parent_pair])]=2
   if double>=0:target[p4.index((double,3))]=2
   for blocks in clique_decompositions(tuple(target)):
    rest=tuple(sorted(b&7 for b in blocks if (b&7).bit_count()>=2))
    if rest!=tuple(sorted(known)):continue
    ell_for((*ds,d4),blocks)
    out.add((d4,double,blocks))
 return out

def main():
 start=time.process_time();A=json.loads((MID/'ADAPTIVE_COMPONENT.json').read_text());F=json.loads((MID/'FOUR_REPAIR.json').read_text());M=json.loads((MID/'MIN10_36.json').read_text());W=json.loads((MID/'WEDGE36.json').read_text());WF=json.loads((MID/'WEDGE_FOUR36.json').read_text())
 result=[];replay=[]
 # Independently enumerate every original adaptive minimum/partner branch.
 for v in (36,37,38):
  expected=set()
  for d in range(-(-(v-1)//5),396//v+1):
   n=2*(v-1)-5*d
   for e in range(d,d+(396-v*d)//n+1):expected.add((d,e))
  got={(b['d'],b['e']) for b in A['branches'] if b['v']==v};assert expected==got
  for b in A['branches']:
   if b['v']!=v:continue
   d,e=b['d'],b['e']
   if b['status']=='pool_gap':assert v==36 and(d,e)in((10,11),(11,11));continue
   rows=[r for r in A['rows'] if r['v']==v and r['degrees'][:2]==[d,e]]
   if b['status']=='two_pass':targets=[r for r in rows if len(r['degrees'])==2];assert len(targets)==1
   else:
    n=2*(v-1)-5*d;t=n-1-(5*e-(v-1));fmax=e+(396-v*d-n*(e-d))//t
    targets=[r for r in rows if len(r['degrees'])==3]
    assert {(tuple(r['degrees']),tuple(r['blocks'])) for r in targets}=={((d,e,f),bs)for f in range(e,fmax+1)for bs in((3,5,6),(7,))}
   if len(targets[0]['degrees'])==3:
    failed={(tuple(r['degrees']),tuple(r['blocks']))for r in targets if not r['strict']}
    assert failed=={(tuple(r['degrees']),tuple(r['blocks']))for r in b.get('failures',[])}
    if v==36:assert not failed
   for r in targets:
    assert sorted(r['assigned'])==sorted(r['degrees'])
    if not r['strict']:continue
    ell=ell_for(r['assigned'],r['blocks']);u=bound(v,r['positions'],ell,True)
    if u>=1:u=bound(v,r['positions'],ell,True,True)
    assert u<1,(r,u)
    replay.append((v,'adaptive',str(u),r['U']))
 # All 27 failing adaptive triple domains must be repaired completely.
 failures=[r for b in A['branches'] if b['v']in(37,38) for r in b.get('failures',[])]
 assert len(failures)==27
 for parent in failures:
  v=parent['v'];ds=tuple(parent['degrees']);delta=ds[0];E=5*sum(ds)-3*(v-1);pool=v-3-E//2;D=delta+(396-sum(ds)-(v-3)*delta)//pool
  domain=four_domain(ds,parent['blocks'],range(delta,D+1))
  rr=[r for r in F['rows'] if r['v']==v and tuple(r['parent_degrees'])==ds and r['parent_blocks']==parent['blocks']]
  assert {(r['degrees'][3],r['double'],tuple(sorted(r['blocks'])))for r in rr}==domain
  for r in rr:
   u=bound(v,r['positions'],ell_for(r['degrees'],r['blocks']));assert u==Q(r['U'])<1
   replay.append((v,'four',str(u),r['U']))
 # v36 min10 weak-wedge complete48 three types and all failedfour domains.
 expected={(a,b,double,tau) for a,b in itertools.combinations_with_replacement(range(10,13),2) for double in(-1,0,1,2)for tau in(0,1)}
 assert {(r['degrees'][1],r['degrees'][2],r['double'],r['tau'])for r in M['three']}==expected
 for parent in M['three']:
  ds=tuple(parent['degrees']);double=parent['double'];tau=parent['tau'];ell=ell_for(ds,parent['blocks'])
  if parent['strict']:
   u=bound(36,parent['positions'],ell);assert u==Q(parent['U'])<1;replay.append((36,'min10_three',str(u),parent['U']));continue
  E=5*sum(ds)-105-2*(double>=0);pool=33-E//2;D=10+(396-sum(ds)-330)//pool
  domain=four_domain(ds,parent['blocks'],range(10,D+1),double if double>=0 else None)
  rr=[r for r in M['four']if tuple(r['degrees'][:3])==ds and r['parent_double']==double and r['parent_tau']==tau]
  assert {(r['degrees'][3],r['newdouble'],tuple(sorted(r['blocks'])))for r in rr}==domain
  for r in rr:
   u=bound(36,r['positions'],ell_for(r['degrees'],r['blocks']));assert u==Q(r['U'])<1;replay.append((36,'min10_four',str(u),r['U']))
 # v36 regular11 weak-wedge lambda1 directly; lambda2 fourth complete31 traces.
 assert {(r['lam_yz'],r['triple'])for r in W['rows']}=={(l,t)for l in(1,2)for t in(0,1)}
 for r in W['rows']:
  l,t=r['lam_yz'],r['triple'];blocks=[7]*t+[3]*(1-t)+[5]*(1-t)+[6]*(l-t)
  if l==1:
   u=bound(36,r['positions'],ell_for((11,11,11),blocks));assert u==Q(r['U'])<1;replay.append((36,'regular_three',str(u),r['U']));continue
  domain=four_domain((11,11,11),blocks,[11],2)
  rr=[a for a in WF['rows']if a['parent_tau']==t]
  assert{(11,a['double'],tuple(sorted(a['blocks'])))for a in rr}==domain
  for a in rr:
   u=bound(36,a['positions'],ell_for(a['degrees'],a['blocks']));assert u==Q(a['U'])<1;replay.append((36,'regular_four',str(u),a['U']))
 for v in(36,37,38):
  rr=[r for r in replay if r[0]==v];result.append(dict(v=v,replayed=len(rr),maximum=str(max(Q(r[2])for r in rr))))
 out=dict(status='PASS',scope='Independent complete local domains and independent injection arithmetic for36–38; selection proof reviewed separately.',declared_imports=['original minimalcounterexample reduction','component quota lemma not independently audited here; reviewer authored it'],rows=result,cpu_seconds=time.process_time()-start)
 (OUT/'REPLAY.json').write_text(json.dumps({'columns':['v','branch','independent_U','submitted_U'],'rows':replay},indent=2))
 out['comparison']={'equal':sum(Q(r[2])==Q(r[3])for r in replay),'independent_stronger':sum(Q(r[2])<Q(r[3])for r in replay),'independent_weaker_but_strict':sum(Q(r[2])>Q(r[3])for r in replay)}
 (OUT/'RESULTS.json').write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
if __name__=='__main__':main()
