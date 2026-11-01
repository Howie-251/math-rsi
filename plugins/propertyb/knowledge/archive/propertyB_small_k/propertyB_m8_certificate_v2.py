"""Exact arithmetic certificates for m(8)>=266 and m(9)>=542.

Requires Python 3.10+, standard library only.
Mathematical interface: a minimum-vertex non-Property-B counterexample has
all vertex-pairs covered. A locked random-greedy coloring can fail only with
an ordered edge pair intersecting exactly in their common center.

Stage boundaries were chosen after exploratory calculations; this independent
script checks every parameter case in the stated exhaustive ranges.
"""
from math import comb
from fractions import Fraction as F
from functools import lru_cache
from itertools import combinations_with_replacement


def C(n, r):
    return comb(n, r) if n >= 0 and 0 <= r <= n else 0

def CEIL(a, b):
    return -(-a // b)

class Calculator:
    def __init__(self, k, m):
        self.k, self.m = k, m

    @lru_cache(None)
    def context(self, v, positions, h):
        before = sum(z not in positions for z in range(1, h))
        after = sum(z not in positions for z in range(h + 1, v + 1))
        left_mask = sum(1 << i for i, z in enumerate(positions) if z < h)
        right_mask = sum(1 << i for i, z in enumerate(positions) if z > h)
        center = positions.index(h) if h in positions else -1
        return before, after, left_mask, right_mask, center

    @lru_cache(None)
    def endpoint(self, v, pos, h, typ, last):
        n = v - len(pos)
        a, b, left, right, j = self.context(v, pos, h)
        r = self.k - typ.bit_count()
        allowed = left if last else right
        capacity = a if last else b
        if j < 0:
            if not n or not r or typ & ~allowed:
                return F(0)
            return F(r * C(capacity, r-1), n * C(n-1, r-1))
        if not typ & (1 << j) or (typ & ~(1 << j)) & ~allowed:
            return F(0)
        return F(C(capacity, r), C(n, r))

    @lru_cache(None)
    def weight(self, v, pos, h, typ_a, typ_b):
        n = v - len(pos)
        a, b, left, right, j = self.context(v, pos, h)
        r, t = self.k - typ_a.bit_count(), self.k - typ_b.bit_count()
        if j < 0:
            if typ_a & ~left or typ_b & ~right or min(r, t) < 1 or r+t-1 > n:
                return F(0)
            return F(C(a, r-1) * C(b, t-1),
                     n * C(n-1, r-1) * C(n-r, t-1))
        if (typ_a & typ_b) != (1 << j) or (typ_a & ~(1 << j)) & ~left \
            or (typ_b & ~(1 << j)) & ~right or r+t > n:
            return F(0)
        return F(C(a, r) * C(b, t), C(n, r) * C(n-r, t))

    def deletion(self, v, pos, counts, j):
        h = pos[j]
        degree = sum(n for typ, n in counts.items() if typ & (1 << j))
        excess = (self.k-1)*degree - (v-1)
        assert excess >= 0
        q = CEIL(excess, self.k-2)
        types = [typ for typ in counts if typ & (1 << j)]
        cells = []
        for i, t in enumerate(types):
            for u in types[i:]:
                cap = C(counts[t], 2) if t == u else counts[t] * counts[u]
                if cap:
                    w = self.weight(v,pos,h,t,u) + self.weight(v,pos,h,u,t)
                    cells.append((w, cap))
        assert sum(c for _,c in cells) >= q
        cells.sort()
        val = F(0)
        for weight, cap in cells:
            taken = min(q, cap)
            val += weight * taken
            q -= taken
            if q == 0:
                break
        assert q == 0
        return val

    def bound(self, v, positions, counts):
        pos = tuple(positions)
        assert len(set(pos)) == len(pos) and sum(counts.values()) == self.m
        assert min(counts.values()) >= 0
        D = {pos[j]: self.deletion(v,pos,counts,j) for j in range(len(pos))}
        total = F(0)
        for h in range(1, v+1):
            a = sum(num*self.endpoint(v,pos,h,t,True) for t,num in counts.items())
            b = sum(num*self.endpoint(v,pos,h,t,False) for t,num in counts.items())
            c = sum(num*(num_b-(t==u))*self.weight(v,pos,h,t,u)
                    for t,num in counts.items() for u,num_b in counts.items())
            c -= D.get(h, F(0))
            assert c >= 0
            total += min(a,b,c)
        return total

    def unlocked(self, v):
        k,m = self.k,self.m
        overlapping = max(0,CEIL(m*C(k,2)-C(v,2), C(k-1,2)))
        ordered = m*(m-1)-2*overlapping
        ans = F(0)
        for h in range(1,v+1):
            a = F(m*k*C(h-1,k-1),v*C(v-1,k-1))
            b = F(m*k*C(v-h,k-1),v*C(v-1,k-1))
            w = F(C(h-1,k-1)*C(v-h,k-1),
                  v*C(v-1,k-1)*C(v-k,k-1))
            ans += min(a,b,ordered*w)
        return ans

    def one(self,v,d):
        return self.bound(v,(v//2,),{0:self.m-d,1:d})

    def two(self,v,d,e):
        return self.bound(v,(v//2,v//2+1),
                          {0:self.m-d-e+1,1:d-1,2:e-1,3:1})

    def three(self,v,ds,triple):
        d,e,f=ds
        if triple:
            prof={0:self.m-d-e-f+2,1:d-1,2:e-1,4:f-1,7:1}
        else:
            prof={0:self.m-d-e-f+3,1:d-2,2:e-2,4:f-2,
                  3:1,5:1,6:1}
        return self.bound(v,(v//2-1,v//2,v//2+1),prof)


def check_triple_existence(k,m, v, degree_cap):
    """Caro--Wei and exact total-degree inequality force 3 low-degree
    pairwise-codegree-one vertices. Tests the bound for every feasible |L|.
    """
    d0=CEIL(v-1,k-1)
    assert degree_cap>=d0
    sumdeg=k*m
    rmin=max(1, CEIL((degree_cap+1)*v-sumdeg,degree_cap+1-d0))
    assert rmin<=v
    A=(k-1)*(degree_cap+1)-(v-1)
    B=(k-1)*(sumdeg-(degree_cap+1)*v)
    for r in range(rmin,v+1):
        assert A*r+B >= 0, (k,m,v,r,'invalid pair upper bound')
        assert r*r > 2*((A+1)*r+B), (k,m,v,r,'CW insufficient')
    return rmin


def check_one_case(cal, tag, v, degrees):
    values=[]
    for d in degrees:
        value=cal.one(v,d)
        assert value<1,(tag,v,d,value)
        values.append(value)
    return max(values)


def check_two_case(cal,v):
    k,m=cal.k,cal.m
    values=[]
    for d in range(CEIL(v-1,k-1),k*m//v+1):
        s=2*(v-1)-(k-1)*d
        assert s>0,(k,m,v,d,'missing codegree-one neighbor')
        B=next(b for b in range(d,m+1)
               if v*d+s*(b+1-d)>k*m)
        for e in range(d,B+1):
            assert m-d-e+1>=0,(k,m,v,d,e,'infeasible profile')
            value=cal.two(v,d,e)
            assert value<1,(k,m,v,d,e,value)
            values.append(value)
    return values


def certify(k,m,parts,degree_cap):
    cal=Calculator(k,m)
    first=parts[0][0]
    last=parts[-1][1]
    for v in range(2*k-1,first):
        assert F(m*(C(v//2,k)+C(v-v//2,k)),C(v,k))<1,(k,v,'balance')
    assert (last+1)*CEIL(last,k-1)>k*m,(k,m,'upper bound')
    for v in range(first,last+1):
        assert v*CEIL(v-1,k-1)<=k*m
    records={name:[] for _,_,name in parts}
    profiles=0
    for lo,hi,stage in parts:
        for v in range(lo,hi+1):
            if stage=='unlocked':
                value=cal.unlocked(v)
                assert value<1,(k,m,stage,v,value)
                records[stage].append((value,v,'-'))
                profiles+=1
            elif stage=='one':
                degrees=range(CEIL(v-1,k-1),k*m//v+1)
                for d in degrees:
                    value=cal.one(v,d)
                    assert value<1,(k,m,stage,v,d,value)
                    records[stage].append((value,v,str(d)))
                    profiles+=1
            elif stage=='two':
                vals=check_two_case(cal,v)
                records[stage].append((max(vals),v,'worst'))
                profiles+=len(vals)
            elif stage=='three':
                check_triple_existence(k,m,v,degree_cap)
                for ds in combinations_with_replacement(range(CEIL(v-1,k-1),degree_cap+1),3):
                    for triple in (False,True):
                        value=cal.three(v,ds,triple)
                        assert value<1,(k,m,stage,v,ds,triple,value)
                        records[stage].append((value,v,str((ds,triple))))
                        profiles+=1
            else:
                raise ValueError(stage)
    print(f'\nCERTIFIED: every {k}-uniform hypergraph with <= {m} edges is 2-colorable')
    print(f'THEOREM: m({k}) >= {m+1}; {profiles} exact rational profiles verified')
    for stage,vals in records.items():
        w=max(vals)
        print(f'  {stage:8s}: {len(vals):4d} records; max U={w[0]} at v={w[1]}, type={w[2]}')
    return records


if __name__ == '__main__':
    certify(8,265,[(47, 84, 'unlocked'), (85, 94, 'one'), (95, 107, 'two'), (108, 120, 'three')],20)
    print('PASS')
