import json
from pathlib import Path

SCOPE = Path(__file__).resolve().parent
source_controller = json.loads((SCOPE.parent/'PARAMETERS.json').read_text())
source_chart = json.loads((SCOPE/'../../r6_f9_projective_halves/cross_port_extension/PARAMETERS.json').read_text())
source_routes = json.loads((SCOPE.parent/'CONTROLLER_ROUTE_CERTIFICATE.json').read_text())
controller = source_controller['controller']
inverse = source_controller['inverse_ports']
directions = source_chart['port_vectors']
names = ['cross_0_1_forward','cross_0_1_reverse','cross_2_3_forward','cross_2_3_reverse',
         'self_4_plus','self_4_minus','self_5_plus','self_5_minus']
by_id = {c['chart_id']:c for c in source_chart['charts']}
charts = [by_id[name] for name in names]
indices = {name:i for i,name in enumerate(names)}
chart_inverse = [indices[c['inverse_chart_id']] for c in charts]
dart_charts = []
for u,row in enumerate(controller):
    dart_row = []
    for p,v in enumerate(row):
        q = inverse[p]
        if p<q: name=f'cross_{p}_{q}_forward'
        elif p>q: name=f'cross_{q}_{p}_reverse'
        else: name=f'self_{p}_'+('plus' if u<v else 'minus')
        dart_row.append(indices[name])
    dart_charts.append(dart_row)
assert set(k for row in dart_charts for k in row)==set(range(8))
for u,row in enumerate(controller):
    for p,v in enumerate(row):
        assert controller[v][inverse[p]] == u
        assert dart_charts[v][inverse[p]] == chart_inverse[dart_charts[u][p]]

def add(a,b): return (a%3+b%3)%3+3*((a//3+b//3)%3)
def neg(a): return (-a%3)+3*(-(a//3)%3)
def mul(a,b):
    x,y=a%3,a//3; z,w=b%3,b//3
    return (x*z-y*w)%3+3*((x*w+y*z)%3)
def dot(a,b):
    r=0
    for x,y in zip(a,b): r=add(r,mul(x,y))
    return r
def mv(M,v): return [dot(row,v) for row in M]
def mm(A,B): return [[dot(row,col) for col in zip(*B)] for row in A]
def cross(a,b): return [add(mul(a[1],b[2]),neg(mul(a[2],b[1]))),
                        add(mul(a[2],b[0]),neg(mul(a[0],b[2]))),
                        add(mul(a[0],b[1]),neg(mul(a[1],b[0])))]
def det(a,b,c): return dot(cross(a,b),c)
def vector_label(v): return v[0]+9*v[1]+81*v[2]
def normalize(v):
    x=next(x for x in v if x)
    inverse_x=next(y for y in range(1,9) if mul(x,y)==1)
    return tuple(mul(y,inverse_x) for y in v)
identity = [[1,0,0],[0,1,0],[0,0,1]]
cert = []
for k,c in enumerate(charts):
    p,q,M = c['source_port'],c['target_port'],c['matrix']
    Mi = charts[chart_inverse[k]]['matrix']
    assert mm(M,Mi) == mm(Mi,M) == identity
    assert mv(M,directions[p]) == directions[q]
    turns=[]
    for i in range(6):
        if i==p: continue
        for j in range(6):
            if j==q: continue
            value=det(mv(M,directions[i]),directions[q],directions[j])
            assert value
            turns.append({'source_outer_port':i,'target_outer_port':j,'determinant':value})
    planes = [(mv(M,directions[i]),directions[q]) for i in range(6) if i!=p]
    planes += [(directions[q],directions[j]) for j in range(6) if j!=q]
    normals = [normalize(cross(a,b)) for a,b in planes]
    assert len(set(normals))==10
    cover=set()
    for a,b in planes:
        plane={vector_label([add(mul(x,ai),mul(y,bi)) for ai,bi in zip(a,b)]) for x in range(9) for y in range(9)}
        assert len(plane)==81
        cover |= plane
    assert len(cover)==729
    cert.append({'chart_id':c['chart_id'],'source_port':p,'target_port':q,
                 'inverse_chart_id':c['inverse_chart_id'],'both_inverse_products_identity':True,
                 'direction_transport_exact':True,'turns':turns,'pencil_plane_normals':normals,
                 'pencil_distinct_planes':10,'pencil_union_vectors':729})
(SCOPE/'ACTUAL_LOCAL_CHART_CERTIFICATE.json').write_text(json.dumps({'selected_charts':8,'actual_turns':200,
    'charts':cert,'all_checks_pass':True},ensure_ascii=False,indent=2)+'\n')
parameters = {
    'field':source_chart['field'],'fiber_dimension':3,'fiber_size':729,
    'controller_order':78,'controller':controller,'ports':source_controller['ports'],'inverse_ports':inverse,
    'controller_parameters':{k:source_controller[k] for k in ['alpha0','alpha1','alpha2','sigma','tau','self_matching_shift']},
    'controller_framework_author':source_controller['controller_framework_author'],
    'controller_framework_source':'../PARAMETERS.json','controller_current_contribution':source_controller['current_change'],
    'directions':directions,'conic_parameters':source_chart['port_parameters'],
    'chart_ids':names,'matrices':[c['matrix'] for c in charts],
    'chart_source_ports':[c['source_port'] for c in charts],'chart_target_ports':[c['target_port'] for c in charts],
    'inverse_charts':chart_inverse,'dart_chart_index':dart_charts,
    'chart_source':'../../r6_f9_projective_halves/cross_port_extension/PARAMETERS.json',
    'dart_chart_rule':'p<q:cross_p_q_forward; p>q:cross_q_p_reverse; p=q:u<v self_p_plus else self_p_minus; q=inverse_ports[p]',
    'vertex_label':'729*u+x0+9*x1+81*x2',
    'edge_rule':'(u,x)~(controller[u][p], matrices[dart_chart_index[u][p]]*x+t*directions[inverse_ports[p]]), t in F9',
    'order':56862,'degree':54,'expected_edges':1535274,
    'edge_file':'graph_d54_D3_n56862.edges','edge_file_format':'No header; a b with a<b, globally lexicographically sorted, each edge once.',
    'local_certificate':'ACTUAL_LOCAL_CHART_CERTIFICATE.json',
    'controller_route_certificate':'../CONTROLLER_ROUTE_CERTIFICATE.json',
    'all_pairs_proof':'PROOF.md','global_record_claim':False,'Lean_complete_here':False,
    'public_degree54_best_located':55350,
    'no_fiber_translation_automorphism_assumed':True,
}
(SCOPE/'PARAMETERS.json').write_text(json.dumps(parameters,ensure_ascii=False,indent=2)+'\n')
routes = [[[0]*3 for target in range(78)] for c in range(3)]
for w in source_routes['witnesses']: routes[w['root_base']][w['target_vertex']] = w['ports']
def c_initializer(obj):
    if isinstance(obj,list): return '{'+','.join(c_initializer(v) for v in obj)+'}'
    return str(obj)
header = '#pragma once\n'
for ctype,name,dims,value in [
    ('int','CTRL','[78][6]',controller),('int','INV','[6]',inverse),
    ('int','DIR','[6][3]',directions),('int','MAT','[8][3][3]',parameters['matrices']),
    ('int','CHARTINV','[8]',chart_inverse),('int','SOURCEPORT','[8]',parameters['chart_source_ports']),
    ('int','TARGETPORT','[8]',parameters['chart_target_ports']),('int','DARTCHART','[78][6]',dart_charts),
    ('int','ROUTES','[3][78][3]',routes)]:
    header += 'static const '+ctype+' '+name+dims+'='+c_initializer(value)+';\n'
(SCOPE/'actual_parameters.hpp').write_text(header)
print('PREP_PASS eight actual charts / 200 turns / eight729-vector pencils; PARAMETERS.json ready')
