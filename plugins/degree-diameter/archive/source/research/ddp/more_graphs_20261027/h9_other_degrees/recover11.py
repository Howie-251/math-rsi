"""One fixed<=20-round WL inverse-labelling test; no S-search or incidence reconstruction."""
from pathlib import Path
from collections import Counter,defaultdict,deque
from array import array
from datetime import datetime,timezone
import json,lzma,resource,sys,time
resource.setrlimit(resource.RLIMIT_CPU,(60,60))
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3]
sys.path.insert(0,str(ROOT/'aris_repo/tools'));from capture_filter import screen
start=time.process_time()
pred=dict(status='FROZEN_BEFORE_WL',prediction_id='N11_WL_RECOVERS_ACTUAL4074_FOLD',
          timestamp=datetime.now(timezone.utc).isoformat(),
          hypothesis='Bare37471 degree<10 singleton anchors preservephi and WL yields33397 classes:4074pairs+29323singletons.',
          fixed_iterations_at_most=20,CPU_limit=60,
          checks='ExactquotientFedgeidentity, simultaneouspairswapautomorphism, originalpointlabelorder; do notforce classes>2 or assumeoldS3075=currentS4074.',
          no_new_geometry=True)
s=json.dumps(pred,indent=2)+'\n';assert not screen(s);(HERE/'P11_WL_PREDICTION.json').write_text(s)
source=ROOT/'research/ddp/breadth_20261027_wave4/pencil_source/deg11_diam5_n37628.txt'
adj=[]
for line in source.read_text().splitlines():
 if line.strip() and not line.startswith('#'):
  row=list(map(int,line.split()));assert row[0]==len(adj);adj.append(row[1:])
assert len(adj)==37628 and max(map(len,adj))==11
N=37471;core=[sorted(v for v in adj[u] if v<N) for u in range(N)]
deg=list(map(len,core));anchors=[u for u in range(N) if deg[u]<10]
def colorize(signatures):
 table={};out=[]
 for s in signatures:
  if s not in table:table[s]=len(table)
  out.append(table[s])
 return out
colors=colorize([(0,u) if deg[u]<10 else (1,deg[u]) for u in range(N)])
history=[]
for it in range(1,21):
 new=colorize([(colors[u],tuple(sorted(colors[v] for v in core[u]))) for u in range(N)])
 bins=defaultdict(list)
 for u,c in enumerate(new):bins[c].append(u)
 hist=Counter(map(len,bins.values()));history.append(dict(iteration=it,classes=len(bins),size_histogram=dict(sorted(hist.items()))))
 same=new==colors;colors=new
 if len(bins)==33397 and hist==Counter({1:29323,2:4074}):break
 if same:break
classes=sorted(bins.values(),key=min)
r=dict(status='WL_SCOPE_INCOMPLETE',n=N,source_n=37628,old_witness_core_n=36472,old_witness_S=3075,
       hypothesized_current_S=4074,anchors=len(anchors),bare_degree_histogram=dict(Counter(deg)),iterations=history,
       classes=len(classes),class_size_histogram=dict(sorted(Counter(map(len,classes)).items())),
       mapping_restored=False,old_S_assumed_unchanged=False,geometry_reconstructed=False,BFS_count=0)
if len(classes)==33397 and all(len(x)<=2 for x in classes):
 class_of=[0]*N;swap=list(range(N))
 for k,vs in enumerate(classes):
  for v in vs:class_of[v]=k
  if len(vs)==2:swap[vs[0]],swap[vs[1]]=vs[1],vs[0]
 assert all(sorted(swap[v] for v in core[u])==core[swap[u]] for u in range(N))
 quotient={tuple(sorted((class_of[u],class_of[v]))) for u in range(N) for v in core[u] if u<v}
 BASE=ROOT/'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout'
 F=set()
 with lzma.open(BASE/'duality_source/graph_d10k5_n33397.edges.xz','rt') as f:
  fn,fm=map(int,next(f).split());assert(fn,fm)==(33397,166425)
  for line in f:
   u,v=map(int,line.split());F.add((u,v))
 assert quotient==F
 qdata=json.loads((BASE/'Q_data.json').read_text());reps=[None]*33397
 for folds,points in [(qdata['generic_fold_ids'],qdata['generic_point_representatives']),(qdata['H3_fold_ids'],qdata['H3_point_representatives'])]:
  for f,p in zip(folds,points):reps[f]=p
 with lzma.open(BASE/'partial_fold_source/tau.txt.xz','rt') as f:tau=list(map(int,f.read().split()))
 phi=[tau[tau[p]] for p in range(66430)]
 fold=[-1]*66430;lab=[]
 for k,vs in enumerate(classes):
  p=reps[k];q=phi[p]
  if len(vs)==1:
   fold[p]=fold[q]=vs[0];lab.append((p,vs[0]))
  else:
   assert p<q
   fold[p],fold[q]=vs;lab.extend([(p,vs[0]),(q,vs[1])])
 assert [v for p,v in sorted(lab)]==list(range(N))
 assert min(fold)==0 and max(fold)==N-1
 (HERE/'point_to_core11.u16.bin').write_bytes(array('H',fold).tobytes())
 # Recover only the same/different colors implied by actual split-edge counts.
 split={k for k,vs in enumerate(classes) if len(vs)==2};constraints=defaultdict(list)
 for u,v in F:
  if u in split and v in split:
   c=sum(b in core[a] for a in classes[u] for b in classes[v]);assert c in(2,4)
   parity=0 if c==4 else 1;constraints[u].append((v,parity));constraints[v].append((u,parity))
 col={};components=0
 for s in sorted(split):
  if s in col:continue
  components+=1;col[s]=0;todo=[s]
  for u in todo:
   for v,p in constraints[u]:
    if v in col:assert col[v]==col[u]^p
    else:col[v]=col[u]^p;todo.append(v)
 # All edge multiplicities and local degree formulas are validated, without claiming a full incidence-voltage reconstruction.
 assert all(sum(b in core[a] for a in classes[u] for b in classes[v])==
            (2 if u in split and v in split and col[u]!=col[v] else len(classes[u])*len(classes[v])) for u,v in F)
 r.update(status='ACTUAL_FOLD_MAPPING_RESTORED',mapping_restored=True,split_fibers=len(split),
          exact_quotient_edges_match=True,simultaneous_pair_swap_automorphism=True,sorted_original_point_labels_match=True,
          point_to_core_file='point_to_core11.u16.bin',color_parity_consistent=True,color_components=components,
          edge_multiplicities_and_degree_model_match=True,
          geometry_orientation_scope='Actualsplitpairmatchingsare retained; abstractcolorsfrom2vs4edges recovered. NofullH9incidencevoltage regeneration attempted.')
 (HERE/'fold11_classes.json').write_text(json.dumps(dict(classes=classes,point_representatives=reps,
     split_fold_ids=sorted(split),split_color_parity=[dict(fold=k,color=col[k]) for k in sorted(split)]),separators=(',',':'))+'\n')
r['CPU_seconds']=time.process_time()-start
# Numeric class data stay in their own file; screen prose in this summary.
assert not screen('\n'.join(v for v in r.values() if isinstance(v,str)))
(HERE/'mapping11_result.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
