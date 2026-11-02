"""Retain every literal source edge and append one certified pin neighborhood."""
import argparse,json
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument('--parameters',type=Path,default=Path(__file__).with_name('HIT.json'))
parser.add_argument('--output',type=Path,required=True)
args=parser.parse_args();p=json.loads(args.parameters.read_text());source=Path(p['source_file'])
pins=p['pins'];n=p['source_n'];m=p['source_m']
assert len(set(pins))==len(pins)<=14 and n==94186
with source.open() as old,args.output.open('w') as out:
    out.write(f'{n+1} {m+len(pins)}\n');count=0
    for line in old:
        if not line.strip() or line.lstrip().startswith('#'):continue
        u,v=map(int,line.split());assert 0<=u<n and 0<=v<n
        out.write(f'{u} {v}\n');count+=1
    assert count==m
    for v in pins:out.write(f'{n} {v}\n')
