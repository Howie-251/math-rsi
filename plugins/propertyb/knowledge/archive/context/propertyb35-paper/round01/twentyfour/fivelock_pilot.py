"""Complete necessary five-seven matching-lock inventories, with consecutive identity-role layouts only."""
from fourlock_pilot import *
def main():
 st=time.time();out=[]
 for k in range(3):
  pairs={(i,j):1+int((i,j) in [(0,1),(2,3)][:k]) for i in range(5) for j in range(i+1,5)}
  nslist=list(inventory(5,[7]*5,pairs));pos=[tuple(range(q,q+5)) for q in range(1,21)]
  for ns in nslist:
   z=min((evaluate(24,ns,p) for p in pos),key=lambda z:z['bound'])
   out.append(dict(matching_edges=k,counts=ns,bound=z['bound'],strict=z['strict'],positions=z['positions']))
  rr=[z for z in out if z['matching_edges']==k]
  print('matching',k,'profiles',len(rr),'strict',sum(z['strict'] for z in rr),'min',min(z['bound'] for z in rr),'max',max(z['bound'] for z in rr),flush=True)
 (HERE/'FIVELOCK_PILOT.json').write_text(json.dumps(json_value(dict(scope=__doc__,elapsed_seconds=time.time()-st,profiles=out)),indent=2)+'\n')
if __name__=='__main__':main()
