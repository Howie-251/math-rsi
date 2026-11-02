"""Check one explicitly supplied candidate. Not run during symbolic preparation."""
import csv
import json
from pathlib import Path
import sys

def check(values):
    if len(values)!=10:
        raise ValueError('Supply a0 a1 a2 a3 sigma01 sigma23 tau02 tau13 rho03 rho12.')
    a0,a1,a2,a3,s01,s23,t02,t13,r03,r12=[v%33 for v in values]
    simple=(len({0,a0,s01})==3 and len({0,a1,r12})==3
            and t02!=0 and a2!=s23 and (a3+r03)%33!=0)
    root=Path(__file__).resolve().parent
    rows=list(csv.DictReader((root/'DISTINCT_FORMS.tsv').open(),delimiter='\t'))
    names=['a0','a1','a2','a3','sigma01','sigma23','tau02','tau13','rho03','rho12','third']
    parameters=[a0,a1,a2,a3,s01,s23,t02,t13,r03,r12,11]
    supports=[[set() for _ in range(4)]for _ in range(4)]
    for row in rows:
        value=sum(int(row[name])*v for name,v in zip(names,parameters))%33
        supports[int(row['source'])][int(row['target'])].add(value)
    missing=[{'source':s,'target':t,'missing':sorted(set(range(33))-supports[s][t])}
             for s in range(4)for t in range(4)if len(supports[s][t])<33]
    return {'modulus':33,'simple':simple,
            'all_exact_three_supports_complete':not missing,
            'candidate_passes_controller_gate':simple and not missing,
            'support_sizes':[[len(c)for c in row]for row in supports],
            'missing_supports':missing,
            'quotient3_cover':all(len({x%3 for x in c})==3 for row in supports for c in row),
            'quotient11_cover':all(len({x%11 for x in c})==11 for row in supports for c in row),
            'graph_generated':False,'BFS_run':False}

if __name__=='__main__':
    print(json.dumps(check([int(x)for x in sys.argv[1:]]),indent=2))
