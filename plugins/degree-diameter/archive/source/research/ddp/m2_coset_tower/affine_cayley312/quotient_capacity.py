#!/usr/bin/env python3
from collections import Counter, defaultdict
from itertools import combinations_with_replacement
from math import comb
from pathlib import Path
import json
import resource
import time

PAIR_PHASES=[(0,0),(0,1)]+[(j,w) for j in range(1,6) for w in range(2)]

def phase_add(a,b):return (a%12+b%12)%12+12*((a//12+b//12)%2)
def phase_inverse(a):return (-a%12)+12*(a//12)

def main():
    start=time.process_time()
    assert pow(2,6,13)==12 and len({pow(2,j,13) for j in range(12)})==12
    add=[[phase_add(a,b) for b in range(24)] for a in range(24)]
    records=[];survivors=[];groups=[];detail=defaultdict(lambda:{'patterns':0,'survivors':0,'projective_input_bound':0})
    for p in range(5):
        i=8-2*p
        inverse=[j^1 if j<2*p else j for j in range(8)]
        layers=[[()]]
        for length in range(3):
            layers.append([word+(s,) for word in layers[-1] for s in range(8) if not word or s!=inverse[word[-1]]])
        assert list(map(len,layers))==[1,8,56,392]
        words=[word for layer in layers for word in layer]
        histogram=Counter();passed=0;patterns=0;bound=0
        for pair_types in combinations_with_replacement(range(12),p):
            phasepairs=[j+12*w for j,w in (PAIR_PHASES[t] for t in pair_types)]
            pairletters=[v for h in phasepairs for v in (h,phase_inverse(h))]
            for central in range(min(1,i)+1):
                for a in range(i-central+1):
                    b=i-central-a
                    letters=pairletters+[6]*a+[18]*b+[12]*central
                    assert len(letters)==8
                    capacity=[0]*24
                    for word in words:
                        phase=0
                        for s in word:phase=add[phase][letters[s]]
                        capacity[phase]+=1
                    assert sum(capacity)==457
                    assert all(capacity[h]==capacity[phase_inverse(h)] for h in range(24))
                    deficient=[h for h,n in enumerate(capacity) if n<13]
                    m=p+a+b
                    projective=(13**(m-1)-1)//12
                    row={'id':len(records),'pair_count':p,'reflection_6_0_count':a,'reflection_6_1_count':b,'central_involution_count':central,'pair_types':list(pair_types),'pair_phases':[list(PAIR_PHASES[t]) for t in pair_types],'capacity_by_j_plus12w':capacity,'minimum_capacity':min(capacity),'deficient_phases':deficient,'passes':not deficient,'free_component_coordinates':m,'projective_input_bound':projective}
                    records.append(row);patterns+=1;histogram[min(capacity)]+=1
                    key=(p,a,b,central);detail[key]['patterns']+=1
                    if not deficient:
                        survivors.append(row);passed+=1;bound+=projective
                        detail[key]['survivors']+=1;detail[key]['projective_input_bound']+=projective
        assert patterns==comb(p+11,p)*(2*i+1)
        groups.append({'pair_count':p,'involution_count':i,'patterns':patterns,'survivors':passed,'maximum_of_minimum_capacity':max(histogram),'minimum_capacity_histogram':dict(sorted(histogram.items())),'projective_input_bound':bound})
    assert len(records)==4060
    compositions=[dict(zip(['pairs','reflection_6_0','reflection_6_1','central'],k),**v) for k,v in sorted(detail.items())]
    result={'status':'COMPLETE_QUOTIENT_CAPACITY','group':'(F13 semidirect_2 C12) x C2','group_order':312,'degree':8,'target_diameter':3,'kernel_size':13,'phase_encoding':'j+12*w, Q=C12 x C2 (not C24)','pair_phase_types':PAIR_PHASES,'patterns_checked':len(records),'survivor_count':len(survivors),'by_pair_count':groups,'by_composition':compositions,'survivors':survivors,'projective_input_bound':sum(r['projective_input_bound'] for r in survivors),'graphs_generated':0,'CPU_seconds':time.process_time()-start}
    out=Path(__file__).resolve().parent
    (out/'QUOTIENT_CAPACITY.json').write_text(json.dumps(result,indent=2)+'\n')
    (out/'quotient_capacity_patterns.json').write_text(json.dumps(records,separators=(',',':'))+'\n')
    usage=resource.getrusage(resource.RUSAGE_SELF)
    (out/'capacity_cpu.json').write_text(json.dumps({'process_CPU_seconds':usage.ru_utime+usage.ru_stime,'enumeration_CPU_seconds':result['CPU_seconds']},indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('survivors','by_composition')},indent=2))

if __name__=='__main__':main()
