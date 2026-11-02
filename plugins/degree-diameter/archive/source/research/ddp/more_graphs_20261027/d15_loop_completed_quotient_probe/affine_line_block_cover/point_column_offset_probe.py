"""Exactly two fixed old-ball line columns per actual source."""
from pathlib import Path
import json
import resource
import struct
import time

resource.setrlimit(resource.RLIMIT_CPU,(2,2))
START=time.process_time()
P=Path(__file__).resolve().parent
BASE=P.parent.parent
pred=json.loads((P/'POINT_COLUMN_OFFSET_PREDICTION.json').read_text())
assert pred['frozen_before_fixed_point_column_OR_comparison']
assert not (P/'POINT_COLUMN_OFFSET_RESULT.json').exists()

def encode(v):
    return sum(x*3**i for i,x in enumerate(v))

def selected_balls(n,wanted):
    wanted=set(wanted)
    balls={}
    full=(1<<n)-1
    if n==15552:
        path=BASE/'d15_D4_current15552/single_vertex_R3_cover/R3_MASKS.bin'
        with path.open('rb') as f:
            count,stored_n,words=struct.unpack('<III',f.read(12))
            assert (count,stored_n,words)==(648,n,243)
            for _ in range(count):
                pin=struct.unpack('<I',f.read(4))[0]
                if pin in wanted:
                    balls[pin]=int.from_bytes(f.read(8*words),'little')&full
                else:
                    f.seek(8*words,1)
    else:
        folder=BASE/'d15_D5_current102060_source/monotone_R4_cover'
        eligible=list(map(int,(folder/'eligible.txt').read_text().split()))
        index={pin:i for i,pin in enumerate(eligible)}
        assert wanted<=set(index)
        with (folder/'radius4.u64le.bin').open('rb') as f:
            for pin in sorted(wanted):
                f.seek(index[pin]*1595*8)
                data=f.read(1595*8)
                assert len(data)==1595*8
                balls[pin]=int.from_bytes(data,'little')&full
    assert set(balls)==wanted
    return balls

def union(pins,balls):
    mask=0
    for pin in pins:
        mask|=balls[pin]
    return mask

def fullblocks(mask,n,q):
    whole=(1<<q)-1
    blocks=0
    for controller in range(n//q):
        if (mask>>(controller*q))&whole==whole:
            blocks|=1<<controller
    return blocks

results=[]
for spec in pred['sources']:
    n,q=spec['n'],spec['bin_size']
    v,p=spec['v0'],spec['p']
    L0=sorted(encode([(t*x)%3 for x in v]) for t in range(3))
    Lp=sorted(encode([(p[i]+t*v[i])%3 for i in range(len(v))]) for t in range(3))
    assert len(set(L0+Lp))==6
    balls=selected_balls(n,L0+Lp)
    old,new=union(L0,balls),union(Lp,balls)
    xor=old^new
    oldblock,newblock=fullblocks(old,n,q),fullblocks(new,n,q)
    first=(xor&-xor).bit_length()-1 if xor else None
    local=None
    if first is not None:
        controller=first//q
        whole=(1<<q)-1
        oldlocal=(old>>(controller*q))&whole
        newlocal=(new>>(controller*q))&whole
        intersection=oldlocal&newlocal
        total=oldlocal|newlocal
        local={'controller':controller,'first_differing_local_offset':first%q,
               'L0_mask_decimal':str(oldlocal),'Lp_mask_decimal':str(newlocal),
               'L0_size':oldlocal.bit_count(),'Lp_size':newlocal.bit_count(),
               'intersection_mask_decimal':str(intersection),'intersection_size':intersection.bit_count(),
               'union_mask_decimal':str(total),'union_size':total.bit_count(),
               'L0_contains_first_target':bool((old>>first)&1),
               'Lp_contains_first_target':bool((new>>first)&1)}
    results.append({**spec,'L0_pins':L0,'Lp_pins':Lp,'cached_balls_read':6,
                    'fullfiber_blockmasks_equal':oldblock==newblock,
                    'L0_fullfiber_mask_decimal':str(oldblock),'Lp_fullfiber_mask_decimal':str(newblock),
                    'fullfiber_columns_size':oldblock.bit_count(),
                    'point_columns_equal':not xor,'point_XOR_nonzero':bool(xor),
                    'point_XOR_size':xor.bit_count(),'L0_total_point_coverage':old.bit_count(),
                    'Lp_total_point_coverage':new.bit_count(),
                    'first_differing_target':first,'first_differing_fiber':local,
                    'prediction_status':'SUPPORTED' if oldblock==newblock and xor else 'REFUTED_FIXED_COMPARISON'})
result={'status':'COMPLETE_FIXED_POINT_COLUMN_OFFSET_COMPARISON','sources':results,
        'CPU_seconds':time.process_time()-START,'new_balls':0,'BFS':0,'solver_calls':0,'new_graphs':0,
        'scope':'Exactly the two frozen parallel lines per source; no changed p,direction or search. Unequal point columns do not by themselves certify a <=5-line or <=15-pin cover.'}
(P/'POINT_COLUMN_OFFSET_RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
