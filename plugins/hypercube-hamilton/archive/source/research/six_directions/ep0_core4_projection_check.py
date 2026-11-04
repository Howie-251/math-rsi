"""Exact T15 core induced by every forced-edge option in two EP0 orbits."""
import itertools,json
from pathlib import Path
R=Path(__file__).resolve().parent
def main():
    reps=json.loads((R/'t15_analytic_geometry.json').read_text())['T15']['residual_orbits'];lookup={}
    for p in itertools.permutations(range(5)):
        tr=[sum(((v>>j)&1)<<p[j] for j in range(5)) for v in range(32)]
        for k,r in enumerate(reps):
            key=tuple(sorted(tr[v] for v in r['avoided'])),tuple(sorted(tr[v] for v in r['included']))
            assert key not in lookup or lookup[key]==k;lookup[key]=k
    rows=[]
    for v,Z,W,h in [(1,[3,5,9],[14,31,47,62],15),(7,[15,23,39],[56,59,61,62],63)]:
        for i in range(6):
            za=[z for z in Z if (z>>i&1)==(v>>i&1)]
            if len(za)!=2:continue
            q=h^(1<<i);a=next(z for z in Z if z not in za)
            def proj(x):
                x^=a;return (x&((1<<i)-1))|((x>>(i+1))<<i)
            for t in W:
                s=t^(1<<i)
                if (q^s).bit_count()!=1:continue
                key=tuple(sorted(proj(z^(1<<i)) for z in za)),tuple(sorted(proj(w) for w in W if w!=t))
                assert lookup[key]==4
                rows.append(dict(target=v,Z=Z,W=W,cut=i,port=q,forced_edge_option=[q,s],consumed_odd_hole=t,
                    T15_avoided=key[0],T15_included=key[1],core=4))
    assert len(rows)==18
    out=dict(status='PASS_GEOMETRIC_PROJECTION',scope='Every permitted forced q-s choice in the two proved EP0 representatives',
        dependency='Proving full T15 core4 suffices to close these 11 Q6 geometries using already audited EP0 and double-bridge transfer',
        core4_currently_proved=False,full_eight_hole_proved=False,rows=rows)
    (R/'ep0_core4_projection_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print('18 forced-edge options all induce T15 core4; 11 Q6 geometries remain conditional on core4')
if __name__=='__main__':main()
