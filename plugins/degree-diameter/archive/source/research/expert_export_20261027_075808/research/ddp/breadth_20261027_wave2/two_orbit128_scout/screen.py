from pathlib import Path
from collections import Counter
import json, time, sys

P=Path(__file__).resolve().parent
started=time.process_time()
# Variables a,b,h1,h2,h3. h0=e is still a named cross edge.
out=[[],[]]
out[0]=[(0,0,0,False),(0,1,0,True)]+[(1,4+2*k,None if k==0 else k+1,False) for k in range(4)]
out[1]=[(1,2,1,False),(1,3,1,True)]+[(0,5+2*k,None if k==0 else k+1,True) for k in range(4)]

def mul(a,b):
    x,s=a; y,t=b
    return ((x+(-1 if s else 1)*y+16*s*t)%32,s^t)

def inv(a):
    x,s=a
    return ((x+16)%32,1) if s else ((-x)%32,0)

def words(root):
    res=[]
    def walk(side,previous,word):
        res.append((side,tuple(word)))
        if len(word)==3:return
        for dst,dart,var,rev in out[side]:
            if previous is not None and dart==(previous^1):continue
            walk(dst,dart,word+[(var,rev)])
    walk(root,None,[])
    return res

paths=[words(0),words(1)]
assert [len(x) for x in paths]==[187,187]
assert [Counter(side for side,w in x) for x in paths]==[Counter({0:99,1:88}),Counter({1:99,0:88})]
records=[];calibration=0
for phase in range(32):
    bits=[(phase>>i)&1 for i in range(5)]
    counts=[]
    for root in range(2):
        slots={(side,p):set() for side in range(2) for p in range(2)}
        for side,word in paths[root]:
            coeff=[0]*5;const=0;oldphase=0
            for var,reverse in word:
                if var is None:continue
                p=bits[var]
                sign=(-1 if oldphase else 1)*((-1 if p==0 else 1) if reverse else 1)
                coeff[var]=(coeff[var]+sign)%32
                const ^= p & (oldphase ^ reverse)
                oldphase ^= p
            slots[side,oldphase].add((tuple(coeff),16*const))
            # Algebraic calibration only: zero plus five unit assignments.
            # These may be graph-illegal and are not searched candidates.
            for unit in range(-1,5):
                xx=[int(i==unit) for i in range(5)]
                g=(0,0)
                for var,reverse in word:
                    h=(0,0) if var is None else (xx[var],bits[var])
                    g=mul(g,inv(h) if reverse else h)
                assert g==((16*const+sum(c*x for c,x in zip(coeff,xx)))%32,oldphase)
                calibration+=1
        counts.append([[len(slots[s,p]) for p in range(2)] for s in range(2)])
    minimum=min(c for root in counts for side in root for c in side)
    records.append(dict(phase_mask=phase,phases_a_b_h1_h2_h3=bits,distinct_affine_form_counts_by_root_target_phase=counts,minimum_fiber_capacity=minimum,passes_capacity=minimum>=32,both_internal_odd=bits[0]==bits[1]==1))
survivors=[r for r in records if r['passes_capacity']]
cpu=time.process_time()-started
assert cpu<10
result=dict(status='COMPLETE_32_PHASE_NECESSARY_CAPACITY_SCREEN',n=128,degree=6,target_D=3,group='Q64',variable_order=['a','b','h1','h2','h3'],cross_anchor='h0=e',phase_patterns=32,capacity_target_per_phase_fiber=32,surviving_patterns=len(survivors),surviving_both_internal_odd=sum(r['both_internal_odd'] for r in survivors),best_minimum_fiber_capacity=max(r['minimum_fiber_capacity'] for r in records),records=records,survivors=survivors,formal_short_words_per_root=187,arithmetic_calibration_word_assignments=calibration,actual_parameter_searches=0,graphs_expanded=0,BFS_roots=0,CPU_seconds=cpu,CPU_budget_seconds=10,entire_graph_family_excluded=not survivors)
(P/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['status','surviving_patterns','surviving_both_internal_odd','best_minimum_fiber_capacity','CPU_seconds','arithmetic_calibration_word_assignments']}))
