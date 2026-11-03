"""Complete quotient and formal-word capacity check; no translation assignments searched."""
from pathlib import Path
from math import gcd
from collections import Counter
import json,time

HERE=Path(__file__).resolve().parent
P=41;M=8;R=3
power=[pow(R,k,P) for k in range(M)]

def canonical(s,t,negate=False):
    triple=(0,s,t);images=[]
    for sign in ([1,-1] if negate else [1]):
        for anchor in triple:
            shifted=sorted((sign*(q-anchor))%M for q in triple)
            shifted.remove(0)
            images.append(tuple(shifted))
    return min(images)

def capacities(kind,beta,sigma,tau):
    variables=3 if kind=='mixed' else 4
    def zero():return (0,)*(variables+1)
    def basis(i):return tuple(int(k==i) for k in range(variables+1))
    def inverse(form,q):return tuple((-power[-q%M]*z)%P for z in form),(-q)%M
    # tuple: named dart, inverse named dart, target layer, quotient voltage, affine voltage.
    steps=[[],[]]
    steps[0]=[('a0','a0',0,4,zero()),('a1','a1',0,4,basis(0))]
    if kind=='mixed':
        b=basis(1);bi,qi=inverse(b,beta)
        steps[1]=[('bp','bm',1,beta,b),('bm','bp',1,qi,bi)]
        cross=[(zero(),0),(basis(2),sigma),(basis(3),tau)]
    else:
        steps[1]=[('b0','b0',1,4,basis(1)),('b1','b1',1,4,basis(2))]
        cross=[(zero(),0),(basis(3),sigma),(basis(4),tau)]
    for i,(form,q) in enumerate(cross):
        inv,qi=inverse(form,q);name=f'c{i}'
        steps[0].append((name,name,1,q,form));steps[1].append((name,name,0,qi,inv))
    results=[]
    for root in [0,1]:
        forms=[[set() for _ in range(M)] for _ in range(2)]
        walks=[[0]*M for _ in range(2)]
        def visit(layer,q,form,forbidden,depth):
            forms[layer][q].add(form);walks[layer][q]+=1
            if depth==5:return
            for name,reverse,newlayer,voltage,linear in steps[layer]:
                if name==forbidden:continue
                newform=tuple((a+power[q]*b)%P for a,b in zip(form,linear))
                visit(newlayer,(q+voltage)%M,newform,reverse,depth+1)
        visit(root,0,zero(),None,0)
        assert sum(map(sum,walks))==1706
        distinct=[[len(cell) for cell in row] for row in forms]
        results.append(dict(root=root,nonbacktracking_walk_counts=walks,distinct_affine_forms=distinct,
                            minimum_distinct=min(map(min,distinct)),minimum_walks=min(map(min,walks)),
                            deficient_cells=[[side,k,distinct[side][k]] for side in range(2) for k in range(M)
                                             if distinct[side][k]<P]))
    return dict(kind=kind,beta=beta,sigma=sigma,tau=tau,roots=results,
                passes_walk_capacity=all(row['minimum_walks']>=P for row in results),
                passes_form_capacity=all(row['minimum_distinct']>=P for row in results),
                minimum_distinct=min(row['minimum_distinct'] for row in results))

def main():
    started=time.process_time();records=[];summary={}
    for kind in ['mixed','both']:
        raw=[]
        for beta in ([0,1,2,3] if kind=='mixed' else [4]):
            for s in range(M):
                for t in range(s,M):
                    if gcd(gcd(gcd(M,4),beta),gcd(s,t))!=1:continue
                    raw.append((beta,s,t))
        anchored=sorted({(b,*canonical(s,t,False)) for b,s,t in raw})
        canonical_rows=sorted({(b,*canonical(s,t,kind=='both')) for b,s,t in raw})
        rows=[capacities(kind,*q) for q in canonical_rows]
        totals=dict(all_quotients_legal=0,capacity_survivors_legal=0,
                    capacity_survivors_after_simple_internal_ordering=0)
        for row in rows:
            beta,s,t=row['beta'],row['sigma'],row['tau']
            cross=40*39 if s==t==0 else 41*40 if s==0 or s==t else 41*41
            internal=(40 if beta==0 else 41) if kind=='mixed' else 41*40
            reduced_internal=(20 if beta==0 else 41) if kind=='mixed' else 41*40//2
            row['legal_translation_assignments']=cross*internal
            row['legal_assignments_simple_internal_ordering']=cross*reduced_internal
            totals['all_quotients_legal']+=cross*internal
            if row['passes_form_capacity']:
                totals['capacity_survivors_legal']+=cross*internal
                totals['capacity_survivors_after_simple_internal_ordering']+=cross*reduced_internal
        records.extend(rows)
        summary[kind]=dict(raw_connected_quotients=len(raw),after_cross_anchoring=len(anchored),
            canonical_quotients=len(canonical_rows),quotients=[list(q) for q in canonical_rows],
            walk_capacity_survivors=sum(r['passes_walk_capacity'] for r in rows),
            affine_form_capacity_survivors=sum(r['passes_form_capacity'] for r in rows),
            survivor_quotients=[[r['beta'],r['sigma'],r['tau']] for r in rows if r['passes_form_capacity']],
            minimum_distinct_histogram=dict(sorted(Counter(r['minimum_distinct'] for r in rows).items())),
            translation_variables=3 if kind=='mixed' else 4,
            assignments_per_quotient_before_legality=P**(3 if kind=='mixed' else 4),**totals)
    result=dict(scope='Only F41 semidirect C8 with r=3; A={(0,4),(1,4)}; degree5 diameter5; no lift assignment search',
                summary=summary,records=records,cpu_seconds=time.process_time()-started)
    (HERE/'capacity_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(summary=summary,cpu_seconds=result['cpu_seconds']),indent=2))

if __name__=='__main__':main()
