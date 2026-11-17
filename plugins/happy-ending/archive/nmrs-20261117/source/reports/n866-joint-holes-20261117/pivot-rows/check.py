#!/usr/bin/env python3
"""Linux stdlib replay of every shared pivot cell and all exported hole vectors."""
import itertools as it,json,pathlib,platform
assert platform.system()=='Linux'
root=pathlib.Path(__file__).resolve().parent;source=root.parent/'first';out=root/'first';U=json.loads((source/'universe.json').read_text());W=list(map(tuple,U['subsets']));S=list(map(tuple,U['column_heights']));index={w:i for i,w in enumerate(W)}
assert W==list(it.combinations(range(1,9),4)) and S==[tuple(w[3-j]-(4-j) for j in range(4)) for w in W]
cells=[{(x,y) for x in range(1,5) for y in range(1,s[x-1]+1)} for s in S];lookup={s:i for i,s in enumerate(S)}
transport={i:index[tuple(sorted(9-v for v in set(range(1,9))-set(w)))] for i,w in enumerate(W)}
assert all(cells[transport[i]]=={(y,x) for x,y in cells[i]} and transport[transport[i]]==i for i in range(70))
rows=json.loads((out/'rows.json').read_text());cycles=json.loads((source/'cycles.json').read_text());checks=0;pivot_cells=0
for r in rows:
    support=set(r['support']);assert len(support)==len(r['support'])
    if r['kind']=='certified_cycle':assert support==set(cycles[r['key']]) and r['rhs']==len(support)-7;continue
    if r['kind']=='imported_total_holes_at_least_7':assert support==set(range(70)) and r['rhs']==7;continue
    assert r['kind']=='shared_pivot' and r['rhs']==1;Omega=tuple(reversed(r['Omega']));faces=[set(Omega)-{v} for v in Omega]
    starts=[index[tuple(sorted(f|{1}))] for f in faces];ends=[index[tuple(sorted(f|{8}))] for f in faces]
    redpaths=[]
    for j in (0,3):
        a,b=S[starts[j]],S[ends[j]];path=[lookup[tuple(max(s,min(e,h)) for s,e in zip(a,b))] for h in range(5)]
        assert len(set(path))==5 and path[0]==starts[j] and path[-1]==ends[j]
        redpaths.append(path)
        segments=[cells[v]-cells[u] for u,v in zip(path,path[1:])];assert all(segments)
        assert all(max(x for x,y in later)<=min(x for x,y in earlier) for earlier,later in zip(segments,segments[1:]))
    expected=set(starts+ends+redpaths[0][1:-1]+redpaths[1][1:-1]);assert len(expected)==13
    pivot=(starts[3],ends[0]);domain=cells[pivot[1]]-cells[pivot[0]];assert domain and {x for x,y in domain}=={1,4}
    for label in domain:
        blue=starts+[ends[0]] if label[0]==4 else [starts[3]]+ends
        red=redpaths[0] if label[0]==4 else redpaths[1]
        assert (blue[0],blue[-1])==(red[0],red[-1]) and len(set(blue)|set(red))==8 and set(blue)&set(red)=={blue[0],blue[-1]}
        segments=[{label} if (u,v)==pivot else cells[v]-cells[u] for u,v in zip(blue,blue[1:])];assert all(segments)
        assert all(max(y for x,y in later)<=min(y for x,y in earlier) for earlier,later in zip(segments,segments[1:]))
        assert set(blue+red)<=expected;pivot_cells+=1
    if r['transpose']:expected={transport[v] for v in expected}
    assert support==expected;checks+=1
cover=json.loads((out/'cover.json').read_text());holes=cover['holes'];assert len(set(holes))==len(holes) and cover['subsets']==[list(W[i]) for i in holes]
assert all(len(set(holes)&set(r['support']))>=r['rhs'] for r in rows)
old=json.loads((source/'cover_10.json').read_text())['holes'];violated=[i for i,r in enumerate(rows) if len(set(old)&set(r['support']))<r['rhs']]
assert any(rows[i]['kind']=='shared_pivot' and rows[i]['transpose'] and rows[i]['Omega'] in ([2,3,4,5],[4,5,6,7]) for i in violated)
print(json.dumps(dict(host=platform.node(),status='PASS',rows=len(rows),shared_pivot_rows=checks,pivot_cell_branches=pivot_cells,verified_holes=len(holes),subsets=cover['subsets'],old_mask_violated_rows=violated,exact_matrix_minimum=7 if len(holes)==7 else None,scope='necessary hole matrix only; not an actual signotope'),indent=2))
