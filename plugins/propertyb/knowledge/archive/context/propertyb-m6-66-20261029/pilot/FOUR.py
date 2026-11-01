"""Exact M65 four-unit-lock exploratory profiles. Requires structural selection lemma externally."""
import importlib.util,json,time,itertools
from pathlib import Path
P=Path(__file__).resolve().parent;ROOT=P.parents[2]
spec=importlib.util.spec_from_file_location('cert',ROOT/'propertyB_small_k/propertyB_m6_certificate.py');c=importlib.util.module_from_spec(spec);spec.loader.exec_module(c);c.M=65

def clique_partitions(s):
 full=(1<<(s*(s-1)//2))-1;pairs=list(itertools.combinations(range(s),2));pidx={p:i for i,p in enumerate(pairs)}
 blocks=[]
 for n in range(2,s+1):
  for vs in itertools.combinations(range(s),n):
   edges=sum(1<<pidx[p] for p in itertools.combinations(vs,2));mask=sum(1<<j for j in vs);blocks.append((edges,mask))
 out=[]
 def rec(left,chosen):
  if not left:out.append(tuple(sorted(chosen)));return
  low=left&-left
  for es,mask in blocks:
   if es&low and es&left==es:rec(left^es,chosen+[mask])
 rec(full,[])
 assert len(set(out))==len(out)
 return sorted(out)
def make_ell(ds,blocks):
 s=len(ds);ell={b:1 for b in blocks}
 for j,d in enumerate(ds):ell[1<<j]=d-sum(bool(b&(1<<j)) for b in blocks)
 ell[0]=65-sum(ell.values());assert min(ell.values())>=0
 return {t:n for t,n in ell.items() if n}
def main():
 start=time.process_time();patterns=clique_partitions(4);assert len(patterns)==6
 rows=[];structural=[]
 for v,D in [(40,10),(41,9),(42,9),(43,9)]:
  d0=c.ceilings(v-1,5);Z=(D+1)*v-390;T=5*(D+1)-v+2
  rmin=c.ceilings(Z,D+1-d0);assert rmin>=4 and 20*Z>3*T*T
  structural.append(dict(v=v,D=D,d0=d0,rmin=rmin,Z=Z,T=T,strict_margin=20*Z-3*T*T))
  pos=tuple(range(v//2-1,v//2+3))
  for ds in itertools.combinations_with_replacement(range(d0,D+1),4):
   for blocks in patterns:
    ell=make_ell(ds,blocks)
    assert all(sum(n for t,n in ell.items() if t&(1<<j))==ds[j] for j in range(4))
    assert all(sum(n for t,n in ell.items() if t&(1<<i) and t&(1<<j))==1 for i,j in itertools.combinations(range(4),2))
    u=c.profile_bound(v,pos,ell)
    rows.append(dict(v=v,degrees=ds,blocks=blocks,ell=ell,positions=pos,U=str(u),approx=float(u),pass_strict=u<1))
 assert len(rows)==132 and all(r['pass_strict'] for r in rows)
 out=dict(structural=structural,scope='all sorted degree tuples and all labelled K4 clique partitions; central continuous four locks; independent 4-lock selection lemma required',profiles=len(rows),patterns=patterns,cpu_seconds=time.process_time()-start,rows=rows,failures=[r for r in rows if not r['pass_strict']])
 (P/'FOUR.json').write_text(json.dumps(out,indent=2));print('CPU',out['cpu_seconds'],'patterns',len(patterns))
 for v in (40,41,42,43):
  rs=[r for r in rows if r['v']==v];print(v,len(rs),sum(not r['pass_strict'] for r in rs),max(r['approx'] for r in rs))
if __name__=='__main__':main()
