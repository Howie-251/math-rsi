from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parent
holes={0,1};targets={14,22,26};F=[(x,x^1) for x in range(2,32,2)];mate={}
for x,y in F:mate[x]=y;mate[y]=x
assert len(mate)==30 and set(mate)==set(range(32))-holes
assert all(t in mate and not(t&1) for t in targets)
remaining_cross=[(x,x^1) for x in range(0,32,2) if x!=0]
assert F==remaining_cross and len(F)%2==1
data=(R/'Q5_THREE_TARGET_CORE85_pairs.bin').read_bytes();assert len(data)%30==0
connected=0
for i in range(0,len(data),30):
    row=data[i:i+30];other={}
    for j in range(0,30,2):a,b=row[j:j+2];other[a]=b;other[b]=a
    assert set(other)==set(mate)
    start=min(mate);x=start
    for n in range(1,16):
        x=other[mate[x]]
        if x==start:
            if n==15:connected+=1
            break
assert connected==0
out=dict(verdict='EXPLICIT_COUNTEREXAMPLE_TO_THREE_TARGET_LOCAL_CLAIM',dimension=5,holes=sorted(holes),omitted=0,
         allowed_endpoints=sorted(targets),matching=[list(e) for e in F],cross_direction=0,
         prescribed_cross_edges=15,available_cross_edges=15,all_allowed_endpoints_on_side=0,
         obstruction='Every path containing all matching edges crosses coordinate0 exactly15 times, so its endpoints have different bit0; every allowed endpoint has bit0=0.',
         selected_forest_rows_checked=len(data)//30,compatible_selected_forests=connected,
         producer_rank=json.loads((R/'Q5_THREE_TARGET_CORE85.json').read_text())['rank_GF2'],
         affects_full_Q6_T15_or_P7=False,
         sha256={'Q5_THREE_TARGET_CORE85_pairs.bin':hashlib.sha256(data).hexdigest()})
(R/'Q5_THREE_TARGET_LAYER_COUNTEREXAMPLE.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ('matching','sha256')}))
