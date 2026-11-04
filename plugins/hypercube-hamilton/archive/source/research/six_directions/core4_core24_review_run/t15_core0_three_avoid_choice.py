"""Diagnostic complete B-face bridge choices for the zero-crossing core 0 cut.

Uses independently checked complete Q4 three-avoid tables. A global transfer
proof and audit are still required; this file does not assert core 0 closure.
"""
import json,itertools,collections
from pathlib import Path
R=Path(__file__).resolve().parent
edge=lambda a,b:tuple(sorted((a,b)))
def pairings(vs):
    if not vs:yield frozenset();return
    a=min(vs)
    for b in sorted(vs-{a}):
        for rest in pairings(vs-{a,b}):yield rest|{(a,b)}
def main():
    d=json.loads((R/'q4_three_avoided_verification.json').read_text())
    neg={tuple(sorted(r['omitted'][:2])):{frozenset(map(tuple,t['matching'])) for t in r['negative_records']} for r in d['families']}
    def swap(x):return (x&~6)|((x&2)<<1)|((x&4)>>1)
    neg[5,6]={frozenset(edge(swap(a),swap(b)) for a,b in f) for f in neg[3,6]}
    failures=[];hist=collections.Counter();allcount=0
    for f in pairings(set(range(16))-{0,1}):
        allcount+=1;mate={a:b for e in f for a,b in (e,e[::-1])};good=[]
        for s,t in ((3,5),(3,6),(5,6)):
            if mate[s]==t:continue
            fs=f-{edge(s,mate[s]),edge(t,mate[t])}|{edge(mate[s],mate[t])}
            if fs not in neg[s,t]:good.append([s,t])
        hist[len(good)]+=1
        if not good:failures.append(sorted(f))
    out=dict(scope='All K(Q4) B matchings with holes0,1; core0 zero-crossing double-bridge choice only',
        matchings=allcount,good_choice_histogram=dict(hist),failures=failures,
        global_transfer_proof_audit_pending=True,full_t15_proved=False,full_p6_proved=False)
    (R/'t15_core0_three_avoid_choice.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({**out,'failures':failures[:3],'failure_count':len(failures)},indent=2))
if __name__=='__main__':main()
