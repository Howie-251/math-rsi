"""Fixed-word formal endpoint algebra mod Phi18. No graph or field grid."""
from collections import Counter
from pathlib import Path
import json
import resource
import time

start=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(10,10))
out=Path(__file__).resolve().parent
zero=(0,)*6
one=(1,0,0,0,0,0)
def times_r(p):
    q=[0]+list(p)
    top=q.pop()
    q[0]-=top
    q[3]+=top
    return tuple(q)
powers=[one]
for j in range(18):powers.append(times_r(powers[-1]))
assert powers[18]==one
def rotate(p,j):
    return tuple(sum(p[k]*powers[(k+j)%18][i] for k in range(6)) for i in range(6))
def negative(p):return tuple(-a for a in p)

A=(0,0,-1,-1,0,0)
B=(-1,0,-1,0,0,0)
assert tuple(a-b for a,b in zip(A,B))==negative(powers[6])
spec=[(0,1,0,zero),(0,2,0,zero),(1,2,6,one),(0,1,10,A),(0,1,14,B),(2,2,3,zero)]
darts=[]
for u,v,j,p in spec:
    darts.append((u,v,j,p))
    darts.append((v,u,(-j)%36,negative(rotate(p,(-j)%18))))
outgoing=[[i for i,d in enumerate(darts) if d[0]==u] for u in range(3)]
rotated=[[rotate(d[3],j%18) for d in darts] for j in range(36)]
all_sets=[]
all_count=0
for root in range(3):
    sets=[[set() for _ in range(36)] for _ in range(3)]
    def visit(v,j,p,last,depth):
        global all_count
        all_count+=1
        sets[v][j].add(p)
        if depth==9:return
        for k in outgoing[v]:
            if k!=(last^1):
                d=darts[k]
                q=tuple(a+b for a,b in zip(p,rotated[j][k]))
                visit(d[1],(j+d[2])%36,q,k,depth+1)
    visit(root,0,zero,-1,0)
    all_sets.append(sets)

slots=[]
for root in range(3):
    for target in range(3):
        for j in range(36):
            slots.append({'root_base':root,'target_base':target,'phase':j,
                          'formal_distinct_count':len(all_sets[root][target][j])})
minimum=min(s['formal_distinct_count'] for s in slots)
result={'status':'COMPLETE_FIXED_CYCLOTOMIC_ENDPOINT_CAPACITY',
        'prediction_disposition':'SUPPORTED' if minimum>=109 else 'REFUTED',
        'ring':'Z[r]/(r^6-r^3+1), integer coefficientbasis1,r,r²,r³,r⁴,r⁵',
        'fixed_offset_rule':{'A':A,'B':B,'C':one,'loop':zero},
        'coefficient_relation':'A-B=-r^6',
        'named_NB_words_enumerated':all_count,'expected_words':3*39365,
        'minimum_formal_endpoint_count':minimum,
        'minimum_slots':[s for s in slots if s['formal_distinct_count']==minimum],
        'formal_count_histogram':dict(Counter(s['formal_distinct_count'] for s in slots)),
        'module109_formally_excluded':minimum<109,
        'actual_field_evaluation_performed':False,
        'scope':'Fixedcanonicaloffsetpolynomialfamily only. Different integer6tuples may coincide after evaluating a chosenfield; enoughformalendpoints is not a coverageproof.',
        'CPU_seconds':time.process_time()-start,'graph_generation':False,'BFS':0,'parameter_grid':False,'pending':[]}
assert all_count==3*39365
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'SLOTS.json').write_text(json.dumps(slots,indent=2)+'\n')
with (out/'POLYNOMIAL_SETS.json').open('w') as f:
    json.dump([{'root_base':root,'target_base':target,'phase':j,'polynomials':sorted(all_sets[root][target][j])}
               for root in range(3) for target in range(3) for j in range(36)],f,separators=(',',':'))
(out/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='formal_count_histogram'},indent=2))
