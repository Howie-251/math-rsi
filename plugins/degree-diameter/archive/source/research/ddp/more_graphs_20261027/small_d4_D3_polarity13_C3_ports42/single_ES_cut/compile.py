"""Prepare one fixed E-S edge-cut family. No solver or chosen graph is run."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import importlib.util,json,time,math
OUT=Path(__file__).resolve().parent;OLD=OUT.parent
spec=importlib.util.spec_from_file_location('original_port_cnf',OLD/'compile.py');original=importlib.util.module_from_spec(spec);spec.loader.exec_module(original)
CNF=original.CNF

def build():
    src=json.loads((OLD/'INPUT.json').read_text());geo=json.loads((OLD/'ROUTE_CLASS_CERTIFICATE.json').read_text())
    points=src['points'];base=[tuple(e) for e in src['base_edges']];absolute=geo['absolute_base_ids'];secants=geo['secant_base_ids'];external=geo['external_base_ids'];adj=[set() for _ in points]
    for u,v in base:adj[u].add(v);adj[v].add(u)
    cutbase=min(e for e in base if (e[0] in external and e[1] in secants) or (e[1] in external and e[0] in secants))
    E=next(u for u in cutbase if u in external);S=next(u for u in cutbase if u in secants)
    T=min(u for u in absolute if u not in adj[S]);e=3*E;s=3*S;a,b,c=39,40,41;cpins=[3*T+j for j in range(3)]
    # Force the selected cut base edge into a canonical spanning tree.
    parent=list(range(13))
    def find(x):
        while parent[x]!=x:x=parent[x]
        return x
    tree=[]
    for u,v in [cutbase]+[f for f in base if f!=cutbase]:
        x,y=find(u),find(v)
        if x!=y:parent[x]=y;tree.append((u,v))
    assert len(tree)==12 and cutbase in tree and len({find(u) for u in range(13)})==1
    chords=[f for f in base if f not in tree];assert len(chords)==12
    ports=src['absolute_ports'];freeA=[v for v in ports if v not in cpins]
    s_options=[v for v in freeA if v//3 not in adj[S]]
    assert len(freeA)==9 and len(s_options)==3
    cnf=CNF();edge={};shift=[];portvars=[]
    def bind(u,v,lit):
        key=tuple(sorted((u,v)));assert u!=v and key not in edge;edge[key]=lit
    for u,v in tree:
        for j in range(3):
            uu,vv=3*u+j,3*v+j
            if {uu,vv}!={e,s}:bind(uu,vv,True)
    for u,v in chords:
        vs=[cnf.new('chord_shift',base_edge=[u,v],shift=z) for z in range(3)];shift.append({'base_edge':[u,v],'selector_ids':vs});cnf.exactly(vs,1,'shift')
        for z,var in enumerate(vs):
            for j in range(3):bind(3*u+j,3*v+(j+z)%3,var)
    assert len(edge)==143 and sum(x is True for x in edge.values())==35
    assert tuple(sorted((e,s))) not in edge
    # Fixed positive structure: external endpoint to a, and full T-fiber to c.
    bind(e,a,True)
    for v in cpins:bind(v,c,True)
    bind(a,b,True);bind(b,c,True)
    for u,v in combinations(freeA,2):
        var=cnf.new('old_abs_pair',endpoints=[u,v]);bind(u,v,var);portvars.append(var)
    for v in s_options:
        assert v//3 not in adj[S]
        var=cnf.new('released_S_pair',endpoints=[s,v]);bind(s,v,var);portvars.append(var)
    for h in [a,b]:
        for v in freeA:
            var=cnf.new('helper_spoke',endpoints=[v,h]);bind(v,h,var);portvars.append(var)
    assert cnf.n==93 and len(portvars)==57 and len(edge)==206
    def X(u,v):return edge.get(tuple(sorted((u,v))),False) if u!=v else False
    for u in freeA:cnf.exactly([X(u,v) for v in range(42) if X(u,v) is not True and X(u,v) in portvars],1,'freeA')
    cnf.exactly([X(s,v) for v in s_options],1,'released_S')
    for h in [a,b]:cnf.exactly([X(h,v) for v in freeA],2,'helper_remaining')
    structural_clauses=len(cnf.clauses);assert structural_clauses==682
    edge_rows=[{'u':u,'v':v,'literal':lit,'fixed':lit is True} for (u,v),lit in sorted(edge.items())]
    Y={};reach_rows=[]
    for u,v in combinations(range(42),2):
        direct=X(u,v);middle=[w for w in range(42) if w!=u and w!=v and X(u,w) is not False and X(w,v) is not False]
        # Only fixed <=2 paths certify Y=true; c's uniform R3 is not an R2 claim.
        if direct is True or any(X(u,w) is True and X(w,v) is True for w in middle):
            Y[u,v]=True;reach_rows.append({'pair':[u,v],'literal':True,'meaning':'fixed realpath length<=2'});continue
        y=cnf.new('reach2',endpoints=[u,v]);Y[u,v]=y;terms=[direct] if direct is not False else []
        for w in middle:terms.append(cnf.conj(X(u,w),X(w,v),'two_path',path=[u,w,v]))
        cnf.add([-y]+terms,'reach2_soundness');reach_rows.append({'pair':[u,v],'literal':y,'direct_or_two_path_witnesses':terms})
    def R(u,v):return True if u==v else Y[tuple(sorted((u,v)))]
    for u,v in combinations(range(42),2):
        if R(u,v) is True:continue
        terms=[R(u,v)]
        for w in range(42):
            if w!=u and w!=v and X(u,w) is not False:terms.append(cnf.conj(X(u,w),R(w,v),'three_route',prefix=[u,w],target=v))
        cnf.add(terms,'diameter3')
    # Symbolic positive certificate: these base paths avoid the cut base edge.
    certpaths=[]
    for v in range(13):
        if v==T:path=[T]
        elif v in adj[T]:path=[T,v]
        else:
            candidates=[[T,w,v] for w in sorted(adj[T]&adj[v]) if cutbase not in [tuple(sorted((T,w))),tuple(sorted((w,v)))]]
            assert candidates;path=candidates[0]
        assert len(path)<=3 and cutbase not in [tuple(sorted(pair)) for pair in zip(path,path[1:])]
        certpaths.append({'target_base':v,'base_path_from_T':path,'old_length':len(path)-1,'cut_base_edge_avoided':True,'lift_cover':'all3 targets via suitable one of the3 T-starting sheets'})
    inputs={'field':3,'points':points,'base_edges':base,'base_classes':{k:geo[k] for k in ['absolute_base_ids','secant_base_ids','external_base_ids']},'old_vertex_encoding':'3*base_point_id+sheet','tree_edges':tree,'chord_edges':chords,'cut_base_edge':cutbase,'cut_external_base':E,'cut_secant_base':S,'deleted_old_lift_edge':sorted((e,s)),'cut_sheets':[0,0],'leaf_c_absolute_base':T,'leaf_c_fixed_old_neighbors':cpins,'fixed_e_a':[e,a],'helpers':{'a':a,'b':b,'c':c},'fixed_helper_path':[[a,b],[b,c]],'absolute_ports':ports,'free_absolute_ports':freeA,'released_external_port':e,'released_secant_port':s,'released_S_pair_options':s_options,'shift_selectors':shift,'port_variable_ids':portvars,'structural_variable_count':93,'structural_clauses':structural_clauses,'potential_edges':edge_rows,'n':42,'m':84,'degree':4,'target_D':3,'old_edges_selected':71,'helper_edges':2,'helper_spokes':8,'old_old_new_edges':3,'scope':'Only deterministic lex E-S cut, sheet0, lex nonadjacent T, P3, fixed e-a and fullT-c. No allcuts claim.'}
    guarantee={'status':'SYMBOLIC_UNIFORM_C_R3_ALL42','T_base':T,'T_not_adjacent_to_cut_S':T not in adj[S],'fixed_c_neighbors':cpins,'old_target_base_paths':certpaths,'all39_old_targets':'For each target sheet, reverse-lift the cut-avoiding basepath from target; its T-start is one of the3 neighbors of c.','new_target_paths':{'a':[c,b,a],'b':[c,b],'c':[c]},'R3_not_R2':True,'actual_voltage_assignments_enumerated':0,'graph_BFS':0}
    return cnf,inputs,reach_rows,guarantee

def main():
    started=time.process_time();cnf,inputs,reach,guarantee=build()
    for name,obj in [('INPUT.json',inputs),('VARIABLE_MAP.json',cnf.vars),('REACH2_MAP.json',reach),('C_FULL_FIBER_GUARANTEE.json',guarantee)]:
        (OUT/name).write_text(json.dumps(obj,indent=2)+'\n')
    path=OUT/'model.cnf'
    with path.open('w') as f:
        f.write('c Fixed E-S singlecut polarity13 cyclic3lift plus P3 positivefamily\n');f.write(f'p cnf {cnf.n} {len(cnf.clauses)}\n')
        for row in cnf.clauses:f.write(' '.join(map(str,row))+' 0\n')
    portcount=len(inputs['released_S_pair_options'])*math.comb(8,2)*math.comb(6,2)*3
    stats={'status':'PREPARED_EXACT_SINGLECUT_CNF_NOT_SOLVED','n':42,'m':84,'deleted_edge':inputs['deleted_old_lift_edge'],'cut_base_edge':inputs['cut_base_edge'],'fixed_T_base':inputs['leaf_c_absolute_base'],'fixed_c_neighbors':inputs['leaf_c_fixed_old_neighbors'],'released_S_pair_options':inputs['released_S_pair_options'],'retained_old_selected_edges':71,'new_helper_edges':2,'new_spokes':8,'new_old_old_edges':3,'structural_variables':93,'shift_selectors':36,'new_port_selectors':57,'shift_assignments':3**12,'labeled_port_completions':portcount,'structural_assignments':3**12*portcount,'potential_edges':206,'fixed_true_edges':41,'CNF_variables':cnf.n,'CNF_clauses':len(cnf.clauses),'structural_clauses':inputs['structural_clauses'],'variable_kind_counts':dict(Counter(v['kind'] for v in cnf.vars)),'clause_kind_counts':dict(cnf.types),'CNF_bytes':path.stat().st_size,'compiler_body_CPU_seconds':time.process_time()-started,'solver_calls':0,'chosen_graphs':0,'graph_BFS':0,'c_R3_positive_certificate':True,'Y2_c_targets_forced_by_R3_certificate':False}
    for n in ['MODEL_STATS.json','PREPARATION_RECEIPT.json']:(OUT/n).write_text(json.dumps(stats,indent=2)+'\n')
    print(json.dumps(stats))
if __name__=='__main__':main()
