from pilot import *
start=time.time();old=json.loads((HERE/'UNIT_FOUR_DP.json').read_text())['cases']
def canon(p):return tuple(sorted(tuple(sorted(B)) for B in p))
def proj(part,S):
 m={i:j for j,i in enumerate(S)};return canon([[m[i] for i in B if i in m] for B in part if any(i in m for i in B)])
allowed={(canon(r['partition']),tuple(r['triples']),r['four']) for r in old if r['neighbor_degrees']==[10]*4 and not r['strict']}
triples=list(combinations(range(5),3));subs=list(combinations(range(5),4));tb=[sum(1<<i for i in S) for S in triples];qb=[sum(1<<i for i in S) for S in subs];domain=[]
for part in parts(5):
 if max(map(len,part))>4:continue
 for ts in product(range(2),repeat=10):
  tm=dict(zip(triples,ts))
  if any((proj(part,S),tuple(tm[t] for t in combinations(S,3)),0) not in allowed for S in subs):continue
  high={**dict(zip(tb,ts)),**dict.fromkeys(qb,0),31:0}
  ns=recover(7,[10]*5,[3]*10,part,high)
  if ns is not None:domain.append(dict(neighbor_degrees=[10]*5,neighbor_codegrees=[3]*10,partition=part,triples=ts,four=[0]*5,five=0,counts=ns))
print('domain',len(domain),flush=True);out=[]
for idx,r in enumerate(domain):
 eng=SubsetEngine(20,6,r['counts']);z=eng.verify(eng.solve());z.update(r);z.update(source_id=idx,strict=z['bound']<1);out.append(z);print(idx,z['bound'],flush=True)
(HERE/'FIVE_TENS.json').write_text(json.dumps(json_value(dict(cases=out,complete=True,elapsed_seconds=time.time()-start)),indent=2)+'\n')
