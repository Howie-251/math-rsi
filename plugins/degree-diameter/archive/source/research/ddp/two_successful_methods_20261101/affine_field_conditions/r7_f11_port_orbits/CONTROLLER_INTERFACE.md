# Derived fixed seven-port controller interface

This note derives an interface from the ten actual F11 charts. It does not search for or instantiate controller parameters. The chart data apply only to the final port order [1,4,infinity,0,2,3,5] and reverse map pi=[1,0,3,2,4,5,6].

Let C_p(u) be a simple controller's neighbor at port p. Require C_pi(p)(C_p(u))=u, seven distinct neighbors at every u, and no controller loops. Ports 0,1 are the two special types and form a spanning two-factor. Ports 2,3 form an oriented ordinary two-factor. Ports 4,5,6 are ordinary perfect matchings. This is more specific than an arbitrary seven-regular controller with sorted neighbor labels.

Use the 0-to-1 chart on each port-0 dart and its literal inverse on the paired port-1 dart. Do the same for ports 2,3. For each matching edge of port 4,5 or 6, choose either endpoint as its plus orientation; the reverse dart uses the actual minus matrix. Both orientations are among the ten checked charts. A cross-port chart cannot be inverted while leaving its source and target port labels fixed. Every dart matrix T satisfies T ell(p)=ell(pi(p)) with exact coefficient one; the reverse matrix is T^-1 and its noise parameter is -t.

## One three-base symbolic topology

Take controller vertices (i,g) with i in {0,1,2}, g in Z/m, with m even and h=m/2. Define permutations A and B by

```
A(0,g)=(0,g+alpha0)
A(1,g)=(2,g+alpha1)
A(2,g)=(1,g+alpha2)
B(i,g)=(i+1 mod 3,g).
```

Assign ports 0,1 to A,A^-1 and ports 2,3 to B,B^-1. Define the three self-reverse matchings as

```
S(0,g)=(1,g+sigma)   S(1,g)=(0,g-sigma)  S(2,g)=(2,g+h)
T(0,g)=(2,g+tau)     T(2,g)=(0,g-tau)    T(1,g)=(1,g+h)
R(1,g)=(2,g+rho)     R(2,g)=(1,g-rho)    R(0,g)=(0,g+h).
```

Assign S,T,R to ports 4,5,6. Each is an involution without fixed vertices. A sufficient and exact set of residue restrictions for the seven displayed neighbors to be distinct and loop-free is

```
alpha0 not in {0,h};
alpha1 != 0, alpha2 != 0, alpha1+alpha2 != 0;
sigma != 0, tau != 0;
rho not in {0,alpha1,-alpha2}.
```

These follow by comparing targets within each of the three bases; they have not been used for a parameter search. In particular R is not the global half-shift added to the old six-port controller: the old S on base 2 and T on base 1 already use that half-shift. R instead exchanges bases 1 and 2 and uses the half-shift only on base 0.

The B edges give the triangle (0,g),(1,g),(2,g) through every vertex. Thus this topology satisfies the same-fiber triangle requirement symbolically. It does not yet satisfy the distinct-controller three-walk coverage requirement merely by its definition.

## Why field checks do not depend on controller parameters

Consider a nonbacktracking three-dart controller walk, with matrices T1,T2,T3. Write p_j for its outgoing port and q_j=pi(p_j) for the target port of dart j. Its affine noise columns at the endpoint are

```
T3*T2*ell(q1), T3*ell(q2), ell(q3).
```

After applying the invertible matrix T3^-1, these become

```
T2*ell(q1), ell(q2), ell(p3).
```

Nonbacktracking means q1!=p2 and p3!=q2. The determinant is therefore one of the 36 nonzero determinants for the **middle chart T2**, up to a column swap. This works for all ten possible middle charts, including either actual orientation of every self port. The three independent F11 noise parameters reach every vector in the endpoint fiber. No controller-specific field-rank enumeration is required.

For adjacent controllers u to v with middle matrix T, three-step routes that backtrack first at u give the six planes span(ell(q),T ell(s)), s!=p, around the affine translate T*x. Routes that backtrack last at v give the six planes span(ell(q),ell(t)), t!=q. The already checked twelve-plane pencil covers F11³. The one-step line is common to these planes. Thus every pair in these adjacent fibers is covered in at most three steps without another finite field check.

To use these observations for a complete diameter-three construction, it is sufficient that every ordered distinct **nonadjacent** controller pair have a nonbacktracking walk of length exactly three, and that every controller vertex lie on a triangle for pairs in the same fiber. A controller distance-two path by itself does not suffice for all fiber differences: its two noise parameters span only a plane. The topology above supplies the triangles by B, but its exact three-walk coverage remains to be established by the root's separate bounded controller work.

For any controller that meets these conditions and the dart binding, its lift would have 1331 times the controller order and degree 7*11=77. This is a conditional consequence, not a produced graph or an accepted diameter claim.
