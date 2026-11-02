from make_groups import table
from itertools import product
for m,k,r in [(7,9,2),(9,7,1),(31,2,30),(8,8,3),(8,8,5),(8,8,7),(16,4,3),(16,4,7),(16,4,15),(4,16,3)]:
    assert pow(r,k,m)==1
    table(f'Meta_{m}_{k}_{r}',list(product(range(m),range(k))),lambda x,y:((x[0]+pow(r,x[1],m)*y[0])%m,(x[1]+y[1])%k),f'(a,b)*(c,d)=(a+{r}^b*c mod{m},b+d mod{k})')
