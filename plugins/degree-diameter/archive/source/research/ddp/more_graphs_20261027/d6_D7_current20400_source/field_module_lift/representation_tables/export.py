"""Specified finite-field representations and source-generator norm checks only."""
from pathlib import Path
import json
import time

started=time.process_time()
out=Path(__file__).resolve().parent
source=out.parents[1]/'h48_complement/SOURCE_SEMIDIRECT_RECIPE.json'
actual=json.loads(source.read_text())
positive=actual['positive_generators']
assert [(g['c17'],g['u'],g['v']) for g in positive]==[(0,0,1),(1,1,12),(5,2,11)]
assert actual['alpha_action']['scalar17']==5 and actual['beta_action']['scalar17']==1

def digits(x,p,d):return [(x//p**i)%p for i in range(d)]
def encode(v,p):return sum(x*p**i for i,x in enumerate(v))
def field(p,d,poly):
    q=p**d
    def add(a,b):return encode([(x+y)%p for x,y in zip(digits(a,p,d),digits(b,p,d))],p)
    def multiply(a,b):
        A,B=digits(a,p,d),digits(b,p,d)
        c=[0]*(2*d-1)
        for i in range(d):
            for j in range(d):c[i+j]=(c[i+j]+A[i]*B[j])%p
        for k in range(2*d-2,d-1,-1):
            t=c[k]
            for j in range(d):c[k-d+j]=(c[k-d+j]-t*poly[j])%p
        return encode(c[:d],p)
    plus=[[add(a,b) for b in range(q)] for a in range(q)]
    times=[[multiply(a,b) for b in range(q)] for a in range(q)]
    neg=[encode([(-x)%p for x in digits(a,p,d)],p) for a in range(q)]
    inv=[0]+[next(b for b in range(1,q) if times[a][b]==1) for a in range(1,q)]
    return {'q':q,'characteristic':p,'extension_degree':d,'modulus_polynomial_low_to_high':poly,
            'encoding':'label=sum(coeff_i*characteristic^i), coeff_i in primefield',
            'add':plus,'mul':times,'neg':neg,'inv':inv,'inv_zero_entry':'unusedplaceholder0',
            'prime_integer_embedding':'integer n maps to n modcharacteristic, not n modq'}

fields={'F7':field(7,1,[0,1]),'F8':field(2,3,[1,1,0,1]),
        'F9':field(3,2,[1,0,1]),'F11':field(11,1,[0,1])}
H=[(u,v) for v in range(16) for u in range(3)]
hmul=[[(u+(-1 if v%2 else 1)*U)%3+3*((v+V)%16) for U,V in H] for u,v in H]
hinv=[(-(-1 if v%2 else 1)*u)%3+3*((-v)%16) for u,v in H]
assert all(hmul[i][hinv[i]]==0 and hmul[hinv[i]][i]==0 for i in range(48))
chi=[pow(5,v,17) for u,v in H]
assert pow(5,16,17)==1 and pow(5,8,17)!=1

def qmul(g,h):
    c,a=g;d,b=h
    return ((c+chi[a]*d)%17,hmul[a][b])
def quotient_order(g):
    x=(0,0)
    for k in range(1,817):
        x=qmul(x,g)
        if x==(0,0):return k
Qpositive=[(g['c17'],g['u']+3*g['v']) for g in positive]
orders=[quotient_order(g) for g in Qpositive]
assert orders==[16,12,16]
Qinverse=[(-pow(chi[h],-1,17)*c%17,hinv[h]) for c,h in Qpositive]
assert len(set(Qpositive+Qinverse))==6

specs=[('q7','F7',[[3,3],[6,4]],7,False),
       ('q8','F8',[[1,1],[0,1]],7,False),
       ('q9_plusg','F9',[[4,8],[0,8]],7,False),
       ('q9_minusg','F9',[[8,4],[0,4]],7,False),
       ('q11_control','F11',[[7,5],[1,4]],8,True)]
summary=[]
for name,key,A,targetD,control_only in specs:
    f=fields[key];q=f['q'];p=f['characteristic'];add=f['add'];mul=f['mul'];neg=f['neg'];inv=f['inv']
    B=[[0,p-1],[1,p-1]]
    I=[[1,0],[0,1]];Z=[[0,0],[0,0]]
    def mm(X,Y):
        return [[add[mul[X[i][0]][Y[0][j]]][mul[X[i][1]][Y[1][j]]] for j in range(2)] for i in range(2)]
    def ma(X,Y):return [[add[X[i][j]][Y[i][j]] for j in range(2)] for i in range(2)]
    def mpow(X,k):
        r=I
        for _ in range(k):r=mm(r,X)
        return r
    def mv(X,V):return [add[mul[X[i][0]][V[0]]][mul[X[i][1]][V[1]]] for i in range(2)]
    assert mpow(A,16)==I and mpow(B,3)==I
    assert mm(mm(A,B),mpow(A,15))==mpow(B,2)
    rho=[mm(mpow(B,u),mpow(A,v)) for u,v in H]
    for i in range(48):assert mm(rho[i],rho[hinv[i]])==I
    norm_checks=[]
    for g,d in zip(positive,orders):
        T=rho[g['u']+3*g['v']];total=Z;power=I
        for j in range(d):total=ma(total,power);power=mm(power,T)
        assert total==Z and power==I
        norm_checks.append({'name':g['name'],'source_order':d,'H_index':g['u']+3*g['v'],
                            'matrix':T,'norm_sum_matrix':total,'new_order_for_all_normal_vectors':d})
    alpha_order=next(k for k in range(1,17) if mpow(A,k)==I)
    invariant=[]
    for v in [[1,t] for t in range(q)]+[[0,1]]:
        imageA,imageB=mv(A,v),mv(B,v)
        if mul[v[0]][imageA[1]]==mul[v[1]][imageA[0]] and mul[v[0]][imageB[1]]==mul[v[1]][imageB[0]]:
            invariant.append(v)
    action=[]
    for T in rho:action.append([encode(mv(T,[i%q,i//q]),q) for i in range(q*q)])
    # encode with q is vector indexing, not an extension-field operation.
    if control_only:
        control=[0,1,0,2]
        control_rule='Sourceprojective(0,1,0,2) embedded inF11; onlyoneD8control.'
    else:
        control=[0,2%p,0,(-1)%p]
        first=next(x for x in control if x)
        control=[mul[inv[first]][x] for x in control]
        control_rule='Sourcecentered(0,2,0,-1), primeintegerembedding thenfirstnonzero=1.'
    caution=[]
    if key=='F8':
        caution.append('AllactionmatriceshaveF2coefficients; iffourinputcoordinates span aproperF2subspaceWofF8, everywordnormal liesinW², so disconnected.')
        assert control==[0,0,0,1]
        caution.append('Thiscontrol hasonlyF2entries and cannotgenerateF8²; it is theoreticallydisconnected, not aD7baseline.')
    if invariant:caution.append('CommoninvariantFqline exists; noirreducibility/automaticconnectivity assumption.')
    folder=out/name;folder.mkdir(exist_ok=True)
    data={'status':'VALID_SPECIFIED_REPRESENTATION_AND_ORDERS','name':name,'field_name':key,'field':f,
          'alpha_matrix':A,'beta_matrix':B,'alpha_image_order':alpha_order,'beta_image_order':3,
          'H_encoding':'h=u+3v, h=beta^u alpha^v','H_elements':[{'u':u,'v':v} for u,v in H],
          'H_mul':hmul,'H_inv':hinv,'rho':rho,'chi17':chi,'chi17_alpha':5,'chi17_beta':1,
          'vector_encoding':'x+q*y, x/y arefieldlabels','rho_on_vectors':action,
          'source_positive_parts':[{'name':g['name'],'c17':g['c17'],'u':g['u'],'v':g['v']} for g in positive],
          'source_positive_quotient_orders':orders,'generator_norm_checks':norm_checks,
          'group_multiplication':'(V,c,h)*(W,d,k)=(V+rho(h)W,c+chi17(h)*d mod17,H_mul[h][k])',
          'group_inverse':'(-rho(hinv)V,-chi17(h)^(-1)c mod17,hinv)',
          'six_quotient_generators_distinct':True,
          'control_tuple_Bx_By_Cx_Cy':control,'control_rule':control_rule,
          'common_invariant_lines':invariant,'connectivity_caution':caution,
          'target_Delta':6,'target_D':targetD,'group_order':816*q*q,
          'control_only':control_only,'normalized_parameter_cases':1 if control_only else (q**4-1)//(q-1),
          'parameter_search':False,'graph_generation':False,'BFS':0}
    (folder/'TABLES.json').write_text(json.dumps(data,indent=2)+'\n')
    summary.append({'name':name,'field':key,'q':q,'TABLES':name+'/TABLES.json','status':data['status'],
                    'alpha_image_order':alpha_order,'invariant_lines':invariant,'control':control,
                    'target_D':targetD,'group_order':816*q*q,'parameter_cases':data['normalized_parameter_cases']})

result={'status':'VALID_ALL_FOUR_D7_REPS_AND_SINGLE_Q11_D8_CONTROL','representations':summary,
        'D7_cases':sum(r['parameter_cases'] for r in summary if r['target_D']==7),
        'D8_control_cases':1,'source_recipe':str(source),
        'D7_normalization_proof':'ScalarFq* multiplication commuteswithallFqlinearHactions, givinggroupautomorphisms fixingA0 andscalingbothfreevectors; firstnonzero=1 isunique. Allzero isdisconnected.',
        'scope':'Four specifiedrepresentations only; no classification ofallrepresentations. Q11 isonecontrol, not aparameterfamily.',
        'CPU_seconds':time.process_time()-started,'parameter_search':False,'graph_generation':False,'BFS':0,'running':False,'pending':[]}
assert result['D7_cases']==2625
(out/'REPRESENTATIONS.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'terminal.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
