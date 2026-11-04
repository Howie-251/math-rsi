"""Extract only five positive B inputs, pending fresh independent review."""
from pathlib import Path
import json
P=Path(__file__).resolve().parent
o=json.loads((P/'FOURTEEN_FINAL25_options.json').read_text());classes=[];formal=[]
for z in o['orbits']:
 orbit=z['orbit'];used={0,1,7} if orbit==0 else {0,1};subset=[]
 for c in z['classes']:
  if c['index'] not in used:continue
  i=orbit*100+c['index'];fp=c['forced_pair'];g={k:c[k] for k in ['minority','majority','omitted']};h=next(h for h in g['minority'] if all((h^p).bit_count()==1 for p in fp))
  cc={'index':i,'orbit':orbit,'Bclass':c['index'],'geometry':g,'forced_pairs':[fp],'forced_cherries':[[h]+fp],'target_rank':512,'source_prefix':c['prefix'],'covered_endpoints':22,'reduced_endpoints':20}
  classes.append(cc);subset.append(cc)
 formal.append({**z,'classes':subset,'options':[x for x in z['options'] if x['Bclass'] in used]})
(P/'FOURTEEN_FINAL25_B_candidate_classes.json').write_text(json.dumps({'classes':classes},indent=2)+'\n')
s=(P/'FOURTEEN_FORCED_prepare.py').read_text();s=s[:s.index('plain=next')]
s=s.replace('FOURTEEN_FORCED_candidate_classes.json','FOURTEEN_FINAL25_B_candidate_classes.json').replace("pre=R/f'FOURTEEN_FORCED_orbit_{i:03d}'","pre=R/f'FOURTEEN_FINAL25_B_reduced_{i:03d}'")
s+="\n(R/'FOURTEEN_FINAL25_B_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY_NOT_INDEPENDENT_ACCEPTANCE','reports':out},indent=2)+'\\n')\n"
(P/'FOURTEEN_FINAL25_B_extract.py').write_text(s)
exec(compile(s,'FOURTEEN_FINAL25_B_extract.py','exec'),{'__file__':str(P/'FOURTEEN_FINAL25_B_extract.py')})
(P/'FOURTEEN_FINAL25_FORMAL_options.json').write_text(json.dumps({'status':'POSITIVE_PRODUCER_INPUTS_ONLY','orbits':formal},indent=2)+'\n')
for z in formal:
 (P/f'FOURTEEN_FINAL25_options_{z["orbit"]}.bin').write_bytes(b''.join(bytes(x[k] for k in ['q','t','w','b','case','permutation_index']) for x in z['options']))
s=(P/'FOURTEEN_FORCED_author_check.py').read_text();s=s[:s.index('coverage=json.loads')].replace('FOURTEEN_FORCED_summary.json','FOURTEEN_FINAL25_B_summary.json')
s+="\n(R/'FOURTEEN_FINAL25_B_author_check.json').write_text(json.dumps({'status':'PRODUCER_AUTHOR_CHECK_SUCCESS_NOT_INDEPENDENT_ACCEPTANCE','totals':dict(tot),'reports':results},indent=2)+'\\n')\n"
(P/'FOURTEEN_FINAL25_B_author_check.py').write_text(s)
print('extracted',len(classes),'positive local inputs')
