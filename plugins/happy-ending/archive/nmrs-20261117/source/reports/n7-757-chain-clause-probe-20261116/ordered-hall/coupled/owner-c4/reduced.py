"""Fresh reduced encoding: occupancy, one red matching and owner intervals only."""
from run import *
import sys

def main():
    bare='--bare' in sys.argv
    name='reduced-bare' if bare else 'reduced'
    d=HERE/name;d.mkdir(exist_ok=True)
    source=HERE.parents[2]/'projected/relaxation.cnf';clauses=[]
    with source.open() as f:
        header=next(f).split();top=int(header[2])
        for line in f:clauses.append(list(map(int,line.split()[:-1])))
    if bare:clauses=clauses[456:] # exactly original 336 chain bans + 120 ordinary row clauses
    groups={'inherited_occupancy':len(clauses)}
    def fresh():
        nonlocal top
        top+=1;return top
    def add(name,rows):
        rows=list(rows);clauses.extend(rows);groups[name]=groups.get(name,0)+len(rows)
    def card(lits,bound,equal,name):
        nonlocal top
        enc=(CardEnc.equals if equal else CardEnc.atleast)(lits,bound,top_id=top,encoding=EncType.seqcounter)
        top=max(top,enc.nv);add(name,enc.clauses)
    cells=[{(x+1,y) for x,h in enumerate((w[2]-3,w[1]-2,w[0]-1)) for y in range(1,h+1)} for w in W]
    cs=[i for i,w in enumerate(W) if 1 in w and 8 in w]
    oa={IX[(1,u,7)]-1 for u in range(2,7)};ob={IX[(2,v,8)]-1 for v in range(3,8)}
    card([c+1 for c in cs],4,True,'exactly_four_C')
    card([u+1 for u in sorted(oa)],1,True,'exactly_one_A_owner')
    card([v+1 for v in sorted(ob)],1,True,'exactly_one_B_owner')
    order={(u,v):fresh() for u,v in it.combinations(range(56),2)}
    def before(u,v):return order[u,v] if u<v else -order[v,u]
    add('total_physical_order',(row for a,b,c in it.combinations(range(56),3) for row in ([-before(a,b),-before(b,c),before(a,c)],[before(a,b),before(b,c),-before(a,c)])))
    add('ideal_inclusion',([before(u,v)] for u in range(56) for v in range(56) if cells[u]<cells[v]))
    left=[u for u,w in enumerate(W) if 1 in w and 8 not in w];right=[v for v,w in enumerate(W) if 8 in w and 1 not in w]
    edges=[];incident={u:[] for u in left+right}
    for u in left:
        for v in right:
            diff=cells[v]-cells[u]
            if not diff:continue
            z=fresh();edges.append({'u':u,'v':v,'variable':z});incident[u].append(z);incident[v].append(z)
            add('one_red_matching_edge',[[-z,u+1],[-z,v+1],[-z,before(u,v)]])
            if (u in oa and (1,5) not in diff) or (v in ob and (3,1) not in diff) or (u in oa and v in ob):
                add('owner_exact_cell_consistency',[[-z]])
    for u in left+right:
        add('one_red_matching_coverage',[[-(u+1)]+incident[u]])
        enc=CardEnc.atmost(incident[u],1,top_id=top,encoding=EncType.seqcounter)
        top=max(top,enc.nv);add('one_red_matching_at_most_one',enc.clauses)
    ae=[e for e in edges if e['u'] in oa];be=[e for e in edges if e['v'] in ob]
    for a in ae:
        for b in be:
            if {a['u'],a['v']}&{b['u'],b['v']}:row=[-a['variable'],-b['variable']]
            else:row=[-a['variable'],-b['variable'],before(a['v'],b['u']),before(b['v'],a['u'])]
            add('two_owner_closed_intervals_disjoint',[row])
    for e in {e['variable']:e for e in ae+be}.values():
        u,v,z=e['u'],e['v'],e['variable']
        add('each_C_outside_each_owner_interval',([-z,-(c+1),before(c,u),before(v,c)] for c in cs))
        inside=[]
        for w in range(56):
            if w in (u,v):continue
            h=fresh();inside.append(h);a,b=before(u,w),before(w,v)
            add('inside_occupied_gate',[[-h,w+1],[-h,a],[-h,b],[h,-(w+1),-a,-b]])
        enc=CardEnc.atleast(inside,4,top_id=top,encoding=EncType.seqcounter)
        top=max(top,enc.nv);add('owner_interval_at_least_six',([-z]+row for row in enc.clauses))
    dump(d/'ledger.json',{'bare':bare,'nvars':top,'nclauses':len(clauses),'groups':groups,'red_matching_edges':edges,'order_variables':[{'u':u,'v':v,'variable':z} for (u,v),z in order.items()],'A_owner_states':[W[u] for u in sorted(oa)],'B_owner_states':[W[v] for v in sorted(ob)],'removed_entirely':['all blue matchings','endpoint DAG','shared multicolor pair labels','27 other red matchings','boundary_pure_source_bounds','first-third role choices','six-representative red-six conditions','cheap two-positive/four-negative units']})
    cnf=d/'formula.cnf'
    with cnf.open('w') as f:
        f.write(f'p cnf {top} {len(clauses)}\n')
        for row in clauses:f.write(' '.join(map(str,row))+' 0\n')
    solved=controlled([SOLVER,str(cnf),str(d/'proof.drat')],d/'solver.log')
    result={'solver':solved,'source_sha256':sha(Path(__file__)),'input_occupancy_cnf_sha256':sha(source),'cnf_sha256':sha(cnf),'accepted':False,'hostname':platform.node(),'nvars':top,'nclauses':len(clauses),'bare':bare}
    if solved['returncode']==20 and not solved['timeout']:
        checked=controlled([CHECKER,str(cnf),str(d/'proof.drat')],d/'checker.log')
        result['checker']=checked;result['proof_sha256']=sha(d/'proof.drat')
        result['status']='CHECKED_UNSAT' if checked['returncode']==0 and 's VERIFIED' in (d/'checker.log').read_text() else 'UNCHECKED_UNSAT'
    elif solved['returncode']==10 and not solved['timeout']:
        model={abs(int(t)):int(t)>0 for line in (d/'solver.log').read_text().splitlines() if line.startswith('v ') for t in line[2:].split() if int(t)}
        assert set(model)==set(range(1,top+1)) and all(any(model[abs(v)]==(v>0) for v in row) for row in clauses)
        def b(u,v):return model[order[u,v]] if u<v else not model[order[v,u]]
        sequence=sorted(range(56),key=lambda v:sum(b(u,v) for u in range(56) if u!=v))
        assert all(b(u,v) for u,v in it.combinations(sequence,2))
        occupied={u for u in range(56) if model[u+1]};assert len(occupied)==40
        assert [sum(k in W[u] for u in occupied) for k in range(1,9)]==[15]*8
        assert len(occupied&set(cs))==4 and len(occupied&oa)==len(occupied&ob)==1
        selected=[e for e in edges if model[e['variable']]];assert len(selected)==11
        assert {e['u'] for e in selected}==occupied&set(left) and {e['v'] for e in selected}==occupied&set(right)
        aedge=next(e for e in selected if e['u'] in oa);bedge=next(e for e in selected if e['v'] in ob)
        ints=[]
        for side,e in [('A',aedge),('B',bedge)]:
            u,v=e['u'],e['v'];inside={w for w in occupied if w in (u,v) or (b(u,w) and b(w,v))}
            assert len(inside)>=6 and not inside&set(cs)
            ints.append({'side':side,'u':W[u],'v':W[v],'occupied_inside':[W[w] for w in sequence if w in inside]})
        assert b(aedge['v'],bedge['u']) or b(bedge['v'],aedge['u'])
        dump(d/'model-audit.json',{'full_56_order':[W[u] for u in sequence],'occupied_order':[W[u] for u in sequence if u in occupied],'red_matching':[{'u':W[e['u']],'v':W[e['v']]} for e in selected],'owner_intervals':ints,'all_clauses_checked':len(clauses),'semantic_audit_passed':True})
        result['status']='SAT_AUDITED_REDUCED_RELAXATION'
    else:result['status']='INCONCLUSIVE'
    dump(d/'result.json',result);print(json.dumps(result),flush=True)
if __name__=='__main__':main()
