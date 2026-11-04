"""Exact geometry consequence of a still-to-be-proved Q5 neighbor lemma.

This checks Hall certificates only. It does not assert Q5 neighbor abundance.
"""
import json,itertools
from pathlib import Path
from eight_ep0_port_triangle_probe import matching_or_hall,edge
R=Path(__file__).resolve().parent
def main():
    base=json.loads((R/'eight_hole_covered_next_probe.json').read_text());rows=[]
    for r in base['joint_results']:
        v=r['target'];Z=set(r['Z']);W=set(r['W']);H={0}|Z|W;good=[]
        for i in r['cuts']:
            S={w^(1<<i) for w in W}
            for q in range(64):
                if q==v or q in H or q^(1<<i) in H or not q.bit_count()%2 or ((q^v)>>i)&1:continue
                N={q^(1<<j) for j in range(6) if j!=i}
                if len(N&S)>=3:good.append(dict(cut=i,q=q,mirror=q^(1<<i),S_neighbors=sorted(N&S)))
        forbidden={edge(t['q'],t['mirror']) for t in good}
        M,hall=matching_or_hall(H,forbidden)
        row=dict(target=v,Z=sorted(Z),W=sorted(W),sufficient_crossing_edges=good,closed_conditional_on_Q5_neighbor_union3=M is None,hall=hall,avoiding_matching=None if M is None else sorted(M))
        rows.append(row);print(v,sorted(Z),'sufficient_edges',len(good),'conditional_closed',M is None,hall,flush=True)
    out=dict(status='PASS_GEOMETRY_ONLY',unproved_import='Every arbitrary KQ5 nearperfect matching with sameparity holes has >=3 possible short neighbors at the included free hole on cycles omitting the other hole',reports=rows,full_eight_hole_proved=False)
    (R/'eight_ep0_three_neighbor_geometry.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':main()
