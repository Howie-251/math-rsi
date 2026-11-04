"""Diagnostic positive Hall exclusions on the fourteen-hole cached residual."""
from pathlib import Path
from collections import deque
import json,hashlib,struct
R=Path(__file__).resolve().parent
cache={};reports=[];hashes={};witnesses=bytearray()
def solve(rec):
    H={0,*rec};L=[x for x in range(64) if x.bit_count()%2==0 and x not in H]
    W={x for x in range(64) if x.bit_count()%2 and x not in H};assert len(L)==len(W)==23
    adj={x:[x^(1<<d) for d in range(6) if x^(1<<d) in W] for x in L};left={};right={}
    def dfs(x,seen):
        for y in adj[x]:
            if y in seen:continue
            seen.add(y)
            if y not in right or dfs(right[y],seen):left[x]=y;right[y]=x;return True
        return False
    for x in L:dfs(x,set())
    if len(left)==23:return None
    S=set(L)-set(left);T=set();queue=deque(S)
    while queue:
        x=queue.popleft()
        for y in adj[x]:
            if y in T:continue
            T.add(y);assert y in right;z=right[y]
            if z not in S:S.add(z);queue.append(z)
    assert T=={y for x in S for y in adj[x]} and len(T)<len(S)
    return sum(1<<x for x in S),sum(1<<y for y in T)
for v in (1,7,31):
    for free in (False,True):
        name=f'EIGHTEEN_POST12_REUSE_remaining_h18_v{v}_{"free" if free else "covered"}.bin'
        raw=(R/name).read_bytes();assert len(raw)%17==0;hashes[name]=hashlib.sha256(raw).hexdigest();keep=bytearray();removed=0
        for idx in range(len(raw)//17):
            rec=raw[17*idx:17*(idx+1)]
            if rec not in cache:cache[rec]=solve(rec)
            hit=cache[rec]
            if hit is None:keep.extend(rec)
            else:removed+=1;witnesses.extend(struct.pack('<BBIQQ',v,int(free),idx,*hit))
        out=f'EIGHTEEN_POST12_HALL_remaining_v{v}_{"free" if free else "covered"}.bin';(R/out).write_bytes(keep)
        reports.append({'v':v,'free_target':free,'input':len(raw)//17,'explicit_Hall_exclusions':removed,'remaining':len(keep)//17});print(reports[-1],flush=True)
(R/'EIGHTEEN_POST12_HALL_witnesses.bin').write_bytes(witnesses)
(R/'EIGHTEEN_POST12_HALL_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY','reports':reports,'input_hashes':hashes,'witness_record_bytes':22,'full_eighteen_hole_proved':False,'full_P6_proved':False},indent=2)+'\n')
