from probe import *
start=time.time();out=[]
# Every required strong pair, degree-seven triple with at least one 3,
# and degree-7/7/8 triple outside its explicit residual set.
for ds in [(7,7),(7,8)]:
 for lam in range(4,8):out.append(best(20,ds,(lam,)))
triples=json.load(open(Path(__file__).with_name('TRIPLE_SCAN.json')))
for r in triples:
 if (r['ds']==[7,7,7] and max(r['ls'])==3) or (r['ds']==[7,7,8] and ((r['ls'][1]!=r['ls'][2]) or max(r['ls'][1:])==3)):
  rr=calc(r['v'],r['ds'],r['ls'],r['t'],r['pos']);assert rr['bound']<1;out.append(rr)
for f in ['QUAD_TWO.json','QUAD_MIXED.json']:
 source=json.load(open(Path(__file__).with_name(f)))['cases']
 for r in source:
  if f=='QUAD_TWO.json' or r['ds']==[7,7,7,8]:
   p=Profile(20,5,tuple(r['pos']),{int(k):v for k,v in r['counts'].items()});cs=[certificate(p,i) for i in range(4)]
   rs=rows(p,deductions={p.positions[i]:cs[i]['loss'] for i in range(4)})
   out.append(dict(v=20,ds=[7]*4 if f=='QUAD_TWO.json' else r['ds'],ls=r.get('ls',[2]*6),t4=r['t4'],t3=r['t3'],pos=p.positions,counts=p.counts,cs=cs,rows=rs,bound=total_bound(rs)))
for r in out:
 assert r['bound']<1
 stubs=[frozenset(i+1 for i in range(len(r['ds'])) if int(t)&(1<<i)) for t,c in r['counts'].items() for _ in range(c)]
 indep=independent_rows(20,r['pos'],stubs)
 for a,b in zip(r['rows'],indep):
  for term in ('A','B','C'):assert a[term]==b[term]
 r['independent_ABC_check']=True
Path(__file__).with_name('SEVEN_MANY_VERIFIED.json').write_text(json.dumps(json_value(dict(seconds=time.time()-start,cases=out)),indent=2))
print('count',len(out),'maximum',max(r['bound'] for r in out),'seconds',time.time()-start)
