"""Inverse classification of bad same-parity targets in a one-vertex-avoided path.
For F holes0,d (d odd), target y odd !=d, the transformed matching is
F-yF(y)+dF(y), holes0,y. A good transformed table gives path d--y avoiding0.
"""
import json
from pathlib import Path
from collections import Counter
ROOT=Path(__file__).resolve().parent
def edge(x,y):return tuple(sorted((x,y)))
def main():
    sources={w:json.loads((ROOT/f'q4_distance{w}_avoided_table_verification.json').read_text()) for w in (1,3)}
    bad={}; odd=[x for x in range(16) if x.bit_count()%2]
    for y in odd:
        weight=y.bit_count()
        permutation=[i for i in range(4) if y>>i&1]+[i for i in range(4) if not y>>i&1]
        def transform(x):return sum(1<<permutation[i] for i in range(4) if x>>i&1)
        bad[y]={frozenset(edge(transform(a),transform(b)) for a,b in c['matching']) for c in sources[weight]['exceptions']}
    by_input={}
    for y in odd:
        for f in bad[y]:
            mate={a:b for e in f for a,b in (e,e[::-1])}
            for d in odd:
                if d==y:continue
                k=mate[d]
                original=frozenset((f-{edge(d,k)})|{edge(y,k)})
                key=(d,tuple(sorted(original)))
                by_input.setdefault(key,set()).add(y)
    histogram=Counter(len(ys) for ys in by_input.values())
    total=8*135135
    histogram[0]=total-len(by_input)
    max_bad=max(histogram)
    witnesses=[{'root':d,'matching':list(f),'bad_targets':sorted(ys),'good_targets':sorted(set(odd)-{d}-ys)} for (d,f),ys in sorted(by_input.items()) if len(ys)==max_bad]
    result={'status':'COMPLETE_INVERSE_TARGET_ENUMERATION','scope':'Q4 F holes0,d odd, paths avoiding0 from d to another odd target',
            'local_inputs_total':total,'inputs_with_any_bad_target':len(by_input),
            'bad_target_histogram':dict(sorted(histogram.items())),
            'maximum_bad_targets':max_bad,'minimum_good_targets':7-max_bad,
            'maximal_bad_witnesses':witnesses,'full_p6_proved':False}
    (ROOT/'q4_avoided_endpoint_flexibility.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ['local_inputs_total','inputs_with_any_bad_target','bad_target_histogram','maximum_bad_targets','minimum_good_targets']}))
if __name__=='__main__':main()
