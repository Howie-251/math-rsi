from make_groups import table,R
from itertools import product
import json
for m,k,r in [(38,9,23),(13,27,3),(15,24,2),(13,28,5)]:
 assert pow(r,k,m)==1
 ix,T=table(f'D7_Meta_{m}_{k}_{r}',list(product(range(m),range(k))),lambda x,y:((x[0]+pow(r,x[1],m)*y[0])%m,(x[1]+y[1])%k),f'(a,b)*(c,d)=(a+{r}^b*c mod{m},b+d mod{k})')
 if m==38:
  p=json.loads((R.parents[2]/'research/ddp/m1_sources/684_recovered_construction.json').read_text());vs=p['voltage_sets'];A=[ix[tuple(v)] for v in vs[0][0]];B=[ix[tuple(v)] for v in vs[1][1]];S=[ix[tuple(v)] for v in vs[0][1]];inv=[row.index(0) for row in T];t=S[0];B=[T[T[t][b]][inv[t]] for b in B];S=[T[s][inv[t]] for s in S];(R/'baseline684_parameters.txt').write_text(' '.join(map(str,A+B+S))+'\n')
