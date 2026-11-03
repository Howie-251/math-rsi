#!/usr/bin/env python3
"""Portable standard-library replay for the single accepted (16,4)16416 graph.

No work runs on import.  Graph replay reads the bundled literal source and I32;
optional Lean replay requires already installed matching third-party libraries.
"""
import argparse,json,os,subprocess
from pathlib import Path

GATE=Path('research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate')
SOURCE=Path('research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt')
AUDIT='F3Graph15552Clone16416Audit'

def repository(value):
    return Path(value or os.environ.get('AR4MATH_ROOT') or Path(__file__).resolve().parents[2]).resolve()

def graph(root,args):
    selected=json.loads((root/GATE/'controller_pack32_gate/SELECTED_BLOCKS.json').read_text())['selected_controllers']
    assert len(selected)==32
    adj=[]
    with (root/SOURCE).open() as f:
        for line in f:
            row=list(map(int,line.split()))
            assert row[0]==len(adj)
            adj.append(row[1:])
    assert len(adj)==15552
    offsets=[a+9*b+27*c for c in range(3) for b in range(3) for a in range(3)]
    centers=[81*i+offset for i in selected for offset in offsets]
    new_by_old=[[] for _ in adj]
    for j,center in enumerate(centers):
        # Freeze the original simple N of the OLD center. Never filter against
        # the new clone label or reinsert the removed virtual self.
        assert center not in adj[center]
        for oldpin in adj[center]:new_by_old[oldpin].append(15552+j)
    n=15552+len(centers)
    old_m=sum(len(row) for row in adj)//2
    added=sum(len(adj[c]) for c in centers)
    output=Path(args.output).resolve()
    output.parent.mkdir(parents=True,exist_ok=True)
    with output.open('x') as f:
        f.write(f'{n} {old_m+added}\n')
        for u,row in enumerate(adj):
            for v in sorted(row):
                if u<v:f.write(f'{u} {v}\n')
            for v in new_by_old[u]:f.write(f'{u} {v}\n')
    print(json.dumps(dict(output=str(output),n=n,m=old_m+added,source_edges=old_m,
                          clones=len(centers),new_edges=added,BFS=0,Lean=0)))

def local_imports(formal):
    seen=set();ordered=[]
    def visit(mod):
        if mod in seen:return
        source=formal/(mod.replace('.','/')+'.lean')
        if not source.is_file():
            if mod.startswith('DegreeDiameter.'):raise FileNotFoundError(source)
            return  # Matching Mathlib/Lean libraries are supplied externally.
        seen.add(mod)
        for line in source.read_text().splitlines():
            if line.startswith('import '):
                for imported in line[7:].split():
                    if imported.startswith('--'):break
                    visit(imported)
        ordered.append((mod,source))
    visit(AUDIT)
    return ordered

def lean(root,args):
    version=subprocess.run([args.lean_bin,'--version'],check=True,text=True,capture_output=True).stdout
    if '4.24.0' not in version:raise ValueError('Use the existing Lean4.24.0 toolchain.')
    output=Path(args.output).resolve();output.mkdir(parents=True,exist_ok=False)
    library=output/'lib';library.mkdir()
    formal=root/'formal'
    env=dict(os.environ,LEAN_PATH=str(library)+os.pathsep+args.dependency_lean_path,LEAN_NUM_THREADS='1')
    ordered=local_imports(formal)
    for mod,source in ordered:
        target=library/(mod.replace('.','/')+'.olean');target.parent.mkdir(parents=True,exist_ok=True)
        with (output/(mod.replace('.','_')+'.log')).open('w') as log:
            subprocess.run([args.lean_bin,'-j1','-s65536','-o',str(target),str(source.relative_to(formal))],
                           cwd=formal,env=env,stdout=log,stderr=log,check=True)
    print('Rebuilt',len(ordered),'project-local modules into',library)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',help='Extracted repo root; defaults to AR4MATH_ROOT or the script-relative root.')
    sub=parser.add_subparsers(dest='mode',required=True)
    graph_args=sub.add_parser('graph',help='Generate the one complete graph to a new output file.')
    graph_args.add_argument('--output',required=True)
    lean_args=sub.add_parser('lean',help='Optional rebuild with already installed Lean/Mathlib; no install or fetch.')
    lean_args.add_argument('--output',required=True)
    lean_args.add_argument('--lean-bin',required=True)
    lean_args.add_argument('--dependency-lean-path',required=True)
    args=parser.parse_args();root=repository(args.root)
    if args.mode=='graph':graph(root,args)
    else:lean(root,args)

if __name__=='__main__':main()
