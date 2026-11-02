#!/usr/bin/env python3
"""One fixedGF7/GF49 literalgeometry;no sourcegraph,BFS,solver orhash."""
import itertools
import json
import resource
import time
from pathlib import Path
OUT=Path(__file__).resolve().parent
Q=7

def write(name,value):(OUT/name).write_text(json.dumps(value,indent=2)+'\n')
def canon(v):
    z=next(x for x in v if x);iz=pow(z,-1,Q)
    return tuple(iz*x%Q for x in v)
def add49(a,b):return ((a%7+b%7)%7)+7*((a//7+b//7)%7)
def sub49(a,b):return ((a%7-b%7)%7)+7*((a//7-b//7)%7)
def mul49(a,b):
    a0,a1=a%7,a//7;b0,b1=b%7,b//7
    return ((a0*b0+3*a1*b1)%7)+7*((a0*b1+a1*b0)%7)
def power49(a,n):
    out=1
    while n:
        if n&1:out=mul49(out,a)
        a=mul49(a,a);n>>=1
    return out
def B(x,y):return 2*(x[0]*y[2]+3*x[1]*y[3]-x[2]*y[0]-3*x[3]*y[1])%7
def trace_B(x,y):
    a=x[0]+7*x[1];b=x[2]+7*x[3];c=y[0]+7*y[1];d=y[2]+7*y[3]
    return 2*(sub49(mul49(a,d),mul49(b,c))%7)%7

def main():
    resource.setrlimit(resource.RLIMIT_CPU,(120,120));start=time.process_time()
    assert (OUT/'PRED.json').exists()
    assert not(OUT/'PARAMETERS.json').exists(),'fixedgeometry alreadyexists;do not regenerate'
    assert 3 not in {a*a%7 for a in range(7)}
    add=[[add49(a,b) for b in range(49)] for a in range(49)]
    mult=[[mul49(a,b) for b in range(49)] for a in range(49)]
    inverse=[None]+[next(b for b in range(1,49) if mult[a][b]==1) for a in range(1,49)]
    trace=[]
    for a in range(49):
        tr=add49(a,power49(a,7));assert tr==(2*(a%7))%7;trace.append(tr)
    assert mul49(7,7)==3
    write('FIELD_TABLES.json',{'GF7_add':[[((a+b)%7) for b in range(7)] for a in range(7)],'GF7_mul':[[a*b%7 for b in range(7)] for a in range(7)],'GF7_neg':[(-a)%7 for a in range(7)],'GF7_inv':[None]+[pow(a,-1,7) for a in range(1,7)],'GF49_encoding':'a0+7*a1 represents a0+a1*beta','GF49_polynomial':'beta^2-3','three_is_nonsquare_GF7':True,'GF49_add':add,'GF49_mul':mult,'GF49_inv':inverse,'relative_trace':trace,'relative_trace_formula':'2*constantcoefficient','trace_all49_power7_checked':True})
    points=[v for v in itertools.product(range(7),repeat=4) if any(v) and canon(v)==v]
    assert len(points)==400
    pid={v:i for i,v in enumerate(points)}
    assert all(B(x,x)==0 for x in itertools.product(range(7),repeat=4))
    gram=[[B(tuple(int(k==i) for k in range(4)),tuple(int(k==j) for k in range(4))) for j in range(4)] for i in range(4)]
    det=0
    for perm in itertools.permutations(range(4)):
        parity=sum(perm[i]>perm[j] for i in range(4) for j in range(i+1,4))%2
        term=1
        for i in range(4):term=term*gram[i][perm[i]]%7
        det+=(1 if parity==0 else -1)*term
    assert det%7==4
    linegens={};orthogonal_pairs=set()
    for p,x in enumerate(points):
        for q in range(p+1,400):
            y=points[q];val=B(x,y);assert val==trace_B(x,y)
            if val:continue
            orthogonal_pairs.add((p,q))
            span={p,q}
            for t in range(1,7):span.add(pid[canon(tuple((a+t*b)%7 for a,b in zip(x,y)))])
            ids=tuple(sorted(span));assert len(ids)==8
            linegens.setdefault(ids,[p,q])
    lines=sorted(linegens)
    assert len(lines)==400
    lid={line:i for i,line in enumerate(lines)}
    pl=[[] for _ in range(400)];pairline={}
    for l,ids in enumerate(lines):
        for p in ids:pl[p].append(l)
        for p,q in itertools.combinations(ids,2):
            assert (p,q) not in pairline
            assert B(points[p],points[q])==0
            pairline[p,q]=l
    assert all(len(v)==8 for v in pl) and set(pairline)==orthogonal_pairs and len(pairline)==11200
    max_intersection=max(len(set(lines[i])&set(lines[j])) for i in range(400) for j in range(i+1,400))
    assert max_intersection==1
    rows=[];projection=[[None]*400 for _ in range(400)];indices=[]
    for p in range(400):
        ir=[]
        for l,ids in enumerate(lines):
            if p in ids:q=p;m=l
            else:
                qs=[q for q in ids if B(points[p],points[q])==0]
                assert len(qs)==1;q=qs[0];m=pairline[tuple(sorted((p,q)))]
                rows.append([p,l,q,m]);projection[p][l]=q
            index=[ids.index(q),pl[p].index(m),lines[m].index(q)]
            assert lines[l][index[0]]==q and pl[p][index[1]]==m and lines[m][index[2]]==q
            ir.append(index)
        indices.append(ir)
    assert len(rows)==156800
    spread=[];owners=[None]*400
    for slope in range(50):
        if slope<49:
            m0,m1=slope%7,slope//7
            x=(1,0,m0,m1);y=(0,1,3*m1%7,m0)
            pair=[m0,m1]
        else:x=(0,0,1,0);y=(0,0,0,1);pair=None
        assert B(x,y)==0
        ids={pid[canon(x)],pid[canon(y)]}
        for t in range(1,7):ids.add(pid[canon(tuple((a+t*b)%7 for a,b in zip(x,y)))])
        ids=tuple(sorted(ids));assert len(ids)==8;l=lid[ids]
        for p in ids:assert owners[p] is None;owners[p]=slope
        spread.append({'index':slope,'slope_code':slope if slope<49 else 'infinity','slope_pair':pair,'line_id':l,'points':ids})
    assert all(owner is not None for owner in owners)
    assert len({s['line_id'] for s in spread})==50
    labels=[s['line_id'] for s in spread]
    parameters={'stage':'GEOMETRY_COMPLETE_FIXED160050_PRODUCTION_AUTHORIZED','GF7':'primefield ordinarymod7','GF49':'GF7[beta]/(beta^2-3),codea0+7a1','point_coordinates':'(u0,u1,v0,v1),u=u0+u1beta,v=v0+v1beta','point_normalization':'firstnonzero coordinate1,lexicographic tuples,pointIDs0..399','points':points,'alternating_form':'Tr(u*vprime-v*uprime),Tr(z)=2*constantcoefficient','alternating_form_matrix':gram,'line_label_rule':'ascending lexicographic8pointIDtuple','lines':[{'line':l,'points':ids,'generating_point_pair':linegens[ids]} for l,ids in enumerate(lines)],'point_incident_lines':pl,'spread':spread,'spread_line_labels':labels,'point_spread_owner':owners,'old_vertex_label':'400*p+l','old_adjacency':'distinct(p,l),(q,m)withpincidentm andqincidentl','new_vertex_label':'160000+j fororiginalslopespreadindexj','new_pins':'all64incidentflags400*p+l withpointonspreadlinej','ordered_pins_rule':'spreadpointsascending,eachpoint_incident_linesascending;keep50slopeorder','edge_table_rule':'strictlyascendingu<v andlexicographicsortedlines','source_order':160000,'source_expected_edges':5118400,'order':160050,'degree':64,'expected_edges':5121600,'scope':'Onefixedoddprime7geometry/orderedGF49slopespread;notgeneralqfamilyorotherqcandidate','public_comparison_reference':'../../public_baseline_audit/DEGREE64_SPREAD_TARGET_GATE_20261101.md','global_record_claim':False}
    write('PARAMETERS.json',parameters)
    write('PROJECTION_WITNESSES.json',{'columns':['point_p','line_l','projected_point_q','joining_line_m'],'rows':rows,'point_line_projection_table':projection,'incident_entries':None})
    write('PROJECTION_INDEX_INPUTS.json',{'point_rows':indices,'indices':'qindexonl,mindexamongthroughp,qindexonm;incidentcaseq=p,m=l','all160000_original_point_line_pairs':True})
    with (OUT/'TABLES_INPUT.txt').open('w') as f:
        f.write('400 8 50\n')
        for ids in lines:f.write(' '.join(map(str,ids))+'\n')
        for ids in pl:f.write(' '.join(map(str,ids))+'\n')
        f.write(' '.join(map(str,labels))+'\n')
        f.write(' '.join(map(str,owners))+'\n')
    result={'status':'PASS_COMPLETE_FIXED_GEOMETRY_READY_FOR_PRODUCTION','points':400,'lines':400,'points_per_line':8,'lines_per_point':8,'incidences':3200,'nonincident_point_line_pairs':156800,'unique_projection_checks':156800,'projection_index_triples_all_pairs':160000,'spread_lines':50,'spread_line_labels':labels,'spread_partitions_points':True,'field_checks':{'GF7_prime_arithmetic':True,'GF49_irreducible_polynomial_beta2minus3':True,'GF49_all48_nonzero_inverses_checked':True,'relative_trace_equals_twice_constant_all49':True,'alternating_form_matches_GF49_trace_for_all79800_projectivepairs':True},'alternating_form_all2401_vectors_checked':True,'nondegenerate_Gram_determinant':4,'point_pair_maximum_common_lines':1,'line_pair_maximum_common_points':1,'all_collinear_pairs_match_B_zero':True,'CPU_seconds':time.process_time()-start,'workers':1,'BFS_calls':0,'solver_calls':0,'source_graph_generated':False,'candidate_graph_generated':False}
    write('GQ_AXIOM_CHECK.json',result)
    print(json.dumps(result))

if __name__=='__main__':main()
