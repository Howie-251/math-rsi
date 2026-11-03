import json
from pathlib import Path
D=Path(__file__).resolve().parent
ROOT=D.parents[3]
OLD=D.parent/'f5_restricted_noise_d10_D4'
p=json.loads((OLD/'INPUT_PARAMETERS.json').read_text())
C=json.loads((ROOT/p['controller_source']).read_text())['controller']
triangles=json.loads((ROOT/'research/ddp/breadth_20261027_wave4/mizuno_d3_source/controller_structure.json').read_text())['triangles']
part={v:i for i,t in enumerate(triangles) for v in t}
types=[[int(part[a]==part[b]) for b in C[a]] for a in range(30)]
assert all(sum(row)==2 for row in types)
nums=(OLD/'INPUT.txt').read_text().split()
assert len(nums)==3121
(D/'INPUT.txt').write_text(' '.join(nums[:2620])+'\n'+' '.join(str(t) for row in types for t in row)+'\n'+' '.join(nums[2620:])+'\n')
p['allocation']='triangle edges3 and external edges2; coefficients forward u<v, inverse sign on reverse'
p['controller_edge_types']=types
p['triangle_axis_root0']=[i for i,t in enumerate(types[0]) if t]
(D/'INPUT_PARAMETERS.json').write_text(json.dumps(p,indent=2)+'\n')
source=(OLD/'run.cpp').read_text()
source=source.replace('int count;in>>count;', 'int typ[30][4];for(auto&row:typ)for(int&v:row)in>>v;\n int count;in>>count;')
old='for(int p=0;p<4;p++)for(int t:A[p])G[u].push_back(C[a][p]*125+M[p][t][x]);'
new='for(int p=0;p<4;p++){const auto&set=typ[a][p]?A[2]:A[0];for(int t:set){int coeff=a<C[a][p]?t:(5-t)%5;G[u].push_back(C[a][p]*125+M[p][coeff][x]);}}'
assert old in source
source=source.replace(old,new)
(D/'run.cpp').write_text(source)
print('New triangle/external branching allocation prepared; old finite-domain result untouched; no graph/BFS yet.')
