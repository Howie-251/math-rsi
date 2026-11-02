"""Complete 90 assignments of the six external ports of triangle 7,17,28."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import numpy as np
import json,time

HERE=Path(__file__).resolve().parent


def main():
    start=time.process_time();source=HERE.parent/'second_mechanism/control_unrestricted_n31.edges'
    rows=[tuple(map(int,l.split())) for l in source.read_text().splitlines()];n,m=rows[0]
    A=np.zeros((n,n),dtype=np.int64)
    for u,v in rows[1:]:A[u,v]=A[v,u]=1
    T=[7,17,28];ports=[2,8,21,23,26,29];fixed=A.copy()
    for u in T:
        for v in ports:fixed[u,v]=fixed[v,u]=0
    results=[]
    for a in combinations(ports,2):
        remaining=set(ports)-set(a)
        for b in combinations(sorted(remaining),2):
            c=sorted(remaining-set(b));assignment=[list(a),list(b),c];B=fixed.copy()
            for u,neighbors in zip(T,assignment):
                for v in neighbors:B[u,v]=B[v,u]=1
            assert np.all(B.sum(axis=1)==4)
            B3=(B@B)@B;z=np.argwhere(B3==0).tolist()
            results.append(dict(assignment=dict(zip(T,assignment)),zero_count=len(z),zero_pairs=z,
                                paired_2_26=any(2 in p and 26 in p for p in assignment),
                                paired_23_29=any(23 in p and 29 in p for p in assignment)))
    best=min(x['zero_count'] for x in results);best_cases=[x for x in results if x['zero_count']==best]
    assert len(results)==90 and best==4 and len(best_cases)==6
    assert all(x['paired_2_26'] and x['paired_23_29'] for x in best_cases)
    out=dict(scope='only six outside attachments of the fixed triangle 7,17,28 may change',
             assignments=90,best_zero_count=best,best_assignments=len(best_cases),
             zero_count_hist=dict(Counter(x['zero_count'] for x in results)),
             cpu_seconds=time.process_time()-start,results=results)
    (HERE/'triangle_port_assignments.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='results'},indent=2))


if __name__=='__main__':main()
