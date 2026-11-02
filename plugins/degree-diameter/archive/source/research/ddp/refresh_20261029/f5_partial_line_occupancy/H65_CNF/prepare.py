#!/usr/bin/env python3
"""Only prepare separate H65 CNF increments; no solver imports or calls."""
import importlib.util,itertools,json,pathlib,time
D=pathlib.Path(__file__).resolve().parent
BASE=D.parent.parent
spec=importlib.util.spec_from_file_location('old_retention_prepare',BASE/'f5_induced_retention_closure/prepare.py')
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)
OLD_MAX=315221

class Recorded(old.CNF):
    def __init__(self,path,nv):
        super().__init__(path);self.nv=nv;self.clauses=[];self.operations=[];self.recorded=set()
    def add(self,*xs):
        if any(x is True for x in xs):return
        ys=list(dict.fromkeys(x for x in xs if x is not False))
        if any(-x in ys for x in ys):return
        self.clauses.append(ys);super().add(*xs)
    def gate(self,name,*args):
        before=self.nv
        out=getattr(super(),name)(*args)
        if type(out) is int and out>before and out not in self.recorded:
            self.operations.append((name,out,args));self.recorded.add(out)
        return out
    def both(self,a,b):return self.gate('both',a,b)
    def either(self,a,b):return self.gate('either',a,b)
    def xor(self,a,b):return self.gate('xor',a,b)
    def majority(self,a,b,c):return self.gate('majority',a,b,c)

def value(x,assign):return x if type(x) is bool else (assign[abs(x)] if x>0 else not assign[-x])
def evaluate(ops,assign):
    for name,out,args in ops:
        vals=[value(x,assign) for x in args]
        assign[out]=({'both':lambda:all(vals),'either':lambda:any(vals),'xor':lambda:vals[0]!=vals[1],
                      'majority':lambda:sum(vals)>=2}[name])()
def satisfied(clauses,assign):return all(any(value(x,assign) for x in row) for row in clauses)
def finish(cnf,body,out):
    cnf.f.close()
    with out.open('w') as f:
        f.write(f'p cnf {cnf.nv} {cnf.nc}\n');f.write(body.read_text())
    body.unlink()
def fragment(name,rows,nv):
    with (D/name).open('w') as f:
        f.write(f'p cnf {nv} {len(rows)}\n')
        for row in rows:f.write(' '.join(map(str,row))+' 0\n')

def main():
    if (D/'MODEL.json').exists():raise SystemExit('prepare already completed; do not silently overwrite')
    start=time.process_time()
    P=json.loads((BASE/'f5_full_d20_D3/PARAMETERS.json').read_text())
    parent=json.loads((BASE/'f5_induced_shared_routes_model/MODEL.json').read_text())
    assert parent['variables']==OLD_MAX
    ell=[tuple(e) for e in P['directions']];T=P['matrices'];inv=P['inverse_ports'];C=P['controller']
    pts=list(itertools.product(range(5),repeat=3))
    def add(x,y):return tuple((a+b)%5 for a,b in zip(x,y))
    def scale(k,x):return tuple(k*a%5 for a in x)
    def line(x,e):return frozenset(add(x,scale(k,e)) for k in range(5))
    def mat(m,x):return tuple(sum(a*b for a,b in zip(row,x))%5 for row in m)
    def code(x):return x[0]+5*x[1]+25*x[2]
    def keep(a,x):return 125*a+code(x)+1
    body=D/'high_flags.body.tmp'
    hs=[OLD_MAX+a+1 for a in range(30)]
    cnf=Recorded(body,OLD_MAX+30)
    layers=[];first_ops=None;first_clauses=None
    for a,h in enumerate(hs):
        op0=len(cnf.operations);cl0=len(cnf.clauses);v0=cnf.nv
        vectors=[[125*a+i+1] for i in range(125)]
        while len(vectors)>1:
            vectors=[cnf.add_bits(vectors[i],vectors[i+1]) if i+1<len(vectors) else vectors[i]
                     for i in range(0,len(vectors),2)]
        bits=vectors[0]
        ge=True
        for i,bit in enumerate(bits):ge=cnf.both(bit,ge) if ((65>>i)&1) else cnf.either(bit,ge)
        cnf.add(-h,ge);cnf.add(h,cnf.neg(ge))
        layers.append({'fiber':a,'high_variable':h,'sum_bits_little_endian':bits,'comparison_literal':ge,
                       'new_gate_variables':cnf.nv-v0,'clauses':cnf.nc-cl0})
        if a==0:first_ops=cnf.operations[op0:];first_clauses=cnf.clauses[cl0:]
    flags_nv=cnf.nv;flags_nc=cnf.nc
    finish(cnf,body,D/'high_flags.added.cnf')

    gate_truth=[]
    for name,nin in [('both',2),('either',2),('xor',2),('majority',3)]:
        temp=D/'gate_calibration.tmp';g=Recorded(temp,nin)
        out=getattr(g,name)(*range(1,nin+1));g.f.close();temp.unlink()
        checked=0
        for xs in itertools.product([False,True],repeat=nin):
            expected={'both':lambda:all(xs),'either':lambda:any(xs),'xor':lambda:xs[0]!=xs[1],
                      'majority':lambda:sum(xs)>=2}[name]()
            for z in [False,True]:
                ass={i+1:x for i,x in enumerate(xs)};ass[out]=z
                assert satisfied(g.clauses,ass)==(z==expected);checked+=1
        gate_truth.append({'gate':name,'complete_input_output_truth_states':checked,'passed':True})
    cal=[]
    patterns=[('prefix',k,list(range(1,k+1))) for k in range(126)]
    patterns += [('suffix',k,list(range(126-k,126))) for k in [64,65]]
    for label,k,ids in patterns:
        selected=set(ids);ass={i:i in selected for i in range(1,126)}
        evaluate(first_ops,ass)
        got=sum((1<<i) for i,bit in enumerate(layers[0]['sum_bits_little_endian']) if value(bit,ass))
        assert got==k
        ass[hs[0]]=k>=65
        assert satisfied(first_clauses,ass)
        ass[hs[0]]=not ass[hs[0]]
        assert not satisfied(first_clauses,ass)
        cal.append({'pattern':label,'input_count':k,'exact_sum':got,'high':k>=65,'wrong_high_rejected':True})
    calibration={'status':'PASS_NO_SOLVER','gate_truth_tables':gate_truth,'layer_assignment_cases':len(cal),'cases':cal,
                 'scope':'First fiber exact gate template; all30 fibers generated by same code with shifted keep IDs.'}
    (D/'CALIBRATION.json').write_text(json.dumps(calibration,indent=2)+'\n')

    edges=[]
    for u in range(30):
        for p,v in enumerate(C[u]):
            if u<v and not(set(C[u])&set(C[v])):edges.append((u,v,p))
    assert len(edges)==30
    rows=[];edgeinfo=[]
    def equiv(a,b,guard):
        rows.append([*guard,-a,b]);rows.append([*guard,a,-b])
    for u,v,p in edges:
        cl0=len(rows);guard=[-hs[u],-hs[v]]
        for a,direction in [(u,p),(v,inv[p])]:
            lines=sorted({tuple(sorted(line(x,ell[direction]),key=code)) for x in pts},key=lambda z:code(z[0]))
            assert len(lines)==25 and all(len(z)==5 for z in lines)
            for ll in lines:
                for x in ll[1:]:equiv(keep(a,ll[0]),keep(a,x),guard)
        images={mat(T[p],x) for x in pts};assert len(images)==125
        for x in pts:equiv(keep(u,x),keep(v,mat(T[p],x)),guard)
        assert len(rows)-cl0==650
        edgeinfo.append({'u':u,'v':v,'source_port':p,'target_port':inv[p],'high_variables':[hs[u],hs[v]],'clauses':650})
    fragment('h65_edges.added.cnf',rows,flags_nv)
    fragment('exists_high.added.cnf',[hs],flags_nv)
    fragment('not_all_high.added.cnf',[[-h for h in hs]],flags_nv)
    elapsed=time.process_time()-start;assert elapsed<10
    model={'status':'PREPARED_NOT_SOLVED','parent_variable_max':OLD_MAX,'keep_variables_unchanged':[1,3750],
           'first_new_variable':OLD_MAX+1,'last_new_variable':flags_nv,'new_variables':flags_nv-OLD_MAX,
           'high_variables':hs,'high_definition':'h_a iff exact retained count in fiber a >=65',
           'layers':layers,'undirected_external_edges':edgeinfo,
           'fragments':{'high_flags.added.cnf':{'clauses':flags_nc,'role':'All exact sum gates, comparators and30 h iff bindings'},
                        'h65_edges.added.cnf':{'clauses':len(rows),'role':'Conditional source/target line saturation and T_p transport'},
                        'exists_high.added.cnf':{'clauses':1,'role':'Requires total retained order>=1921; otherwise omit'},
                        'not_all_high.added.cnf':{'clauses':1,'role':'Requires saved all-high impossibility proof; otherwise omit'}},
           'total_new_clauses_if_all_fragments_used':flags_nc+len(rows)+2,
           'calibration':'CALIBRATION.json','CPU_seconds':elapsed,'CPU_budget_seconds':10,'workers':1,
           'solver_calls':0,'source_graph_BFS':0,'source_edge_table_reads':0,'new_graphs':0,
           'merge_note':'Fresh range starts after315221. Another independently prepared increment may use the same fresh IDs; rebase its non-keep variables before merging, never concatenate colliding ranges.'}
    (D/'MODEL.json').write_text(json.dumps(model,indent=2)+'\n')
    (D/'TERMINAL.json').write_text(json.dumps({'running':False,'status':'PREPARED_NOT_SOLVED','CPU_seconds':elapsed,'solver_calls':0},indent=2)+'\n')
    print(json.dumps({k:model[k] for k in ['status','first_new_variable','last_new_variable','new_variables','fragments','total_new_clauses_if_all_fragments_used','CPU_seconds']}))
if __name__=='__main__':main()
