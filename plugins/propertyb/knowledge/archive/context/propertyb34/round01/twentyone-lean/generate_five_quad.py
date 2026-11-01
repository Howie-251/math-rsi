from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
s=(ROOT/'context/propertyb34/round01/twenty-lean/generate_two_quad.py').read_text()
a=s.index('raw=json.load');b=s.index('D=[]',a)
s=s[:a]+'''raw=[]
for r0 in json.load(open(ROOT/'context/propertyb34-hour1-20261013/low-math/TWENTYONE_FIVE_VERIFIED.json'))['witnesses']:
 if len(r0['ds'])!=4:continue
 r=dict(r0);counts={int(k):v for k,v in r['counts'].items()}
 r['ls']=[sum(n for m,n in counts.items() if m&p==p) for p in (3,5,9,6,10,12)]
 r['t3']=[counts.get(m,0) for m in (7,11,13,14)];r['t4']=counts.get(15,0)
 assert r['kind']=='dual'
 r['certificate_kind']='avoided_dual';raw.append(r)
''' +s[b:]
s=s.replace(" if r['ds']!=[7,7,8,8]:continue\n",'')
s=s.replace('Profile(20,','Profile(21,').replace('pair_weight(20,','pair_weight(21,').replace('(19-R.bit_count())','(20-R.bit_count())')
s=s.replace('len(dual)<=2','len(dual)<=3').replace('(2-len(dual))','(3-len(dual))').replace('len(D)==168','len(D)==95')
s=s.replace('dict(co=r[\'ls\']','dict(degrees=r[\'ds\'],co=r[\'ls\']')
s=s.replace('TwentySevenTwoQuad','TwentyOneFiveQuad').replace('Fin 168','Fin 95').replace('Fin 2 →','Fin 3 →').replace('Fin 2,','Fin 3,')
s=s.replace('def degree : Fin 4 → ℕ := ![7,7,8,8]','')
s=s.replace("s+='def coData", "s+='def degree : Case → Fin 4 → ℕ := '+vec(vec(d['degrees']) for d in D)+'\\n'\ns+='def coData")
s=s.replace('recovered 34 degree','recovered 34 (degree i)').replace('Fin 20','Fin 21').replace('⟨20,','⟨21,').replace('(20-1-','(21-1-')
s=s.replace('TWO_QUAD_DATA','FIVE_QUAD_DATA').replace("print('168 profiles", "print('95 profiles")
exec(compile(s,__file__,'exec'),globals())
