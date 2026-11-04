from pathlib import Path
import json,hashlib,struct
R=Path(__file__).resolve().parent
names=['TWELVE_HALL_PROOF.md','TWELVE_HALL_filter.py','TWELVE_HALL_summary.json',
       'TWELVE_HALL_witnesses.bin','TWELVE_HALL_freeze.py']
raws={v:(R/f'TWELVE_NEW_TYPES_positive_remaining_v{v}.bin').read_bytes() for v in (1,7,31)}
removed={v:set() for v in raws}
data=(R/'TWELVE_HALL_witnesses.bin').read_bytes();assert len(data)==7483*21
for v,i,S,T in struct.iter_unpack('<BIQQ',data):
    assert v in raws and i<len(raws[v])//11 and i not in removed[v]
    rec=raws[v][11*i:11*(i+1)];H={0,*rec}
    ss={x for x in range(64) if S>>x&1};tt={x for x in range(64) if T>>x&1}
    assert ss and all(x not in H and x.bit_count()%2==0 for x in ss)
    assert tt=={x^(1<<d) for x in ss for d in range(6) if x^(1<<d) not in H}
    assert len(tt)<len(ss);removed[v].add(i)
for v,raw in raws.items():
    out=b''.join(raw[11*i:11*(i+1)] for i in range(len(raw)//11) if i not in removed[v])
    assert out==(R/f'TWELVE_HALL_remaining_v{v}.bin').read_bytes()
    names.extend([f'TWELVE_NEW_TYPES_positive_remaining_v{v}.bin',f'TWELVE_HALL_remaining_v{v}.bin'])
manifest={'status':'FROZEN_CANDIDATE_INDEPENDENT_REVIEW_PENDING',
          'files':{n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in names},
          'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'TWELVE_HALL_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print('Author checked and froze7483 explicit neighborhood-deficiency witnesses.')
