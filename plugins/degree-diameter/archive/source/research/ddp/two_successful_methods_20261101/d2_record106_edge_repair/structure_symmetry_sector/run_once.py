#!/usr/bin/env python3
import time
START=time.process_time()
import collections,itertools,json,math,os,resource,sys
from datetime import datetime,timezone
from pathlib import Path

D=Path(__file__).resolve().parent
C=D.parent
resource.setrlimit(resource.RLIMIT_CPU,(4,4))
F=[7,17,23,34,46,54,59,105]
prior_result=json.loads((C/'structure_probe/RESULT.json').read_text())
prior_terminal=json.loads((C/'structure_probe/TERMINAL.json').read_text())
PRIOR=max(prior_result['case_CPU_seconds'],prior_terminal['case_CPU_seconds'])
PHASES=[]

def dump(name,x):
    (D/name).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def mark(stage,**extra):
    PHASES.append(dict(stage=stage,batch_CPU_seconds=time.process_time()-START,**extra))
    dump('HANDLE.json',dict(pid=os.getpid(),stage=stage,actual_process_started=True,
        batch_CPU_budget_seconds=4,prior_case_CPU_seconds=PRIOR,case_CPU_budget_seconds=20,
        single_worker=True,updated_UTC=datetime.now(timezone.utc).isoformat()))
    dump('BUDGET_LEDGER.json',dict(batch_CPU_budget_seconds=4,prior_case_CPU_seconds=PRIOR,
        case_CPU_budget_seconds=20,stages=PHASES))

class InterfaceFailure(Exception):
    def __init__(self,reason,witness):self.reason=reason;self.witness=witness

def cycles(p):
    unseen=set(range(106));out=[]
    while unseen:
        x=min(unseen);orbit=[];v=x
        while v not in orbit:
            orbit.append(v);unseen.discard(v);v=p[v]
        assert v==x
        out.append(orbit)
    return out

def finish(result,note):
    (D/'NOTE.md').write_text(note+'\n')
    result.update(prior_case_CPU_seconds=PRIOR,
        inherited_RESULT_case_CPU_seconds=prior_result['case_CPU_seconds'],
        inherited_TERMINAL_case_CPU_seconds=prior_terminal['case_CPU_seconds'],
        batch_CPU_seconds=time.process_time()-START,case_CPU_seconds=PRIOR+time.process_time()-START,
        batch_CPU_budget_seconds=4,case_CPU_budget_seconds=20,single_worker=True,pid=os.getpid(),
        source_D2_or_common_neighbor_rechecks=0,graph_BFS=0,solver=0,field_rank_Lean_web_runs=0,
        new_graph_or_parameter_or_Lean_increment=0,old_or_root_Wiki_files_modified=False)
    dump('RESULT.json',result)
    mark('TERMINAL',outcome=result['status'])
    dump('TERMINAL.json',dict(status=result['status'],running=False,all_processes_terminal=True,
        prior_case_CPU_seconds=PRIOR,batch_CPU_seconds=time.process_time()-START,
        case_CPU_seconds=PRIOR+time.process_time()-START,batch_CPU_budget_seconds=4,
        case_CPU_budget_seconds=20,no_automatic_continuation=True))
    print(json.dumps(dict(status=result['status'],pid=os.getpid(),
        batch_CPU_seconds=time.process_time()-START,case_CPU_seconds=PRIOR+time.process_time()-START,
        accepted_permutations=result.get('accepted_permutation_count',0),
        order7=result.get('selected_generator_order')),ensure_ascii=False),flush=True)

def main():
    mark('READING_INHERITED_COLORS_AND_LITERAL_ADJACENCY')
    classes=sorted([sorted(v)for v in prior_result['color_classes']if len(v)==7],key=lambda x:x[0])
    core=next(v for v in prior_result['color_classes']if len(v)==49)
    if len(classes)!=7:raise InterfaceFailure('seven_small_colors_not_present',dict(classes=classes))
    small=set().union(*map(set,classes));color={v:i for i,row in enumerate(classes)for v in row}
    A=[set()for _ in range(106)]
    with (C/'source106.author.adjlist.txt').open()as f:
        for line in f:
            values=list(map(int,line.split()));A[values[0]]=set(values[1:])
    edges=[(u,v)for u in range(106)for v in sorted(A[u])if u<v]
    # Only new structural signatures are checked; no source degree/D2 revalidation.
    unique={}
    for u in sorted(small):
        links={}
        for ci,cl in enumerate(classes):
            n=sorted(A[u]&set(cl))
            if len(n)>1:
                raise InterfaceFailure('small_color_link_not_one_to_one',dict(u=u,color=ci,neighbors=n))
            if n:links[ci]=n[0]
        unique[u]=links
    sectors=[];assigned={}
    for seed in classes[0]:
        queue=[seed];bycolor={color[seed]:seed}
        for u in queue:
            for ci,v in unique[u].items():
                if ci in bycolor and bycolor[ci]!=v:
                    raise InterfaceFailure('sector_color_conflict',dict(seed=seed,vertex=u,color=ci,
                        old=bycolor[ci],new=v))
                if ci not in bycolor:bycolor[ci]=v;queue.append(v)
        if len(bycolor)!=7:
            raise InterfaceFailure('sector_not_complete_seven_colors',dict(seed=seed,bycolor=bycolor))
        row=[bycolor[i]for i in range(7)]
        if any(v in assigned for v in row):
            raise InterfaceFailure('sectors_overlap',dict(seed=seed,row=row))
        for v in row:assigned[v]=len(sectors)
        sectors.append(row)
    if set(assigned)!=small:raise InterfaceFailure('sector_union_not_small49',dict(assigned=sorted(assigned)))
    signatures={};core_sig={}
    for u in sorted(core):
        n=sorted(A[u]&small)
        if len(n)!=7:
            raise InterfaceFailure('core_small_neighbor_count_not_seven',dict(u=u,neighbors=n))
        bycolor=collections.defaultdict(list)
        for v in n:bycolor[color[v]].append(v)
        if any(len(bycolor[i])!=1 for i in range(7)):
            raise InterfaceFailure('core_signature_not_one_per_color',dict(u=u,neighbors_by_color=dict(bycolor)))
        signature=tuple(assigned[bycolor[i][0]]for i in range(7))
        if signature in signatures:
            raise InterfaceFailure('duplicate_core_small_signature',dict(first=signatures[signature],second=u,
                signature=signature))
        signatures[signature]=u;core_sig[u]=signature
    dump('SECTOR_AND_CORE_SIGNATURES.json',dict(fixed=F,small_color_classes=classes,
        sectors_by_color=sectors,core_signatures=[dict(vertex=u,sector_by_color=list(s))for u,s in core_sig.items()]))
    mark('ENUMERATING_AT_MOST_5040_SECTOR_PERMUTATIONS',sectors=7,unique_core_signatures=49)
    accepted=[];reject=collections.Counter();tested=0;complete=True;generator=None
    edge_checks=0
    for perm7 in itertools.permutations(range(7)):
        if time.process_time()-START>3.35:complete=False;break
        tested+=1;p=list(range(106))
        for si,row in enumerate(sectors):
            for ci,v in enumerate(row):p[v]=sectors[perm7[si]][ci]
        fail=False
        for u,sig in core_sig.items():
            target=signatures.get(tuple(perm7[s]for s in sig))
            if target is None:reject['transformed_core_signature_missing']+=1;fail=True;break
            p[u]=target
        if fail:continue
        if len(set(p))!=106:
            raise InterfaceFailure('forced_map_not_bijective',dict(sector_permutation=perm7,permutation=p))
        for u,v in edges:
            edge_checks+=1
            if p[v]not in A[p[u]]:
                reject['literal_edge_not_preserved']+=1;fail=True;break
        if fail:continue
        orb=cycles(p);order=math.lcm(*(len(o)for o in orb))
        record=dict(sector_permutation=list(perm7),permutation=p,order=order,
            actual_edges_checked=len(edges),fixed_labels=F)
        accepted.append(record)
        if order==7 and generator is None:
            generator=dict(**record,orbits=orb)
    dump('ACTUAL_AUTOMORPHISMS.json',dict(complete_sector_permutation_enumeration=complete,
        tested_sector_permutations=tested,accepted=accepted))
    result=dict(status=('ORDER7_AUTOMORPHISM_FOUND'if generator else
                       'COMPLETE_SECTOR_CLASS_NO_ORDER7'if complete else'UNKNOWN_SECTOR_BUDGET_STOP'),
        inherited_partial_propagation_UNKNOWN_preserved=True,new_sector_signature_interface_supported=True,
        fixed_labels=F,small_color_count=7,small_vertices=49,sector_count=7,
        vertices_per_sector=7,core_vertices=49,core_signatures_unique=True,
        sector_permutations_tested=tested,complete_sector_enumeration=complete,
        rejected_reason_counts=dict(reject),accepted_permutation_count=len(accepted),
        actual_edge_membership_checks=edge_checks,full_edges_per_accepted_permutation=len(edges),
        accepted_order_histogram=dict(sorted(collections.Counter(x['order']for x in accepted).items())),
        selected_generator_order=7 if generator else None,generator=generator,
        actual_automorphism_proof='Forced bijection, all582 original edges map to original edges; equal finite edge count gives adjacency iff.',
        generalized_graph_isomorphism_search=False,rewiring_enumeration_started=False)
    if generator:
        dump('ORDER7_GENERATOR_AND_ORBITS.json',generator)
        note='''# Actual C7 sector-signature action, not a graph-distance rerun

The inherited15-label propagation remains historically UNKNOWN. The new, distinct interface succeeded: the49 small labels split into seven forced seven-color sectors; each of the49 remaining core labels has one small neighbor per color and a unique sector signature. SECTOR_AND_CORE_SIGNATURES.json gives the literal data. No common-neighbor or sourceD2 checks were repeated.

Only the at-most5040 sector permutations were tested. Missing transformed core signatures reject a sector permutation before edge checking; all complete forced bijections were checked against every582 actual source edge before acceptance. ACTUAL_AUTOMORPHISMS.json contains the accepted full106-label permutations. Because each is bijective and preserves all edges, edge images have the same cardinality and give adjacency equivalence, not merely a sampled homomorphism. ORDER7_GENERATOR_AND_ORBITS.json contains one actually verified order-seven generator and all its cycles. The eight stated fixed labels are fixed pointwise, and all other98 labels lie in14 seven-cycles.

This proves a concrete C7 source automorphism; it does not prove feasibility of either former or current D2 rewiring model. It also does not need a classification of the entire source automorphism group. No graph was changed or counted.

## Consequences for the next generation rule, on paper only

For a C7-invariant pin set S of size10 or11, there must be exactly one of the14 seven-orbits plus3 or4 of the eight fixed labels. Two nontrivial orbits are already too large; fixed labels alone are too few. If a later candidate rewiring is required to preserve this C7, its edges within the selected seven-orbit are unions of the three undirected cyclic-difference edge orbits (each seven edges), and a selected fixed vertex is connected either to all seven orbit vertices or none. Fixed/fixed edges remain individual choices. This is a genuine new reduction from a proved action, not an assertion that every solution has this symmetry.

For target107/max11/D2, every vertex must have degree at least10, since a degree-d root covers at most1+11d vertices in two steps. With only3/4selected fixed points, an originally absent fixed-to-seven-orbit edge bundle cannot be added: it would add7neighbors to a fixed vertex whose at-most3 original fixed neighbors cannot release enough slots. An originally present bundle cannot be deleted either: after losing7neighbors, adding z and at most3fixed neighbors still leaves degree at most8. Therefore any symmetry-preserving candidate in this small-S shape must keep those fixed/orbit bundles exactly as in the source. Selected fixed vertices can release their new-z slot only by modifying fixed/fixed edges.

Every nonfixed source vertex has degree11. Inside a seven-orbit, source and final invariant internal degrees are even (unions of cyclic-difference rings). Since its selected-fixed incidences are unchanged, adding z forces final orbit-internal degree exactly source orbit-internal degree minus2: cap11 requires a decrease at least1, parity raises it to2, and minimum degree10 prevents a larger decrease. In particular an independent seven-orbit cannot serve as S's orbit under this invariant rule. This is a structural necessary condition, not a newly run orbit-choice or rewiring test.

Old selected/outside common-neighbor obligations and closed domination remain necessary. Orbit edge-count arithmetic alone does not give D2; the existing exact internal-pin model remains the reference for those obligations. No symmetry-preserving rewiring, new S enumeration, solver or candidate graph is started by this note. Root may choose a separate next bounded experiment from these constraints.
'''
    else:
        note='''# Sector-signature symmetry gate terminal

The specific sector/signature interface was supported, and the actual tested prefix/complete sector-permutation result is in RESULT.json. No edge-verified order-seven element was returned. This only concerns the stated sector-permutation rule and the recorded budget; no general graph-isomorphism search or broader no-C7 claim is made. No S=7+3/4 construction is analyzed as a proved symmetry reduction, and no rewiring follows.
'''
    finish(result,note)

try:
    main()
except InterfaceFailure as error:
    finish(dict(status='SECTOR_SIGNATURE_INTERFACE_REFUTED',reason=error.reason,counterexample=error.witness,
        selected_generator_order=None,generalized_graph_isomorphism_search=False),
        '# The specific sector interface failed\nThe exact counterexample is preserved in RESULT.json. No fallback isomorphism search or new symmetry/rewiring pattern was attempted.')
except Exception as error:
    finish(dict(status='UNKNOWN_IMPLEMENTATION_ERROR_NO_RETRY',exception=repr(error),selected_generator_order=None),
        '# One bounded implementation attempt stopped\nThe exception is recorded, all spent CPU counts in this batch, and no retry or mathematical negative conclusion is claimed.')
