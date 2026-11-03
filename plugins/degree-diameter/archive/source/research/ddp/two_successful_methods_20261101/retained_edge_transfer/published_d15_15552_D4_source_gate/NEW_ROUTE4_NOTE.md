# Actual15552 route4: fullrank hypothesis refuted, onepair allx coset cover supported

No pre-existing actual length4 source certificate was found in the reviewed
source/recovery reports. The historical source-gap report explicitly left
such a calculation undone. Old13608 charts are a different source and were
not used. This one new experiment uses only the saved actual960 arcs and
the five literal(B,v,c) types; it generates no graph and runs no BFS, old
atomic field/kernel-rank checker, solver, Lean, query or paid review.

## Fullrank4 words do not cover every controller pair

The actual five types have exactly one outgoing arc per type at every one
of the192 controllers. Their full literal transition table is saved in
NEW_ROUTE4_TYPES_AND_TRANSITIONS.json. Type numbering is first appearance
in the actual affine table, not an idealized five-direction model.

For a length4 word, the computed noise columns are exactly
B4*B3*B2*v1, B4*B3*v2, B4*v3, v4. These are new composed-route ranks; the
rank3 assertions for the five atomicB maps were not recomputed. Among625
words the ranks are1:5,2:90,3:274,4:256. All256 rank4 words have saved
actual inverse-noise matrices inNEW_ROUTE4_WORDS625.json.

Following each literal typeword from every actual sourcecontroller yields
33216 fullrank-covered orderedcontrollerpairs and3648 missing ones:
192 equal-layer,192 distinct adjacent-layer,3264 other pairs. Allmissing
pairs are stored without sampling inNEW_ROUTE4_MISSING_PAIRS.json. Thus the
strong single-fullrank-word hypothesis is REFUTED. This is not a failure
of the published source's D4 guarantee or the actual16389 finalgraph.

## Exactly one missingpair was examined in detail

Select the lexicographically firstmissingpair(0,0), as frozen before running.
All781 typewords oflength0..4 were considered, and61 reach this pair:
length0:1, length1:1, length2:5, length3:9, length4:45. Their individual
noise-image sizes are1 for1 word,3 for12 words, and9 for48 words; none is
close to a single81-point fullrank image. Nevertheless their affine-image
union coversall81 targets at x=(0,0,0,0) and at the one preselected basis
start e0=(1,0,0,0). No other start or secondmissingpair was tested.

These61 routes fall into26 exact(M_w,c_w) groups. The largest group's
noise union has only39 points, and no exactsame(M,c) group covers81. Full
route matrices, constants, noise columns, allgroup spans and coefficient
witnesses are inNEW_ROUTE4_SELECTED_PAIR.json. The largest group contains
words[1,3],[1,0,0,3],[1,1,3,3],[1,2,4,3],[1,3,0,0],[1,3,1,3],
[1,3,2,4],[1,3,3,1], with commonM rows
(0,0,0,0),(2,1,0,0),(2,0,1,0),(2,0,0,1), c=0.

The observed fullcoverage therefore combines differentM groups; individual
lowrank routes complement each other's targets. Atzero, only the noise
images matter because the constants arezero. Atbasis e0, the images receive
their actualword-dependentM_w*e0 shifts; those shifted images also cover81.
These two observed starts do not prove the claim for allx. In particular,
span(the union of noise images)=F3^4 would be a weaker and insufficient test;
we used the actual union of image sets and stored every element witness.

## Initial-stage sourceproof gap (before the authorized follow-up below)

For the33216 fullrank pairs, one fixed word plus its inverse-noise matrix
is a compact sufficient certificate for every fiberstartx and targety:
noise=N_w^{-1}(y−M_w*x−c_w). Generic affine route algebra then constructs
the four completed steps. A futurekernel proof would check the literal
controller endpoint and inverse identity; no graph-distance BFS is needed.

For3648 missingpairs, that interface is insufficient. A valid stronger
certificate must prove, for an actualfinite wordfamily ending at thatpair,

    for everyx,y inF3^4, somewordw satisfies
    y−M_w*x−c_w in image(N_w).

A same(M,c) family whose actual noise-image union isall81 is a simple
translation-invariant sufficient case, valid even for singularM. The
selectedpair explicitly lacks that easy certificate (best39). It instead
needs a genuine input-dependent affine-coset cover/pencil identity across
differentM groups, with symbolic conditions or a finite complete cover
certificate. The current zero/e0 samples do not fill that gap. No all81
start sweep,192^2*81 pointpair sweep, secondpair, longerwords, newfield or
formalqueue was run or is authorized by this experiment.

To turn completedrelations into genuine simple-source Walks, form each
actual state sequence then delete only consecutive equal GLOBAL labels.
Those are precisely the virtualself stays; every otherstep is a bound
originalsimple edge. Removing stays yields a genuine Walk oflength<=4.
Selfcontroller/localdifferent and differentcontroller/localequal steps
must remain. The complementary agent independently supported this bridge
and the exactsame(M,c) union criterion, with zero numerical reruns.

The separately authorized fresh all16389-root acceptance has its own
receipts and budget. Its mathematicalD4 success is fully compatible with
this refuted stronger route hypothesis and is not counted as this small
route experiment's result. This batch adds0graph/parameter/Lean and stops.


## Same original10CPU batch: the weaker onepair coset criterion succeeds

Root authorized only the samepair(0,0), not a newsource/pair or timer. The
newprediction was recorded inNEW_ROUTE4_PRED before examining the saved61
route matrices. For eachword putH_w=imageN_w. Test each of the fourcolumns
of(M_w−I) andc_w for membership in its ownH_w. These are newcomposed-route
column tests, not a repeat of the fiveatomicB ranks.

Actualresult:53 of61 closedwords qualify. TheirH image sizes are1 for1word,
3 for10words,9 for42words. The actual union ofthose53 H isALL81, not merely
a spanning set. NEW_ROUTE4_TRANSLATION_COSETS.json gives every qualifying
word, M,c, noise columns, everyindividualH vector, fourcolumn coefficient
witnesses andconstant coefficient witness, plus an explicit81-vector map
to a qualifyingword andnoise coefficients. No starting fiberpoints were
enumerated in this follow-up and no secondcontrollerpair was examined.

Here is the complete allx proof supplied by those finite coefficients.
Letd_i be a noise coefficient vector withN_w*d_i=(M_w−I)e_i andletd_c have
N_w*d_c=c_w. For anyx, linearity gives

    M_w*x+c_w+H_w = x+H_w.

For arbitraryx,y put h=y−x. The storedunion certificate chooseswordw and
alpha withN_w*alpha=h. Take actualnoise

    alpha − sum_i x_i*d_i − d_c.

ThenM_w*x+c_w+N_w*noise=y. Everychosenword ends atcontroller0 from0 and
haslength<=4, hence after deleting only global-label stays it yields a
trueoriginalsource Walk oflength<=4 from(0,x) to(0,y). This conclusion is
for allx,y, deduced from the fourcolumn identities and actualset union;
it is not an extrapolation from the earlierzero/e0 observations. No M
invertibility or exactsame(M,c) assumption is needed.

This resolves the selected(0,0) pair's initial-stage gap by a genuinely
weaker and successful certificate interface. It preserves alloriginal
negative conclusions: no singlefullrank4word for3648 pairs, no exactsame
(M,c) noiseunion81 for the selectedpair (best39), and the originaltwo-start
checks alone are insufficient. The supplied53word cover hasnot been
kernel-formalized. The other3647 missingpairs still require actualroute
cover certificates. A useful eventual generic lemma is the displayed
common-reference affine-coset identity with column membership; further
controllerpair/profile tests or a fullsource Lean batch need root's separate
authorization. We stop here with0 graph/parameter/Lean increments.
