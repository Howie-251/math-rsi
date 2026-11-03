# Why the single-fault star succeeded at degree13

The first complete51418-point graph uses a concrete old route proxy. Prototype51013 is an original sourceextra of degree10. Its complete neighborhood has only one saturated point, corevertex11352 of degree13. Retaining the other9neighbors and connecting the new point to free sourceextra50577 repairs the entire lost part of its routes. The proxy matches the deleted point's complete neighborhood **inside the actual50554-point core**, while its extra neighbors differ. It is not a full false twin.

This analysis uses only the original51417/324451 raw source, the saved3614-target mask and three specified-root distance traversals. It neither rechecks the new graph nor uses an old raw-point orientation, core coloring or geometric reconstruction. The core/extra distinction below is the actual bound label partition: core0..50553, extras50554..51416.

## The literal neighborhood relation

The10 shared core neighbors of deleted11352 and guard50577 are

    C=[45032,45492,46220,47212,47859,48752,48996,49317,49778,50066].

| Old vertex | Role | Degree | Core neighbors | Extra neighbors |
|---|---|---:|---|---|
| 51013 | prototype, sourceextra | 10 | its complete10neighbors | none |
| 11352 | deleted saturated corepin | 13 | exactlyC | 50848,51013,51287 |
| 50577 | free guard, sourceextra | 11 | exactlyC | 51275 |

The prototype's complete neighbor set is[2813,9214,11352,15101,25662,33884,38121,38574,42842,48533]. Deleting11352 leaves the9mandatory pins used by the new point. Guard50577 has two degree slots available in the original source, so one new edge to it is legal. Its existing edges reach the shared core neighbors without consuming new slots at those neighbors, including the already saturated ones.

The frozen initial hypothesis was stronger: N(50577)⊆N(11352). It was **refuted**, since51275 is guard-only. What survives is exact equality of their actual core neighborhoods, and a small explicit change in their extras. This distinction matters for both the route explanation and future screening.

## Which routes were lost and repaired

The retained9pins miss3535core vertices and79extras, total3614. For every such targetx, no retained pin has distance≤4 to x. Since the old prototype has sourceD≤5 routes to x, every prototype→x route of length≤5 must start with deletedpin11352. This is a genuine private route region relative to the retained9pins, not just a large count of unsatisfied vertices.

The targeted old-source distances are:

| Target layer | d(prototype,x) | d(deleted,x) | d(guard,x) | Targets |
|---|---:|---:|---:|---:|
| core | 4 | 3 | 3 | 69 |
| core | 4 | 3 | 4 | 2 |
| core | 5 | 4 | 3 | 6 |
| core | 5 | 4 | 4 | 3458 |
| extras | 4 | 3 | 3 | 8 |
| extras | 5 | 4 | 4 | 71 |

Thus the guard restores all3614targets within4 old steps. It preserves the deleted pin's exact target distance for3606targets, is one step faster for6core targets and one step slower for2core targets. All changes remain within the required radius4.

For3608targets, at least one shortest guard route starts through a shared core neighbor inC. The remaining6core targets have their shortest guard route through the guard-only extra51275. For example:

- Core0:50577→45032→6270→50615→0, length4, through a shared core branch.
- Core14555:50577→51275→45825→14555, length3; deleted11352 has distance4.
- Extra50615:50577→45032→6270→50615, length3, again through a shared core branch.
- Core7384 is a slower case: deleted distance3, guard route50577→45492→13659→47904→7384 of length4.

The saved production target-mask row for guard50577 has popcount3614, matching the whole original target list. This evidence was reused rather than recalculating the completed new graph.

“Private guard branch” here means private among **shortest** guard routes. In particular51275 is the unique shortest first step for the6 faster core targets. It also participates in shortest routes for96of the3614targets. We did not test whether those6 also have length4 routes throughC, so we do not claim51275 is indispensable among all routes of length≤4. Full per-neighbor shortest contributions and actual route examples are in MECHANISM.json.

The deleted-only prototype neighbor51013 cannot supply a short route to any missing target via a retained pin: that would contradict the definition of the missing set. For the2slower targets, a deleted shortest route cannot start inC, or the same route would give guard distance3. Hence their deleted shortest routes use a deleted-only extra branch, while an alternative shared-core route of length4 suffices for the guard. No raw geometric identity is assumed in this deduction.

## One original-base control separates redundancy from seed dependence

Only the first no-guard continuation success was tested on the original base: prototype3962, degree11, deleted saturated pin6216, retained10pins

    [4265,12745,19050,27238,28353,35121,39510,44910,48508,50638].

The frozen prediction was that these pins already cover the original51417vertices, before the first51418seed was present. One multisource depth4 check supports it: **original R4 missing0**, all51417covered, and original neighbor degrees[12,11,11,12,11,11,11,10,11,12] are legal. The existing continuation evidence separately covers all51418vertices of its actual then-current base.

There is an exact local redundancy inside these retained pins. Sourceextra50638 already belongs to the retained10 and has the same10core neighbors as removedpin6216:

    [72,637,1245,1817,2545,3273,3962,4353,4746,49943].

It also has extras51213 and51391. Therefore this case already had a core-neighborhood proxy before the seed was added; the original-base fullR4 check confirms that the extras obligation was also satisfied. The first seed was not necessary for this one case's original-target coverage. This is not a claim about all39later successes, and no alternative graph was generated or counted.

The targeted three-root analysis cost0.2344CPU seconds; this one original-base control cost0.1421CPU seconds, combined0.3765CPU seconds. No other continuation acceptance was retested, and no new graph/all-source BFS was run.

## How this changes source and rule selection

The complete spare-star scan found minimum saturated-neighbor count1 on source13, with91such prototypes. The corresponding minimum on source14 was9. Total free slots alone did not identify this opportunity: source13 offered stars whose existing route structure needed only one obstruction removed, while the same single-fault rule has no prototype on source14.

A concrete next selection rule is to look for a free **proxy of the saturated pin**, prioritizing equal or highly overlapping actual core neighborhoods. First inspect whether a retained neighbor already supplies such a proxy, as50638 does for6216. Otherwise look for a free old point with that core-neighborhood signature, as50577 does for11352. Its extra attachments and the actual private target region then decide whether it truly replaces the lost routes. This is a structural choice of guards, rather than an unmotivated search over all anchor combinations.

Neither equal core neighborhoods nor a low saturated-neighbor count alone guarantees a complete graph. Every accepted candidate must still pass actual current degrees and full current R4 over both core and extras. The differing extra branches in the first example show why that final complete check remains necessary. The original construction roles of these extras—copy, pencil or another author object—have not been identified here; the graph-theoretic proxy relation is exact without naming them.

Evidence: MECHANISM_PREDICTION.json; MECHANISM.json; analyze_mechanism.py; CONTROL_PREDICTION.json; ORIGINALBASE_CONTROL.json; control_original_base.py; first_hit.json; independent_newroot51418.json. Later continuation, global counts and delivery are owned by root and the production agent; no shared Wiki/HTML/ZIP/family was modified here.
