"""Replace only uncompiled new witness declarations by 32-entry packed blocks."""
import json,re,time
from pathlib import Path
T=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());Q=R/'formal/DegreeDiameter/Portfolio'
s=json.loads((D/'CHECKPOINT.json').read_text());assert not s['active_modules']
done=set(s['completed']);plan=json.loads((D/'MODULE_PLAN.json').read_text())
barrier=json.loads((D/'PAUSE_BARRIER.json').read_text());mod=barrier['module']
assert mod not in done
(Q/(mod+'.lean')).write_text((D/'PAUSE_BARRIER_SOURCE.lean.txt').read_text())
def parse(line):
    ts=re.findall(r'\(|\)|\.leaf|\.node|[0-9]+',line);at=0
    def p():
        nonlocal at
        assert ts[at]=='(';at+=1;k=ts[at];at+=1
        if k=='.leaf':v=int(ts[at]);at+=1
        else:assert k=='.node';v=(p(),p())
        assert ts[at]==')';at+=1;return v
    return p()
def get(t,i):
    while isinstance(t,tuple):t=t[i%2];i//=2
    return t
def tree(v):
    n=1
    while n<len(v):n*=2
    v=list(v)+[0]*(n-len(v))
    def emit(x):return '(.leaf '+str(x[0])+')'if len(x)==1 else'(.node '+emit(x[::2])+' '+emit(x[1::2])+')'
    return emit(v)
count=0
for mod in plan['leaves']:
    if 'Row'not in mod or mod in done:continue
    path=Q/(mod+'.lean');src=path.read_text()
    line=next(x for x in src.splitlines()if x.startswith('def witnessRow : NatTable := '))
    t=parse(line.split(':=',1)[1]);nl=640 if 'Derived' in mod else 585
    words=[get(t,i)for i in range(nl)]
    blocks=[sum(v*4194304**k for k,v in enumerate(words[start:start+32]))for start in range(0,nl,32)]
    declaration='def witnessBlocks : NatTable := '+tree(blocks)+'\ndef witnessWord (l : Line) : Nat :=\n  (witnessBlocks.get (l.val/32) / 4194304^(l.val%32)) % 4194304'
    src=src.replace(line,declaration).replace('witnessRow.get l.val','witnessWord l')
    assert all((blocks[i//32]//4194304**(i%32))%4194304==words[i]for i in range(nl))
    path.write_text(src);count+=1
result=dict(status='ONLY_UNCOMPILED_NEW_ROW_DECLARATIONS_REPACKED',CPU_seconds=time.process_time()-T+0.1,conservative_unmetered_parse_failure_charge=0.1,converted_rows=count,unchanged_passed_modules=len(done),block_size=32,word_base=4194304,control_barrier_failure_preserved=True,reason='actual one-row NatTable declarations cost about11.4 CPU per row; reduce declarations, retain same finite equations')
(D/'ADAPTATION_BLOCKS_RESULT.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result))
