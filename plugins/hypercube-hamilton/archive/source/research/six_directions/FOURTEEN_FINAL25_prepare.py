"""Fresh positive producer exploration, no independent acceptance."""
from pathlib import Path
from itertools import permutations
import json
P=Path(__file__).resolve().parent
maps=[tuple(sum(((x>>q[d])&1)<<d for d in range(5)) for x in range(32)) for q in permutations(range(5))]
T={7,11,13,19,21,25};units={1,2,4,8,16};seeds={0:(3,4,7),3:(15,1,7)}
out=[]
for orbit in [0,1]:
 WA=units|({14} if orbit==0 else set());M={0} if orbit==0 else {0,30};classes={};options=[]
 for t in sorted(T):
  for w in sorted(units):
   for b in sorted(units-{w}):
    U=WA-{w,b};J=(T-{t})|U;R={w,b}
    key=min((tuple(sorted(tr[x] for x in M)),tuple(sorted(tr[x] for x in J)),tuple(sorted(tr[x] for x in U)),tuple(sorted(tr[x] for x in R))) for tr in maps)
    if key not in classes:
     i=len(classes);classes[key]={'index':i,'minority':key[0],'majority':key[1],'omitted':key[2],'forced_pair':key[3],'prefix':f'FOURTEEN_FINAL25_B{orbit}_{i:03d}'}
    i=classes[key]['index']
    for case,seed in seeds.items():
     for pi,tr in enumerate(maps):
      if (tr[seed[1]],tr[seed[2]])!=(b,t):continue
      options.append({'q':tr[seed[0]],'t':t,'w':w,'b':b,'case':case,'permutation_index':pi,'Bclass':i})
 for c in classes.values():
  (P/(c['prefix']+'_config.txt')).write_text(' '.join(map(str,list(c['minority'])+list(c['majority'])))+'\n'+' '.join(map(str,c['omitted']))+'\n')
 item={'orbit':orbit,'T':sorted(T),'odd_A_holes':[14] if orbit==0 else [],'required_even_A':[] if orbit==0 else [30],'classes':list(classes.values()),'options':options};out.append(item)
 print('orbit',orbit,'classes',len(classes),'options',len(options))
 s=(P/'TWELVE_NEW_T19_search.cpp').read_text().replace('if(rows.size()==R||examined>=limitRows)done=true;','if(rows.size()==512||examined>=limitRows)done=true;')
 if orbit==1:
  s=s.replace('array<unsigned char,34>','array<unsigned char,36>').replace('edges.size()!=17','edges.size()!=18').replace('i<4;++i','i<3;++i').replace('data(),34','data(),36')
 (P/f'FOURTEEN_FINAL25_B{orbit}_search.cpp').write_text(s)
(P/'FOURTEEN_FINAL25_options.json').write_text(json.dumps({'status':'PRODUCER_EXPLORATION','orbits':out},indent=2)+'\n')
