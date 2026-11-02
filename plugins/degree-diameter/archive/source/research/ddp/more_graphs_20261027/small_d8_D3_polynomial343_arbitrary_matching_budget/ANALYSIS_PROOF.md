# Polynomial source plus one arbitrary matching: endpoint obstruction

Status: **VALID, complete for the stated augmentation family**. This is a paper derivation; no graph, matching, BFS or solver was run for this analysis. The existing `RESULT.json` and `FORMAL_ENDPOINT_IMAGE.json` give a separate finite check at q=7.

## Source and exact three-walk image

For an odd prime power q, let G_q be the simple graph on F_q^3 obtained from the formal neighbours

    (a,b,c) -> (s, a*s-b, a^2*s+a*s^2-c)

by omitting self-loops. Adjacency is symmetric: the two endpoint conditions are b+e=a*d and c+f=a*d*(a+d). Distinct s give distinct first coordinates. Thus the maximum degree is q. The vertices (a,a^2/2,a^3) have one formal self-loop and actual degree q-1. In particular p=(0,0,0) has degree q-1.

A formal three-walk from p, with successive first coordinates u,v,d, ends at

    (d,e,f),   e=v*(d-u),   f=e*(v+d+u).

This image is exactly the actual closed ball B3_G(p). An actual walk of length less than three can be prefixed with the formal loop at p; conversely any formal self-loop can be removed without changing the endpoint.

Fix d. When e=0, f=0, giving one endpoint. When e is nonzero, v is nonzero and u=d-e/v, so

    f/e-2*d = v-e/v.

Two nonzero values v and v' have the same image precisely when v'=v or v'=-e/v. The involution v -> -e/v has two fixed points when -e is a nonzero square, and none otherwise. Its image therefore has (q+1)/2 or (q-1)/2 elements, respectively. Exactly half the nonzero e have each type. Consequently

    |B3_G(p)| = q * [1 + q*(q-1)/2]
               = q*(q^2-q+2)/2.

For q=7 this is 7*22=154. This proves the image size without relying on enumeration. The saved finite result agrees: 22 endpoints for every first coordinate d, with endpoint multiplicities 1:42, 2:105, and 13:7.

## Complete classification after adding a matching

Let M be any simple matching in the complement of G_q; M need not be perfect or maximal. Write m for its partially defined mate map, D for its matched vertices, and H=G_q union M. All balls below are closed balls in the unchanged graph G_q.

For a shortest path of length at most three, two consecutive matching edges would immediately backtrack. Thus every endpoint is in one of the following sets:

* O=B3_G(p), from paths with no matching edge.
* F=B2_G(m(p)), if p is matched: the single matching edge is first.
* U=union over u in N_G(p) intersect D of B1_G(m(u)): the single matching edge is in the middle. This also includes a path ending immediately after that matching edge.
* L=m(B2_G(p) intersect D): the single matching edge is last.
* V=m(N_G(m(p)) intersect D), if p is matched: the only reduced two-matching pattern is M-G-M.

These include all paths of length zero, one and two as well. A three-matching walk reduces to a one-matching walk. The sets may overlap, which only makes a sum of their sizes a weaker upper bound.

Since Delta(G_q)<=q and d_G(p)=q-1,

    |F| <= q^2+1,
    |U| <= (q-1)*(q+1)=q^2-1,
    |L| <= |B2_G(p)| <= q^2-q+1,
    |V| <= q.

It follows uniformly for every partial matching M that

    |B3_H(p)| <= q*(q^2-q+2)/2 + 3*q^2+1.

For q=7 the right hand side is 154+50+48+43+7=302. Hence at least 41 of the 343 vertices are outside B3_H(p), for every matching M. This is a uniform lower bound on missing targets from the fixed root; it is not a measured ordinary unordered bad-pair count, and it does not give an exact global diameter.

The same inequality is strict below q^3 for every odd q>=7: the difference is (q^3-5*q^2-2*q-2)/2>0. This extends the stated single-matching obstruction to that polynomial-source family; it does not exclude other graphs of order q^3 and maximum degree q+1.

## Auxiliary automorphism-matching observation

If an involutive automorphism rho of any graph fixes p, adding its nontrivial, non-old-edge pairs cannot enlarge any ball about p. In a mixed walk, commute each rho step past old graph steps using the automorphism property, move all rho steps to the fixed root, and remove them. Therefore B_D_new(p)=B_D_old(p). On an odd-order graph every involutive permutation has a fixed point, so its matching cannot improve the diameter beyond the eccentricity of that point. This is only an auxiliary rule-selection observation here: the arbitrary-matching bound above is stronger and already covers these matchings.

## Scope and evidence

The conclusion covers all simple complement matchings added to this fixed polynomial source, including partial matchings. It does not cover several added matchings, arbitrary added edges, deletions or rewiring, or general 343-vertex graphs of maximum degree eight. No actual augmented graph was generated; actual_n, actual_D and ordinary bad pairs stay null in the experimental record.

Existing evidence: `check_endpoint_budget.py`, `RESULT.json`, `FORMAL_ENDPOINT_IMAGE.json`. The q=5 instance requires the additional partner-ball overlap argument recorded separately in `../small_d6_D3_polynomial125_matching_overlap/ANALYSIS_PROOF.md`.
