#!/usr/bin/env python3
"""Complete reduced voltage design for internal degrees 2222 over Z15.

Analytic reduction fixes A0=A1={+-3}, A2=A3={+-6}. Each of the four
cross-triples is a transversal modulo three. Only the two nonadjacent orbit
pairs remain after same-orbit coverage; they are checked exactly.
"""
import itertools
import json
import time
from pathlib import Path

M=15
FULL=(1<<M)-1
OUT=Path(__file__).with_suffix("")


def mask(a):
    return sum(1<<i for i in a)


def sums(a,b):
    return mask({(x+y)%M for x in a for y in b})


def negative(a):
    return tuple(sorted((-x)%M for x in a))


def expand(params):
    x,y,z,w=(params[k] for k in ("X","Y","Z","W"))
    c=[[(3,12),(),x,y],[(),(3,12),z,w],
       [negative(x),negative(z),(6,9),()],
       [negative(y),negative(w),(),(6,9)]]
    missing=[];score=0;edges=set()
    for i in range(4):
        for j in range(i,4):
            cover=mask(c[i][j])|(1 if i==j else 0)
            for k in range(4):cover|=sums(c[i][k],c[k][j])
            bad=[t for t in range(M) if not (cover>>t)&1]
            if i==j:assert not bad
            missing.append(dict(orbits=[i,j],missing_offsets=bad))
            score+=len(bad)*M
    for i in range(4):
        for j in range(4):
            for t in range(M):
                for d in c[i][j]:
                    u,v=i*M+t,j*M+(t+d)%M
                    assert u!=v
                    edges.add(tuple(sorted((u,v))))
    assert len(edges)==240
    return dict(n=60,edges=sorted(edges),parameters=params,
                voltage_bad_pair_count=score,missing_offsets=missing)


def main():
    start=time.process_time()
    triples=[tuple(sorted(t)) for t in itertools.product(range(0,15,3),range(1,15,3),range(2,15,3))]
    triples.sort()
    norm=[i for i,t in enumerate(triples) if 0 in t]
    neg=[negative(t) for t in triples]
    diff=[sums(t,nt) for t,nt in zip(triples,neg)]
    h=mask((0,3,6,9,12))
    compat=[[j for j in range(125) if (diff[i]|diff[j]|h)==FULL] for i in range(125)]
    compatsets=[set(t) for t in compat]
    cross=[[sums(a,nb) for nb in neg] for a in triples]
    cases=0;first=0;target=0;hist={};best=None;bestscore=None
    for i in norm:
        for j in norm:
            if j not in compatsets[i]:continue
            for k in norm:
                if k not in compatsets[i]:continue
                for l in sorted(compatsets[j]&compatsets[k]):
                    cases+=1
                    c01=cross[i][k]|cross[j][l]
                    c23=cross[j][i]|cross[l][k]
                    score=30-c01.bit_count()-c23.bit_count()
                    first+=c01==FULL
                    target+=score==0
                    hist[score*15]=hist.get(score*15,0)+1
                    if bestscore is None or score<bestscore:
                        bestscore=score
                        best=expand(dict(X=triples[i],Y=triples[j],Z=triples[k],W=triples[l],
                                         A0=[3,12],A1=[3,12],A2=[6,9],A3=[6,9]))
                        assert best["voltage_bad_pair_count"]==score*15
    assert best is not None
    path=OUT.with_name(OUT.name+".best.edges.json")
    path.write_text(json.dumps(best,indent=2)+"\n")
    result=dict(modulus=15,scope="2222 quotient after analytic primitive-character reduction",
                transversals=len(triples),normalized_tree_transversals=len(norm),
                cases_with_all_same_orbit_coverage=cases,
                first_remaining_orbit_pair_covered=first,valid_targets=target,
                bad_pair_histogram=hist,best_bad_pair_count=best["voltage_bad_pair_count"],
                best_parameters=best["parameters"],best_candidate_file=path.name,
                cpu_seconds=time.process_time()-start,
                exhaustive_family_exclusion=target==0)
    OUT.with_suffix(".results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":main()
