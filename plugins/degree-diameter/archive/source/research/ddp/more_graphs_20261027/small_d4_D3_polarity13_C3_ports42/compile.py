"""Compile one exact finite 42-vertex template. Does not invoke a solver."""
from pathlib import Path
from itertools import product,combinations
from collections import Counter
import json,time,math
OUT=Path(__file__).resolve().parent

def canon(v):
    a=next(x for x in v if x);inv=1 if a==1 else 2
    return tuple(x*inv%3 for x in v)
def build():
    points=sorted({canon(v) for v in product(range(3),repeat=3) if any(v)})
    dot=lambda x,y:sum(a*b for a,b in zip(x,y))%3
    absolute=[i for i,v in enumerate(points) if dot(v,v)==0]
    base=[(u,v) for u,v in combinations(range(13),2) if dot(points[u],points[v])==0]
    degrees=Counter(x for e in base for x in e)
    assert len(points)==13 and len(base)==24 and len(absolute)==4
    assert all(degrees[u]==(3 if u in absolute else 4) for u in range(13))
    assert not any(u in absolute and v in absolute for u,v in base)
    parent=list(range(13))
    def find(x):
        while parent[x]!=x:x=parent[x]
        return x
    tree=[]
    for u,v in base:
        a,b=find(u),find(v)
        if a!=b:parent[a]=b;tree.append((u,v))
    assert len(tree)==12 and len({find(u) for u in range(13)})==1
    chords=[e for e in base if e not in tree]
    assert len(chords)==12
    cnf=CNF();edge={};shift=[];portvars=[];ports=sorted(3*v+s for v in absolute for s in range(3));helpers=[39,40,41]
    def bind(u,v,lit):
        k=tuple(sorted((u,v)));assert u!=v and k not in edge;edge[k]=lit
    for u,v in tree:
        for s in range(3):bind(3*u+s,3*v+s,True)
    for u,v in chords:
        vs=[cnf.new('chord_shift',base_edge=[u,v],shift=z) for z in range(3)]
        shift.append({'base_edge':[u,v],'selector_ids':vs})
        cnf.exactly(vs,1,'shift')
        for z,var in enumerate(vs):
            for s in range(3):bind(3*u+s,3*v+(s+z)%3,var)
    for u,v in combinations(ports,2):
        var=cnf.new('old_port_pair',endpoints=[u,v]);bind(u,v,var);portvars.append(var)
    for u in ports:
        for h in helpers:
            var=cnf.new('helper_spoke',endpoints=[u,h]);bind(u,h,var);portvars.append(var)
    assert cnf.n==138 and len(portvars)==102 and len(edge)==246
    bind(39,40,True);bind(40,41,True)
    assert len(edge)==248 and sum(lit is True for lit in edge.values())==38
    def X(u,v):return edge.get(tuple(sorted((u,v))),False) if u!=v else False
    for u in ports:cnf.exactly([X(u,v) for v in range(42) if X(u,v) is not True and X(u,v) in portvars],1,'port')
    for h,k in zip(helpers,[3,2,3]):cnf.exactly([X(h,u) for u in ports],k,'helper')
    structural_clauses=len(cnf.clauses);assert structural_clauses==2506
    edge_rows=[{'u':u,'v':v,'literal':lit,'fixed':lit is True} for (u,v),lit in sorted(edge.items())]
    Y={};reach_rows=[]
    for u,v in combinations(range(42),2):
        direct=X(u,v)
        middle=[w for w in range(42) if w!=u and w!=v and X(u,w) is not False and X(w,v) is not False]
        # A forced direct edge or forced2-path certifies D2 for all assignments.
        if direct is True or any(X(u,w) is True and X(w,v) is True for w in middle):
            Y[u,v]=True;reach_rows.append({'pair':[u,v],'literal':True,'meaning':'fixed path of length<=2'});continue
        y=cnf.new('reach2',endpoints=[u,v]);Y[u,v]=y
        terms=[direct] if direct is not False else []
        for w in middle:terms.append(cnf.conj(X(u,w),X(w,v),'two_path',path=[u,w,v]))
        cnf.add([-y]+terms,'reach2_soundness')
        reach_rows.append({'pair':[u,v],'literal':y,'direct_or_two_path_witnesses':terms})
    def R(u,v):return True if u==v else Y[tuple(sorted((u,v)))]
    for u,v in combinations(range(42),2):
        if R(u,v) is True:continue
        terms=[R(u,v)]
        for w in range(42):
            if w!=u and w!=v and X(u,w) is not False:
                terms.append(cnf.conj(X(u,w),R(w,v),'three_route',prefix=[u,w],target=v))
        cnf.add(terms,'diameter3')
    inputs={'field':3,'points':points,'base_edges':base,'base_degrees':[degrees[u] for u in range(13)],'absolute_base_points':absolute,'tree_edges':tree,'chord_edges':chords,'old_vertex_encoding':'3*base_point_id+sheet','sheets':[0,1,2],'old_vertices':39,'absolute_ports':ports,'helpers':{'a':39,'b':40,'c':41},'fixed_helper_path':[[39,40],[40,41]],'helper_attachment_counts':[3,2,3],'shift_selectors':shift,'structural_variable_count':138,'port_variable_ids':portvars,'structural_clauses':structural_clauses,'graph_n':42,'graph_m':84,'desired_degree':4,'target_D':3,'source_old_edges_per_assignment':72,'new_spokes_per_assignment':8,'remaining_port_pair_edges_per_assignment':2,'potential_edges':edge_rows,'gauge':'All12 canonical spanning-tree shifts are0; arbitrary port gadgets are closed under independent fiber C3 relabeling.'}
    return cnf,inputs,reach_rows

class CNF:
    def __init__(self):self.n=0;self.vars=[];self.clauses=[];self.types=Counter()
    def new(self,kind,**data):
        self.n+=1;self.vars.append({'id':self.n,'kind':kind,**data});return self.n
    def add(self,lits,kind):
        out=set()
        for x in lits:
            if x is True:return
            if x is False:continue
            assert isinstance(x,int) and x!=0
            if -x in out:return
            out.add(x)
        self.clauses.append(sorted(out,key=lambda z:(abs(z),z)));self.types[kind]+=1
    def exactly(self,vs,k,kind):
        assert all(isinstance(v,int) and not isinstance(v,bool) for v in vs)
        for group in combinations(vs,k+1):self.add([-v for v in group],kind+'_atmost')
        for group in combinations(vs,len(vs)-k+1):self.add(group,kind+'_atleast')
    def conj(self,a,b,role,**label):
        if a is False or b is False:return False
        if a is True:return b
        if b is True:return a
        if a==b:return a
        if a==-b:return False
        w=self.new('and_witness',role=role,arguments=[a,b],**label)
        self.add([-w,a],role+'_soundness');self.add([-w,b],role+'_soundness')
        return w

def main():
    started=time.process_time();cnf,inputs,reach=build()
    (OUT/'INPUT.json').write_text(json.dumps(inputs,indent=2)+'\n')
    (OUT/'VARIABLE_MAP.json').write_text(json.dumps(cnf.vars,indent=2)+'\n')
    (OUT/'REACH2_MAP.json').write_text(json.dumps(reach,indent=2)+'\n')
    path=OUT/'model.cnf'
    with path.open('w') as f:
        f.write('c F3 polarity13 cyclic3 lift plus arbitrary12port P3 completion\n')
        f.write(f'p cnf {cnf.n} {len(cnf.clauses)}\n')
        for c in cnf.clauses:f.write(' '.join(map(str,c))+' 0\n')
    placements=math.comb(12,3)*math.comb(9,2)*math.comb(7,3)*3
    stats={'status':'PREPARED_EXACT_CNF_NOT_SOLVED','n':42,'m':84,'base_n':13,'base_m':24,'absolute_points':4,'ports':12,'base_degree_histogram':dict(Counter(inputs['base_degrees'])),'tree_edges':12,'chords':12,'structural_variables':138,'ternary_shift_selectors':36,'binary_port_selectors':102,'shift_assignments':3**12,'labeled_port_completions':placements,'structural_assignments':3**12*placements,'potential_edges':248,'fixed_true_edges':38,'conditional_old_lift_edges':108,'port_potential_edges':102,'CNF_variables':cnf.n,'CNF_clauses':len(cnf.clauses),'structural_clauses':inputs['structural_clauses'],'variable_kind_counts':dict(Counter(v['kind'] for v in cnf.vars)),'clause_kind_counts':dict(cnf.types),'CNF_bytes':path.stat().st_size,'CPU_seconds':time.process_time()-started,'solver_calls':0,'SAT_results':0,'chosen_graphs':0,'graph_BFS':0,'scope':'Only the explicitly mapped polarity13 C3 shift lift plus helper P3 port completion; not all42graphs.'}
    (OUT/'MODEL_STATS.json').write_text(json.dumps(stats,indent=2)+'\n');(OUT/'PREPARATION_RECEIPT.json').write_text(json.dumps(stats,indent=2)+'\n');print(json.dumps(stats))
if __name__=='__main__':main()
