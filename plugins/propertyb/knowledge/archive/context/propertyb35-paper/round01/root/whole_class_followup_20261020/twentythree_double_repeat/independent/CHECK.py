#!/usr/bin/env python3
"""Block-event inclusion-exclusion, no literal X color enumeration."""
from pathlib import Path
from itertools import combinations
from collections import Counter
from math import comb
from time import process_time
import json
P=Path(__file__).resolve().parent
ONE={(0,0):1}
def choose(n,k):return comb(n,k) if 0<=k<=n else 0

def plus(*terms):
    out=Counter()
    for factor,poly in terms:
        for key,value in poly.items():out[key]+=factor*value
    return {key:v for key,v in out.items() if v}

def mult(a,b):
    out=Counter()
    for (r,s),n in a.items():
        for (t,u),m in b.items():
            red=r|t;blue=s|u
            if not red&blue:out[red,blue]+=n*m
    return {key:v for key,v in out.items() if v}

def any_mono(blocks,color):
    out=Counter()
    for size in (1,2,3):
        for selected in combinations(blocks,size):
            forced=0
            for mask in selected:forced|=mask
            out[(forced,0) if color=='red' else (0,forced)]+=(-1)**(size+1)
    return dict(out)

def histogram(poly):
    out=[0]*13
    for (red,blue),coefficient in poly.items():
        assert not red&blue
        free=12-red.bit_count()-blue.bit_count()
        for j in range(13):out[j]+=coefficient*choose(free,j-blue.bit_count())
    assert all(v>=0 for v in out)
    return out

def independent_matrices():
    # Enumerate ordered bounded row compositions, deriving the third row.
    rows=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
    for r1 in rows:
        for r2 in rows:
            r3=tuple(4-r1[j]-r2[j] for j in range(3))
            if min(r3)>=0 and sum(r3)==4:yield [list(r1),list(r2),list(r3)]

def evaluate(matrix):
    row=[0]*3;col=[0]*3;nextpoint=0
    for i,entries in enumerate(matrix):
        for j,n in enumerate(entries):
            bits=((1<<n)-1)<<nextpoint
            row[i]|=bits;col[j]|=bits;nextpoint+=n
    assert nextpoint==12
    RP=any_mono(row,'red');BP=any_mono(row,'blue')
    RQ=any_mono(col,'red');BQ=any_mono(col,'blue')
    CP=mult(RP,BP);CQ=mult(RQ,BQ)
    core=plus((1,CP),(1,CQ),(-1,mult(CP,CQ)))
    forcedblue=mult(mult(RP,RQ),mult(plus((1,ONE),(-1,BP)),plus((1,ONE),(-1,BQ))))
    forcedred=mult(mult(BP,BQ),mult(plus((1,ONE),(-1,RP)),plus((1,ONE),(-1,RQ))))
    hist=[histogram(p) for p in (core,forcedblue,forcedred)]
    answers={}
    for q in (8,9):
        pieces=[0,0,0]
        for j in range(13):
            k=q-j
            pieces[0]+=hist[0][j]*choose(6,k)
            pieces[1]+=hist[1][j]*(2*choose(3,k-3)-int(k==6))
            pieces[2]+=hist[2][j]*(2*choose(3,k)-int(k==0))
        answers[str(q)]={'failure':sum(pieces),'core':pieces[0],'forced_blue':pieces[1],'forced_red':pieces[2]}
    return {'matrix':matrix,'quotas':answers,'X_state_histograms':hist,
            'polynomial_sizes':[len(poly) for poly in (core,forcedblue,forcedred)]}

def main():
    started=process_time();matrices=list(independent_matrices());assert len(matrices)==120
    records=[evaluate(m) for m in matrices]
    original=json.loads((P.parent/'RESULT.json').read_text())
    index={tuple(sum(r['matrix'],[])):r for r in original['records']}
    assert len(index)==120
    for r in records:
        other=index[tuple(sum(r['matrix'],[]))]
        assert r['quotas']==other['quotas'] and r['X_state_histograms']==other['X_state_histograms']
    maxs={str(q):max(r['quotas'][str(q)]['failure'] for r in records) for q in (8,9)}
    assert maxs=={'8':5082,'9':6156}
    output={'status':'PASS','method':'independent ordered row compositions; Boolean block-event polynomial inclusion-exclusion; binomial completion',
            'matrices':120,'quota_results':maxs,'compared_matrix_quota_pairs':240,
            'compared_X_histogram_entries':120*3*13,'literal_colors_enumerated':0,
            'maximum_polynomial_terms':max(max(r['polynomial_sizes']) for r in records),
            'cpu_seconds':process_time()-started,'records':records}
    (P/'RESULT.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps({k:v for k,v in output.items() if k!='records'}))
if __name__=='__main__':main()
