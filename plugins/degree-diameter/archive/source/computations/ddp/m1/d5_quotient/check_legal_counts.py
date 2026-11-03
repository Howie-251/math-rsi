"""Independent legal-count check via hyperplane inclusion-exclusion in P2(F13).
This does not generate the searcher's projective representatives or run its BFS.
"""
from pathlib import Path
from itertools import combinations
import json

def rank(rows,p):
    a=[list(x) for x in rows];r=0
    for c in range(4):
        t=next((i for i in range(r,len(a)) if a[i][c]%p),None)
        if t is None:continue
        a[r],a[t]=a[t],a[r];iv=pow(a[r][c]%p,-1,p)
        a[r]=[x*iv%p for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                k=a[i][c];a[i]=[(x-k*y)%p for x,y in zip(a[i],a[r])]
        r+=1
    return r

def expected(s,p):
    forms=[]
    for i in range(4):
        if s[i]==0:forms.append(tuple(int(j==i) for j in range(4)))
    if s[2]==s[3]:forms.append((0,0,1,-1))
    out=0
    for k in range(len(forms)+1):
        for subset in combinations(forms,k):
            d=3-rank(subset,p)
            assert d>=0
            projective=(p**d-1)//(p-1)
            out+=(-1)**k*projective
    return out

def main():
    h=Path(__file__).resolve().parent
    rows=[json.loads(x) for x in (h/'complete.skeleton_results.jsonl').read_text().splitlines()]
    skeletons=[list(map(int,x.split())) for x in (h/'skeletons.txt').read_text().splitlines()]
    assert len(rows)==len(skeletons)==1464
    for i,row in enumerate(rows):
        assert row['skeleton_id']==i and row['residues']==skeletons[i]
        assert row['status']=='COMPLETE' and row['projective_visited']==183
        assert expected(row['residues'],13)==row['legal_fully_scored']
    result=dict(method='inclusion-exclusion of forbidden projective hyperplanes using modular ranks',
                skeletons_checked=len(rows),every_row_count_matches=True,
                legal_total=sum(expected(s,13) for s in skeletons),
                minimum_from_rows=min(x['minimum_missing'] for x in rows if x['minimum_missing'] is not None))
    (h/'independent_legal_counts.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
