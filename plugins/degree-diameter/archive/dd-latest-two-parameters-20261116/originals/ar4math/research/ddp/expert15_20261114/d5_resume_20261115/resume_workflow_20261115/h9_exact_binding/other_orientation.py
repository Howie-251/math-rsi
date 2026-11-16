"""One effective component complement, fixed same-edge/P; no search or BFS."""
from pathlib import Path
from array import array
import json,resource,time,os
P=Path(__file__).resolve().parent;R=P.parent;AR=P.parents[5]
resource.setrlimit(resource.RLIMIT_CPU,(4,4));start=time.process_time();wall=time.monotonic()
O=R/'h9_other_orientation';O.mkdir(exist_ok=False)
def binary(name,kind):
 a=array(kind);a.frombytes((P/name).read_bytes());return a
result={}
try:
 tau=binary('tau.i32.bin','i');pi=binary('pi.u16.bin','H');lines=binary('line_points.i32.bin','i');tinv=[0]*len(tau)
 for u,v in enumerate(tau):tinv[v]=u
 eps=bytearray((P/'eps.u8.bin').read_bytes());cl=json.loads((AR/'research/ddp/more_graphs_20261027/h9_other_degrees/fold11_classes.json').read_text())
 orient=json.loads((P/'FORMULA_ORIENTATION.json').read_text());isolated={r['root']for r in orient['old_rootbits']if r['size']==1}
 c=json.loads((R/'h9_joint_gate/batch202/CANDIDATE.json').read_text());old={r['fold']:r['color']for r in cl['split_color_parity']};colors={}
 for f in cl['split_fold_ids']:
  value=old[f]if f in isolated else 1-c['colors'][str(f)];colors[f]=value
  p=cl['point_representatives'][f];q=tau[tau[p]];eps[p]=eps[q]=value
 assert sum(colors[f]!=old[f]for f in colors)==105
 edges=set();sigma=array('i')
 for p in range(66430):
  l=tau[p]if eps[p]else tinv[p];sigma.append(l)
  for q in lines[(l-66430)*10:(l-66430+1)*10]:
   u,v=pi[p],pi[q]
   if u!=v:edges.add((min(u,v),max(u,v)))
 assert len(edges)==203747
 oldcore=set();outside=set()
 with(P/'source.edges').open()as f:
  n,m=map(int,next(f).split());assert n==37631
  for s in f:
   u,v=map(int,s.split());e=(min(u,v),max(u,v));(oldcore if e[1]<37471 else outside).add(e)
 missing=len(oldcore-edges);extra=len(edges-oldcore);edges|=outside
 for p in c['pins']:edges.add((p,37631))
 degrees=[0]*37632
 for u,v in edges:degrees[u]+=1;degrees[v]+=1
 assert max(degrees)==11 and degrees[37631]==10
 assert degrees==list((P/'degrees.u8.bin').read_bytes())
 (O/'eps.u8.bin').write_bytes(eps);(O/'sigma.i32.bin').write_bytes(sigma.tobytes());(O/'degrees.u8.bin').write_bytes(bytes(degrees))
 (O/'CANDIDATE.json').write_text(json.dumps({'plane_id':605,'colors':colors,'pins':c['pins'],'operation':'complement4060component;isolatedoldcolors','old_color_differences':105},separators=(',',':'))+'\n')
 with(O/'candidate37632.edges').open('w')as f:
  f.write(f'37632 {len(edges)}\n')
  for u,v in sorted(edges):f.write(f'{u} {v}\n')
 result={'status':'OTHER_EFFECTIVE_ORIENTATION_BOUND','n':37632,'m':len(edges),'core_n':37471,'core_m':203747,'max_degree':11,'new_degree':10,'same_degree_vector_as_canonical':True,'retained_exterior_edges':len(outside),'old_core_removed_edges':missing,'old_core_added_edges':extra,'changed_colors_relative_true_old':105,'geometry_rebuilt':False,'BFS_run':False,'new_graph_accepted':False}
except Exception as e:result={'status':'ERROR_OR_LIMIT','error':str(e),'new_graph_accepted':False}
finally:
 result.update(whole_CPU=time.process_time()-start,whole_wall=time.monotonic()-wall,whole_CPU_cap=4,running=False)
 (O/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
