"""Compute exact common unresolved B inputs from candidate bridge lists."""
import itertools,json
from pathlib import Path
R=Path(__file__).resolve().parent
edge=lambda a,b:tuple(sorted((a,b)))

def nulls(s,t,y):
    for p in itertools.permutations(range(4)):
        def tr(v):return sum(((v>>i)&1)<<p[i] for i in range(4))
        a,b=sorted((tr(s),tr(t)));yy=tr(y)
        path=R/f'r4_boundary_blocking_{a}_{b}_{yy}.json'
        if not path.exists():continue
        data=json.loads(path.read_text());inv={tr(v):v for v in range(16)}
        ans={}
        for r in data['reports']:
            ans.setdefault(r['c'],set()).update(frozenset(edge(inv[u],inv[v]) for u,v in row['matching']) for row in r['items'] if row['blocking_pairing'] is None)
        return ans
    return None

def main():
    reports=[]
    for core,rs in ((1,(3,5,9)),(4,(3,5,15)),(24,(6,10,15))):
        tables=[nulls(s,t,1) for s,t in itertools.combinations(rs,2)]
        if any(t is None for t in tables):continue
        for c in sorted(set.intersection(*(set(t) for t in tables))):
            joint=set.intersection(*(t[c] for t in tables))
            reports.append(dict(core=core,c=c,bridges=rs,unresolved=len(joint),matchings=[sorted(F) for F in sorted(joint,key=lambda f:sorted(f))]))
            print(core,c,[len(t[c]) for t in tables],len(joint),flush=True)
    (R/'r4_joint_blocking_check.json').write_text(json.dumps(dict(scope='Candidate joint blocker residuals only',reports=reports),indent=2)+'\n')
if __name__=='__main__':main()
