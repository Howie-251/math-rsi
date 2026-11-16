"""Exact formula and old-matching orientation check; no graph-distance traversal."""
from pathlib import Path
from array import array
import json,resource,time
P=Path(__file__).resolve().parent;AR=P.parents[5]
resource.setrlimit(resource.RLIMIT_CPU,(3,3));start=time.process_time()
def binary(name,kind):
 a=array(kind);a.frombytes((P/name).read_bytes());return a
tau=binary('tau.i32.bin','i');pi=binary('pi.u16.bin','H');lines=binary('line_points.i32.bin','i')
tinv=[0]*len(tau)
for u,v in enumerate(tau):tinv[v]=u
cl=json.loads((AR/'research/ddp/more_graphs_20261027/h9_other_degrees/fold11_classes.json').read_text())
j=json.loads((P.parent/'h9_binding/JOINT_INPUT.json').read_text());cand=json.loads((P.parent/'h9_joint_gate/batch202/CANDIDATE.json').read_text())
pins=set(cand['pins']);colors={int(k):v for k,v in cand['colors'].items()};oldcolors={r['fold']:r['color']for r in cl['split_color_parity']}
edges=set();olddeg=[0]*37631
with(P/'source.edges').open()as f:
 n,m=map(int,next(f).split())
 for s in f:
  u,v=map(int,s.split());edges.add((min(u,v),max(u,v)));olddeg[u]+=1;olddeg[v]+=1
actual=list((P/'degrees.u8.bin').read_bytes());same={f:0 for f in colors};parent={f:f for f in colors}
def find(x):
 while parent[x]!=x:parent[x]=parent[parent[x]];x=parent[x]
 return x
for f,g in j['split_edges']:
 parent[find(f)]=find(g)
 if colors[f]==colors[g]:same[f]+=1;same[g]+=1
splitpins=set()
for r in j['split_fibers']:
 f=r['fold']
 for p,e in zip(r['actual_pins'],r['external_loads']):
  splitpins.add(p);assert actual[p]==10+same[f]+e+(p in pins),(p,actual[p],10+same[f]+e+(p in pins))
assert all(actual[p]==olddeg[p]+(p in pins)for p in range(37631)if p not in splitpins)
assert actual[37631]==10
def raw(f):
 p=cl['point_representatives'][f];return[p,tau[tau[p]]]
def matching(f,g,bit):
 out=set()
 for a,b in[(f,g),(g,f)]:
  targets=set(cl['classes'][b])
  for p in raw(a):
   l=tau[p]if oldcolors[a]^bit else tinv[p]
   for q in lines[(l-66430)*10:(l-66430+1)*10]:
    u,v=pi[p],pi[q]
    if v in targets and u!=v:out.add((min(u,v),max(u,v)))
 return out
allowed={find(f):{0,1}for f in colors};checked=0;witness={}
for f,g in j['split_edges']:
 if oldcolors[f]==oldcolors[g]:continue
 old={(min(u,v),max(u,v))for u in cl['classes'][f]for v in cl['classes'][g]if(min(u,v),max(u,v))in edges}
 assert len(old)==2
 good={b for b in[0,1]if matching(f,g,b)==old};root=find(f);allowed[root]&=good;checked+=1
 assert allowed[root],('inconsistent old sigma',f,g,good)
 if len(good)==1 and root not in witness:witness[root]={'f':f,'g':g,'bit':next(iter(good)),'old_matching':sorted(old)}
components={}
for f in colors:components.setdefault(find(f),[]).append(f)
oldeps=bytearray(66430)
for f in colors:
 for p in raw(f):oldeps[p]=oldcolors[f]^min(allowed[find(f)])
regenerated=set();oldsigma=array('i')
for p in range(66430):
 l=tau[p]if oldeps[p]else tinv[p];oldsigma.append(l)
 for q in lines[(l-66430)*10:(l-66430+1)*10]:
  u,v=pi[p],pi[q]
  if u!=v:regenerated.add((min(u,v),max(u,v)))
oldcore={(u,v)for u,v in edges if v<37471}
assert regenerated==oldcore,('oldcore identity',len(oldcore-regenerated),len(regenerated-oldcore))
(P/'old_sigma.i32.bin').write_bytes(oldsigma.tobytes())
result={'status':'EXACT_DEGREE_FORMULA_AND_OLD_ORIENTATION_PASS','split_endpoint_degrees_checked':len(splitpins),'immutable_and_exterior_degrees_checked':37631-len(splitpins),'new_degree':10,'oppositecolor_edges_compared':checked,'components':len(components),'component_sizes':sorted(map(len,components.values())),'old_rootbits':[{'root':r,'size':len(components[r]),'allowed_bits':sorted(bs),'witness':witness.get(r)}for r,bs in sorted(allowed.items())],'candidate_changed':False,'full_old_core_edge_identity_checked':True,'old_core_edges':len(oldcore),'missing_old_core_edges':0,'extra_old_core_edges':0,'CPU':time.process_time()-start}
(P/'FORMULA_ORIENTATION.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result),flush=True)
