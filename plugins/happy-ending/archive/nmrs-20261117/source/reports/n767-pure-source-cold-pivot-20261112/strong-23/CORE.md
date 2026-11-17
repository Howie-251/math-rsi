# Independently checked trimmed core

These are clauses of the original literal twenty-three-point private-gap model; this is not a new mathematical extraction assumption. Both the original proof and the trimmed proof were checked.

| Core | Original | Predicate | Physical literals (disjunction) |
|---:|---:|---|---|
| 1 | 21 | weak_R6_B3 | `not E_R6(17, 23) OR R(17, 18, 23)` |
| 2 | 85 | weak_R6_B3 | `not E_R6(14, 23) OR R(14, 15, 23)` |
| 3 | 86 | weak_R6_B3 | `R(14, 16, 23) OR not E_R6(14, 23)` |
| 4 | 121 | weak_R6_B3 | `not E_R6(13, 23) OR R(13, 14, 23)` |
| 5 | 370 | weak_R6_B3 | `not E_R6(9, 23) OR R(9, 15, 23)` |
| 6 | 419 | weak_R6_B3 | `not E_R6(9, 19) OR R(9, 18, 19)` |
| 7 | 780 | weak_R6_B3 | `not E_R6(6, 16) OR R(6, 15, 16)` |
| 8 | 817 | weak_R6_B3 | `not E_R6(5, 23) OR R(5, 6, 23)` |
| 9 | 892 | weak_R6_B3 | `not E_R6(5, 18) OR R(5, 6, 18)` |
| 10 | 904 | weak_R6_B3 | `not E_R6(5, 17) OR R(5, 6, 17)` |
| 11 | 925 | weak_R6_B3 | `not E_R6(5, 15) OR R(5, 6, 15)` |
| 12 | 934 | weak_R6_B3 | `not E_R6(5, 14) OR R(5, 6, 14)` |
| 13 | 1097 | weak_R6_B3 | `not E_R6(4, 14) OR R(4, 6, 14)` |
| 14 | 1635 | weak_R6_B3 | `not E_R6(1, 19) OR R(1, 18, 19)` |
| 15 | 1685 | weak_R6_B3 | `not E_R6(1, 15) OR R(1, 6, 15)` |
| 16 | 1698 | weak_R6_B3 | `not E_R6(1, 14) OR R(1, 6, 14)` |
| 17 | 1761 | weak_R6_B3 | `not E_R6(1, 7) OR R(1, 6, 7)` |
| 18 | 3049 | weak_R5_B4 | `R(9, 15, 18) OR not E_R5(9, 19) OR R(15, 18, 19)` |
| 19 | 5295 | weak_R5_B4 | `not E_R5(5, 19) OR R(5, 6, 18) OR R(6, 18, 19)` |
| 20 | 5491 | weak_R5_B4 | `R(6, 15, 16) OR not E_R5(5, 16) OR R(5, 6, 15)` |
| 21 | 5566 | weak_R5_B4 | `not E_R5(5, 14) OR R(6, 9, 14) OR R(5, 6, 9)` |
| 22 | 5572 | weak_R5_B4 | `R(7, 9, 14) OR R(5, 7, 9) OR not E_R5(5, 14)` |
| 23 | 5577 | weak_R5_B4 | `R(5, 8, 9) OR R(8, 9, 14) OR not E_R5(5, 14)` |
| 24 | 6406 | weak_R5_B4 | `not E_R5(4, 16) OR R(4, 5, 15) OR R(5, 15, 16)` |
| 25 | 6500 | weak_R5_B4 | `not E_R5(4, 14) OR R(5, 9, 14) OR R(4, 5, 9)` |
| 26 | 6513 | weak_R5_B4 | `R(4, 7, 9) OR R(7, 9, 14) OR not E_R5(4, 14)` |
| 27 | 10529 | weak_R5_B4 | `R(5, 7, 11) OR not E_R5(1, 11) OR R(1, 5, 7)` |
| 28 | 10567 | weak_R5_B4 | `not E_R5(1, 10) OR R(1, 6, 9) OR R(6, 9, 10)` |
| 29 | 13496 | weak_R4_B5 | `not E_R4(9, 19) OR R(9, 14, 15) OR R(14, 15, 18) OR R(15, 18, 19)` |
| 30 | 44281 | no_R7 | `not R(15, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 31 | 44282 | no_R7 | `not R(14, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 32 | 44287 | no_R7 | `not R(9, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 33 | 44290 | no_R7 | `not R(6, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 34 | 44295 | no_R7 | `not R(1, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 35 | 44313 | R6_endpoint_implication | `not R(17, 19, 20) OR E_R6(17, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR not R(21, 22, 23)` |
| 36 | 44358 | R6_endpoint_implication | `E_R6(14, 23) OR not R(14, 19, 20) OR not R(19, 20, 21) OR not R(20, 21, 22) OR not R(21, 22, 23)` |
| 37 | 44371 | R6_endpoint_implication | `not R(13, 19, 20) OR E_R6(13, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR not R(21, 22, 23)` |
| 38 | 44385 | no_R7 | `not R(9, 11, 19) OR not R(11, 19, 20) OR not R(19, 20, 21) OR not R(20, 21, 22) OR not R(21, 22, 23)` |
| 39 | 44413 | R6_endpoint_implication | `E_R6(9, 23) OR not R(9, 19, 20) OR not R(19, 20, 21) OR not R(20, 21, 22) OR not R(21, 22, 23)` |
| 40 | 45597 | no_R7 | `not R(19, 21, 22) OR not R(17, 19, 21) OR not R(16, 17, 19) OR not R(21, 22, 23) OR not R(15, 16, 17)` |
| 41 | 46094 | R6_endpoint_implication | `not R(19, 21, 22) OR not R(13, 19, 21) OR not R(9, 13, 19) OR E_R6(9, 23) OR not R(21, 22, 23)` |
| 42 | 46161 | R6_endpoint_implication | `not R(19, 21, 22) OR not R(12, 19, 21) OR not R(9, 12, 19) OR E_R6(9, 23) OR not R(21, 22, 23)` |
| 43 | 46199 | no_R7 | `not R(11, 19, 21) OR not R(10, 11, 19) OR not R(19, 21, 22) OR not R(21, 22, 23) OR not R(9, 10, 11)` |
| 44 | 60777 | packet | `R(19, 20, 22) OR not R(19, 21, 22) OR not R(19, 20, 21) OR not R(20, 21, 22)` |
| 45 | 60778 | packet | `not R(19, 20, 22) OR R(19, 21, 22) OR not R(19, 20, 21) OR not R(20, 21, 22)` |
| 46 | 61767 | packet | `R(19, 20, 22) OR R(19, 21, 22) OR not R(19, 20, 21) OR not R(20, 21, 22)` |
| 47 | 149429 | no_R7 | `not R(17, 18, 23) OR not R(6, 15, 16) OR not R(1, 6, 15) OR not R(16, 17, 18) OR not R(15, 16, 17)` |
| 48 | 149435 | R6_endpoint_implication | `not R(5, 15, 16) OR not R(17, 18, 23) OR not R(15, 16, 17) OR not R(16, 17, 18) OR E_R6(5, 23)` |
| 49 | 149806 | no_R7 | `not R(9, 16, 17) OR not R(1, 6, 9) OR not R(17, 18, 23) OR not R(6, 9, 16) OR not R(16, 17, 18)` |
| 50 | 149812 | R6_endpoint_implication | `not R(5, 9, 16) OR not R(9, 16, 17) OR not R(17, 18, 23) OR not R(16, 17, 18) OR E_R6(5, 23)` |
| 51 | 200832 | R6_endpoint_implication | `not R(6, 15, 16) OR not R(1, 6, 15) OR not R(16, 17, 19) OR not R(15, 16, 17) OR E_R6(1, 19)` |
| 52 | 200844 | R5_endpoint_implication | `not R(5, 15, 16) OR not R(16, 17, 19) OR not R(15, 16, 17) OR E_R5(5, 19)` |
| 53 | 202164 | R6_endpoint_implication | `not R(1, 6, 9) OR not R(9, 16, 17) OR not R(16, 17, 19) OR not R(6, 9, 16) OR E_R6(1, 19)` |
| 54 | 202176 | R5_endpoint_implication | `not R(9, 16, 17) OR not R(5, 9, 16) OR not R(16, 17, 19) OR E_R5(5, 19)` |
| 55 | 202465 | no_R7 | `not R(14, 15, 16) OR not R(1, 6, 14) OR not R(15, 16, 17) OR not R(16, 17, 18) OR not R(6, 14, 15)` |
| 56 | 202471 | R6_endpoint_implication | `not R(14, 15, 16) OR not R(5, 14, 15) OR not R(15, 16, 17) OR not R(16, 17, 18) OR E_R6(5, 18)` |
| 57 | 247052 | no_R7 | `not R(9, 15, 16) OR not R(15, 16, 17) OR not R(8, 9, 15) OR not R(7, 8, 9) OR not R(6, 7, 8)` |
| 58 | 272589 | no_R7 | `not R(8, 14, 16) OR not R(14, 16, 23) OR not R(7, 8, 14) OR not R(1, 6, 7) OR not R(6, 7, 8)` |
| 59 | 272595 | R6_endpoint_implication | `not R(8, 14, 16) OR not R(7, 8, 14) OR not R(5, 7, 8) OR not R(14, 16, 23) OR E_R6(5, 23)` |
| 60 | 280534 | packet | `not R(9, 14, 23) OR not R(14, 15, 23) OR not R(9, 14, 15) OR R(9, 15, 23)` |
| 61 | 280628 | packet | `R(9, 14, 23) OR not R(14, 15, 23) OR not R(9, 14, 15) OR R(9, 15, 23)` |
| 62 | 286382 | no_R7 | `not R(14, 15, 18) OR not R(7, 8, 14) OR not R(8, 14, 15) OR not R(1, 6, 7) OR not R(6, 7, 8)` |
| 63 | 286388 | R6_endpoint_implication | `not R(7, 8, 14) OR not R(5, 7, 8) OR not R(8, 14, 15) OR not R(14, 15, 18) OR E_R6(5, 18)` |
| 64 | 319583 | no_R7 | `not R(13, 14, 23) OR not R(12, 13, 14) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 65 | 326347 | no_R7 | `not R(13, 14, 15) OR not R(12, 13, 14) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 66 | 332842 | packet | `not R(12, 13, 20) OR not R(12, 19, 20) OR R(12, 13, 19) OR R(13, 19, 20)` |
| 67 | 333449 | packet | `R(12, 13, 20) OR not R(12, 19, 20) OR R(12, 13, 19) OR R(13, 19, 20)` |
| 68 | 357474 | packet | `R(12, 19, 20) OR not R(12, 13, 20) OR R(12, 13, 19) OR R(13, 19, 20)` |
| 69 | 357486 | R6_endpoint_implication | `not R(12, 13, 19) OR E_R6(9, 19) OR not R(10, 11, 12) OR not R(9, 10, 11) OR not R(11, 12, 13)` |
| 70 | 360520 | no_R7 | `not R(6, 9, 10) OR not R(12, 13, 14) OR not R(10, 11, 12) OR not R(9, 10, 11) OR not R(11, 12, 13)` |
| 71 | 360521 | no_R7 | `not R(5, 9, 10) OR not R(12, 13, 14) OR not R(10, 11, 12) OR not R(9, 10, 11) OR not R(11, 12, 13)` |
| 72 | 360522 | no_R7 | `not R(4, 9, 10) OR not R(12, 13, 14) OR not R(10, 11, 12) OR not R(9, 10, 11) OR not R(11, 12, 13)` |
| 73 | 360552 | R6_endpoint_implication | `not R(5, 10, 11) OR E_R6(5, 14) OR not R(10, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 74 | 360556 | R6_endpoint_implication | `not R(4, 10, 11) OR E_R6(4, 14) OR not R(10, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 75 | 360572 | no_R7 | `not R(7, 9, 11) OR not R(6, 7, 9) OR not R(9, 11, 12) OR not R(12, 13, 14) OR not R(11, 12, 13)` |
| 76 | 360640 | R6_endpoint_implication | `not R(7, 11, 12) OR not R(5, 7, 11) OR not R(11, 12, 13) OR not R(12, 13, 14) OR E_R6(5, 14)` |
| 77 | 360673 | no_R7 | `not R(5, 11, 12) OR not R(3, 5, 11) OR not R(1, 3, 5) OR not R(12, 13, 14) OR not R(11, 12, 13)` |
| 78 | 360678 | R5_endpoint_implication | `E_R5(5, 14) OR not R(5, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 79 | 360685 | R5_endpoint_implication | `not R(4, 11, 12) OR E_R5(4, 14) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 80 | 360832 | no_R7 | `not R(8, 9, 12) OR not R(9, 12, 13) OR not R(12, 13, 14) OR not R(7, 8, 9) OR not R(6, 7, 8)` |
| 81 | 365186 | packet | `not R(11, 12, 20) OR not R(11, 19, 20) OR R(11, 12, 19) OR R(12, 19, 20)` |
| 82 | 365613 | packet | `R(11, 12, 20) OR not R(11, 19, 20) OR R(11, 12, 19) OR R(12, 19, 20)` |
| 83 | 382738 | packet | `not R(11, 13, 19) OR R(11, 12, 19) OR not R(11, 12, 13) OR R(12, 13, 19)` |
| 84 | 385291 | no_R7 | `not R(3, 4, 11) OR not R(4, 11, 13) OR not R(11, 13, 14) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 85 | 387093 | R5_endpoint_implication | `not R(11, 12, 19) OR E_R5(9, 19) OR not R(9, 10, 11) OR not R(10, 11, 12)` |
| 86 | 389625 | packet | `R(10, 11, 13) OR not R(10, 12, 13) OR not R(10, 11, 12) OR not R(11, 12, 13)` |
| 87 | 389757 | packet | `R(10, 11, 13) OR R(10, 12, 13) OR not R(10, 11, 12) OR not R(11, 12, 13)` |
| 88 | 411632 | R4_endpoint_implication | `E_R4(9, 19) OR not R(10, 11, 19) OR not R(9, 10, 11)` |
| 89 | 412965 | packet | `R(5, 11, 15) OR not R(10, 11, 15) OR R(5, 10, 11) OR not R(5, 10, 15)` |
| 90 | 413601 | packet | `R(9, 10, 12) OR not R(9, 11, 12) OR not R(9, 10, 11) OR not R(10, 11, 12)` |
| 91 | 420069 | no_R7 | `not R(9, 15, 23) OR not R(1, 6, 7) OR not R(7, 8, 9) OR not R(6, 7, 8) OR not R(8, 9, 15)` |
| 92 | 420075 | R6_endpoint_implication | `not R(9, 15, 23) OR not R(5, 7, 8) OR not R(7, 8, 9) OR not R(8, 9, 15) OR E_R6(5, 23)` |
| 93 | 421139 | no_R7 | `not R(9, 15, 18) OR not R(1, 6, 7) OR not R(7, 8, 9) OR not R(6, 7, 8) OR not R(8, 9, 15)` |
| 94 | 421145 | R6_endpoint_implication | `not R(9, 15, 18) OR not R(5, 7, 8) OR not R(7, 8, 9) OR not R(8, 9, 15) OR E_R6(5, 18)` |
| 95 | 422695 | R6_endpoint_implication | `not R(7, 9, 14) OR not R(9, 14, 19) OR not R(6, 7, 9) OR not R(1, 6, 7) OR E_R6(1, 19)` |
| 96 | 422707 | R5_endpoint_implication | `not R(7, 9, 14) OR not R(9, 14, 19) OR not R(5, 7, 9) OR E_R5(5, 19)` |
| 97 | 423042 | R6_endpoint_implication | `not R(8, 9, 14) OR not R(5, 7, 8) OR not R(9, 14, 17) OR not R(7, 8, 9) OR E_R6(5, 17)` |
| 98 | 423238 | packet | `R(8, 14, 16) OR not R(8, 9, 14) OR not R(8, 9, 16) OR not R(9, 14, 16)` |
| 99 | 423239 | packet | `R(8, 14, 16) OR not R(9, 14, 16) OR not R(8, 9, 16) OR R(8, 9, 14)` |
| 100 | 423245 | R6_endpoint_implication | `not R(8, 9, 14) OR not R(9, 14, 16) OR E_R6(6, 16) OR not R(6, 7, 8) OR not R(7, 8, 9)` |
| 101 | 423303 | packet | `R(8, 14, 16) OR R(8, 9, 16) OR not R(9, 14, 16) OR not R(8, 9, 14)` |
| 102 | 423351 | packet | `not R(6, 14, 16) OR R(6, 9, 16) OR not R(9, 14, 16) OR not R(6, 9, 14)` |
| 103 | 423379 | packet | `R(6, 9, 16) OR R(6, 14, 16) OR not R(9, 14, 16) OR not R(6, 9, 14)` |
| 104 | 423381 | packet | `not R(5, 14, 16) OR not R(5, 9, 14) OR not R(9, 14, 16) OR R(5, 9, 16)` |
| 105 | 423398 | packet | `not R(5, 9, 14) OR not R(9, 14, 16) OR R(5, 9, 16) OR R(5, 14, 16)` |
| 106 | 423435 | packet | `not R(9, 14, 16) OR R(9, 14, 15) OR R(14, 15, 16) OR R(9, 15, 16)` |
| 107 | 423451 | no_R7 | `not R(8, 9, 14) OR not R(1, 6, 7) OR not R(9, 14, 15) OR not R(6, 7, 8) OR not R(7, 8, 9)` |
| 108 | 423457 | R6_endpoint_implication | `not R(8, 9, 14) OR not R(5, 7, 8) OR not R(9, 14, 15) OR not R(7, 8, 9) OR E_R6(5, 15)` |
| 109 | 424686 | packet | `R(9, 12, 13) OR R(9, 12, 19) OR not R(9, 13, 19) OR R(12, 13, 19)` |
| 110 | 425527 | no_R7 | `not R(8, 9, 13) OR not R(1, 6, 7) OR not R(7, 8, 9) OR not R(6, 7, 8) OR not R(9, 13, 14)` |
| 111 | 425533 | R6_endpoint_implication | `not R(8, 9, 13) OR not R(5, 7, 8) OR not R(7, 8, 9) OR not R(9, 13, 14) OR E_R6(5, 14)` |
| 112 | 432954 | packet | `not R(5, 9, 11) OR R(5, 10, 11) OR not R(9, 10, 11) OR R(5, 9, 10)` |
| 113 | 446764 | R6_endpoint_implication | `not R(8, 9, 19) OR not R(1, 6, 7) OR not R(6, 7, 8) OR not R(7, 8, 9) OR E_R6(1, 19)` |
| 114 | 446776 | R5_endpoint_implication | `not R(8, 9, 19) OR not R(5, 7, 8) OR not R(7, 8, 9) OR E_R5(5, 19)` |
| 115 | 447178 | R5_endpoint_implication | `E_R5(5, 16) OR not R(5, 7, 8) OR not R(8, 9, 16) OR not R(7, 8, 9)` |
| 116 | 447185 | R5_endpoint_implication | `not R(4, 7, 8) OR E_R5(4, 16) OR not R(8, 9, 16) OR not R(7, 8, 9)` |
| 117 | 447281 | packet | `R(7, 8, 15) OR not R(7, 9, 15) OR not R(7, 8, 9) OR not R(8, 9, 15)` |
| 118 | 447298 | R6_endpoint_implication | `not R(1, 6, 7) OR E_R6(1, 15) OR not R(6, 7, 8) OR not R(7, 8, 9) OR not R(8, 9, 15)` |
| 119 | 447309 | R6_endpoint_implication | `not R(1, 5, 7) OR not R(5, 7, 8) OR E_R6(1, 15) OR not R(8, 9, 15) OR not R(7, 8, 9)` |
| 120 | 447357 | packet | `R(5, 8, 15) OR not R(5, 8, 9) OR not R(8, 9, 15) OR not R(5, 9, 15)` |
| 121 | 447412 | packet | `R(7, 8, 14) OR not R(8, 9, 14) OR not R(7, 9, 14) OR not R(7, 8, 9)` |
| 122 | 458110 | no_R7 | `not R(5, 7, 9) OR not R(4, 5, 7) OR not R(7, 9, 15) OR not R(3, 4, 5) OR not R(1, 3, 4)` |
| 123 | 458163 | packet | `R(7, 8, 14) OR R(8, 9, 14) OR not R(7, 9, 14) OR not R(7, 8, 9)` |
| 124 | 459342 | packet | `R(5, 8, 15) OR not R(5, 7, 15) OR not R(5, 7, 8) OR not R(7, 8, 15)` |
| 125 | 459812 | packet | `not R(6, 8, 9) OR R(6, 7, 9) OR not R(6, 7, 8) OR not R(7, 8, 9)` |
| 126 | 459850 | packet | `R(6, 7, 9) OR R(6, 8, 9) OR not R(6, 7, 8) OR not R(7, 8, 9)` |
| 127 | 459852 | packet | `R(5, 7, 9) OR not R(5, 8, 9) OR not R(5, 7, 8) OR not R(7, 8, 9)` |
| 128 | 463453 | packet | `R(6, 9, 16) OR not R(6, 14, 16) OR R(9, 14, 16) OR not R(6, 9, 14)` |
| 129 | 463552 | no_R7 | `not R(4, 6, 14) OR not R(6, 14, 15) OR not R(3, 4, 6) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 130 | 472305 | packet | `not R(5, 14, 16) OR not R(5, 9, 14) OR R(5, 9, 16) OR R(9, 14, 16)` |
| 131 | 474007 | no_R7 | `not R(4, 5, 11) OR not R(5, 11, 15) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 132 | 475859 | no_R7 | `not R(4, 5, 8) OR not R(5, 8, 15) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 133 | 476505 | no_R7 | `not R(5, 7, 15) OR not R(4, 5, 7) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 134 | 476807 | no_R7 | `not R(5, 6, 23) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 135 | 477032 | no_R7 | `not R(5, 6, 18) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 136 | 477074 | no_R7 | `not R(5, 6, 17) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 137 | 477155 | no_R7 | `not R(5, 6, 15) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 138 | 477194 | no_R7 | `not R(5, 6, 14) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 139 | 477374 | pure_p_no_in_R6 | `not R(5, 6, 9) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4)` |
| 140 | 483548 | pure_p_no_in_R6 | `not R(3, 4, 7) OR not R(4, 7, 9) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 141 | 484367 | R6_endpoint_implication | `not R(4, 5, 15) OR E_R6(1, 15) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 142 | 484395 | R6_endpoint_implication | `E_R6(1, 14) OR not R(4, 5, 14) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 143 | 484516 | packet | `not R(4, 5, 10) OR R(4, 5, 9) OR R(4, 9, 10) OR R(5, 9, 10)` |
| 144 | 484520 | pure_p_no_in_R6 | `not R(4, 5, 9) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 145 | 484564 | R6_endpoint_implication | `not R(4, 5, 7) OR E_R6(1, 7) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 146 | 484581 | packet | `R(3, 4, 6) OR not R(3, 5, 6) OR not R(3, 4, 5) OR not R(4, 5, 6)` |
| 147 | 488675 | packet | `not R(3, 5, 10) OR not R(3, 10, 11) OR R(3, 5, 11) OR R(5, 10, 11)` |
| 148 | 488690 | packet | `R(3, 5, 10) OR not R(3, 10, 11) OR R(3, 5, 11) OR R(5, 10, 11)` |
| 149 | 491155 | R5_endpoint_implication | `E_R5(1, 11) OR not R(3, 4, 11) OR not R(1, 2, 3) OR not R(2, 3, 4)` |
| 150 | 491168 | packet | `R(3, 4, 10) OR R(3, 10, 11) OR not R(3, 4, 11) OR R(4, 10, 11)` |
| 151 | 491172 | R5_endpoint_implication | `not R(3, 4, 10) OR E_R5(1, 10) OR not R(1, 2, 3) OR not R(2, 3, 4)` |
| 152 | 491245 | packet | `R(1, 3, 5) OR not R(1, 4, 5) OR not R(3, 4, 5) OR not R(1, 3, 4)` |
| 153 | 491248 | packet | `R(1, 3, 5) OR R(1, 4, 5) OR not R(3, 4, 5) OR not R(1, 3, 4)` |
| 154 | 497615 | packet | `not R(1, 3, 4) OR R(1, 2, 4) OR not R(1, 2, 3) OR not R(2, 3, 4)` |
| 155 | 497616 | packet | `R(1, 3, 4) OR not R(1, 2, 4) OR not R(1, 2, 3) OR not R(2, 3, 4)` |
| 156 | 497618 | packet | `R(1, 3, 4) OR R(1, 2, 4) OR not R(1, 2, 3) OR not R(2, 3, 4)` |
| 157 | 503780 | frozen_red_path | `R(1, 2, 3)` |
| 158 | 531958 | frozen_red_path | `R(2, 3, 4)` |
| 159 | 553753 | frozen_red_path | `R(3, 4, 5)` |
| 160 | 555346 | A_no_in_B4 | `R(3, 4, 7) OR R(4, 7, 8)` |
| 161 | 557178 | no_B6 | `R(3, 4, 11) OR R(4, 11, 12) OR R(11, 12, 19) OR R(12, 19, 20)` |
| 162 | 557228 | no_B6 | `R(4, 11, 13) OR R(3, 4, 11) OR R(11, 13, 19) OR R(13, 19, 21)` |
| 163 | 558533 | A_no_in_B4 | `R(3, 5, 6) OR R(5, 6, 15)` |
| 164 | 570373 | frozen_red_path | `R(4, 5, 6)` |
| 165 | 571098 | A_no_in_B4 | `R(5, 7, 8) OR R(4, 5, 7)` |
| 166 | 571604 | A_no_in_B4 | `R(5, 7, 15) OR R(4, 5, 7)` |
| 167 | 571780 | no_B6 | `R(5, 8, 9) OR R(4, 5, 8) OR R(8, 9, 19) OR R(9, 19, 20)` |
| 168 | 572269 | no_B6 | `R(11, 12, 19) OR R(9, 11, 12) OR R(4, 5, 9) OR R(5, 9, 11)` |
| 169 | 572482 | T_no_B5_endpoints | `R(5, 9, 15) OR R(4, 5, 9) OR R(9, 15, 16)` |
| 170 | 572632 | no_B6 | `R(11, 19, 20) OR R(10, 11, 19) OR R(4, 5, 10) OR R(5, 10, 11)` |
| 171 | 572790 | A_no_in_B4 | `R(5, 10, 15) OR R(4, 5, 10)` |
| 172 | 572930 | no_B6 | `R(5, 11, 12) OR R(12, 19, 20) OR R(11, 12, 19) OR R(4, 5, 11)` |
| 173 | 573431 | A_no_in_B4 | `R(4, 5, 14) OR R(5, 14, 15)` |
| 174 | 585180 | A_no_in_B4 | `R(6, 14, 15) OR R(5, 6, 14)` |
| 175 | 590057 | A_no_in_B4 | `R(10, 11, 15) OR R(5, 10, 11)` |
| 176 | 592042 | frozen_red_path | `R(6, 7, 8)` |
| 177 | 600775 | frozen_red_path | `R(7, 8, 9)` |
| 178 | 603268 | T_no_B5_endpoints | `R(9, 11, 19) OR R(7, 9, 11) OR R(11, 19, 21)` |
| 179 | 603714 | no_T_to_T_B4 | `R(9, 14, 16) OR R(7, 9, 14)` |
| 180 | 603766 | T_no_B5_endpoints | `R(7, 9, 14) OR R(9, 14, 18) OR R(14, 18, 19)` |
| 181 | 603801 | no_T_to_T_B4 | `R(7, 9, 15) OR R(9, 15, 16)` |
| 182 | 603888 | no_T_to_T_B4 | `R(7, 9, 16) OR R(9, 16, 17)` |
| 183 | 605248 | T_no_B5_endpoints | `R(7, 11, 12) OR R(12, 19, 21) OR R(11, 12, 19)` |
| 184 | 607956 | T_no_B5_endpoints | `R(9, 12, 19) OR R(12, 19, 20) OR R(8, 9, 12)` |
| 185 | 608125 | T_no_B5_endpoints | `R(9, 13, 19) OR R(8, 9, 13) OR R(13, 19, 20)` |
| 186 | 608182 | no_T_to_T_B4 | `R(9, 14, 16) OR R(8, 9, 14)` |
| 187 | 608234 | T_no_B5_endpoints | `R(9, 14, 18) OR R(8, 9, 14) OR R(14, 18, 19)` |
| 188 | 608249 | T_no_B5_endpoints | `R(14, 19, 20) OR R(9, 14, 19) OR R(8, 9, 14)` |
| 189 | 608269 | frozen_red_path | `R(8, 9, 15)` |
| 190 | 608357 | no_T_to_T_B4 | `R(8, 9, 16) OR R(9, 16, 17)` |
| 191 | 611091 | no_T_to_T_B4 | `R(8, 14, 15) OR R(14, 15, 16)` |
| 192 | 611563 | frozen_red_path | `R(9, 10, 11)` |
| 193 | 613219 | A_no_in_B4 | `R(9, 13, 14) OR R(13, 14, 15)` |
| 194 | 613697 | frozen_red_path | `R(10, 11, 12)` |
| 195 | 615060 | frozen_red_path | `R(11, 12, 13)` |
| 196 | 615413 | A_no_in_B4 | `R(11, 13, 14) OR R(13, 14, 15)` |
| 197 | 615891 | frozen_red_path | `R(12, 13, 14)` |
| 198 | 616754 | frozen_red_path | `R(15, 16, 17)` |
| 199 | 616937 | frozen_red_path | `R(16, 17, 18)` |
| 200 | 616963 | B_no_out_B4 | `R(17, 19, 20) OR R(16, 17, 19)` |
| 201 | 616970 | B_no_out_B4 | `R(17, 19, 21) OR R(16, 17, 19)` |
| 202 | 617070 | frozen_red_path | `R(18, 19, 20)` |
| 203 | 617087 | frozen_red_path | `R(19, 20, 21)` |
| 204 | 617088 | frozen_red_path | `R(20, 21, 22)` |
| 205 | 617089 | frozen_red_path | `R(21, 22, 23)` |
