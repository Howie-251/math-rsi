from pathlib import Path
from itertools import product
import json,resource,subprocess,time
P=Path(__file__).resolve().parent
assert not (P/'CAPACITY.json').exists(), 'Do not rerun completed screen.'
t=time.process_time();wall=time.monotonic();r=resource.getrusage(resource.RUSAGE_CHILDREN);children=r.ru_utime+r.ru_stime
I=(1,0,0,1)
mat=[I]+[a for a in product(range(3),repeat=4) if (a[0]*a[3]-a[1]*a[2])%3==1 and a!=I]
assert len(mat)==24 and (2,0,0,2) in mat
index={a:i for i,a in enumerate(mat)}
def mm(a,b):
    p,q,r,s=a;x,y,z,w=b
    return ((p*x+q*z)%3,(p*y+q*w)%3,(r*x+s*z)%3,(r*y+s*w)%3)
def mi(a):
    p,q,r,s=a
    return s,-q%3,-r%3,p
table=[[index[mm(a,b)] for b in mat] for a in mat];inv=[index[mi(a)] for a in mat]
adj=[[(0,0,0,1),(0,1,0,-1),(1,4,None,0),(1,6,2,1)],[(1,2,1,1),(1,3,1,-1),(0,5,None,0),(0,7,2,-1)]]
paths=[]
for root in range(2):
    rows=[]
    def dfs(side,last,coeff,word,parent):
        letter=6 if not word else word[-1]
        at=len(rows);rows.append(dict(parent=parent,letter=letter,target=side,coeff=coeff,word=word))
        if len(word)==5:return
        for dst,dart,var,sign in adj[side]:
            if last is not None and dart==(last^1):continue
            cc=coeff.copy()
            if var is not None:cc[var]=(cc[var]+sign)%8
            # SL letters: a,a^-1,b,b^-1,h,h^-1,I.
            ll=6 if var is None else (0 if var==0 else 2 if var==1 else 4)+(sign<0)
            dfs(dst,dart,cc,word+[ll],at)
    dfs(root,None,[0,0,0],[],-1);assert len(rows)==485;paths.append(rows)

# Independent direct numeric SL word evaluation checks96 function cells.
check=(1,5,7);letters=[mat[check[0]],mi(mat[check[0]]),mat[check[1]],mi(mat[check[1]]),mat[check[2]],mi(mat[check[2]]),I]
expected=[]
for root in range(2):
    slots=[set() for _ in range(48)]
    for row in paths[root]:
        x=I
        for letter in row['word']:x=mm(x,letters[letter])
        slots[row['target']*24+index[x]].add(tuple(row['coeff']))
    expected.extend(map(len,slots))
with (P/'capacity_input.txt').open('w') as f:
    for row in table:f.write(' '.join(map(str,row))+'\n')
    f.write(' '.join(map(str,inv))+'\n')
    for rows in paths:
        f.write(str(len(rows))+'\n')
        for row in rows:
            c=row['coeff'];form=c[0]+8*c[1]+64*c[2]
            f.write(f"{row['parent']} {row['letter']} {row['target']} {form}\n")
    f.write(' '.join(map(str,check))+'\n'+' '.join(map(str,expected))+'\n')
(P/'sl23.json').write_text(json.dumps(dict(matrices=mat,identity_index=0,negative_identity_index=index[(2,0,0,2)],table=table,inverse=inv),indent=2)+'\n')
with (P/'compile_capacity.log').open('w') as log:
    subprocess.run(['g++','-std=c++17','-O3','capacity.cpp','-o','capacity'],cwd=P,stdout=log,stderr=subprocess.STDOUT,check=True)
with (P/'capacity.log').open('w') as log:subprocess.run([str(P/'capacity')],cwd=P,stdout=log,stderr=subprocess.STDOUT,check=True)
x=json.loads((P/'capacity.raw.json').read_text());r=resource.getrusage(resource.RUSAGE_CHILDREN);cpu=time.process_time()-t+r.ru_utime+r.ru_stime-children
x.update(group='SL(2,F3) direct product C8',group_order=192,n=384,degree=4,target_D=5,quotient='SL(2,F3), central fiber C8',central_variables=['alpha_a','alpha_b','alpha_h'],capacity_target_per_quotient_fiber=8,short_words_per_root=485,scout_total_CPU_seconds=cpu,wall_seconds=time.monotonic()-wall,old_scope_check='No exact group/target/split found in inspected fixed-string markdown and make_groups sources.',CPU_budget_seconds=5,whole_template_capacity_excluded=x['surviving_quotient_triples']==0)
assert cpu<5
(P/'CAPACITY.json').write_text(json.dumps(x,indent=2)+'\n')
print(json.dumps({k:x[k] for k in ['status','surviving_quotient_triples','minimum_fiber_capacity_maximum','scout_total_CPU_seconds','whole_template_capacity_excluded']}))
