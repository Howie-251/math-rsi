#!/usr/bin/env python3
"""Linux-only full inclusion-order shared labels, colors and same-end path DP."""
import collections,hashlib,itertools as it,json,pathlib,platform,shutil,time
assert platform.system()=='Linux'
root=pathlib.Path(__file__).resolve().parent;out=root/'base';out.mkdir(exist_ok=False);start=time.monotonic()
source=root.parent/'n866-joint-holes-20261117';U=json.loads((source/'first/universe.json').read_text());W=list(map(tuple,U['subsets']));S=U['column_heights'];cells=[{(x,y) for x in range(1,5) for y in range(1,s[x-1]+1)} for s in S]
succ={a:[b for b in range(70) if cells[a]<cells[b]] for a in range(70)};between={(a,b):[t for t in succ[a] if cells[t]<cells[b]] for a in range(70) for b in succ[a]}
pairs=[(a,b) for a in range(70) for b in succ[a]];triples=[(a,b,c) for a,b in pairs for c in succ[b]];quads=[(a,b,c,d) for a,b,c in triples for d in succ[c]]
nextvar=70;labels={};colors={};reach4={};reach5={};threshold={}
def fresh():
    global nextvar
    nextvar+=1;return nextvar
for a,b in pairs:labels[a,b]={cell:fresh() for cell in sorted(cells[b]-cells[a])}
for t in triples:colors[t]=fresh()
for a,u,v in triples:
    if between[a,u]:
        for col in (0,1):reach4[a,u,v,col]=fresh()
for a,t,u,v in quads:
    if (a,t,u,0) in reach4:
        for col in (0,1):
            if (a,v,col) not in reach5:reach5[a,v,col]=fresh()
for i in range(1,71):
    for j in range(1,min(12,i)+1):threshold[i,j]=fresh()
counts=collections.Counter();body=out/'body.cnf';f=body.open('w')
def emit(clause,kind):f.write(' '.join(map(str,clause))+' 0\n');counts[kind]+=1
rows=json.loads((source/'pivot-rows/first/rows.json').read_text());rows=[r for r in rows if r['kind']!='imported_total_holes_at_least_7'];assert len(rows)==93
for r in rows:assert r['rhs']==1;emit([i+1 for i in r['support']],'necessary_row')
for (a,b),choices in labels.items():
    vs=list(choices.values());emit(vs,'pair_label_at_least_one')
    for x,y in it.combinations(vs,2):emit([-x,-y],'pair_label_at_most_one')
for a,b,c in triples:
    gate=[a+1,b+1,c+1];color=colors[a,b,c]
    for (x,y),u in labels[a,b].items():
        for (xx,yy),v in labels[b,c].items():
            if xx<=x:emit(gate+[-u,-v,color],'blue_growth')
            if yy<=y:emit(gate+[-u,-v,-color],'red_growth')
valid={(0,0,0,0),(0,0,0,1),(0,0,1,1),(0,1,1,1),(1,1,1,1),(1,1,1,0),(1,1,0,0),(1,0,0,0)}
for a,t,u,v in quads:
    gate=[a+1,t+1,u+1,v+1];cs=[colors[z] for z in ((a,t,u),(a,t,v),(a,u,v),(t,u,v))]
    for bits in it.product((0,1),repeat=4):
        if bits not in valid:emit(gate+[-z if bit else z for z,bit in zip(cs,bits)],'chain_packet')
    for col in (0,1):
        # Every four-point same-color chain forces its shared-source/last-pair DP state.
        c1=colors[a,t,u];c2=colors[t,u,v]
        emit(gate+[-c1 if col else c1,-c2 if col else c2,reach4[a,u,v,col]],'path4_forward')
        if (a,t,u,col) in reach4:
            emit([v+1,-reach4[a,t,u,col],-c2 if col else c2,reach5[a,v,col]],'path5_forward')
for a,z,col in reach5:
    if col==0:emit([-reach5[a,z,0],-reach5[a,z,1]],'no_same_end_two_color_5')
for i in range(1,71):
    emit([-i,threshold[i,1]],'counter_input')
    if i>1:
        for j in range(1,min(i-1,12)+1):emit([-threshold[i-1,j],threshold[i,j]],'counter_inherit')
        for j in range(2,min(i,12)+1):emit([-i,-threshold[i-1,j-1],threshold[i,j]],'counter_increment')
f.close();total=sum(counts.values());cnf=out/'formula.cnf'
with cnf.open('w') as target,body.open() as source_file:target.write('p cnf %s %s\n'%(nextvar,total));shutil.copyfileobj(source_file,target)
metadata=dict(universe=U,rows=rows,labels=[dict(pair=[a,b],choices=[dict(cell=cell,variable=v) for cell,v in choices.items()]) for (a,b),choices in labels.items()],colors=[dict(triple=t,variable=v) for t,v in colors.items()],reach4=[dict(key=k,variable=v) for k,v in reach4.items()],reach5=[dict(key=k,variable=v) for k,v in reach5.items()],threshold=[dict(key=k,variable=v) for k,v in threshold.items()])
(out/'metadata.json').write_text(json.dumps(metadata,separators=(',',':'))+'\n')
stats=dict(host=platform.node(),source_sha256=hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),variables=nextvar,clauses=total,counts=dict(counts),pairs=len(pairs),triples=len(triples),quads=len(quads),reach4_states=len(reach4),reach5_states=len(reach5),cnf_sha256=hashlib.sha256(cnf.read_bytes()).hexdigest(),seconds=time.monotonic()-start)
(out/'result.json').write_text(json.dumps(stats,indent=2)+'\n');print(json.dumps(stats),flush=True)
