"""Independent positive-cycle validation; does not prove input-domain completeness."""
import argparse,hashlib,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('inputs',type=Path);p.add_argument('certificates',type=Path)
p.add_argument('--offset',type=int,default=0);p.add_argument('--count',type=int,required=True)
p.add_argument('--holes',type=int,nargs=10,required=True);p.add_argument('--output',type=Path,required=True)
a=p.parse_args();holes=set(a.holes);assert len(holes)==10 and 0 in holes
assert a.certificates.stat().st_size==a.count*53
digest=hashlib.sha256()
with a.inputs.open('rb') as f,a.certificates.open('rb') as g:
    f.seek(a.offset*22)
    for i in range(a.count):
        inp=f.read(22);record=g.read(53);digest.update(record)
        assert len(inp)==22 and record[:22]==inp,(i,'input mismatch')
        assert set(inp)==set(range(32))-holes and len(set(inp))==22,(i,'holes')
        cycle=list(record[22:]);assert len(cycle)==31 and set(cycle)==set(range(1,32)),(i,'vertices')
        edges={tuple(sorted((cycle[j],cycle[(j+1)%31]))) for j in range(31)}
        required={tuple(sorted(inp[j:j+2])) for j in range(0,22,2)}
        assert required<=edges,(i,'missing matching edge')
        for x,y in edges-required:assert (x^y).bit_count()==1,(i,'new long edge',x,y)
out={'status':'PASS','scope':'Positive cycles only; domain completeness separate',
     'input_file':str(a.inputs),'offset':a.offset,'count':a.count,'certificate_sha256':digest.hexdigest(),
     'holes':sorted(holes),'full_A10_proved':False}
a.output.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
