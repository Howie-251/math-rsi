#!/usr/bin/env python3
"""Exact <=3 symbolic walks; no voltage assignment, deck group or fiber graph."""
import json
import time
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
PERMS=[(0,1,2,3),(1,0,2,3),(1,0,3,2),(1,2,0,3),(1,2,3,0)]
EXPECTED=[[13,13,13,13],[11,11,13,13],[11,11,11,11],[17,17,17,13],[15,15,15,15]]

def append_letter(word,k):
    if word and word[-1]==-k:return word[:-1]
    return word+(k,)

def main():
    start=time.process_time();rows=[];total_walks=0
    for typ,P in enumerate(PERMS):
        ip=[P.index(i) for i in range(4)];roots=[]
        for root in range(4):
            # index, exponent vector, reduced free-group word, port word
            layers=[[(root,(0,0,0,0),(),())]]
            for length in range(3):
                nxt=[]
                for i,exp,word,ports in layers[-1]:
                    for p,mask in enumerate((1,2,3)):
                        nxt.append((i^mask,exp,word,ports+(p,)))
                    v=list(exp);v[i]+=1
                    nxt.append((P[i],tuple(v),append_letter(word,i+1),ports+(3,)))
                    j=ip[i];v=list(exp);v[j]-=1
                    nxt.append((j,tuple(v),append_letter(word,-j-1),ports+(4,)))
                layers.append(nxt)
            walks=[x for layer in layers for x in layer];total_walks+=len(walks)
            same=[x for x in walks if x[0]==root]
            exps=sorted({x[1] for x in same});free=sorted({x[2] for x in same})
            witnesses=[]
            for w in free:
                choices=[x for x in same if x[2]==w]
                pick=min(choices,key=lambda x:(len(x[3]),x[3]))
                witnesses.append({'reduced_free_word':w,'integer_exponents':pick[1],'ports':pick[3]})
            roots.append({'root_index':root,'abelian_signature_count':len(exps),'free_word_count':len(free),'integer_signatures':exps,'free_word_witnesses':witnesses,'same_index_walk_counts_by_length':[sum(x[0]==root for x in layer) for layer in layers],'all_walks_length0_to3':len(walks)})
        counts=[x['free_word_count'] for x in roots]
        assert counts==EXPECTED[typ],(P,counts)
        assert [x['abelian_signature_count'] for x in roots]==EXPECTED[typ]
        best=min(roots,key=lambda x:x['free_word_count'])
        rows.append({'P':P,'roots':roots,'chosen_obstruction_root':best['root_index'],'same_index_reachable_deck_elements_upper':best['free_word_count'],'cannot_cover_group_order16':best['free_word_count']<16})
    assert total_walks==3120
    certificate={'status':'ALL_FIVE_UNIFORM_PERMUTATION_TYPES_SYMBOLICALLY_EXCLUDED_AT_DECK_ORDER16','permutation_types':rows,'formal_walks_enumerated':total_walks,'actual_voltage_assignments_evaluated':0,'group_instances_enumerated':0,'max_of_type_min_root_bounds':max(x['same_index_reachable_deck_elements_upper'] for x in rows),'generalization':'For any regular deck group H, same-index endpoints have at most the number of reduced free words. All |H|>15 are excluded; this is a conditional paper path-count argument, not a group enumeration.','CPU_seconds':time.process_time()-start}
    (HERE/'SYMBOLIC_CERTIFICATE.json').write_text(json.dumps(certificate,indent=2)+'\n')
    result={'status':certificate['status'],'formal_walks_enumerated':total_walks,'permutation_root_signature_counts':EXPECTED,'chosen_type_root_upper_bounds':[x['same_index_reachable_deck_elements_upper'] for x in rows],'same_index_deck_vertices_required':16,'potential_parameter_assignments_covered_by_proof':327680,'actual_numeric_assignments_enumerated':0,'numeric_gate_compiled':True,'numeric_gate_executed':False,'source_or_fiber_graphs_generated':0,'controller_candidates_found':0,'solver_calls':0,'Lean_calls':0,'CPU_seconds':certificate['CPU_seconds'],'CPU_budget_seconds':60,'all_owned_jobs_terminal':True,'stronger_paper_scope':'UniformK4 blocks x any regular deck group H with a single external F(i,h)=(P(i),h*g_i) and its inverse has4|H|<=60 if D3; in particular cannot enlarge the accepted60controller through any |H|>=16.','unexcluded':'Nonuniform external2factors,other controller organizations,changed fiber route mechanisms or general4096vertex graphs.'}
    (HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    (HERE/'TERMINAL.json').write_text(json.dumps({'status':result['status'],'running':False,'numeric_gate_executed':False,'graphs_added':0,'next':'Stop this uniform K4 single-F organization; do not start327680voltage enumeration, other moduli or deck-group ladder.'},indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
