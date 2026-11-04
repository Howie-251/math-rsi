"""Exhaustive B-side signatures for the canonical three-bridge sufficient rule.

This is planning evidence only: a failure of the sufficient rule is NOT a
counterexample, and the bridge lemma requires its own semantic audit.
"""
import itertools as it,collections,json,math,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
H={7,11,13};Y={1,2,4};p,q=0,8
V=[x for x in range(16) if x not in H]
reports=[]
for c in (1,3,5):
    hist=collections.Counter();sub=collections.Counter();total=0;examples={}
    mate=[255]*16
    dst=R/f'A8_three_bridge_low_B_c{c}.bin'
    with dst.open('wb') as f:
        def visit(ports):
            global total
            total+=1
            port_bridges=len(Y&ports)
            internal_pairs=sum(mate[y] in Y for y in Y)//2
            fixed=mate[p]==q
            active_p=p in ports or mate[p] in Y
            active_q=q in ports or mate[q] in Y
            extra=int(active_p and active_q)
            count=port_bridges+internal_pairs+extra
            state='fixed_obstruction' if fixed else ('proper_gap' if (c+3)//2>count else 'low_gap')
            hist[state]+=1
            if state=='low_gap':
                sub[(port_bridges,internal_pairs,extra)]+=1
                f.write(bytes(mate))
            if state not in examples:
                examples[state]={'ports':sorted(ports),'matching':[[i,mate[i]] for i in V if i<mate[i]<16],
                                 'port_bridges':port_bridges,'internal_Y_pairs':internal_pairs,
                                 'extra_ob_root_pair':extra,'prescribed_pairs':count}
        def pair(rem,ports):
            if not rem:visit(ports);return
            x=rem[0]
            for i,y in enumerate(rem[1:],1):
                mate[x]=y;mate[y]=x
                pair(rem[1:i]+rem[i+1:],ports)
                mate[x]=mate[y]=255
        for port_tuple in it.combinations(V,c):
            ports=set(port_tuple)
            pair(tuple(x for x in V if x not in ports),ports)
    pairs=(13-c)//2
    expected=math.comb(13,c)*math.prod(range(1,2*pairs,2))
    assert total==expected
    if c==5:assert set(sub)=={(3,0,1)}
    reports.append({'crossings':c,'complete_B_inputs':total,'histogram':dict(hist),
                    'low_gap_signatures':[{'Y_ports':a,'Y_internal_pairs':b,'OB_root_pair':d,'count':n}
                       for (a,b,d),n in sorted(sub.items())],
                    'examples':examples,'low_gap_input_file':dst.name,
                    'low_gap_input_sha256':hashlib.sha256(dst.read_bytes()).hexdigest()})
out={'scope':'Exhaustive canonical B signatures for an audited-or-pending sufficient rule; not an A8 closure',
     'B_original_holes':sorted(H),'bridge_vertices':sorted(Y),'obstruction_edge':[p,q],
     'reports':reports,'full_a8_proved':False,'producer_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
(R/'A8_three_bridge_low_B_signatures.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps([{k:v for k,v in x.items() if k not in ['examples']} for x in reports],indent=2))
