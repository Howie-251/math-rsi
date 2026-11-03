#!/usr/bin/env python3
"""Independent BFS of the exact neutral-then-improving path and state replay."""
import bisect,json
from pathlib import Path
from twin_seed_unrestricted_switch_verify import read,verify
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin59_neutral_component_run'
def main():
    report=json.loads((OUT/'component.json').read_text())
    _,seed=read(Path(report['source']));states=[seed];ordered_keys=[tuple(sorted(seed))]
    for node in report['stored_states'][1:]:
        g=set(states[node['parent']])
        for e in node['change']['removed']:assert tuple(e) in g;g.remove(tuple(e))
        for e in node['change']['added']:assert tuple(e) not in g;g.add(tuple(e))
        encoded=tuple(sorted(g));pos=bisect.bisect_left(ordered_keys,encoded)
        assert pos==len(ordered_keys) or ordered_keys[pos]!=encoded
        ordered_keys.insert(pos,encoded);states.append(g)
    assert len(states)==report['distinct_stored_states']<=100
    previous=json.loads((HERE/'twin_seed_unrestricted_switch_run/deflated59.json').read_text())['neighborhoods'][1]
    first=report['expansions'][0]
    assert first['complete'] and first['bad_pair_histogram']==previous['bad_pair_histogram']
    assert first['valid_switches_evaluated']==previous['valid_distinct_switches']
    assert sum(s['valid_switches_evaluated'] for s in report['expansions'])==report['candidate_switches_evaluated']
    reference=seed;checks=[]
    for move in report['path']:
        checked,reference=verify(Path(move['file']),move['bad_pairs'],reference,move['change'],41)
        assert reference==states[move['node']];checks.append(checked)
    assert checks[-1]['uncovered_pair_count']==report['endpoint_bad_pairs']<27
    result={'all_stored_states_replay_and_have_distinct_sorted_edge_sequences':True,
      'start_neighborhood_matches_previous_complete_enumeration':True,
      'all_saved_path_graphs_independently_bfs_verified':True,'path_checks':checks,
      'search_stopped_at_first_strict_improvement':report['stop_reason']=='first_strict_improvement',
      'component_completely_closed':False}
    (OUT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
if __name__=='__main__':main()
