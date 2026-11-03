import itertools,json
from pathlib import Path
D=Path(__file__).resolve().parent
ROOT=D.parents[3]
C=json.loads((ROOT/'research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json').read_text())['controller']
A=json.loads((D.parent/'f5_complementary_triples/MATRICES_AND_PENCILS.json').read_text())
L=A['directions']; inv=A['inverse_ports'];Ts=[p['T'] for p in A['ports']]
def digits(x):return (x%5,x//5%5,x//25)
def encode(x):return x[0]+5*x[1]+25*x[2]
def apply(T,x,t,v):return tuple((sum(T[i][j]*x[j] for j in range(3))+t*v[i])%5 for i in range(3))
maps=[[[encode(apply(Ts[p],digits(x),t,L[inv[p]])) for x in range(125)] for t in range(5)] for p in range(4)]
for a in range(30):
 for p in range(4):assert C[C[a][p]][inv[p]]==a
for p in range(4):
 for t in range(5):
  for x in range(125):assert maps[inv[p]][(-t)%5][maps[p][t][x]]==x
cases=[([1,4],[0,1,4])]
cases.extend((list(a),list(b)) for a in itertools.combinations(range(5),2) for b in itertools.combinations(range(5),3) if (list(a),list(b))!=cases[0])
assert len(cases)==100
with (D/'INPUT.txt').open('w') as f:
 f.write(' '.join(str(x) for row in C for x in row)+'\n')
 f.write(' '.join(str(x) for p in maps for t in p for x in t)+'\n')
 f.write('100\n')
 for a,b in cases:f.write(' '.join(map(str,a+b))+'\n')
(D/'INPUT_PARAMETERS.json').write_text(json.dumps(dict(controller_source='research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json',local_label='x0+5*x1+25*x2',matrices=Ts,directions=L,inverse_ports=inv,cases=[dict(A0=a,A2=b) for a,b in cases]),indent=2)+'\n')
print('Prepared 100 exact new graph rules; no BFS or graph generation.')
