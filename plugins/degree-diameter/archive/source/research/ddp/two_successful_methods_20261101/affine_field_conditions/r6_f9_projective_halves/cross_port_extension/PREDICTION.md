# PREDICTION — fixed-S cross-port local glue

Recorded before this new bounded check. Inherit the completed parent r6/F9 classification and all12 self-port charts without rerunning them: all720 normalized PGL2(F9) permutations and252 five-subsets were already completely classified, and all six fixed B_p belong to the180-element orbit invariant under complement.

Only fixed S=[inf,0,1,2,3,6] is used. Thus, for every pair p,q, B_p and PG1(F9)\B_q lie in the same orbit, so some pure PGL map takes one to the other. This does not assert a property of arbitrary six directions.

Prediction: for each15 unordered pair p<q, choose the lexicographically first suitable coefficient tuple from the already saved720-entry PGL table. Define T_(p,q)=H_q^-1 diag(1,Q_f)H_p, Q_f=[[d,c],[b,a]]. Its reverse is its literal3×3 inverse. The new30 actual oriented cross-port charts should all preserve source-to-target port vectors exactly, have25 full-rank central turns, and provide ten distinct plane rays covering729 vectors. There should be750 new turn checks; together with the inherited300 self-port turns,42 actual charts account for1050 turns.

For a controller dart u→v with local sourceport p and targetport q, use canonical T_(p,q) if p<q, its canonical inverse if p>q, and the inherited self-port T_p+ if p=q and u<v (T_p- if u>v). This should ensure that every reverse dart uses the true inverse even when each controller vertex assigns port labels from its own sorted neighbor list. No global6-edge-coloring is assumed or needed by this rule.

One new single-worker run, CPU hard limit5seconds. Reuse old group/field/self-chart artifacts; no re-enumeration of the group, no252-subset classification, no old12-chart recheck. No controller generation, fiber graph, BFS, solver, Lean, hash or installation. This prepares local glue only; it neither waits for nor claims a successful C78 controller or54-degree graph. On failure preserve its exact local counterexample and stop.
