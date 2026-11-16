"""Read saved exact rows; bound disjoint in-plane/out-of-plane selector resources."""
from pathlib import Path
from array import array
from collections import Counter
import json,resource,sys,time
OUT=Path(__file__).resolve().parent
def main():
 start=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(2,3))
 D=OUT/'current_graph_data';meta=json.loads((D/'PROVIDERS_META.json').read_text())
 assert meta['source_n']==42402 and meta['provider_rows']==1046
 free=array('I');free.frombytes((D/'FREE_IDS.u32le.bin').read_bytes())
 assert sys.byteorder=='little' and len(free)==13857
 index={v:i for i,v in enumerate(free)};full=(1<<len(free))-1
 raw=(D/'PERIPHERY_R4_FREE.u64le.bin').read_bytes();step=meta['provider_row_bytes']
 assert len(raw)==1046*step
 providers=[int.from_bytes(raw[i*step:(i+1)*step],'little') for i in range(1046)]
 assert all(p and p&~full==0 for p in providers)
 tables=json.loads((OUT/'LINE_PROVIDER_TABLES.json').read_text())
 core={r['plane_global_id']:r['strict_pin_lower_bound'] for r in json.loads((OUT/'INCIDENCE_RESOURCE_BOUNDS.json').read_text())['planes']}
 records=[];hist=Counter();newclosed=[];closed=[];anchor=None
 for plane in tables['planes']:
  if plane['status']!='NECESSARY_GATE_OPEN':continue
  pid=plane['plane_global_id'];A=sum(1<<index[v] for v in plane['available_actual_pin_ids'])
  # Only targets missed by the union of ALL available in-plane pins enter this bound.
  missing=[j for j,p in enumerate(providers) if not p&A]
  if not missing:external=0;intersection=full;witness=None;contradiction_prefix=[]
  else:
   intersection=full;contradiction_prefix=[]
   for j in missing:
    intersection&=providers[j];contradiction_prefix.append(41356+j)
    if not intersection:break
   assert intersection&A==0
   external=1 if intersection else 2
   witness=free[(intersection&-intersection).bit_length()-1] if intersection else None
   if intersection:contradiction_prefix=[]
  joint=core[pid]+external;hist[(core[pid],external,joint)]+=1
  if joint>12:closed.append(pid)
  if core[pid]<=12<joint:newclosed.append(pid)
  r=dict(plane_global_id=pid,available_in_plane_pins=len(plane['available_actual_pin_ids']),
   all_available_plane_union_missing_periphery=[41356+j for j in missing],
   missing_count=len(missing),in_plane_pin_lower_bound=core[pid],
   outside_plane_pin_lower_bound=external,joint_selector_lower_bound=joint,
   one_external_pin_intersection_count=intersection.bit_count() if missing else None,
   one_external_pin_witness=witness,empty_intersection_witness_targets=contradiction_prefix,
   excludes_budget12=joint>12)
  records.append(r)
  if pid==635:anchor=r
 result=dict(status='COMPLETE_SAVED_ROW_EXTERNAL_RESOURCE_CHECK',planes_checked=len(records),
  excluded_budget12_by_joint_bound=len(closed),newly_excluded_beyond_incidence_bound=len(newclosed),
  newly_excluded_plane_ids=newclosed,still_not_excluded=754-len(closed),
  lower_bound_histogram=[dict(core=a,external=b,joint=c,planes=count) for (a,b,c),count in sorted(hist.items())],
  proof='For A=all current available in-plane pins, every target missed by OR(A) requires a selected vertex outside A. If all such target provider sets have empty intersection, at least two distinct outside vertices are necessary. Add this to the independent necessary in-plane line-cover bound because the selector domains are disjoint.',
  planes=records,CPU_seconds=time.process_time()-start,BFS_calls=0,solver_calls=0,search_calls=0,
  fixed_selected_P_used=False,in_flight_solver_modified=False,new_graphs=0)
 (OUT/'EXTERNAL_RESOURCE_EXPLANATION.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ['planes','lower_bound_histogram']}))
 print('anchor635',json.dumps(anchor))
if __name__=='__main__':main()
