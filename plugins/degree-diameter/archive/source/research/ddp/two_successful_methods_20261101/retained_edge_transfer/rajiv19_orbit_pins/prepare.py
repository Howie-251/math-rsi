#!/usr/bin/env python3
"""Build source once in author PG labels; compare explicit radius2 pin rules.
No source-diameter BFS, solver, hash, or execution of author check_fibre.
"""
import itertools
import json
import time
from collections import Counter
from pathlib import Path

HERE=Path(__file__).resolve().parent
PRIMARY=HERE.parent.parent/'public_baseline_audit/degree19_source_primary'
Q=11

def canon(v):
    z=next(a for a in v if a)
    iz=pow(z,-1,Q)
    return tuple(a*iz%Q for a in v)

def transvection(line,l):
    return frozenset(canon(((v[0]+l*v[1])%Q,v[1],v[2],v[3])) for v in line)

def dump(name,data):
    (HERE/name).write_text(json.dumps(data,indent=2)+'\n')

def main():
    start=time.process_time()
    assert (HERE/'PRED.json').exists()
    W=json.loads((PRIMARY/'fq_d19_k3_n2783.json').read_text())
    assert W['q']==Q and W['X']==[2,4,5,6,7,9] and W['Xp']==[1,3,8,10]
    # Read only mathematical parameters, omitting inherited checksum fields.
    dump('SOURCE_PARAMETERS.json',{k:W[k] for k in ['construction','d','k','n','q','field','X','Xp','t','gadget']})
    affine=sorted(canon((a,1,b,c)) for a,b,c in itertools.product(range(Q),repeat=3))
    assert len(set(affine))==Q**3
    pid={p:i for i,p in enumerate(affine)}
    coord_pid={(a,b,c):pid[canon((a,1,b,c))] for a,b,c in itertools.product(range(Q),repeat=3)}
    directions=[(1,k) for k in range(Q)]+[(0,1)]
    inf=(1,0,0,0)
    raw_lines={}
    for w,(s,t) in enumerate(directions):
        for h,l in itertools.product(range(Q),repeat=2):
            m=canon((h,0,s,t))
            if s:
                ps=[canon(((l+h*z)%Q,1,z,(t*z-h)%Q)) for z in range(Q)]
            else:
                ps=[canon(((l+h*z)%Q,1,h,z)) for z in range(Q)]
            raw_lines[w,h,l]=frozenset([m,*ps])
    lines=sorted(set(raw_lines.values()),key=lambda s:sorted(s))
    assert len(lines)==Q**2*(Q+1)==1452
    assert all(len(s)==12 and inf not in s for s in lines)
    lid={s:1331+i for i,s in enumerate(lines)}
    # The following sorting is exactly fibre_build's Ms/pencils/base/z convention.
    Ms={w:frozenset([inf,*(canon((h,0,s,t)) for h in range(Q))]) for w,(s,t) in enumerate(directions)}
    class_order=sorted(range(Q+1),key=lambda w:sorted(Ms[w]))
    beta=[]; beta_info=[]; line_owner={}
    for i,w in enumerate(class_order):
        s,t=directions[w]
        hs=sorted(range(Q),key=lambda h:canon((h,0,s,t)))
        row=[];info=[]
        for a,h in enumerate(hs):
            base=min((raw_lines[w,h,l] for l in range(Q)),key=lambda s:sorted(s))
            for l in range(Q):
                line=transvection(base,l);v=a*Q+l;j=lid[line]
                row.append(j);line_owner[j]=(i,v)
            info.append({'pencil_index':a,'m':canon((h,0,s,t)),'coordinate_h':h,'base_global_line':lid[base]})
        assert len(set(row))==121
        beta.append(row);beta_info.append({'class':i,'coordinate_direction':[s,t],'pencils':info})
    assert len(line_owner)==1452
    gn=[set() for _ in range(121)]
    for a,b in W['gadget']:
        assert a!=b and a//Q!=b//Q
        gn[a].add(b);gn[b].add(a)
    assert all(len(s)==4 for s in gn)
    kn=[set(s) for s in gn]
    for a,l in itertools.product(range(Q),repeat=2):
        for x in W['Xp']:kn[a*Q+l].add(a*Q+(l+x)%Q)
    assert all(len(s)==8 for s in kn)
    nb=[set() for _ in range(2783)]
    def edge(a,b):
        assert a!=b;nb[a].add(b);nb[b].add(a)
    for line,j in lid.items():
        for p in line:
            if p in pid:edge(pid[p],j)
    for (a,b,c),v in coord_pid.items():
        for x in W['X']:edge(v,coord_pid[(a+x)%Q,b,c])
    for row in beta:
        for v in range(121):
            for u in kn[v]:edge(row[v],row[u])
    assert all(len(nb[v])==18 for v in range(1331))
    assert all(len(nb[v])==19 for v in range(1331,2783))
    edges=[(v,u) for v in range(2783) for u in sorted(nb[v]) if v<u]
    assert len(edges)==25773
    with (HERE/'source_d19_D3_n2783.edges').open('w') as f:
        f.write('2783 25773\n')
        for v,u in edges:f.write(f'{v} {u}\n')
    dump('SOURCE_GEOMETRY.json',{'author_point_PG_labels':affine,'beta_global_line_labels':beta,'class_pencil_bases':beta_info,'label_bridge':'All normalized affine PG points and all1452 explicit isotropic noninf lines, each sorted exactly as author fibre_build; same sorted Ms,pencil intersections,lexminbase and z_l.'})
    pp=set(range(1331));ll=set(range(1331,2783))
    def radius2(pins):
        out=set(pins)
        for v in pins:
            out.update(nb[v])
            for w in nb[v]:out.update(nb[w])
        return out
    # Actual general point-to-lines provider formula, checked against adjacency.
    point_line=[]
    for p in range(1331):
        incident=[v for v in nb[p] if v>=1331]
        assert len(incident)==12
        slots=[None]*12;formula=set()
        for j in incident:
            i,v=line_owner[j];slots[i]=v
            formula.update(beta[i][u] for u in range((v//Q)*Q,(v//Q+1)*Q))
            formula.update(beta[i][u] for u in gn[v])
        actual=radius2([p])&ll
        assert formula==actual
        assert len(actual)==180
        point_line.append(slots)
    orbit=sorted(coord_pid[a,0,0] for a in range(Q))
    exceptional_class=0;fixed_vertex=0;L0=beta[0][0]
    line_pins=sorted(nb[L0]&pp)
    assert len(line_pins)==11
    comparison=[]
    for name,pins in [('transvection_orbit',orbit),('one_W_line',line_pins)]:
        r=radius2(pins);classcov=[]
        for i,row in enumerate(beta):
            covered=sorted(v for v,j in enumerate(row) if j in r)
            classcov.append({'class':i,'covered':len(covered),'missing':121-len(covered),'covered_K_vertices':covered,'pin_incident_K_vertices':sorted({point_line[p][i] for p in pins})})
        comparison.append({'rule':name,'pins':pins,'point_targets_covered':len(r&pp),'line_targets_covered':len(r&ll),'line_targets_missing':len(ll-r),'classes':classcov})
    assert comparison[0]['point_targets_covered']==1331
    assert comparison[1]['point_targets_covered']==1331
    assert [c['covered'] for c in comparison[1]['classes']]==[15]+[121]*11
    dump('CONTROLLED_COMPARISON.json',{'predictions_supported':True,'actual_general_point_provider_checks':1331,'each_point_line_provider_cardinality':180,'gadget_external_degree':4,'class_K_degree':8,'comparisons':comparison,'one_W_line_source_vertex':L0,'one_W_line_affine_coordinates':[[next(x for x in coord_pid if coord_pid[x]==p),p] for p in line_pins]})
    providers=[set(range((v//Q)*Q,(v//Q+1)*Q))|gn[v] for v in range(121)]
    fixed=providers[0]
    # If <=8 extra classline providers are chosen, at least2 of the other10
    # pencils remain unchosen. Their22 vertices can only be covered by gadget
    # edges from vertex0 and the8 chosen additional vertices. Bound that count.
    pairbounds=[]
    for a,b in itertools.combinations(range(1,11),2):
        omitted=set(range(11*a,11*(a+1)))|set(range(11*b,11*(b+1)))
        fixed_count=len(gn[0]&omitted)
        contributions=sorted([(len(gn[v]&omitted),v) for v in range(1,121) if v//Q not in (a,b)],reverse=True)
        top=contributions[:8]
        upper=fixed_count+sum(c for c,v in top)
        pairbounds.append({'omitted_pencils':[a,b],'targets':22,'fixed_gadget_contribution':fixed_count,'top8_optimistic_contributions':top,'coverage_upper':upper,'strictly_below22':upper<22})
    survivors=[x for x in pairbounds if not x['strictly_below22']]
    dump('OMITTED_PENCIL_CAPACITY.json',{'fixed_K_vertex':0,'extra_budget':8,'all45_omitted_pencil_pairs':pairbounds,'all_pairs_strictly_excluded':not survivors,'surviving_pairs':survivors,'maximum_optimistic_coverage':max(x['coverage_upper'] for x in pairbounds)})
    dump('CLASS_COVER_INPUT.json',{'fixed_vertex':0,'extra_budget':8,'providers':[sorted(s) for s in providers],'fixed_covered':sorted(fixed),'remaining_targets':sorted(set(range(121))-fixed),'columns':list(range(1,121)),'beta_exceptional':beta[0],'point_pin_candidates_for_each_K_vertex':[sorted(nb[beta[0][v]]&pp) for v in range(121)],'fixed_point_pins':line_pins})
    result={'status':'FIXED_ONE_WLINE_PLUS8_EXCLUDED_BY_CAPACITY' if not survivors else 'POINT_PREDICTIONS_PASS_CLASS_COVER_GATE_OPEN','source_n':2783,'source_m':25773,'point_degree':18,'line_degree':19,'source_diameter':'inherited publicTheorem1/source, not rerun','source_BFS_roots':0,'source_generated_once':True,'actual_point_provider_checks':1331,'orbit_line_coverage':comparison[0]['line_targets_covered'],'orbit_line_missing':comparison[0]['line_targets_missing'],'one_Wline_line_coverage':comparison[1]['line_targets_covered'],'one_Wline_line_missing':comparison[1]['line_targets_missing'],'exceptional_class':0,'fixed_K_vertex':0,'omitted_pairs_excluded':45-len(survivors),'omitted_pair_survivors':len(survivors),'pair_capacity_max':max(x['coverage_upper'] for x in pairbounds),'solver_calls':0,'new_graphs':0,'CPU_seconds':time.process_time()-start,'budget_CPU_seconds':60,'source_edges_label_bridge':'exact author PG canonical and beta convention; no foreign verifier entrypoint executed'}
    dump('PREPROCESS_RESULT.json',result)
    print(json.dumps(result))

if __name__=='__main__':main()
