"""Literal reconstruction from one certified affine relation table.

Import load()/neighbors(), or invoke: python generator.py TABLE.json OUTPUT.edges
This utility is saved without running a graph export or any distance check.
"""
from pathlib import Path
import json
import sys

def load(path):
    table=json.loads(Path(path).read_text())
    assert table['complete']
    bycontroller=[[] for _ in range(table['controller_count'])]
    for arc in table['arcs']:
        bycontroller[arc['from']].append(arc)
    return table,bycontroller

def neighbors(vertex,table,bycontroller):
    k,q=table['dimension'],table['bin_size']
    a,x=divmod(vertex,q)
    digits=[(x//(3**i))%3 for i in range(k)]
    for arc in bycontroller[a]:
        z=[(arc['c'][j]+sum(arc['B'][j][i]*digits[i] for i in range(k)))%3 for j in range(k)]
        for t in range(3):
            y=sum(((z[j]+t*arc['v'][j])%3)*(3**j) for j in range(k))
            other=arc['to']*q+y
            if other!=vertex:
                yield other

if __name__=='__main__':
    assert len(sys.argv)==3
    table,bycontroller=load(sys.argv[1])
    with Path(sys.argv[2]).open('w') as f:
        f.write(f"{table['n']} {table['m']}\n")
        count=0
        for vertex in range(table['n']):
            for other in sorted(neighbors(vertex,table,bycontroller)):
                if vertex<other:
                    f.write(f'{vertex} {other}\n')
                    count+=1
        assert count==table['m']
