import json
from pathlib import Path
A=((4,2),(1,1)); B=((0,4),(1,4)); I=((1,0),(0,1))
def mm(X,Y):return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2))%5 for j in range(2)) for i in range(2))
def mp(X,n):
 r=I
 for _ in range(n):r=mm(r,X)
 return r
def mv(X,v):return tuple(sum(X[i][j]*v[j] for j in range(2))%5 for i in range(2))
def rho(u,v):return mm(mp(B,u),mp(A,v))
def mul(g,h):
 x,y,c,u,v=g; X,Y,C,U,V=h
 W=mv(rho(u,v),(X,Y))
 return ((x+W[0])%5,(y+W[1])%5,(c+pow(5,v,17)*C)%17,(u+(-1 if v%2 else 1)*U)%3,(v+V)%16)
def inv(g):
 x,y,c,u,v=g; U=(-(-1 if v%2 else 1)*u)%3; V=(-v)%16
 W=mv(rho(U,V),(x,y))
 return (-W[0]%5,-W[1]%5,-pow(5,V,17)*c%17,U,V)
def conj(t,g):return mul(mul(t,g),inv(t))
def scale(g,s,t):return (g[0]*s%5,g[1]*s%5,g[2]*t%17,g[3],g[4])
alpha=(0,0,0,0,1); beta2=(0,0,0,2,0)
sourceA=(0,0,0,0,1);sourceB=(0,2,1,1,12);sourceC=(0,4,5,2,11)
records=[]
def finish(name,g,h,expected,chain):
 assert (g,h)==expected,(name,g,h)
 records.append({'source_subset':name,'first':list(g),'second':list(h),'normalized':{'a':g[4],'b':h[4],'v':list(h[:2]),'c':h[2]},'operations':chain,'inherited_D':11})
g=conj(alpha,sourceA);h=conj(alpha,inv(sourceB))
g,h=scale(g,2,6),scale(h,2,6)
finish('AB',g,h,((0,0,0,0,1),(1,4,1,1,4)),['invert B','conjugate both by alpha','scale V by 2 and C17 by 6'])
g=conj(alpha,sourceA);h=conj(alpha,inv(sourceC))
g,h=scale(g,2,5),scale(h,2,5)
finish('AC',g,h,((0,0,0,0,1),(1,1,1,1,5)),['invert C','conjugate both by alpha','scale V by 2 and C17 by 5'])
g,h=conj(beta2,sourceC),conj(beta2,sourceB)
assert g==(4,0,5,0,11) and h==(2,0,1,1,12)
t=(2,2,9,0,0);g,h=conj(t,g),conj(t,h)
assert g==(0,0,0,0,11) and h==(2,2,8,1,12)
g,h=conj(alpha,inv(g)),conj(alpha,inv(h))
assert h==(1,3,7,1,4)
g,h=scale(g,1,5),scale(h,1,5)
finish('BC',g,h,((0,0,0,0,5),(1,3,1,1,4)),['choose C first','conjugate both by beta^2','conjugate both by N element (2,2,c9)','invert both generators','conjugate both by alpha','scale C17 by 5'])
assert mp(A,2)==((3,0),(0,3)) and mp(A,8)==I
assert mm(mm(A,B),mp(A,7))==mp(B,2)
out={'status':'VALID_COMPLETE_216_NORMALIZATION_AND_THREE_CONTROL_IDENTITIES','covering_representatives':216,'inherited_controls':records,'new_cases_after_inherited_controls':213,'family_enumerations':0,'graph_generation':0,'BFS':0,'scope':'All connected degree-four Cayley graphs on this fixed source abstract group, up to the listed automorphisms and inverse-pair changes; no claim about other groups.'}
Path(__file__).with_name('CONTROL_IDENTITIES.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'status':out['status'],'controls':[r['normalized'] for r in records],'BFS':0}))
