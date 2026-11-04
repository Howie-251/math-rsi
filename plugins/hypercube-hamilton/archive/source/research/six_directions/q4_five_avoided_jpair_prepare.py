"""Complete finite tables for two free-hole and two J-endpoint bridges."""
import itertools,json,subprocess,hashlib
from pathlib import Path
from verify_q4_three_avoided import pairings,components,edge
R=Path(__file__).resolve().parent;V=set(range(16))
def verify(omitted):
    name='q4_five_avoided_'+'_'.join(map(str,omitted))+'.bin';p=R/name
    if not p.exists():subprocess.check_output([str(R/'q4_five_avoided_probe.exe'),*map(str,omitted),str(p)])
    data=p.read_bytes();assert len(data)==945*27;holes={0,*omitted};support=V-set(omitted)
    domain=set(pairings(V-holes));assert len(domain)==945;pos=neg=checks=0
    for off in range(0,len(data),27):
        m=data[off:off+16];cyc=data[off+16:off+27]
        assert {v for v in V if m[v]==255}==holes
        assert all(m[v]<16 and m[v]!=v and m[m[v]]==v for v in V-holes)
        F=frozenset((v,m[v]) for v in V-holes if v<m[v]);assert F in domain;domain.remove(F)
        if cyc!=bytes([255])*11:
            assert len(set(cyc))==11 and set(cyc)==support
            E={edge(a,b) for a,b in zip(cyc,cyc[1:]+cyc[:1])}
            assert F<=E and all((a^b).bit_count()==1 for a,b in E-F);pos+=1
        else:
            neg+=1
            for a,b in itertools.combinations(sorted(v for v in support if v.bit_count()==1),2):
                for N in pairings(support-{0,a,b},True,F):
                    H=N|{edge(0,a),edge(0,b)};assert not H&F and len(components(support,F|H))>1;checks+=1
    assert not domain
    return dict(omitted=omitted,file=name,positive=pos,negative=neg,negative_degree_completions=checks,sha256=hashlib.sha256(data).hexdigest())
def main():
    reports=[]
    for core,retained in ((1,(3,5,9)),(4,(3,5,15))):
        rows=[]
        for s,t in itertools.combinations(retained,2):
            for E1,E2 in itertools.combinations(((6,7),(10,11),(12,13)),2):
                for z,w in ((E1[0],E2[1]),(E2[0],E1[1])):
                    row=verify((s,t,z,w,1));rows.append(row)
                    print(core,s,t,z,w,row['positive'],row['negative'],'PASS',flush=True)
        reports.append(dict(core=core,rows=rows))
    (R/'q4_five_avoided_jpair_verification.json').write_text(json.dumps(dict(status='PASS',reports=reports,fresh_semantic_audit_pending=True),indent=2)+'\n')
if __name__=='__main__':main()
