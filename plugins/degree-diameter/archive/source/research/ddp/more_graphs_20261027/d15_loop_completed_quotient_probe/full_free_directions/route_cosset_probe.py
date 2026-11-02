"""One algebra-selected route word per source, then its literal endpoints."""
from pathlib import Path
import itertools
import json
import resource
import time

resource.setrlimit(resource.RLIMIT_CPU,(5,5))
START=time.process_time()
P=Path(__file__).resolve().parent
assert json.loads((P/'ROUTE_COSSET_SEARCH_PREDICTION.json').read_text())['frozen_before_word_selection_and_endpoint_enumeration']
assert not (P/'ROUTE_COSSET_RESULT.json').exists()

def matvec(B,x):
    return tuple(sum(a*b for a,b in zip(row,x))%3 for row in B)

def matmul(A,B):
    k=len(A)
    return [[sum(A[i][h]*B[h][j] for h in range(k))%3 for j in range(k)] for i in range(k)]

def basis(vectors,k):
    rows=[list(v) for v in vectors]
    at=0
    for j in range(k):
        pivot=next((i for i in range(at,len(rows)) if rows[i][j]),None)
        if pivot is None:
            continue
        rows[at],rows[pivot]=rows[pivot],rows[at]
        inverse=rows[at][j]
        rows[at]=[(inverse*x)%3 for x in rows[at]]
        for i in range(len(rows)):
            if i!=at and rows[i][j]:
                scale=rows[i][j]
                rows[i]=[(x-scale*y)%3 for x,y in zip(rows[i],rows[at])]
        at+=1
    return [tuple(v) for v in rows[:at]]

def inside(x,W,k):
    return len(basis(W+[x],k))==len(W)

def encode(x):
    return sum(t*3**i for i,t in enumerate(x))

contexts=[]
predictions=[]
for label in ['source15552','source102060']:
    table=json.loads((P.parent/'affine_relation_recovery'/f'{label}_AFFINE_RELATIONS.json').read_text())
    interface=json.loads((P/f'{label}_FREE_DIRECTION_GROUPS.json').read_text())
    k,q=table['dimension'],table['bin_size']
    r=interface['D']-1
    arcs_by_controller={}
    for index,arc in enumerate(table['arcs']):
        assert not any(arc['c'])
        arcs_by_controller.setdefault(arc['from'],[]).append((index,arc))
    for arcs in arcs_by_controller.values():
        arcs.sort(key=lambda item:item[1]['to'])
        assert len(arcs)==5
    first=next(item for item in arcs_by_controller[0] if item[1]['to']==0)
    free0=next(c for c in interface['controllers'] if c['controller']==0)
    v0=tuple(first[1]['v'])
    tested=0
    selected=None
    selected_word=None
    for tail in itertools.product(range(5),repeat=r-1):
        word=[first]
        current=0
        for choice in tail:
            item=arcs_by_controller[current][choice]
            word.append(item)
            current=item[1]['to']
        M=[[int(i==j) for j in range(k)] for i in range(k)]
        W=[]
        for _,arc in word:
            M=matmul(arc['B'],M)
            W=basis([matvec(arc['B'],v) for v in W]+[tuple(arc['v'])],k)
        tested+=1
        if len(W)!=k-1 or not inside(matvec(M,v0),W,k):
            continue
        for direction in free0['directions']:
            p=tuple(direction['normalized_vector'])
            if direction['is_old_canonical_direction'] or inside(matvec(M,p),W,k):
                continue
            selected={
                'source':label,'n':table['n'],'D':interface['D'],'dimension':k,
                'word_length':r,'start_controller':0,'final_controller':current,
                'arc_indices':[i for i,_ in word],
                'controller_word':[0]+[a['to'] for _,a in word],
                'lex_tail_choices':list(tail),'words_tested_before_selection_inclusive':tested,
                'M':M,'W_RREF_basis':[list(v) for v in W],'rank_W':len(W),
                'canonical_v0':list(v0),'canonical_port_labels':[0,encode(v0),encode(tuple(-t%3 for t in v0))],
                'new_direction_p':list(p),'new_port_labels':[0,encode(p),encode(tuple(-t%3 for t in p))],
                'new_direction_index':direction['direction_index'],
                'M_v0':list(matvec(M,v0)),'M_p':list(matvec(M,p)),
                'M_v0_in_W':True,'M_p_in_W':False,
                'predicted_old_endpoint_count':3**(k-1),
                'predicted_new_endpoint_count':3**k,
                'predicted_intersection_count':3**(k-1),
                'predicted_new_targets_outside_old':2*3**(k-1),
                'scope':'Along this one fixed word, using completed literal relations; no all-target cover or new graph claim.'}
            selected_word=word
            break
        if selected:
            break
    if selected is None:
        selected={'source':label,'n':table['n'],'D':interface['D'],'dimension':k,
                  'word_length':r,'start_controller':0,'status':'NO_WITNESS_IN_FIXED_WORD_SCOPE',
                  'words_tested':tested,'words_planned':5**(r-1)}
    predictions.append(selected)
    contexts.append((table,selected,selected_word))

# This write precedes every call that enumerates concrete route endpoints.
(P/'ROUTE_COSSET_PREDICTION.json').write_text(json.dumps({
    'status':'CONCRETE_WORD_PREDICTIONS_FROZEN_BEFORE_ENDPOINT_ENUMERATION',
    'sources':predictions,'CPU_seconds_before_endpoint_enumeration':time.process_time()-START},
    ensure_ascii=False,indent=2)+'\n')

def actual_endpoints(table,word,port_labels):
    k,q=table['dimension'],table['bin_size']
    digits=lambda x:tuple(x//3**i%3 for i in range(k))
    states={digits(pin):[pin] for pin in port_labels}
    for _,arc in word:
        next_states={}
        for x,path in sorted(states.items()):
            z=matvec(arc['B'],x)
            for t in range(3):
                y=tuple((z[j]+t*arc['v'][j])%3 for j in range(k))
                next_states.setdefault(y,path+[arc['to']*q+encode(y)])
        states=next_states
    return states

results=[]
for table,pred,word in contexts:
    if word is None:
        results.append(pred)
        continue
    old=actual_endpoints(table,word,pred['canonical_port_labels'])
    new=actual_endpoints(table,word,pred['new_port_labels'])
    oldset,newset=set(old),set(new)
    common=oldset&newset
    assert len(oldset)==pred['predicted_old_endpoint_count']
    assert len(newset)==pred['predicted_new_endpoint_count']
    assert len(common)==pred['predicted_intersection_count']
    assert oldset<=newset and len(newset)==table['bin_size']
    witness=min(newset-oldset,key=encode)
    path=new[witness]
    compressed=[path[0]]
    for vertex in path[1:]:
        if vertex!=compressed[-1]:
            compressed.append(vertex)
    actual={'source':pred['source'],'status':'CONCRETE_NEW_DIRECTION_COSSET_PREDICTION_SUPPORTED',
            'controller_word':pred['controller_word'],'new_direction_p':pred['new_direction_p'],
            'canonical_v0':pred['canonical_v0'],'old_endpoint_count':len(oldset),
            'new_endpoint_count':len(newset),'intersection_count':len(common),
            'new_targets_outside_old':len(newset-oldset),'new_covers_entire_final_fiber':True,
            'old_local_endpoint_offsets':sorted(encode(x) for x in oldset),
            'new_local_endpoint_offsets':sorted(encode(x) for x in newset),
            'extra_target_literal_label':pred['final_controller']*table['bin_size']+encode(witness),
            'extra_target_route_with_virtual_stays':path,
            'same_route_after_removing_virtual_stays':compressed,
            'compressed_route_length':len(compressed)-1,
            'interpretation':'Only one fixed controller word was enumerated. Every virtual diagonal stay can be deleted, leaving a literal source walk of no greater length. This certifies entire-fiber route complementarity at equal cost3, not full-graph D or a cover.'}
    results.append(actual)
result={'status':'COMPLETE_FIXED_WORD_COSSET_PREDICTION_CHECK',
        'sources':results,'CPU_seconds':time.process_time()-START,
        'new_balls':0,'BFS':0,'solver_calls':0,'new_graphs':0}
(P/'ROUTE_COSSET_RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'status':result['status'],'CPU_seconds':result['CPU_seconds'],
                  'sources':[{key:value for key,value in source.items() if key not in
                              ['old_local_endpoint_offsets','new_local_endpoint_offsets']}
                             for source in results]},ensure_ascii=False))
