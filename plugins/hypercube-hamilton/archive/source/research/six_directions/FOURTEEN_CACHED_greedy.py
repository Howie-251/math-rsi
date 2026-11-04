"""Select a sufficient subset of cached *candidate* local inputs, no acceptance."""
from pathlib import Path
from collections import defaultdict,Counter
import json,struct,hashlib
P=Path(__file__).resolve().parent
cat=json.loads((P/'FOURTEEN_CACHED_catalog.json').read_text());scan=json.loads((P/'FOURTEEN_CACHED_result.json').read_text())
rows={(0 if r['family']==30 else 1000)+r['local_id']:r for r in cat['rows']}
sets=defaultdict(set);hits={};sources={};offsets={};targets={};offset=0
for report in scan['reports']:
 v=report['v'];free=report['free_target'];tag=f"h14_v{v}_{'free' if free else 'covered'}";raw=(P/f'FOURTEEN_REUSE_remaining_{tag}.bin').read_bytes();sources[tag]=raw;offsets[tag]=offset
 assert len(raw)==report['input']*13
 data=(P/f'FOURTEEN_CACHED_all_hits_{tag}.bin').read_bytes();assert len(data)%28==0
 for off in range(0,len(data),28):
  record=data[off:off+28];index,family,d,local,S,M,J,U=struct.unpack('<IBBHQIII',record);assert index<report['input'] and d<6
  code=(0 if family==30 else 1000)+local;assert code in rows
  rid=offset+index;assert code not in hits.setdefault(rid,{})
  hits[rid][code]=record;sets[code].add(rid);targets[rid]=(v,free)
 offset+=report['input']
assert offset==48211 and sum(map(len,sets.values()))==278524
assert {str(k):len(v) for k,v in sets.items()}==scan['candidate_hit_histogram']
union=set(hits);assert len(union)==35665
todo=set(sets);taken=set();selected=[];steps=[]
while todo:
 code=max(todo,key=lambda k:(len(sets[k]-taken),-k));new=sets[code]-taken
 if not new:break
 selected.append(code);steps.append({'code':code,'family':rows[code]['family'],'local_id':rows[code]['local_id'],'new_covered':len(new),'target_status_histogram':{str(k):v for k,v in Counter(targets[i] for i in new).items()}})
 taken|=sets[code];todo.remove(code)
assert taken==union
for report in scan['reports']:
 v=report['v'];free=report['free_target'];tag=f"h14_v{v}_{'free' if free else 'covered'}";raw=sources[tag];off=offsets[tag];witness=bytearray();residual=bytearray()
 for i in range(len(raw)//13):
  rid=off+i
  if rid not in union:residual.extend(raw[i*13:i*13+13]);continue
  code=next(k for k in selected if k in hits[rid]);witness.extend(hits[rid][code])
 assert bytes(residual)==(P/f'FOURTEEN_CACHED_remaining_{tag}.bin').read_bytes()
 assert len(witness)//28==report['candidate_covered']
 (P/f'FOURTEEN_CACHED_selected_witness_{tag}.bin').write_bytes(witness)
reg={'status':'GREEDY_UNREVIEWED_LOCAL_CANDIDATES_ONLY','selected_count':len(selected),'selected_codes':selected,'covered_candidate_union':35665,'same_union_as_all_cached_candidate_hits':True,
 'rows':[rows[k] for k in selected],'steps':steps,'selected_type_counts':dict(Counter(rows[k]['type'] for k in selected)),
 'greedy_optimality_claimed':False,'local_inputs_accepted':False,'full_fourteen_hole_proved':False,'full_P6_proved':False}
(P/'FOURTEEN_CACHED_greedy_registry.json').write_text(json.dumps(reg,indent=2)+'\n')
print(json.dumps({'selected_count':len(selected),'selected_types':reg['selected_type_counts'],'covered_candidate_union':35665,'remaining':12546,'selected_codes':selected},indent=2))
