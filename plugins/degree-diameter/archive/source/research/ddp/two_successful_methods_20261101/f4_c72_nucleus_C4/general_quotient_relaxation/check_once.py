#!/usr/bin/env python3
"""Actual quotient labels + relaxed120matching gate from saved unique routes.
Does not read source edges, rerun controller distances, create maps or solve SAT.
"""
import itertools
import json
import time
from collections import Counter
from pathlib import Path
HERE=Path(__file__).resolve().parent
PARENT=HERE.parent
L=[(0,0,1)]+[(1,t,(0,1,3,2)[t]) for t in range(4)]
N=(0,1,0)
INV=(0,1,3,2)
PG=[(0,1)]+[(1,t) for t in range(4)]

def mul(a,b):
    out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return out
def dot(x,y):
    out=0
    for a,b in zip(x,y):out^=mul(a,b)
    return out
def mv(A,x):return tuple(dot(row,x) for row in A)
def qpoint(v):
    x=v[1:];z=next(a for a in x if a)
    return tuple(mul(INV[z],a) for a in x)
def save(path,data):path.write_text(json.dumps(data,indent=2)+'\n')

def quotient_binding():
    rows=[]
    for p in range(5):
        if p==0:H=[[0,0,1],[1,0,0],[0,1,0]]
        else:
            t=p-1;H=[[1,0,0],[t,1,0],[0,t,1]]
        assert mv(H,L[p])==(1,0,0)
        point_rows={i:qpoint(mv(H,L[i])) for i in range(5) if i!=p}
        nucleus=qpoint(mv(H,N))
        assert len(set(point_rows.values()))==4 and nucleus not in point_rows.values()
        assert set(point_rows.values())|{nucleus}==set(PG)
        assert all(point_rows[i]==PG[i] for i in point_rows) and nucleus==PG[p]
        rows.append({'port':p,'H':H,'H_Lp':[1,0,0],'incoming_other_conic_projections':[{'port':i,'PGpoint':v,'PGlabel':PG.index(v)} for i,v in point_rows.items()],'nucleus_projection':nucleus,'omitted_PGlabel':PG.index(nucleus),'PGlabel_order':PG})
    return rows

def source_gate(name,perms):
    old=json.loads((PARENT/name/'EDGE_DOMAINS.json').read_text())
    actual_input=json.loads((PARENT/name/'INPUT.json').read_text())
    assert [tuple(x) for x in actual_input['directions']]==L
    assert tuple(actual_input['nucleus'])==N
    allrows=[];empty=[];hist=Counter();first_matching=None
    for e in old:
        p,r=e['port'],e['reverse_port']
        bad={tuple(x['entry']):x['ordered_unique_pairs'] for x in e['unique_forbidden_entries']}
        assert all(i!=p and j!=r for i,j in bad)
        allowed=[pi for pi in perms if all(pi[i]!=j for i,j in bad)]
        hist[len(allowed)]+=1
        row={'edge':e['edge'],'source':e['source'],'target':e['target'],'port':p,'reverse_port':r,'source_incoming_rows':[i for i in range(5) if i!=p],'source_omitted_Nrow':p,'target_outgoing_columns':[j for j in range(5) if j!=r],'target_Njoker_column':r,'forbidden_entries':list(sorted(bad)),'domain_size':len(allowed),'one_full_quotient_permutation':allowed[0] if allowed else None}
        if allowed and first_matching is None:first_matching=row.copy()
        if not allowed:
            empty.append(e['edge']);found=None;I=[i for i in range(5) if i!=p]
            for size in range(1,5):
                for S in itertools.combinations(I,size):
                    J=sorted({j for i in S for j in range(5) if (i,j) not in bad})
                    if len(J)<len(S):found=(list(S),J);break
                if found:break
            assert found is not None
            S,J=found
            row['Hall']={'incoming_rows':S,'allowed_quotient_columns':J,'cardinalities':[len(S),len(J)],'joker_included':r in J,'strict_obstruction':len(J)<len(S)}
            row['unique_route_witnesses']=[{'forbidden_entry':key,'witness':pairs[0]} for key,pairs in sorted(bad.items())]
        allrows.append(row)
    assert len(allrows)==180
    folder=HERE/name;folder.mkdir(exist_ok=True)
    save(folder/'ALL_EDGE_MATCHING_DOMAINS.json',allrows)
    if empty:save(folder/'MINIMAL_HALL_CERTIFICATE.json',next(x for x in allrows if x['edge']==empty[0]))
    if first_matching:save(folder/'ONE_MATCHING_EXAMPLE.json',first_matching)
    # Explicitly show what happened to the former first24-domain witness.
    oldfirst=json.loads((PARENT/name/'EMPTY_EDGE_CERTIFICATE.json').read_text())['edge']
    result={'status':'GENERAL_QUOTIENT_HALL_OBSTRUCTION' if empty else 'ALL180_QUOTIENT_DOMAINS_SURVIVE_INTERFACE_ONLY','edge_domains_checked':180,'quotient_permutations_per_edge_before_constraints':120,'old24domain_first_empty_edge':oldfirst,'relaxed_domain_size_of_old_first_edge':allrows[oldfirst]['domain_size'],'domain_cardinality_histogram':dict(sorted(hist.items())),'empty_domain_edges':empty,'surviving_edge_domains':180-len(empty),'first_Hall_obstruction':next((x for x in allrows if x['domain_size']==0),None),'source_BFS_or_shortword_recomputation':0,'matrix360enumerations':0,'solver_calls':0,'graphs_generated':0}
    save(folder/'RESULT.json',result)
    return result

def main():
    start=time.process_time();assert (HERE/'PRED.json').exists()
    binding=quotient_binding();save(HERE/'QUOTIENT_BINDING.json',binding)
    perms=list(itertools.permutations(range(5)));assert len(perms)==120
    sources={name:source_gate(name,perms) for name in ['Exoo72','Michel72']}
    survivors=[name for name,r in sources.items() if not r['empty_domain_edges']]
    result={'status':'BOTH_GENERAL_PORTLINE_QUOTIENT_DOMAINS_OBSTRUCTED' if not survivors else 'RELAXED_QUOTIENT_SURVIVOR_INTERFACE_ONLY','CPU_seconds':time.process_time()-start,'CPU_budget_seconds':30,'workers':1,'quotient_binding_checks':5,'sources':{name:{k:v for k,v in r.items() if k!='first_Hall_obstruction'} for name,r in sources.items()},'surviving_controllers':survivors,'new_graphs':0,'solver_calls':0,'active_handles':[],'source_BFS_or_shortword_recomputation':0,'matrix360enumerations':0,'scope':'Only unique-distance3 necessary rank constraints with arbitrary injective5quotient-direction maps; no old all-bad-conic-N argument used. No D0/D2 sufficiency or full graph result is claimed.'}
    save(HERE/'RESULT.json',result)
    save(HERE/'TERMINAL.json',{'status':result['status'],'running':False,'solver_calls':0,'graphs_added':0,'next':'Stop this necessary gate and return actual interface; no automatic matrix/D0/D2/SAT/controller/seed continuation.'})
    print(json.dumps(result))

if __name__=='__main__':main()
