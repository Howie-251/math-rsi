"""Migrate the finite native geometry screen to current42345 degrees only."""
from pathlib import Path
from array import array
import json
import resource
import subprocess
import time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
START=time.process_time()
children_start=resource.getrusage(resource.RUSAGE_CHILDREN)
assert json.loads((OUT/'PREDICTION.json').read_text())['frozen_before_currentbase_degree_enumeration']
source=OUT.parent/'h9_d12_followups/graphs/graph_d12_D5_n42345.edges'
# The native kernel only needs current degrees; this data file is not a new graph.
with source.open() as f:
 n,m=map(int,f.readline().split());degree=[0]*n;count=0
 for line in f:
  u,v=map(int,line.split());degree[u]+=1;degree[v]+=1;count+=1
assert (n,m,count,max(degree))==(42345,245253,245253,12)
(OUT/'current_degree.txt').write_text(''.join(f'{v} {d}\n' for v,d in enumerate(degree)))
(OUT/'excluded_centers.txt').write_text('')

# Keep the completedN11 artifact unchanged. Store the literal migrated native source here.
text=(OUT.parent/'h9_global_line_pool/enumerate.cpp').read_text()
old='require(*max_element(fold.begin(),fold.end())==37470,"wrongN11core mapping");'
new='require(*max_element(fold.begin(),fold.end())==41355,"wrongN12core mapping");'
assert old in text;text=text.replace(old,new)
old='require(excluded.size()==118,"expected118 previously exhausted centers");'
new='require(excluded.empty(),"D12currentbase enumerates all centers");'
assert old in text;text=text.replace(old,new)
old='int u,v,d=0;s>>u;require(u==int(degree.size()),"wrongraw rows");while(s>>v)d++;degree.push_back(d);'
new='int u,d;s>>u>>d;require(u==int(degree.size()),"wrongdegree rows");degree.push_back(d);'
assert old in text;text=text.replace(old,new)
text=text.replace('degree.size()==37628','degree.size()==42345').replace('==11,"wrongN11 source"','==12,"wrongN12 source"').replace('sum==410592','sum==490506').replace('wrongN11edgecount','wrongN12edgecount')
text=text.replace('degree[fold[p]]>=11','degree[fold[p]]>=12')
text=text.replace('66312','66430').replace('9558','0')
text=text.replace('base_n\\\":37628','base_n\\\":42345').replace('target_degree\\\":11','target_degree\\\":12')
text=text.replace('<<11-r.pins.size()','<<12-r.pins.size()')
text=text.replace('reused_exhausted_centers\\\":118','reused_exhausted_centers\\\":0')
(OUT/'enumerate.cpp').write_text(text)
compile_start=resource.getrusage(resource.RUSAGE_CHILDREN)
subprocess.run(['g++','-O3','-std=c++17',str(OUT/'enumerate.cpp'),'-o',str(OUT/'enumerate')],check=True)
compile_end=resource.getrusage(resource.RUSAGE_CHILDREN)
compile_cpu=(compile_end.ru_utime+compile_end.ru_stime)-(compile_start.ru_utime+compile_start.ru_stime)
geo=ROOT/'research/ddp/global_coverage_20261027/h9_quadric_line_signature'
args=[str(OUT/'enumerate'),str(geo/'point_coords.u8.bin'),str(geo/'point_to_core.u16.bin'),
      str(OUT/'current_degree.txt'),str(OUT/'excluded_centers.txt'),str(OUT),'7']
with (OUT/'native.log').open('w') as log:subprocess.run(args,stdout=log,stderr=log,check=True)
d=json.loads((OUT/'native_result.json').read_text())
pool=json.loads((OUT/'pool.json').read_text())
assert pool['base_n']==42345 and pool['target_degree']==12
for r in pool['records']:
 assert r['anchor_cap']==12-len(r['pins'])
 assert all(degree[v]<12 for v in r['pins'])
 r['remaining_anchor_capacity']=r['anchor_cap']
 r['pin_current_degrees']=[degree[v] for v in r['pins']]
(OUT/'pool.json').write_text(json.dumps(pool,indent=2)+'\n')
children_end=resource.getrusage(resource.RUSAGE_CHILDREN)
child_cpu=(children_end.ru_utime+children_end.ru_stime)-(children_start.ru_utime+children_start.ru_stime)
d.update(prediction_id='N12_GLOBAL_Q_LINE_DEGREE_POOL_ON_42345',source_n=n,source_m=m,target_degree=12,target_D=5,
 source_graph='../h9_d12_followups/graphs/graph_d12_D5_n42345.edges',
 source_independent_check='../h9_d12_followups/graphs/independent_all_source_BFS_42345.json',
 compile_CPU_seconds=compile_cpu,total_children_CPU_seconds=child_cpu,
 preparation_CPU_seconds=time.process_time()-START,total_CPU_seconds=child_cpu+time.process_time()-START,
 pending=[] if d['complete_all66430_center_scope'] else ['unprocessed centers UNKNOWN; no automatic continuation'],
 BFS_performed=False,old_coverage_profiles_retried=False,anchors_optimized=False,new_graph_generated=False)
(OUT/'RESULT.json').write_text(json.dumps(d,indent=2)+'\n')
print(json.dumps(d,indent=2))
