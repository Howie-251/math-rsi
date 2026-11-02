from array import array
import json
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
ROOT=BASE.parents[3]
OLD=ROOT/'research/ddp/more_graphs_20261027/d14_D5_mizuno_extension'
N=94186; K=3685; W=1472; ROWBYTES=8*W; FULL=(1<<N)-1

def dump(name,obj):
    (HERE/name).write_text(json.dumps(obj,indent=2)+'\n')

def load_context():
    assert sys.byteorder=='little'
    free=list(map(int,(BASE/'FREE_ORDER.txt').read_text().split()))
    records=[list(map(int,s.split())) for s in (BASE/'FREE_SPARES.txt').read_text().splitlines()]
    assert len(free)==K and [r[0] for r in records]==free
    spare=[r[1] for r in records]
    assert spare.count(1)==3670 and spare.count(2)==15
    raw3=(BASE/'allfree_R3.u64le.bin').read_bytes()
    raw4=(OLD/'allfree_cover_probe/allfree_R4.u64le.bin').read_bytes()
    assert len(raw3)==len(raw4)==K*ROWBYTES
    b3=[int.from_bytes(raw3[i:i+ROWBYTES],'little') for i in range(0,len(raw3),ROWBYTES)]
    b4=[int.from_bytes(raw4[i:i+ROWBYTES],'little') for i in range(0,len(raw4),ROWBYTES)]
    assert all(not (a&~b) and not (b>>N) and (a>>v)&1 for a,b,v in zip(b3,b4,free))
    p3=array('H');p3.frombytes((BASE/'target_R3_provider_counts.u16le.bin').read_bytes())
    p4=array('H');p4.frombytes((OLD/'allfree_cover_probe/target_support.u16le.bin').read_bytes())
    assert len(p3)==len(p4)==N
    legacy=json.loads((OLD/'RARE15_MISSING.json').read_text())
    if isinstance(legacy,dict):
        options=[v for v in legacy.values() if isinstance(v,list) and len(v)==9754]
        assert len(options)==1
        legacy=options[0]
    assert len(legacy)==9754 and len(set(legacy))==9754 and all(isinstance(t,int) and 0<=t<N for t in legacy)
    return dict(free=free,spare=spare,b3=b3,b4=b4,raw3=raw3,raw4=raw4,v3=memoryview(raw3).cast('Q'),v4=memoryview(raw4).cast('Q'),p3=p3,p4=p4,legacy=legacy,combined=[int(a)+int(b) for a,b in zip(p3,p4)])

def missing_labels(mask):
    result=[]
    while mask:
        bit=mask&-mask;result.append(bit.bit_length()-1);mask^=bit
    return result

def evaluate(ctx,A,B):
    assert len(A)==len(set(A))<=13 and len(B)==len(set(B))<=13
    assert all((j in A)+(j in B)<=ctx['spare'][j] for j in set(A)|set(B))
    r4=[0,0];r3=[0,0]
    for side,pins in enumerate([A,B]):
        for j in pins:r4[side]|=ctx['b4'][j];r3[side]|=ctx['b3'][j]
    return dict(own4=r4,own3=r3,missing=[FULL&~(r4[0]|r3[1]),FULL&~(r4[1]|r3[0])],single=[r4[0]==FULL,r4[1]==FULL])

def save_hit(ctx,A,B,ev,origin):
    parameters=dict(status='CACHED_PRODUCTION_COVER_HIT_PENDING_ROOT_ACCEPTANCE',source_graph='research/ddp/more_graphs_20261027/d14_D5_mizuno_extension/source94186.edges',source_n=N,source_m=657452,delta=14,D=5,origin=origin,A=[ctx['free'][j] for j in A],B=[ctx['free'][j] for j in B],source_allroot_BFS=0,new_graphs_exported=0)
    single_sides=[i for i in (0,1) if ev['single'][i]]
    if single_sides:
        side=single_sides[0];pins=[ctx['free'][j] for j in [A,B][side]]
        dump('SINGLE_HELPER_HIT.json',dict(parameters,chosen_side='AB'[side],pins=pins,new_n=N+1,new_m=657452+len(pins),new_degree=len(pins),complete_cached_R4=True))
    joint=not any(ev['missing'])
    if joint:
        dump('K2_HIT.json',dict(parameters,new_n=N+2,new_m=657453+len(A)+len(B),new_degrees=[len(A)+1,len(B)+1],complete_cached_two_root_cover=True))
    return bool(single_sides) or joint

def coverage_row(ctx,side,t):
    w,bit=divmod(t,64); result=[]
    for j in range(K):
        if ctx['v4'][j*W+w]>>bit&1:result.append(1+side*K+j)
        if ctx['v3'][j*W+w]>>bit&1:result.append(1+(1-side)*K+j)
    assert result
    return result
