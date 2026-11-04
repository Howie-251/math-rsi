"""New producer exploration. No independent acceptance, no ledger changes."""
from pathlib import Path
from itertools import permutations
import json
P=Path(__file__).resolve().parent
maps=[tuple(sum(((x>>q[d])&1)<<d for d in range(5)) for x in range(32)) for q in permutations(range(5))]
T={7,11,13,19,21,25,31};WA={1,2,4,8,14,16,22};units={1,2,4,8,16}
def canon(J,U,R):
 return min((tuple(sorted(tr[x] for x in J)),tuple(sorted(tr[x] for x in U)),tuple(sorted(tr[x] for x in R))) for tr in maps)
accepted={}
for c in json.loads((P/'FOURTEEN_FORCED_candidate_classes.json').read_text())['classes']:
 g=c['geometry']
 if g['minority']==[0] and len(c['forced_pairs'])==1:
  accepted[canon(g['majority'],g['omitted'],c['forced_pairs'][0])]=c['index']
classes={};options=[];seeds={0:(3,4,7),3:(15,1,7)}
for t in sorted(T-{31}):
 for w in sorted(units):
  for b in sorted(units-{w}):
   U=WA-{w,b};J=(T-{t})|U;R={w,b};key=canon(J,U,R)
   if key not in classes:
    i=len(classes);classes[key]={'index':i,'majority':key[0],'omitted':key[1],'forced_pair':key[2],'accepted14_index':accepted.get(key)}
   i=classes[key]['index']
   for case,seed in seeds.items():
    for pi,tr in enumerate(maps):
     q=tr[seed[0]]
     if (tr[seed[1]],tr[seed[2]])!=(b,t):continue
     options.append({'q':q,'t':t,'w':w,'b':b,'case':case,'permutation_index':pi,'Bclass':i})
for c in classes.values():
 pre=f'SIXTEEN_STAR_B_{c["index"]:03d}';c['prefix']=pre
 (P/(pre+'_config.txt')).write_text(' '.join(map(str,[0]+list(c['majority'])))+'\n'+' '.join(map(str,c['omitted']))+'\n')
out={'status':'PRODUCER_OPTIONS_ONLY','T':sorted(T),'odd_A_holes':[14,22],'classes':list(classes.values()),'options':options}
(P/'SIXTEEN_STAR_options.json').write_text(json.dumps(out,indent=2)+'\n')
print('classes',len(classes),'accepted',sum(c['accepted14_index'] is not None for c in classes.values()),'options',len(options))
