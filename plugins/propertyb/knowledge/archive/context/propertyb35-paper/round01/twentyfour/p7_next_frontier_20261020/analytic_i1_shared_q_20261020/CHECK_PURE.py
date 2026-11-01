"""Scalar support for r5..8 proofs; not a P-source checker."""
from itertools import product
from pathlib import Path
import json

DIR=Path(__file__).parent
r5=[]
for x0,x1,x2 in product(range(6),repeat=3):
    if x0+x1+x2!=5:
        continue
    H=x1+2*x2
    if H<5:
        continue
    upper=15-2*H+x2+1+H
    assert H-x2>=(H+1)//2>=3
    assert upper<=13<14
    r5.append(dict(x=[x0,x1,x2],H_C=H,J_upper=upper))

r6=[]
for H in [6,7,8]:
    for h0,h1 in product(range(7),repeat=2):
        if h0+h1!=18-H:
            continue
        assert sorted([h0,h1]) in [[6,6],[5,6],[4,6],[5,5]]
        for s0 in range(8-h0+1):
            for s1 in range(8-h1+1):
                if s0+s1 < 10-(20-2*H):
                    continue
                if [h0,h1]!=[5,5]:
                    assert any(h==6 and s>=1 for h,s in [(h0,s0),(h1,s1)])
                else:
                    assert s0==s1==3
                r6.append(dict(H_C=H,D_h=[h0,h1],D_s=[s0,s1]))

calls=[]
for hd in [6,7]:
    for sq in [0,1]:
        for sd in range(9-hd):
            for ell in range(min(sq,sd)+1):
                m4=5-sq+8-hd-sd
                t=3-sq-sd+ell
                if hd==6 and (sq,sd,ell)==(1,1,1):
                    gate="requires_non_neighbor_selection"
                elif ell==0:
                    assert m4<=7 and t<=4 and 24-m4<=35
                    gate="pure_at_most_seven"
                else:
                    assert m4+ell<=5 and t<=3
                    gate="five_mixed_three_T"
                calls.append(dict(D_h=hd,q_s=sq,D_s=sd,J_qd=ell,m4=m4,m3=ell,T=t,gate=gate))

r8=[]
for h in product(range(4),repeat=5):
    H=sum(h)
    if H>=12:
        assert h.count(3)>=2
        r8.append(dict(C_h=list(h),H_C=H,h3_count=h.count(3)))
r8_calls=[]
for sq in [0,1]:
    m,negative_pairs,t,B=4-sq,5,1-sq,25-(4-sq)
    assert 0<=m<=4 and negative_pairs<=5 and 0<=t<=2
    assert negative_pairs+t+B==27
    r8_calls.append(dict(q_h=3,q_s=sq,m4=m,N2=negative_pairs,T=t,B=B,
                         D=7,gate="four_large_five_pairs_two_T"))
pure_inventories=[[17-2*r,r,0] for r in range(9)]
assert len(pure_inventories)==9 and all(row[0]>=0 for row in pure_inventories)
out=dict(status="PASS",scope="scalar necessary cases and imported gate parameters only",
         r5_frequency_rows=len(r5),r6_D_rows=r6,r7_gate_calls=calls,
         r8_required_frequency_rows=len(r8),r8_gate_calls=r8_calls,
         all_pure_inventories=pure_inventories,
         new_pure_whole_inventories=[[7,5,0],[5,6,0],[3,7,0],[1,8,0]],
         mathematical_scope="all nine pure P3 inventories; imported-gate cross-family review status recorded separately")
(DIR/"CHECK_PURE.json").write_text(json.dumps(out,indent=2)+"\n")
print(dict(status="PASS",r5_frequency_rows=len(r5),r6_D_rows=len(r6),
           r7_gate_calls=len(calls),r8_required_frequency_rows=len(r8),
           r8_gate_calls=len(r8_calls),all_pure_inventories=len(pure_inventories)))
