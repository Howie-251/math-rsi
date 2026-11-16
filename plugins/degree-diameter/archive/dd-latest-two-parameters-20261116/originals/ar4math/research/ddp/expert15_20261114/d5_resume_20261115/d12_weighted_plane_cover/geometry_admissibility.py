"""Only existing-plane geometry/degree gates; no graph BFS, guard balls, or solver."""
from pathlib import Path
from collections import Counter
from array import array
import json,resource,time

OUT=Path(__file__).resolve().parent
ROOT=next(p for p in OUT.parents if p.name=='ar4math')
OLD=ROOT/'research/ddp/more_graphs_20261027'
SIG=ROOT/'research/ddp/global_coverage_20261027/h9_quadric_line_signature'
def add(x,y):return (x%3+y%3)%3+3*((x//3+y//3)%3)
def mul(x,y):return ((x%3)*(y%3)+2*(x//3)*(y//3))%3+3*(((x%3)*(y//3)+(x//3)*(y%3))%3)
def power(x,n):
 y=1
 for _ in range(n):y=mul(y,x)
 return y
def dot(a,b):
 x=0
 for u,v in zip(a,b):x=add(x,mul(u,v))
 return x
def normalize(v):
 z=next(x for x in v if x); inv=power(z,7)
 return [mul(x,inv) for x in v]
def save(name,j):(OUT/name).write_text(json.dumps(j,separators=(',',':'))+'\n')
def main():
 start=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(5,6))
 assert not (OUT/'RESULT.json').exists(),'Completed run exists; no silent rerun.'
 coeff=json.loads((OLD/'h9_redei15/pool/orbit.json').read_text())['coefficient_points_PG2F9']
 nums=list(map(int,(OLD/'h9_baer_nonflat_F3_pool/coefficient_points91.txt').read_text().split()))
 assert nums[0]==91 and coeff==[nums[1+3*i:4+3*i] for i in range(91)]
 lines=[[j for j,p in enumerate(coeff) if dot(ell,p)==0] for ell in coeff]
 assert all(len(line)==10 for line in lines)
 assert Counter(j for line in lines for j in line)==Counter({j:10 for j in range(91)})
 bits=[sum(1<<j for j in line) for line in lines]
 assert all((bits[i]&bits[j]).bit_count()==1 for i in range(91) for j in range(i))
 flat=json.loads((OLD/'h9_baer_plane_pool/planes.json').read_text())['records']
 nonflat=json.loads((OLD/'h9_baer_nonflat_F3_pool/nonflat_planes.json').read_text())['records']
 assert len(flat)==364 and len(nonflat)==756
 planes=[dict(global_id=i,kind='flat',local_id=r['plane_index'],basis=r['basis_y_x_z'],raw_ids91=r['point_ids91']) for i,r in enumerate(flat)]
 planes += [dict(global_id=364+i,kind='nonflat',local_id=r['nonflat_plane_index'],basis=r['RREF_basis'],raw_ids91=r['Q9_point_ids91']) for i,r in enumerate(nonflat)]
 fold=array('H');fold.frombytes((SIG/'point_to_core.u16.bin').read_bytes())
 assert len(fold)==66430 and min(fold)==0 and max(fold)==41355
 degpath=OLD/'accepted_d11_d12_full_neighborhood_clones/source_degrees_d12.u8.bin'
 deg=degpath.read_bytes();assert len(deg)==42402 and max(deg)==12
 profile=json.loads((OLD/'accepted_d11_d12_full_neighborhood_clones/PROFILE_D12.json').read_text())
 assert (profile['source_n'],profile['source_m'])==(42402,245937)
 assert dict(Counter(deg))=={int(k):v for k,v in profile['degree_histogram'].items()}
 source=ROOT/profile['source_file']
 with source.open() as f:assert list(map(int,f.readline().split()))==[42402,245937]
 rawcoords=(SIG/'point_coords.u8.bin').read_bytes();assert len(rawcoords)==66430*7
 pool77=json.loads((OLD/'h9_redei15/pool/pool12.json').read_text())['records'][77]
 witness=pool77['witness'];assert (witness['plane_global_index'],witness['plane_local_index'],witness['orbit_index'])==(635,271,602)
 checks=[]
 for index in [77,635]:
  plane=planes[index]
  assert index==77 or plane['basis']==witness['plane_basis']
  for j,c in enumerate(coeff):
   v=[dot(c,[plane['basis'][i][k] for i in range(3)]) for k in range(7)]
   assert normalize(v)==list(rawcoords[7*plane['raw_ids91'][j]:7*plane['raw_ids91'][j]+7]),(index,j)
  checks.append(dict(plane_global_id=index,kind=plane['kind'],local_id=plane['local_id'],all91_coefficient_points_match_raw_coordinates=True))
 # One decision per complete plane, with every line's actual free pin providers retained.
 records=[];retained=[];empty=[];forced_over=[];forcedhist=Counter();availablehist=Counter()
 for plane in planes:
  pins91=[fold[r] for r in plane['raw_ids91']]
  providers=[sorted({pins91[j] for j in line if deg[pins91[j]]<12}) for line in lines]
  empty_lines=[i for i,ps in enumerate(providers) if not ps]
  forced=sorted({ps[0] for ps in providers if len(ps)==1})
  allowed=sorted({v for v in pins91 if deg[v]<12})
  if empty_lines:state='EXCLUDED_EMPTY_LINE';empty.append(plane['global_id'])
  elif len(forced)>12:state='EXCLUDED_MORE_THAN12_FORCED_PINS';forced_over.append(plane['global_id'])
  else:state='NECESSARY_GATE_OPEN';retained.append(plane['global_id'])
  forcedhist[len(forced)]+=1;availablehist[len(allowed)]+=1
  records.append(dict(plane_global_id=plane['global_id'],kind=plane['kind'],plane_local_id=plane['local_id'],
   raw_point_ids91=plane['raw_ids91'],actual_pin_ids91=pins91,available_actual_pin_ids=allowed,
   line_free_pin_providers=providers,empty_line_indices=empty_lines,forced_pin_ids=forced,status=state))
 binding=dict(source_file=profile['source_file'],source_n=42402,source_m=245937,source_D5='Inherited, not revalidated',
  degree_file=str(degpath.relative_to(ROOT)),degree_histogram=dict(Counter(deg)),pi_file=str((SIG/'point_to_core.u16.bin').relative_to(ROOT)),
  core_vertex_interval=[0,41356],periphery_vertex_interval=[41356,42402],periphery_count=1046,
  coefficient_points_file='research/ddp/more_graphs_20261027/h9_baer_nonflat_F3_pool/coefficient_points91.txt',
  coordinate_binding_checks=checks,pool77_witness=dict(pool_index=77,plane_global_id=635,nonflat_local_id=271,orbit_index=602),
  flat_global77_is_different_plane=True,total_degree_budget=12,no_fixed_core_guard_quota=True)
 save('SOURCE_BINDING.json',binding)
 save('PG2_9_INCIDENCE.json',dict(coefficient_points=coeff,line_normal_vectors=coeff,line_point_indices=lines,
  line_size=10,point_degree=10,pairwise_distinct_lines_intersect_in_one_point=True))
 save('LINE_PROVIDER_TABLES.json',dict(source_binding=binding,planes=records))
 save('RETAINED_PLANE_IDS.json',retained)
 result=dict(status='COMPLETE_GEOMETRY_NECESSARY_GATES',planes=1120,excluded_empty_line=len(empty),
  excluded_forced_pins_gt12=len(forced_over),necessary_gate_open=len(retained),retained_plane_ids=retained,
  forced_pin_count_histogram=dict(forcedhist),available_actual_pin_count_histogram=dict(availablehist),
  anchor_pool77_plane635_status=records[635]['status'],flat_global77_status=records[77]['status'],
  guarantees='Empty line / >12 forced pins exclude only this plane blocking certificate, not all graph extensions.',
  open_is_not_feasible=True,no_core_guard_role_quota=True,BFS_calls=0,guard_columns=0,solver_calls=0,new_graphs=0,
  CPU_seconds=time.process_time()-start)
 save('RESULT.json',result);print(json.dumps(result))
if __name__=='__main__':main()
