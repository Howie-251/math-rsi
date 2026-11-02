from pathlib import Path
import json,re,time
start=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());O=R/'formal/DegreeDiameter/Portfolio'
P=json.loads((R/'research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json').read_text())
C,T,L,iv=P['controller'],P['matrices'],P['outgoing_return_directions'],[1,0,3,2]
def flat(x):return sum((flat(y)if isinstance(y,list)else[y]for y in x),[])
def arr(x):return '#['+', '.join(map(str,flat(x)))+']'
def rows(x):return '#['+', '.join(arr(y)for y in x)+']'
def mul(a,b):
    c=0
    while b:
        if b&1:c^=a
        b>>=1;a<<=1
        if a&4:a^=7
    return c
def mv(M,x):return [mul(row[0],x[0])^mul(row[1],x[1])^mul(row[2],x[2])for row in M]
def route(a,ps,ns):
    x=[0,0,0]
    for p,t in zip(ps,ns):
        x=[y^mul(t,l)for y,l in zip(mv(T[a][p],x),L[iv[p]])];a=C[a][p]
    return x
def inverse(M):
    A=[row[:]+[int(i==j)for j in range(3)]for i,row in enumerate(M)]
    for j in range(3):
        k=next(i for i in range(j,3)if A[i][j]);A[j],A[k]=A[k],A[j]
        t=next(t for t in range(1,4)if mul(t,A[j][j])==1);A[j]=[mul(t,x)for x in A[j]]
        for i in range(3):
            if i!=j:
                t=A[i][j];A[i]=[x^mul(t,y)for x,y in zip(A[i],A[j])]
    return [row[3:]for row in A]
def intern(vs):
    pool=[];index=[];seen={}
    for v in vs:
        key=tuple(v)
        if key not in seen:seen[key]=len(pool);pool.append(list(key))
        index.append(seen[key])
    return pool,index
templates={k:(O/f'F4Graph1920Row0{k}.lean').read_text()for k in['Data','Certificate','Walks']}
modules={'Data':[],'Certificate':[],'Walks':[]}
for a in range(1,30):
    words=[0]*30;inverses=[[0]*9 for _ in range(30)];count=0
    for rec in P['pair_certificate']:
        if rec['u']!=a or rec['kind']!='full_rank':continue
        b=rec['v'];ps=rec['word'];words[b]=ps[0]+4*ps[1]+16*ps[2]
        cols=[route(a,ps,[int(i==j)for i in range(3)])for j in range(3)]
        inverses[b]=flat(inverse([list(row)for row in zip(*cols)]));count+=1
    assert count==26
    adj=[]
    for p in range(4):
        out=[None]*64
        for side in range(2):
            for q in range(4):
                ps=[q,iv[q],p]if side==0 else[p,q,iv[q]]
                for n in range(64):
                    v=route(a,ps,[n%4,n//4%4,n//16]);d=v[0]+4*v[1]+16*v[2]
                    if out[d]is None:out[d]=n+64*q+256*side
        assert all(x is not None for x in out);adj.append(out)
    pool,idx=intern(inverses)
    for kind in modules:
        text=templates[kind].replace('F4Graph1920Row0',f'F4Graph1920Row{a}').replace('F4Graph1920.Row0',f'F4Graph1920.Row{a}').replace('row0_full_walk_bound',f'row{a}_full_walk_bound')
        if kind=='Data':
            for name,value in[('wordData',arr(words)),('inversePool',rows(pool)),('inverseIndex',arr(idx)),('adjacentData',rows(adj))]:
                text,n=re.subn(r'^(def '+name+r'[^\n]*:= )[^\n]*',lambda m:m.group(1)+value,text,flags=re.M);assert n==1
        else:
            for function in['controller','routeController','routeVec','route_before_center','route_after_center','stepVec','liftAt']:
                text=text.replace(function+' 0 ',function+f' {a} ')
        name=f'F4Graph1920Row{a}{kind}';path=O/(name+'.lean');assert not path.exists();path.write_text(text);modules[kind].append(name)
record=dict(status='REMAINING29_ROW_LITERAL_WITNESSES_AND_MODULES_PREPARED',CPU_seconds=time.process_time()-start,
    phases=modules,row_count=29,NB_pairs=754,adjacent_darts=116,adjacent_residuals=7424,
    old_modules_or_passed_pilot_modified=False,old_graph_BFS_rank_verifier_solver_runs=0,
    coefficient_preparation='New decoder witnesses for29literal rows; kernel equations still require new module PASS')
(D/'FULL_PREPARATION_RESULT.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(dict(status=record['status'],CPU_seconds=record['CPU_seconds'],new_modules=87)))
