"""Finish the same finite r=2 divisor scope; do not replay the closed m75."""
from pathlib import Path
import itertools
import json
import math
import time

OUT = Path(__file__).resolve().parent
prediction = dict(scope_moduli=[93,123,155], prior_modulus75_replayed=False,
    reason='These are the remaining divisors of2^20-1 with55<m<=160, selected before the original canonical CRT tests.',
    prediction='At leastone remaining connected translation class will cover the thinnest phase; complete20phase coverage remains a separate requirement.',
    budget_CPU_seconds=5, stop='Finish only this fixed divisor/phase scope, no othermodulus or localrepair.',
    reuse='One previously failed canonical B1023,C1,D19 unitorbit per modulus is inherited without reevaluation.')
(OUT/'OTHER_DIVISORS_PREDICTION.json').write_text(json.dumps(prediction,indent=2)+'\n')
start=time.process_time()
results=[]
for modulus,p,q,pbase,qbase in [(93,3,31,3,31),(123,3,41,3,41),(155,5,31,5,31)]:
    begin=time.process_time()
    powers=[pow(2,i,modulus) for i in range(20)]
    gens=[]
    for i,phase in enumerate([1,12,11,16]):
        vector=[0,0,0]
        if i:vector[i-1]=1
        reverse=(-phase)%20
        gens.extend([(phase,tuple(vector)),(reverse,tuple(-powers[reverse]*x%modulus for x in vector))])
    forms=[set() for _ in range(20)]
    def visit(phase,vector,last,depth):
        forms[phase].add(vector)
        if depth==4:return
        for j,(increment,shift) in enumerate(gens):
            if last>=0 and j==(last^1):continue
            visit((phase+increment)%20,tuple((vector[k]+powers[phase]*shift[k])%modulus for k in range(3)),j,depth+1)
    visit(0,(0,0,0),-1,0)
    counts=[len(f) for f in forms]
    ordered=sorted(range(20),key=lambda i:(counts[i],i));thin=ordered[0]
    def local(mod,prime):
        return ([(1,b,c) for b in range(mod) for c in range(mod)]
                +[(a,1,c) for a in range(0,mod,prime) for c in range(mod)]
                +[(a,b,1) for a in range(0,mod,prime) for b in range(0,mod,prime)])
    left,right=local(p,pbase),local(q,qbase)
    scope=len(left)*len(right)
    row=dict(modulus=modulus,target_order=20*modulus,normalized_scope=scope,
        phase_capacities=counts,thinnest_phase=thin,
        new_cases_evaluated=0,cached_canonical_rejections=0,
        thin_survivors=0,full_cover_hits=[],all_source_BFS=0,new_graphs_generated=0)
    if min(counts)<modulus:
        row.update(status='STRICT_FORM_CAPACITY_BELOW_MODULUS',scope_closed=True)
    else:
        units=[u for u in range(modulus) if math.gcd(u,modulus)==1]
        known_orbit={tuple(u*x%modulus for x in (1023%modulus,1,19%modulus)) for u in units}
        inverse=pow(q,-1,p);ordered_forms=[sorted(f) for f in forms]
        completed=0
        for a,b in itertools.product(left,right):
            if time.process_time()-start>5:break
            B,C,D=tuple(b[k]+q*((a[k]-b[k])*inverse%p) for k in range(3))
            completed+=1
            if (B,C,D) in known_orbit:
                row['cached_canonical_rejections']+=1
                continue
            row['new_cases_evaluated']+=1
            for phase in ordered:
                covered={(v[0]*B+v[1]*C+v[2]*D)%modulus for v in ordered_forms[phase]}
                if phase==thin and len(covered)==modulus:row['thin_survivors']+=1
                if len(covered)<modulus:break
            else:
                row['full_cover_hits'].append(dict(B=B,C=C,D=D))
        row.update(status='COMPLETE_PROJECTIVE_SCOPE' if completed==scope else 'CPU_LIMIT_UNATTEMPTED_REMAINDER',
                   scope_closed=completed==scope,scope_cases_processed=completed)
    row['CPU_seconds']=time.process_time()-begin
    results.append(row)
result=dict(status='FINITE_DIVISOR_SCOPE_FINISHED' if all(r['scope_closed'] for r in results) else 'CPU_LIMIT',
    rows=results,old_modulus75_replayed=False,prediction_supported=any(r['thin_survivors'] for r in results),
    CPU_seconds=time.process_time()-start,pending=[])
(OUT/'OTHER_DIVISORS_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result),flush=True)
