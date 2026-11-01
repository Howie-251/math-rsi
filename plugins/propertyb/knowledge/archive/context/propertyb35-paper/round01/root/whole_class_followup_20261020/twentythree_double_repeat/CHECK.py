#!/usr/bin/env python3
import json,sys
from pathlib import Path
from itertools import product
from math import comb
from time import process_time
P=Path(__file__).resolve().parent

def choose(n,k):return comb(n,k) if 0<=k<=n else 0

def matrices():
    # Four independent entries; all five others forced by margins.
    for a,b,c,d in product(range(5),repeat=4):
        z=[[a,b,4-a-b],[c,d,4-c-d],[4-a-c,4-b-d,a+b+c+d-4]]
        if min(sum(z,[]))>=0:
            assert all(sum(r)==4 for r in z)
            assert all(sum(z[i][j] for i in range(3))==4 for j in range(3))
            yield z

def component(M):
    row=[0]*3;col=[0]*3;idx=0
    for i in range(3):
        for j in range(3):
            for unused in range(M[i][j]):
                row[i]|=1<<idx;col[j]|=1<<idx;idx+=1
    assert idx==12
    dist=[[0]*13 for _ in range(3)]
    for blue in range(1<<12):
        j=blue.bit_count()
        ra=any(blue&t==0 for t in row);ba=any(blue&t==t for t in row)
        rb=any(blue&t==0 for t in col);bb=any(blue&t==t for t in col)
        if (ra and ba) or (rb and bb):dist[0][j]+=1
        elif ra and rb:dist[1][j]+=1 # forced blue
        elif ba and bb:dist[2][j]+=1 # forced red
    out={}
    for q in (8,9):
        fail=core=fb=fr=0
        for j in range(13):
            k=q-j
            core+=dist[0][j]*choose(6,k)
            fb+=dist[1][j]*(2*choose(3,k-3)-int(k==6))
            fr+=dist[2][j]*(2*choose(3,k)-int(k==0))
        fail=core+fb+fr
        out[str(q)]={'failure':fail,'core':core,'forced_blue':fb,'forced_red':fr}
    return {'matrix':M,'quotas':out,'X_state_histograms':dist}

def main():
    started=process_time();ms=list(matrices());assert len(ms)==120
    if '--profile' in sys.argv:
        rows=[component(M) for M in ms[:3]]
        out={'status':'PROFILE_COMPLETE','matrices':len(ms),'profile_count':3,
             'cpu_seconds':process_time()-started,'estimated_complete_cpu_seconds':(process_time()-started)*len(ms)/3,
             'examples':rows}
        (P/'PROFILE.json').write_text(json.dumps(out,indent=2)+'\n')
        print(json.dumps({k:v for k,v in out.items() if k!='examples'}));return
    records=[]
    for M in ms:
        assert process_time()-started<30,'30 CPU budget'
        records.append(component(M))
    maxs={str(q):max(r['quotas'][str(q)]['failure'] for r in records) for q in (8,9)}
    assert maxs=={'8':5082,'9':6156}
    assert all(sum(r['quotas'][str(q)]['failure']==maxs[str(q)] for r in records)==6 for q in (8,9))
    degrees=[]
    for d in range(6,20):
        v8=40898-572*d+maxs['8'];v9=37180+572*d+maxs['9']
        degrees.append({'d':d,'quota8_total':v8,'quota8_margin':43758-v8,
                        'quota9_total':v9,'quota9_margin':48620-v9})
    assert all(r['quota8_margin']>=1210 for r in degrees)
    out={'status':'PASS','matrix_count':len(ms),'X_assignments_per_matrix':4096,
         'quota8_sample_space':43758,'quota9_sample_space':48620,
         'max_component_failure':maxs,
         'maximizers':{str(q):[r['matrix'] for r in records if r['quotas'][str(q)]['failure']==maxs[str(q)]] for q in (8,9)},
         'fixed_single_edge_union_bounds':degrees,'cpu_seconds':process_time()-started,'records':records}
    (P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='records'}))
if __name__=='__main__':main()
