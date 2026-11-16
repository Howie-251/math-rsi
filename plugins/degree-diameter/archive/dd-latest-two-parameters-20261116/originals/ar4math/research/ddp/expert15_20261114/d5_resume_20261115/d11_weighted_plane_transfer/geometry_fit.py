"""Degree11 actual-map line-hitset fit; no unproved core-distance assertion."""
from pathlib import Path
from collections import Counter
from array import array
import json,resource,time
OUT=Path(__file__).resolve().parent
ROOT=next(p for p in OUT.parents if p.name=='ar4math')
OLD=ROOT/'research/ddp/more_graphs_20261027'
def main():
 t=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(4,5))
 assert not (OUT/'RESULT.json').exists()
 M=OLD/'h9_other_degrees';mapmeta=json.loads((M/'mapping11_result.json').read_text())
 assert mapmeta['mapping_restored'] and mapmeta['n']==37471 and mapmeta['exact_quotient_edges_match']
 fold=array('H');fold.frombytes((M/'point_to_core11.u16.bin').read_bytes())
 fibers=Counter(fold);assert len(fold)==66430 and min(fold)==0 and max(fold)==37470 and len(fibers)==37471
 profile=json.loads((OLD/'accepted_d11_d12_full_neighborhood_clones/PROFILE_D11.json').read_text())
 degrees=(OLD/'accepted_d11_d12_full_neighborhood_clones/source_degrees_d11.u8.bin').read_bytes()
 assert len(degrees)==37631 and dict(Counter(degrees))=={int(k):v for k,v in profile['degree_histogram'].items()}
 with (ROOT/profile['source_file']).open() as f:assert list(map(int,f.readline().split()))==[37631,205329]
 cls=json.loads((M/'fold11_classes.json').read_text())['classes']
 split={u for a in cls if len(a)==2 for u in a}
 pg=json.loads((OUT.parent/'d12_weighted_plane_cover/PG2_9_INCIDENCE.json').read_text())
 nums=list(map(int,(OLD/'h9_baer_nonflat_F3_pool/coefficient_points91.txt').read_text().split()))
 assert nums[0]==91 and pg['coefficient_points']==[nums[1+3*j:4+3*j] for j in range(91)]
 lines=pg['line_point_indices'];assert len(lines)==91 and all(len(x)==10 for x in lines)
 flat=json.loads((OLD/'h9_baer_plane_pool/planes.json').read_text())['records']
 nonflat=json.loads((OLD/'h9_baer_nonflat_F3_pool/nonflat_planes.json').read_text())['records']
 planes=[dict(global_id=i,kind='flat',local_id=r['plane_index'],raw_ids=r['point_ids91']) for i,r in enumerate(flat)]
 planes+=[dict(global_id=364+i,kind='nonflat',local_id=r['nonflat_plane_index'],raw_ids=r['Q9_point_ids91']) for i,r in enumerate(nonflat)]
 assert len(planes)==1120
 rows=[];statushist=Counter();lbhist=Counter();openids=[]
 for p in planes:
  pins=[fold[r] for r in p['raw_ids']]
  providers=[sorted({pins[j] for j in line if degrees[pins[j]]<11}) for line in lines]
  empty=[j for j,ps in enumerate(providers) if not ps]
  forced=sorted({ps[0] for ps in providers if len(ps)==1})
  available=sorted({v for v in pins if degrees[v]<11})
  lb=None
  if empty:state='EXCLUDED_EMPTY_LINE'
  elif len(forced)>11:state='EXCLUDED_FORCED_PINS_GT11'
  else:
   inc={}
   for ell,ps in enumerate(providers):
    for v in ps:inc[v]=inc.get(v,0)|(1<<ell)
   covered=0
   for v in forced:covered|=inc[v]
   residual=((1<<91)-1)^covered
   contributions=sorted(((bits&residual).bit_count() for v,bits in inc.items() if v not in forced),reverse=True)
   total=0;k=0
   while total<residual.bit_count():total+=contributions[k];k+=1
   lb=max((91+max(b.bit_count() for b in inc.values())-1)//max(b.bit_count() for b in inc.values()),len(forced)+k)
   lbhist[lb]+=1
   if lb>11:state='EXCLUDED_INCIDENCE_RESOURCE_GT11'
   else:state='NECESSARY_GATE_OPEN';openids.append(p['global_id'])
  statushist[state]+=1
  rows.append(dict(plane_global_id=p['global_id'],kind=p['kind'],local_id=p['local_id'],raw_point_ids91=p['raw_ids'],
    actual_pin_ids91=pins,available_actual_pin_ids=available,line_free_pin_providers=providers,
    empty_line_indices=empty,forced_pin_ids=forced,in_plane_pin_lower_bound=lb,status=state))
 binding=dict(Delta=11,source_file=profile['source_file'],source_n=37631,source_m=205329,
  actual_core_interval=[0,37471],actual_periphery_interval=[37471,37631],actual_periphery_count=160,
  map_file=str((M/'point_to_core11.u16.bin').relative_to(ROOT)),map_entries=66430,map_range=[0,37470],
  map_all_core_vertices_have_preimage=True,map_fiber_size_histogram=dict(Counter(fibers.values())),
  old37628_core_preserved_by_three_accepted_extensions=True,degree_file='research/ddp/more_graphs_20261027/accepted_d11_d12_full_neighborhood_clones/source_degrees_d11.u8.bin',
  actual_free_vertices=profile['free_vertices'],actual_spare_slots=profile['spare_degree_slots'],
  actual_free_core_vertices=sum(degrees[u]<11 for u in range(37471)),
  actual_free_split_endpoints=sum(degrees[u]<11 for u in split),
  same_33397_quotient_exact=True,core_R4_projection_status='CONDITIONAL_NOT_FULLY_BOUND_TO_RAW_SIGMA_ORIENTATION_IN_READ_EVIDENCE',
  missing_evidence='recover11 checks pair-swap, exact quotient, split edge counts and canonical label order, but not edge-by-edge H9 G_sigma-to-this-core projection.',
  prior_mapping_scope=mapmeta['geometry_orientation_scope'],
  no_degree12_map_or_core_numbering_used=True,conditional_generator_family_is_well_defined=True)
 (OUT/'SOURCE_BINDING.json').write_text(json.dumps(binding,indent=2)+'\n')
 (OUT/'LINE_PROVIDER_TABLES.json').write_text(json.dumps(dict(source_binding=binding,planes=rows),separators=(',',':'))+'\n')
 (OUT/'RETAINED_PLANE_IDS.json').write_text(json.dumps(openids)+'\n')
 result=dict(status='COMPLETE_ACTUAL_D11_MAPPED_PLANE_NECESSARY_FIT',planes=1120,status_counts=dict(statushist),
  retained_plane_count=len(openids),retained_plane_ids=openids,resource_lower_bound_histogram=dict(lbhist),
  scope='Only the concrete actual-map line-hitset candidate family. No claim of a fully inherited universal core R4 theorem; actual candidate whole-source R4 would be required.',
  does_not_reuse_old_Baer_Redei_no_as_general_no=True,BFS_calls=0,solver_calls=0,random_generations=0,
  new_graphs=0,CPU_seconds=time.process_time()-t)
 (OUT/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
if __name__=='__main__':main()
