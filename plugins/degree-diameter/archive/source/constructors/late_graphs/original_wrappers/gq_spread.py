#!/usr/bin/env python3
"""Replay frozen formulas only. No solver, BFS, Lean or geometry search."""
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
BASE=HERE/'research/ddp/two_successful_methods_20261101/retained_edge_transfer'
def neighbors(data,p,l):
    width=len(data['lines'])
    u=width*p+l
    ns={width*q+m for q in data['lines'][l]['points'] for m in data['point_incident_lines'][p]}
    ns.discard(u)
    if l in data['point_incident_lines'][p]:ns.add(width*width+data['point_spread_owner'][p])
    return ns

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--order',type=int,choices=[7242,7531,160050],required=True);ap.add_argument('--output',type=Path,required=True);a=ap.parse_args()
    if a.output.exists():raise FileExistsError(a.output)
    folder=BASE/('opposite_gq77_spread64' if a.order==160050 else 'opposite_gq44_spread25')
    d=json.loads((folder/'PARAMETERS.json').read_text());width=len(d['lines']);old=width*width
    bonus=[{width*p+l for p in item['points'] for l in d['point_incident_lines'][p]} for item in d['spread']]
    extra={}
    if a.order==7531:
        rows=json.loads((folder/'ovoid_product26/IMMUTABLE_SOURCE_PINS.json').read_text())['rows']
        for row in rows:
            for pin in row['original_source_pins']:extra.setdefault(pin,[]).append(7242+row['index'])
    expected={7242:90525,7531:97750,160050:5121600}[a.order]
    with a.output.open('x') as out:
        out.write(f'{a.order} {expected}\n')
        for u in range(old+len(bonus)):
            ns=neighbors(d,*divmod(u,width)) if u<old else bonus[u-old]
            ns.update(extra.get(u,[]))
            for v in sorted(x for x in ns if x>u):out.write(f'{u} {v}\n')
if __name__=='__main__':main()
