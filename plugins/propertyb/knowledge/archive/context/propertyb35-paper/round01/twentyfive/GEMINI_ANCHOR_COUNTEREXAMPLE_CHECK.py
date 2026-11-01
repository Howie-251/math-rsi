"""Check Gemini's actual a5 example refuting universal fixed-anchor solvability.
For each anchor, exhaust the old seven-label/one-external-flip family with
anchor color blue; complementary colorings cover anchor color red.
"""
from pathlib import Path
from itertools import combinations
import json,time
P=Path(__file__).resolve().parent;st=time.perf_counter();full=2**25-1
ray=[[1,2,3,4],[5,10,15,20],[6,12,18,24],[7,14,16,23],[8,11,19,22],[9,13,17,21]]
G=[[0]+ray[4][:2]+ray[5][:2],ray[0][:3]+ray[1][:2],ray[0][3:]+ray[1][2:]+ray[4][2:3]+ray[5][2:3],ray[2][:3]+ray[3][:2],ray[2][3:]+ray[3][2:]+ray[4][3:]+ray[5][3:]]
G=[sorted(g) for g in G];assert sorted(v for g in G for v in g)==list(range(25))
L=[sorted(5*x+y for x in range(5) for y in range(5) if x==t) for t in range(5)]
L += [sorted(5*x+(m*x+t)%5 for x in range(5)) for m in range(5) for t in range(5)]
assert len({tuple(e) for e in L})==30 and all(g not in L for g in G)
E=L+G; Em=[sum(1<<v for v in e) for e in E];owner={v:i for i,g in enumerate(G) for v in g}
assert len({tuple(e) for e in E})==35
assert all(sum(v in e for e in E)==7 for v in range(25))
assert all(sum(u in e and v in e for e in E)==(2 if owner[u]==owner[v] else 1) for u,v in combinations(range(25),2))
records=[]
for x in range(25):
 gi=owner[x];gg=G[gi];outside=[v for v in range(25) if owner[v]!=gi]
 anchor=[j for j,e in enumerate(E) if x in e];assert len(anchor)==7
 lab={v:[t for t,j in enumerate(anchor) if v in E[j]] for v in outside};assert all(len(z)==1 for z in lab.values())
 masks=[sum(1<<v for v in outside if lab[v][0]==t) for t in range(7)]
 local_masks=[sum(1<<v for i,v in enumerate([z for z in gg if z!=x]) if m>>i&1) for m in range(16)]
 n=0;byflip={};first=None
 for flip in [None]+[i for i in range(5) if i!=gi]:
  flipmask=0 if flip is None else sum(1<<v for v in G[flip]);nf=0
  for b in range(128):
   outside_red=flipmask
   for t,mask in enumerate(masks):
    if b>>t&1:outside_red^=mask
   for gm in local_masks:
    red=outside_red|gm
    if all(0<(red&em)<em for em in Em):
     n+=1;nf+=1
     if first is None:first=dict(flip=flip,label_mask=b,red=sorted(v for v in range(25) if red>>v&1))
  byflip[str(flip)]=nf
 records.append(dict(anchor=x,group_index=gi,scheme_count=10240,successes=n,successes_by_flip=byflip,first_success=first))
assert records[0]['successes']==0
# A proper coloring found in the already certified affine color family.
col=json.loads((P/'AFFINE_AUGMENTATION.json').read_text())['color_orbit']; proper=None
for row in col:
 r=row['red_mask']
 if all(0<(r&em)<em for em in Em):proper=sorted(v for v in range(25) if r>>v&1);break
assert proper is not None
out=dict(scope=__doc__,vertices=list(range(25)),ray_order=ray,groups=G,edges=E,all_groups_nonlines=True,degree7_and_exact_paircodegrees_verified=True,per_anchor=records,proper_red_from_affine_family=proper,per_edge_red_counts=[len(set(e)&set(proper)) for e in E],summary=dict(failed_anchors=[r['anchor'] for r in records if not r['successes']],successful_anchors=[r['anchor'] for r in records if r['successes']],schemes_per_anchor=10240,total_schemes=25*10240,elapsed_seconds=time.perf_counter()-st))
(P/'GEMINI_ANCHOR_COUNTEREXAMPLE_CHECK.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out['summary'],indent=2));print('groups',G);print('proper_red',proper)
