"""Generate then independently check the 21 four-bridge Q4 tables."""
import itertools,json,subprocess,hashlib
from pathlib import Path
from verify_q4_three_avoided import pairings,components,edge
R=Path(__file__).resolve().parent;V=set(range(16))
def main():
    rows=[]
    for core,rs in ((1,(3,5,9)),(4,(3,5,15)),(24,(6,10,15))):
        for z in range(16):
            if not z.bit_count()%2 or z==1:continue
            omitted=(*rs,1,z);name='q4_five_avoided_'+'_'.join(map(str,omitted))+'.bin';p=R/name
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
                            H=N|{edge(0,a),edge(0,b)}
                            assert not H&F and len(components(support,F|H))>1;checks+=1
            assert not domain
            rows.append(dict(core=core,omitted=omitted,file=name,positive=pos,negative=neg,negative_degree_completions=checks,sha256=hashlib.sha256(data).hexdigest()))
            print(core,z,pos,neg,'PASS',flush=True)
    (R/'q4_five_avoided_verification.json').write_text(json.dumps(dict(status='PASS',scope='21 marked Q4 five-avoided geometries, complete 945 records each',rows=rows,fresh_semantic_audit_pending=True),indent=2)+'\n')
if __name__=='__main__':main()
