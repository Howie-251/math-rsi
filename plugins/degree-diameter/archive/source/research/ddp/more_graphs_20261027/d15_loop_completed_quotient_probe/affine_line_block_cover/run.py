"""Actual cached affine-line block masks and one bounded small SAT per source."""
from pathlib import Path
from collections import Counter
import json
import os
import resource
import signal
import struct
import subprocess
import time

P=Path(__file__).resolve().parent
BASE=P.parent.parent
ROOT=BASE.parent.parent.parent
CAD=ROOT/'.tools/lean-4.24.0-linux/bin/cadical'
START=time.process_time()
WALL=time.monotonic()
child0=resource.getrusage(resource.RUSAGE_CHILDREN)
CHILD0=child0.ru_utime+child0.ru_stime
assert json.loads((P/'PREDICTION.json').read_text())['frozen_before_line_masks_or_solver']
assert not (P/'RESULT.json').exists()
resource.setrlimit(resource.RLIMIT_CPU,(10,11))
results=[]
proc=None
cursor={'source':None,'stage':'INITIALIZING'}

def owncpu():
    return time.process_time()-START

def aggregate():
    r=resource.getrusage(resource.RUSAGE_CHILDREN)
    return owncpu()+r.ru_utime+r.ru_stime-CHILD0

def save(name,value):
    (P/name).write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n')

def terminal(status):
    result={'status':status,'sources':results,'cursor':cursor,
            'parent_preparation_and_decode_CPU_seconds':owncpu(),
            'aggregate_parent_children_CPU_seconds':aggregate(),
            'configured_aggregate_CPU_seconds':35,'wall_seconds':time.monotonic()-WALL,
            'new_balls':0,'source_BFS':0,'new_graphs':0,
            'scope':'Only at-most5 affine-line full-target-fibre certificate on these two fixed sources.'}
    save('RESULT.json',result)
    save('RUN_HANDLE.json',{'status':'TERMINAL','terminal_status':status,'pid':os.getpid()})
    print(json.dumps({k:v for k,v in result.items() if k!='sources'}),flush=True)

def cpu_stop(_signal,_frame):
    if proc is not None and proc.poll() is None:
        proc.kill()
        proc.wait()
    terminal('UNKNOWN_PARENT_PREPARATION_CPU_LIMIT')
    raise SystemExit(0)

signal.signal(signal.SIGXCPU,cpu_stop)

def read_balls(n,labels):
    full=(1<<n)-1
    balls={}
    if n==15552:
        path=BASE/'d15_D4_current15552/single_vertex_R3_cover/R3_MASKS.bin'
        data=memoryview(path.read_bytes())
        count,stored_n,words=struct.unpack_from('<III',data)
        assert (count,stored_n,words)==(648,n,243)
        stride=4+8*words
        assert len(data)==12+count*stride
        order=[]
        for i in range(count):
            at=12+i*stride
            pin=struct.unpack_from('<I',data,at)[0]
            order.append(pin)
            balls[pin]=int.from_bytes(data[at+4:at+stride],'little')&full
        assert order==labels
    else:
        folder=BASE/'d15_D5_current102060_source/monotone_R4_cover'
        order=[int(x) for x in (folder/'eligible.txt').read_text().split()]
        assert order==labels and len(order)==810
        data=memoryview((folder/'radius4.u64le.bin').read_bytes())
        stride=1595*8
        assert len(data)==810*stride
        for i,pin in enumerate(order):
            balls[pin]=int.from_bytes(data[i*stride:(i+1)*stride],'little')&full
    assert set(balls)==set(labels)
    return balls

def union_masks(pins,balls):
    mask=0
    for pin in pins:
        mask|=balls[pin]
    return mask

def first_bit(mask):
    return (mask&-mask).bit_length()-1 if mask else None

def sequential_atmost(inputs,k,nextvar):
    if len(inputs)<=k:
        return [],nextvar
    clauses=[]
    previous=None
    for x in inputs:
        current=list(range(nextvar,nextvar+k))
        nextvar+=k
        clauses.append([-x,current[0]])
        if previous is not None:
            for j in range(k):
                clauses.append([-previous[j],current[j]])
            for j in range(1,k):
                clauses.append([-x,-previous[j-1],current[j]])
            clauses.append([-x,-previous[k-1]])
        previous=current
    return clauses,nextvar

save('RUN_HANDLE.json',{'status':'PREPARING_AFFINE_LINE_MASKS','pid':os.getpid(),
                        'configured_aggregate_CPU_seconds':35,'preparation_CPU_seconds':10})

for label,n,D in [('source15552',15552,4),('source102060',102060,5)]:
    cursor={'source':label,'stage':'READING_CERTIFIED_FREE_INTERFACE'}
    phase_start=owncpu()
    interface=json.loads((P.parent/'full_free_directions'/f'{label}_FREE_DIRECTION_GROUPS.json').read_text())
    q,k=interface['bin_size'],interface['dimension']
    controllers=n//q
    free=interface['literal_free_ball_row_order']
    source_dir=BASE/('d15_D4_current15552' if n==15552 else 'd15_D5_current102060_source')
    profile=json.loads((source_dir/'SOURCE_PROFILE.json').read_text())
    assert profile['n']==n and set(profile['free_vertices'])==set(free)
    assert profile['degree_histogram']['14']==len(free)
    balls=read_balls(n,free)
    digits=[[x//3**i%3 for i in range(k)] for x in range(q)]
    powers=[3**i for i in range(k)]
    raw_lines=[]
    first_by_mask={}
    max_points_by_target=[0]*controllers
    fibre_full=(1<<q)-1
    for controller in interface['controllers']:
        a=controller['controller']
        offsets=controller['local_free_offsets27']
        controller_count=0
        for direction in controller['directions']:
            v=direction['normalized_vector']
            seen=set()
            for offset in offsets:
                line=tuple(sorted(sum(((digits[offset][j]+t*v[j])%3)*powers[j] for j in range(k)) for t in range(3)))
                if line in seen:
                    continue
                seen.add(line)
                pins=[a*q+x for x in line]
                assert len(set(pins))==3 and all(pin in balls for pin in pins)
                line_union=union_masks(pins,balls)
                blockmask=0
                tail=line_union
                for b in range(controllers):
                    part=tail&fibre_full
                    tail>>=q
                    count=part.bit_count()
                    if count>max_points_by_target[b]:
                        max_points_by_target[b]=count
                    if part==fibre_full:
                        blockmask|=1<<b
                item={'raw_line_index':len(raw_lines),'controller':a,
                      'direction_index':direction['direction_index'],
                      'direction':v,'local_offsets':list(line),'pins':pins,
                      'blockmask_decimal':str(blockmask),'blocks_covered':blockmask.bit_count()}
                raw_lines.append(item)
                if blockmask in first_by_mask:
                    first_by_mask[blockmask]['multiplicity']+=1
                else:
                    first_by_mask[blockmask]={'mask':blockmask,'first_witness':item,'multiplicity':1}
                controller_count+=1
                cursor={'source':label,'stage':'PREPARING_AFFINE_LINE_MASKS',
                        'controller':a,'direction_index':direction['direction_index'],
                        'raw_lines_complete':len(raw_lines)}
            assert len(seen)==9
        assert controller_count==117
    assert len(raw_lines)==117*interface['loop_controller_count']
    unique=[v for mask,v in first_by_mask.items() if mask]
    allblocks=0
    for item in unique:
        allblocks|=item['mask']
    targetfull=(1<<controllers)-1
    missingblocks=targetfull&~allblocks
    missingfirst=first_bit(missingblocks)
    topfive=sum(sorted((v['mask'].bit_count() for v in unique),reverse=True)[:5])
    masks_receipt={'source':label,'n':n,'D':D,'bin_size':q,
                   'raw_lines':raw_lines,'raw_line_count':len(raw_lines),
                   'exact_mask_count_including_zero':len(first_by_mask),
                   'positive_unique_mask_count':len(unique),
                   'positive_unique_masks':[{'mask_decimal':str(v['mask']),
                                             'multiplicity':v['multiplicity'],
                                             'first_witness':v['first_witness']} for v in unique],
                   'block_union_missing_count':missingblocks.bit_count(),
                   'first_missing_controller':missingfirst,
                   'first_missing_controller_max_points_from_any_line':None if missingfirst is None else max_points_by_target[missingfirst],
                   'max_points_covered_by_single_line_per_target':max_points_by_target,
                   'five_largest_column_size_sum':topfive,
                   'source_graph_or_ball_recomputed':False}
    save(f'{label}_LINE_BLOCK_MASKS.json',masks_receipt)
    result={'source':label,'n':n,'m':interface['m'],'D':D,'bin_size':q,
            'raw_line_count':len(raw_lines),'positive_unique_masks':len(unique),
            'block_union_missing_count':missingblocks.bit_count(),
            'first_missing_controller':missingfirst,
            'first_missing_controller_max_points_from_any_line':None if missingfirst is None else max_points_by_target[missingfirst],
            'five_largest_column_size_sum':topfive,
            'preparation_parent_CPU_seconds':owncpu()-phase_start,'solver_calls':0,
            'candidate':None,'actual_new_graph_n':None,'actual_new_graph_D':None,
            'ordinary_bad_unordered_pairs':None}
    if missingblocks or topfive<controllers:
        result['status']='CERTIFICATE_NECESSARY_BLOCK_UNION_REJECT' if missingblocks else 'CERTIFICATE_FIVE_COLUMN_CAPACITY_REJECT'
        results.append(result)
        save(f'{label}_RESULT.json',result)
        print(json.dumps(result),flush=True)
        continue
    if owncpu()>9.4 or aggregate()>23:
        result['status']='UNKNOWN_PREPARATION_OR_AGGREGATE_BUDGET_BEFORE_SOLVER'
        results.append(result)
        save(f'{label}_RESULT.json',result)
        break
    cursor={'source':label,'stage':'BUILDING_COMPLETE_BLOCK_CNF'}
    rows=[[] for _ in range(controllers)]
    for variable,item in enumerate(unique,1):
        mask=item['mask']
        while mask:
            bit=mask&-mask
            rows[bit.bit_length()-1].append(variable)
            mask^=bit
    assert all(rows)
    count=len(unique)
    cardinal,nextvar=sequential_atmost(list(range(1,count+1)),5,count+1)
    clauses=rows+cardinal
    cnf=P/f'{label}.cnf'
    with cnf.open('w') as stream:
        stream.write(f'p cnf {nextvar-1} {len(clauses)}\n')
        for clause in clauses:
            stream.write(' '.join(map(str,clause))+' 0\n')
    result.update({'line_selectors':count,'CNF_variables':nextvar-1,
                   'CNF_clauses':len(clauses),'target_block_clauses':controllers,
                   'CNF_file':cnf.name,'preparation_parent_CPU_seconds':owncpu()-phase_start})
    def child_limits():
        resource.setrlimit(resource.RLIMIT_CPU,(10,11))
    before_child=resource.getrusage(resource.RUSAGE_CHILDREN)
    child_cpu0=before_child.ru_utime+before_child.ru_stime
    with (P/f'{label}.stdout').open('w') as stdout,(P/f'{label}.stderr').open('w') as stderr:
        proc=subprocess.Popen([str(CAD),'-t','8',str(cnf)],stdout=stdout,stderr=stderr,preexec_fn=child_limits)
        cursor={'source':label,'stage':'ONE_BOUNDED_BLOCK_SAT','solver_pid':proc.pid}
        save('RUN_HANDLE.json',{'status':'ONE_BOUNDED_BLOCK_SAT','pid':os.getpid(),
                                'solver_pid':proc.pid,'source':label,'solver_internal_wallseconds':8,
                                'solver_OS_CPU_soft_hard':[10,11]})
        try:
            code=proc.wait(timeout=13)
        except subprocess.TimeoutExpired:
            proc.kill()
            code=proc.wait()
    after_child=resource.getrusage(resource.RUSAGE_CHILDREN)
    result.update({'solver_calls':1,'solver_returncode':code,
                   'solver_CPU_seconds':after_child.ru_utime+after_child.ru_stime-child_cpu0})
    if code==10:
        true=set()
        for line in (P/f'{label}.stdout').read_text().splitlines():
            if line.startswith('v '):
                true.update(x for x in map(int,line.split()[1:]) if x>0)
        assert all(any((lit>0 and lit in true) or (lit<0 and -lit not in true) for lit in clause) for clause in clauses)
        selected=[v for v in range(1,count+1) if v in true]
        assert len(selected)<=5
        selected_lines=[unique[v-1]['first_witness'] for v in selected]
        pins=sorted({pin for line in selected_lines for pin in line['pins']})
        assert 1<=len(pins)<=15 and all(pin in set(profile['free_vertices']) for pin in pins)
        full_old=(1<<n)-1
        complete_union=union_masks(pins,balls)
        assert complete_union==full_old
        candidate={'status':'GEOMETRIC_CERTIFICATE_AND_FULL_CACHED_COVER_VERIFIED',
                   'source':label,'source_n':n,'source_m':interface['m'],'D':D,'Delta':15,
                   'source_profile_degree_binding':str((source_dir/'SOURCE_PROFILE.json').relative_to(ROOT)),
                   'selected_line_variables':selected,'selected_lines':selected_lines,
                   'distinct_old_pins':pins,'distinct_pin_count':len(pins),
                   'old_pin_degrees':[14]*len(pins),'all_old_edges_to_be_retained':True,
                   'full_cached_target_covered':complete_union.bit_count(),'full_cached_target_missing':0,
                   'candidate_n':n+1,'candidate_m':interface['m']+len(pins),
                   'graph_exported_here':False,'new_source_BFS':0}
        result['candidate']=candidate
        result['status']='VERIFIED_NEIGHBOR_SET_FIRST_HIT'
        save('FIRST_HIT.json',candidate)
        results.append(result)
        save(f'{label}_RESULT.json',result)
        print('FIRST_HIT_READY '+json.dumps(candidate),flush=True)
        terminal('FIRST_HIT_STOP_REMAINING_SOURCE_UNTESTED')
        raise SystemExit(0)
    result['status']='RAW_UNSAT_FOR_LINE_BLOCK_CERTIFICATE' if code==20 else 'UNKNOWN_ONE_SOLVER_CALL'
    results.append(result)
    save(f'{label}_RESULT.json',result)
    print(json.dumps(result),flush=True)

cursor={'stage':'TERMINAL','source':None}
terminal('COMPLETE_FIXED_LINE_CERTIFICATE_BATCH' if len(results)==2 else 'UNKNOWN_BUDGET_WITH_UNTESTED_SOURCE')
