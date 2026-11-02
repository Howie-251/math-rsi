# Fixed J5-plus-I1 auxiliary family: all3840 inputs fail

The complete prescribed3840-input gate finished without a K64 of diameter at most3. Both branches contributed1920 inputs. Every candidate failed exact radius3 coverage already at root0, so no later root was evaluated. There are no untested inputs, timeout, candidate selection by deficiency, or positive edge artifact. This closes only the fixed affine permutation and two-coset S family described below.

## Actual source opportunity

The local primary text read was `../d11_D6_mechanism_read/paper_extracted.txt`, Definition1, Theorem1 and its proof, and the q8 discussion on PDF pages3–4. It requires an auxiliary graph K on eight pencils of eight vertices that contains all pencil differences X'={1,x,x²}; its diameter at most3 is sufficient for the fiber extension. With X={3,5,6,7} and q8, the extension order is8³+8²(8+1)=1088. Points have degree9+4=13, and lines have degree8+deg(K), so a degree5 auxiliary graph would give maximum degree13.

The author explicitly supplies a degree3 extra gadget, producing auxiliary degree6 and main degree14, and identifies the degree13 opportunity as one for which the needed gadget was not found. The present experiment therefore targets that stated missing degree2 gadget. It does not claim that the author never tried the opportunity. The project ledger search did not identify a previous complete execution of this exact affine class; prior binary72 and F5 flat-lift records have different structures and acceptance conditions.

## Exhausted scope

Vertices are F2^6 encoded0..63. The external permutation is fixed:

    sigma(v)=v XOR((v AND30)>>1) XOR16.

Its actual inverse was obtained from its full64-entry permutation table. The code checked eight cycles of length8. Thus sigma and its inverse give two distinct neighbors at every vertex.

The linear part is A=J5 plus I1, with N=A-I of rank4. Its cokernel has dimension2 and coordinates bits4 and5. The induced three nonzero generator directions give a four-vertex K4 coarse quotient with a repeated generator. The earlier K4-square-K2 wording was corrected before the prediction and computation; it belongs to a different, untested linear part.

Let U={32,...,47} and V={48,...,63}. Enumerated S consists of either an unordered pair from U and one element of V, or one from U and an unordered pair from V. Each branch has C(16,2)*16=1920 inputs, with no overlap, totaling3840. No coordinate/projective quotient or additional symmetry reduction was imposed.

All three S elements have bit5=1 and are distinct. Any sum of three therefore still has bit5=1; a pair sums to zero only if equal. Hence S is independent. The internal edges v--(v XOR s) form eight designated Q3 subgraphs, one in each coset of span(S). External edges preserve bit5 while internal edges change it, so the two types cannot coincide. Together with the cycle check this gives a simple5-regular64-vertex graph for every input; actual adjacency and reverse-edge checks were also performed. Theorem1 requires the cube edges to be present, not that those cubes be induced, so no extra induced-pencil restriction was used.

The graph was represented explicitly by64 adjacency rows and64 neighbor masks. For a root, three exact frontier/visited-mask updates compute its complete radius3 ball. If the result was not all64 bits, the candidate was rejected immediately. A first candidate passing all64 roots would have stopped the enumeration and saved its160 edges, sigma, S, and the literal (a,l) cube-coset relabeling. That branch was never reached.

## Terminal evidence

`INPUT.json` contains sigma, its inverse, its eight cycles, the correct rank/cokernel, and the input ranges. `CASES.jsonl` has one record for each cursor0..3839, including S, branch, first failed root, reached count, and first missing vertex. `TERMINAL.json` records:

- status `COMPLETE_3840_NO_K64_D3`;
-3840 candidates constructed and evaluated, branch counts1920/1920;
-3840 exact root-radius checks, all failed at root0;
-0 successful all64-root checks, positive K64 files, or1088-point graphs;
- one worker, PID32679, actual CPU0.421581270 seconds;
- no remaining cursor, restart, or pending action.

The fixed affine class is exhausted, not all auxiliary K64 graphs, all affine permutations, or the q8 fiber-extension method. No J4/J6 alternative, field, controller, random start, local repair, or bad-pair optimization was run. The main(13,3) novelty comparison remains the parent's responsibility only after an actual successful construction.
