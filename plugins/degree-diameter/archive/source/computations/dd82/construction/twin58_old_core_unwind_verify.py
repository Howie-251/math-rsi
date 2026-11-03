#!/usr/bin/env python3
"""Reconstruct the selected finite repair and independently BFS its full graph."""
from pathlib import Path
from collections import Counter
import json
from twin59_to_58_deflation_verify import read_edges,bfs
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin58_old_core_unwind_run'
def main():
    r=json.loads((OUT/'repair.json').read_text())
    _,source=read_edges(Path(r['source']));n,actual=read_edges(OUT/'repair.best.edges')
    assert n==58 and r['complete_for_stated_choices'] and r['choices']==120*720==86400
    assert r['valid_choices']==86400 and r['rejected_existing_or_duplicate_attachment']==0
    assert sum(r['bad_pair_histogram'].values())==r['valid_choices']
    assert min(map(int,r['bad_pair_histogram']))==r['minimum_bad_pairs']
    removedold={tuple(e) for e in r['removed_old_edges_order58']}
    removedaux={tuple(e) for e in r['best_removed_auxiliary_edges_order58']}
    added={tuple(e) for e in r['best_added_attachment_edges_order58']}
    assert removedold|removedaux<=source and not added&source
    assert len(removedold)==len(removedaux)==3 and len(added)==6
    assert actual==(source-removedold-removedaux)|added
    aux=set(range(40,48));old=set(range(58))-aux
    assert all(u in aux and v in aux for u,v in removedaux)
    assert all(u in old and v in old for u,v in removedold)
    released=Counter(v for e in removedold|removedaux for v in e)
    assert Counter(v for e in added for v in e)==released
    assert all((u in old)!=(v in old) for u,v in added)
    sourceadj=[set() for _ in range(58)]
    for u,v in source:sourceadj[u].add(v);sourceadj[v].add(u)
    assert sum(u in aux and v in aux for u,v in source)==10
    assert all(not(sourceadj[u]&aux) for e in removedold for u in e)
    # The six distinct old endpoints each receive exactly one auxiliary slot.
    # Consequently all 120*720 distinguished-slot choices have six new,
    # pairwise different attachments and preserve degrees; no rescoring needed.
    fixedadj=[set() for _ in range(58)]
    for u,v in source-removedold:fixedadj[u].add(v);fixedadj[v].add(u)
    old55=53;aux43=41;forced_old=[9,14,28]
    assert sourceadj[old55]&aux=={aux43}
    assert all(old55 not in fixedadj[u] and not(fixedadj[u]&fixedadj[old55]&old) for u in forced_old)
    assert len(sourceadj[aux43]&aux)==2
    obstruction={'label_convention':'original order60 labels',
      'fixed_auxiliary_neighbors_of_old55':[43],
      'old_vertices_forced_to_attach_to43_for_old_pair_coverage':forced_old,
      'source_auxiliary_degree_of43':2,'required_new_attachment_slots_at43':3,
      'maximum_released_slots_at43_by_deleting_auxiliary_edges':2,
      'conclusion':'Every graph in this prescribed repair family retains at least one of (9,55),(14,55),(28,55) as a bad pair'}
    (OUT/'repair_obstruction.json').write_text(json.dumps(obstruction,indent=2)+'\n')
    check=bfs(58,actual);before=bfs(58,source)
    assert before['bad_pair_count']==21 and check['bad_pair_count']==r['minimum_bad_pairs']
    basebad={(x['u'],x['v']) for x in before['bad_pairs']};newbad={(x['u'],x['v']) for x in check['bad_pairs']}
    label=lambda v:v if v<41 else v+2
    def converted(pairs):return [[label(u),label(v)] for u,v in sorted(pairs)]
    def categories(pairs):return dict(Counter('old-old' if u in old and v in old else 'auxiliary-auxiliary' if u in aux and v in aux else 'old-auxiliary' for u,v in pairs))
    delta={'old_bad_pair_count':len(basebad),'new_bad_pair_count':len(newbad),
      'repaired_bad_pair_count':len(basebad-newbad),'introduced_bad_pair_count':len(newbad-basebad),
      'retained_bad_pair_count':len(basebad&newbad),
      'repaired_bad_pairs_order58':sorted(basebad-newbad),'introduced_bad_pairs_order58':sorted(newbad-basebad),
      'retained_bad_pairs_order58':sorted(basebad&newbad),
      'repaired_bad_pairs_original60':converted(basebad-newbad),'introduced_bad_pairs_original60':converted(newbad-basebad),
      'retained_bad_pairs_original60':converted(basebad&newbad),
      'source_bad_pair_categories':categories(basebad),'new_bad_pair_categories':categories(newbad)}
    (OUT/'repair.best.verification.json').write_text(json.dumps(check,indent=2)+'\n')
    (OUT/'bad_pair_changes.json').write_text(json.dumps(delta,indent=2)+'\n')
    result={'selected_repair_exactly_reconstructed':True,'all_choices_legal_by_distinct_old_endpoints_and_absent_initial_attachments':True,
      'independent_all_source_bfs_verified':True,'best_bad_pairs':check['bad_pair_count'],
      'distance_histogram':check['distance_histogram'],'valid_degree8_diameter2':check['valid_degree8_diameter2'],
      'source_bad_pairs':21,'change_counts':{k:v for k,v in delta.items() if k.endswith('_count')},
      'three_required_slots_exceed_two_available_at_auxiliary43':True,
      'scope':'Complete specified 86400 repair choices, counted with distinguished auxiliary slots; no claim of unique resulting graphs'}
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2));print('categories',delta['new_bad_pair_categories'])
if __name__=='__main__':main()
