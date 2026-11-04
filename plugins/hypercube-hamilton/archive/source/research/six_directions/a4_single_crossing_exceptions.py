"""Complete inverse enumeration of the canonical one-crossing transfer stalls.
This enumerates local A-side matchings, not full Q5 counterexamples.
"""
import json
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parent
def edge(x,y):return tuple(sorted((x,y)))
def permute(x):return (x&3)|((x&4)<<1)|((x&8)>>1)
def main():
    source=json.loads((ROOT/'q4_distance3_avoided_table_verification.json').read_text())
    assert source['status']=='PASS' and len(source['exceptions'])==53
    bad7={frozenset(map(tuple,c['matching'])) for c in source['exceptions']}
    bad11={frozenset(edge(permute(x),permute(y)) for x,y in f) for f in bad7}
    bad={7:bad7,11:bad11};failures={};candidates=set()
    for w in (7,11):
        for f in bad[w]:
            mate={x:y for e in f for x,y in (e,e[::-1])}
            for d,k in mate.items():
                original=frozenset((f-{edge(d,k)})|{edge(w,k)})
                key=(d,tuple(sorted(original)));candidates.add(key)
                original_mate={x:y for e in original for x,y in (e,e[::-1])}
                bridge_results=[]
                for w2 in (7,11):
                    if w2==d:
                        bridge_results.append({'bridge':w2,'reason':'port_with_single_crossing'})
                    else:
                        k2=original_mate[w2]
                        transformed=frozenset((original-{edge(w2,k2)})|{edge(d,k2)})
                        bridge_results.append({'bridge':w2,'reason':'bad_table' if transformed in bad[w2] else 'works'})
                if all(x['reason']!='works' for x in bridge_results):
                    failures[key]={'port':d,'matching':sorted(original),'bridge_results':bridge_results}
    items=[failures[k] for k in sorted(failures)]
    result={'status':'COMPLETE_LOCAL_TRANSFER_EXCEPTION_ENUMERATION','scope':'canonical Q5 A4 cut0 with exactly one crossing edge; local A=Q4 forbidden0, bridge endpoints7,11',
            'local_A_inputs_total':15*135135,'inverse_candidates':len(candidates),
            'local_A_exceptions':len(items),'by_port':dict(sorted(Counter(x['port'] for x in items).items())),
            'exceptions':items,'q5_a4_counterexamples':False,'q5_a4_proved':False,'full_p6_proved':False}
    (ROOT/'a4_single_crossing_exceptions.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['local_A_inputs_total','inverse_candidates','local_A_exceptions','by_port']}))
if __name__=='__main__':main()
