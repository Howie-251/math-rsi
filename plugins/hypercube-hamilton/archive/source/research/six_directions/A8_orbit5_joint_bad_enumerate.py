"""Exact disjoint enumeration of matchings failing all four fixed templates.

The four-template classification is a proof input requiring independent audit.
No Hamilton or full-orbit conclusion is made by this enumeration alone.
"""
import itertools as it,json,functools,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
H={0,2,4,8,15,23,27,29};V=[x for x in range(32) if x not in H];idx={x:i for i,x in enumerate(V)}
cuts=[(2,{6,10},(3,18)),(4,{6,12},(5,20)),(8,{10,12},(9,24)),(16,{18,20,24},(16,17))]
all_edges=set(it.combinations(V,2));rules=[]
for bit,Y,ob in cuts:
    S=Y|set(ob);allow=set()
    for a,b in all_edges:
        if bool(a&bit)!=bool(b&bit):
            if (a if a&bit else b) not in S:continue
        elif a&bit and((a in Y and b not in S)or(b in Y and a not in S)):continue
        allow.add((a,b))
    assert len(allow)==164
    rules.append(allow)
reports=[];total=0;binary=R/'A8_orbit5_joint_bad_inputs.bin'
with binary.open('wb') as f:
    for mask in range(16):
        fixed=[cuts[i][2] for i in range(4) if mask>>i&1]
        endpoints=[x for e in fixed for x in e]
        reason=None
        if len(set(endpoints))!=len(endpoints):reason='fixed edges overlap'
        allowed=set(all_edges)
        for i in range(4):
            if not(mask>>i&1):allowed&=rules[i];allowed.discard(cuts[i][2])
        if any(e not in allowed for e in fixed):reason='fixed edge violates another nonfixed rule'
        if reason:
            reports.append({'fixed_mask':mask,'count':0,'reason':reason});continue
        residual=[x for x in V if x not in endpoints]
        adj=[0]*24
        for a,b in allowed:
            if a in residual and b in residual:adj[idx[a]]|=1<<idx[b];adj[idx[b]]|=1<<idx[a]
        initial=sum(1<<idx[x] for x in residual)
        def select(state):
            candidates=[i for i in range(24) if state>>i&1]
            return min(candidates,key=lambda i:(adj[i]&state).bit_count())
        @functools.lru_cache(None)
        def count(state):
            if not state:return 1
            i=select(state);tail=state^(1<<i);ys=adj[i]&tail;ans=0
            while ys:
                bit=ys&-ys;ys-=bit;ans+=count(tail^bit)
            return ans
        n=count(initial);offset=total
        assert n<20000000,(mask,n)
        def emit(state,pairs):
            if not state:
                es=sorted(tuple(sorted(e)) for e in fixed+pairs)
                assert len(es)==12 and sorted(x for e in es for x in e)==V
                # Disjoint branch membership is exact, including nonfixed absences.
                assert sum((int(cuts[i][2] in es)<<i) for i in range(4))==mask
                f.write(bytes(x for e in es for x in e));return
            i=select(state);tail=state^(1<<i);ys=adj[i]&tail
            while ys:
                bit=ys&-ys;ys-=bit;j=bit.bit_length()-1
                if count(tail^bit):emit(tail^bit,pairs+[(V[i],V[j])])
        emit(initial,[]);total+=n
        report={'fixed_mask':mask,'count':n,'offset_records':offset,'dp_states':count.cache_info().currsize,
                'required_edges':fixed,'residual_vertices':residual,'residual_edges':[[a,b] for a,b in sorted(allowed) if a in residual and b in residual]}
        reports.append(report);print(mask,n,'total',total,flush=True)
out={'scope':'Complete matchings failing four fixed templates, conditional on signature proof; no A8 closure',
     'holes':sorted(H),'forbidden':0,'input_bytes_per_record':24,'records':total,'branches':reports,
     'input_file':binary.name,'input_sha256':hashlib.sha256(binary.read_bytes()).hexdigest(),
     'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'full_a8_proved':False}
(R/'A8_orbit5_joint_bad_enumeration.json').write_text(json.dumps(out,indent=2)+'\n')
print('TOTAL',total)
