"""One arithmetic norm5 generator set on PSL2(F11); reduced words<=4 only.

This is an endpoint necessary screen, not a group/parameter search or graph BFS.
"""
from itertools import product
from pathlib import Path
import json
import time

HERE=Path(__file__).resolve().parent
Q=11

def canonical(m):
    m=tuple(x%Q for x in m)
    return min(m,tuple(-x%Q for x in m))

def multiply(a,b):
    return canonical((a[0]*b[0]+a[1]*b[2],a[0]*b[1]+a[1]*b[3],
                      a[2]*b[0]+a[3]*b[2],a[2]*b[1]+a[3]*b[3]))

def inverse(m):
    return canonical((m[3],-m[1],-m[2],m[0]))

def run():
    started=time.process_time()
    identity=canonical((1,0,0,1))
    group=sorted({canonical((a,b,c,d)) for a,b,c,d in product(range(Q),repeat=4)
                  if (a*d-b*c)%Q==1})
    assert len(group)==660
    # Quaternion I,J with I²=J²=-Id and IJ=-JI overF11; 1²+3²=-1.
    I=(1,3,3,-1)
    J=(0,1,-1,0)
    # Ordinary multiplication, since I/J have determinant1 but projective sign
    # canonicalization does not affect the six final PSL classes.
    def rawmul(a,b):
        return ((a[0]*b[0]+a[1]*b[2])%Q,(a[0]*b[1]+a[1]*b[3])%Q,
                (a[2]*b[0]+a[3]*b[2])%Q,(a[2]*b[1]+a[3]*b[3])%Q)
    K=rawmul(I,J)
    generators=[]
    for unit in [I,J,K]:
        for sign in [1,-1]:
            # norm(1+-2i)=5; sqrt5=4, inverse4=3, so determinant becomes1.
            m=tuple(3*(a+sign*2*b)%Q for a,b in zip((1,0,0,1),unit))
            generators.append(canonical(m))
    assert len(set(generators))==6 and identity not in generators
    assert all(g in group for g in generators)
    inverse_labels=[generators.index(inverse(m)) for m in generators]
    assert inverse_labels==[1,0,3,2,5,4]
    raw_by_length=[0]*5
    endpoints_by_length=[set() for _ in range(5)]
    def words(m,prev,depth):
        raw_by_length[depth]+=1
        endpoints_by_length[depth].add(m)
        if depth==4:
            return
        for label,g in enumerate(generators):
            if prev>=0 and label==inverse_labels[prev]:
                continue
            words(multiply(m,g),label,depth+1)
    words(identity,-1,0)
    assert raw_by_length==[1,6,30,150,750]
    reachable=set().union(*endpoints_by_length)
    missing=sorted(set(group)-reachable)
    cumulative=[]
    cum=set()
    for e in endpoints_by_length:
        cum|=e;cumulative.append(len(cum))
    result=dict(status='FIXED_NORM5_PSL11_D4_ENDPOINT_SCREEN_FAILED' if missing else 'UNIT_ROOT_D4_ENDPOINT_COVER_HIT',
                construction='Quaternion norm5 six generators, reduced modulo11 in PSL2(F11)',
                target_Delta=6,target_D=4,savedL=441,
                group_order=660,hypothetical_graph_edges=1980,order_margin=219,
                modulus=11,vertex_rule='determinant1 matrices modulo +/-Id; lexicographically least sign',
                quaternion_units_matrix_images=dict(I=I,J=J,K=K),
                quaternion_norm=5,determinant_normalization_scalar=3,
                quaternions=[[1,2,0,0],[1,-2,0,0],[1,0,2,0],[1,0,-2,0],[1,0,0,2],[1,0,0,-2]],
                generators=generators,inverse_labels=inverse_labels,
                raw_reduced_words_by_length=raw_by_length,total_reduced_words=sum(raw_by_length),
                distinct_endpoints_exact_length=list(map(len,endpoints_by_length)),
                distinct_endpoints_cumulative=cumulative,
                unit_root_missing_count=len(missing),missing_matrices=missing,
                first_missing_matrix=missing[0] if missing else None,
                scope='Exactly this modulus11 and six norm5 generator classes; no other group/modulus/generator choices.',
                ordinary_graph_BFS_performed=False,full_graph_adjacency_generated=False,
                random_search_performed=False,parameter_search_performed=False,
                new_lower_bounds=0,CPU_seconds=time.process_time()-started)
    (HERE/'PROBE.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ['missing_matrices','quaternions','quaternion_units_matrix_images','generators']}))
    return result

if __name__=='__main__':
    run()
