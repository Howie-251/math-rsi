"""Replay the explicit affine counterexample; no search is required."""
from pathlib import Path
from fractions import Fraction as Q
import json
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
sys.dont_write_bytecode=True
sys.path.insert(0,str(ROOT/'context/propertyb34/round01/high-math'))
from bare_layout import BareLayout

d=json.loads((HERE/'NONCONTIGUOUS_AFFINE_COUNTEREXAMPLE.json').read_text())
eng=BareLayout(25,d['positions'])
for name,witness in d['counterexamples'].items():
    sets=witness['low_sets']
    for i in range(9):
        assert int(i in sets[0])+int(i in sets[1])==int(i in sets[2])+int(i in sets[3])
    values=[]
    for low in sets:
        assert len(low)==5
        counts={0:d['empty'],**{1<<i:7-d['incidences'][i]-int(i in low) for i in range(9)},
                **{t:1 for t in d['full']}}
        assert sum(counts.values())==34 and min(counts.values())>=0
        true,rows=eng.bound(counts,True)
        value=true if name=='true_min' else sum((r[c] for r,c in zip(rows,d['choices'])),Q())
        values.append(value)
    assert list(map(str,values))==witness['values']
    difference=values[0]+values[1]-values[2]-values[3]
    assert difference==Q(witness['parallelogram_difference']) and difference!=0
    print(name,str(difference),'PASS')
