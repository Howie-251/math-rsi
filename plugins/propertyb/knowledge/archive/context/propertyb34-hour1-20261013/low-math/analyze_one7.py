from probe import *
source=json.load(open(Path(__file__).with_name('QUAD_ONE7.json')))['cases'];duals={r['index']:r for r in json.load(open(Path(__file__).with_name('DUAL_REFINEMENT.json')))['cases'] if r['source']=='QUAD_ONE7.json'}
triples=json.load(open(Path(__file__).with_name('TRIPLE_SCAN.json')))
lookup={(tuple(r['ds']),tuple(r['ls']),r['t']):Fraction(r['bound']) for r in triples}
left=[]
for idx,r in enumerate(source):
 if Fraction(r['bound'])<1 or (idx in duals and Fraction(duals[idx]['bound'])<1):continue
 counts={int(t):c for t,c in r['counts'].items()}
 skip=False
 for a,b in combinations(range(1,4),2):
  ls=tuple(sum(c for t,c in counts.items() if t&mask==mask) for mask in (1|(1<<a),1|(1<<b),(1<<a)|(1<<b)))
  tm=1|(1<<a)|(1<<b);tri=sum(c for t,c in counts.items() if t&tm==tm)
  if lookup[((7,8,8),ls,tri)]<1:skip=True
 # Three unit degree-eight points also color.
 ls888=tuple(sum(c for t,c in counts.items() if t&mask==mask) for mask in (6,10,12))
 tri888=sum(c for t,c in counts.items() if t&14==14)
 if lookup[((8,8,8),tuple(sorted(ls888)),tri888)]<1:skip=True
 if not skip:left.append(dict(index=idx,**r,dual=duals.get(idx)))
print('remaining',len(left))
canon={}
for r in left:
 c={int(t):n for t,n in r['counts'].items()};forms=[]
 for pp in permutations((1,2,3)):
  perm=(0,)+pp
  forms.append(tuple(sorted((sum(1<<perm[i] for i in range(4) if t&(1<<i)),n) for t,n in c.items() if n)))
 key=min(forms);canon.setdefault(key,[]).append(r['index'])
for key,ids in canon.items():print(ids,dict(key))
Path(__file__).with_name('ONE7_REMAINING.json').write_text(json.dumps(json_value(dict(cases=left,canonical=[dict(indices=ids,counts=dict(key)) for key,ids in canon.items()])),indent=2))
