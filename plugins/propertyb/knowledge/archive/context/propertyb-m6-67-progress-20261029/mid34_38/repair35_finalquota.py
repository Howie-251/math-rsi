exec((__import__('pathlib').Path(__file__).resolve().parent.parent/'tail39_41/kernel.py').read_text())
import importlib.util
spec=importlib.util.spec_from_file_location('dp',P.parent/'small31_33/diagnose.py');dp=importlib.util.module_from_spec(spec);spec.loader.exec_module(dp)
def component_delete(v,pos,ell,j):
 bit=1<<j;other=((1<<len(pos))-1)^bit;typ=[T for T,n in ell.items() if n and T&bit];best=F(0);cells=[]
 for ai,T in enumerate(typ):
  for U in typ[ai:]:
   cap=c.C(ell[T],2) if T==U else ell[T]*ell[U]
   if cap:cells.append((T|U,cap,c.weight(v,pos,pos[j],T,U)+c.weight(v,pos,pos[j],U,T)))
 for R in range(1<<len(pos)):
  if R&~other:continue
  f=sum(n for T,n in ell.items() if T&bit and not T&R);q=dp.quota(v-R.bit_count(),f);cost=F(0)
  for _,cap,w in sorted((cell for cell in cells if not cell[0]&R),key=lambda z:z[2]):
   take=min(q,cap);cost+=take*w;q-=take
  assert q==0
  best=max(best,cost)
 return best
c.bad_pair_deletion=component_delete
start=time.process_time();rows=[]
for r in json.loads((P/'MIN10_35.json').read_text())['failures']:
 ell={}
 for b in r['blocks']:ell[b]=ell.get(b,0)+1
 for j,d in enumerate(r['degrees']):ell[1<<j]=d-sum(n for b,n in ell.items() if b&(1<<j))
 ell[0]=66-sum(ell.values());u=c.profile_bound(35,tuple(r['positions']),ell)
 rows.append(r|dict(U=str(u),strict=u<1))
out=dict(rows=rows,failures=[r for r in rows if not r['strict']],cpu_seconds=time.process_time()-start)
(P/'REPAIR35_FINALQUOTA.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'],'remaining',len(out['failures']));print(out['failures'])
