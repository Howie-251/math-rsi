#!/usr/bin/env python3
from collections import Counter
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
import json
import resource
import time

def main():
    start=time.process_time()
    assert pow(3,8,17)==16 and pow(3,16,17)==1
    assert len({pow(3,j,17) for j in range(16)})==16
    records=[]
    surviving=[]
    groups=[]
    for pairs in range(5):
        involutions=8-2*pairs
        inverse=[i^1 if i<2*pairs else i for i in range(8)]
        layers=[[()]]
        for length in range(3):
            layers.append([word+(s,) for word in layers[-1] for s in range(8)
                           if not word or s!=inverse[word[-1]]])
        assert list(map(len,layers))==[1,8,56,392]
        words=[word for layer in layers for word in layer]
        passed=0;hist=Counter()
        for phases in combinations_with_replacement(range(8),pairs):
            letter_phases=[s for j in phases for s in (j,-j%16)]+[8]*involutions
            capacity=[0]*16
            for word in words:
                capacity[sum(letter_phases[s] for s in word)%16]+=1
            assert sum(capacity)==457 and all(capacity[j]==capacity[-j%16] for j in range(16))
            deficient=[j for j,c in enumerate(capacity) if c<17]
            row={'id':len(records),'pair_count':pairs,'involution_count':involutions,
                 'pair_phases':list(phases),'capacity':capacity,'minimum_capacity':min(capacity),
                 'deficient_phases':deficient,'passes':not deficient}
            records.append(row);hist[min(capacity)]+=1
            if not deficient:
                surviving.append(row);passed+=1
        coordinate_count=pairs+involutions
        projective=(17**(coordinate_count-1)-1)//16
        groups.append({'pair_count':pairs,'involution_count':involutions,
                       'patterns':comb(pairs+7,pairs),'survivors':passed,
                       'minimum_capacity_histogram':dict(sorted(hist.items())),
                       'coordinates':coordinate_count,'projective_classes_per_pattern':projective,
                       'projective_input_bound':passed*projective})
    assert len(records)==comb(12,4)==495
    result={'status':'COMPLETE_QUOTIENT_CAPACITY','group':'F17 semidirect_3 C16',
            'group_order':272,'degree':8,'target_diameter':3,'kernel_size':17,
            'patterns_checked':len(records),'survivor_count':len(surviving),
            'by_component_count':groups,'survivors':surviving,
            'projective_input_bound':sum(g['projective_input_bound'] for g in groups),
            'CPU_seconds':time.process_time()-start,'graphs_generated':0}
    out=Path(__file__).resolve().parent
    (out/'QUOTIENT_CAPACITY.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'quotient_capacity_patterns.json').write_text(json.dumps(records,separators=(',',':'))+'\n')
    usage=resource.getrusage(resource.RUSAGE_SELF)
    (out/'capacity_cpu.json').write_text(json.dumps({'process_CPU_seconds':usage.ru_utime+usage.ru_stime,'enumeration_CPU_seconds':result['CPU_seconds']},indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='survivors'},indent=2))

if __name__=='__main__':main()
