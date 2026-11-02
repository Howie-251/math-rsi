"""Report the actual completed or budget-stopped production; no graph construction/BFS."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
term=json.loads((HERE/'production.terminal.json').read_text())
meta=json.loads((HERE/'production.metadata.json').read_text())
summary=json.loads((HERE/'production.summary.json').read_text())
best=json.loads((HERE/'production.best.json').read_text())
allstats=term['counts'];conditional=allstats['BB_survivor_stats']
assert best['S'] and sum([2790*best['root_missing'][0],465*best['root_missing'][1],93*best['root_missing'][2]])==2*best['bad_unordered_pairs']
layer=best['root_missing_by_target_layer']
types={'LL':2790*layer[0][0]//2,'LB':2790*layer[0][1],'LH':2790*layer[0][2],
       'BB':465*layer[1][1]//2,'BH':465*layer[1][2],'HH':93*layer[2][2]//2}
assert sum(types.values())==best['bad_unordered_pairs']
complete=term['status']=='COMPLETE_NO_SOLUTION' and term['next_cursor']==18829360
if complete:
 finding='The complete 18,829,360-input safely reduced marked scope was checked with no diameter-5 graph. By the preserved scope in SCOPE.md this computationally excludes all HH-compatible generating sets in this fixed cyclic head-triangle tower. It does not exclude arbitrary degree-7 graphs or the whole M2 mechanism.'
elif term['status']=='D5_CANDIDATE':
 finding='A diameter-5 candidate was found and the production stopped immediately. Its independent full-source check and the current public lower-bound comparison remain separate acceptance steps; no new-record claim is made here.'
else:
 finding='The production stopped at the CPU boundary with the actual cursor saved. This is a partial prefix and does not exclude the full normalized scope or the construction family.'
names=['t1: four involutions','t1: one pair plus two involutions','t1: two pairs','t2: two involutions','t2: one nonzero pair']
rows=[]
for label,m,s in zip(names,meta['branches'],term['per_branch']):
 ss=s['BB_survivor_stats'];rootmins='—' if not ss else '/'.join(map(str,ss['root_minimum_missing']))
 joint=0 if not ss else ss['head_and_block_zero']
 rows.append(f"| {m['branch']} {label} | {m['safe_16_anchor_inputs']:,} | {s['HH_legal_inputs_checked']:,} | {s['BB_pass']:,} | {rootmins} | {joint} |")
conditional_text='No BB survivors were scored.' if conditional is None else f"Among the **{conditional['scored']:,} BB survivors**, root minima are **{conditional['root_minimum_missing']}**, root-zero counts are **{conditional['root_zero_counts']}**, and **{conditional['head_and_block_zero']:,}** inputs have both block and head roots complete. These are conditional counts; rejected BB inputs were not BFS-scored. Coordinatewise minima can occur on different inputs."
text=f'''# p31 cyclic head-triangle tower: production result

**Actual terminal: `{term['status']}`**, cursor **{term['next_cursor']:,} / 18,829,360**.

{finding}

The earlier 1,400 random stratified samples are preserved in [PROFILE_REPORT.md](PROFILE_REPORT.md). They were not an enumeration prefix, were not subtracted from production, and their scores were not used as cached production results. Only their 1,400 already-saved BB masks were reused for formula calibration, without generating a graph or running BFS. The separate p43 profile is finished and paused; its sole final independent check found D6, not D5.

## Preserved scope and exact iterator

[SCOPE.md](SCOPE.md) proves the 35,305,050 marked parent range covers every HH-compatible inverse-closed six-element set for this fixed tower. The action uses G=(F31⋊_3 C30)×C3, H=<k^5>, K=C30. HH compatibility forces t=1 or2 cross inverse pairs, at least one nonzero-field cross component, and at least one nonzero-field internal component. A marked nonzero w1 representative is scaled to (1,1,j).

The authorized safe reduction uses T_j=F_(-3^j) composed with C3 inversion, mapping the marked exponent j to -j. It keeps all **16 layers j=0..15**, including **all parameters at fixed layers 0 and15**. Other cross representatives transform as (x,1,k) -> (3^(j-k)x,1,-k), and internal field coordinates scale by -3^j. This is the proved coverage reduction of SCOPE §6, not division by two or a claim of free action. Multiple markings in t2 remain allowed.

Actual internal pools are 31 involutions and 449 noninvolutory inverse pairs, of which 14 pairs have zero field. The five C++ internal lists have sizes **31,465 / 208,785 / 100,485 / 465 / 435**. The t1 two-pair list omits only pairs of zero-field components; the t2 pair list requires nonzero field. For t2, the second w1 representative is encoded by ci=0..929 and only ci=31*j+1 is excluded, exactly the marked anchor. Its field may be zero. Different inverse components are disjoint by construction.

The iterator order is branch, actual internal-set index, j=0..15, then the second w1 representative for t2. It starts at cursor0 and includes an exact cursor formula checked during production. All actual branch counts match the independent SCOPE.json arithmetic and a narrow independent read-only check found no omitted component or fixed layer. The actual scope is **18,829,360**, split into t1 **5,451,760** and t2 **13,377,600**.

| Branch | Full safe scope | Actually checked | BB passes / actual scores | Conditional root minima L/B/H | Full B+H roots |
|---|---:|---:|---:|---|---:|
'''+ '\n'.join(rows)+f'''

## Exact filter, actual graphs and statistics

Every input in this iterator satisfies HH. The original BB reachable sets are computed exactly in five multiplicative-H-orbit masks, each containing 18 bits. All nonzero field orbits have size6; zero-field orbits have size1 and are always covered by identity/head-triangle routes. Thus BB missing is a multiple of6. The same formula's masks match all 1,400 prior actual block-root BFS results. The necessary BB test is the only production filter.

All **{allstats['BB_pass']:,} BB survivors** actually pass through graph expansion and three-root depth-5 BFS, with a pointwise check against all465 BB targets. Leaves=2790, blocks=465, heads=93; n=3348, degree7, edges=11718. The builder includes all93 head-triangle edges and checks simple regular adjacency. Left G preserves all graph edges and acts transitively on each layer, so weighted root scores give the exact total of bad unordered pairs.

{conditional_text}

Complete block/head-root candidates are saved in `production.block_head_complete.jsonl`, with actual generating sets, positions and scores. These are not successes unless their leaf root is also complete. The first such candidate was cursor1,194,332, S=[1148,1763,294,2538,1414,1416], with roots242/0/0 and 337,590 bad unordered pairs, all LL. This observation changed which route condition remained open in that candidate but did not justify skipping LL.

The global and per-branch exact BB histograms/counts and conditional root/layer statistics are in `production.terminal.json`. No full-root population is claimed for inputs rejected by BB. Next position is `{term['next_position']}`.

## Saved final graph

Selection: `{best['selection']}`. This minimizes bad pairs among the actually scored BB survivors in the executed range, not among BB-rejected inputs.

    position={best['position']}
    S={best['S']}
    root missing={best['root_missing']}
    layer missing L/B/H:
      {layer[0]}
      {layer[1]}
      {layer[2]}
    bad unordered pairs={best['bad_unordered_pairs']:,}

Its type counts are {types}. These follow from the recorded exact representative-root distances, without another BFS. Complete edges and actual parameters are `production.best.edges` and `production.best.json`. If an independently verified D5 graph is not returned, this diagnostic cannot count as a new lower bound.

## Actual budget and terminal evidence

The fixed budget is one worker and cumulative **360 CPU seconds**, including the preceding shared profiles' 2.805399 seconds. New preparation, compilation and saved-mask calibration cost {summary['new_preparation_CPU_seconds']:.6f} seconds. Production driver's actual cost was {summary['production_driver_CPU_seconds']:.6f} seconds; cumulative implementation/profile/production cost is **{summary['cumulative_CPU_seconds']:.6f} seconds**. Independent final verification is separately recorded. No process restart, extra parameter, seed continuation or budget enlargement occurred.

The first100,000 actual inputs cost0.211690 CPU seconds, with0.194087 seconds in the BB frontend and no surviving graph in that first four-involution prefix. This was explicitly not treated as the full-production cost estimate; subsequent actual BFS costs remained inside the same process budget. `production.first100k.json`, `production.log`, `production.run.json`, `production.prepare.json` and `production.summary.json` preserve the real checkpoints and final cursor.

## Independent final verification

The parent will trigger exactly one independent reconstruction and all-source check of this final production graph. The earlier p31 profile-best and first sample were not independently full-source checked; no duplicate check is requested. This section will be updated with the actual final-check result.
'''
(HERE/'REPORT.md').write_text(text)
t=json.loads((HERE/'terminal.json').read_text());t['report']='REPORT.md';t['complete_safe_scope_checked']=complete;t['new_record']=False;t['no_running_process']=True;t['best_pair_types']=types
(HERE/'terminal.json').write_text(json.dumps(t,indent=2)+'\n')
print(json.dumps({'status':term['status'],'cursor':term['next_cursor'],'best':best,'types':types,'conditional_stats':conditional},indent=2))
