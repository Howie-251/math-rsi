"""Complete negative-output inverse families and auxiliary-pairing blockers.

Each positive blocker is an explicit perfect matching, not a failed search.
This is a candidate universal bridge lemma pending independent proof audit.
"""
import itertools,json,collections,sys
from pathlib import Path
R=Path(__file__).resolve().parent
edge=lambda a,b:tuple(sorted((a,b)))
def pairings(vs):
    if not vs:yield frozenset();return
    a=vs[0]
    for b in vs[1:]:
        for f in pairings(tuple(v for v in vs if v not in (a,b))):yield f|{(a,b)}
PM={};CACHE={}
def disconnected(n,D,F):
    dm=dict((a,b) for e in D for a,b in (e,e[::-1]));fm=dict((a,b) for e in F for a,b in (e,e[::-1]))
    v=0;k=0
    while True:
        v=fm[dm[v]];k+=1
        if v==0:return k<n//2
def blocker(outputs):
    base=min(outputs,key=lambda f:sorted(f));order=[v for e in sorted(base) for v in e];tr={v:i for i,v in enumerate(order)}
    fs=tuple(sorted(tuple(sorted(edge(tr[a],tr[b]) for a,b in F)) for F in outputs));n=len(order);key=(n,fs)
    if key not in CACHE:
        if n not in PM:PM[n]=list(pairings(tuple(range(n))))
        hit=None
        for D in PM[n]:
            if all(disconnected(n,D,F) for F in fs):hit=tuple(sorted(D));break
        CACHE[key]=hit
    hit=CACHE[key]
    return None if hit is None else sorted(edge(order[a],order[b]) for a,b in hit)
def main():
    z,y=map(int,sys.argv[1:3]);raw=(R/f'q4_balanced_two_avoided_{z}_{y}.bin').read_bytes();neg=[]
    for i in range(0,len(raw),30):
        if raw[i+16:i+30]==bytes([255])*14:
            m=raw[i:i+16];neg.append(frozenset((a,m[a]) for a in range(16) if a<m[a]<16))
    reports=[]
    for c in (5,7,9,11,13):
        m=(13-c)//2
        for mode in ('internal','occupied'):
            if mode=='internal' and m==0:continue
            cases=collections.defaultdict(set)
            for L in neg:
                if mode=='occupied':
                    for J in itertools.combinations(sorted(L),m):
                        cases[frozenset(J)].add(L-set(J))
                else:
                    for e in L:
                        for k,q in (e,e[::-1]):
                            for J in itertools.combinations(sorted(L-{e}),m-1):
                                F=frozenset(J)|{edge(z,k)}
                                out=L-set(J)-{e}|{edge(z,q)};cases[F].add(frozenset(out))
            rows=[];fail=[]
            for F,outs in sorted(cases.items(),key=lambda t:sorted(t[0])):
                D=blocker(outs);row=dict(matching=sorted(F),bad_outputs=[sorted(Q) for Q in sorted(outs,key=lambda Q:sorted(Q))],blocking_pairing=D)
                rows.append(row)
                if D is None:fail.append(row)
            reports.append(dict(c=c,mode=mode,inverse_candidates=len(cases),max_bad_outputs=max(map(len,cases.values()),default=0),
                unresolved=len(fail),items=rows))
            print(z,y,c,mode,len(cases),'unblocked',len(fail),'cache',len(CACHE),flush=True)
    out=dict(scope='All negative-output inverse families for one balanced bridge geometry',bridge=z,omitted=y,negative_inputs=len(neg),reports=reports,
        full_t15_proved=False,independent_review_pending=True)
    (R/f'r3_boundary_blocking_{z}_{y}.json').write_text(json.dumps(out)+'\n')
if __name__=='__main__':main()
