"""Reconstruct the 42403-vertex (maximum degree12, diameter<=5) graph.

The bound source is the inherited accepted42402 graph. This script keeps every
old edge and adds vertex42402 adjacent to the twelve explicitly listed vertices.
No search program or cached distance table is required to reconstruct the graph.
"""
from pathlib import Path
import argparse

PINS=(979,4045,4563,5711,6513,7312,8156,15138,21547,29557,37599,41421)
SOURCE_REL=Path("research/ddp/more_graphs_20261027/h9_redei15/production/continuation/graphs/graph_d12_D5_n42402.edges")

def generate(source: Path, output: Path):
    with source.open() as f:
        n,m=map(int,f.readline().split())
        edges=[tuple(map(int,line.split())) for line in f if line.strip()]
    assert (n,m)==(42402,245937) and len(edges)==m
    normalized={tuple(sorted(edge)) for edge in edges}
    assert len(normalized)==m and all(0<=u<v<n for u,v in normalized)
    degrees=[0]*n
    for u,v in normalized:
        degrees[u]+=1;degrees[v]+=1
    assert max(degrees)<=12 and len(PINS)==len(set(PINS))==12
    assert all(degrees[v]<12 for v in PINS)
    result=sorted(normalized|{(v,n) for v in PINS})
    assert len(result)==m+12
    with output.open("w") as f:
        f.write(f"{n+1} {len(result)}\n")
        for u,v in result:f.write(f"{u} {v}\n")
    print(f"{output}: n={n+1}, m={len(result)}, old_edges_retained={m}")

def main():
    root=next(p for p in Path(__file__).resolve().parents if p.name=="ar4math")
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source",type=Path,default=root/SOURCE_REL)
    ap.add_argument("--output",type=Path,default=Path(__file__).resolve().parent/"graph_d12_D5_n42403.edges")
    args=ap.parse_args();generate(args.source,args.output)

if __name__=="__main__":main()

