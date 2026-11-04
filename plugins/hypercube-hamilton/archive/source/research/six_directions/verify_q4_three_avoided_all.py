"""Independently check the 12 canonical three-avoided table families.

Positive cycles and complete matching domains are checked directly. Negatives
are checked by exhausting complementary short-degree factors, not DFS failure.
"""
import json,itertools,hashlib,collections
from pathlib import Path
from verify_q4_three_avoided import pairings,components,edge
R=Path(__file__).resolve().parent;V=set(range(16))

def main():
    source=json.loads((R/'q4_three_avoided_all_generation.json').read_text())
    rows=[];geometries=set()
    for row in source['rows']:
        omitted=tuple(row['avoided']);holes={0,*omitted};support=V-set(omitted)
        raw=(R/row['file']).read_bytes();assert len(raw)==10395*29
        domain=set(pairings(V-holes));assert len(domain)==10395
        positive=negative=completion_count=0
        for off in range(0,len(raw),29):
            m=raw[off:off+16];cyc=raw[off+16:off+29]
            assert {v for v in V if m[v]==255}==holes
            assert all(m[v]<16 and m[v]!=v and m[m[v]]==v for v in V-holes)
            F=frozenset((v,m[v]) for v in V-holes if v<m[v]);assert F in domain;domain.remove(F)
            if cyc!=bytes([255])*13:
                assert len(set(cyc))==13 and set(cyc)==support
                E={edge(a,b) for a,b in zip(cyc,cyc[1:]+cyc[:1])}
                assert F<=E and all((a^b).bit_count()==1 for a,b in E-F);positive+=1
            else:
                negative+=1
                for a,b in itertools.combinations(sorted(v for v in support if v.bit_count()==1),2):
                    for N in pairings(support-{0,a,b},True,F):
                        H=N|{edge(0,a),edge(0,b)}
                        assert not H&F and len(components(support,F|H))>1;completion_count+=1
        assert not domain and positive==row['positive'] and negative==row['negative']
        orb=set()
        for p in itertools.permutations(range(4)):
            tr=lambda v:sum(((v>>j)&1)<<p[j] for j in range(4))
            s,t=sorted(map(tr,omitted[:2]));orb.add((s,t,tr(omitted[2])))
        assert orb==set(map(tuple,row['orbit'])) and not orb&geometries;geometries|=orb
        rows.append(dict(file=row['file'],omitted=omitted,positive=positive,negative=negative,negative_completions=completion_count,sha256=hashlib.sha256(raw).hexdigest()))
    ev=[v for v in range(1,16) if v.bit_count()%2==0];odd=[v for v in range(16) if v.bit_count()%2]
    assert geometries=={(s,t,y) for s,t in itertools.combinations(ev,2) for y in odd}
    out=dict(status='PASS',scope='All168 marked Q4 three-avoided geometries via12 coordinate orbits; finite deterministic check',families=rows,total_records=12*10395,total_geometries=len(geometries),fresh_semantic_audit_pending=True)
    (R/'q4_three_avoided_all_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='families'}))
if __name__=='__main__':main()
