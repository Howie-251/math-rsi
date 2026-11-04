"""Exact geometry consequences of eight candidate T15 orbit theorems.

Counts are conditional until their proof audit is integrated. They are not
counts of matchings and do not establish the existence of realizing matchings.
"""
import json,collections,hashlib
from pathlib import Path
R=Path(__file__).resolve().parent
CORES={13,14,19,31,32,35,37,38}
def main():
    data=json.loads((R/'eight_t15_core_map.json').read_text())
    def a1b4(r):
        return any(sum((z>>i&1)==(r['target']>>i&1) for z in r['Z'])==1 and
            all((w>>i&1)==(r['target']>>i&1) for w in r['W']) for i in range(6))
    before=[r for r in data['targets'] if not a1b4(r)]
    newly=[r for r in before if set(r['core_choices'])&CORES]
    after=[r for r in before if not set(r['core_choices'])&CORES]
    exceptions=[r for r in data['without_a2b1_geometries'] if not a1b4(r)]
    assert len(before)==41408 and len(exceptions)==50
    patterns={tuple(r['core_choices']) for r in after}
    forced={p[0] for p in patterns if len(p)==1}
    todo={p for p in patterns if not set(p)&forced}
    best=None
    def cover(selected,uncovered):
        nonlocal best
        if best is not None and len(selected)>=len(best):return
        if not uncovered:best=set(selected);return
        p=min(uncovered,key=lambda p:(len(p),p))
        for c in p:cover(selected|{c},{q for q in uncovered if c not in q})
    cover(set(forced),patterns-{p for p in patterns if set(p)&forced})
    assert all(set(p)&best for p in patterns)
    for v in (1,7,31):
        rows=[r for r in after+exceptions if r['target']==v]
        (R/f'remaining_eight_after_single_face_{v}.bin').write_bytes(b''.join(bytes(r['Z']+r['W']) for r in rows))
    out=dict(status='CONSEQUENCES_CONDITIONAL_ON_EIGHT_CORE_AUDIT',closed_core_candidates=sorted(CORES),
        previous_remaining=41458,newly_covered=len(newly),remaining=len(after)+len(exceptions),
        newly_by_target=dict(collections.Counter(r['target'] for r in newly)),
        remaining_by_target=dict(collections.Counter(r['target'] for r in after+exceptions)),
        remaining_with_a2b1=len(after),remaining_without_a2b1=len(exceptions),
        remaining_choice_patterns=[list(p) for p in sorted(patterns)],
        forced_remaining_cores=sorted(forced),minimum_additional_core_cover=len(best),
        selected_additional_cores=sorted(best),
        full_eight_hole_proved=False,full_p6_proved=False,
        scope='Normalized marked hole configurations; arbitrary realizing matchings covered only by the audited theorem, not by these counts',
        source_hashes={n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in ['eight_t15_core_map.json','t15_analytic_geometry.json']})
    (R/'eight_after_single_face_cores.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
