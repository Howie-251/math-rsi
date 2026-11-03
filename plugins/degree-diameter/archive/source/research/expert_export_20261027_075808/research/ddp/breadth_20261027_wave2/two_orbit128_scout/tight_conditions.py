"""Necessary sum conditions for exactly-32-form target fibers, no graph search."""
from pathlib import Path
import json,time
P=Path(__file__).resolve().parent
t0=time.process_time()
screen=json.loads((P/'RESULT.json').read_text())
out=[[(0,0,0,False),(0,1,0,True)]+[(1,4+2*k,None if k==0 else k+1,False) for k in range(4)],
     [(1,2,1,False),(1,3,1,True)]+[(0,5+2*k,None if k==0 else k+1,True) for k in range(4)]]

def solve(A,b,m,n):
    A=[[x%m for x in row] for row in A]; b=[x%m for x in b]
    if not A or m==1:return [0]*n
    if not n:return [] if not any(b) else None
    pivot=next(((i,j) for i,row in enumerate(A) for j,x in enumerate(row) if x%2),None)
    if pivot is None:
        if any(x%2 for x in b):return None
        return solve([[x//2 for x in row] for row in A],[x//2 for x in b],m//2,n)
    i,j=pivot;row=A[i];rhs=b[i];iv=pow(row[j],-1,m)
    cols=[k for k in range(n) if k!=j]
    AA=[];bb=[]
    for k in range(len(A)):
        if k==i:continue
        c=A[k][j]*iv%m
        AA.append([(A[k][l]-c*row[l])%m for l in cols]);bb.append((b[k]-c*rhs)%m)
    xx=solve(AA,bb,m,n-1)
    if xx is None:return None
    x=[0]*n
    for k,v in zip(cols,xx):x[k]=v
    x[j]=(iv*(rhs-sum(row[k]*x[k] for k in cols)))%m
    assert all(sum(a*y for a,y in zip(r,x))%m==v for r,v in zip(A,b))
    return x

records=[]
for survivor in screen['survivors']:
    bits=survivor['phases_a_b_h1_h2_h3'];equations=[]
    for root in range(2):
        slots={(side,p):set() for side in range(2) for p in range(2)}
        def walk(side,last,phase,coeff,const,length):
            slots[side,phase].add((tuple(coeff),const))
            if length==3:return
            for dst,dart,var,rev in out[side]:
                if last is not None and dart==(last^1):continue
                cc=coeff.copy();c=const;p=0 if var is None else bits[var]
                if var is not None:
                    cc[var]=(cc[var]+((-1)**(phase+(p+1 if rev else 0))))%32
                    c=(c+16*p*(int(rev)+phase))%32
                walk(dst,dart,phase^p,cc,c,length+1)
        walk(root,None,0,[0]*5,0,0)
        for (side,p),forms in slots.items():
            if len(forms)!=32:continue
            coefficients=[sum(c[k] for c,b in forms)%32 for k in range(5)]
            constant=sum(b for c,b in forms)%32
            equations.append(dict(root=root,target_orbit=side,phase=p,coefficient_sum=coefficients,constant_sum=constant,rhs=(16-constant)%32))
    A=[e['coefficient_sum'] for e in equations];b=[e['rhs'] for e in equations]
    x=solve(A,b,32,5)
    if x is not None:assert all(sum(a*y for a,y in zip(r,x))%32==z for r,z in zip(A,b))
    records.append(dict(phase_mask=survivor['phase_mask'],equations=equations,consistent=x is not None,one_linear_solution=x))
result=dict(status='COMPLETE_TIGHT_FIBER_SUM_NECESSARY_CONDITIONS',scope='Exactly32 distinct affine forms must evaluate to all residues mod32; their sum must equal16. This does not assert those residues are distinct.',phase_patterns_checked=len(records),inconsistent_patterns=[r['phase_mask'] for r in records if not r['consistent']],records=records,CPU_seconds=time.process_time()-t0,actual_parameter_searches=0,graphs_expanded=0,BFS_roots=0)
(P/'TIGHT_SUM.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','phase_patterns_checked','inconsistent_patterns','CPU_seconds']}))
for r in records: print(r['phase_mask'],[(e['coefficient_sum'],e['rhs']) for e in r['equations']],r['one_linear_solution'])
