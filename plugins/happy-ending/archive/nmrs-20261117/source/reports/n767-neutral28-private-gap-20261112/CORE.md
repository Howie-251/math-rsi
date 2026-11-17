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
| 14 | 1743 | weak_R6_B3 | `not E_R6(1, 10) OR R(1, 9, 10)` |
| 15 | 1761 | weak_R6_B3 | `R(1, 6, 7) OR not E_R6(1, 7)` |
| 16 | 1763 | weak_R6_B3 | `R(1, 3, 6) OR not E_R6(1, 6)` |
| 17 | 1982 | weak_R5_B4 | `not E_R5(13, 23) OR R(13, 14, 15) OR R(14, 15, 23)` |
| 18 | 3049 | weak_R5_B4 | `not E_R5(9, 19) OR R(15, 18, 19) OR R(9, 15, 18)` |
| 19 | 5295 | weak_R5_B4 | `not E_R5(5, 19) OR R(5, 6, 18) OR R(6, 18, 19)` |
| 20 | 5491 | weak_R5_B4 | `not E_R5(5, 16) OR R(6, 15, 16) OR R(5, 6, 15)` |
| 21 | 5566 | weak_R5_B4 | `R(6, 9, 14) OR not E_R5(5, 14) OR R(5, 6, 9)` |
| 22 | 5572 | weak_R5_B4 | `R(7, 9, 14) OR R(5, 7, 9) OR not E_R5(5, 14)` |
| 23 | 5577 | weak_R5_B4 | `R(5, 8, 9) OR not E_R5(5, 14) OR R(8, 9, 14)` |
| 24 | 6400 | weak_R5_B4 | `R(5, 9, 16) OR not E_R5(4, 16) OR R(4, 5, 9)` |
| 25 | 6406 | weak_R5_B4 | `R(4, 5, 15) OR R(5, 15, 16) OR not E_R5(4, 16)` |
| 26 | 6500 | weak_R5_B4 | `not E_R5(4, 14) OR R(5, 9, 14) OR R(4, 5, 9)` |
| 27 | 6513 | weak_R5_B4 | `R(4, 7, 9) OR not E_R5(4, 14) OR R(7, 9, 14)` |
| 28 | 10529 | weak_R5_B4 | `not E_R5(1, 11) OR R(1, 5, 7) OR R(5, 7, 11)` |
| 29 | 10567 | weak_R5_B4 | `R(1, 6, 9) OR not E_R5(1, 10) OR R(6, 9, 10)` |
| 30 | 44281 | no_R7 | `not R(15, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 31 | 44290 | no_R7 | `not R(6, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 32 | 44295 | no_R7 | `not R(1, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 33 | 44313 | R6_endpoint_implication | `not R(17, 19, 20) OR E_R6(17, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR not R(21, 22, 23)` |
| 34 | 44358 | R6_endpoint_implication | `not R(14, 19, 20) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR E_R6(14, 23)` |
| 35 | 44371 | R6_endpoint_implication | `not R(13, 19, 20) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR E_R6(13, 23)` |
| 36 | 44383 | R6_endpoint_implication | `not R(12, 19, 20) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR E_R6(12, 23)` |
| 37 | 44394 | R6_endpoint_implication | `not R(11, 19, 20) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR E_R6(11, 23)` |
| 38 | 45146 | R5_endpoint_implication | `not R(13, 20, 21) OR E_R5(13, 23) OR not R(20, 21, 22) OR not R(21, 22, 23)` |
| 39 | 45608 | no_R7 | `not R(19, 21, 22) OR not R(17, 19, 21) OR not R(16, 17, 19) OR not R(21, 22, 23) OR not R(15, 16, 17)` |
| 40 | 60922 | packet | `R(19, 20, 22) OR not R(19, 21, 22) OR not R(19, 20, 21) OR not R(20, 21, 22)` |
| 41 | 60923 | packet | `not R(19, 20, 22) OR R(19, 21, 22) OR not R(19, 20, 21) OR not R(20, 21, 22)` |
| 42 | 61921 | packet | `R(19, 20, 22) OR R(19, 21, 22) OR not R(19, 20, 21) OR not R(20, 21, 22)` |
| 43 | 89876 | packet | `not R(13, 19, 21) OR R(13, 20, 21) OR not R(19, 20, 21) OR R(13, 19, 20)` |
| 44 | 150326 | no_R7 | `not R(17, 18, 23) OR not R(6, 15, 16) OR not R(1, 6, 15) OR not R(16, 17, 18) OR not R(15, 16, 17)` |
| 45 | 150332 | R6_endpoint_implication | `not R(5, 15, 16) OR not R(17, 18, 23) OR not R(15, 16, 17) OR not R(16, 17, 18) OR E_R6(5, 23)` |
| 46 | 150708 | no_R7 | `not R(9, 16, 17) OR not R(17, 18, 23) OR not R(6, 9, 16) OR not R(1, 6, 9) OR not R(16, 17, 18)` |
| 47 | 150714 | R6_endpoint_implication | `not R(5, 9, 16) OR not R(9, 16, 17) OR not R(17, 18, 23) OR not R(16, 17, 18) OR E_R6(5, 23)` |
| 48 | 202123 | R6_endpoint_implication | `not R(6, 15, 16) OR not R(1, 6, 15) OR not R(16, 17, 19) OR not R(15, 16, 17) OR E_R6(1, 19)` |
| 49 | 202135 | R5_endpoint_implication | `not R(5, 15, 16) OR not R(16, 17, 19) OR not R(15, 16, 17) OR E_R5(5, 19)` |
| 50 | 203465 | R6_endpoint_implication | `not R(9, 16, 17) OR not R(1, 6, 9) OR not R(16, 17, 19) OR not R(6, 9, 16) OR E_R6(1, 19)` |
| 51 | 203477 | R5_endpoint_implication | `not R(9, 16, 17) OR not R(5, 9, 16) OR not R(16, 17, 19) OR E_R5(5, 19)` |
| 52 | 204074 | no_R7 | `not R(8, 15, 16) OR not R(7, 8, 15) OR not R(15, 16, 17) OR not R(16, 17, 18) OR not R(6, 7, 8)` |
| 53 | 204442 | no_R7 | `not R(14, 16, 17) OR not R(1, 6, 9) OR not R(9, 14, 16) OR not R(16, 17, 18) OR not R(6, 9, 14)` |
| 54 | 204448 | R6_endpoint_implication | `not R(14, 16, 17) OR not R(5, 9, 14) OR not R(9, 14, 16) OR not R(16, 17, 18) OR E_R6(5, 18)` |
| 55 | 205433 | R6_endpoint_implication | `not R(8, 9, 16) OR not R(9, 16, 17) OR not R(16, 17, 18) OR not R(5, 8, 9) OR E_R6(5, 18)` |
| 56 | 281444 | necessary_blue_fan | `not R(14, 15, 23)` |
| 57 | 287224 | necessary_blue_fan | `not R(14, 15, 18)` |
| 58 | 314704 | necessary_blue_fan | `not R(13, 15, 23)` |
| 59 | 328307 | no_R7 | `not R(13, 14, 15) OR not R(12, 13, 14) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 60 | 332916 | packet | `not R(12, 20, 21) OR R(13, 20, 21) OR R(12, 13, 21) OR R(12, 13, 20)` |
| 61 | 334794 | packet | `not R(12, 19, 21) OR R(13, 19, 21) OR R(12, 13, 21) OR R(12, 13, 19)` |
| 62 | 346589 | necessary_blue_fan | `not R(12, 15, 23)` |
| 63 | 358269 | a4_R6_terminal_cut | `not R(12, 13, 21) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 64 | 358882 | a4_R6_terminal_cut | `not R(12, 13, 20) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 65 | 359494 | a4_R6_terminal_cut | `not R(12, 13, 19) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 66 | 362539 | no_R7 | `not R(7, 9, 10) OR not R(12, 13, 14) OR not R(10, 11, 12) OR not R(9, 10, 11) OR not R(11, 12, 13)` |
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
| 91 | 425395 | packet | `R(6, 9, 16) OR not R(6, 14, 16) OR not R(9, 14, 16) OR not R(6, 9, 14)` |
| 92 | 425425 | packet | `not R(5, 14, 16) OR not R(5, 9, 14) OR R(5, 9, 16) OR not R(9, 14, 16)` |
| 93 | 441817 | packet | `R(5, 14, 15) OR not R(5, 8, 14) OR not R(8, 14, 15) OR not R(5, 8, 15)` |
| 94 | 441818 | packet | `R(5, 14, 15) OR R(5, 8, 14) OR not R(8, 14, 15) OR not R(5, 8, 15)` |
| 95 | 445952 | packet | `R(10, 11, 15) OR not R(8, 10, 15) OR R(8, 10, 11) OR not R(8, 11, 15)` |
| 96 | 449222 | R5_endpoint_implication | `E_R5(5, 16) OR not R(8, 9, 16) OR not R(5, 7, 8) OR not R(7, 8, 9)` |
| 97 | 449229 | R5_endpoint_implication | `not R(4, 7, 8) OR not R(8, 9, 16) OR E_R5(4, 16) OR not R(7, 8, 9)` |
| 98 | 449325 | packet | `R(7, 8, 15) OR not R(7, 9, 15) OR not R(7, 8, 9) OR not R(8, 9, 15)` |
| 99 | 449338 | no_R7 | `not R(3, 6, 7) OR not R(1, 3, 6) OR not R(6, 7, 8) OR not R(7, 8, 9) OR not R(8, 9, 15)` |
| 100 | 449353 | R6_endpoint_implication | `not R(5, 7, 8) OR not R(1, 5, 7) OR E_R6(1, 15) OR not R(8, 9, 15) OR not R(7, 8, 9)` |
| 101 | 449402 | packet | `R(5, 9, 15) OR not R(5, 8, 15) OR not R(8, 9, 15) OR not R(5, 8, 9)` |
| 102 | 449456 | necessary_blue_fan | `not R(8, 9, 14)` |
| 103 | 460165 | no_R7 | `not R(3, 5, 7) OR not R(5, 7, 9) OR not R(7, 9, 15) OR not R(2, 3, 5) OR not R(1, 2, 3)` |
| 104 | 460177 | no_R7 | `not R(4, 7, 9) OR not R(3, 4, 7) OR not R(7, 9, 15) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 105 | 465299 | R6_endpoint_implication | `not R(3, 6, 14) OR not R(6, 14, 19) OR not R(2, 3, 6) OR not R(1, 2, 3) OR E_R6(1, 19)` |
| 106 | 465581 | no_R7 | `not R(4, 6, 14) OR not R(3, 4, 6) OR not R(6, 14, 15) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 107 | 474380 | no_R7 | `not R(4, 5, 14) OR not R(5, 14, 15) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 108 | 476016 | no_R7 | `not R(4, 5, 11) OR not R(5, 11, 15) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 109 | 477235 | no_R7 | `not R(4, 5, 9) OR not R(5, 9, 15) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 110 | 478111 | no_R7 | `not R(4, 5, 8) OR not R(5, 8, 9) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 111 | 478808 | no_R7 | `not R(5, 6, 23) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 112 | 479033 | no_R7 | `not R(5, 6, 18) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 113 | 479156 | no_R7 | `not R(5, 6, 15) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 114 | 479195 | no_R7 | `not R(5, 6, 14) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 115 | 479375 | no_R7 | `not R(5, 6, 9) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 116 | 479440 | no_R7 | `not R(5, 6, 7) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 117 | 486361 | R6_endpoint_implication | `not R(4, 5, 15) OR E_R6(1, 15) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 118 | 486491 | R6_endpoint_implication | `not R(4, 5, 10) OR E_R6(1, 10) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 119 | 486557 | R6_endpoint_implication | `E_R6(1, 7) OR not R(4, 5, 7) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 120 | 486574 | packet | `R(3, 4, 6) OR not R(3, 5, 6) OR not R(3, 4, 5) OR not R(4, 5, 6)` |
| 121 | 486577 | R6_endpoint_implication | `E_R6(1, 6) OR not R(4, 5, 6) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 122 | 493148 | R5_endpoint_implication | `E_R5(1, 11) OR not R(3, 4, 11) OR not R(1, 2, 3) OR not R(2, 3, 4)` |
| 123 | 493161 | packet | `R(3, 10, 11) OR not R(3, 4, 11) OR R(3, 4, 10) OR R(4, 10, 11)` |
| 124 | 493165 | R5_endpoint_implication | `not R(3, 4, 10) OR E_R5(1, 10) OR not R(1, 2, 3) OR not R(2, 3, 4)` |
| 125 | 493232 | packet | `R(2, 3, 5) OR not R(2, 4, 5) OR not R(2, 3, 4) OR not R(3, 4, 5)` |
| 126 | 505773 | frozen_red_path | `R(1, 2, 3)` |
| 127 | 534028 | frozen_red_path | `R(2, 3, 4)` |
| 128 | 535937 | A_no_in_B4 | `R(2, 3, 6) OR R(3, 6, 7)` |
| 129 | 539497 | A_no_in_B4 | `R(2, 4, 5) OR R(4, 5, 8)` |
| 130 | 555873 | frozen_red_path | `R(3, 4, 5)` |
| 131 | 557475 | A_no_in_B4 | `R(3, 4, 7) OR R(4, 7, 8)` |
| 132 | 559313 | no_B6 | `R(3, 4, 11) OR R(4, 11, 12) OR R(11, 12, 19) OR R(12, 19, 21)` |
| 133 | 559362 | no_B6 | `R(4, 11, 13) OR R(3, 4, 11) OR R(11, 13, 19) OR R(13, 19, 21)` |
| 134 | 560671 | A_no_in_B4 | `R(3, 5, 6) OR R(5, 6, 15)` |
| 135 | 560762 | A_no_in_B4 | `R(5, 7, 8) OR R(3, 5, 7)` |
| 136 | 572523 | frozen_red_path | `R(4, 5, 6)` |
| 137 | 573365 | private_x2_no_in_B5 | `R(4, 5, 7) OR R(5, 7, 9) OR R(7, 9, 10)` |
| 138 | 574250 | T_no_B5_endpoints | `R(5, 8, 15) OR R(4, 5, 8) OR R(8, 15, 16)` |
| 139 | 574966 | no_B6 | `R(5, 10, 15) OR R(4, 5, 10) OR R(10, 15, 18) OR R(15, 18, 19)` |
| 140 | 575093 | no_B6 | `R(5, 11, 12) OR R(4, 5, 11) OR R(11, 12, 20) OR R(12, 20, 21)` |
| 141 | 575622 | T_no_B5_endpoints | `R(5, 14, 16) OR R(4, 5, 14) OR R(14, 16, 17)` |
| 142 | 585126 | private_x2_no_in_B5 | `R(6, 7, 9) OR R(5, 6, 7) OR R(7, 9, 10)` |
| 143 | 594215 | frozen_red_path | `R(6, 7, 8)` |
| 144 | 602528 | no_T_to_T_B4 | `R(6, 14, 15) OR R(14, 15, 18)` |
| 145 | 602564 | no_T_to_T_B4 | `R(6, 14, 16) OR R(14, 16, 17)` |
| 146 | 602949 | frozen_red_path | `R(7, 8, 9)` |
| 147 | 606026 | no_T_to_T_B4 | `R(7, 9, 15) OR R(9, 15, 18)` |
| 148 | 607418 | T_no_B5_endpoints | `R(7, 11, 12) OR R(11, 12, 19) OR R(12, 19, 20)` |
| 149 | 610356 | no_T_to_T_B4 | `R(9, 14, 16) OR R(8, 9, 14)` |
| 150 | 610423 | T_no_B5_endpoints | `R(9, 14, 19) OR R(14, 19, 20) OR R(8, 9, 14)` |
| 151 | 610443 | frozen_red_path | `R(8, 9, 15)` |
| 152 | 610531 | no_T_to_T_B4 | `R(8, 9, 16) OR R(9, 16, 17)` |
| 153 | 610553 | no_T_to_T_B4 | `R(9, 16, 18) OR R(8, 9, 16)` |
| 154 | 611518 | no_T_to_T_B4 | `R(8, 10, 15) OR R(10, 15, 18)` |
| 155 | 612251 | no_T_to_T_B4 | `R(8, 11, 15) OR R(11, 15, 18)` |
| 156 | 613316 | no_T_to_T_B4 | `R(8, 14, 15) OR R(14, 15, 18)` |
| 157 | 613737 | frozen_red_path | `R(9, 10, 11)` |
| 158 | 616815 | frozen_red_path | `R(10, 11, 12)` |
| 159 | 618178 | frozen_red_path | `R(11, 12, 13)` |
| 160 | 618531 | A_no_in_B4 | `R(11, 13, 14) OR R(13, 14, 15)` |
| 161 | 619009 | frozen_red_path | `R(12, 13, 14)` |
| 162 | 619872 | frozen_red_path | `R(15, 16, 17)` |
| 163 | 620055 | frozen_red_path | `R(16, 17, 18)` |
| 164 | 620081 | B_no_out_B4 | `R(17, 19, 20) OR R(16, 17, 19)` |
| 165 | 620088 | B_no_out_B4 | `R(17, 19, 21) OR R(16, 17, 19)` |
| 166 | 620188 | frozen_red_path | `R(18, 19, 20)` |
| 167 | 620205 | frozen_red_path | `R(19, 20, 21)` |
| 168 | 620206 | frozen_red_path | `R(20, 21, 22)` |
| 169 | 620207 | frozen_red_path | `R(21, 22, 23)` |
