# Complete quotient-filtered check of the 7203-vertex head-triangle family

The complete normalized HH scope of **28,894,320** inputs is finished. The necessary quotient BB condition rejects 28,663,824 inputs; all remaining **230,496** received the exact original BB test, and **none passes**. Thus this fixed group action and head-triangle tower give no diameter-5 graph. This is a finite construction-family result, not a new lower bound or an arbitrary-graph exclusion.

With no original BB survivors, exactly one minimum-BB diagnostic graph was expanded and scored afterward. Its 2,508,408 bad-pair score is not a minimum over the family; its selection criterion is the BB deficit.

## Construction and candidate preservation

The actual implementation, labels, initial 1200-input profile, and independently checked first graph remain in `PROFILE_REPORT.md` and `structure.json`. In brief, A=F7²×C3, encoded by x=u+7v+49w, and K has coordinates (b,j)∈F7×Z6, encoded by b+7j. Its multiplication and action are

    (b,j)(d,l)=(b+4^j*d mod7,j+l mod6),
    (b,j)(u,v,w)=(3^(5j)*u+b*3^j*v mod7,3^j*v mod7,w).

The semidirect product uses componentwise modular addition and inverse (-k^-1(x),k^-1); F7 addition is not XOR. H consists of (b,0). Leaf, block, and head labels are x+147k, 6174+x+147j, and 7056+x. Leaf edges are g—gs; tree edges connect each leaf to its block and each block to its head. For each fixed (u,v), the three heads with w=0,1,2 form K3. The graph has 7203 vertices, 28812 edges, and degree 8.

`STRUCTURE_SCOPE.md` proves complete HH preservation: exactly two cross inverse pairs are necessary, one of each nonzero field colour, with unique w=1 representatives. A simultaneous upper-triangular field transformation, also conjugating K, normalizes their vectors to (1,0) and (0,1). Their two K coordinates remain arbitrary. The other three generators have w=0 and form one inverse pair plus one involution, or three distinct involutions, covering both colours. There are 16380 actual internal triples and 42² cross choices, giving 28,894,320 normalized inputs. This covers every HH-compatible seven-element inverse-closed S for the fixed tower.

## Exact quotient filter and original input counts

The epimorphism (u,v,w;b,j)→(v,w,j) has quotient order 126, operation

    (v,w,j)(z,t,l)=(v+3^j*z,w+t,j+l),

and seven original block targets above each quotient target. A missing quotient target implies at least seven missing original targets; quotient coverage alone does not imply original coverage.

The independent complete quotient check has 3780 pattern records, representing 1944 distinct projected S sets. Its 24 passing records reduce to **16 unique allowed sets**, stored in `QUOTIENT_BB_ALLOWED.json` with code v+7w+21j. Candidate preservation is proved in `QUOTIENT_BB_CHECK.md`; this and `STRUCTURE_SCOPE.md` were read in full for the batch.

Production preparation iterated the actual 16380 internal triples with all 36 pairs of cross exponents: **589,680 blocks**. Each projected S was sorted and deduplicated as a set, permitting identity images and repeated projected generators. Exactly **4704** blocks matched the 16 allowed sets. Every selected block matched the independent `quotient_lift_allowed_keys.jsonl` exactly. Each was expanded by all 49 choices of the two cross b parameters, giving 230,496 original inputs. Candidates were not regenerated from the 24 overlapping pattern records.

The complete order and original cursor mapping are in `production.metadata.json` and `production.selected_keys.jsonl`. Production started at a new filtered cursor 0; the 1200 random profile inputs were not an enumeration prefix and were not used to skip production inputs.

## Original BB evaluation

For target exponent j, the exact 147-bit mask is

    M_j = R_j ∪ P ∪ Q_j ∪ {(0,0,1),(0,0,2)},
    R_j = H·{x_w : w∈W3, exponent(w)=j},
    P   = H·{x_s : s∈W1},
    Q_j = H·{D_(j-j_s)x_s : s∈W1}.

W1 and W3 include identity. The last term is the new head-triangle route, included in every exponent layer. The six masks cover the 882 actual block targets. Original BB deficit is the sum of 147−popcount(M_j).

The implementation removes only immediate inverse cancellations from length-at-most-three words; those reduce to included shorter words. The new masks matched all 1200 saved actual BFS BB counts and all 882 target memberships of the independently checked first sample. This calibration used no new graph or BFS (`production.BB_calibration.json`). Every quotient survivor then received the original six-mask test.

| Branch | Internal composition | Full normalized inputs | Original BB evaluations | BB passes | Minimum BB deficit among quotient survivors |
|---|---|---:|---:|---:|---:|
| 0 | Axis pair + off-axis involution | 9,112,824 | 28,812 | 0 | 31 |
| 1 | Off-axis pair + axis involution | 9,112,824 | 86,436 | 0 | 40 |
| 2 | Two axis involutions + one off-axis | 1,111,320 | 0 | 0 | — |
| 3 | One axis involution + two off-axis | 9,112,824 | 115,248 | 0 | 41 |
| 4 | Axis + off-axis + zero involutions | 444,528 | 0 | 0 | — |
| Total | | **28,894,320** | **230,496** | **0** | **31** |

Branches 2 and 4 were rejected by the quotient condition, without original BB or BFS. The complete original-BB histogram is in `production.terminal.json`; deficits on quotient survivors range from 31 to 73, with 168 inputs attaining 31.

**31 is not claimed as the minimum over all 28,894,320 inputs.** Quotient-rejected inputs were not scored by the original masks. There is also no population of fully scored BB survivors: it is empty, with corresponding root minima recorded as null. Root-zero count fields do not mean every input received BFS.

The remaining obstruction after quotient coverage is confined to v=0: when v≠0, H acts transitively on the seven u preimages, so quotient coverage fills them all. The exact original test still finds missing targets among the 126 fixed-axis block targets. It never equates quotient coverage with original coverage.

## One diagnostic graph

The authorized minimum-BB fallback is:

    filtered cursor 1422; original-scope cursor 4,830,372;
    branch 0; internal index 2738; cross K codes [7,36];
    S=[1079,5247,5348,1601,2061,4117,3102].

Actual three-root BFS gives

    root missing=[744,434,276],
    missing by root/target layer=[[689,53,2],[371,31,32],[84,192,0]],
    bad unordered pairs=2508408.

Left G action preserves all edges, including triangles, and is transitive on the three layers. Thus the exact bad-pair weight is (6174*m_leaf+882*m_block+147*m_head)/2. The full graph is `production.best.edges`; its JSON explicitly labels it as a minimum-BB fallback, not a minimum bad-pair graph. The smaller bad-pair score from the random profile remains preserved and is not contradicted by this different criterion.

The final independent implementation reconstructed every edge exactly. One generic all-source check verified all 7203 roots: simple, connected, 8-regular, **diameter 7**, with exactly **2,508,408** bad unordered pairs. Independent representative-root distances also match the saved three-root scores and BB deficit 31. The pair-type counts are LL 2,126,943; LB 327,222; LH 12,348; BB 13,671; BH 28,224; HH 0. See `production.best.independent_check.json` and `best.independent_verify.json`. This is acceptance of the diagnostic graph, not a new lower bound or a best-bad-pair claim. No preflight or other graph was rerun.

## Cost and terminal scope

All 230,496 original BB inputs completed with `COMPLETE_NO_SOLUTION`, filtered cursor 230496. No BB-survivor graph was generated; exactly one final diagnostic graph was expanded. No process remains running.

The first 10000 inputs took 0.022285 CPU seconds: original BB 0.011999, graph/BFS 0, other 0.010286. This was an observation inside production, not an extra profile. New preparation/compilation/calibration cost 1.932476 seconds; production plus driver cost 0.546666. Including the earlier profile and its independent check, the cumulative recorded charge is **6.128809515 CPU seconds**, below the 180-second single-worker limit. Independent mathematical scope calculations are recorded separately. There were no restarts or range extensions.

This is complete finite computational evidence for the specified family, combined with mathematical candidate preservation and necessary-route conditions; it is not a formal certificate. It does not reopen previous d7 zero/one-pair families or cover another group action. No subsequent search was started.

The final independent check used 0.09900906300000001 Python CPU seconds and 1.600223 checker seconds. Including it, the cumulative recorded charge is **7.8280415780000006 seconds**. All requested terminal validation is complete; no result remains pending.
