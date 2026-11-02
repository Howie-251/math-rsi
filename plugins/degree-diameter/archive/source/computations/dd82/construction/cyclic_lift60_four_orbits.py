#!/usr/bin/env python3
"""Exact difference-family search for the Z15 four-orbit (3,3,2) design.

All same-orbit pairs are automatically covered, via a partition of the seven
unsigned difference types. Root cross-covers uniquely determine the other two
triple sets, reducing the exact feasibility check to 7560 normalized cases.
"""
import itertools
import json
import time
from collections import defaultdict
from pathlib import Path

M = 15
FULL = (1 << M)-1
OUT = Path(__file__).with_suffix("")


def mask(a):
    return sum(1 << t for t in a)


def sm(a,b):
    return mask({(x+y)%M for x in a for y in b})


def neg(a):
    return tuple(sorted((-x)%M for x in a))


def differences(a):
    return tuple(sorted({min((x-y)%M,(y-x)%M)
                         for x,y in itertools.combinations(a,2)}))


def expand_and_check(params):
    x,y,z,w,u,v = (tuple(params[k]) for k in ("X","Y","Z","W","U","V"))
    c = [[(),x,y,u], [neg(x),(),v,z], [neg(y),neg(v),(),w],
         [neg(u),neg(z),neg(w),()]]
    missing = []
    score = 0
    for i in range(4):
        for j in range(i,4):
            cover = mask(c[i][j]) | (1 if i==j else 0)
            for k in range(4):
                cover |= sm(c[i][k],c[k][j])
            bad = [t for t in range(M) if not (cover>>t)&1]
            if i == j:
                assert not bad
            score += len(bad)*M
            missing.append(dict(orbits=[i,j],missing_offsets=bad))
    edges = set()
    for i in range(4):
        for j in range(i+1,4):
            for t in range(M):
                for d in c[i][j]:
                    edges.add((i*M+t,j*M+(t+d)%M))
    assert len(edges)==240
    return dict(n=60,edges=sorted(edges),parameters=params,
                voltage_bad_pair_count=score,missing_offsets=missing)


def main():
    start = time.process_time()
    normal = defaultdict(list)
    allsets = defaultdict(list)
    for triple in itertools.combinations(range(M),3):
        ds = differences(triple)
        if len(ds)==3:
            allsets[ds].append(triple)
            if triple[0]==0:
                normal[ds].append(triple)
    pairs = []
    cases = 0
    first_root = 0
    both_root = 0
    exact_score_hist = defaultdict(int)
    diagnostic = None
    diagnostic_root_missing = None
    best_exact = None
    by_complement = []
    for p in sorted(normal):
        for q in sorted(normal):
            if set(p)&set(q):
                continue
            d = (set(range(1,8))-set(p)-set(q)).pop()
            pairs.append(dict(P=p,Q=q,u=d))
            u = (0,d)
            zoptions = [(z,sm(u,neg(z))) for z in allsets[q]]
            woptions = [(w,sm(u,neg(w))) for w in allsets[p]]
            # Convolution by the two-element U is invertible in an odd group.
            assert len({m for _,m in zoptions})==len(zoptions)
            assert len({m for _,m in woptions})==len(woptions)
            zdict = {m:z for z,m in zoptions}
            wdict = {m:w for w,m in woptions}
            subtotal = [0,0,0]
            for x in normal[p]:
                for y in normal[q]:
                    for t in range(M):
                        v = tuple(sorted((t,(t+d)%M)))
                        cases += 1
                        subtotal[0] += 1
                        xy = mask(x)|sm(y,neg(v))
                        yx = mask(y)|sm(x,v)
                        z = zdict.get(FULL^xy) if xy.bit_count()==9 else None
                        w = wdict.get(FULL^yx) if yx.bit_count()==9 else None
                        if z is not None:
                            first_root += 1
                            subtotal[1] += 1
                        if z is not None and w is not None:
                            both_root += 1
                            subtotal[2] += 1
                            obj = expand_and_check(dict(X=x,Y=y,Z=z,W=w,U=u,V=v))
                            score = obj["voltage_bad_pair_count"]
                            exact_score_hist[score] += 1
                            if best_exact is None or score<best_exact["voltage_bad_pair_count"]:
                                best_exact = obj
                        # Also preserve a fully defined failed graph if the two
                        # exact root obligations have no simultaneous solution.
                        z0,mz = max(zoptions,key=lambda item:(xy|item[1]).bit_count())
                        w0,mw = max(woptions,key=lambda item:(yx|item[1]).bit_count())
                        badroot = 30-(xy|mz).bit_count()-(yx|mw).bit_count()
                        if diagnostic_root_missing is None or badroot<=diagnostic_root_missing:
                            obj = expand_and_check(dict(X=x,Y=y,Z=z0,W=w0,U=u,V=v))
                            if diagnostic_root_missing is None or badroot<diagnostic_root_missing or \
                                    obj["voltage_bad_pair_count"]<diagnostic["voltage_bad_pair_count"]:
                                diagnostic_root_missing=badroot
                                diagnostic=obj
            by_complement.append(dict(P=p,Q=q,u=d,cases=subtotal[0],
                                      first_root_exact=subtotal[1],both_root_exact=subtotal[2]))
    chosen = best_exact if best_exact is not None else diagnostic
    assert chosen is not None
    candidate = OUT.with_name(OUT.name+".best.edges.json")
    candidate.write_text(json.dumps(chosen,indent=2)+"\n")
    result = dict(modulus=M,scope="empty internal sets; cross sizes 3,3,2,2,3,3",
                  triple_difference_types=len(normal),normalized_triples=sum(map(len,normal.values())),
                  complementary_pairs=pairs,normalized_cases=cases,
                  first_root_exact=first_root,both_root_exact=both_root,
                  exact_root_graph_bad_pair_histogram=dict(exact_score_hist),
                  complement_counts=by_complement,cpu_seconds=time.process_time()-start,
                  candidate_file=candidate.name,candidate_parameters=chosen["parameters"],
                  candidate_bad_pair_count=chosen["voltage_bad_pair_count"],
                  candidate_selection="best exact-root completion" if best_exact else
                      "one greedy completion per normalized case, minimized first on root missing offsets",
                  diagnostic_root_missing_offsets=diagnostic_root_missing,
                  target_found=chosen["voltage_bad_pair_count"]==0,
                  exhaustive_family_exclusion=not any(k==0 for k in exact_score_hist))
    OUT.with_suffix(".results.json").write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__=="__main__":
    main()
