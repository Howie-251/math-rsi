"""Exact necessary degree/coverage screen for four cyclic orbits of length15."""
from itertools import combinations_with_replacement,permutations
from pathlib import Path
import json,time

def screen():
    start=time.process_time();examined=0;kept=[];orbits={}
    for a in combinations_with_replacement(range(0,9,2),4):
        d=[8-v for v in a]
        for x in range(9):
            for y in range(9):
                z=(d[0]+d[1]+d[2]-d[3])//2-x-y
                c=[[0,x,y,d[0]-x-y],[x,0,z,d[1]-x-z],
                   [y,z,0,d[2]-y-z],[d[0]-x-y,d[1]-x-z,d[2]-y-z,0]]
                if any(v<0 for row in c for v in row):continue
                assert all(a[i]+sum(c[i])==8 for i in range(4))
                examined+=1
                if any(min(15,1+a[i]+a[i]*a[i]//2)+sum(min(14,c[i][j]*(c[i][j]-1)) for j in range(4) if i!=j)<15 for i in range(4)):continue
                if any(c[i][j]*(1+a[i]+a[j])+sum(c[i][k]*c[k][j] for k in range(4) if k!=i and k!=j)<15 for i in range(4) for j in range(i+1,4)):continue
                item=dict(internal_degrees=a,cross_sizes=c);kept.append(item)
                key=min(tuple(a[p[i]] for i in range(4))+tuple(c[p[i]][p[j]] for i in range(4) for j in range(i+1,4)) for p in permutations(range(4)))
                orbits.setdefault(key,item)
    result=dict(modulus=15,orbit_count=4,integer_quotients_examined=examined,labelled_survivors=kept,
                orbit_representatives=list(orbits.values()),cpu_seconds=time.process_time()-start,
                scope='Necessary capacities only. Surviving parameters are not realizable graph claims.')
    assert len(kept)==7 and len(orbits)==3
    return result

if __name__=='__main__':
    result=screen();out=Path(__file__).with_suffix('.json')
    assert not out.exists(),'No unchanged rerun'
    out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['labelled_survivors','orbit_representatives']}))
