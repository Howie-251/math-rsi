# Blind proof audit: three twelve-vertex partner exclusions

Date: 2026-10-11. Reviewer: `/root/proof_review_n62_two_partners_blind`.

**Verdict: PASS for the three local exclusion arguments, relative to their stated actual-graph dependencies.** No fatal, critical, major, or minor mathematical issue was found. Review independence is **same-family**, and semantic acceptance is **provisional**. This is a fresh review of the complete current text of both target papers, without reading prior audits of either paper. It is not a Lean verification or an exclusion of all order-62 graphs.

The two target files were not edited. Only this Markdown audit and its JSON companion are emitted. The user's output restrictions override the skill's default hashes, TeX/PDF, HTML, state, skeleton, and wiki artifacts.

## Scope and quantified claims

Let G be any finite simple undirected graph on 62 vertices, of maximum degree at most eight and diameter at most two. Let A be its adjacency matrix and B=A²+A−7I−J. For any two distinct components H,K of the positive support of B, write h=|H|, k=|K|, a=r_HK, b=r_KH, s=r_HH, t=r_KK, where r_CD counts neighbors **in D of a vertex in C**.

The claims checked are the nonexistence of each pair of components with parameters:

1. (h,k,a,b,s,t)=(12,20,5,3,1,2).
2. (h,k,a,b,s,t)=(12,24,6,3,0,2).
3. (h,k,a,b,s,t)=(12,20,5,3,0,2).

The first paper additionally imports the established triple-repeat exclusion B≤2. This is needed in its presented proof for the minimum nonempty type size. The third exclusion uses only regularity, nonnegative B, and the actual component quotient; it does not need B≤2, the D1 local structure, or any component-size classification. The three local claims apply to arbitrary components with the specified parameters.

## Assumptions, notation, and dependency ledger

| Object or premise | Type / discharge |
|---|---|
| A | Symmetric 62×62 zero-diagonal 0–1 adjacency matrix of the original graph. |
| Regularity | If deg(v)≤7, its distance-two ball has at most 1+7+7·7=57 vertices. Thus A1=8·1. |
| B | Symmetric integral matrix with zero diagonal, nonnegative by diameter two, and B1=3·1. |
| AB=BA | A commutes with its polynomial and with J because G is regular. |
| B≤2 | Named established triple-repeat exclusion imported through `RECOVERED_REDUCTION.md`; its statement and displayed proof were read, but its finite enumeration was not rerun in this bounded audit. No independent closure of that import is claimed. |
| Equitability | Re-derived below from the actual B eigenspace; no claim that A preserves each component separately. |
| R | Integer quotient with r_CD directed from C to D; size balance |C|r_CD=|D|r_DC follows by edge counting. |
| d_C | The 62-vector A1_C, whose value at v is the number of neighbors of v in C. |
| Exterior type | Pair (x,y)=(d_H(v),d_K(v)); counts are integers and the type is a union of entire B components. |
| Type-size rule | Each B component has even size since 3|C| is twice an integer edge weight. A size-two component would have its unique entry equal to 3, excluded by B≤2. Thus each nonempty type has even size ≥4, including (0,0). |
| Combined remaining list | Conditional on the cited finite-inequality and twelve-by-twelve reductions. Their stated lists match the claimed subtraction; this audit does not independently rerun the separator checker or re-certify those source theorems. |

Dependency graph: legal graph → regularity and actual B identities → component equitability and quotient → exact moments / pointwise bounds / neighbor balance → the three contradictions. The first two branches also use the imported B≤2 → type-size rule. The residual-list conclusion separately imports the two other reduction papers. No circular dependency occurs. There are no limits, probability modes, asymptotic constants, or analytic interchanges in these arguments.

## Re-derived foundational obligations

For any real f,

    fᵀ(3I−B)f = ½ Σ_uv B_uv(f_u−f_v)².

Consequently the B-eigenspace of eigenvalue three is exactly the vectors constant on each support component. Since B1_C=3·1_C and AB=BA, A1_C belongs to that eigenspace. This proves component equitability.

Restricting A²+A=7I+J+B to component-constant vectors gives

    R1=8·1,     R²+R=10I+1nᵀ.

In particular the (H,K) entry has right-hand side **k**, not h. For every component C,

    (A²+A)1_C = 10·1_C + |C|·1,

so at v outside C,

    (A d_C)(v)+d_C(v)=|C|.

This identity does not require that original-graph edges remain inside B components.

For the exterior vertices, degree sums give Sx=h(8−s−a) and Sy=k(8−t−b). The total norm of d_H is 1_HᵀA²1_H=h(h+10−s); subtracting its H and K contributions gives

    Qx=h(h+10−s−s²)−kb²,
    Qy=k(k+10−t−t²)−ha².

Likewise 1_HᵀA²1_K=hk−ha. Subtracting hsa and kbt=hat gives

    Qxy=h[k−a(1+s+t)].

Thus the second factorial moments are Qx−Sx and Qy−Sy. At an exterior vertex, retaining the H and K neighbors in the nonnegative neighbor-balance sum yields

    (s+1)x+by≤h,     ax+(t+1)y≤k,     x+y≤8.

Every formula and direction agrees with the source Section 8 and the two audited papers.

## Local proof-obligation checks

### First paper, case (12,20,5,3,1,2), lines 28–63

The moment vector in order (N,Σx,Σx(x−1),Σy,Σy(y−1),Σxy) is exactly

    (30,24,36,60,120,0).

Nonnegative xy and zero sum make the positive-x and positive-y supports disjoint. On Y, Cauchy gives 60²≤|Y|·180, hence |Y|≥20 and |X|≤10. The domain gives x≤4. A nonempty x=4 type contributes at least 4·4·3=48 to a factorial moment of 36, so x≤3. Writing u,v,w for the counts with x=1,2,3 gives

    u+2v+3w=24,     v+3w=18,
    u=3w−12,       v=18−3w,       |X|=6+w.

Therefore 4≤w≤4. Thus X has six vertices of type (2,0) and four of type (3,0), and |Y|=20. Cauchy is an equality, so y is constant on Y and equals 3. There is no exterior (0,0) vertex.

For v∈X, d_K is 5 on H, 2 on K, 3 on Y, and 0 on X. Since v has no K-neighbor and d_K(v)=0, neighbor balance becomes

    20=5x_v+3|N(v)∩Y|.

For x_v=2 or 3, the residual is respectively 10 or 5, not divisible by 3. The value 5 on H is the correctly directed r_HK. All existence and equality conditions used here are discharged.

### First paper, case (12,24,6,3,0,2), lines 65–108

The exact moment vector is

    (26,24,24,72,168,72).

The domains are x+3y≤12, 2x+y≤8, and x+y≤8. A nonempty x=4 type would contribute at least 48 to a factorial moment of 24. If x=3 occurs, its total count must be four: any nonempty joint type already contains at least four vertices, and four exhaust the moment. Then x=2 never occurs and twelve vertices have x=1. The bounds y≤2 at x=3 and y≤3 at x=1 give Σxy≤60, contradicting 72. This includes the possibility of multiple x=3 joint types: their combined count four cannot support two nonempty types.

It follows that x≤2, and the x moments force twelve x=2 vertices, zero x=1 vertices, and fourteen x=0 vertices. On the x=2 set X, Σ_X y=36 and y≤3, forcing all twelve vertices to have type (2,3).

For the remaining fourteen vertices,

    Σ n_j=14,     Σ j n_j=36,     Σ j(j−1)n_j=96,

with 0≤j≤4. Subtracting twice the first moment from the factorial moment gives 2n_4−n_1−n_2=12. Hence 6≤n_4≤9; evenness leaves 6 or 8. For n_4=6, n_1=n_2=0, n_3=4, n_0=4. For n_4=8, the equations force n_1=4, n_2=n_3=0, n_0=2. The latter is forbidden specifically by the nonempty-type lower bound; evenness alone would not exclude it.

The forced types are therefore (2,3):12, (0,3):4, (0,4):6, (0,0):4. In particular a vertex v of type (0,3) exists. The function d_H is 0 on H, 3 on K, 2 on X, and 0 on all other exterior vertices. Therefore

    12=3·3+2|N(v)∩X|,

which is impossible. Both the coefficient 3=r_KH and the parity contradiction are correct.

### Second paper, case (12,20,5,3,0,2), lines 76–146

For any exterior component E of size e, put p=r_HE, q=r_KE, x=r_EH, y=r_EK. Edge balance is exactly

    12p=ex,     20q=ey.

The H row budget is Σ_E p=8−0−5=3. If x>0, then p∈{1,2,3}. Multiplying the balance equations by y and x gives 3py=5qx, so 5 divides py. Every possible positive p is coprime to 5, so 5 divides y.

Actual neighbor balance with C=H gives x+3y≤12. Hence if x,y>0, then 1≤y≤3, contradicting 5|y. Therefore xy=0 for every exterior component, and py=0 too, because balance makes x=0 imply p=0.

The correctly oriented (H,K) quotient equation is

    0·5+5·2+Σ_E p y+5=20,

so Σ_E py=5, contradicting that every summand is zero. No assumption concerning the parity or minimum size of E is used.

The optional exterior-moment interpretation, lines 148–178, also checks: its vector is (30,36,48,60,120,60), its three domain inequalities are correct, and Σ_E exy=12Σ_E py=60. For an entire joint type T, equitability and edge counting give 12 dividing |T|x and 20 dividing |T|y, with no assumption that T is a single component.

## Counterexample and boundary pass

The check targeted actual possible gaps rather than asking whether abstract moment data alone construct a graph.

- Checked the x=4 and x=3 boundary types and the possible splitting of x=3 across several joint types.
- Checked Cauchy equality and exhaustion of all exterior vertices in the first case; no missing zero type remains there.
- Checked the n_4=8 branch in the second case explicitly. It gives the even but illegal count vector (n_0,n_1,n_2,n_3,n_4)=(2,4,0,0,8), so removing the minimum-size rule would invalidate that presented type argument.
- Checked x=0, y=0, p=0, and empty exterior supports in the divisibility argument. Balance handles each zero case, and the off-diagonal identity itself forces a positive mixed contribution.
- Reversing a and b would break the first final equation; direct evaluation of d_K on H confirms that the paper uses the correct orientation.
- The displayed forced moment distributions satisfy their moment and domain equations exactly. They are only necessary data and are not claimed to realize a graph.

No counterexample under the stated hypotheses was found. These checks support the written derivations; failure to find a counterexample is not used in place of a proof.

## Reads, commands, and limits

Complete target reads:

- `proofs/dd82/n62/D1_TWELVE_TWO_LARGE_PARTNER_EXCLUSIONS.md`, lines 1–122.
- `proofs/dd82/n62/D1_TWELVE_TWENTY_ZERO_TWO_EXCLUSION.md`, lines 1–193.

Other actual reads:

- Project `AGENTS.md` and `.agents/skills/proof-checker/SKILL.md`, complete.
- `D1_COMPONENT_MINIMUM_SIZES.md`, lines 1–79 and 231–end, with a second numbered read of 243–285.
- `GLOBAL_DOUBLE_TRIANGLE_QUOTIENT.md`, lines 1–49 and 138–210, plus keyword matches elsewhere in that file.
- `RECOVERED_REDUCTION.md`, lines 1–240, to identify the original hypotheses and the imported B≤2 result. Its finite-check source was not opened or executed.
- `D1_TWELVE_EXTERIOR_MOMENT_REFINEMENT.md` and `D1_TWELVE_COMPONENT_EXTERIOR_EXCLUSION.md`, complete, to verify the conditional remaining-list dependency and its stated scope. No prior audit file was opened.

Executed command families were `pwd`, `rg --files`, `rg -n`, `cat`, `nl -ba`, `sed -n`, `ls -la`, `date -u`, and an inline standard-library `python3` arithmetic check. An initial overly broad filename-only `rg` scan was stopped with Ctrl-C after truncated output; it did not read prior audit content. The scoped `rg --files -g AGENTS.md proofs reviews .agents` reported no closer instructions. Attempts to read the two ancestor AGENTS paths found neither file.

The arithmetic check independently substituted all three parameter tuples into the general moment formulas; asserted the two proposed distributions' moments, type lower bounds, parity, and pointwise domains; and checked the final modular contradictions and the positive off-diagonal contribution. It exited 0 and printed:

    (12,20,5,3,1,2) -> (30,24,36,60,120,0)
    (12,24,6,3,0,2) -> (26,24,24,72,168,72)
    (12,20,5,3,0,2) -> (30,36,48,60,120,60)
    All exact moment substitutions, stated distributions, and final modular contradictions checked.

The inline check uses the formulas recorded above and deterministic integer arithmetic, with no solver, floating computation, or search for a 62-vertex graph. The mathematical forcing steps were checked by hand. No separator enumeration, triple-repeat enumeration, Lean compilation, or external cross-family review was performed in this task.

A fresh bounded arithmetic shard, `/root/proof_review_n62_two_partners_blind/arithmetic_obligations`, was requested as `gpt-6-astra` with `ultra` reasoning and a new context containing only the two finite systems. It independently confirmed the forced type implications and explicitly identified the rejected size-two zero type. The shard also gave a shorter independent proof of case 1: Cauchy forces positive-support sizes 10 and 20, and then Σ_X(x−2)(x−3)=60−5·24+6·10=0 forces x∈{2,3}. Thus B≤2 is required by the first paper’s presented method, but is unnecessary for that first exclusion if this alternative argument is used. Its result corroborates arithmetic obligations only and does not constitute an independent-family semantic acceptance.

### Arithmetic-shard execution provenance

The shard reported three actual `python - <<'PY'` executions, each exit 0, with no project-file reads or task-file writes:

1. A package-availability probe using `importlib.util.find_spec` for scipy, z3, and sympy returned True, False, True; none of these packages was imported or used in the proof check.
2. A standard-library enumeration generated the seventeen admissible case-2 (x,y) points and enumerated nonnegative half-counts a_0,…,a_4, disallowing a_j=1, with Σa_j=13, Σj a_j=12, and Σj(j−1)a_j=12. Its only profiles were (7,0,6,0,0) and (5,6,0,2,0).
3. An `itertools.product` enumeration checked case-2 residual half-counts with sum 7, first y moment 18, and factorial y moment 48. The even-only residuals were (1,2,0,0,4) and (2,0,0,2,3); only the second obeyed the minimum-four rule. It also enumerated case-1 positive x/y half-counts, obtaining the sole solution x counts (0,3,2,0), y counts (0,0,10,0,0,0), and zero zero-type count.

These are direct exact integer enumerations of the reduced arithmetic obligations. In case 2, the reduction to the residual y counts still uses the manual mixed-moment contradiction for the second x profile and the equality forcing y=3 on the x=2 set. The shard did not claim an unrestricted enumeration of all seventeen joint-type multiplicities.

## Conclusion and remaining scope

The current written arguments exclude all three specified parameter tuples. Under the separately cited reductions, removing these tuples and the twelve-by-twelve alternatives leaves precisely the seven listed size-sixteen tuples. The claim that those seven cases remain undecided is consistent with the targets' scope. Larger heavy components and the full order-62 problem remain open. No change to either author paper is required by this audit.
