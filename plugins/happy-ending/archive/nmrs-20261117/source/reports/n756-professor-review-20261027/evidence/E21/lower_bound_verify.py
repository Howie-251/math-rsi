"""Standalone, solver-free verification. MUST run on the Linux server only."""
import csv
import hashlib
import itertools
import json
from pathlib import Path
import platform

ROOT = Path('/data/ktqiu_hdd/math_agent')
SOURCE = ROOT/'res/state_charging/20260903_qeq_position_context_satfirst_p0_v1/cases/000_qeq_k01_gap02_right_anchor_g331_global_missing_g330/solver.out'
EXPECTED = '584c4fa4bc89432d46de3a1f8afb488fc7bbd42b0084840d0660a251477df646'
OUT = Path(__file__).resolve().parent

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    assert platform.system() == 'Linux', 'Scientific verification is Linux-only'
    assert digest(SOURCE) == EXPECTED
    assignment = {}
    for line in SOURCE.read_text().splitlines():
        if line.startswith('v '):
            for token in line.split()[1:]:
                lit = int(token)
                if lit:
                    key=abs(lit)
                    assert key not in assignment or assignment[key] == (lit>0)
                    assignment[key] = lit>0
    n=25
    triples=list(itertools.combinations(range(1,n+1),3))
    # The frozen lib/erdos.py etv builder allocates these triple variables first,
    # in itertools.combinations order; SATInstance._fresh_var starts at one.
    colors={t:assignment[i] for i,t in enumerate(triples,1)}
    with (OUT/'color.tsv').open('w',newline='') as stream:
        writer=csv.writer(stream,delimiter='\t')
        writer.writerow(['i','j','k','red_true_blue_false'])
        for t in triples: writer.writerow([*t,int(colors[t])])
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
    result={'schema':'n756_standalone_lower_bound_verification_v1','pass':passed,'execution_platform':platform.platform(),'solver_invocations':0,'source_solver_output':str(SOURCE),'source_solver_output_sha256':digest(SOURCE),'verifier_sha256':digest(Path(__file__)),'variable_mapping':'ids 1..2300 = lexicographic combinations(1..25,3); true=red','mapping_source_bindings':{str(ROOT/p):digest(ROOT/p) for p in ['lib/erdos.py','lib/sat_tseitin.py']},'triple_count':len(colors),'color_tsv_sha256':digest(OUT/'color.tsv'),'packet_count':packet_count,'packet_violations':packet_violations,'maximum_blue_path_vertices':maximum_blue,'maximum_red_path_vertices':maximum_red,'outer_pair_count':outer_pair_count,'weak_7_gon_outer_pair_violations':weak_violations,'catalog_count':len(catalog),'ordinary_catalog_count':len(normal),'exceptional_catalog_count':len(catalog)-len(normal),'states_by_vertex':states,'state_injection':len(set(states))==n,'exceptional_count_e':e,'missing_ordinary_count_m':m,'count_identity':n==25+e-m}
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
    assert passed

if __name__=='__main__': main()
