"""Fresh-reviewer falsification attempts; these checks do not replace the proof."""
from itertools import combinations, permutations
from fractions import Fraction as F
from math import comb, factorial, isqrt
from decimal import Decimal as D, localcontext
from pathlib import Path
import json
import time

started = time.process_time()


def mono(c, e):
    v = c & e
    return v == 0 or v == e


def inspect_hypergraph(n, k, edges):
    # All equiprobable initial colorings and delay orders; eligibility is grouped
    # by Hamming weight so all tested p values are checked exactly afterwards.
    f0 = [0] * (n + 1)
    f1 = [0] * (n + 1)
    orders = tuple(permutations(range(n)))
    gamma = sum((e & f).bit_count() == 1 for e in edges for f in edges if e != f)
    outcomes = 0
    for c in range(1 << n):
        initially = [e for e in edges if mono(c, e)]
        for b in range(1 << n):
            bw = b.bit_count()
            for order in orders:
                z = c
                for x in order:
                    bit = 1 << x
                    if not b & bit:
                        continue
                    if any(e & bit and (z & e) == (c & e) for e in initially):
                        z ^= bit
                old = any(mono(z, e) and (z & e) == (c & e) for e in initially)
                new = any(mono(z, e) and (z & e) != (c & e) for e in edges)
                f0[bw] += old
                f1[bw] += new
                outcomes += 1
    for p in (F(0), F(1, 3), F(1, 2), F(1)):
        prob0 = sum(F(f0[j], (1 << n) * factorial(n)) * p**j * (1-p)**(n-j) for j in range(n+1))
        prob1 = sum(F(f1[j], (1 << n) * factorial(n)) * p**j * (1-p)**(n-j) for j in range(n+1))
        a = 1 - (1-p)**k
        integ = sum(F((-1)**j * comb(k-1, j), 2*j+1) * p**(2*j+1) for j in range(k))
        if edges:
            # Raising nonnegative sides to d exactly checks the Jensen bound.
            d = 2**(k-1)
            assert (1-prob0)**d >= a**len(edges), (n,k,edges,p,'old')
        assert prob1 <= F(gamma, 4**(k-1))*integ, (n,k,edges,p,'new')
    return outcomes


graphs = outcomes = 0
for n in range(2, 5):
    for k in range(2, min(n, 3)+1):
        universe = [sum(1 << x for x in edge) for edge in combinations(range(n), k)]
        for mask in range(1 << len(universe)):
            edges = [e for i,e in enumerate(universe) if mask >> i & 1]
            outcomes += inspect_hypergraph(n,k,edges)
            graphs += 1
# Two 3-edges with one shared vertex exercises the distinct-set blame bound.
outcomes += inspect_hypergraph(5,3,[0b00111,0b11001])
graphs += 1

# Triangle: for k=2,M=3 the criterion must never accept the non-B example.
# Check polynomial identity Q^2-a^3 = p^2(1-p)^3(9-5p)/4 coefficientwise.
def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c
def power(a,n):
    r=[F(1)]
    for _ in range(n): r=mul(r,a)
    return r
q2=power([0,F(3,2),0,F(-1,2)],2)
a3=power([0,2,-1],3)
lhs=[x-y for x,y in zip(q2,a3)]
rhs=mul([0,0,F(1,4)],mul(power([1,-1],3),[9,-5]))
assert lhs==rhs

# Fano plane is a no-common-point clique reaching k^2-k+1 and is non-B.
fano=[(0,1,2),(0,3,4),(0,5,6),(1,3,5),(1,4,6),(2,3,6),(2,4,5)]
fm=[sum(1 << x for x in e) for e in fano]
assert all((e&f).bit_count()==1 for e,f in combinations(fm,2))
assert not set.intersection(*(set(e) for e in fano))
assert all(any(mono(c,e) for e in fm) for c in range(128))
for k in (2,3,17):
    q=20
    star=[{0,*range(1+i*(k-1),1+(i+1)*(k-1))} for i in range(q)]
    assert len(set.union(*star))==q*(k-1)+1
    assert all(len(e&f)==1 for e,f in combinations(star,2))

# Decimal stress tests are explicitly only falsification, not an all-k proof
# or optimization/certification of B_RS. J is first evaluated as an exact rational.
scalar_checks=0
min_margin=None
with localcontext() as ctx:
    ctx.prec=70
    for k in (17,18,20,32,64,128):
        d=2**(k-1)
        for p in sorted({F(1,k*k),F(1,k),F(1),*(F(j,4*k) for j in range(1,21))}):
            a=1-(1-p)**k
            J=sum(F((-1)**j*comb(k-1,j),2*j+1)*p**(2*j+1) for j in range(k))
            la=(D(a.numerator)/D(a.denominator)).ln()
            lj=(D(J.numerator)/D(J.denominator)).ln()
            def accepted(m):
                if m==1:return True
                return D(m*(m-1)).ln()-2*D(d).ln()+lj < D(m)/D(d)*la
            lo,hi=1,k*2**k
            while lo+1<hi:
                mid=(lo+hi)//2
                if accepted(mid):lo=mid
                else:hi=mid
            M=lo
            if M<2**k:continue
            s=int(D(M).sqrt()/(8*(1+D(k).ln())))
            N=M+s
            v=(1+isqrt(1+4*k*(k-1)*N))//2
            r=min(v,max(k*k-k+1,(v-1)//(k-1)))
            g=min(F(N*(N-1)),F(N*N*(r-1),r))
            margin=D(N)/D(d)*la-((D(g.numerator)/D(g.denominator)).ln()-2*D(d).ln()+lj)
            assert s>=1 and r>1 and margin>0,(k,p,M,s,margin)
            scalar_checks+=1
            min_margin=min(min_margin,margin) if min_margin is not None else margin

result={
    'status':'PASS','purpose':'adversarial consistency checks; not the mathematical proof',
    'exact_recoloring_hypergraphs':graphs,'exact_recoloring_outcomes':outcomes,
    'rational_eligibility_probabilities':['0','1/3','1/2','1'],
    'type1_jensen_bound':'checked by exact rational powers',
    'type2_single_intersection_bound':'checked by exact rational arithmetic',
    'triangle_strictness_identity':'Q^2-a^3=p^2(1-p)^3(9-5p)/4 >= 0 on [0,1]',
    'fano':'all 128 colorings fail; 7-edge no-common-point clique saturates k^2-k+1',
    'common_point_stars':'20 edges, k=2,3,17; exact support equality checked',
    'scalar_stress_checks':scalar_checks,
    'scalar_precision_digits':70,
    'smallest_observed_positive_log_margin':str(min_margin),
    'counterexamples_found':0,'cpu_seconds':time.process_time()-started,
}
Path(__file__).with_name('COUNTEREXAMPLE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
