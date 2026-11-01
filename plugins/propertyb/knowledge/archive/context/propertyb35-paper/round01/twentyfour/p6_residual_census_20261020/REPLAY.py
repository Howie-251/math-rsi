"""Rebuild each actual-index P trace, independent of selector count formulas."""
import json,time
from pathlib import Path
from itertools import combinations
from collections import Counter
HERE=Path(__file__).resolve().parent
P=tuple(range(6));PAIRS=tuple(combinations(P,2));C=31
START=time.process_time();j=json.loads((HERE/'CENSUS.json').read_text())
seen=set();passes=Counter();ng=0;direct_choices=0;menu_count=Counter();first_menu_checked=set()

def reconstruct(r):
    inv=r['inventory'];nine=r['nine'];T=r['higher'];g=r['J']
    deg=[8+int(v==nine) for v in P];ci=[1]*5+[0]
    h=[sum(v in t for t in T) for v in P]
    s=[sum(g[k] for k,e in enumerate(PAIRS) if v in e) for v in P]
    u=[deg[v]-ci[v]-h[v]-s[v] for v in P]
    assert sum(g)==inv[0] and sum(len(t)==3 for t in T)==inv[1] and sum(len(t)==4 for t in T)==inv[2]
    assert min(u)>=0
    assert all(s[v]+sum(len(t)-1 for t in T if v in t)<=4*deg[v]-18-4*ci[v] for v in P)
    assert all(set(e)<=set(range(5)) or any(set(e)<=set(t) for t in T) or g[k]>0 for k,e in enumerate(PAIRS))
    common=set(range(5))
    for t in T:common&=set(t)
    assert not common
    traces=[C]+[sum(1<<v for v in t) for t in T]
    traces += [sum(1<<v for v in e) for k,e in enumerate(PAIRS) for _ in range(g[k])]
    traces += [1<<v for v in P for _ in range(u[v])]
    assert len(traces)==35
    key=(tuple(inv),nine,tuple(map(tuple,T)),tuple(g));assert key not in seen;seen.add(key)
    def classify(blue):
        mask=sum(1<<v for v in blue);pos=Counter();neg=Counter()
        assert C&mask and C&~mask
        for tr in traces:
            if tr&mask and tr&~mask:continue
            (pos if tr&~mask==0 else neg)[5-tr.bit_count()]+=1
        ulb=max(max(0,18-3*s[v]-sum(5-len(t) for t in T if v in t)) for v in blue)
        return (pos[4],pos[3],pos[2],pos[1],neg[1],neg[2],neg[3],neg[4],ulb)
    return classify

def valid_tag(tag,s):
    p4,p3,p2,p1,n1,n2,t,b,_=s
    assert not(p2 or p1 or n1 or n2)
    if tag=='eight_mixed_2small_L18':return p4+p3==8 and p3<=2 and t==0 and b<=20
    if tag=='eight_four_2T_L18':return p4==8 and p3==0 and t<=2 and b<=18
    if tag=='seven_mixed_2small_1T':return p4+p3<=7 and p3<=2 and t<=1
    if tag=='seven_mixed_4small_0T':return p4+p3<=7 and p3<=4 and t==0
    if tag=='eight_four_1T_L18':return p4==8 and p3==0 and t<=1 and b<=19
    if tag=='ten_four_0T':return p4<=10 and p3==0 and t==0 and b<=27
    raise AssertionError(tag)

for line in (HERE/'CENSUS_PASSED.jsonl').open():
    r=json.loads(line);classify=reconstruct(r);sig=classify(r['blue']);direct_choices+=1
    assert sig==tuple(r['signature']) and valid_tag(r['gate'],sig)
    passes[r['gate']]+=1
for line in (HERE/'CENSUS_NONGATED.jsonl').open():
    r=json.loads(line);classify=reconstruct(r);ss=set()
    for k in (2,3):
        for blue in combinations(P,k):ss.add(classify(blue));direct_choices+=1
    menu=j['menus'][r['menu_id']]
    assert ss=={tuple(s['counts']) for s in menu['signatures']}
    if r['menu_id'] not in first_menu_checked:
        assert all(classify(s['one_blue_for_first_member'])==tuple(s['counts']) for s in menu['signatures'])
        first_menu_checked.add(r['menu_id'])
    ng+=1;menu_count[r['menu_id']]+=1
assert passes==j['passed_by_gate'] and ng==j['nongated']
assert len(seen)==j['total_necessary']==123621
assert all(menu_count[m['id']]==m['necessary_count'] for m in j['menus'])
out={'status':'PASS','unique_P_inputs':len(seen),'passed_tag_checks':sum(passes.values()),
     'nongated_full_menus_replayed':ng,'source_index_colourings_rebuilt':direct_choices,
     'independent_scope':'Actual trace expansion, signatures, six used gate parameters and record cardinalities; not a second orbit/domain generator.',
     'cpu_seconds':time.process_time()-START}
(HERE/'REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print(out)
