"""Bounded physical DP census; no SAT solver and no legacy generator imports."""
from itertools import combinations
from pathlib import Path
import hashlib,json,platform,time
ROOT=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(name):
 rows=(ROOT/name).read_text().splitlines();color={}
 for row in rows[1:]:
  a,b,c,value=row.split();color[int(a),int(b),int(c)]=value in ('1','R')
 n=max(max(t) for t in color);assert set(color)==set(combinations(range(1,n+1),3))
 return n,color
def lengths(n,color,red):
 reach={(s,s,t):1<<2 for s,t in combinations(range(1,n+1),2)}
 for last in range(2,n+1):
  for first in range(1,last):
   for previous in range(first,last):
    bits=reach.get((first,previous,last),0)
    if not bits:continue
    for new in range(last+1,n+1):
     if color[previous,last,new]==red:
      key=(first,last,new);reach[key]=reach.get(key,0)|(bits<<1)
 out={e:0 for e in combinations(range(1,n+1),2)}
 for (s,p,t),bits in reach.items():out[s,t]|=bits
 return {e:[k for k in range(2,n+1) if bits&(1<<k)] for e,bits in out.items()}
def audit(name,n,color,construction):
 vertices=range(1,n+1)
 packets=all(sum(x!=y for x,y in zip(bits,bits[1:]))<=1 for q in combinations(vertices,4)
             for bits in [[color[t] for t in combinations(q,3)]])
 red,blue=lengths(n,color,True),lengths(n,color,False)
 rs={s for (s,t),ls in red.items() if 6 in ls};re={t for (s,t),ls in red.items() if 6 in ls}
 bs={s for (s,t),ls in blue.items() if 5 in ls};be={t for (s,t),ls in blue.items() if 5 in ls}
 H=bs&be;I=set(vertices)-(rs|re|bs|be)
 maxR=max(max(ls) for ls in red.values());maxB=max(max(ls) for ls in blue.values())
 weak=[(e,r,b) for e in red for r in red[e] for b in blue[e] if r+b>=9]
 checks=dict(packets=packets,no_R7=maxR<=6,no_B6=maxB<=5,no_weak7=not weak)
 result=dict(case=name,n=n,h=len(H),i=len(I),h_minus_i=len(H)-len(I),H=sorted(H),I=sorted(I),
             R6_sources=sorted(rs),R6_terminals=sorted(re),B5_sources=sorted(bs),B5_terminals=sorted(be),
             max_R=maxR,max_B=maxB,checks=checks,construction=construction)
 assert all(checks.values()),result
 case=ROOT/name;case.mkdir()
 with (case/'colors.tsv').open('w') as f:
  f.write('a\tb\tc\tcolor\n')
  for t in sorted(color):f.write('\t'.join(map(str,t))+('\tR\n' if color[t] else '\tB\n'))
 (case/'endpoint-lengths.json').write_text(json.dumps([dict(pair=e,R=red[e],B=blue[e]) for e in red],indent=2)+'\n')
 result['color_sha256']=sha(case/'colors.tsv')
 (case/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 return result
def red_join(a,b):
 na,ca=a;nb,cb=b;n=na+nb;out={}
 for t in combinations(range(1,n+1),3):
  out[t]=ca[t] if t[-1]<=na else cb[tuple(v-na for v in t)] if t[0]>na else True
 return n,out
def main():
 assert platform.system()=='Linux';assert not (ROOT/'summary.json').exists()
 begin=time.monotonic();results=[]
 inputs={name:load(name) for name in ('actual21.tsv','weak6-21.tsv','standard25.tsv')}
 n,c=inputs['standard25.tsv'];swapped=(n,{t:not red for t,red in c.items()})
 blue5=(5,{t:False for t in combinations(range(1,6),3)})
 cases=[('actual21',inputs['actual21.tsv'],'prior actual H internal B5 witness'),
        ('weak6-21',inputs['weak6-21.tsv'],'prior actual H weak6 witness'),
        ('standard25',inputs['standard25.tsv'],'original archived exact color table'),
        ('swapped25',swapped,'color swap of standard25'),
        ('join30-right',red_join(swapped,blue5),'all-red join swapped25 < all-blue5'),
        ('join30-left',red_join(blue5,swapped),'all-red join all-blue5 < swapped25')]
 for name,(n,c),description in cases:
  results.append(audit(name,n,c,description))
  found=results[-1]['h_minus_i']>=11
  summary=dict(cases=results,found=found,seconds=time.monotonic()-begin,
               definition='h=|SrcB5 intersect EndB5|; i=complement of all four R6/B5 source/end roles',
               input_bindings={name:sha(ROOT/name) for name in inputs})
  (ROOT/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
  if found:break
 (ROOT/'done.json').write_text(json.dumps(dict(found=found,cases=len(results)))+'\n')
 print(json.dumps(summary))
if __name__=='__main__':main()
