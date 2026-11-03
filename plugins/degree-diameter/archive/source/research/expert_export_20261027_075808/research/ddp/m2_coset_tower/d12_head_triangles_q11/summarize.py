"""Summarize the saved 192 actual samples; no new graph or BFS."""
from pathlib import Path
import json
HERE=Path(__file__).resolve().parent
inputs=[json.loads(s) for s in (HERE/'profile.inputs.jsonl').read_text().splitlines()]
rows=[json.loads(s) for s in (HERE/'profile.results.jsonl').read_text().splitlines()]
term=json.loads((HERE/'profile.terminal.json').read_text());meta=json.loads((HERE/'profile.metadata.json').read_text());state=json.loads((HERE/'terminal.json').read_text());best=json.loads((HERE/'profile.best.json').read_text())
assert len(rows)==len(inputs)==192 and all(i['cell_id']==r['cell_id'] and i['S']==r['S'] for i,r in zip(inputs,rows))
def types(r):
 z=r['root_missing_by_target_layer']
 d={'LL':39930*z[0][0]//2,'LB':39930*z[0][1],'LH':39930*z[0][2],
    'BB':3630*z[1][1]//2,'BH':3630*z[1][2],'HH':363*z[2][2]//2}
 assert sum(d.values())==r['bad_unordered_pairs']
 assert 39930*z[0][1]==3630*z[1][0] and 39930*z[0][2]==363*z[2][0] and 3630*z[1][2]==363*z[2][1]
 return d
alltypes=[types(r) for r in rows];qp=[r for r in rows if r['quotient_BB_missing']==0]
with (HERE/'quotient_BB_zero.samples.jsonl').open('w') as f:
 for r in qp:f.write(json.dumps({'parameters':inputs[r['cell_id']],'result':r})+'\n')
groups={}
for i,r in zip(inputs,rows):
 c=i['cell'];key=(c['cross_inverse_pairs'],c['internal_pairs'],c['internal_involutions']);groups.setdefault(key,[]).append(r)
branches=[]
for key,rr in groups.items():
 branches.append({'t':key[0],'internal_pairs':key[1],'internal_involutions':key[2],
  'actual_cells':len(rr),'cell_ids':[r['cell_id'] for r in rr],
  'quotient_BB_zero':sum(r['quotient_BB_missing']==0 for r in rr),
  'original_BB_zero':sum(r['original_BB_missing']==0 for r in rr),
  'minimum_quotient_BB_missing':min(r['quotient_BB_missing'] for r in rr),
  'minimum_original_BB_missing':min(r['original_BB_missing'] for r in rr),
  'minimum_bad_pairs':min(r['bad_unordered_pairs'] for r in rr),
  'root_minimum_missing':[min(r['root_missing'][k] for r in rr) for k in range(3)],
  'root_zero_counts':[sum(r['root_missing'][k]==0 for r in rr) for k in range(3)],
  'head_and_block_zero':sum(r['root_missing'][1]==r['root_missing'][2]==0 for r in rr)})
diag={'scope':'192 saved actual rows only','branches':branches,'best_bad_pair_types':types(best),
 'type_minimum_bad_pairs':{k:min(d[k] for d in alltypes) for k in alltypes[0]},
 'quotient_BB_zero_cell_ids':[r['cell_id'] for r in qp],
 'axis_BB_missing_among_quotient_passes':[r['original_axis_BB_missing'] for r in qp],
 'offaxis_BB_missing_among_quotient_passes':[r['original_offaxis_BB_missing'] for r in qp],
 'all_weighted_type_counts_and_transpose_identities_match':True,'additional_graphs_or_BFS':0}
(HERE/'profile.branch_summary.json').write_text(json.dumps(diag,indent=2)+'\n')
table=[]
for b in branches:table.append(f"| {b['t']} | {b['internal_pairs']} | {b['internal_involutions']} | {b['actual_cells']} | {b['quotient_BB_zero']} | {b['minimum_original_BB_missing']} | {b['minimum_bad_pairs']:,} |")
z=best['root_missing_by_target_layer']
text='''# q11, r3, c2 head-triangle tower: 192-cell profile complete

All **192 authorized cells were scored**, exactly one actual generating set per cell. The result is **no diameter-5 graph**, **one quotient-BB pass**, and **zero original-BB passes**. The full q11 family remains open: these samples are not an exhaustive generating-set search, and no additional sample or parameter was started.

The observed minimum original BB missing is **153**. The single quotient-complete sample is cell186 (t=4); all153 missing original block targets have v=0, with zero offaxis missing. Thus the fixed-axis issue occurs in an actual sample even after its quotient is complete. This is not a uniform impossibility proof. Every sample was actually expanded and given three complete BFS traversals; BB was only a diagnostic.

## Actual group, graph and deterministic cells

The read mathematical interfaces are [HEAD_TRIANGLE_PARAMETER_EXTENSION.md](../d8_head_triangles/HEAD_TRIANGLE_PARAMETER_EXTENSION.md) and [HEAD_TRIANGLE_Q11_PROFILE_DESIGN.md](../d8_head_triangles/HEAD_TRIANGLE_Q11_PROFILE_DESIGN.md), together with the latter's actual192-cell JSON. We used q11,r3,c2 exactly, with field arithmetic modulo11, never XOR.

A=F11²×C3 has coordinates(u,v,w), encoding x=u+11v+121w. K has coordinates(b,j), encoding b+11j, and

    (b,j)(d,l)=(b+2^(2j)d mod11,j+l mod10),
    (b,j)(u,v,w)=(2^(3j)u+b*2^j*v,2^j*v,w).

G multiplication is(x,k)(y,l)=(x+k(y),kl). K inverse is(-2^(-2j)b,-j); G inverse is(-k^-1(x),k^-1), with w negated modulo3. All39,930 group inverses and4,392,300 K-action composition identities were checked in both the sample preparer and the compiled group engine.

Leaves are g=x+363(b+11j); parent blocks are39930+x+363j; heads are43560+x. Each leaf has11 Cayley neighbors and one parent block; each block has11 leaves and one head. For each of the121(u,v) values, all three w-heads form K3, adding363 actual head edges. Layer sizes are**39930/3630/363**, for**43,923 vertices, degree12, 263,538 edges**. Every graph builder invocation checks all degrees, loops and repeated neighbors.

The fixed seed is**2026102611**, using one Python random.Random/MT19937 stream in design cell_id order. Actual component pools are sorted by integer code; inverse pairs use their smaller endpoint as representative. For every cell we draw the two marked A/B anchors' unrestricted K codes, then extra cross representatives in O/A/B order, then within each O/A/B color draw the requested internal pairs followed by involutions. Pool counts are pairs54/545/5995, involutions1/10/110 and w1 cross representatives110/1100/12100. Anchors have field vectors(1,0),(0,1), and extra cross representatives exclude the chosen anchors.

The actual eleven-element S for every cell is checked to be distinct, nonidentity, inverse closed, and to have exactly the requested cross/pair/involution colors. Actual K-orbit HH coverage contains all363 head targets in every sample. All192 S are distinct and are saved with component choices and full coordinates in`profile.inputs.jsonl`. The t=2/3/4 sample counts are exactly**81/81/30**. For t>2 the marked normalization is not a claim of uniform sampling of unmarked sets or graph isomorphism classes.

## Exact original and quotient BB diagnostics

The implementation computes**ten** original masks, one per K/H index. Each mask contains363 actual targets. It retains the exact R_j, P, Q_j and two head-triangle terms from the design. H saturation fixes(u,0,w) individually and fills all11 u-values when v is nonzero. The full group products are taken before saturation; their order is unchanged.

Independently formed projected words use(v,w,j), order330, and give ten33-bit quotient masks. Projected generator collisions and identity projections remain legal. For every sample, projected original masks equal the explicitly computed quotient masks. Every missing quotient target corresponds to11 missing original targets. A quotient pass forces all original offaxis BB targets covered, leaving at most330 possible axis targets.

All**696,960 original BB targets** across192 samples were compared individually with actual block-root BFS and match. The first actual complete graph and its mask data are saved as`preflight.edges/json`; it was then reused as the first scored sample without another BFS. No independent preflight check was requested. Every sample has three complete BFS, not just a formula score or root sample used without a symmetry argument.

Left G acts transitively on each layer and preserves the head triangles, so the exact bad unordered pair total is

    (39930*m_leaf+3630*m_block+363*m_head)/2.

Global root minima are**624/800/150**, and all three root-zero counts are0. Original-BB-zero and complete block-plus-head-root counts are also0. Different samples may attain different coordinatewise minima. Type-specific minima and transposed type identities from the saved rows are in`profile.branch_summary.json`; this arithmetic did not generate another graph or run BFS.

## Component-branch results

Each row aggregates exactly the cells prescribed for its t, internal-pair and internal-involution counts. There were zero original BB passes in every row.

| Cross pairs t | Internal pairs | Internal involutions | Cells scored | Quotient BB passes | Minimum original BB missing | Minimum bad pairs |
|---:|---:|---:|---:|---:|---:|---:|
'''+ '\n'.join(table)+f'''

The complete per-cell results, original/quotient masks, axis/offaxis BB split, root distances and actual eccentricities are in`profile.results.jsonl`. The actual three t-branch root/layer minima and zero counts are in`profile.terminal.json`; the nine component-branch summaries are in`profile.branch_summary.json`.

## Saved best actual sample

The saved graph minimizes the exact bad-pair total among these192 actual samples only:

    cell_id={best['cell_id']}, cross pairs t={best['cross_inverse_pairs']}
    S={best['S']}
    root missing={best['root_missing']}
    root eccentricities={best['root_eccentricities']}
    missing by source/target L/B/H:
      {z[0]}
      {z[1]}
      {z[2]}
    bad unordered pairs={best['bad_unordered_pairs']:,}
    quotient BB missing={best['quotient_BB_missing']}
    original BB missing={best['original_BB_missing']} (axis157, offaxis77).

The exact type counts are{types(best)}. The complete edge list and parameters are`profile.best.edges` and`profile.best.json`. Representative eccentricities imply diameter7 under the layer-transitive action; independent final all-source verification remains a separate check below.

Cell186, the sole quotient pass and minimum-original-BB sample, has roots799/903/1890, bad17,934,015, and original BB153 entirely on the axis. Its actual parameters and already-computed diagnostics are preserved in`quotient_BB_zero.samples.jsonl`; it was not expanded or rescored again after the profile. This sample is distinct from the minimum-bad-pair choice.

## Budget and terminal state

One worker completed the full fixed profile with no restart or budget extension. Preparation and compilation used1.808050 CPU seconds; the profile driver used1.495981 seconds; total**3.304038 CPU seconds** is below the separate60-second allowance. The C++ process itself used1.493053 seconds: formula diagnostics0.008001, graph build0.485174, actual BFS0.556844, with remaining time in initialization/output and other work. Independent final checking is separately accounted.

Actual cursor is192 and status`PROFILE_COMPLETE`; no process remains running. The implementation is`prepare.py`, `profile.cpp`, and`run_profile.py`. Tables, actual component lists, seeds, scope, checkpoints and terminal state are retained in`structure_tables.json`, `generator_lists.json`, `profile.metadata.json`, `profile.run.json`, `profile.log` and`terminal.json`. The profile neither proves all192 cells impossible nor closes the full q11 family.

## Independent final check

Pending the parent-owned single independent reconstruction and all-source check of`profile.best.edges`. No independent first-sample or historical graph recheck is requested. This section will be amended with the actual result and CPU cost.
'''
# Keep mathematical symbols readable without changing code identifiers.
for a,b in [('All39','All 39'),('and4,','and 4,'),('are39930','are 39930'),('are43560','are 43560'),('has11','has 11'),('the121','the 121'),('adding363','adding 363'),('in`','in `'),('as`','as `'),('is`','is `'),('of`','of `'),('are`','are `'),('used1.','used 1.'),('diagnostics0.','diagnostics 0.'),('build0.','build 0.'),('BFS0.','BFS 0.'),('cursor is192','cursor is 192'),('below the separate60','below the separate 60')]:text=text.replace(a,b)
(HERE/'REPORT.md').write_text(text)
state['report']='REPORT.md';state['no_running_process']=True;state['new_record']=False;state['full_family_open']=True;state['best_bad_pair_types']=types(best)
(HERE/'terminal.json').write_text(json.dumps(state,indent=2)+'\n')
print(json.dumps({'report':'REPORT.md','by_component_branches':branches,'best_types':types(best)},indent=2))
