from pathlib import Path
from array import array
from collections import Counter,defaultdict
import json,time,resource
P=Path(__file__).resolve().parent;R=P.parent;A=next(p for p in P.parents if p.name=='ar4math');G=R/'d12_weighted_plane_cover';OLD=A/'research/ddp/more_graphs_20261027';SIG=A/'research/ddp/global_coverage_20261027/h9_quadric_line_signature'
def main():
 t=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(1,2))
 tables=json.loads((G/'LINE_PROVIDER_TABLES.json').read_text());planes={v['plane_global_id']:v for v in tables['planes']};lines=json.loads((G/'PG2_9_INCIDENCE.json').read_text())['line_point_indices'];pool=json.loads((OLD/'h9_redei15/pool/pool12.json').read_text())['records'];oldsets=[set(r['pins'])for r in pool]
 pi=array('H');pi.frombytes((SIG/'point_to_core.u16.bin').read_bytes());coords=(SIG/'point_coords.u8.bin').read_bytes();rawlookup={coords[7*r:7*r+7]:r for r in range(len(pi))};cube=[x%3+3*((2*(x//3))%3)for x in range(9)]
 def sigma(r):return rawlookup[bytes(cube[x]for x in coords[7*r:7*r+7])]
 records=[]
 for row in [json.loads(s)for s in(P/'ADDITIONS.jsonl').read_text().splitlines()if s]:
  plane=planes[row['plane_id']];core=set(row['core']);rawids=plane['raw_point_ids91'];indices={i for i,r in enumerate(rawids)if pi[r]in core};rawset={rawids[i]for i in indices};groups=defaultdict(list)
  for i in sorted(indices):groups[int(pi[rawids[i]])].append(rawids[i])
  counts=[len(indices.intersection(line))for line in lines];private={i:[j for j,line in enumerate(lines)if len(indices.intersection(line))==1 and i in line]for i in indices};fixed=[r for r in rawset if sigma(r)==r];paired=[];split=[];unpaired=[]
  for r in sorted(rawset):
   s=sigma(r)
   if s==r:continue
   if s not in rawset:unpaired.append(r)
   elif r<s:(paired if pi[r]==pi[s]else split).append([r,s])
  records.append(dict(order=row['order'],new_vertex=row['new_vertex'],plane_id=row['plane_id'],plane_kind=plane['kind'],plane_local_id=plane['plane_local_id'],core=row['core'],tail=row['tail'],core_pin_count=len(core),raw_preimage_count=len(rawset),raw_coefficient_indices=sorted(indices),raw_point_ids=sorted(rawset),actual_pin_preimage_groups=dict(groups),frobenius_fixed_raw_count=len(fixed),frobenius_paired_same_pin_count=len(paired),frobenius_split_pair_count=len(split),frobenius_unpaired_selected_raw_count=len(unpaired),fixed_raw_ids=sorted(fixed),paired_same_pin_raw_ids=paired,split_pair_raw_ids=split,unpaired_selected_raw_ids=unpaired,line_intersection_hist=dict(sorted(Counter(counts).items())),blocking=min(counts)>0,raw_inclusion_minimal=all(private.values()),raw_points_without_tangent_indices=sorted(i for i,v in private.items()if not v),raw_private_tangent_line={str(i):v[0]for i,v in private.items()if v},old85_equal=[i for i,s in enumerate(oldsets)if s==core],old85_subset_of_core=[i for i,s in enumerate(oldsets)if s<=core],core_subset_of_old85=[i for i,s in enumerate(oldsets)if core<=s],actual_R4_evidence='ADDITIONS.jsonl: current source n='+str(row['source_n'])+'; all vertices covered; no BFS rerun'))
 result=dict(status='COMPLETE_READONLY_METADATA_ANALYSIS',input_pi=str((SIG/'point_to_core.u16.bin').relative_to(A)),plane_tables=str((G/'LINE_PROVIDER_TABLES.json').relative_to(A)),old85_pool=str((OLD/'h9_redei15/pool/pool12.json').relative_to(A)),old85_count=len(pool),definitions={'raw_preimages':'All raw points in this own saved91-point plane whose actual pi image is selected in the core.','fixed':'Raw sigma(r)=r.','paired':'Selected nonfixed sigma pair whose two raw points have the same actual pi image.','split':'Selected nonfixed sigma pair whose two raw points have different actual pi images.','unpaired':'Selected raw point whose sigma mate is not in this raw set; reported separately, not counted as a pair.','raw_minimal':'Every selected raw point has a tangent among the saved91 projective lines.','old85_relation':'Comparison of actual core pin sets, not plane name or raw count.'},records=records,BFS_calls=0,solver_calls=0,new_searches=0,independent_all8_prefix_status='PASS as reported by parent',CPU=time.process_time()-t)
 (P/'GEOMETRY_SERIES.json').write_text(json.dumps(result,indent=2)+'\n')
 for v in records:print(v['order'],'plane',v['plane_id'],'raw',v['raw_preimage_count'],'fixed/paired/split/unpaired',v['frobenius_fixed_raw_count'],v['frobenius_paired_same_pin_count'],v['frobenius_split_pair_count'],v['frobenius_unpaired_selected_raw_count'],'hist',v['line_intersection_hist'],'minimal',v['raw_inclusion_minimal'],'equal/sub/super',v['old85_equal'],v['old85_subset_of_core'],v['core_subset_of_old85'])
 print('CPU',result['CPU'])
if __name__=='__main__':main()
