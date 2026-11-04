from pathlib import Path
import json
R=Path(__file__).resolve().parent
selected=[x['index'] for x in json.loads((R/'FOURTEEN_MID_LOCAL_greedy_registry.json').read_text())['selected']];assert selected==[1,15,44]
s=(R/'FOURTEEN_MID_LOCAL_profile.py').read_text().replace('FOURTEEN_MID_LOCAL','FOURTEEN_MID_SELECTED')
s=s.replace("for row in summary['reports']:","for row in summary['reports']:\n if row['index'] not in (1,15,44):continue")
(R/'FOURTEEN_MID_SELECTED_profile.py').write_text(s)
classes=[c for c in json.loads((R/'FOURTEEN_MID_LOCAL_candidate_classes.json').read_text())['classes'] if c['index'] in selected]
assert len(classes)==3
(R/'FOURTEEN_MID_REDUCED_candidate_classes.json').write_text(json.dumps({'classes':classes},indent=2)+'\n')
s=(R/'FOURTEEN_FORCED_prepare.py').read_text();s=s[:s.index('plain=next(')].replace('FOURTEEN_FORCED','FOURTEEN_MID_REDUCED')
s+="\nfor c in classes:\n if not c['forced_pairs']:out.append({**c,'prefix':c['source_prefix'],'forest_record_bytes':36,'rows':2048,'status':'PRODUCER_ONLY'})\n"
s+="(R/'FOURTEEN_MID_REDUCED_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY','reports':out},indent=2)+'\\n')\nprint('Prepared',len(out),'local inputs')\n"
(R/'FOURTEEN_MID_REDUCED_prepare.py').write_text(s)
