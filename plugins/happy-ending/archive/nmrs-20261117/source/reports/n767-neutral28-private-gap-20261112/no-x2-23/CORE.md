# Independently checked trimmed core

These are clauses of the original literal twenty-three-point private-gap model; this is not a new mathematical extraction assumption. Both the original proof and the trimmed proof were checked.

| Core | Original | Predicate | Physical literals (disjunction) |
|---:|---:|---|---|
| 1 | 21 | weak_R6_B3 | `not E_R6(17, 23) OR R(17, 18, 23)` |
| 2 | 85 | weak_R6_B3 | `not E_R6(14, 23) OR R(14, 15, 23)` |
| 3 | 122 | weak_R6_B3 | `not E_R6(13, 23) OR R(13, 15, 23)` |
| 4 | 168 | weak_R6_B3 | `not E_R6(12, 23) OR R(12, 15, 23)` |
| 5 | 224 | weak_R6_B3 | `not E_R6(11, 23) OR R(11, 15, 23)` |
| 6 | 546 | weak_R6_B3 | `not E_R6(8, 14) OR R(8, 9, 14)` |
| 7 | 817 | weak_R6_B3 | `not E_R6(5, 23) OR R(5, 6, 23)` |
| 8 | 892 | weak_R6_B3 | `not E_R6(5, 18) OR R(5, 6, 18)` |
| 9 | 934 | weak_R6_B3 | `not E_R6(5, 14) OR R(5, 6, 14)` |
| 10 | 1097 | weak_R6_B3 | `not E_R6(4, 14) OR R(4, 6, 14)` |
| 11 | 1278 | weak_R6_B3 | `not E_R6(3, 14) OR R(3, 6, 14)` |
| 12 | 1635 | weak_R6_B3 | `not E_R6(1, 19) OR R(1, 18, 19)` |
| 13 | 1685 | weak_R6_B3 | `not E_R6(1, 15) OR R(1, 6, 15)` |
| 14 | 1688 | weak_R6_B3 | `R(1, 9, 15) OR not E_R6(1, 15)` |
| 15 | 1743 | weak_R6_B3 | `not E_R6(1, 10) OR R(1, 9, 10)` |
| 16 | 1761 | weak_R6_B3 | `R(1, 6, 7) OR not E_R6(1, 7)` |
| 17 | 1763 | weak_R6_B3 | `R(1, 3, 6) OR not E_R6(1, 6)` |
| 18 | 1982 | weak_R5_B4 | `not E_R5(13, 23) OR R(13, 14, 15) OR R(14, 15, 23)` |
| 19 | 3049 | weak_R5_B4 | `not E_R5(9, 19) OR R(15, 18, 19) OR R(9, 15, 18)` |
| 20 | 5295 | weak_R5_B4 | `not E_R5(5, 19) OR R(5, 6, 18) OR R(6, 18, 19)` |
| 21 | 5491 | weak_R5_B4 | `not E_R5(5, 16) OR R(6, 15, 16) OR R(5, 6, 15)` |
| 22 | 5566 | weak_R5_B4 | `R(6, 9, 14) OR not E_R5(5, 14) OR R(5, 6, 9)` |
| 23 | 5572 | weak_R5_B4 | `R(7, 9, 14) OR R(5, 7, 9) OR not E_R5(5, 14)` |
| 24 | 5577 | weak_R5_B4 | `R(5, 8, 9) OR not E_R5(5, 14) OR R(8, 9, 14)` |
| 25 | 6400 | weak_R5_B4 | `R(5, 9, 16) OR not E_R5(4, 16) OR R(4, 5, 9)` |
| 26 | 6406 | weak_R5_B4 | `R(4, 5, 15) OR not E_R5(4, 16) OR R(5, 15, 16)` |
| 27 | 6500 | weak_R5_B4 | `not E_R5(4, 14) OR R(5, 9, 14) OR R(4, 5, 9)` |
| 28 | 6513 | weak_R5_B4 | `R(4, 7, 9) OR not E_R5(4, 14) OR R(7, 9, 14)` |
| 29 | 10529 | weak_R5_B4 | `not E_R5(1, 11) OR R(1, 5, 7) OR R(5, 7, 11)` |
| 30 | 10567 | weak_R5_B4 | `R(1, 6, 9) OR not E_R5(1, 10) OR R(6, 9, 10)` |
| 31 | 44281 | no_R7 | `not R(15, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 32 | 44290 | no_R7 | `not R(6, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 33 | 44295 | no_R7 | `not R(1, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 34 | 44313 | R6_endpoint_implication | `not R(17, 19, 20) OR E_R6(17, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR not R(21, 22, 23)` |
| 35 | 44358 | R6_endpoint_implication | `not R(14, 19, 20) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR E_R6(14, 23)` |
| 36 | 44371 | R6_endpoint_implication | `not R(13, 19, 20) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR E_R6(13, 23)` |
| 37 | 44383 | R6_endpoint_implication | `not R(12, 19, 20) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR E_R6(12, 23)` |
| 38 | 44394 | R6_endpoint_implication | `not R(11, 19, 20) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR E_R6(11, 23)` |
| 39 | 45146 | R5_endpoint_implication | `not R(13, 20, 21) OR E_R5(13, 23) OR not R(20, 21, 22) OR not R(21, 22, 23)` |
| 40 | 45608 | no_R7 | `not R(19, 21, 22) OR not R(17, 19, 21) OR not R(16, 17, 19) OR not R(21, 22, 23) OR not R(15, 16, 17)` |
| 41 | 60922 | packet | `R(19, 20, 22) OR not R(19, 21, 22) OR not R(19, 20, 21) OR not R(20, 21, 22)` |
| 42 | 60923 | packet | `not R(19, 20, 22) OR R(19, 21, 22) OR not R(19, 20, 21) OR not R(20, 21, 22)` |
| 43 | 61921 | packet | `R(19, 20, 22) OR R(19, 21, 22) OR not R(19, 20, 21) OR not R(20, 21, 22)` |
| 44 | 89876 | packet | `not R(13, 19, 21) OR R(13, 20, 21) OR not R(19, 20, 21) OR R(13, 19, 20)` |
| 45 | 150326 | no_R7 | `not R(17, 18, 23) OR not R(6, 15, 16) OR not R(1, 6, 15) OR not R(16, 17, 18) OR not R(15, 16, 17)` |
| 46 | 150332 | R6_endpoint_implication | `not R(5, 15, 16) OR not R(17, 18, 23) OR not R(15, 16, 17) OR not R(16, 17, 18) OR E_R6(5, 23)` |
| 47 | 150708 | no_R7 | `not R(9, 16, 17) OR not R(17, 18, 23) OR not R(6, 9, 16) OR not R(1, 6, 9) OR not R(16, 17, 18)` |
| 48 | 150714 | R6_endpoint_implication | `not R(5, 9, 16) OR not R(9, 16, 17) OR not R(17, 18, 23) OR not R(16, 17, 18) OR E_R6(5, 23)` |
| 49 | 202123 | R6_endpoint_implication | `not R(6, 15, 16) OR not R(1, 6, 15) OR not R(16, 17, 19) OR not R(15, 16, 17) OR E_R6(1, 19)` |
| 50 | 202135 | R5_endpoint_implication | `not R(5, 15, 16) OR not R(16, 17, 19) OR not R(15, 16, 17) OR E_R5(5, 19)` |
| 51 | 203465 | R6_endpoint_implication | `not R(9, 16, 17) OR not R(1, 6, 9) OR not R(16, 17, 19) OR not R(6, 9, 16) OR E_R6(1, 19)` |
| 52 | 203477 | R5_endpoint_implication | `not R(9, 16, 17) OR not R(5, 9, 16) OR not R(16, 17, 19) OR E_R5(5, 19)` |
| 53 | 204074 | no_R7 | `not R(8, 15, 16) OR not R(7, 8, 15) OR not R(15, 16, 17) OR not R(16, 17, 18) OR not R(6, 7, 8)` |
| 54 | 204442 | no_R7 | `not R(14, 16, 17) OR not R(1, 6, 9) OR not R(9, 14, 16) OR not R(16, 17, 18) OR not R(6, 9, 14)` |
| 55 | 204448 | R6_endpoint_implication | `not R(14, 16, 17) OR not R(5, 9, 14) OR not R(9, 14, 16) OR not R(16, 17, 18) OR E_R6(5, 18)` |
| 56 | 205433 | R6_endpoint_implication | `not R(8, 9, 16) OR not R(9, 16, 17) OR not R(16, 17, 18) OR not R(5, 8, 9) OR E_R6(5, 18)` |
| 57 | 281444 | necessary_blue_fan | `not R(14, 15, 23)` |
| 58 | 287224 | necessary_blue_fan | `not R(14, 15, 18)` |
| 59 | 314704 | necessary_blue_fan | `not R(13, 15, 23)` |
| 60 | 328307 | no_R7 | `not R(13, 14, 15) OR not R(12, 13, 14) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 61 | 332916 | packet | `not R(12, 20, 21) OR R(13, 20, 21) OR R(12, 13, 21) OR R(12, 13, 20)` |
| 62 | 334794 | packet | `not R(12, 19, 21) OR R(13, 19, 21) OR R(12, 13, 21) OR R(12, 13, 19)` |
| 63 | 346589 | necessary_blue_fan | `not R(12, 15, 23)` |
| 64 | 358269 | a4_R6_terminal_cut | `not R(12, 13, 21) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 65 | 358882 | a4_R6_terminal_cut | `not R(12, 13, 20) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 66 | 359494 | a4_R6_terminal_cut | `not R(12, 13, 19) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 67 | 362540 | no_R7 | `not R(6, 9, 10) OR not R(12, 13, 14) OR not R(10, 11, 12) OR not R(9, 10, 11) OR not R(11, 12, 13)` |
| 68 | 362545 | no_R7 | `not R(1, 9, 10) OR not R(12, 13, 14) OR not R(10, 11, 12) OR not R(9, 10, 11) OR not R(11, 12, 13)` |
| 69 | 362554 | R6_endpoint_implication | `not R(8, 10, 11) OR not R(12, 13, 14) OR not R(10, 11, 12) OR not R(11, 12, 13) OR E_R6(8, 14)` |
| 70 | 362572 | R6_endpoint_implication | `not R(5, 10, 11) OR E_R6(5, 14) OR not R(10, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 71 | 362576 | R6_endpoint_implication | `not R(4, 10, 11) OR E_R6(4, 14) OR not R(10, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 72 | 362579 | R6_endpoint_implication | `E_R6(3, 14) OR not R(3, 10, 11) OR not R(10, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 73 | 362660 | R6_endpoint_implication | `not R(5, 7, 11) OR not R(7, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14) OR E_R6(5, 14)` |
| 74 | 362698 | R5_endpoint_implication | `E_R5(5, 14) OR not R(5, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 75 | 362705 | R5_endpoint_implication | `E_R5(4, 14) OR not R(4, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 76 | 375600 | necessary_blue_fan | `not R(11, 15, 23)` |
| 77 | 377800 | necessary_blue_fan | `not R(11, 15, 18)` |
| 78 | 384766 | packet | `not R(11, 13, 19) OR R(11, 12, 19) OR not R(11, 12, 13) OR R(12, 13, 19)` |
| 79 | 387319 | no_R7 | `not R(3, 4, 11) OR not R(4, 11, 13) OR not R(11, 13, 14) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 80 | 389081 | packet | `not R(11, 12, 20) OR R(11, 12, 19) OR R(11, 19, 20) OR R(12, 19, 20)` |
| 81 | 389121 | R5_endpoint_implication | `not R(11, 12, 19) OR E_R5(9, 19) OR not R(9, 10, 11) OR not R(10, 11, 12)` |
| 82 | 402415 | necessary_blue_fan | `not R(10, 15, 18)` |
| 83 | 415001 | packet | `R(5, 11, 15) OR not R(5, 10, 15) OR not R(10, 11, 15) OR R(5, 10, 11)` |
| 84 | 421688 | R6_endpoint_implication | `not R(8, 9, 16) OR not R(9, 16, 18) OR not R(5, 7, 8) OR not R(7, 8, 9) OR E_R6(5, 18)` |
| 85 | 423163 | necessary_blue_fan | `not R(9, 15, 18)` |
| 86 | 424739 | R6_endpoint_implication | `not R(7, 9, 14) OR not R(1, 6, 7) OR not R(6, 7, 9) OR not R(9, 14, 19) OR E_R6(1, 19)` |
| 87 | 424751 | R5_endpoint_implication | `not R(7, 9, 14) OR not R(5, 7, 9) OR not R(9, 14, 19) OR E_R5(5, 19)` |
| 88 | 424768 | packet | `not R(6, 14, 19) OR R(6, 9, 19) OR not R(9, 14, 19) OR not R(6, 9, 14)` |
| 89 | 424769 | packet | `R(6, 14, 19) OR not R(6, 9, 19) OR not R(9, 14, 19) OR not R(6, 9, 14)` |
| 90 | 424796 | packet | `R(6, 14, 19) OR R(6, 9, 19) OR not R(9, 14, 19) OR not R(6, 9, 14)` |
| 91 | 425005 | R5_endpoint_implication | `E_R5(1, 18) OR not R(1, 6, 9) OR not R(9, 14, 18) OR not R(6, 9, 14)` |
| 92 | 425395 | packet | `R(6, 9, 16) OR not R(6, 14, 16) OR not R(9, 14, 16) OR not R(6, 9, 14)` |
| 93 | 425425 | packet | `not R(5, 14, 16) OR not R(5, 9, 14) OR R(5, 9, 16) OR not R(9, 14, 16)` |
| 94 | 441817 | packet | `R(5, 14, 15) OR not R(5, 8, 14) OR not R(8, 14, 15) OR not R(5, 8, 15)` |
| 95 | 441818 | packet | `R(5, 14, 15) OR R(5, 8, 14) OR not R(8, 14, 15) OR not R(5, 8, 15)` |
| 96 | 445952 | packet | `R(10, 11, 15) OR not R(8, 10, 15) OR R(8, 10, 11) OR not R(8, 11, 15)` |
| 97 | 449222 | R5_endpoint_implication | `E_R5(5, 16) OR not R(8, 9, 16) OR not R(5, 7, 8) OR not R(7, 8, 9)` |
| 98 | 449229 | R5_endpoint_implication | `not R(4, 7, 8) OR not R(8, 9, 16) OR E_R5(4, 16) OR not R(7, 8, 9)` |
| 99 | 449325 | packet | `R(7, 8, 15) OR not R(7, 9, 15) OR not R(7, 8, 9) OR not R(8, 9, 15)` |
| 100 | 449338 | no_R7 | `not R(3, 6, 7) OR not R(1, 3, 6) OR not R(6, 7, 8) OR not R(7, 8, 9) OR not R(8, 9, 15)` |
| 101 | 449353 | R6_endpoint_implication | `not R(5, 7, 8) OR not R(1, 5, 7) OR E_R6(1, 15) OR not R(8, 9, 15) OR not R(7, 8, 9)` |
| 102 | 449402 | packet | `R(5, 9, 15) OR not R(5, 8, 15) OR not R(8, 9, 15) OR not R(5, 8, 9)` |
| 103 | 449456 | necessary_blue_fan | `not R(8, 9, 14)` |
| 104 | 460165 | no_R7 | `not R(3, 5, 7) OR not R(5, 7, 9) OR not R(7, 9, 15) OR not R(2, 3, 5) OR not R(1, 2, 3)` |
| 105 | 460177 | no_R7 | `not R(4, 7, 9) OR not R(3, 4, 7) OR not R(7, 9, 15) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 106 | 465299 | R6_endpoint_implication | `not R(3, 6, 14) OR not R(6, 14, 19) OR not R(2, 3, 6) OR not R(1, 2, 3) OR E_R6(1, 19)` |
| 107 | 465581 | no_R7 | `not R(4, 6, 14) OR not R(3, 4, 6) OR not R(6, 14, 15) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 108 | 469339 | packet | `not R(1, 9, 15) OR R(1, 6, 15) OR not R(1, 6, 9) OR not R(6, 9, 15)` |
| 109 | 469342 | packet | `R(1, 9, 15) OR R(1, 6, 15) OR not R(1, 6, 9) OR not R(6, 9, 15)` |
| 110 | 474380 | no_R7 | `not R(4, 5, 14) OR not R(5, 14, 15) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 111 | 476016 | no_R7 | `not R(4, 5, 11) OR not R(5, 11, 15) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 112 | 477235 | no_R7 | `not R(4, 5, 9) OR not R(5, 9, 15) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 113 | 478111 | no_R7 | `not R(4, 5, 8) OR not R(5, 8, 9) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 114 | 478808 | no_R7 | `not R(5, 6, 23) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 115 | 479033 | no_R7 | `not R(5, 6, 18) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 116 | 479156 | no_R7 | `not R(5, 6, 15) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 117 | 479195 | no_R7 | `not R(5, 6, 14) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 118 | 479375 | no_R7 | `not R(5, 6, 9) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 119 | 479440 | no_R7 | `not R(5, 6, 7) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 120 | 486361 | R6_endpoint_implication | `not R(4, 5, 15) OR E_R6(1, 15) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 121 | 486491 | R6_endpoint_implication | `not R(4, 5, 10) OR E_R6(1, 10) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 122 | 486557 | R6_endpoint_implication | `E_R6(1, 7) OR not R(4, 5, 7) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 123 | 486574 | packet | `R(3, 4, 6) OR not R(3, 5, 6) OR not R(3, 4, 5) OR not R(4, 5, 6)` |
| 124 | 486577 | R6_endpoint_implication | `E_R6(1, 6) OR not R(4, 5, 6) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 125 | 493148 | R5_endpoint_implication | `E_R5(1, 11) OR not R(3, 4, 11) OR not R(1, 2, 3) OR not R(2, 3, 4)` |
| 126 | 493161 | packet | `R(3, 10, 11) OR not R(3, 4, 11) OR R(3, 4, 10) OR R(4, 10, 11)` |
| 127 | 493165 | R5_endpoint_implication | `not R(3, 4, 10) OR E_R5(1, 10) OR not R(1, 2, 3) OR not R(2, 3, 4)` |
| 128 | 493232 | packet | `R(2, 3, 5) OR not R(2, 4, 5) OR not R(2, 3, 4) OR not R(3, 4, 5)` |
| 129 | 505773 | frozen_red_path | `R(1, 2, 3)` |
| 130 | 533972 | frozen_red_path | `R(2, 3, 4)` |
| 131 | 535872 | A_no_in_B4 | `R(2, 3, 6) OR R(3, 6, 7)` |
| 132 | 539424 | A_no_in_B4 | `R(2, 4, 5) OR R(4, 5, 8)` |
| 133 | 555782 | frozen_red_path | `R(3, 4, 5)` |
| 134 | 557377 | A_no_in_B4 | `R(3, 4, 7) OR R(4, 7, 8)` |
| 135 | 559212 | no_B6 | `R(3, 4, 11) OR R(4, 11, 12) OR R(11, 12, 19) OR R(12, 19, 21)` |
| 136 | 559261 | no_B6 | `R(4, 11, 13) OR R(3, 4, 11) OR R(11, 13, 19) OR R(13, 19, 21)` |
| 137 | 560567 | A_no_in_B4 | `R(3, 5, 6) OR R(5, 6, 15)` |
| 138 | 560658 | A_no_in_B4 | `R(5, 7, 8) OR R(3, 5, 7)` |
| 139 | 572412 | frozen_red_path | `R(4, 5, 6)` |
| 140 | 573249 | A_no_in_B4 | `R(4, 5, 7) OR R(5, 7, 9)` |
| 141 | 574133 | T_no_B5_endpoints | `R(5, 8, 15) OR R(4, 5, 8) OR R(8, 15, 16)` |
| 142 | 574849 | no_B6 | `R(5, 10, 15) OR R(4, 5, 10) OR R(10, 15, 18) OR R(15, 18, 19)` |
| 143 | 574976 | no_B6 | `R(5, 11, 12) OR R(4, 5, 11) OR R(11, 12, 20) OR R(12, 20, 21)` |
| 144 | 575505 | T_no_B5_endpoints | `R(5, 14, 16) OR R(4, 5, 14) OR R(14, 16, 17)` |
| 145 | 585003 | A_no_in_B4 | `R(6, 7, 9) OR R(5, 6, 7)` |
| 146 | 594090 | frozen_red_path | `R(6, 7, 8)` |
| 147 | 599582 | no_T_to_T_B4 | `R(6, 9, 15) OR R(9, 15, 18)` |
| 148 | 602403 | no_T_to_T_B4 | `R(6, 14, 15) OR R(14, 15, 18)` |
| 149 | 602439 | no_T_to_T_B4 | `R(6, 14, 16) OR R(14, 16, 17)` |
| 150 | 602824 | frozen_red_path | `R(7, 8, 9)` |
| 151 | 605901 | no_T_to_T_B4 | `R(7, 9, 15) OR R(9, 15, 18)` |
| 152 | 607293 | T_no_B5_endpoints | `R(7, 11, 12) OR R(11, 12, 19) OR R(12, 19, 20)` |
| 153 | 610231 | no_T_to_T_B4 | `R(9, 14, 16) OR R(8, 9, 14)` |
| 154 | 610282 | no_T_to_T_B4 | `R(9, 14, 18) OR R(8, 9, 14)` |
| 155 | 610298 | T_no_B5_endpoints | `R(9, 14, 19) OR R(14, 19, 20) OR R(8, 9, 14)` |
| 156 | 610318 | frozen_red_path | `R(8, 9, 15)` |
| 157 | 610406 | no_T_to_T_B4 | `R(8, 9, 16) OR R(9, 16, 17)` |
| 158 | 610428 | no_T_to_T_B4 | `R(9, 16, 18) OR R(8, 9, 16)` |
| 159 | 611393 | no_T_to_T_B4 | `R(8, 10, 15) OR R(10, 15, 18)` |
| 160 | 612126 | no_T_to_T_B4 | `R(8, 11, 15) OR R(11, 15, 18)` |
| 161 | 613191 | no_T_to_T_B4 | `R(8, 14, 15) OR R(14, 15, 18)` |
| 162 | 613612 | frozen_red_path | `R(9, 10, 11)` |
| 163 | 616690 | frozen_red_path | `R(10, 11, 12)` |
| 164 | 618053 | frozen_red_path | `R(11, 12, 13)` |
| 165 | 618406 | A_no_in_B4 | `R(11, 13, 14) OR R(13, 14, 15)` |
| 166 | 618884 | frozen_red_path | `R(12, 13, 14)` |
| 167 | 619747 | frozen_red_path | `R(15, 16, 17)` |
| 168 | 619930 | frozen_red_path | `R(16, 17, 18)` |
| 169 | 619956 | B_no_out_B4 | `R(17, 19, 20) OR R(16, 17, 19)` |
| 170 | 619963 | B_no_out_B4 | `R(17, 19, 21) OR R(16, 17, 19)` |
| 171 | 620063 | frozen_red_path | `R(18, 19, 20)` |
| 172 | 620080 | frozen_red_path | `R(19, 20, 21)` |
| 173 | 620081 | frozen_red_path | `R(20, 21, 22)` |
| 174 | 620082 | frozen_red_path | `R(21, 22, 23)` |
