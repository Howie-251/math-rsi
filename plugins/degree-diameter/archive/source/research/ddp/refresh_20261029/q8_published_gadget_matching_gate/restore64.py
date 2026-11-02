"""Bind one published witness to cube+extra adjacency. No distance computation."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import json,os,resource,time
D=Path(__file__).resolve().parent
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
t,c=time.monotonic(),time.process_time()
(D/'HANDLE.json').write_text(json.dumps({'pid':os.getpid(),'status':'RUNNING','hard_cpu_seconds':5,'workers':1},indent=2)+'\n')
w=json.loads((D/'PUBLISHED_WITNESS_FILTERED.json').read_text())
assert (w['q'],w['d'],w['k'],w['n'],w['t'])==(8,14,3,1088,3)
assert w['Xp']==[1,2,4]
# Retain mathematical source fields; no unrelated pinned-digest metadata.
w={k:w[k] for k in ('construction','d','k','n','q','field','X','Xp','t','gadget')}
w['cube_encoding']='8*pencil+l; l xor1,2,4'
(D/'PUBLISHED_WITNESS_FILTERED.json').write_text(json.dumps(w,indent=2)+'\n')
extra=sorted(tuple(sorted(e)) for e in w['gadget'])
assert len(extra)==96 and len(set(extra))==96
assert all(0<=u<v<64 and u//8!=v//8 for u,v in extra)
cube=sorted({tuple(sorted((8*a+l,8*a+(l^x)))) for a in range(8) for l in range(8) for x in w['Xp']})
assert len(cube)==96 and not set(cube)&set(extra)
A=[set() for _ in range(64)];E=[set() for _ in range(64)]
for u,v in extra:E[u].add(v);E[v].add(u)
for u,v in cube+extra:A[u].add(v);A[v].add(u)
assert Counter(map(len,E))=={3:64}
assert Counter(map(len,A))=={6:64}
out={'adjacency':[sorted(x) for x in A],'extra_edges':extra,'cube_encoding':w['cube_encoding'],
     'cube_edges':cube,'vertex_coordinates':[[v//8,v%8] for v in range(64)],
     'source_credit':{'author':'Rishabh Rajiv','DOI':'10.5281/zenodo.23052995','paper_section':'2, PDFpage4','archive_member':'witnesses/fq_d14_k3_n1088.json','main1088_graph_read':False},
     'source_K_D3':'published witness assertion inherited; no BFS or distance recomputation here'}
(D/'PUBLISHED_K64.json').write_text(json.dumps(out,indent=2)+'\n')
(D/'extra96.edges').write_text('64 96\n'+''.join(f'{u} {v}\n' for u,v in extra))
(D/'K64_192.edges').write_text('64 192\n'+''.join(f'{u} {v}\n' for u,v in sorted(cube+extra)))
cpu,wall=time.process_time()-c,time.monotonic()-t
r={'status':'PUBLISHED_K64_SOURCE_READY','n':64,'cube_edges':96,'cube_degree_histogram':{3:64},'extra_edges':96,'extra_degree_histogram':{3:64},'K_edges':192,'K_degree_histogram':{6:64},'cube_extra_disjoint':True,'extra_cross_pencil':True,'labels':'vertex=8*pencil+l, pencil0..7,l0..7=bits1,x,x2','published_K_D3_inherited':True,'source_distance_BFS':0,'solver_calls':0,'matching_searches':0,'main1088_graphs_read':0,'cpu_seconds':cpu,'wall_seconds':wall,'pid':os.getpid()}
(D/'RESULT.json').write_text(json.dumps(r,indent=2)+'\n')
(D/'HANDLE.json').write_text(json.dumps({'pid':os.getpid(),'status':'TERMINAL','exit_code':0,'cpu_seconds':cpu,'wall_seconds':wall},indent=2)+'\n')
(D/'TERMINAL.json').write_text(json.dumps({'status':r['status'],'pending':[],'new_tasks_started':0},indent=2)+'\n')
print(json.dumps(r,indent=2))
