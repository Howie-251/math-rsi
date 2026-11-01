from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
s=(ROOT/'context/propertyb34/round01/twenty-lean/generate_two_quad.py').read_text()
a=s.index('raw=json.load');b=s.index('D=[]',a)
s=s[:a]+'''from itertools import permutations
source=json.load(open(ROOT/'context/propertyb34-hour1-20261013/low-math/SEVEN_ONE_VERIFIED.json'))['witnesses']
groups={}
def canonical(r):
 counts={int(k):v for k,v in r['counts'].items()}
 choices=[]
 for pp in permutations((1,2,3)):
  perm=(0,)+pp;out=[0]*16
  for m,n in counts.items():out[sum(1<<perm[j] for j in range(4) if m>>j&1)]=n
  choices.append(tuple(out))
 return min(choices)
for r in source:
 if r['ds']!=[7,8,8,8]:continue
 groups.setdefault(canonical(r),[]).append(r)
raw=[]
for group in groups.values():
 r=dict(min(group,key=lambda r:(r['kind']=='dual',F(r['bound']))))
 counts={int(k):v for k,v in r['counts'].items()}
 r['ls']=[sum(n for m,n in counts.items() if m&p==p) for p in (3,5,9,6,10,12)]
 r['t3']=[counts.get(m,0) for m in (7,11,13,14)];r['t4']=counts.get(15,0)
 r['certificate_kind']='pure' if r['kind']=='pure' else 'avoided_dual'
 raw.append(r)
''' +s[b:]
s=s.replace("[7,7,8,8]", "[7,8,8,8]").replace('len(dual)<=2','len(dual)<=3').replace('(2-len(dual))','(3-len(dual))').replace('len(D)==168','len(D)==99')
s=s.replace('TwentySevenTwoQuad','TwentySevenOneQuad').replace('Fin 168','Fin 99').replace('Fin 2 →','Fin 3 →').replace('Fin 2,','Fin 3,')
s=s.replace('![7,7,8,8]','![7,8,8,8]').replace('TWO_QUAD_DATA','ONE_QUAD_DATA').replace("print('168 profiles", "print('99 orbit profiles")
exec(compile(s,__file__,'exec'),globals())
