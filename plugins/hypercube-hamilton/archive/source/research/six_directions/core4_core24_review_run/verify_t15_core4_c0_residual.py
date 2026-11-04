from pathlib import Path
import json,hashlib,collections
p=Path(__file__).parent
I=(p/'t15_core4_fourbridge_c0_residual_inputs.bin').read_bytes();W=(p/'t15_core4_c0_residual.bin').read_bytes()
assert len(I)%26==len(W)%56==0 and len(I)//26==len(W)//56
byA=collections.defaultdict(set)
for k in range(len(I)//26):
 r=I[26*k:26*k+26];w=W[56*k:56*k+56];assert w[:26]==r
 cyc=list(w[26:]);assert len(set(cyc))==30 and set(cyc)==set(range(32))-{1,2}
 req={tuple(sorted(r[j:j+2])) for j in range(0,26,2)};assert len(req)==13
 assert len({v for e in req for v in e})==26 and set(range(32))-{v for e in req for v in e}=={0,1,2,7,11,31}
 E={tuple(sorted((cyc[j],cyc[(j+1)%30]))) for j in range(30)}
 assert req<=E and all((a^b).bit_count()==1 for a,b in E-req)
 byA[r[:14]].add(r[14:])
H=collections.Counter(map(len,byA.values()))
A07=[(a,b) for a,b in byA.items() if bytes((4,11)) in [a[j:j+2] for j in range(0,14,2)]]
# lift(local0,one)=4, lift(local7,one)=15, not11.
A07=[(a,b) for a,b in byA.items() if bytes((4,15)) in [a[j:j+2] for j in range(0,14,2)]]
assert len(A07)==10395 and len({frozenset(b) for a,b in A07})==1
out={'certificates':len(I)//26,'checked':True,'residual_A':len(byA),'B_count_per_A_histogram':dict(H),'A_with_edge_4_15':len(A07),'shared_B_family_size':len(A07[0][1]),'input_sha256':hashlib.sha256(I).hexdigest(),'witness_sha256':hashlib.sha256(W).hexdigest()}
(p/'t15_core4_c0_residual_verification.json').write_text(json.dumps(out,indent=2));print(out)
