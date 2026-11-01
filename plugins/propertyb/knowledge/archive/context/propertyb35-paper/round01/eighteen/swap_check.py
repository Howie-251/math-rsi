#!/usr/bin/env python3
"""Exact local swap counts; fixed edge pairs only, not a hypergraph search."""
from itertools import combinations
from math import comb
import json, time
from pathlib import Path
OUT = Path(__file__).resolve().parent
N=18
E=sum(1<<i for i in range(5))
FULL=(1<<N)-1

def formula(t):
    red=2*(5-t)**2*comb(8+t,t)
    blue=2*5*comb(9,4) if t==1 else 0
    return {'new_same_colour':red,'new_opposite_colour':blue,'total':red+blue}

def direct(t):
    g=sum(1<<i for i in list(range(t))+list(range(5,10-t)))
    same=other=0
    # All source colourings where e is all red. Complement symmetry doubles.
    for rest in combinations(range(5,18),4):
        red=E | sum(1<<i for i in rest)
        blue=FULL^red
        if red&g in (0,g): continue  # target is not monochromatic in source
        for x in range(5):
            for y in range(5,18):
                if not (blue>>y)&1: continue
                new=red^(1<<x)^(1<<y)
                if new&g==g: same+=1
                elif new&g==0: other+=1
    return {'new_same_colour':2*same,'new_opposite_colour':2*other,'total':2*(same+other)}

start=time.perf_counter()
rows=[]
for t in range(5):
    f,d=formula(t),direct(t)
    assert f==d,(t,f,d)
    rows.append({'intersection':t,'formula':f,'direct_fixed_edge_pair_enumeration':d})
space=comb(18,9)
incidence=2*comb(13,4)
profiles=[]
for m in [34,35,36,37]:
    unique=2*space-m*incidence
    lhs=45*unique
    rhs=m*(m-1)*max(x['formula']['total'] for x in rows)
    profiles.append({'m':m,'balanced_space':space,'edge_incidence':incidence,'total_incidence':m*incidence,'unique_lower_bound_assuming_no_good':unique,'required_swap_incidence':lhs,'uniform_pair_swap_upper':rhs,'strict_slack':lhs-rhs,'contradiction':lhs>rhs})
result={'status':'exact_local_replay_pass','scope':'5 fixed intersection types, all 715 source red-containing-edge colourings and all 45 swaps per type; blue-source counts by complement bijection','rows':rows,'profiles':profiles,'elapsed_seconds':time.perf_counter()-start}
(OUT/'SWAP_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
