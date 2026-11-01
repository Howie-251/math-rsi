# A short structural proof of the four-by-four matching-repair lemma

Let A be a nonnegative integer 4 by 4 matrix whose row and column sums are four. Put

    P=per(A),  M=max a_ij,
    T=max_{i<k,j<l}(a_ij a_kl+a_il a_kj).

Then

    P-T>=22,       P-2M>=22,

and equality in either inequality occurs only for the all-one matrix J.

The proof below is self-contained. It replaces the 10,147-input verification by a structural split according to M. Its only small constant computations are three displayed binary-type matrices and eight explicit one-variable quadratic formulas. No external permanent theorem, floating-point estimate or assertion of computational exhaustiveness is used.

## 1. A centered expansion used only when M=2

Suppose B has zero row and column sums. For k=0,...,4 let r_k(B) be the sum of the permanents of all k by k submatrices, with r_0=1. Expanding by which entries come from B gives

    per(J+B)=sum_{k=0}^4 (4-k)! r_k(B).

Here r_1=0 and r_2=(1/2)sum b_ij^2. For the latter identity, sum over two distinct rows: their sum over distinct columns is minus their inner product, and then use zero column sums.

For three fixed rows, inclusion-exclusion on coincident columns, using the three zero row sums, gives twice the sum of the products of their entries in a common column. Thus

    r_3(B)=2 sum_j sum_{i<k<l} b_ij b_kj b_lj
          =(2/3)sum_ij b_ij^3.

The last equality is the elementary identity e_3(x1,x2,x3,x4)=(x1^3+...+x4^3)/3 when x1+...+x4=0. Consequently the general centered identity is

    per(J+B)=24+sum b_ij^2+(2/3)sum b_ij^3+per(B).

In the M=2 application, B=A-J has entries in {-1,0,1}; hence sum b_ij^3=sum b_ij=0. Only in this application do we use

    per(A)=24+S+per(B),       S=sum b_ij^2.                 (1)

The cubic term has not been discarded for arbitrary real centered matrices.

## 2. All matrices with M=2

A column has one of the three unordered types

    F=(1,1,1,1),   U=(2,1,1,0),   V=(2,2,0,0).

The same is true of rows. In B their respective support sizes are zero, two and four. In each row or column of B the positive and negative entries balance.

### A flat row or column

If A has an all-one row or column then per(B)=0. Thus P=24+S. For a nonzero integer matrix with zero row and column sums, its nonzero support has at least four positions: every nonzero row and column has support at least two, giving a bipartite cycle of length at least four. Here S is the support size, so P>=28.

By transposition assume there is an all-one column. Every row then has at most one entry equal to two. In a two-by-two permanent, if one product is four, the other product is at most one; otherwise each product is at most two. Hence T<=5. Therefore

    P-T>=23,       P-2M>=24.                              (2)

These are already strictly greater than 22. The all-one matrix itself belongs to M=1 and will be handled separately.

### No flat row or column

Let v be the number of V-columns; the other 4-v columns are U-columns. A U-column contributes two nonzero entries to B, a V-column four. A zero row sum forces each row support size to be even and, since rows are not flat, at least two.

If v=3, the unique U-column would have to be nonzero in all four rows to correct the odd contribution from the three V-columns; it has only two nonzeros. This is impossible. Thus v is 0,1,2 or4.

**v=0.** All column supports have size two, giving eight nonzeros. Every row support must therefore also have size two. The support is a simple two-regular bipartite graph, hence either one eight-cycle or two four-cycles. The signs alternate along every cycle. Each cycle has two perfect matchings; for the possible four- or eight-cycles both matching products are positive. Thus per(B)=2 or4, S=8 and P=34 or36. Since T<=8, both target inequalities are strict.

**v=1.** Each row meets the V-column. Its number of U-column nonzeros is odd. The three U-columns give six incidences, so exactly one row meets all three and the other rows meet one each. These three latter incidences belong to distinct U-columns. Thus the support is forced: one central row and three leaves. After row and column permutations there are only the following matrix C or its entrywise complement 2J-C, according to the sign at the intersection of the central row and V-column:

    C = [ 2 2 0 0
          2 0 1 1
          0 1 2 1
          0 1 1 2 ].

Indeed, each U-column has its two signs opposite, and the V-column has two plus and two minus signs; once the central sign is fixed, its three leaf signs are fixed up to leaf permutation. Expanding the first row of C gives per(C)=2*6+2*10=32. Formula (1) is unchanged by B -> -B, so per(2J-C)=32 as well. Again T<=8, so P-T>=24 and P-2M=28.

**v=2.** Row parity forces the two U-columns to have the same two-row support. On those two rows their signs are either aligned or opposed. In the aligned case the V-columns are forced up to permutations. In the opposed case each row has one two and one zero in the V-columns. Up to interchanging the V-columns, interchanging the two ordinary rows, and interchanging the two supported rows together with the U-columns, the two twos of one V-column lie either both on supported rows or on one supported and one ordinary row. These give exactly three forms:

    C1 = [ 0 0 2 2       C2 = [ 2 0 2 0       C3 = [ 2 0 2 0
           2 2 0 0              2 0 0 2              0 2 0 2
           2 0 1 1              0 2 1 1              2 0 1 1
           0 2 1 1 ],           0 2 1 1 ],           0 2 1 1 ].

Their permanents, by expansion in the first row, are respectively 32,32,40. Since T<=8, P-T>=24 and P-2M>=28.

**v=4.** Write A=2D. The zero-one matrix D has every row and column sum two. Its support is again one eight-cycle or two four-cycles. Accordingly per(D)=2 or4, so P=32 or64. In the eight-cycle case no two-by-two submatrix of D is all one, so T<=4; hence P-T>=28. In the other case T<=8 and P-T>=56. Also P-2M>=28 in both cases.

This exhausts M=2, and every bound is strictly greater than 22.

## 3. All matrices with M=3: eight one-variable families

Choose an entry three and move it to position (1,1). Its row and column each have exactly one further entry one; move them to (1,2) and (2,1). Writing b=a22, c=a23, e=a32 and t=a33, all row and column constraints now force

    A(b,c,e,t) =
      [ 3  1       0          0
        1  b       c          3-b-c
        0  e       t          4-e-t
        0  3-b-e   4-c-t      b+c+e+t-3 ].                (3)

All entries lie between zero and three. Independently swapping columns3,4 and rows3,4 lets us require

    c>=3-b-c,   e>=3-b-e.

Transposition of (3) interchanges c and e, so also require c>=e. Since b is one of 0,1,2,3, these conditions leave exactly the eight rows of the table below. The indicated ranges of t follow directly by requiring the four entries of the lower-right block to lie in {0,1,2,3}. This is the complete structural coverage, not an inference from a program.

| (b,c,e) | allowed integer t | per A(b,c,e,t) | lower bound |
| --- | --- | --- | --- |
| (3,0,0) | 1,2,3 | 20(t-2)^2+80 | 80 |
| (2,1,1) | 0,1,2 | 14t^2-32t+66 | 48 |
| (1,1,1) | 0,1,2,3 | 8(t-1)(t-2)+38 | 38 |
| (1,2,1) | 0,1,2 | 8(t-1)^2+40 | 40 |
| (1,2,2) | 0,1 | 8t^2+4t+40 | 40 |
| (0,2,2) | 0,1,2 | 2t^2+40 | 40 |
| (0,3,2) | 0,1 | 2t^2+8t+56 | 56 |
| (0,3,3) | 0 | 2t^2+28t+82 | 82 |

The formulas follow by expanding the first row: if K is the lower-right two-by-two block, d=3-b-c and h=3-b-e, then

    per(A)=(3b+1)per(K)
           +3[c(e K22+h K12)+d(e K21+h K11)].

For the second table row, put u=t-1 in {-1,0,1}: the polynomial is 48+14u^2-4u>=48. In the third row, (t-1)(t-2)>=0 for every integer t. All other lower bounds are immediate from the displayed squares or nonnegative terms. Hence P>=38 for every M=3 matrix.

For completeness, T<=10. In any selected two-by-two block let m be its largest entry. Move it to the upper-left position. The opposite entry is at most m; both remaining entries are at most min(m,4-m), using the row and column sums through the largest entry. Therefore its permanent is at most

    m^2+min(m,4-m)^2.

For integer m=0,1,2,3 these bounds are 0,2,8,10. Thus

    P-T>=38-10=28,       P-2M>=38-6=32.

## 4. All matrices with M=4

An entry four exhausts its row and column, so A is permutation-equivalent to the direct sum of [4] and a nonnegative integer three-by-three matrix D with row and column sums four. We first show per(D)>=16 by its possible row types.

If D contains an entry four, it splits into [4] and a two-by-two matrix with row and column sums four. The latter has form [[z,4-z],[4-z,z]], whose permanent is 2(z-2)^2+8>=8; hence per(D)>=32.

If D has maximum entry three, normalize that entry and the residual ones in its row and column. Then

    D = [ 3 1 0
          1 z 3-z
          0 3-z 1+z ],       z=0,1,2.

Its permanent is 6z^2-14z+28, whose three values are 28,20,24, all at least16.

It remains that D has entries at most two. If it has a row (2,2,0), place it first. The third column then has two entries two in the other rows, forcing

    D = [ 2 2 0
          z 2-z 2
          2-z z 2 ],        z=0,1,2.

Its permanent is identically16. If there is no such row, every row has type (2,1,1); column sums force the twos to form a permutation matrix. Thus D=J3+Q for a permutation matrix Q, and per(D)=per(J3+I3)=16.

The three-by-three bound is proved in all cases. Consequently P=4per(D)>=64. Every two-by-two permanent of A is at most16, since it is at most the product of its two row sums, each at most four. Hence

    P-T>=48,       P-2M>=56.

## 5. Equality and the repair conclusion

If M=1, every row has four entries at most one and sum four, so A=J. Then P=24, T=2 and 2M=2, giving both equalities22. The preceding sections prove strict inequalities for every M>=2, completing the lemma and its equality statement.

In the matching-repair application, deleting at most T completions or twice the largest cell therefore leaves at least22 perfect matchings. This formulation applies to any two partitions of a sixteen-element set into four four-element blocks; its proof is a fixed structural integer-matrix lemma, with no hypergraph classification or outside-incidence assumptions.
