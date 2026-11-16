#!/usr/bin/env python3
"""Reconstruct, bind exact edges, and recheck all uncovered distance pairs.

No network, original-machine paths or solver are used. Requires Python3 and a
C++17 compiler (g++ by default). Existing original independent receipts are also
included; this packaging rerun does not replace their provenance or prove Lean.
"""
from pathlib import Path
import argparse,json,subprocess,tempfile,time
import reproduce as r
HERE=Path(__file__).resolve().parent

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output-dir',type=Path);p.add_argument('--all-roots',action='store_true',help='Optional costly full BFS; not required for the stated source/core theorem cover.');a=p.parse_args()
    with tempfile.TemporaryDirectory(prefix='dd-check-') as td:
        out=a.output_dir or Path(td);out.mkdir(parents=True,exist_ok=True);binary=Path(td)/'check_roots';start=time.monotonic()
        subprocess.run(['g++','-O3','-std=c++17',str(HERE/'check_roots.cpp'),'-o',str(binary)],check=True)
        rows=[]
        for family,name,fn,cap,lo in [('11,5','graph_d11_D5_n37632.edges',r.construct_h9,11,37471),('12,5','graph_d12_D5_n42433.edges',r.construct_d12,12,42402)]:
            graph=out/name;generated=fn(graph);n,e=r.read_edges(graph);refn,ref=r.read_edges(HERE/'graphs'/name);assert n==refn and e==ref
            if family=='12,5':
                sn,se=r.read_edges(HERE/'inputs/d12_source42402.edges');assert sn==42402 and se<=e
                theorem='All old42402-old42402 pairs inherit D<=5 from the accepted source; all31 new vertices are full BFS roots in this final graph. Concrete source Lean remains open.'
            else:
                # Literal core construction was generated from actual tau/pi/incidence/colors above.
                assert len([edge for edge in e if edge[1]<37471])==203747
                theorem='All core-core pairs use the supplied true-H9 arbitrary-sigma partial-fold proof and literal input binding; full BFS for all160 old exterior vertices and new z covers every remaining pair. Concrete Lean remains open.'
            raw=subprocess.run([str(binary),str(graph),str(cap),'5',str(0 if a.all_roots else lo),str(n)],check=True,text=True,capture_output=True)
            check=json.loads(raw.stdout);rows.append(dict(family=family,generation=generated,exact_reference_edge_set_match=True,raw_BFS=check,all_pairs_argument=theorem))
        receipt=dict(status='PASS_PORTABLE_REPRODUCTION_AND_SPECIFIED_COMPLETE_PAIR_COVER',checks=rows,all_roots_requested=a.all_roots,wall_seconds=time.monotonic()-start,new_research_results=0,concrete_Lean_complete=False)
        if a.output_dir:(out/'CHECK_RESULT.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n')
        print(json.dumps(receipt,ensure_ascii=False,indent=2))
if __name__=='__main__':main()
