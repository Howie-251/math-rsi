# Current (5,7)=6000: exact recipe and a bounded transfer decision

The primary author README and construction.json both describe the current 6000-vertex graph. No exact source6000/deg5-dia7 fixed scope was found in the existing method ledger search. The earlier source20400/H48 work concerns a different group and graph. Only these two primary files were downloaded; no 6000-vertex edge list, original-source BFS, or source search code was executed.

Primary sources:
- https://raw.githubusercontent.com/f4t4nt/degree-diameter-graphs/main/graphs/deg5/dia7/README.md
- https://raw.githubusercontent.com/f4t4nt/degree-diameter-graphs/main/graphs/deg5/dia7/construction.json

## Actual construction

There are two base vertices. The group has order 3000 and normal form (w,c^i,z^j)y^m, where w is a column in F5^2, i modulo 3, j modulo 5, m modulo 8. Put

    B=[[0,4],[1,4]], A=[[1,1],[2,4]].

Then B^3=I, A^2=3I, A^8=I, and ABA^-1=B^-1. The group is ((F5^2 semidirect C3) x C5) semidirect C8. Multiplication is

    (w,i,j,m)(W,I,J,M)
      =(w+B^i A^m W, i+2^m I mod3, j+2^m J mod5, m+M mod8).

The three links 0 to 1 have voltages identity, P=((0,1),c,z)y^4, and Q=((1,4),c,z^4)y^7. Base0 has a loop of voltage y, and base1 a loop of voltage D=((0,2),c,z^4)y^4. Reverse darts use the true group inverses. Direct small group arithmetic gives orders y=8, D=30, P=30, Q=8. The three link voltages are distinct, and both loop voltages have order greater than 2, so this rule gives a simple 5-regular lift. The published diameter7 is inherited from the author, not reverified here. The two base fibers are the two deck-group orbits.

## New prediction and exact local test

PREDICTION.json froze the numerical prediction that some target in the z-deleted quotient has fewer than 13 nonbacktracking words of length at most 7. It is supported.

Deleting z leaves a group of order600, and the two-base projected graph has 1200 states. All named nonbacktracking words of length0 through7 were enumerated from each of its two identity roots: 27306 words per root, 54612 total. This is word enumeration, not graph BFS.

The rootbase0 minimum is12. The rootbase1 minimum is10, at targetbase1 with quotient normal coordinates w=(2,4), c-exponent1, y-exponent0. Every projected walk of length at most7 reduces to one of these named nonbacktracking words without changing its endpoint. Every ordinary cover has a unique lift of each projected word from a fixed start. Consequently this fixed projected graph cannot support a degree5/D7 ordinary cover with more than10 sheets, irrespective of a cyclic scalar action or the individual sheet voltages. This specifically blocks the natural C13/C17 enlargement before graph generation.

For the exact source z-exponents 1 and4, the same thin slot has only9 distinct formal z endpoint polynomials in Z[r]/(r^8-1). The full formal sets are saved in FORMAL_Z_POLYNOMIAL_SETS.json. A legal cyclic action satisfies r^8=1. Evaluating nine polynomials can give at most nine cyclic endpoints; this stronger bound is for the fixed literal z-voltage rule, not arbitrary replacement voltages. No modulus or scalar action was numerically evaluated in this task.

## Constructive consequence and stopping scope

The source z action has exact order4. All larger cyclic moduli preserving this action order and the literal voltage rule are blocked: moduli11 and higher violate the raw ten-route bound; modulus10 violates the nine-polynomial bound; the unit groups modulo6,7,8,9 have no element of order4. Thus simply enlarging the source z factor while preserving its action order is not a useful candidate. The next meaningful rule would need to change the action order, the projected voltage arrangement, or another part of the group. None of those alternatives was started or declared impossible.

The small arithmetic/word test used 0.113592038 CPU seconds. No original source BFS, candidate graph generation, candidate modulus evaluation, or whole-graph diameter test was performed. Ordinary bad-pair counts and any new graph's actual diameter remain null. The transfer source stage is complete and stopped pending a parent decision.
