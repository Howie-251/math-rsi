#!/usr/bin/env python3
"""Direct graph invariants, exact state replay and independent all-source BFS."""
from pathlib import Path
from collections import Counter
import bisect,json,shutil,time
from twin59_to_58_deflation_verify import read_edges,bfs
HERE=Path(__file__).resolve().parent
OUT=HERE/'twin58_nonworsening_levels_run'
def write(path,value,indent=2):path.write_text(json.dumps(value,indent=indent)+'\n')
def invariants(path):
    n,edges=read_edges(path);adj=[set() for _ in range(n)]
    for u,v in edges:adj[u].add(v);adj[v].add(u)
    common=Counter();edgecommon=Counter();bad=[]
    for u in range(n):
        for v in range(u+1,n):
            c=len(adj[u]&adj[v]);common[c]+=1
            if v in adj[u]:edgecommon[c]+=1
            elif not c:bad.append([u,v])
    triangles=sum(k*v for k,v in edgecommon.items())//3
    return {'path':str(path),'n':n,'m':len(edges),'degree_histogram':dict(Counter(map(len,adj))),
      'triangles':triangles,'common_neighbor_histogram':dict(sorted(common.items())),
      'edge_common_neighbor_histogram':dict(sorted(edgecommon.items())),
      'bad_pair_count':len(bad),'bad_pairs':bad,
      'bad_endpoint_degrees':dict(sorted(Counter(v for e in bad for v in e).items()))}
def main():
    start=time.process_time();r=json.loads((OUT/'episode.json').read_text());source=Path(r['source'])
    new=invariants(source);brown=invariants(HERE/'brown58_three_switch.seed.edges')
    fields=('triangles','common_neighbor_histogram','edge_common_neighbor_histogram')
    witnesses=[k for k in fields if new[k]!=brown[k]];assert 'triangles' in witnesses
    write(OUT/'seed_comparison.json',{'new_seed':new,'brown_seed':brown,'nonisomorphic_witness':witnesses})
    n,seed=read_edges(source);assert n==58;states=[seed];ordered=[tuple(sorted(seed))]
    for node in r['stored_states'][1:]:
        assert node['node']==len(states) and 0<=node['parent']<len(states)
        g=states[node['parent']].copy()
        for e in node['change']['removed']:assert tuple(e) in g;g.remove(tuple(e))
        for e in node['change']['added']:assert tuple(e) not in g;g.add(tuple(e))
        key=tuple(sorted(g));pos=bisect.bisect_left(ordered,key)
        assert pos==len(ordered) or ordered[pos]!=key
        ordered.insert(pos,key);states.append(g)
    assert len(states)==r['distinct_stored_states']<=r['maximum_distinct_stored_states']
    summaries=[];fullchecks={}
    wanted={0}|{b['node'] for b in r['new_best_graphs']}
    for i,g in enumerate(states):
        check=bfs(58,g);assert check['bad_pair_count']==r['stored_states'][i]['bad_pairs']
        summaries.append({'node':i,**{k:v for k,v in check.items() if k!='bad_pairs'}})
        if i in wanted:fullchecks[i]=check
    for b in r['new_best_graphs']:
        nn,g=read_edges(Path(b['file']));assert nn==58 and g==states[b['node']]
        check=fullchecks[b['node']];assert check['bad_pair_count']==b['bad_pairs']
        write(Path(b['file']).with_suffix('.verification.json'),check)
    assert sum(e['valid_switches_evaluated'] for e in r['expansions'])==r['candidate_switches_evaluated']
    for e in r['expansions']:assert sum(e['bad_pair_histogram'].values())==e['valid_switches_evaluated']
    assert sum(e['complete'] for e in r['expansions'])==sum(l['fully_expanded_states'] for l in r['levels'])
    finalnode=r['final_best_path'][-1] if r['final_best_path'] else 0
    finalcheck=fullchecks[finalnode];assert finalcheck['bad_pair_count']==r['final_bad_pairs']
    with (OUT/'final.edges').open('w') as out:
        out.write('58 232\n')
        for u,v in sorted(states[finalnode]):out.write(f'{u} {v}\n')
    write(OUT/'final.json',{'n':58,'source':str(source),'episode_node':finalnode,
      'edges':[list(e) for e in sorted(states[finalnode])]})
    write(OUT/'final.verification.json',finalcheck)
    write(OUT/'expanded_states.json',{'n':58,'states':[{'node':i,'edges':[list(e) for e in sorted(g)]} for i,g in enumerate(states)]},None)
    result={'seed_nonisomorphic_to_brown_by_triangle_count':True,
      'all_stored_states_replayed_and_exactly_distinct':True,
      'all_stored_states_independently_bfs_verified':True,'state_count':len(states),
      'all_improving_saved_candidates_bfs_verified':True,'strict_improvements':r['strict_improvements'],
      'final_bad_pairs':r['final_bad_pairs'],'terminal_neutral_component_closed':r['terminal_neutral_component_closed'],
      'stop_reason':r['stop_reason'],'verification_cpu_seconds':time.process_time()-start,
      'state_checks':summaries}
    write(OUT/'verification.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='state_checks'},indent=2))
if __name__=='__main__':main()
