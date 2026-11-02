"""One frozen real-controller pair and two inverse-compatible packet rules."""
import time
START=time.process_time()
from pathlib import Path
from itertools import product
import json,resource
resource.setrlimit(resource.RLIMIT_CPU,(8,8))
HERE=Path(__file__).resolve().parent
BAR=[1,0,3,2]
PRIOR=2.3

def save(n,o):(HERE/n).write_text(json.dumps(o,ensure_ascii=False,indent=2)+'\n')
if (HERE/'ATTEMPT.json').exists():raise RuntimeError('one-shot packet test already attempted')
save('ATTEMPT.json',{'status':'STARTED','prior_read_input_paper_prep_CPU':PRIOR,'case_cap':10})
old=json.loads((HERE.parent/'EXISTING_C30_BINARY_CHART_INPUT.json').read_text())
C=old['typed_controller']['controller'];s,t=0,18
assert C[0][0]==18 and C[18][1]==0
A=[2,1,4]
charts={'ARC':{'maps':[A,A,[1,2,7],[1,2,7]],'v':[1,2,4,7]},'COLLINEAR':{'maps':[A,A,[6,2,3],[6,2,3]],'v':[1,2,4,3]}}
def apply(cols,x):
 y=0
 for k in range(3):
  if x>>k&1:y^=cols[k]
 return y

def ctrl(w):
 u=s
 for p in w:u=C[u][p]
 return u
words=[list(w)for length in range(4)for w in product(range(4),repeat=length)if ctrl(w)==t]
packets=[[0,q,BAR[q]]for q in [0,2,3]]
assert all(w in words for w in packets)
save('FROZEN_CONTROLLER_ROUTES.json',{'s':s,'t':t,'C0':C[0],'C18':C[18],'all_actual_le3_words':words,'rank2_packet':packets,'controller_chart_source':old['typed_controller']['origin_parameters'],'no_controller_search':True})
results={}
for name,ch in charts.items():
 maps=ch['maps'];v=ch['v']
 for p in range(4):
  for x in range(8):
   assert apply(maps[BAR[p]],apply(maps[p],x))==x
  assert apply(maps[BAR[p]],v[p])==v[BAR[p]]
  for x in range(8):
   for lam in [0,1]:
    y=apply(maps[p],x)^(v[p]if lam else 0)
    reverse={apply(maps[BAR[p]],y)^(v[BAR[p]]if mu else 0)for mu in [0,1]}
    assert x in reverse
 def image(w,x):
  current={x}
  for p in w:
   current={apply(maps[p],y)^(v[p]if lam else 0)for y in current for lam in [0,1]}
  return current
 ranks=[]
 for w in words:
  im=image(w,0);size=len(im);assert size in [1,2,4,8]
  ranks.append({'word':w,'rank':size.bit_length()-1,'zero_source_image':sorted(im)})
 packet_ranks=[len(image(w,0)).bit_length()-1 for w in packets]
 rows=[]
 for x in range(8):
  pimages=[image(w,x)for w in packets]
  total=set().union(*(image(w,x)for w in words))
  packet=set().union(*pimages)
  rows.append({'source_x':x,'packet_word_images':[sorted(z)for z in pimages],'packet_union':sorted(packet),'packet_covered':len(packet),'all_routes_union':sorted(total),'all_routes_covered':len(total),'all_routes_missing':sorted(set(range(8))-total)})
 results[name]={'complete_inverse_checks':True,'maps_column_codes':maps,'forward_offset_codes':v,'individual_actual_route_ranks':ranks,'three_packet_ranks':packet_ranks,'source_rows':rows,'maximum_individual_rank':max(x['rank']for x in ranks)}
p0=all(c['complete_inverse_checks']for c in results.values())
p1=all(r['packet_covered']==r['all_routes_covered']==8 for r in results['ARC']['source_rows'])and results['ARC']['maximum_individual_rank']<=2
p2=all(r['packet_covered']==6 and r['all_routes_covered']==7 for r in results['COLLINEAR']['source_rows'])and results['COLLINEAR']['source_rows'][0]['all_routes_missing']==[7]
result={'status':'COMPLETE_ACTUAL_PAIR_CONTROLLED_BINARY_PACKET_TEST','controller_pair':[s,t],'actual_le3_route_count':len(words),'predictions':{'P0_fullinverse_both':p0,'P1_arc_packet_full_without_rank3':p1,'P2_legal_collinear_packet6_total7':p2},'charts':results,'actual_native_CPU':time.process_time()-START,'prior_CPU':PRIOR,'case_CPU':PRIOR+time.process_time()-START,'case_cap':10,'graph_controllergeneration_BFS_Lean_ARIS_solver':0,'new_accepted_graph_parameter_Lean':[0,0,0],'scope':'one actualC30adjacentpair, two fixedinverse-compatibleF2charts, eight sourcecoordinates; no diagonal/nonadjacent/C32fullclaim','next':'STOP_LOCAL_TEST; preserve Fano4arc directions for nextgeneration; nonCayleyC32 or othereligiblecontroller still missing','terminal':True}
save('RESULT.json',result);save('TERMINAL.json',result)
print(json.dumps({'status':result['status'],'routecount':len(words),'predictions':result['predictions'],'ARC_packet_counts':[r['packet_covered']for r in results['ARC']['source_rows']],'COLLINEAR_packet_counts':[r['packet_covered']for r in results['COLLINEAR']['source_rows']],'COLLINEAR_total_counts':[r['all_routes_covered']for r in results['COLLINEAR']['source_rows']],'case_CPU':result['case_CPU'],'newgraphs':0},ensure_ascii=False),flush=True)
