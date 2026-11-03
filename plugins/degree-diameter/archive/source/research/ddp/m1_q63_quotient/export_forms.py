#!/usr/bin/env python3
"""Export all surviving skeletons and weakest-first exact symbolic fibers."""
from pathlib import Path
import importlib.util
import json

P = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('q63_symbolic', P/'enumerate.py')
symbolic = importlib.util.module_from_spec(spec)
spec.loader.exec_module(symbolic)
rows = json.loads((P/'surviving_skeletons.json').read_text())
with (P/'all_survivor_forms.txt').open('w') as out:
    print(len(rows), file=out)
    for index, row in enumerate(rows):
        a,b = row['alpha'], row['beta']
        sigmas = row['sigmas']
        balls = symbolic.symbolic_balls(a,b,sigmas)
        buckets = [(len(bucket),root,side,residue,sorted(bucket))
                   for root, sides in enumerate(balls)
                   for side, residues in enumerate(sides)
                   for residue,bucket in enumerate(residues)]
        buckets.sort()
        print(index,a,b,*sigmas,len(buckets),file=out)
        for length,root,side,residue,forms in buckets:
            assert length >= 7
            print(root,side,residue,length,*forms,file=out)
print('Exported',len(rows),'surviving skeletons.')
