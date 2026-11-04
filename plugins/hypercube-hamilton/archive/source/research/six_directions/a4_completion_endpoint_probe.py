"""Exact finite accounting of endpoint availability for canonical A-side partials.
All negative endpoint decisions are derived from the certified Q4 tables.
"""
import itertools
import json
import math
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parent
def edge(x,y):return tuple(sorted((x,y)))
def main():
    sources={w:json.loads((ROOT/f'q4_distance{w}_avoided_table_verification.json').read_text()) for w in (1,3)}
    odd=[x for x in range(16) if x.bit_count()%2]
    bad_original={}
    for y in odd:
        perm=[i for i in range(4) if y>>i&1]+[i for i in range(4) if not y>>i&1]
        def tr(x):return sum(1<<perm[i] for i in range(4) if x>>i&1)
        values=set()
        for item in sources[y.bit_count()]['exceptions']:
            f=frozenset(edge(tr(a),tr(b)) for a,b in item['matching'])
            mate={a:b for e in f for a,b in (e,e[::-1])}
            for d,k in mate.items():
                original=frozenset((f-{edge(d,k)})|{edge(y,k)})
                values.add((d,original))
        bad_original[y]=values
    failures=json.loads((ROOT/'a4_single_crossing_exceptions.json').read_text())['exceptions']
    results=[]
    for c in (1,3,5,7,9,11,13,15):
        m=(15-c)//2
        partial_counts=Counter()
        for item in failures:
            f=tuple(map(tuple,item['matching']))
            for sub in itertools.combinations(f,m):partial_counts[sub]+=1
        total=c*math.prod(range(1,c-1,2))
        stalls=[frozenset(f) for f,k in partial_counts.items() if k==total]
        classified=[]
        for f in stalls:
            ports=set(range(1,16))-{x for e in f for x in e}
            assert len(ports)==c
            good=[];bad_counts={}
            for y in odd:
                bad=sum(f<=original for d,original in bad_original[y])
                if y in ports:bad+=math.prod(range(1,c-1,2))
                assert bad<=total
                if bad<total:good.append(y)
                bad_counts[y]=bad
            classified.append({'matching':sorted(f),'ports':sorted(ports),'good_endpoints':good,'bad_completion_counts':bad_counts})
        item={'crossings':c,'completion_count':total,'fixed_target_stalls':len(stalls),
              'good_endpoint_histogram':dict(sorted(Counter(len(x['good_endpoints']) for x in classified).items())),
              'stalls':classified}
        results.append(item)
    result={'scope':'canonical A-side completion endpoint availability, not a full Q5 proof',
            'levels':results,'q5_a4_proved':False,'full_p6_proved':False}
    (ROOT/'a4_completion_endpoint_probe.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps([{k:x[k] for k in ['crossings','completion_count','fixed_target_stalls','good_endpoint_histogram']} for x in results]))
if __name__=='__main__':main()
