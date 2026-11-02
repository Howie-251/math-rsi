import json,time
from pathlib import Path
p=Path(__file__).resolve().parent;start=time.process_time()
src=json.loads((p/'SOURCE.json').read_text());W=[tuple(v-1 for v in row) for row in src['W_images_1based']];I=tuple(range(32))
def mul(g,h):return tuple(h[g[j]] for j in range(32))
def inv(g):
 a=[0]*32
 for i,j in enumerate(g):a[j]=i
 return tuple(a)
G=[I];ix={I:0}
for g in G:
 for w in W:
  z=mul(g,w)
  if z not in ix:ix[z]=len(G);G.append(z)
assert len(G)==672
V=W+[inv(W[4]),inv(W[5])]
right=[[ix[mul(g,w)] for w in V] for g in G]
ports=[[(0,0),(0,1),(1,4),(1,5)],[(1,2),(1,3),(0,6),(0,7)]]
reach={(0,0)};shell={(0,0)};shellcounts=[1]
for depth in range(1,8):
 nextset={(c,right[g][j]) for b,g in shell for c,j in ports[b]}-reach
 reach|=nextset;shell=nextset;shellcounts.append(len(shell))
missing=[(b,g) for b in range(2) for g in range(672) if (b,g) not in reach]
r=dict(status='REVERSE_COMPOSITION_SOURCE_ROOT_R7_MATCH' if not missing else 'REVERSE_COMPOSITION_STILL_CONFLICT',composition='GAP right action: (g*W)[j]=W[g[j]]',group_order=len(G),single_projection_root=[0,0],projected_R7_reached=len(reach),projected_missing=len(missing),shell_counts=shellcounts,first_missing=missing[:1],source_allroot_BFS=0,candidate_graphs=0,CPU_seconds=time.process_time()-start)
(p/'SOURCE_BINDING_CHECK.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r))
