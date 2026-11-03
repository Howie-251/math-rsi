#!/usr/bin/env python3
"""Portable optional replay entrypoint; no work occurs until a subcommand runs.

Inputs are the packaged original repo-relative files. Outputs go to a new
directory. This adapter does not edit the validated producers or Lean sources,
install dependencies, fetch packages, or compute artifact hashes.
"""
import argparse
import os
from pathlib import Path
import shutil
import subprocess

STAGE=Path('research/ddp/two_successful_methods_20261101')
SOURCE=STAGE/'retained_edge_transfer/opposite_gq77_spread64'
P33=SOURCE/'published_partial_ovoid33'
PREFIX='GQ77Published33CloneFamily'

def repository(value):
    root=Path(value or os.environ.get('AR4MATH_ROOT')or Path(__file__).resolve().parent.parent).resolve()
    if not(root/SOURCE/'graph_d64_D3_n160050.edges').is_file():
        raise FileNotFoundError('Set --root or AR4MATH_ROOT to the extracted repo root containing research/ and formal/.')
    return root

def graphs(args,root):
    output=Path(args.output).resolve();output.mkdir(parents=True,exist_ok=False)
    names=['multiplicity65_72_family','multiplicity73_79_family']if args.batch=='all'else[
        'multiplicity65_72_family'if args.batch=='lower'else'multiplicity73_79_family']
    for name in names:
        inputs=root/P33/name;work=output/name;work.mkdir();(work/'graphs').mkdir()
        shutil.copy2(inputs/'CENTERS_INPUT.txt',work/'CENTERS_INPUT.txt')
        subprocess.run([args.cxx,'-O3','-std=c++17',str(inputs/'produce.cpp'),'-o',str(work/'produce')],check=True)
        with(work/'PRODUCER_REPLAY.json').open('w')as out:
            subprocess.run([str(work/'produce'),str(root/SOURCE/'graph_d64_D3_n160050.edges'),str(args.cpu_per_batch)],
                           cwd=work,stdout=out,check=True)
        print(work/'graphs')

def lean(args,root):
    version=subprocess.run([args.lean_bin,'--version'],check=True,capture_output=True,text=True).stdout
    if '4.24.0'not in version:raise ValueError('This source package is pinned to Lean4.24.0.')
    output=Path(args.output).resolve();output.mkdir(parents=True,exist_ok=False)
    library=output/'lib';library.mkdir()
    formal=root/'formal';seen=set();order=[]
    def visit(mod):
        if mod in seen:return
        source=formal/(mod.replace('.','/')+'.lean')
        if not source.is_file():return  # Lean/Mathlib come from the supplied existing dependency path.
        seen.add(mod)
        for line in source.read_text().splitlines():
            if not line.startswith('import '):continue
            for imported in line[7:].split():
                if imported.startswith('--'):break
                visit(imported)
        order.append((mod,source))
    for mod in [PREFIX+'Audit',PREFIX+'UpperAudit']:visit(mod)
    env=dict(os.environ);env['LEAN_PATH']=str(library)+os.pathsep+args.dependency_lean_path
    env['LEAN_NUM_THREADS']='1'
    with(output/'COMPILE_COMMANDS.txt').open('w')as record:
        for mod,source in order:
            target=library/(mod.replace('.','/')+'.olean');target.parent.mkdir(parents=True,exist_ok=True)
            command=[args.lean_bin,'-j1','-o',str(target),str(source.relative_to(formal))]
            record.write(repr(command)+'\n');record.flush()
            with(output/(mod.replace('.','_')+'.log')).open('w')as log:
                subprocess.run(command,cwd=formal,env=env,stdout=log,stderr=log,check=True)
    print('Compiled local import closure into',library)

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',help='Extracted repo root; defaults to AR4MATH_ROOT or this script parent repo.')
    commands=parser.add_subparsers(dest='mode',required=True)
    graph=commands.add_parser('graphs',help='Reproduce the15 complete graph files from included source160050.')
    graph.add_argument('--batch',choices=['lower','upper','all'],default='all')
    graph.add_argument('--output',required=True,help='New output directory,not an existing artifact directory.')
    graph.add_argument('--cxx',default='g++');graph.add_argument('--cpu-per-batch',type=float,default=25)
    compiler=commands.add_parser('lean',help='Optional expert rebuild using an already installed matching Lean/Mathlib.')
    compiler.add_argument('--output',required=True,help='New output directory for local oleans/logs.')
    compiler.add_argument('--lean-bin',required=True,help='Existing Lean4.24.0 executable; no install or fetch.')
    compiler.add_argument('--dependency-lean-path',required=True,help='Existing pinned Mathlib/dependency .olean paths,OS-path-separated.')
    args=parser.parse_args();root=repository(args.root)
    if args.mode=='graphs':graphs(args,root)
    else:lean(args,root)

if __name__=='__main__':main()
