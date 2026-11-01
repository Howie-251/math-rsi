"""Complete necessary P-side census; no exterior incidence or H enumeration.

C=01234,a=5; one9/five8; inventories (6,2,0),(5,1,1),(4,3,0),(3,2,1).
Remove only the separately closed case with a C point common to all high traces.
"""
from collections import Counter
from itertools import combinations,combinations_with_replacement,permutations
from pathlib import Path
import json,time,argparse
HERE=Path(__file__).resolve().parent
P=tuple(range(6));C=frozenset(range(5));a=5
PAIRS=tuple(combinations(P,2));PAIRIDX={e:k for k,e in enumerate(PAIRS)}
SELECTIONS=tuple(combinations(P,2))+tuple(combinations(P,3))
INVENTORIES=((6,2,0),(5,1,1),(4,3,0),(3,2,1))

def accept(sig):
    p4,p3,p2,p1,n1,n2,t,b,ulb=sig
    m=p4+p3+p2+p1
    if p1 or n1:return None
    if m==0:return 'empty'
    if n2:
        if p3 or p2:return None
        if p4==5 and ulb>=17 and n2<=4 and t<=1 and b<=22:return 'five_sparse_4N2'
        if p4==4 and ulb>=14 and n2<=4 and t==0 and b<=23:return 'four_sparse_4N2'
        if p4==5 and ulb>=17 and n2<=3 and t<=3 and b<=21:return 'five_sparse_3N2'
        if p4==4 and ulb>=14 and n2<=3 and t<=2 and b<=22:return 'four_sparse_3N2'
        if p4==3 and ulb>=11 and n2<=3 and t<=1 and b<=23:return 'three_sparse_3N2'
        if p4==2 and ulb>=8 and n2<=3:return 'two_disjoint_3N2'
        return None
    if m<=4 and t<=3:return 'four_small_3T'
    if m<=5 and t<=1:return 'five_small_1T'
    if m<=5 and p2<=3 and t<=2:return 'five_small_2T'
    if p2:return None
    if m<=7 and p3<=2 and t<=1:return 'seven_mixed_2small_1T'
    if m<=7 and p3<=4 and t==0:return 'seven_mixed_4small_0T'
    if m==8 and p3<=2 and t==0 and b<=20:return 'eight_mixed_2small_L18'
    if p3:return None
    if p4<=5 and ((t<=10 and b<=32) or t+b<=35):return 'five_four_35negative'
    if p4<=6 and t<=6 and b<=35:return 'six_four_6T'
    if p4<=6 and ulb>=14 and t<=8 and b<=20:return 'six_four_large_union'
    if p4<=7 and t<=4 and b<=35:return 'seven_four_4T'
    if p4<=10 and t==0 and b<=27:return 'ten_four_0T'
    if p4<=11 and t==0 and b<=17:return 'eleven_four_L18'
    if p4==8 and t<=2 and b<=18:return 'eight_four_2T_L18'
    if p4==8 and t<=1 and b<=19:return 'eight_four_1T_L18'
    return None

def graphs(n):
    out=[]
    for idx in combinations_with_replacement(range(15),n):
        g=[0]*15;d=[0]*6;support=0
        for k in idx:
            g[k]+=1;support|=1<<k;i,j=PAIRS[k];d[i]+=1;d[j]+=1
        out.append((tuple(g),tuple(d),support))
    return out

def higher_reps(n3,n4,nine):
    perms=tuple(tuple(p)+(5,) for p in permutations(range(5)) if (tuple(p)+(5,))[nine]==nine)
    families=[]
    for ts in combinations_with_replacement(tuple(combinations(P,3)),n3):
        for qs in combinations_with_replacement(tuple(combinations(P,4)),n4):
            T=tuple(sorted(ts+qs));common=set(C)
            for t in T:common.intersection_update(t)
            if not common:families.append(T)
    def image(T,p):return tuple(sorted(tuple(sorted(p[i] for i in t)) for t in T))
    reps=sorted({min(image(T,p) for p in perms) for T in families})
    return [(T,len({image(T,p) for p in perms})) for T in reps],len(families)

def selection_data(T):
    out=[]
    for blue in SELECTIONS:
        S=set(blue);pm2=pm1=nm2=nm1=0
        for tr in T:
            st=set(tr)
            if st<=S:
                if len(st)==3:pm2+=1
                else:pm1+=1
            elif not st&S:
                if len(st)==3:nm2+=1
                else:nm1+=1
        inside=tuple(k for k,e in enumerate(PAIRS) if set(e)<=S)
        outside=tuple(k for k,e in enumerate(PAIRS) if not set(e)&S)
        out.append((blue,pm2,pm1,nm2,nm1,inside,outside))
    return out

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--cpu-limit',type=float,default=120)
    ap.add_argument('--prefix',default='CENSUS');args=ap.parse_args()
    start=time.process_time();domains={n:graphs(n) for n in (3,4,5,6)}
    rows=[];passed=Counter();menus=[];menu_ids={};menu_counts=Counter();ng=total=0;timeout=False
    keys=(HERE/(args.prefix+'_NONGATED.jsonl')).open('w')
    accepted_keys=(HERE/(args.prefix+'_PASSED.jsonl')).open('w')
    stop=None
    for inv in INVENTORIES:
      n2,n3,n4=inv;n1=24+n3+2*n4
      for nine in (0,5):
        deg=tuple(8+int(v==nine) for v in P);ci=(1,1,1,1,1,0)
        reps,labelled_high=higher_reps(n3,n4,nine)
        for ri,(T,orbsize) in enumerate(reps):
            h=tuple(sum(v in t for t in T) for v in P)
            w=tuple(sum(len(t)-1 for t in T if v in t) for v in P)
            cap=tuple(min(deg[v]-ci[v]-h[v],4*deg[v]-18-4*ci[v]-w[v]) for v in P)
            required=sum(1<<k for k,(i,j) in enumerate(PAIRS) if not ({i,j}<=C or any(i in t and j in t for t in T)))
            sd=selection_data(T);rowpass=Counter();legal=rowng=0;examined=0
            for gi,(g,d,support) in enumerate(domains[n2]):
                examined+=1
                if support&required!=required or any(x>y for x,y in zip(d,cap)):continue
                legal+=1;total+=1
                u=tuple(deg[v]-ci[v]-h[v]-d[v] for v in P)
                # Every q-singleton exterior4 is positive if q is blue. All
                # other edges through q cover at most 3*dJ(q)+sum(5-|T|)
                # exterior points. Actual q/L pair coverage therefore gives
                # this safe lower bound on their union.
                per_union=tuple(max(0,18-3*d[v]-sum(5-len(t) for t in T if v in t)) for v in P)
                failed=[];ok=None;blue_used=None
                for blue,p2,p1,n2small,n1small,ins,outs in sd:
                    p4=sum(u[v] for v in blue);p3=sum(g[k] for k in ins)
                    t=sum(g[k] for k in outs);b=n1-p4
                    ulb=max(per_union[v] for v in blue)
                    sig=(p4,p3,p2,p1,n1small,n2small,t,b,ulb)
                    tag=accept(sig)
                    if tag:ok=tag;blue_used=blue;break
                    failed.append((blue,sig))
                if ok:
                    passed[ok]+=1;rowpass[ok]+=1
                    accepted_keys.write(json.dumps({'inventory':inv,'nine':nine,'higher':T,'J':g,'blue':blue_used,'signature':sig,'gate':ok},separators=(',',':'))+'\n')
                else:
                    ng+=1;rowng+=1
                    # Full menu is retained: at most35 signatures, deduped
                    # only when the exact size counts and guaranteed union
                    # lower bound coincide. First blue label is a witness.
                    sm={}
                    for blue,sig in failed:sm.setdefault(sig,blue)
                    menu=tuple(sorted(sm))
                    if menu not in menu_ids:
                        menu_ids[menu]=len(menus)
                        menus.append({'id':len(menus),'signatures':[{'counts':s,'one_blue_for_first_member':sm[s]} for s in menu]})
                    mid=menu_ids[menu];menu_counts[mid]+=1
                    keys.write(json.dumps({'inventory':inv,'nine':nine,'higher':T,'J':g,'menu_id':mid},separators=(',',':'))+'\n')
                if total%2000==0 and time.process_time()-start>args.cpu_limit:
                    timeout=True;stop={'inventory':inv,'nine':nine,'higher_orbit_index':ri,'J_raw_index':gi,'higher':T};break
            rows.append({'inventory':inv,'nine':nine,'higher':T,'high_orbit_size':orbsize,
                         'high_orbits_in_cell':len(reps),'labelled_high_families_in_cell':labelled_high,
                         'orbit_finished':not timeout,'raw_J_examined':examined,
                         'necessary':legal,'nongated':rowng,'passed':dict(rowpass)})
            if timeout:break
        if timeout:break
      if timeout:break
    keys.close();accepted_keys.close()
    for m in menus:m['necessary_count']=menu_counts[m['id']]
    out={'status':'BUDGET_PREFIX' if timeout else 'COMPLETE_NECESSARY_P_CENSUS',
         'scope':__doc__,'cpu_seconds':time.process_time()-start,'cpu_limit':args.cpu_limit,
         'inventories':INVENTORIES,'raw_J_counts':{n:len(d) for n,d in domains.items()},
         'signature_order':['P4','P3','P2','P1','N1','N2','N3','N4','guaranteed_positive_union_lower_bound'],
         'catalog':'proofs/propertyb35/REPAIR_GATE_CATALOG.md',
         'geometry_gates_only_when_union_bound_proved':True,
         'proper_C_blue_pairs_then_triples':True,'all_unresolved_source_signs_retained':True,
         'total_necessary':total,'passed':sum(passed.values()),'passed_by_gate':dict(passed),
         'nongated':ng,'nongated_menu_classes':len(menus),'menus':menus,'rows':rows,'stop_position':stop,
         'PL_realizability':'Necessary aggregate P/L capacities only. No actual exterior incidence realization or H asserted.'}
    assert total==sum(passed.values())+ng and ng==sum(menu_counts.values())
    (HERE/(args.prefix+'.json')).write_text(json.dumps(out,separators=(',',':'))+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('rows','menus')},indent=2))
if __name__=='__main__':main()
