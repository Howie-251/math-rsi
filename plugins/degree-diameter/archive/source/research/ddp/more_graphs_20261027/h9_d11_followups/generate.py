"""Reproduce any acceptedprefix of this fixedliteralH9 degree11sequence."""
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
def generate(output,prefix=None):
 data=json.loads((HERE/'parameters.json').read_text())
 if prefix is None:prefix=len(data['extensions'])
 assert 0<=prefix<=len(data['extensions'])
 output=Path(output)
 protected={HERE/data['final_edge_file'],ROOT/data['initial_verified_graph']}
 if output.resolve() in {p.resolve() for p in protected}:
  raise ValueError('Useaseparatereproductionoutput;preservetheverificationartifacts.')
 edges=[];n=0
 with (ROOT/data['source_file']).open() as f:
  for line in f:
   if not line.strip() or line.startswith('#'):continue
   row=list(map(int,line.split()));assert row[0]==n
   edges.extend((n,v) for v in row[1:] if n<v);n+=1
 assert n==37628 and len(edges)==205296
 sequence=[data['initial_verified_addition']]+[r['new_neighbors'] for r in data['extensions'][:prefix]]
 for pins in sequence:
  assert len(pins)==len(set(pins))<=11 and all(0<=p<n for p in pins)
  edges.extend((p,n) for p in pins);n+=1
 edges.sort();output.write_text(f'{n} {len(edges)}\n'+''.join(f'{u} {v}\n' for u,v in edges))
if __name__=='__main__':
 generate(sys.argv[1] if len(sys.argv)>1 else HERE/'reproduced_final.edges',int(sys.argv[2]) if len(sys.argv)>2 else None)
