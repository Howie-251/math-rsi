"""Rare-low-unit branch: x degree6 plus minimum-energy four degree8 unit neighbours, same actual partition."""
from pair_pilot import *
sys.path.insert(0,str(ROOT/'context/propertyb35-paper/round01/twentyfour'))
from fourlock_pilot import inventory
GRAPHS={'empty':{},'one':{(0,1):1},'two_matching':{(0,1):1,(2,3):1},'path3':{(0,1):1,(1,2):1},'double':{(0,1):2},'triangle':{(0,1):1,(0,2):1,(1,2):1},'path4':{(0,1):1,(1,2):1,(2,3):1},'double_one':{(0,1):2,(2,3):1}}
def parts(xs):
 if not xs:yield [];return
 x,*ys=xs
 for pp in parts(ys):
  yield [(x,)]+pp
  for j,b in enumerate(pp):yield pp[:j]+[tuple(sorted((x,)+b))]+pp[j+1:]
def domain(name):
 ed=GRAPHS[name]
 for pp in parts(list(range(4))):
  pairs={(i,j):1+ed.get((i,j),0)-int(any(i in b and j in b for b in pp)) for i,j in itertools.combinations(range(4),2)}
  for outside in inventory(4,[7]*4,pairs,29):
   ns={m:0 for m in range(32)}
   for m,n in outside.items():ns[m<<1]=n
   ns[1]=6-len(pp)
   for b in pp:ns[1|sum(1<<(i+1) for i in b)]=1
   yield pp,ns

def main():
 st=time.time();pos=set()
 for k in range(1,20):
  seq=tuple(range(k,k+5))
  for i in range(5):pos.add((seq[i],)+tuple(v for j,v in enumerate(seq) if i!=j))
 for seq in [(1,2,11,12,13),(1,6,11,16,21)]:
  for i in range(5):pos.add((seq[i],)+tuple(v for j,v in enumerate(seq) if i!=j))
 out=[]
 for name in GRAPHS:
  dom=list(domain(name));print('domain',name,len(dom),flush=True)
  # First pilot: no noncenter >=3 traces.
  dom=[(pp,ns) for pp,ns in dom if not any(n and not(m&1) and m.bit_count()>=3 for m,n in ns.items())]
  for pp,ns in dom:
   z=min((evaluate(23,ns,p) for p in pos),key=lambda z:z['bound'])
   out.append(dict(graph=name,partition=pp,counts=ns,bound=z['bound'],strict=z['strict'],positions=z['positions']))
  rr=[z for z in out if z['graph']==name];print('pilot',name,len(rr),sum(z['strict'] for z in rr),'minmax',min(z['bound'] for z in rr),max(z['bound'] for z in rr),flush=True)
 (HERE/'FOUR_EIGHT_STAR.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed_seconds=time.time()-st,profiles=out)),indent=2)+'\n')
 print('seconds',time.time()-st)
if __name__=='__main__':main()
