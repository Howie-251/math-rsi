"""Candidate complete inverse families for two bridges; no global proof claim.

New files only. A has four same-parity holes x,s,t,w, omits x.
B has holes 0,y, omits y. Original crossing count c is even.
Every reported positive is an explicit auxiliary perfect matching.
"""
import itertools,json,collections,sys
from pathlib import Path
from r3_boundary_blocking_probe import blocker,edge
R=Path(__file__).resolve().parent

def negative_table(s,t,y):
    for p in itertools.permutations(range(4)):
        def tr(v):return sum(((v>>i)&1)<<p[i] for i in range(4))
        a,b=sorted((tr(s),tr(t)));yy=tr(y)
        path=R/f'q4_three_avoided_{a}_{b}_{yy}.bin'
        if not path.exists():continue
        inv={tr(v):v for v in range(16)};raw=path.read_bytes();neg=[]
        assert len(raw)==10395*29
        for off in range(0,len(raw),29):
            if raw[off+16:off+29]==bytes([255])*13:
                mm=raw[off:off+16]
                neg.append(frozenset(edge(inv[v],inv[mm[v]]) for v in range(16) if v<mm[v]<16))
        return neg
    raise ValueError((s,t,y))

def families(neg,s,t,c,mode):
    m=(14-c)//2;cases=collections.defaultdict(set)
    for L in neg:
        if mode=='ports':
            for J in itertools.combinations(sorted(L),m):
                J=frozenset(J);cases[J].add(L-J)
        elif mode=='paired':
            for J in itertools.combinations(sorted(L),m-1):
                J=frozenset(J);cases[J|{edge(s,t)}].add(L-J)
        elif mode in ('s_port','t_port'):
            z=t if mode=='s_port' else s
            for e in L:
                for k,q in (e,e[::-1]):
                    for J in itertools.combinations(sorted(L-{e}),m-1):
                        J=frozenset(J)
                        cases[J|{edge(z,k)}].add(L-J-{e}|{edge(z,q)})
        elif mode=='distinct':
            if m<2:continue
            # R pairs the two bridge endpoints to each other.
            for e in L:
                for k,l in (e,e[::-1]):
                    for J in itertools.combinations(sorted(L-{e}),m-2):
                        J=frozenset(J)
                        cases[J|{edge(s,k),edge(t,l)}].add(L-J-{e}|{edge(s,t)})
            # R pairs each bridge endpoint to a different crossing port.
            for e,f in itertools.permutations(sorted(L),2):
                for k,q in (e,e[::-1]):
                    for l,p in (f,f[::-1]):
                        for J in itertools.combinations(sorted(L-{e,f}),m-2):
                            J=frozenset(J)
                            cases[J|{edge(s,k),edge(t,l)}].add(L-J-{e,f}|{edge(s,q),edge(t,p)})
        else:raise ValueError(mode)
    return cases

def main():
    s,t,y=map(int,sys.argv[1:4]);minimum=int(sys.argv[4]) if len(sys.argv)>4 else 4
    neg=negative_table(s,t,y)
    reports=[]
    for c in range(minimum,13,2):
        for mode in ('distinct','paired','s_port','t_port','ports'):
            cases=families(neg,s,t,c,mode);rows=[];unresolved=0
            for F,qs in sorted(cases.items(),key=lambda x:sorted(x[0])):
                ports=set(range(16))-{0,y}-{v for e in F for v in e}
                assert len(ports)==c and len(F)==(14-c)//2
                boundary={'distinct':ports|{s,t},'paired':ports,'s_port':(ports-{s})|{t},'t_port':(ports-{t})|{s},'ports':ports-{s,t}}[mode]
                assert all({v for e in Q for v in e}==boundary and 2*len(Q)==len(boundary) for Q in qs)
                D=blocker(qs);unresolved+=D is None
                rows.append(dict(matching=sorted(F),bad_outputs=[sorted(Q) for Q in sorted(qs,key=lambda q:sorted(q))],blocking_pairing=D))
            reports.append(dict(c=c,mode=mode,inverse_candidates=len(cases),unresolved=unresolved,items=rows))
            print(s,t,y,c,mode,len(cases),'unblocked',unresolved,flush=True)
            out=dict(scope='Candidate two-bridge inverse blocking; mathematical audit pending',bridges=[s,t],B_omitted=y,negative_inputs=len(neg),reports=reports,full_t15_proved=False)
            (R/f'r4_boundary_blocking_{s}_{t}_{y}.json').write_text(json.dumps(out)+'\n')
if __name__=='__main__':main()
