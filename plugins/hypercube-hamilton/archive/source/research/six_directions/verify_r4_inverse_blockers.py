"""Independent r4 inverse enumeration by sequential subdivision of Q edges.

Does not import the producer inverse formulas, blocker search, or connectivity
test. Every accepted blocker is checked by ordinary undirected traversal.
"""
import json,itertools,collections,sys,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
ed=lambda a,b:tuple(sorted((a,b)))
def mat(edges):
    F=frozenset(ed(a,b) for a,b in edges);vs=[v for e in F for v in e]
    assert len(vs)==len(set(vs)) and all(a!=b for a,b in F)
    return F
def negative(s,t,y):
    catalogue=json.loads((R/'q4_three_avoided_all_generation.json').read_text())
    for row in catalogue['rows']:
        for p in itertools.permutations(range(4)):
            transform=lambda v:sum(((v>>j)&1)<<p[j] for j in range(4))
            a,b,yy=row['avoided']
            if {transform(a),transform(b)}!={s,t} or transform(yy)!=y:continue
            raw=(R/row['file']).read_bytes();assert len(raw)==10395*29
            out=set()
            for off in range(0,len(raw),29):
                if raw[off+16:off+29]!=bytes([255])*13:continue
                m=raw[off:off+16]
                out.add(mat((transform(v),transform(m[v])) for v in range(16) if v<m[v]<16))
            return out
    raise ValueError((s,t,y))
def insert_vertex(F,Q,z):
    for a,b in Q:
        for k,q in ((a,b),(b,a)):
            # F must remain a matching; the Q endpoint k must be original.
            if any(k in e for e in F):continue
            yield F|{ed(k,z)},Q-{ed(a,b)}|{ed(z,q)}
def inverse(neg,s,t,m,mode):
    ans=collections.defaultdict(set)
    count=m-(2 if mode=='distinct' else 0 if mode=='ports' else 1)
    if count<0:return ans
    for L in neg:
        for selected in itertools.combinations(sorted(L),count):
            F=mat(selected);Q=L-F
            if mode=='ports':ans[F].add(Q)
            elif mode=='paired':ans[F|{ed(s,t)}].add(Q)
            elif mode in ('s_port','t_port'):
                z=t if mode=='s_port' else s
                for FF,QQ in insert_vertex(F,Q,z):ans[FF].add(QQ)
            else:
                for FF,QQ in insert_vertex(F,Q,s):
                    for FFF,QQQ in insert_vertex(FF,QQ,t):
                        # Reject an internally paired bridge: that case uses
                        # a separate quotient and separate boundary support.
                        if ed(s,t) not in FFF:ans[FFF].add(QQQ)
    return ans
def disc(D,Q):
    vertices={v for e in Q for v in e}
    assert {v for e in D for v in e}==vertices
    adj={v:set() for v in vertices}
    for a,b in D|Q:adj[a].add(b);adj[b].add(a)
    todo=[min(vertices)];seen=set()
    while todo:
        v=todo.pop()
        if v not in seen:seen.add(v);todo.extend(adj[v]-seen)
    return seen!=vertices
def main():
    s,t,y=map(int,sys.argv[1:4]);name=f'r4_boundary_blocking_{s}_{t}_{y}.json'
    raw=(R/name).read_bytes();source=json.loads(raw);neg=negative(s,t,y);summary=[];total=0
    assert len(neg)==source['negative_inputs']
    for row in source['reports']:
        c,mode=row['c'],row['mode'];expected=inverse(neg,s,t,(14-c)//2,mode);actual={};null=[];checked=0
        for item in row['items']:
            F=mat(item['matching']);qs={mat(q) for q in item['bad_outputs']}
            assert F not in actual and qs==expected[F];actual[F]=qs
            ports=set(range(16))-{0,y}-{v for e in F for v in e}
            assert len(F)==(14-c)//2 and len(ports)==c
            boundary=ports|{s,t} if mode=='distinct' else ports if mode=='paired' else (ports-{s})|{t} if mode=='s_port' else (ports-{t})|{s} if mode=='t_port' else ports-{s,t}
            assert all({v for e in q for v in e}==boundary for q in qs)
            if item['blocking_pairing'] is None:null.append(sorted(F));continue
            D=mat(item['blocking_pairing']);assert all(disc(D,q) for q in qs);checked+=1
        assert actual==expected and len(actual)==row['inverse_candidates'] and len(null)==row['unresolved']
        summary.append(dict(c=c,mode=mode,inverse_families=len(actual),blockers_checked=checked,unresolved=len(null),unresolved_F=null));total+=checked
        print(s,t,y,c,mode,len(actual),checked,'PASS',flush=True)
    out=dict(status='PASS',scope='Complete negative inverse families and positive auxiliary blockers; null cases left open',source_sha256=hashlib.sha256(raw).hexdigest(),reports=summary,total_blockers=total,fresh_semantic_audit_pending=True)
    (R/f'r4_inverse_blockers_{s}_{t}_{y}_verification.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
