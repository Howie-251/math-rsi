"""One new formal module and all25 evaluations. No graph/BFS/solver."""
from pathlib import Path
import json,time
HERE=Path(__file__).resolve().parent
started=time.process_time()
pred=json.loads((HERE/'PREDICTION.json').read_text())
data=json.loads((HERE.parent/'CONTROL_CAPACITY_ROOT.json').read_text())
mt=data['Q8_multiplication']
zero=(0,)*8
def rotate(h,vec):
    out=[0]*8
    for block in (0,4):
        for k in range(4):
            unit=mt[h][k]
            out[block+unit%4] += vec[block+k]*(-1 if unit>=4 else 1)
    return tuple(out)
def negative(v):return tuple(-x for x in v)
rows=[[] for _ in range(5)]
def add_edge(a,b,h,normal):
    inverse=next(t for t in range(8) if mt[h][t]==0)
    rows[a].append((b,h,normal))
    rows[b].append((a,inverse,negative(rotate(inverse,normal))))
for b in [2,3,4]:add_edge(0,b,0,zero)
add_edge(1,4,0,zero)
add_edge(1,2,5,zero)
add_edge(1,3,6,(0,-1,0,0,0,0,0,0))
for b,normal in [
    (2,(1,0,0,0,0,0,0,0)),
    (3,(0,0,0,0,1,0,0,0)),
    (4,(0,1,0,0,0,0,0,0))]:
    rows[b].append((b,4,normal))
assert all(len(r)==3 for r in rows)
raw=[];prefixes=0
def walk(base,h,normal,previous,depth,path):
    global prefixes
    prefixes+=1
    vertex=8*base+h
    if vertex==20:
        raw.append({'length':depth,'controller_path':path,'coefficients':list(normal)})
    if depth==9:return
    for b,g,w in rows[base]:
        nh=mt[h][g]
        if 8*b+nh==previous:continue
        rw=rotate(h,w)
        walk(b,nh,tuple(a+c for a,c in zip(normal,rw)),vertex,depth+1,path+[8*b+nh])
walk(2,0,zero,-1,0,[16])
assert prefixes==1534
assert len(raw)==29
unique=sorted({tuple(r['coefficients']) for r in raw})
formal={'status':'COMPLETE_NEW_FREE_MODULE_ENDPOINTS','formal_module':'R*e1 directsum R*w','basis_order':['e1','i*e1','j*e1','k*e1','w','i*w','j*w','k*w'],'all_NB_prefixes_D9':prefixes,'critical_raw_paths':29,'distinct_formal_endpoints':len(unique),'raw_routes':raw,'distinct_endpoints':[list(x) for x in unique]}
(HERE/'FORMAL_ENDPOINTS.json').write_text(json.dumps(formal,indent=2)+'\n')
I=((1,0),(0,1));ii=((0,1),(4,0));jj=((0,2),(2,0))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%5 for j in range(2)) for i in range(2))
kk=mm(ii,jj)
basis=[I,ii,jj,kk]
def eval_coeffs(c,w):
    out=[0,0]
    for block,vector in [(0,(1,0)),(4,w)]:
        for k,A in enumerate(basis):
            for row in range(2):
                out[row] += c[block+k]*sum(A[row][j]*vector[j] for j in range(2))
    return tuple(x%5 for x in out)
evaluations=[]
for x in range(5):
    for y in range(5):
        image=sorted({eval_coeffs(c,(x,y)) for c in unique})
        evaluations.append({'w':[x,y],'image_cardinality':len(image),'image':[list(v) for v in image],'missing':[[a,b] for a in range(5) for b in range(5) if (a,b) not in image]})
passers=[r['w'] for r in evaluations if r['image_cardinality']==25]
maximum=max(r['image_cardinality'] for r in evaluations)
result={'status':'COMPLETE25_GATES_PASSERS_NOT_GRAPH_VERIFIED' if passers else 'COMPLETE25_GATES_NO_PASSER_FIXED_RULE_CLOSED',
        'prediction_result':'SUPPORTED' if passers else 'REFUTED','critical_raw_paths':29,'distinct_free_module_endpoints':len(unique),'evaluated_w':25,'max_image':maximum,'required_image':25,'passers':passers,'passer_count':len(passers),'image_cardinalities_lex_w':[r['image_cardinality'] for r in evaluations],'formal_coefficients_per_endpoint':8,'actual_graph_n':None,'actual_D':None,'ordinary_bad_unordered_pairs':None,'new_graphs':0,'BFS':0,'solver_runs':0,'new_formal_word_enumerations':1,'source360_BFS':0,'CPU_seconds':time.process_time()-started,'pending':[]}
(HERE/'EVALUATIONS.json').write_text(json.dumps({'evaluation_scope':'fixedq5representation,all25independentwonly','evaluations':evaluations},indent=2)+'\n')
(HERE/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(HERE/'terminal.json').write_text(json.dumps({'status':result['status'],'running':False,'pending':[],'prediction_result':result['prediction_result'],'passer_count':len(passers),'new_graphs':0,'BFS':0},indent=2)+'\n')
print(json.dumps(result))
