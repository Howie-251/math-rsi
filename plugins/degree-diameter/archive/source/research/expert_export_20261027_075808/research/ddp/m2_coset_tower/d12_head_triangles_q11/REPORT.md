# q11, r3, c2 head-triangle tower: 192-cell profile complete

All **192 authorized cells were scored**, exactly one actual generating set per cell. The result is **no diameter-5 graph**, **one quotient-BB pass**, and **zero original-BB passes**. The full q11 family remains open: these samples are not an exhaustive generating-set search, and no additional sample or parameter was started.

The observed minimum original BB missing is **153**. The single quotient-complete sample is cell186 (t=4); all153 missing original block targets have v=0, with zero offaxis missing. Thus the fixed-axis issue occurs in an actual sample even after its quotient is complete. This is not a uniform impossibility proof. Every sample was actually expanded and given three complete BFS traversals; BB was only a diagnostic.

## Actual group, graph and deterministic cells

The read mathematical interfaces are [HEAD_TRIANGLE_PARAMETER_EXTENSION.md](../d8_head_triangles/HEAD_TRIANGLE_PARAMETER_EXTENSION.md) and [HEAD_TRIANGLE_Q11_PROFILE_DESIGN.md](../d8_head_triangles/HEAD_TRIANGLE_Q11_PROFILE_DESIGN.md), together with the latter's actual192-cell JSON. We used q11,r3,c2 exactly, with field arithmetic modulo11, never XOR.

A=F11²×C3 has coordinates(u,v,w), encoding x=u+11v+121w. K has coordinates(b,j), encoding b+11j, and

    (b,j)(d,l)=(b+2^(2j)d mod11,j+l mod10),
    (b,j)(u,v,w)=(2^(3j)u+b*2^j*v,2^j*v,w).

G multiplication is(x,k)(y,l)=(x+k(y),kl). K inverse is(-2^(-2j)b,-j); G inverse is(-k^-1(x),k^-1), with w negated modulo3. All 39,930 group inverses and 4,392,300 K-action composition identities were checked in both the sample preparer and the compiled group engine.

Leaves are g=x+363(b+11j); parent blocks are 39930+x+363j; heads are 43560+x. Each leaf has 11 Cayley neighbors and one parent block; each block has 11 leaves and one head. For each of the 121(u,v) values, all three w-heads form K3, adding 363 actual head edges. Layer sizes are**39930/3630/363**, for**43,923 vertices, degree12, 263,538 edges**. Every graph builder invocation checks all degrees, loops and repeated neighbors.

The fixed seed is**2026102611**, using one Python random.Random/MT19937 stream in design cell_id order. Actual component pools are sorted by integer code; inverse pairs use their smaller endpoint as representative. For every cell we draw the two marked A/B anchors' unrestricted K codes, then extra cross representatives in O/A/B order, then within each O/A/B color draw the requested internal pairs followed by involutions. Pool counts are pairs54/545/5995, involutions1/10/110 and w1 cross representatives110/1100/12100. Anchors have field vectors(1,0),(0,1), and extra cross representatives exclude the chosen anchors.

The actual eleven-element S for every cell is checked to be distinct, nonidentity, inverse closed, and to have exactly the requested cross/pair/involution colors. Actual K-orbit HH coverage contains all363 head targets in every sample. All192 S are distinct and are saved with component choices and full coordinates in `profile.inputs.jsonl`. The t=2/3/4 sample counts are exactly**81/81/30**. For t>2 the marked normalization is not a claim of uniform sampling of unmarked sets or graph isomorphism classes.

## Exact original and quotient BB diagnostics

The implementation computes**ten** original masks, one per K/H index. Each mask contains363 actual targets. It retains the exact R_j, P, Q_j and two head-triangle terms from the design. H saturation fixes(u,0,w) individually and fills all11 u-values when v is nonzero. The full group products are taken before saturation; their order is unchanged.

Independently formed projected words use(v,w,j), order330, and give ten33-bit quotient masks. Projected generator collisions and identity projections remain legal. For every sample, projected original masks equal the explicitly computed quotient masks. Every missing quotient target corresponds to11 missing original targets. A quotient pass forces all original offaxis BB targets covered, leaving at most330 possible axis targets.

All**696,960 original BB targets** across192 samples were compared individually with actual block-root BFS and match. The first actual complete graph and its mask data are saved as `preflight.edges/json`; it was then reused as the first scored sample without another BFS. No independent preflight check was requested. Every sample has three complete BFS, not just a formula score or root sample used without a symmetry argument.

Left G acts transitively on each layer and preserves the head triangles, so the exact bad unordered pair total is

    (39930*m_leaf+3630*m_block+363*m_head)/2.

Global root minima are**624/800/150**, and all three root-zero counts are0. Original-BB-zero and complete block-plus-head-root counts are also0. Different samples may attain different coordinatewise minima. Type-specific minima and transposed type identities from the saved rows are in `profile.branch_summary.json`; this arithmetic did not generate another graph or run BFS.

## Component-branch results

Each row aggregates exactly the cells prescribed for its t, internal-pair and internal-involution counts. There were zero original BB passes in every row.

| Cross pairs t | Internal pairs | Internal involutions | Cells scored | Quotient BB passes | Minimum original BB missing | Minimum bad pairs |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 0 | 7 | 11 | 0 | 1188 | 410,935,965 |
| 2 | 1 | 5 | 25 | 0 | 356 | 98,169,720 |
| 2 | 2 | 3 | 30 | 0 | 192 | 27,323,010 |
| 2 | 3 | 1 | 15 | 0 | 166 | 16,845,015 |
| 3 | 0 | 5 | 21 | 0 | 338 | 102,489,420 |
| 3 | 1 | 3 | 39 | 0 | 159 | 23,928,960 |
| 3 | 2 | 1 | 21 | 0 | 196 | 14,133,405 |
| 4 | 0 | 3 | 18 | 0 | 217 | 26,646,015 |
| 4 | 1 | 1 | 12 | 1 | 153 | 17,934,015 |

The complete per-cell results, original/quotient masks, axis/offaxis BB split, root distances and actual eccentricities are in `profile.results.jsonl`. The actual three t-branch root/layer minima and zero counts are in `profile.terminal.json`; the nine component-branch summaries are in `profile.branch_summary.json`.

## Saved best actual sample

The saved graph minimizes the exact bad-pair total among these192 actual samples only:

    cell_id=142, cross pairs t=3
    S=[5884, 6861, 10531, 14279, 17919, 20023, 24952, 29291, 33035, 36444, 38574]
    root missing=[624, 870, 530]
    root eccentricities=[6, 7, 6]
    missing by source/target L/B/H:
      [565, 56, 3]
      [616, 234, 20]
      [330, 200, 0]
    bad unordered pairs=14,133,405
    quotient BB missing=7
    original BB missing=234 (axis157, offaxis77).

The exact type counts are{'LL': 11280225, 'LB': 2236080, 'LH': 119790, 'BB': 424710, 'BH': 72600, 'HH': 0}. The complete edge list and parameters are `profile.best.edges` and`profile.best.json`. Representative eccentricities imply diameter7 under the layer-transitive action; independent final reconstruction and orbit-root verification remain a separate check below.

Cell186, the sole quotient pass and minimum-original-BB sample, has roots799/903/1890, bad17,934,015, and original BB153 entirely on the axis. Its actual parameters and already-computed diagnostics are preserved in `quotient_BB_zero.samples.jsonl`; it was not expanded or rescored again after the profile. This sample is distinct from the minimum-bad-pair choice.

## Budget and terminal state

One worker completed the full fixed profile with no restart or budget extension. Preparation and compilation used 1.808050 CPU seconds; the profile driver used 1.495981 seconds; total**3.304038 CPU seconds** is below the separate 60-second allowance. The C++ process itself used 1.493053 seconds: formula diagnostics 0.008001, graph build 0.485174, actual BFS 0.556844, with remaining time in initialization/output and other work. Independent final checking is separately accounted.

Actual cursor is 192 and status`PROFILE_COMPLETE`; no process remains running. The implementation is `prepare.py`, `profile.cpp`, and`run_profile.py`. Tables, actual component lists, seeds, scope, checkpoints and terminal state are retained in `structure_tables.json`, `generator_lists.json`, `profile.metadata.json`, `profile.run.json`, `profile.log` and`terminal.json`. The profile neither proves all192 cells impossible nor closes the full q11 family.

## Independent final check

The parent-owned single independent check is complete. All 263,538 edges match an independent reconstruction, confirming a simple connected 12-regular graph. Complete BFS from the three proved layer-orbit roots gives eccentricities 6/7/6, diameter 7 and 14,133,405 bad unordered pairs; the root missing counts are 624/870/530. All 3,630 original BB targets and ten saved masks agree, including axis157/offaxis77. As directed, no additional traversal from all 43,923 roots was run. `INDEPENDENT_CHECK.md` proves the left-action preservation of the head triangles; `profile.best.independent_check.json` and `best.independent_verify.json` preserve the actual result. Independent CPU was 0.822879706 seconds, giving 4.126917706 seconds including this profile and preparation. No independent preflight or historical graph recheck occurred; there is no pending check.
