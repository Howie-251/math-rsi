"""Producer certificate extraction, never independent acceptance."""
from pathlib import Path
import json,collections
P=Path(__file__).resolve().parent
o=json.loads((P/'SIXTEEN_STAR_options.json').read_text())
chosen={5,6,7};classes=[]
for c in o['classes']:
 if c['index'] not in chosen:continue
 i=c['index'];classes.append({'index':i,'geometry':{'index':i,'type':'T1_11','minority':[0],'majority':c['majority'],'omitted':c['omitted']},'forced_pairs':[c['forced_pair']],'forced_cherries':[[0]+c['forced_pair']],'target_rank':256,'source_prefix':c['prefix'],'covered_endpoints':20,'reduced_endpoints':18})
(P/'SIXTEEN_STAR_B_candidate_classes.json').write_text(json.dumps({'classes':classes},indent=2)+'\n')
# Reuse extraction logic on fresh names only; it writes no existing package files.
s=(P/'FOURTEEN_FORCED_prepare.py').read_text();s=s[:s.index('plain=next')]
s=s.replace('FOURTEEN_FORCED_candidate_classes.json','SIXTEEN_STAR_B_candidate_classes.json').replace("pre=R/f'FOURTEEN_FORCED_orbit_{i:03d}'","pre=R/f'SIXTEEN_STAR_B_reduced_{i:03d}'")
s+="\n(R/'SIXTEEN_STAR_B_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY_NOT_INDEPENDENT_ACCEPTANCE','reports':out},indent=2)+'\\n')\n"
(P/'SIXTEEN_STAR_B_extract.py').write_text(s)
exec(compile(s,'SIXTEEN_STAR_B_extract.py','exec'),{'__file__':str(P/'SIXTEEN_STAR_B_extract.py')})
formal={**o,'classes':classes,'options':[x for x in o['options'] if x['Bclass'] in chosen]}
(P/'SIXTEEN_STAR_FORMAL_options.json').write_text(json.dumps(formal,indent=2)+'\n')
print('Extracted 3 positive classes',len(formal['options']),'opening options')
