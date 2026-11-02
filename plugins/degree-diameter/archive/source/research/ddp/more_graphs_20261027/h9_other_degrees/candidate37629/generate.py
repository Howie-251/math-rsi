"""Reproduce the fixed37629witness; never overwrites its independentchecked edge artifact."""
from pathlib import Path
import json,sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[4]
def generate(output):
 p=json.loads((HERE/'params.json').read_text())
 output=Path(output)
 if output.resolve()==(HERE/p['verified_edge_file']).resolve():
  raise ValueError('Use a separate reproduction output; the checked edge table is preserved.')
 edges=[];n=0
 with (ROOT/p['source_file']).open() as f:
  for line in f:
   if not line.strip() or line.startswith('#'):continue
   row=list(map(int,line.split()));assert row[0]==n
   edges.extend((n,v) for v in row[1:] if n<v);n+=1
 assert n==p['source_n'] and len(edges)==p['source_m']
 pins=p['new_neighbors'];assert len(pins)==len(set(pins))==11
 edges.extend((v,n) for v in pins);edges.sort()
 assert len(edges)==p['m']
 output.write_text(f"{n+1} {len(edges)}\n"+''.join(f"{u} {v}\n" for u,v in edges))
if __name__=='__main__':
 generate(sys.argv[1] if len(sys.argv)>1 else HERE/'reproduced.edges')
