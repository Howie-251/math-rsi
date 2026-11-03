"""Actualdegree11fold: fixed122line witnesses and samecenter81-line degree pool."""
from pathlib import Path
from itertools import combinations,product
from collections import Counter
from array import array
from datetime import datetime,timezone
import json,resource,sys,time
resource.setrlimit(resource.RLIMIT_CPU,(90,90))
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
API=ROOT/'research/ddp/global_coverage_20261027/h9_quadric_line_signature';sys.path.insert(0,str(API))
from geometry import ADD as add,MUL as mul,INV as inv,normalize,line_points,on_quadric
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
start=time.process_time();assert json.loads((HERE/'mapping11_result.json').read_text())['mapping_restored']
pred=dict(prediction_id='N11_FIXED122_QCENTERS_DEGREE_POOL',status='FROZEN_BEFORE122IDENTIFICATION_AND81LINE_POOL',
          timestamp=datetime.now(timezone.utc).isoformat(),
          hypothesis='Actual122sourcepinsetscontainQlineimages; theirfixednonHlinecentersgiveadegree11feasiblepoolpossiblycompletablewithin11pins.',
          scope='Onlythese122sourceobjectsandall81linesperrecoveredcenter; no newcenters,fields,oldSsearchornewsource.',
          completion_policy='ReuseexistingexactR4cache. Trycompleteanchorcapwhen<=2; ifcap>2andno<=2completion,reportlargeranchorobligationwithoutoptimization.')
(HERE/'P11_GEOMETRY_PREDICTION.json').write_text(json.dumps(pred,indent=2)+'\n')
raw=(API/'point_coords.u8.bin').read_bytes();points=[tuple(raw[7*i:7*i+7]) for i in range(66430)];index={p:i for i,p in enumerate(points)}
fold=array('H');fold.frombytes((HERE/'point_to_core11.u16.bin').read_bytes());assert len(fold)==66430
lifts=[[] for _ in range(37471)]
for p,v in enumerate(fold):lifts[v].append(p)
source=ROOT/'research/ddp/breadth_20261027_wave4/pencil_source/deg11_diam5_n37628.txt';adj=[]
for line in source.read_text().splitlines():
 if line.strip() and not line.startswith('#'):
  row=list(map(int,line.split()));assert row[0]==len(adj);adj.append(row[1:])
degree=list(map(len,adj));assert len(adj)==37628 and max(degree)==11
neg=[(-a%3)%3+3*((-(a//3))%3) for a in range(9)]
sub=[[add[a][neg[b]] for b in range(9)] for a in range(9)]
EQ=[((1,2),(3,4)),((5,4),(3,2)),((2,0),(3,5)),((6,5),(3,0)),((0,1),(3,6)),((4,6),(3,1))]
def hline(x,z):
 def p(i,j):return sub[mul[x[i]][z[j]]][mul[x[j]][z[i]]]
 return all(p(a,b)==p(c,d) for (a,b),(c,d) in EQ)
def flatrows(x):
 r=[]
 for (a,b),(c,d) in EQ:
  t=[0]*7;t[b]=add[t[b]][x[a]];t[a]=sub[t[a]][x[b]];t[d]=sub[t[d]][x[c]];t[c]=add[t[c]][x[d]];r.append(t)
 return r+[[x[4],x[5],x[6],x[3],x[0],x[1],x[2]]]
def kernel(rows):
 a=[list(r) for r in rows];piv=[]
 for col in range(7):
  pr=next((i for i in range(len(piv),len(a)) if a[i][col]),None)
  if pr is None:continue
  r=len(piv);a[r],a[pr]=a[pr],a[r];a[r]=[mul[inv[a[r][col]]][x] for x in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][col]:
    fac=a[i][col];a[i]=[sub[x][mul[fac][y]] for x,y in zip(a[i],a[r])]
  piv.append(col)
 out=[]
 for f in range(7):
  if f not in piv:
   x=[0]*7;x[f]=1
   for i,p in enumerate(piv):x[p]=neg[a[i][f]]
   out.append(x)
 return out
subjects=[];tested=0
for vertex in range(37500,37622):
 A=sorted(v for v in adj[vertex] if v<37471);aset=set(A);seen=set();chosen=None;fallback=None;local=0
 for a,b in combinations(A,2):
  for p,q in product(lifts[a],lifts[b]):
   tested+=1;local+=1
   try:pts=line_points(points[p],points[q])
   except ValueError:continue
   ids=tuple(sorted(index[x] for x in pts))
   if ids in seen:continue
   seen.add(ids);pins=sorted({fold[x] for x in ids})
   if not set(pins)<=aset:continue
   isH=hline(points[p],points[q]);w=dict(point_labels=list(ids),line_basis=[list(points[p]),list(points[q])],pins=pins,extra_core_anchors=sorted(aset-set(pins)),is_H9_line=isH)
   if not isH:chosen=w;break
   if fallback is None:fallback=w
  if chosen is not None:break
 chosen=chosen or fallback
 row=dict(vertex=vertex,actual_core_pins=A,other_neighbors=sorted(v for v in adj[vertex] if v>=37471),matched=chosen is not None,tested_lift_pairs=local,witness=chosen)
 if chosen and not chosen['is_H9_line']:
  x,z=map(tuple,chosen['line_basis']);ker=kernel(flatrows(x)+flatrows(z));assert len(ker)==1
  y=normalize(ker[0]);assert on_quadric(y)
  row.update(center_original_label=index[y],center_coordinates=list(y))
 subjects.append(row)
(HERE/'degree11_line_witnesses.json').write_text(json.dumps(dict(records=subjects),indent=2)+'\n')
centers={r['center_original_label']:r for r in subjects if 'center_original_label'in r}
seenlines=set();seenpins=set();pool={};blocked=Counter();pin_hist=Counter();rawcount=0
for center,row in sorted(centers.items()):
 y=tuple(row['center_coordinates']);x,z=map(tuple,row['witness']['line_basis'])
 for a in range(9):
  u=normalize(tuple(sub[x[j]][mul[a][y[j]]] for j in range(7)))
  for b in range(9):
   v=normalize(tuple(sub[z[j]][mul[b][y[j]]] for j in range(7)));rawcount+=1
   pts=line_points(u,v);ids=tuple(sorted(index[p] for p in pts));assert not hline(u,v)
   if ids in seenlines:continue
   seenlines.add(ids);pins=tuple(sorted({fold[p] for p in ids}));seenpins.add(pins);pin_hist[len(pins)]+=1
   bad=[p for p in pins if degree[p]>=11];blocked[len(bad)]+=1
   if bad or len(pins)>11:continue
   w=dict(center_original_label=center,center_coordinates=list(y),source_vertex=row['vertex'],dual_parameters=[a,b],line_basis=[list(u),list(v)],point_labels=list(ids))
   if pins not in pool:pool[pins]=dict(pins=list(pins),anchor_cap=11-len(pins),pin_degrees=[degree[p] for p in pins],witnesses=[])
   pool[pins]['witnesses'].append(w)
records=[pool[k] for k in sorted(pool)]
result=dict(status='COMPLETE_FIXED122_CENTER_DEGREE_POOL',subjects=122,matched=sum(r['matched'] for r in subjects),
            H9_line_only=sum(r['matched'] and r['witness']['is_H9_line'] for r in subjects),nonH_centers=len(centers),
            unmatched_vertices=[r['vertex'] for r in subjects if not r['matched']],tested_lift_pairs=tested,
            raw81_lines=rawcount,unique_original_lines=len(seenlines),unique_fold_pinsets=len(seenpins),
            pin_size_histogram=dict(pin_hist),saturated_pin_histogram=dict(blocked),degree_feasible_distinct_pinsets=len(records),
            feasible_pin_size_histogram=dict(Counter(len(r['pins']) for r in records)),pool=records,
            graph_generated=False,incidence_reconstructed=False,BFS_count=0,CPU_seconds=time.process_time()-start)
assert not screen('\n'.join(v for v in result.values() if isinstance(v,str)))
(HERE/'degree11_pool.json').write_text(json.dumps(dict(base_n=37628,target_degree=11,records=records),indent=2)+'\n')
(HERE/'degree11_geometry_result.json').write_text(json.dumps({k:v for k,v in result.items() if k!='pool'},indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='pool'},indent=2))
