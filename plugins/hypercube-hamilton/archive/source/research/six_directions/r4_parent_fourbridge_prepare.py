"""Prepare core4/core24 inputs and a separate parameterized producer copy."""
import json,itertools
from pathlib import Path
from q4_five_avoided_jpair_prepare import verify
R=Path(__file__).resolve().parent
def main():
    source=(R/'r4_joint_fourbridge_generic.cpp').read_text()
    replacements={
        'int core,c;':'int core,c,xhole;',
        'for(int v=1;v<16;v++)if(find(hs,hs+3,v)==hs+3)':'for(int v=0;v<16;v++)if(v!=xhole&&find(hs,hs+3,v)==hs+3)',
        'if(core==4)hs[2]=15;':'xhole=core==24?3:0;if(core==4)hs[2]=15;',
        'if(!a||!b||a==bs[2]':'if(a==xhole||b==xhole||a==bs[2]',
        'genN(65534u&~(1u<<u)':'genN(65535u&~(1u<<xhole)&~(1u<<u)',
        'unsigned acovered=65534u;':'unsigned acovered=65535u&~(1u<<xhole);',
    }
    for a,b in replacements.items():assert source.count(a)==1,a;source=source.replace(a,b)
    (R/'r4_joint_fourbridge_parent.cpp').write_text(source)
    raw=json.loads((R/'r4_joint_blocking_check.json').read_text());records=[]
    for core in (4,24):
        rows=[r for r in raw['reports'] if r['core']==core]
        for row in rows:
            if row['c'] not in (4,6,8):continue
            (R/f'r4_joint_fourbridge_core{core}_B{row["c"]}.txt').write_text(''.join(' '.join(str(v) for e in F for v in e)+'\n' for F in row['matchings']))
        J=next(r['matchings'][0] for r in rows if r['c']==8);assert len(J)==3
        oriented=[tuple(sorted(e,key=lambda v:v.bit_count()%2)) for e in J]
        retained=(3,5,15) if core==4 else (6,10,15)
        for s,t in itertools.combinations(retained,2):
            for E1,E2 in itertools.combinations(oriented,2):
                for z,w in ((E1[0],E2[1]),(E2[0],E1[1])):
                    assert len({0,1,s,t,z,w})==6
                    row=verify((s,t,z,w,1));records.append(dict(core=core,**row))
        print(core,'J',J,'tables checked',flush=True)
    (R/'r4_parent_fourbridge_preparation.json').write_text(json.dumps(dict(status='PASS',scope='Inputs/tables only; no theorem closure',rows=records),indent=2)+'\n')
if __name__=='__main__':main()
