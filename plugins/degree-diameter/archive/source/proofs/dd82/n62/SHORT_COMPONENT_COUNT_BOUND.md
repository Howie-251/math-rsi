# A shorter bound of nine actual repeat components

## Claim and scope

For any actual legal order62 graph, let c be the number of positive-support
components of its actual repeat matrix. Then c is odd and c<=9.
This note replaces the use of the full H,K>=14 chain in the connectedness
integration by the earlier H,K>=12 theorem and a short component-budget
argument. Its local delta review and Gemini B24 accepted the proof, with
all imports retained explicitly below. It does not exclude c=3,5,7,9 or order62 itself.

## Imported original-graph facts

Use the actual B=A^2+A-7I-J, nonnegative symmetric with zero diagonal and
row sum3. The analytic general triple-repeat exclusion in
TRIPLE_REPEAT_ANALYTIC_COMPONENT_EXCLUSION.md gives B<=2, hence
each positive-support component has at least four vertices. Indeed a
component with one vertex cannot have row sum3, two vertices would require
weight3, and three vertices would contradict evenness below.

The global quotient paper supplies actual equitability, even component
sizes n_i, row sums8, balance n_i r_ij=n_j r_ji, and
c+2 tr(R)=17. Thus c is odd. The existence of an actual D1 double pair
comes from D0_DOUBLE_COMPONENTS_AND_D1_OUTLET.md, Section3, using recovered
double parity, triangle pairing, and the D0 component classification.
Let H contain its heavy endpoints and K its generated triangle.

The earlier D1_COMPONENT_MINIMUM_SIZES.md, Sections1–5, proves
h=|H|>=12 and k=|K|>=12. Those sections retain their actual D1 rows and
light-mate transport dependencies. No later exclusion of twelve-point
components, sixteen/twenty/twenty-four partners, or exterior finite
inequality check is used here.

For any actual component C_i of size n_i and original internal degree
r_ii, the exact nonnegative common-neighbor budget is

    sum_j r_ij(r_ji-1) = n_i+2-r_ii.                    (1)

This follows from row sums and the diagonal equation of R^2+R=10I+1 n^T,
or from the actual pair-count in the earlier minimum-size paper.
All summands are nonnegative: positive off-diagonal r_ij has positive
integer reverse entry by balance; diagonal r_ii(r_ii-1)>=0.

For H=K the actual internal original degree is at least4. For H!=K put
a=r_HK>=4 and b=r_KH>=3. These are actual D1 incidence facts.

## Proof

If H=K, then tr(R)>=4 and c+2tr(R)=17 immediately gives c<=9.

Suppose H!=K. Packing h,k>=12 and the other component sizes at least4 gives

    24+4(c-2)<=62,

so c<=11. Because c is odd, it remains only to rule out c=11.

Under c=11, the other nine components consume at least36 vertices, hence
h+k<=26. Both sizes are even and at least12. The ordered possibilities are

    (h,k)=(12,12), (12,14), (14,12).

For (12,14), balance 12a=14b and 0<a,b<=8 force (a,b)=(7,6).
The H term a(b-1)=35 exceeds h+2=14 in (1), a contradiction.
For (14,12), balance 14a=12b forces (a,b)=(6,7);
now a(b-1)=36 exceeds h+2=16. Neither unequal-size case is possible.

Thus h=k=12 and a=b. The D1 inequalities imply a>=4. Applying (1)
to H gives a(a-1)<=14, so a=b=4.

The nine remaining even component sizes are at least4 and sum38.
Consequently they are eight fours and one six; in particular each
remaining component L has size at most6.

Write alpha=r_HH and x_L=r_HL. Balance gives

    r_LH=(12/|L|) x_L>=2 x_L.

If x_L>0, integrality gives r_LH>=2, so
x_L(r_LH-1)>=x_L; the same inequality holds when x_L=0.
The H row sum is8, and its K entry is4. Therefore

    sum_L x_L = 4-alpha,
    sum_L x_L(r_LH-1) >= 4-alpha,                       (2)

where L runs over the nine remaining components. But (1), including
the diagonal contribution alpha(alpha-1), gives exactly

    sum_L x_L(r_LH-1)
      = 14-alpha - 4(4-1) - alpha(alpha-1)
      = 2-alpha^2.                                     (3)

Combining (2)–(3) forces alpha^2-alpha+2<=0, impossible because
alpha is a nonnegative integer and alpha(alpha-1)>=0.
Thus c!=11. Oddness now gives c<=9.

## Dependency improvement and remaining work

This proof uses only the earlier lower bounds H,K>=12. It avoids the
entire subsequent twelve-component exclusion chain used to reach14,
while retaining the global triple-repeat exclusion, D1 existence,
actual equitability, even component sizes, trace identity and the
minimum-size proof through Section5.

Once this note is independently checked, it can replace Section1 of
CONNECTED_REPEAT_REDUCTION.md. The existing exact quotient enumerations
and actual-graph exclusions for c=3,5,7,9 then give the same connectedness
conclusion with fewer imported proofs. Those exact computations remain
external rather than Lean certified. No new computation, graph search,
axiom, or known63–65 reproof is used here.
