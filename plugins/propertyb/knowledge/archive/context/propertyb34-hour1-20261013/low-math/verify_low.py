from probe import *
start=time.time();out=[]
for ds,lam in [((5,d),1) for d in range(5,9)]+[((6,d),a) for d in (6,7) for a in range(1,7)]+[((6,8),1)]:
 r=best(20,ds,(lam,));assert r['bound']<1
 stubs=[frozenset(i+1 for i in range(2) if t&(1<<i)) for t,c in r['counts'].items() for _ in range(c)]
 independent=independent_rows(20,r['pos'],stubs)
 for row,other in zip(r['rows'],independent):
  for term in ('A','B','C'):assert row[term]==other[term]
  assert row['bound']==min(other['A'],other['B'],other['C']-row['deduction'])
 r['independent_ABC_check']=True;out.append(r)
 print(ds,lam,r['pos'],r['bound'])
Path(__file__).with_name('LOW_DEGREE_SIX_VERIFIED.json').write_text(json.dumps(json_value(dict(scope='17 local formula witnesses; independent ABC comparison; no Lean claim',seconds=time.time()-start,cases=out)),indent=2))
