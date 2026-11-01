"""A colorable11-edge local witness against completing the fixed blue-to-red move{x} by arbitrary red flips."""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
HERE=Path(__file__).parent

def main():
    start=time.time();P=set(range(9));x=9;b1=10;next_vertex=13
    G=frozenset(range(5));F=frozenset([x,5,6,7,8]);edges=[G,F,frozenset([0,x,10,11,12])]
    for y in range(1,9):
        edges.append(frozenset([y]+list(range(next_vertex,next_vertex+4))));next_vertex+=4
    assert next_vertex==45 and len(edges)==len(set(edges))==11
    assert all(len(e)==5 for e in edges) and set().union(*edges)==set(range(45))
    def bad(red):return [i for i,e in enumerate(edges) if e<=red or e.isdisjoint(red)]
    assert bad(P)==[0]
    witnesses={y:next(i for i,e in enumerate(edges) if e&P=={y}) for y in P}
    unit={str(y):sum(x in e and y in e for e in edges) for y in range(5,9)}
    assert set(unit.values())=={1}
    hist=Counter();tested=0
    for n in range(10):
        for T in combinations(P,n):
            bb=bad((P-set(T))|{x});assert bb
            hist[len(bb)]+=1;tested+=1
    assert tested==512
    proper=(P-{0})|{b1};assert not bad(proper)
    out=dict(status='PASS',scope=__doc__,vertices=45,edges=11,simple_five_uniform=True,initial_red_vertices=sorted(P),initial_bad_edge_indices=[0],private_red_witness_indices=witnesses,unit_codegrees_x_y=unit,fixed_blue_to_red_vertex=x,red_flip_subsets_checked=tested,successful_fixed_x_exchanges=0,bad_edge_count_histogram=dict(sorted(hist.items())),explicit_proper_final_red=sorted(proper),edge_list=[sorted(e) for e in edges],global_colorings_enumerated=0,scope_exclusion='This local example is colorable and is not pair-covering or minimum-degree6/7; it does not refute an actual target branch.',elapsed_seconds=time.time()-start)
    (HERE/'LOCAL_OBSTRUCTION_CHECK.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='edge_list'},indent=2))
if __name__=='__main__':main()
