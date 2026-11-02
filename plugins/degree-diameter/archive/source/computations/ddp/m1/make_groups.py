from pathlib import Path
from itertools import permutations,product
import json
R=Path(__file__).resolve().parent

def table(name,elems,mul,formula):
    ix={x:i for i,x in enumerate(elems)}
    T=[[ix[mul(x,y)] for y in elems] for x in elems]; n=len(elems)
    assert T[0]==list(range(n)) and [row[0] for row in T]==list(range(n))
    assert all(0 in row for row in T)
    p=R/'group_tables'/name
    p.with_suffix('.txt').write_text(str(n)+'\n'+'\n'.join(' '.join(map(str,row)) for row in T)+'\n')
    p.with_suffix('.json').write_text(json.dumps({'name':name,'order':n,'formula':formula,'labels':elems},indent=2)+'\n')
    return ix,T

def alt(p):return sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2==0
A4=[p for p in permutations(range(4)) if alt(p)]; S4=list(permutations(range(4)))
for m,P,tag in [(5,A4,'C5xA4'),(6,A4,'C6xA4'),(7,A4,'C7xA4'),(3,S4,'C3xS4')]:
    ix,T=table(tag,list(product(range(m),P)),lambda x,y:((x[0]+y[0])%m,tuple(x[1][y[1][i]] for i in range(4))),'(k,p)*(l,q)=((k+l) mod m,p compose q)')
    if m==5:
        a=ix[(0,(1,0,3,2))]; b=ix[(0,(3,2,1,0))]
        S=[ix[(1,(0,3,1,2))],ix[(1,(3,2,1,0))],ix[(3,(1,2,0,3))],ix[(4,(0,1,2,3))],ix[(2,(3,0,2,1))]]
        inv=[row.index(0) for row in T]; t=S[0]
        # Relabel right fiber h -> h*t^-1.
        b=T[T[t][b]][inv[t]]; S=[T[s][inv[t]] for s in S]
        (R/'baseline_parameters.txt').write_text(' '.join(map(str,[a,b]+S))+'\n')
# Unitriangular4(F2), coordinates 01,02,03,12,13,23, tuple0 identity.
def ut(x,y):
    a,b,c,d,e,f=x; A,B,C,D,E,F=y
    return (a^A,b^B^(a&D),c^C^(a&E)^(b&F),d^D,e^E^(d&F),f^F)
table('UT4_2',list(product(range(2),repeat=6)),ut,'I+X over F2; (I+X)(I+Y)=I+X+Y+XY, upper triangular coordinates01,02,03,12,13,23')
# D8 x D8, D8=C4 semidirect C2 by inversion.
def dd(x,y):
    a,b,c,d=x; A,B,C,D=y
    return ((a+(-1)**b*A)%4,(b+B)%2,(c+(-1)**d*C)%4,(d+D)%2)
table('D8xD8',list(product(range(4),range(2),range(4),range(2))),dd,'((a,b),(c,d))*((A,B),(C,D))=((a+(-1)^b A mod4,b+B mod2),(c+(-1)^d C mod4,d+D mod2))')
# Heisenberg ring Z4.
table('Heis_Z4',list(product(range(4),repeat=3)),lambda x,y:((x[0]+y[0])%4,(x[1]+y[1])%4,(x[2]+y[2]+x[0]*y[1])%4),'(a,b,c)*(A,B,C)=(a+A,b+B,c+C+a*B) modulo4')
print('Wrote7 groups and exact source baseline parameters.')
