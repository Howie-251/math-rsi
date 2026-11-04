"""Complete inverse candidates when both r3 bridges are B ports at c=5."""
import json,itertools
from pathlib import Path
R=Path(__file__).resolve().parent
edge=lambda a,b:tuple(sorted((a,b)))
def main():
    data=(R/'q4_balanced_two_avoided_3_1.bin').read_bytes();neg=[]
    for i in range(0,len(data),30):
        if data[i+16:i+30]==bytes([255])*14:
            m=data[i:i+16];neg.append(frozenset((v,m[v]) for v in range(16) if v<m[v]<16))
    assert len(neg)==3
    def swap(v):return (v&~6)|((v&2)<<1)|((v&4)>>1)
    negatives={3:neg,5:[frozenset(edge(swap(a),swap(b)) for a,b in f) for f in neg]}
    candidates={}
    for r,s in ((3,5),(5,3)):
        fs=set()
        for L in negatives[r]:
            for Q in itertools.combinations(sorted(L),2):
                ports={r,*[v for e in Q for v in e]}
                if s not in ports:continue
                F=L-set(Q);assert len(F)==4 and set(range(16))-{0,7,1}-{v for e in F for v in e}==ports
                fs.add((tuple(sorted(ports)),tuple(sorted(F))))
        candidates[r]=fs
    both=candidates[3]&candidates[5]
    out=dict(scope='core0 r3 cut, c5, both bridge mirrors occupied; necessary B inverse candidates only',
        bridge_candidate_counts={str(r):len(v) for r,v in candidates.items()},
        simultaneous_candidates=[dict(ports=p,matching=f) for p,f in sorted(both)],
        count=len(both),full_core0_proved=False,full_t15_proved=False)
    (R/'t15_core0_r3_c5_inverse.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
