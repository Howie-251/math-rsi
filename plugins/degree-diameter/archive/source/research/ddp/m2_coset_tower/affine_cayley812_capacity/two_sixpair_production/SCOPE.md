# Fixed two-mode degree-12 production scope

This production searches only the pair-phase multisets `(3,4,4,6,7,11)` and `(5,7,9,10,12,12)` in `F29 semidirect_2 C28`. They are the two six-pair modes whose minimum symbolic fiber capacity is 45. Other phase modes are outside this run.

An element is encoded `x+29*j`; multiplication is `(x,j)(y,k)=(x+2^j*y mod29,j+k mod28)`. The twelve actual generators are six pairs `s_i,s_i^(-1)`, with inverse `(-2^(-j)*x,-j)`. No reflection is present.

Each component representative has one field variable. The faithful scalar action gives the common affine automorphisms `F_(lambda,t)(x,j)=(lambda*x+(1−2^j)*t,j)`. In both modes the first phase is nonzero, so its scalar differs from one. A unique common translation sets its field coordinate to zero. The remaining five field coordinates are then considered up to nonzero common scalar multiplication. Enumerating a first nonzero position, putting one there, and enumerating every base-29 tail gives exactly

`1+29+29^2+29^3+29^4 = (29^5−1)/28 = 732,541`

marked projective inputs per mode, or **1,465,082** total. The all-zero remaining vector lies in the 28-element complement and cannot generate the full group. No second normalization is applied. The reused linear-basis machinery has the identity basis and rank zero, so it imposes no extra equations: actual fields are simply `(0,z0,z1,z2,z3,z4)`.

All pair phases are between 1 and 13, hence neither the identity nor an involution can arise as one of these representatives, whatever its field value. In each mode exactly one phase is repeated twice. Its two actual inverse pairs coincide exactly when those two field coordinates coincide. This is one nonzero homogeneous equation on the five remaining coordinates, giving `(29^4−1)/28=25,260` illegal projective inputs. All other pairs have different phase classes and cannot collide. Thus the expected complete-run counts are **707,281 legal and 25,260 illegal per mode**, or **1,414,562 legal and 50,520 illegal** overall. The program still checks the actual twelve elements individually rather than relying on this count.

For every legal input, a complete BFS from the identity computes connectivity, eccentricity and all distance layers. Cayley left translation is transitive, so one complete root determines the graph diameter and the global unordered radius-three defect `812*root_deficit/2`. The BFS is not truncated at distance three. Only one minimum-deficit complete edge table is retained, with ties left at the first occurrence.

The single process stops immediately on a diameter-three graph or completes the exact scope. A CPU-limit exit preserves the next pattern, projective first-nonzero position, base-29 tail, local index and global cursor, without restarting. The 120 CPU-second budget includes preparation and compilation. Root owns the unique independent final graph check; there is no separate production preflight or repeated graph audit here.
