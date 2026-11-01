from itertools import combinations
from collections import Counter
from pathlib import Path
import json,time
start=time.process_time();x=0;G={0,1,2,3,4};F={0,5,6,7,8}
star=[G,F,{0,9,13,11,17},{0,9,14,12,18},{0,10,15,11,19},{0,10,16,12,20}]
red={0,1,2,3,4,9,10,13,14,15,16};blue=set(range(21))-red
p=13;U={1,2,3,5,6};B={9,10,11,12};V=set(range(1,21))-{p}-U-B
assert len(V)==10
D={0:6,p:7};D.update({v:8 for v in U|B});D.update({v:9 for v in V})
private_red=[{g,17,18,19,20} for g in range(1,5)]
private_blue=[{f,9,10,14,15} for f in range(5,9)]
edges=star+private_red+private_blue
assert len({frozenset(e) for e in edges})==14 and all(len(e)==5 for e in edges)
assert len(red-{0})==len(blue)==10
link=[e-{0} for e in star]
assert sum(e<=red for e in link)==sum(e<=blue for e in link)==1
co=lambda u,v:sum(u in e and v in e for e in edges)
assert all(co(0,v)==(2 if v in B else 1) for v in range(1,21))
partial_degree={v:sum(v in e for e in edges) for v in range(21)}
assert all(partial_degree[v]<=D[v] for v in D)
repeat={v:sum(max(co(v,w)-1,0) for w in range(21) if w!=v) for v in range(21)}
assert all(repeat[v]<=4*D[v]-20 for v in D)
def bad(R):return [i for i,e in enumerate(edges) if e<=R or e.isdisjoint(R)]
assert bad(red)==[0]
blocked=[]
for g in range(1,5):
 for f in range(5,9):
  R=(red-{g})|{f};bb=bad(R)
  assert 6+(g-1) in bb and 10+(f-5) in bb
  blocked.append({'red_endpoint':g,'blue_endpoint':f,'bad_original_indices':bb})
# The exact x/y/s joint move repairs this partial source, illustrating the needed larger move.
y=5;s=9;after=(red-{x,s})|{y}
assert bad(after)==[]
triple_moves=[]
for y in range(5,9):
    Py=[e-{y} for e in edges if x not in e and e & blue=={y}]
    assert Py
    Cy=set.intersection(*(set(e) for e in Py))
    for s in sorted(red-{x}):
        Qs=[e for e in edges if x not in e and e & red=={s}]
        Xs=[e for e in star if e & red=={x,s}]
        criterion=s in Cy and all(y in e for e in Qs+Xs)
        actual=not bad((red-{x,s})|{y})
        assert criterion==actual
        if actual:triple_moves.append([x,y,s])
assert len(triple_moves)==16
bounds=[]
for q in range(5):
 unsafeG=min(4-q,1+q//2);unsafeF=min(q,(6-q)//2)
 assert 4-unsafeG>=2 and 4-unsafeF>=2
 bounds.append({'blue_repeated_B':q,'safe_G_lower':4-unsafeG,'safe_F_lower':4-unsafeF})
out={'status':'PASS_LOCAL_SOURCE_AND_EXACT_MOVE','safe_point_bounds':bounds,
'partial_source':{'edges':[sorted(e) for e in edges],'red':sorted(red),'blue':sorted(blue),'target_degree':D,'partial_degree':partial_degree,'partial_row_repetition':repeat,'p7':p,'U8':sorted(U),'B8_twice':sorted(B),'V9':sorted(V),'blocked_safe_G_F_swaps':blocked,'repairing_three_point_move':{'x_to_blue':x,'y_to_red':y,'s_to_blue':s},'all_40_exact_triple_tests_checked':True,'repairing_triple_moves':triple_moves,'is_full_35edge_paircover_H':False,'asserts_full_A1_extension_exists':False},'cpu_seconds':time.process_time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],len(blocked),'safe swaps blocked; exact triple move verified',out['cpu_seconds'])
