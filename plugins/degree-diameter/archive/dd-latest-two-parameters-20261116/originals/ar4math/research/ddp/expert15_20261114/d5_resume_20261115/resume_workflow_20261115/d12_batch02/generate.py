"""Reproduce every accepted prefix from actual G42419 and recorded neighborhoods."""
from pathlib import Path
import argparse,json
P=Path(__file__).resolve().parent
def main():
 p=argparse.ArgumentParser();p.add_argument('--prefix',type=int);p.add_argument('--output',type=Path,required=True);a=p.parse_args()
 steps=[json.loads(s)for s in(P/'ADDITIONS.jsonl').read_text().splitlines()if s]
 k=len(steps)if a.prefix is None else a.prefix;assert 0<=k<=len(steps)
 source=P.parent/'d12_batch01/graph_d12_D5_n42419.edges'
 with source.open()as f:
  n,m=map(int,next(f).split());edges=[tuple(map(int,s.split()))for s in f if s.strip()]
 assert n==42419 and m==246141 and len(edges)==m
 for row in steps[:k]:
  assert row['new_vertex']==n and row['source_n']==n
  edges.extend((v,n)for v in row['pins']);n+=1
 assert len(edges)==m+sum(len(row['pins'])for row in steps[:k])
 with a.output.open('w')as f:
  f.write(f'{n} {len(edges)}\n')
  for u,v in sorted(edges):f.write(f'{u} {v}\n')
 print(f'Reproduced prefix {k}: {n} vertices, {len(edges)} edges.')
if __name__=='__main__':main()
