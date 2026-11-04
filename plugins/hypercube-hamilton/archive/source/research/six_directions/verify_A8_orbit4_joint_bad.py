"""No-search verification of all orbit-four exceptions and positive cycles.

Regenerates the disjoint graph matching domains without importing the producer,
uses reversed vertex order and no memoized counting, and checks every cycle.
"""
import itertools as it,json,hashlib,time
from pathlib import Path
R=Path(__file__).resolve().parent
H={0,1,2,4,15,23,27,29};V=set(range(32))-H
CUTS=[(2,{3,6},(10,18)),(4,{5,6},(12,20)),(8,{9,10,12},(8,24)),(16,{17,18,20},(16,24))]
def encode(edges):return bytes(x for e in sorted(tuple(sorted(e)) for e in edges) for x in e)
def forbidden_for(edge,bit,Y,ob):
    a,b=edge;B=[x for x in edge if x&bit];S=Y|set(ob)
    if len(B)==1:return B[0] not in S
    if len(B)==2:return (a in Y and b not in S)or(b in Y and a not in S)
    return False
raw=(R/'A8_orbit4_joint_bad_inputs.bin').read_bytes()
assert len(raw)%24==0
domain={raw[i:i+24] for i in range(0,len(raw),24)}
assert len(domain)*24==len(raw)
counts=[];odd_witnesses=[]
for state in range(16):
    must=[ob for j,(_,_,ob) in enumerate(CUTS) if state&(1<<j)]
    covered=[x for e in must for x in e]
    if len(set(covered))!=len(covered):counts.append(0);continue
    remaining=V-set(covered)
    def allowed(edge):
        for j,(bit,Y,ob) in enumerate(CUTS):
            if not(state>>j&1) and(edge==ob or forbidden_for(edge,bit,Y,ob)):return False
        return True
    if not all(allowed(e) for e in must):counts.append(0);continue
    graph={x:set() for x in remaining}
    for x,y in it.combinations(sorted(remaining),2):
        if allowed((x,y)):graph[x].add(y);graph[y].add(x)
    # A separately checkable reason for every empty nonconflicting branch.
    unseen=set(remaining);odd=[]
    while unseen:
        reach={min(unseen)};front=list(reach)
        while front:
            x=front.pop()
            for y in graph[x]-reach:reach.add(y);front.append(y)
        unseen-=reach
        if len(reach)%2:odd.append(sorted(reach))
    n=[0]
    def gen(left,edges):
        if not left:
            rec=encode(must+edges)
            assert rec in domain,('missing/duplicate generated input',state,list(rec))
            domain.remove(rec);n[0]+=1;return
        x=max(left)
        for y in sorted(graph[x]&left,reverse=True):gen(left-{x,y},edges+[(x,y)])
    if not odd:gen(set(remaining),[])
    counts.append(n[0]);odd_witnesses.append({'fixed_mask':state,'odd_components':odd})
assert not domain and counts==[0,0,0,2025,0,0,0,99225,0,0,0,99225,0,0,0,0],counts
cert=(R/'A8_orbit4_joint_bad_certificates.bin').read_bytes()
assert len(cert)//55==len(raw)//24 and len(cert)%55==0
for i in range(len(raw)//24):
    rec=cert[55*i:55*i+55];assert rec[:24]==raw[24*i:24*i+24]
    pairs={frozenset(rec[j:j+2]) for j in range(0,24,2)}
    assert len(pairs)==12 and set(rec[:24])==V and len(set(rec[:24]))==24
    cyc=list(rec[24:]);assert len(cyc)==31 and set(cyc)==set(range(1,32))
    edges={frozenset((cyc[j],cyc[(j+1)%31])) for j in range(31)}
    assert len(edges)==31 and pairs<=edges
    for edge in edges-pairs:
        x,y=tuple(edge);assert (x^y).bit_count()==1
files=['A8_orbit4_joint_bad_inputs.bin','A8_orbit4_joint_bad_certificates.bin','verify_A8_orbit4_joint_bad.py']
out={'status':'PASS','independent_domain_enumeration':True,'producer_imported':False,
     'scope':'200475 exact joint-bad matching inputs and all corresponding positive31cycles; semantic bridge coverage requires review',
     'counts_by_fixed_mask':counts,'matching_count':len(raw)//24,'positive_cycles':len(cert)//55,
     'odd_component_certificates':odd_witnesses,
     'hashes':{x:hashlib.sha256((R/x).read_bytes()).hexdigest() for x in files},'full_a8_proved':False}
(R/'A8_orbit4_joint_bad_verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['odd_component_certificates','hashes']}))
