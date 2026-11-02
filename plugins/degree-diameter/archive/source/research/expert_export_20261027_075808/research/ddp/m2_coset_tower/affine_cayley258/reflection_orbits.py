#!/usr/bin/env python3
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
from math import comb
import json
import resource
import time

def normalized_images(points):
    return [tuple(sorted((x-u)*pow(v-u,-1,43)%43 for x in points))
            for u in points for v in points if u!=v]

def main():
    start=time.process_time();base=Path(__file__).resolve().parent
    classes=defaultdict(list)
    for a,b in combinations(range(2,43),2):
        points=(0,1,a,b)
        images=normalized_images(points)
        assert all(t[0:2]==(0,1) and len(set(t))==4 for t in images)
        classes[min(images)].append(points)
    assert sum(map(len,classes.values()))==820
    records=[];stabilizers=Counter()
    for rep,members in sorted(classes.items()):
        images=normalized_images(rep)
        stabilizer=images.count(rep)
        assert min(images)==rep and len(members)==12//stabilizer
        stabilizers[stabilizer]+=1
        records.append({'id':len(records),'reflection_fields':rep,'stabilizer_order':stabilizer,'normalized_member_count':len(members),'normalized_members':members,'full_affine_orbit_size':43*42//stabilizer})
    assert len(records)==74 and stabilizers=={1:63,2:10,3:1}
    assert sum(r['full_affine_orbit_size'] for r in records)==comb(43,4)
    result={'status':'COMPLETE_REFLECTION_SET_ORBITS','field':43,'normalized_sets_checked':820,'affine_orbits':74,'stabilizer_histogram':dict(sorted(stabilizers.items())),'all_four_element_subsets':comb(43,4),'covered_four_element_subsets':sum(r['full_affine_orbit_size'] for r in records),'orbits':records,'actual_graphs_generated':0,'raw_scope_three_patterns':3*74*43**2,'CPU_seconds':time.process_time()-start}
    (base/'REFLECTION_ORBITS.json').write_text(json.dumps(result,indent=2)+'\n')
    with (base/'reflection_representatives.txt').open('w') as stream:
        stream.write('74\n')
        for r in records:stream.write(' '.join(map(str,r['reflection_fields']))+'\n')
    usage=resource.getrusage(resource.RUSAGE_SELF)
    (base/'orbit_cpu.json').write_text(json.dumps({'process_CPU_seconds':usage.ru_utime+usage.ru_stime,'enumeration_CPU_seconds':result['CPU_seconds']},indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='orbits'},indent=2))

if __name__=='__main__':main()
