"""P6 one-internal necessary inventory pilot, two- and three-higher-trace residuals, with the new two-small eight-mixed gate.

No exterior sets or original H are enumerated. Stop on the first inventory
not covered by the listed, dimension-correct existing signed-set gates.
"""
from collections import Counter
from itertools import combinations,combinations_with_replacement,permutations
from pathlib import Path
import json,time

HERE=Path(__file__).resolve().parent
START=time.process_time()
PAIRS=tuple(combinations(range(6),2))
C=frozenset(range(5));a=5

def gate(m4,m3,t,b):
    if m4+m3==8 and m3<=2 and t==0 and b<=20:return 'new_eight_mixed_two_small_L18'
    if m3==0 and m4<=11 and t==0 and b<=17:return 'eleven_four_L18_zero_T'
    if m4==8 and m3==0 and t<=2 and b<=18:return 'new_eight_four_L18_two_T'
    if m4==7 and m3==1 and t==0 and b<=20:return 'eight_mixed_L18'
    if m4==8 and m3==0 and t<=1 and b<=19:return 'eight_four_L18_one_T'
    if m4+m3==0:return 'empty'
    if m4+m3<=7 and m3<=2 and t<=1:return 'seven_mixed_two_small_one_T'
    if m4+m3<=7 and m3<=4 and t==0:return 'seven_mixed_four_small_zero_T'
    if m4+m3<=4 and t<=3:return 'four_small_3T'
    if m4+m3<=5 and t<=2:return 'five_small_2T'
    if m3==0:
        if m4<=5 and t<=10 and b<=32:return 'five_four_10T'
        if m4<=6 and t<=6 and b<=35:return 'six_four_6T'
        if m4<=7 and t<=4 and b<=35:return 'seven_four_4T35B'
        if m4<=10 and t==0 and b<=27:return 'ten_four_zero_T'
    # Deliberately do not apply either L<=17 eight-positive theorem.
    return None

def J_domain(n):
    rows=[]
    for indices in combinations_with_replacement(range(15),n):
        g=[0]*15;d=[0]*6;mask=0
        for k in indices:
            g[k]+=1;mask|=1<<k
            u,v=PAIRS[k];d[u]+=1;d[v]+=1
        rows.append((tuple(g),tuple(d),mask))
    return rows

graphs={n:J_domain(n) for n in (3,4,5,6)}
rows=[];failure=None;timed_out=False
for inventory in [(6,2,0),(5,1,1),(4,3,0),(3,2,1)]:
    n2,n3,n4=inventory;n1=24+n3+2*n4
    for nine in (0,5):
        degree=[8+int(v==nine) for v in range(6)]
        ci=[1]*5+[0]
        automorphisms=[]
        for perm in permutations(range(5)):
            p=tuple(perm)+(5,)
            if p[nine]==nine:automorphisms.append(p)
        triples=list(combinations(range(6),3));quads=list(combinations(range(6),4))
        # Repeated higher traces are permitted: different H edges may have
        # the same P trace. Keep only the residual with no C point common
        # to all higher traces. For exactly two this is intersection subset{a}.
        high_families=(tuple(ts)+tuple(qs)
                       for ts in combinations_with_replacement(triples,n3)
                       for qs in combinations_with_replacement(quads,n4))
        actual_pairs=[]
        for ts in high_families:
            common=set(C)
            for t in ts:common &= set(t)
            if not common:actual_pairs.append(tuple(sorted(ts)))
        def image(T,p):return tuple(sorted(tuple(sorted(p[v] for v in t)) for t in T))
        representatives=sorted({min(image(T,p) for p in automorphisms) for T in actual_pairs})
        for T in representatives:
            h=[sum(v in t for t in T) for v in range(6)]
            w=[sum(len(t)-1 for t in T if v in t) for v in range(6)]
            cap=[min(degree[v]-ci[v]-h[v],4*degree[v]-18-4*ci[v]-w[v]) for v in range(6)]
            required=0
            for k,(i,j) in enumerate(PAIRS):
                if not ({i,j}<=C or any(i in t and j in t for t in T)):required|=1<<k
            eligible=[(k,i,j) for k,(i,j) in enumerate(PAIRS)
                      if (i in C or j in C) and all(i in t or j in t for t in T)]
            count=Counter();legal=0
            for g,d,mask in graphs[n2]:
                if mask&required != required or any(x>y for x,y in zip(d,cap)):continue
                legal+=1
                singles=[degree[v]-ci[v]-h[v]-d[v] for v in range(6)]
                accepted=False
                signatures=[]
                # Try every proper-C blue pair, not only those hitting the
                # higher traces. All-red higher traces remain negative1/2.
                def signature(selected):
                    selected=set(selected)
                    pos=Counter();neg=Counter()
                    traces=[tuple(C)]+[tt for tt in T]
                    traces += [PAIRS[k] for k,v in enumerate(g) for _ in range(v)]
                    traces += [(v,) for v in range(6) for _ in range(singles[v])]
                    assert len(traces)==35
                    for tr in traces:
                        st=set(tr)
                        if st & selected and st-selected:continue
                        (pos if st<=selected else neg)[5-len(st)]+=1
                    assert pos[0]==neg[0]==0
                    m4,m3,m2=pos[4],pos[3],pos[2]
                    t,b=neg[3],neg[4]
                    which=None
                    if not (pos[1] or neg[1] or neg[2]):
                        if m2:
                            which=('four_small_3T' if m4+m3+m2<=4 and t<=3 else
                                   'five_small_2T' if m4+m3+m2<=5 and m2<=3 and t<=2 else None)
                        else:which=gate(m4,m3,t,b)
                    return {'blue':sorted(selected),'m4':m4,'m3':m3,'m2':m2,'m1':pos[1],
                            'negative1':neg[1],'negative2':neg[2],'T':t,'B':b,'gate':which}
                for selected in combinations(range(6),2):
                    if not set(selected)&C:continue
                    sig=signature(selected);signatures.append(sig)
                    if sig['gate']:
                        count[sig['gate']]+=1;accepted=True;break
                if not accepted:
                    triple_signatures=[]
                    for selected in combinations(range(6),3):
                        if not set(selected)&C:continue
                        sig=signature(selected);triple_signatures.append(sig)
                        if sig['gate']:
                            count['three_blue:'+sig['gate']]+=1;accepted=True;break
                    if accepted:continue
                    failure={'inventory':inventory,'nine_degree_point':nine,'C':sorted(C),'a':a,
                             'higher_traces':T,'degrees':degree,'ci':ci,'hi':h,'J_degrees':d,
                             'singleton_counts':singles,'n1':n1,
                             'J':[{ 'pair':PAIRS[k],'multiplicity':v} for k,v in enumerate(g) if v],
                             'all_proper_C_blue_pair_signatures':signatures,
                             'all_proper_C_three_blue_signatures':triple_signatures,
                             'P_L_realizability':'Not determined; only necessary P inventory tested. No exterior blocks or whole H searched.'}
                    break
            rows.append({'inventory':inventory,'nine_degree_point':nine,'higher_traces':T,
                         'high_orbits_for_this_inventory_and_nine':len(representatives),
                         'high_orbit_finished':failure is None,'necessary_J_checked':legal,
                         'successful_gate_counts':dict(count)})
            if failure:break
            if time.process_time()-START>120:timed_out=True;break
        if failure or timed_out:break
    if failure or timed_out:break

out={'scope':__doc__,'exact_inventories_attempted':[(6,2,0),(5,1,1),(4,3,0),(3,2,1)],
     'read_new_zero_T_four_small_extension':True,
     'used_L17_eight_positive_gate':False,'used_L18_eight_positive_one_T_gate':True,
     'used_exact_L18_eight_mixed_gate':True,
     'eleven_four_zero_T_source':'proofs/propertyb35/ELEVEN_POSITIVE_FOUR_SET_REPAIR.md',
     'attempted_all_proper_C_three_blue_subsets_after_pair_failure':True,
     'all_red_higher_traces_retained_as_negative1_or_negative2':True,
     'new_eight_two_triples_source':'proofs/propertyb35/EIGHT_POSITIVE_18_TWO_TRIPLES.md',
     'new_eight_mixed_two_small_source':'proofs/propertyb35/EIGHT_MIXED_TWO_SMALL_EIGHTEEN_REPAIR.md',
     'higher_trace_multisets_allow_repetition':True,
     'higher_trace_filter':'common intersection with C empty; equivalent to T1 intersection T2 subset {a} for two higher traces',
     'added_gate_sources':['proofs/propertyb35/EIGHT_MIXED_POSITIVE_EIGHTEEN_REPAIR.md','proofs/propertyb35/EIGHT_POSITIVE_18_ONE_TRIPLE.md'],
     'raw_J_multisets':{str(n):len(g) for n,g in graphs.items()},
     'rows':rows,'first_nongated':failure,'timed_out':timed_out,
     'status':'FIRST_NONGATED_NECESSARY_P_INVENTORY' if failure else 'PROFILE_COMPLETE',
     'cpu_seconds':time.process_time()-START}
(HERE/'RUN.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=2))
