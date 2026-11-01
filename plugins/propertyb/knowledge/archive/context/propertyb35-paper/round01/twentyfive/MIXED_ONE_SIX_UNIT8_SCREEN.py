"""Complete eight-unit catalogue, one degree6 mark and seven degree7 locks.
Every65 large-block family is reconsidered at M35; no old55-feasible shortcut.
Only18 consecutive layouts are tested, then exact low-mark-preserving orbit
transport. This is a bounded diagnostic, not a claim that eight locks exist.
"""
from pathlib import Path
from fractions import Fraction as Q
import json,sys,time
P=Path(__file__).resolve().parent;root=P.parents[3];S=root/'context/propertyb34/round01/high-math';sys.dont_write_bytecode=True
sys.path[:0]=[str(S),str(root/'computations'),str(root/'computations/propertyb33/round01')]
from unit_catalogue import fullblocks,canonical
from bare_layout import BareLayout
from multilock import Profile,json_value
from pure_quota import certificate
st=time.perf_counter();src=json.loads((S/'UNIT_CATALOGUE_8.json').read_text());engines=[BareLayout(25,range(a,a+8)) for a in range(1,19)];domain=[];new=[]
for base,big in enumerate(src['orbits']):
 bs=fullblocks(big,8);high=[7-sum(t>>i&1 for t in bs) for i in range(8)];e0=35-len(bs)-sum(high)
 if min(high)<0 or e0+1<0:continue
 for low in range(8):
  if high[low]<1:continue
  singles=[z-int(i==low) for i,z in enumerate(high)];ns={t:1 for t in bs};ns.update({1<<i:z for i,z in enumerate(singles) if z});ns[0]=e0+1
  assert sum(ns.values())==35 and all(sum(n for t,n in ns.items() if t>>i&1)==(6 if i==low else 7) for i in range(8))
  domain.append(dict(base=base,big=big,low=low,old_empty=e0,counts=ns))
 if e0<0:new.append(dict(base=base,old_empty=e0,new_empty=e0+1,low_labels=[i for i,z in enumerate(high) if z>=1],big=big))
results=[]
def evaluate(eng,ns):
 bare,abc=eng.bound(ns,True);prof=Profile(25,5,eng.pos,ns);cs=[certificate(prof,i) for i in range(8)];loss={eng.pos[i]:cs[i]['loss'] for i in range(8)};v=sum((min(a,b,c-loss.get(k,Q())) for k,(a,b,c) in enumerate(abc,1)),Q());return v,bare
for z in domain:
 best=None;bestbare=None
 for eng in engines:
  v,bare=evaluate(eng,z['counts'])
  if best is None or v<best['bound']:best=dict(bound=v,positions=eng.pos)
  if bestbare is None or bare<bestbare['bound']:bestbare=dict(bound=bare,positions=eng.pos)
 key,m=canonical(z['big'],8,extra=[int(i==z['low']) for i in range(8)],with_perm=True);colored=(key,m[z['low']]);cp=[0]*8
 for i,j in enumerate(m):cp[j]=best['positions'][i]
 results.append(dict(**z,**best,best_bare=bestbare,canonical_large=key,canonical_low=m[z['low']],old_to_canonical=m,canonical_positions=cp))
 if time.perf_counter()-st>9:break
complete=len(results)==len(domain);groups={}
for j,z in enumerate(results):groups.setdefault((tuple(z['canonical_large']),z['canonical_low']),[]).append(j)
transported=[];orbits=[]
for k,js in groups.items():
 witness=min(js,key=lambda j:results[j]['bound']);w=results[witness];members=[]
 for j in js:
  z=results[j];pos=[w['canonical_positions'][z['old_to_canonical'][i]] for i in range(8)];v,bare=evaluate(BareLayout(25,pos),z['counts']);assert v==w['bound'];members.append(z['low']);transported.append(dict(base=z['base'],low=z['low'],bound=v,bare=bare,positions=pos,counts=z['counts'],from_low=w['low'],canonical_large=k[0],canonical_low=k[1]))
 orbits.append(dict(base=w['base'],canonical_large=k[0],canonical_low=k[1],low_orbit=sorted(members),bound=w['bound'],witness_low=w['low'],positions=w['positions']))
summary=dict(scope=__doc__,source_catalogue_complete=src['complete'],source_families=len(src['orbits']),feasible_families=len({z['base'] for z in domain}),feasible_marked_inputs=len(domain),screen_complete=complete,processed=len(results),strict_before_transport=sum(z['bound']<1 for z in results),strict_after_transport=sum(z['bound']<1 for z in transported),residual_after_transport=sum(z['bound']>=1 for z in transported),colored_orbits=len(orbits),residual_colored_orbits=sum(z['bound']>=1 for z in orbits),maximum=max(z['bound'] for z in transported),elapsed_seconds=time.perf_counter()-st)
out=dict(summary=summary,newly_feasible_old_negative_empty=new,residual_orbits=[z for z in orbits if z['bound']>=1],orbits=orbits,results=transported)
(P/'MIXED_ONE_SIX_UNIT8_SCREEN.json').write_text(json.dumps(json_value(out),indent=2)+'\n');print(json.dumps(json_value(summary),indent=2));print('residual_orbits',json.dumps(json_value(out['residual_orbits']),indent=2))
