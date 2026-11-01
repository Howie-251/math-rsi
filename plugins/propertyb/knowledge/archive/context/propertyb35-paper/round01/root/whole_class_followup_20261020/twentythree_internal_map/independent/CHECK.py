#!/usr/bin/env python3
"""Independent direct-color single stars and additive-growth G-trace domain."""
from itertools import combinations, product
from collections import Counter
from math import comb
from pathlib import Path
from fractions import Fraction
from time import process_time
import json, sys
P=Path(__file__).resolve().parent
ROOT=P.parent
FULL=(1<<18)-1

def build(sizes,repeated):
    sets=[set() for _ in sizes]; nxt=0
    for memberships in repeated:
        for i in memberships: sets[i].add(nxt)
        nxt+=1
    for i,n in enumerate(sizes):
        while len(sets[i])<n: sets[i].add(nxt);nxt+=1
    assert nxt==18
    return [sum(1<<x for x in s) for s in sets]

def shapes():
    out=[]
    for n,rep in [('triple',[(0,1,2)]),('same',[(0,1),(0,1)]),('adjacent',[(0,1),(1,2)]),('disjoint',[(0,1),(2,3)])]:
        out.append(('w0_'+n,build([4]*5,rep),['']*5))
    for n,rep in [('34',[(0,1)]),('44',[(1,2)])]:
        for c in 'RB':out.append(('w1_'+n+'_'+c,build([3,4,4,4,4],rep),[c,'','','','']))
    for pin in ['RR','BB','RB']:
        out.append(('w2_double_'+pin,build([2,4,4,4,4],[]),[pin,'','','','']))
    for pin in ['RR','BB','RB']:
        out.append(('w2_two_'+pin,build([3,3,4,4,4],[]),[pin[0],pin[1],'','','']))
    return out

def masks(q): return [sum(1<<x for x in t) for t in combinations(range(18),q)]

def failures(blocks,pins,states):
    red=[b for b,p in zip(blocks,pins) if 'B' not in p]
    blue=[b for b,p in zip(blocks,pins) if 'R' not in p]
    total=0
    for m in states:
        if any((m&b)==0 for b in red) and any((m&b)==b for b in blue):total+=1
    return total

def inventory_domain():
    # Grow all admissible multisets from the empty one; unlike the source's
    # fixed trace-variable recursion this explores the submultiset lattice.
    alphabet=list(combinations(range(5),2))+list(combinations(range(5),3))
    seen={()}; todo=[()]
    while todo:
        old=todo.pop()
        spent=[sum(len(t)-1 for t in old if z in t) for z in range(4)]
        for t in alphabet:
            if any(spent[z]+len(t)-1>2 for z in t if z<4):continue
            new=tuple(sorted(old+(t,)))
            if new not in seen:seen.add(new);todo.append(new)
    return sorted(seen)

def single_deduction(q,c,m):
    if m<=1:return 0
    # Reconstruct every case from event intersection cardinalities.
    blue=(c=='B'); nblue=q
    def f(sz):
        k=nblue-sz if blue else nblue
        return comb(18-sz,k) if 0<=k<=18-sz else 0
    j=[f(8-i) for i in range(4)];t=[f(9),f(8)]
    mm=min(m,6)
    candidates=[j[3]+(mm-2)*j[0]]
    if mm>=3:candidates.append(2*j[2]+(mm-3)*j[0])
    for h in (0,1):
        u=max(0,4*mm-18-2*h)
        candidates.append(comb(mm,2)*j[0]+(j[1]-j[0])*u+(j[2]-j[0])*h-comb(mm,3)*t[0]-h*(mm-2)*(t[1]-t[0]))
    return min(candidates)+max(0,m-6)*j[0]

def cost(q,r,c):
    k=q-r if c=='B' else q
    return comb(18-r,k) if 0<=k<=18-r else 0

def run():
    start=process_time();S=shapes();states={q:masks(q) for q in (8,9)}
    count=5 if '--profile' in sys.argv else len(S)
    direct={}
    for name,blocks,pins in S[:count]:
        direct[name]={q:failures(blocks,pins,states[q]) for q in (8,9)}
    if '--profile' in sys.argv:
        out={'status':'PILOT_PASS','types':count,'direct_color_states':count*sum(map(len,states.values())),'cpu_seconds':process_time()-start,'counts':direct}
        (P/'PILOT.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out));return
    expect={'w0_triple':[2557,3186],'w0_same':[3186,3996],'w0_adjacent':[2967,3708],'w0_disjoint':[2940,3672],'w1_34_R':[2910,3984],'w1_34_B':[3558,3984],'w1_44_R':[2896,3975],'w1_44_B':[3567,3975],'w2_double_RR':[3486,5388],'w2_double_BB':[5598,5388],'w2_double_RB':[2334,2892],'w2_two_RR':[2568,3816],'w2_two_BB':[3726,3816],'w2_two_RB':[3906,4764]}
    assert all([direct[n][8],direct[n][9]]==v for n,v in expect.items())
    fail={}
    for q in (8,9):
        fail[q]={'w0':max(direct[n][q] for n in direct if n.startswith('w0'))}
        for c in 'RB':fail[q]['w1_'+c]=max(direct['w1_'+s+'_'+c][q] for s in ('34','44'))
        for kind in ('double','two'):
            for sig in ('RR','BB','RB'):fail[q]['w2_'+kind+'_'+sig]=direct['w2_'+kind+'_'+sig][q]
    domain=inventory_domain();assert len(domain)==732
    src=json.loads((ROOT/'HUNTER_RESULT.json').read_text())
    source={(tuple(sorted(tuple(t) for t in r['traces'])),r['d']):r for r in src['records']}
    assert len(source)==10209
    rows=[];residual=[];n_options=0;rawstrict=0;special_counts=Counter()
    for tr in domain:
        inc=Counter(z for t in tr for z in t); K=15+sum(len(t)-1 for t in tr)
        for d in range(max(6,1+inc[4]),K+1):
            singles=[5-inc[z] for z in range(4)]+[d-1-inc[4]]
            best=None;bestraw=None
            for free in combinations(range(4),2):
                if any(set(free)<=set(t) for t in tr):continue
                fixed=[z for z in range(5) if z not in free]
                for colors in product('RB',repeat=3):
                    if len(set(colors))==1:continue
                    col=dict(zip(fixed,colors));types=[]
                    for z in free:
                        groups=[tuple(col[v] for v in t if v!=z) for t in tr if z in t]
                        pins=''.join(sorted((c for g in groups for c in g),reverse=True));w=len(pins)
                        types.append('w0' if not w else 'w1_'+pins if w==1 else 'w2_'+('double_' if len(groups)==1 else 'two_')+pins)
                    for q in (8,9):
                        fixed_events=[]
                        for z in fixed:fixed_events.extend([(4,col[z])]*singles[z])
                        for t in tr:
                            if set(t)&set(free):continue
                            colors_t={col[z] for z in t}
                            if len(colors_t)==1:fixed_events.append((5-len(t),next(iter(colors_t))))
                        pure_count=K-d
                        raw=sum(cost(q,r,c) for r,c in fixed_events)+pure_count*(cost(q,5,'R')+cost(q,5,'B'))+sum(fail[q][kind] for kind in types)
                        nfixed=sum(singles[z] for z in fixed)+sum(not(set(t)&set(free)) for t in tr)+pure_count
                        assert nfixed==24
                        groups=Counter(col[z] for z in fixed for _ in range(singles[z]))
                        discount=sum(single_deduction(q,c,n) for c,n in groups.items())
                        total=raw-discount
                        item=(Fraction(total,comb(18,q)),total,q,list(free),col,types,dict(groups),discount)
                        rawitem=Fraction(raw,comb(18,q))
                        if best is None or item[0]<best[0]:best=item
                        if bestraw is None or rawitem<bestraw:bestraw=rawitem
                        n_options+=1
            assert best and best[1]==source[(tr,d)]['total'] and comb(18,best[2])==source[(tr,d)]['sample_space']
            rawstrict+=bestraw<1
            if best[0]<1:method='ordinary'
            elif not tr:
                assert d in (6,7);assert 47167-572*d<43758;method='external_three_free'
            else:
                assert len(tr)==2 and all(len(t)==2 and max(t)<4 for t in tr) and len(set(tr[0]+tr[1]))==4 and d in (6,7)
                method='new_three_free' if d==6 else 'red4_blue10'
            special_counts[method]+=1
            row={'traces':tr,'d':d,'total':best[1],'space':comb(18,best[2]),'method':method,'quota':best[2],'free':best[3],'colors':best[4],'free_types':best[5],'singleton_color_counts':best[6],'deduction':best[7]}
            rows.append(row)
            if best[0]>=1:residual.append(row)
    assert len(rows)==10209 and rawstrict==10160 and len(residual)==8
    assert 4*3003+4*1001+11*1573+2910+3567+3186==42982
    assert 8*2002+11*1430+2*3984+3996==43710
    blue10=[286+8,3*66+6,45+10*22,45+65+10*20-8,45+2*65+10*18-16,45+2*65+10*18-16-9,45+3*65+10*16-24-63]
    assert min(blue10)==204 and 4*3003+10*1001+10*1573+2910+3567-270-204==43755
    out={'status':'PASS','review_independence':'same-family','acceptance_status':'provisional','inventory_count':len(domain),'degree_keys':len(rows),'all_source_optimal_totals_equal':True,'direct_color_states':len(S)*sum(map(len,states.values())),'direct_counts':direct,'options_checked':n_options,'ordinary_raw_strict':rawstrict,'closure_counts':dict(special_counts),'residual':residual,'blue10_cases':blue10,'special_d7_margin':3,'cpu_seconds':process_time()-start,'rows':rows}
    (P/'RESULT.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('rows','direct_counts','residual')}))
if __name__=='__main__':run()
