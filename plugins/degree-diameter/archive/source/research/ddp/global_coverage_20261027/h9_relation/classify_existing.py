"""N_core structural signatures and one explicit relabel comparison; no distances."""
from pathlib import Path
from collections import defaultdict, Counter
import json,lzma,time

OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[3]
K=41356;OLDN=41699;NEWN=42342
oldpath=ROOT/'research/ddp/breadth_20261027_wave3/hexagon_partial_fold_scout/partial_fold_source/graph_d12k5_n41699.edges.xz'
newpath=ROOT/'research/ddp/breadth_20261027_wave4/pencil_source/deg12_diam5_n42342.txt'
started=time.process_time();oa=[set() for _ in range(OLDN)]
with lzma.open(oldpath,'rt') as f:
    assert tuple(map(int,f.readline().split()))==(41699,237699)
    for line in f:
        if line.strip():
            u,v=map(int,line.split());oa[u].add(v);oa[v].add(u)
na=[]
for line in newpath.read_text().splitlines():
    if not line.strip() or line.startswith('#'):continue
    vals=list(map(int,line.split()));assert vals[0]==len(na);na.append(set(vals[1:]))
assert len(na)==NEWN
# Core equality was established by the prior one-off full edge comparison;
# here its common adjacency defines signatures, not geometric point types.
core=[{v for v in na[u] if v<K} for u in range(K)]
prototypes=defaultdict(list)
for u in range(K):prototypes[tuple(sorted(core[u]))].append(u)
def sig(adj,v):return tuple(sorted(x for x in adj[v] if x<K))
oldgroups=defaultdict(list);newgroups=defaultdict(list)
for v in range(K,OLDN):oldgroups[sig(oa,v)].append(v)
for v in range(K,NEWN):newgroups[sig(na,v)].append(v)
oldcopygroups=defaultdict(list)
for v in range(K,41636):oldcopygroups[sig(oa,v)].append(v)
newcopylike={v for s,vs in newgroups.items() if s in prototypes for v in vs}
noncopylike=[v for v in range(K,NEWN) if v not in newcopylike]
records=[]
for s,vs in sorted(newgroups.items(),key=lambda x:x[1][0]):
    for v in vs:
        records.append(dict(vertex=v,N_core=list(s),copy_like=bool(prototypes.get(s)),
            core_prototype_ids=prototypes.get(s,[]),old_extra_ids_same_N_core=oldgroups.get(s,[]),
            old_H3copy_ids_same_N_core=oldcopygroups.get(s,[]),
            current_extra_neighbors=sorted(w for w in na[v] if w>=K)))
def block_check(pool):
    ids=sorted(pool);missing=[];extra=[];expected_count=actual_count=0
    for ii,u in enumerate(ids):
        pu=prototypes[sig(na,u)][0]
        for v in ids[ii+1:]:
            pv=prototypes[sig(na,v)][0]
            ex=pv in core[pu];ac=v in na[u];expected_count+=ex;actual_count+=ac
            if ex and not ac:missing.append([u,v])
            if ac and not ex:extra.append([u,v])
    return dict(vertices=len(ids),expected_clone_block_edges=expected_count,actual_edges=actual_count,
                missing_required_edges=len(missing),extra_edges=len(extra),
                exact_clone_blowup_adjacency=not missing and not extra,
                first_missing=missing[:16],first_extra=extra[:16])
allblock=block_check(newcopylike)
old_H3_pool={v for s in oldcopygroups for v in newgroups.get(s,[]) if s in prototypes}
h3block=block_check(old_H3_pool)
def explicit_map_check(oldids):
    group=defaultdict(list)
    for v in oldids:group[sig(oa,v)].append(v)
    mapping={};unmapped=[];supply=[]
    for s,ids in sorted(group.items(),key=lambda x:x[1][0]):
        candidates=newgroups.get(s,[]) if s in prototypes else []
        for a,b in zip(ids,candidates):mapping[a]=b
        unmapped.extend(ids[len(candidates):])
        supply.append(dict(N_core=list(s),core_prototype_ids=prototypes.get(s,[]),
                           old_extra_ids=ids,current_candidate_ids=candidates,
                           old_count=len(ids),current_count=len(candidates),
                           shortfall=max(0,len(ids)-len(candidates))))
    ids=sorted(mapping);mismatches=[]
    for i,u in enumerate(ids):
        for v in ids[i+1:]:
            before=v in oa[u];after=mapping[v] in na[mapping[u]]
            if before!=after:mismatches.append(dict(old_edge=[u,v],new_edge=[mapping[u],mapping[v]],old_adjacent=before,new_adjacent=after))
    return dict(scope='fixed common core identity; sorted within each identicalN_core signature, no embedding search',
                old_extra_vertices=len(oldids),signature_pairable=len(mapping),unmapped_old_ids=sorted(unmapped),
                mappings=[[v,mapping[v]] for v in ids],tail_tail_mismatches=len(mismatches),
                first_tail_tail_mismatches=mismatches[:20],
                mapped_subset_is_exact_induced_extension_of_common_core=not mismatches,
                full_old_extra_set_retained_under_this_map=not unmapped and not mismatches,
                signature_supply=supply)
map280=explicit_map_check(list(range(K,41636)))
map343=explicit_map_check(list(range(K,OLDN)))
oldclass=dict(H3copy280_Ncore_matches_core_prototype=sum(sig(oa,v) in prototypes for v in range(K,41636)),
              padding63_Ncore_matches_core_prototype=sum(sig(oa,v) in prototypes for v in range(41636,OLDN)))
hist=Counter(len(prototypes[sig(na,v)]) for v in range(K,NEWN))
result=dict(status='COMPLETE_STRUCTURAL_SIGNATURE_CLASSIFICATION_NO_DISTANCES',common_core=K,current_extras=NEWN-K,
            current_copylike_extras=len(newcopylike),current_not_core_full_neighborhood_clone=len(noncopylike),
            current_noncopylike_ids=noncopylike,current_prototype_candidate_count_histogram=dict(hist),
            old_extra_classification=oldclass,all_current_copylike_block_check=allblock,
            current_pool_matching_old280_signatures_block_check=h3block,
            old280_explicit_relabel_check=map280,old343_explicit_relabel_check=map343,
            type_warning='copylike means N_core equals a core full neighborhood only; not an H3copy/pencil geometric identification',
            relation_warning='A current vertex may carry additional edges to noncopylike extras. Old-copy retention tests compare actual selected tail-tail adjacencies, not signatures alone.',
            no_graph_isomorphism_or_embedding_search=True,no_distances_or_BFS=True,
            CPU_seconds=time.process_time()-started)
(OUT/'structural_classification.json').write_text(json.dumps(result,indent=2)+'\n')
(OUT/'current_extra_signatures.json').write_text(json.dumps(dict(records=sorted(records,key=lambda x:x['vertex'])),indent=2)+'\n')
print(json.dumps({k:result[k] for k in ['current_extras','current_copylike_extras','current_not_core_full_neighborhood_clone','current_prototype_candidate_count_histogram','old_extra_classification','all_current_copylike_block_check','current_pool_matching_old280_signatures_block_check','CPU_seconds']},indent=2))
for name,val in [('old280',map280),('old343',map343)]:print(name,{k:v for k,v in val.items() if k in ['signature_pairable','tail_tail_mismatches','mapped_subset_is_exact_induced_extension_of_common_core','full_old_extra_set_retained_under_this_map']},'unmapped',len(val['unmapped_old_ids']))
