# Source gauge and cross-characteristic control rule

The actual primary source `AUTHOR_construction.json` uses the LEFT semidirect law

`(v,j)(w,k)=(v+a^j*w,j+k)`, with `p=6073`, `a=2685`, `j mod23`.

Its positive generators are `(5228,2),(5308,16),(987,14),(5277,17)`. This is the actual recovered recipe; it is not inferred from the source order. The earlier 7D7 example used a different RIGHT-law convention, so its endpoint recurrence must not be reused unchanged.

## Exact source gauge, checked by small arithmetic

Conjugation by `h=(c,0)` sends `(v,j)` to `(v+(1-a^j)c,j)`. Choose `c=2468`, which kills the first generator translation. The four translated values are `[0,5474,1208,3116]`. Multiplication by the field scalar `d=5474^-1=1683` gives `[0,1,4682,3229]`, or the centered representatives `[0,1,-1391,-2844]`.

Renumber phases by `j'=12j mod23`, using `2^-1=12 mod23`. The new action is `beta=a^2=574`, of exact order 23, and the four positive phases become `[1,8,7,20]`.

Explicitly the source group isomorphism is

`F(v,j)=(d*(v+(1-a^j)c),12j)`.

The identity `beta^(12j)=a^j` and the cocycle equality

`(1-a^j)+a^j*(1-a^k)=1-a^(j+k)`

prove that F respects the LEFT law. Thus this gauge removes translation/scaling freedom before selecting a transfer. It does not change the old graph. The exact values are stored in `ANALYSIS_GAUGE.json`; no old-source BFS was run.

## What genuinely transfers

For the preceding fixed q137 control, phase quotient, inverse pairing, and formal cyclotomic endpoint identities survived, yet the actual graph had diameter 8. There is no field embedding from F113 to F137. In particular source equalities that vanish only in the source characteristic, and source endpoint images covering an entire finite field, do not follow from retaining action order or small centered translations.

Here freeze the normalized integer generator translations `[0,1,-1391,-2844]` and phases `[1,8,7,20]` only if the parent elects that literal family. For a prefix ending in phase j, the actual LEFT-law word recurrence is

`P_new(t)=P_old(t)+t^j*c_s(t)`.

For a generator with phase k and polynomial translation c, its inverse dart has phase -k and translation polynomial `-t^(-k)*c`. All reduced words of length at most seven are sufficient for the Cayley distance question because immediate inverse cancellations preserve the endpoint. Reducing endpoint polynomials modulo `Phi23(t)=1+t+...+t^22` preserves formal identities for every target prime other than 23 and every action of exact order 23.

The new control-selection gate is specific: for an actual thin phase slot j, form the complete set

`S_j(q,beta)={P_w(beta) mod q : |w|<=7, phase(w)=j}`.

Require `|S_j(q,beta)|=q` before constructing that target graph. A raw count or formal polynomial count at least q is only a necessary prefilter. A failure of this exact image gate excludes that proposed embedding; success in the first thin slot does not establish the other slots. If all 23 slots pass, the complete Cayley identity-root route certificate has diameter at most seven. A subsequent actual adjacency check can bind the recipe implementation without recomputing the old graph.

The source action has 22 primitive order-23 embeddings in any compatible prime field. Integer size of a primitive root does not express compatibility of endpoint images. Consequently a finite, explicitly authorized all-22-embedding question is more principled than choosing the smallest primitive root and then repairing its missing vertices. A low-degree source relation used to choose a literal lift must first be distinguished from a source-only congruence. Centered representatives are a frozen transfer convention, not a universal invariant: adding 6073 to an old coefficient gives the same source graph but generally a different target recipe.

## Current execution boundary

Only the displayed gauge and action arithmetic were computed here. No thin-slot word enumeration, target-prime test, embedding scan, graph construction, or BFS was performed. The parent mentioned q6211 as a possible target; no claim about its graph or any of its embeddings is made. The producer remains the sole owner of route enumeration and any authorized target generation. The next numerical prediction must name that actual thin slot and frozen family before testing it. This is a control-selection note within the current 8D7 source mechanism, not a separate experiment or a reopening of the failed q137 control.
