"""Independent standard-library validation of all global and transfer witnesses."""
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def edge(a,b):return tuple(sorted((a,b)))
def edges(p,closed=False):return {edge(a,b) for a,b in zip(p,p[1:]+(p[:1] if closed else []))}
def main():
    source=ROOT/'canonical_a4_construction_results.json';data=json.loads(source.read_text())
    for case in data['cases']:
        f={tuple(e) for e in case['matching']};flat=[x for e in f for x in e]
        assert len(flat)==len(set(flat))==28 and set(range(32))-set(flat)=={0,1,14,22}
        c=case['cycle'];assert len(c)==len(set(c))==31 and set(c)==set(range(32))-{1}
        ce=edges(c,True);assert len(ce)==31 and f<=ce
        assert all((a^b).bit_count()==1 for a,b in ce-f)
        cross={e for e in f if (e[0]^e[1])&1};assert len(cross)==case['crossings']
        fa={e for e in f if all(x%2 for x in e)}
        de={edge(2*a+1,2*b+1) for a,b in case['auxiliary']}
        p=case['a_path'];assert set(p)==set(range(3,32,2)) and len(p)==len(set(p))==15
        assert p[0]==2*case['root']+1 and p[-1]==2*case['target']+1
        pe=edges(p);assert fa|de<=pe and not fa&de
        assert all((a^b).bit_count()==1 for a,b in pe-fa-de)
        transfer=pe-de|cross|{edge(2*case['target']+1,2*case['target'])}
        used=set();union=set();ends=[]
        for segment in case['transfer_paths']:
            assert len(segment)>=2 and len(segment)==len(set(segment))
            assert not used&set(segment);used.update(segment)
            assert segment[0]%2==segment[-1]%2==0
            ends.extend((segment[0],segment[-1]));union|=edges(segment)
        assert union==transfer and len(ends)==len(set(ends))
        bc=case['b_cycle'];lb={tuple(e) for e in case['b_matching']}
        assert len(bc)==len(set(bc)) and len(bc) in (15,16)
        assert lb<=edges(bc,True)
        assert all((a^b).bit_count()==1 for a,b in edges(bc,True)-lb)
    result={'status':'PASS','certificates_checked':len(data['cases']),
            'scope':'individual canonical A4 and transfer certificates, not exhaustive inputs',
            'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'full_p6_proved':False}
    (ROOT/'canonical_a4_construction_verification.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))
if __name__=='__main__':main()
