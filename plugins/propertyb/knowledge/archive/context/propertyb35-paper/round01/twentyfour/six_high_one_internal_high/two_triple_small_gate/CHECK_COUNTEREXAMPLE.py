"""A ten-point signed counterexample; check all 32 minimal and 1024 red sets."""
from itertools import product
from pathlib import Path
import json
import time


def construct():
    positives = [[2*i, 2*i+1] for i in range(5)]
    triples = [[0,2,4], [1,2,4]]
    quads = [[b,5,6,8+c] for b,c in product(range(2), repeat=2)]
    quads += [[3,4,6,8+c] for c in range(2)]
    quads += [[b,3,7,8+c] for b,c in product(range(2), repeat=2)]
    quads += [[2,5,7,8+c] for c in range(2)]
    return dict(ground=list(range(10)), positive_sets=positives,
                negative_triples=triples, negative_quads=quads)


def verify(witness):
    p = [set(a) for a in witness['positive_sets']]
    t = [set(a) for a in witness['negative_triples']]
    b = [set(a) for a in witness['negative_quads']]
    assert len(p)==5 and all(len(a)==2 for a in p)
    assert len(t)==2 and all(len(a)==3 for a in t)
    assert len(b)==12 and all(len(a)==4 for a in b)
    assert len({tuple(sorted(a)) for a in t+b})==14
    degrees=[]
    for v in witness['ground']:
        a=sum(v in f for f in p)
        c=sum(v in f for f in t)
        d=sum(v in f for f in b)
        assert a==1 and c+d<=6 and a+c+d<=7
        degrees.append(dict(point=v,positive=a,negative_triple=c,
                            negative_quad=d,total=a+c+d))
    # Direct set inclusion on every minimal transversal.
    minimal=[]
    for choices in product(range(2),repeat=5):
        red={2*i+choices[i] for i in range(5)}
        blockers=[f'T{i}' for i,f in enumerate(t) if f<=red]
        blockers += [f'B{i}' for i,f in enumerate(b) if f<=red]
        assert len(blockers)==1
        minimal.append(dict(bits=choices,red=sorted(red),blockers=blockers))
    # Separate bit-mask method on all red subsets, not only minimal ones.
    pm=[sum(1<<v for v in a) for a in witness['positive_sets']]
    nm=[sum(1<<v for v in a) for a in witness['negative_triples']+witness['negative_quads']]
    hitting=0
    repairs=[]
    for mask in range(1<<10):
        if all(mask&a for a in pm):
            hitting+=1
            if all(mask&a!=a for a in nm):repairs.append(mask)
    assert hitting==3**5==243 and not repairs
    directions=[0]*5
    for a in b:
        fixed={v//2 for v in a}
        assert len(fixed)==4
        directions[next(i for i in range(5) if i not in fixed)]+=1
    assert directions==[4,4,4,0,0]
    return dict(status='PASS_COUNTEREXAMPLE',point_occurrences=degrees,
                minimal_transversal_count=32,minimal_transversals=minimal,
                all_red_subsets_checked=1024,hitting_red_subsets=243,
                repair_count=0,quad_cube_direction_counts=directions,
                minimum_transversal_blocker_count=1,maximum_transversal_blocker_count=1)


def main():
    start=time.process_time()
    witness=construct()
    result=dict(witness=witness,verification=verify(witness),
                scope='signed-set counterexample only; not a five-uniform H or 35-edge counterexample',
                process_seconds=time.process_time()-start)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(status=result['verification']['status'],
                          repair_count=0,red_subsets=1024,
                          degrees=[r['total'] for r in result['verification']['point_occurrences']],
                          process_seconds=result['process_seconds'])))


if __name__=='__main__':main()
