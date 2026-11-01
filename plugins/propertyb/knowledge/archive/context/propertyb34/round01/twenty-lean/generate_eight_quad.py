from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
s=(ROOT/'context/propertyb34/round01/twenty-lean/generate_two_quad.py').read_text()
a=s.index('raw=json.load');b=s.index('D=[]',a)
s=s[:a]+'''source=json.load(open(ROOT/'context/propertyb34-hour1-20261013/low-math/EIGHT_VERIFIED.json'))
raw=[]
for r0 in source['witnesses']:
 if r0['ds'] != [8,8,8,8]: continue
 r=dict(r0)
 counts={int(k):v for k,v in r['counts'].items()}
 r['ls']=[sum(n for m,n in counts.items() if m&p==p) for p in (3,5,9,6,10,12)]
 r['t3']=[counts.get(m,0) for m in (7,11,13,14)];r['t4']=counts.get(15,0)
 r['certificate_kind']='pure' if r['kind']=='pure' else 'avoided_dual'
 raw.append(r)
''' +s[b:]
s=s.replace('[7,7,8,8]', '[8,8,8,8]').replace('len(dual)<=2','len(dual)<=3').replace('(2-len(dual))','(3-len(dual))').replace('len(D)==168','len(D)==79')
s=s.replace('TwentySevenTwoQuad','TwentyEightQuad').replace('Fin 168','Fin 79').replace('Fin 2 →','Fin 3 →').replace('Fin 2,','Fin 3,')
s=s.replace('![7,7,8,8]','![8,8,8,8]').replace('TWO_QUAD_DATA','EIGHT_QUAD_DATA').replace("print('168 profiles", "print('79 orbit profiles")
exec(compile(s,__file__,'exec'),globals())
a=(ROOT/'formal/Aris4Math/ThirtyFour/TwentySevenOneQuad.lean').read_text()
a=a.replace('TwentySevenOneQuad','TwentyEightQuad')
(ROOT/'formal/Aris4Math/ThirtyFour/TwentyEightQuad.lean').write_text(a)
