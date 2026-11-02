# Frozen sumset and same-label obstruction check

Fix the current cyclic model: vertices(a in Z8,l in F2^3), internal cube flips1,2,4, sigma(a,l)=(a+delta_l,pi(l)), true inverse, and pi=[3,4,7,0,1,6,5,2]. No other pi/group is considered.

Prediction1: among the21 three-element subsets of Z8 containing0, A+B=Z8 holds precisely for the18 ordered pairs with one set a three-term AP of odd step±1 and the other of odd step±3. In particular neither set has a pair of elements differing by4.

Prediction2: the complete same-label phase set for walks of length at most3 is {0} union ±w_l union ±delta_l union ±delta_pi(l) union ±delta_j union ±delta_pi(j), where w_l=delta_l+delta_pi(l), and j=l XOR1 is one endpoint of the pi edge between two cube neighbors of l. The other endpoint is pi(j), also a cube neighbor of l. This classification will be proved directly by I/E word types, not by graph/BFS enumeration.

The previously checked antipode equality A_l+A_r=Z8, A_l={0,delta_l,-delta_pi(l)}, forces all A_l to have exactly3 elements. Prediction1 then excludes4 from every term in Prediction2. Thus (a,l) cannot reach(a+4,l) in at most3 steps for any delta assignment satisfying the necessary antipode conditions. This would close the full fixed-pi cyclic-voltage family, not merely the previous candidate.

Only the21² exact sumset table is authorized numerically, <=5 CPU seconds, one worker. No graph generation, BFS, solver, delta enumeration, alternative pi, or new group.
