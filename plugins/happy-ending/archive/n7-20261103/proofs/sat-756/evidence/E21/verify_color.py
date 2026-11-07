"""Portable TSV-only, solver-free verification. MUST run on the Linux server only."""
import csv
import hashlib
import itertools
import json
from pathlib import Path
import platform

OUT = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    assert platform.system() == 'Linux', 'Scientific verification is Linux-only'
    import sys
    if len(sys.argv) != 2:
        raise SystemExit('Usage: python3 verify_color.py color.tsv')
    input_path=Path(sys.argv[1])
    n=25
    triples=list(itertools.combinations(range(1,n+1),3))
    colors={}
    with input_path.open(newline='') as stream:
        reader=csv.DictReader(stream,delimiter='\t')
        assert reader.fieldnames == ['i','j','k','red_true_blue_false']
        for row in reader:
            assert None not in row and None not in row.values()
            i,j,k=[int(row[x]) for x in ['i','j','k']]
            assert 1<=i<j<k<=n and (i,j,k) not in colors
            assert row['red_true_blue_false'] in ['0','1']
            colors[i,j,k] = row['red_true_blue_false']=='1'
    assert set(colors)==set(triples) and len(colors)==2300
    packet_violations=[]
    packet_count=0
    for four in itertools.combinations(range(1,n+1),4):
        packet_count+=1
        signs=[colors[t] for t in itertools.combinations(four,3)]
        if sum(a!=b for a,b in zip(signs,signs[1:]))>1: packet_violations.append(four)
    lengths={c:{} for c in (False,True)}
    starts={c:{} for c in (False,True)}
    for j in range(2,n+1):
        for i in range(1,j):
            for c in (False,True):
                lengths[c][i,j]=max([2]+[lengths[c][k,i]+1 for k in range(1,i) if colors[k,i,j]==c])
                starts[c][2,i,j]={i}
                for size in range(3,6):
                    union=set()
                    for k in range(1,i):
                        if colors[k,i,j]==c: union.update(starts[c].get((size-1,k,i),set()))
                    starts[c][size,i,j]=union
    weak_violations=[]
    outer_pair_count=0
    for j in range(2,n+1):
        blue=set().union(*(starts[False][4,i,j] for i in range(1,j)))
        red=set().union(*(starts[True][5,i,j] for i in range(1,j)))
        outer_pair_count+=j-1
        weak_violations.extend((i,j) for i in blue&red)
    states=[]
    for j in range(1,n+1):
        states.append(tuple(max([0]+[lengths[True][i,j]-1 for i in range(1,j) if lengths[False][i,j]-1>=x]) for x in range(1,4)))
    catalog=[(a,b,c) for a in range(5) for b in range(a+1) for c in range(b+1)]
    def ordinary(s): return sum(x>0 for x in s)+max(s)<=6
    normal={s for s in catalog if ordinary(s)}
    e=sum(not ordinary(s) for s in states)
    m=len(normal-set(states))
    maximum_blue=max(lengths[False].values())
    maximum_red=max(lengths[True].values())
    passed=(not packet_violations and maximum_blue<5 and maximum_red<6 and not weak_violations and len(set(states))==n and all(s in catalog for s in states) and e==m)
    result={'schema':'n756_portable_color_verification_v1','pass':passed,'execution_platform':platform.platform(),'solver_invocations':0,'input_color_tsv':str(input_path),'input_color_tsv_sha256':digest(input_path),'verifier_sha256':digest(Path(__file__)),'color_semantics':'TSV value 1=red, 0=blue','triple_count':len(colors),'color_tsv_sha256':digest(input_path),'packet_count':packet_count,'packet_violations':packet_violations,'maximum_blue_path_vertices':maximum_blue,'maximum_red_path_vertices':maximum_red,'outer_pair_count':outer_pair_count,'weak_7_gon_outer_pair_violations':weak_violations,'catalog_count':len(catalog),'ordinary_catalog_count':len(normal),'exceptional_catalog_count':len(catalog)-len(normal),'states_by_vertex':states,'state_injection':len(set(states))==n,'exceptional_count_e':e,'missing_ordinary_count_m':m,'count_identity':n==25+e-m}
    (OUT/'portable-verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    assert passed

if __name__=='__main__': main()
