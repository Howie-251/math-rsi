"""At most425 actual N-twists, then source semidirect-coordinate recovery."""
from array import array
from pathlib import Path
import json
import resource
import time

START=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(5,5))
OUT=Path(__file__).resolve().parent;BASE=OUT.parent
def ints(path):
    a=array('I');a.frombytes(Path(path).read_bytes());return list(a)
def save(name,data):(OUT/name).write_text(json.dumps(data,indent=2)+'\n')
def stop(status,detail):
    d={'status':status,'detail':detail,'CPU_seconds':time.process_time()-START,'newgraphs':0,'BFS':0,'pending':[]}
    save('RESULT.json',d);save('checkpoint.json',d);print(json.dumps(d));raise SystemExit
def compose(a,b):return [a[x] for x in b]
def inverse(a):
    b=[0]*len(a)
    for i,j in enumerate(a):b[j]=i
    return b
def power(a,k):
    b=[0]*len(a);seen=[False]*len(a)
    for first in range(len(a)):
        if seen[first]:continue
        cyc=[];x=first
        while not seen[x]:seen[x]=True;cyc.append(x);x=a[x]
        assert x==first
        for i,v in enumerate(cyc):b[v]=cyc[(i+k)%len(cyc)]
    return b

gens=json.loads((BASE/'rooted_wl_recovery/six_generators/GENERATORS.json').read_text())
S=[ints(r['map_file']) for r in gens['generators']];n=20400
alpha=S[0];alpha_inv=S[3];beta0=power(S[1],4)
a=ints(BASE/'normal425_cover/a5.pi.u32le.bin')
b=ints(BASE/'normal425_cover/b5.pi.u32le.bin')
z=ints(BASE/'normal425_cover/z17.pi.u32le.bin')
raw=ints(BASE/'normal425_cover/vertex_coordinates.u32le.bin')
oldcoords=[tuple(raw[4*v:4*v+4]) for v in range(n)]
normal0={oldcoords[v][1:]:v for v in range(n) if oldcoords[v][0]==0}
zero_lookup={v:c for c,v in normal0.items()}
assert len(normal0)==425
def Napply(c,v):
    i,j,k=c
    for _ in range(i):v=a[v]
    for _ in range(j):v=b[v]
    for _ in range(k):v=z[v]
    return v

tested=[];selected=None
for idx in range(425):
    c=(idx%5,idx//5%5,idx//25)
    def beta_at(v):return Napply(c,beta0[v])
    q=beta_at(0);order3=q!=0 and beta_at(beta_at(q))==0
    inverted=False
    if order3:inverted=alpha[beta_at(alpha_inv[0])]==beta_at(q)
    tested.append({'index':idx,'N_coordinates':c,'order3':order3,'alpha_inverts':inverted})
    if order3 and inverted:selected=c;break
save('CANDIDATE_TESTS.json',{'scope_max':425,'actual_tested':len(tested),'rows':tested,'first_hit':selected})
if selected is None:stop('UNKNOWN_NO_COMPLEMENT_IN_FIXED425_NTWISTS',{'tested':425})
beta=[Napply(selected,beta0[v]) for v in range(n)];beta_inv=power(beta,2)
assert beta[beta[beta[0]]]==0 and beta[0]!=0
assert alpha[beta[alpha_inv[0]]]==beta_inv[0]
alpha_powers=[power(alpha,v) for v in range(16)]
beta_powers=[list(range(n)),beta,beta_inv]
H=[];Hbycoset={}
for u in range(3):
    for v in range(16):
        q=beta_powers[u][alpha_powers[v][0]];c,i,j,k=oldcoords[q]
        assert c not in Hbycoset
        row={'u':u,'v':v,'identity_image':q,'N_coset':c,'old_N_offset':[i,j,k]}
        H.append(row);Hbycoset[c]=row
if len(Hbycoset)!=48:stop('REFUTED_48_NORMALFORMS_NOT_DISTINCT_NCOSETS',H)

def action(h,hi):
    cols=[]
    for g in [a,b,z]:cols.append(zero_lookup.get(h[g[hi[0]]]))
    assert all(c is not None for c in cols)
    assert cols[0][2]==cols[1][2]==0 and cols[2][0]==cols[2][1]==0
    return {'matrix5':[[cols[0][0],cols[1][0]],[cols[0][1],cols[1][1]]],
            'scalar17':cols[2][2],'conjugate_coordinates':cols}
act_alpha=action(alpha,alpha_inv);act_beta=action(beta,beta_inv)
MA=act_alpha['matrix5'];MB=act_beta['matrix5'];chi=act_alpha['scalar17']
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2))%5 for j in range(2)] for i in range(2)]
I=[[1,0],[0,1]]
mpA=[I]
for _ in range(16):mpA.append(mm(mpA[-1],MA))
mpB=[I,MB,mm(MB,MB)]
assert MB==[[0,4],[1,4]] and mm(mpB[2],MB)==I and mpA[16]==I
assert mm(mm(MA,MB),mpA[15])==mpB[2]
assert act_beta['scalar17']==1
chi_order=next(k for k in range(1,17) if pow(chi,k,17)==1)
assert chi_order==16
save('checkpoint.json',{'status':'ACTUAL_H48_ACTIONS_VERIFIED_SOURCE_COORDINATES_MATCHING',
                       'Ntwists_tested':len(tested),'beta_Ntwist':selected,
                       'alpha_action':act_alpha,'beta_action':act_beta,'H_cosets':48})

def groupcoord(v):
    c,i,j,k=oldcoords[v];h=Hbycoset[c];di,dj,dk=h['old_N_offset']
    return ((i-di)%5,(j-dj)%5,(k-dk)%17,h['u'],h['v'])
coords=[groupcoord(v) for v in range(n)]
lookup={c:v for v,c in enumerate(coords)};assert len(lookup)==n
source=[groupcoord(s[0]) for s in S]
assert source[0]==(0,0,0,0,1)
actions={(u,v):(mm(mpB[u],mpA[v]),pow(chi,v,17)) for u in range(3) for v in range(16)}
def multiply(g,h):
    x,y,c,u,v=g;X,Y,C,U,V=h;M,r=actions[u,v]
    return ((x+M[0][0]*X+M[0][1]*Y)%5,
            (y+M[1][0]*X+M[1][1]*Y)%5,(c+r*C)%17,
            (u+(1 if v%2==0 else -1)*U)%3,(v+V)%16)
for s,inv in enumerate([3,4,5,0,1,2]):assert multiply(source[s],source[inv])==(0,0,0,0,0)
csr=ints(BASE/'rooted_wl_recovery/adjacency.csr.u32le.bin');assert csr[:2]==[20400,122400]
off=csr[2:2+n+1];flat=csr[2+n+1:];arcs=0
for v,g in enumerate(coords):
    predicted=sorted(lookup[multiply(g,s)] for s in source)
    assert predicted==sorted(flat[off[v]:off[v+1]])
    arcs+=6
assert arcs==122400
(OUT/'beta.pi.u32le.bin').write_bytes(array('I',beta).tobytes())
(OUT/'vertex_group_coordinates.u32le.bin').write_bytes(array('I',[x for c in coords for x in c]).tobytes())
source_rows=[{'index':i,'name':['A','B','C','A^-1','B^-1','C^-1'][i],
              'normal5':list(s[:2]),'c17':s[2],'u':s[3],'v':s[4],
              'actual_root_image':S[i][0]} for i,s in enumerate(source)]
recipe={'status':'READY_ACTUAL_SOURCE_SEMIDIRECT_RECIPE','source_n':20400,'source_m':61200,
        'degree':6,'source_reported_D':7,'normal_moduli':[5,5,17],
        'complement_H48':{'alpha_order':16,'beta_order':3,
                         'relation':'alpha beta alpha^-1 = beta^-1',
                         'normalform':'beta^u alpha^v;u mod3,v mod16',
                         'multiplication':'(u,v)*(U,V)=(u+(-1)^v U mod3,v+V mod16)',
                         'beta_N_twist_of_B4':selected,'candidate_count':len(tested),'elements':H},
        'alpha_action':act_alpha,'beta_action':act_beta,'alpha_scalar17_order':chi_order,
        'group_normalform':'n(x,y,c) beta^u alpha^v',
        'multiplication':'(n,h)*(n2,h2)=(n+rho(h)n2,h*h2);rho(beta^u alpha^v) hasmatrix MB^u MA^v onF5^2 andscalar chi_alpha^v onC17',
        'permutation_composition':'Leftaction;rightfactoractsfirst onvertex;sourceCayleysteps are rightmultiplication g*s',
        'positive_generators':source_rows[:3],'all_six_generators':source_rows,
        'inverse_indices':[3,4,5,0,1,2],
        'vertex_coordinate_file':str(OUT/'vertex_group_coordinates.u32le.bin'),
        'vertex_coordinate_layout':'uint32 quintuple(x,y,c,u,v) peroldvertex; x,y mod5,c mod17,u mod3,v mod16',
        'full_source_directed_adjacencies_matched':122400,'full_source_undirected_edges_matched':61200,
        'source_BFS':0,'candidate_graphs':0}
save('SOURCE_SEMIDIRECT_RECIPE.json',recipe)
result={'status':recipe['status'],'Ntwists_tested':len(tested),'scope_max_Ntwists':425,
        'beta_N_twist':selected,'H_order':48,'H_Ncosets_distinct':48,
        'alpha_action':act_alpha,'beta_action':act_beta,'alpha_scalar17_order':chi_order,
        'positive_generators':source_rows[:3],'full_source_directed_adjacencies_matched':arcs,
        'full_source_undirected_edges_matched':61200,'all_vertex_group_coordinates':n,
        'source_BFS':0,'large_group_enumeration':False,'new_graphs':0,
        'CPU_seconds':time.process_time()-START,'pending':[],'running':False}
save('RESULT.json',result);save('checkpoint.json',result);save('terminal.json',result)
print(json.dumps(result,indent=2))
