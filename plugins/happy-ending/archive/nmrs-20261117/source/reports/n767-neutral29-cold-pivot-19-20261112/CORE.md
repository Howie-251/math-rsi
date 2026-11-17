# Independently checked trimmed core

These are clauses of the original literal nineteen-point model; this is not a new mathematical extraction assumption. Both the original proof and the trimmed proof were checked.

| Core | Original | Predicate | Physical literals (disjunction) |
|---:|---:|---|---|
| 1 | 21 | weak_R6_B3 | `not E_R6(13, 19) OR R(13, 14, 19)` |
| 2 | 121 | weak_R6_B3 | `not E_R6(9, 19) OR R(9, 10, 19)` |
| 3 | 336 | weak_R6_B3 | `not E_R6(6, 15) OR R(6, 14, 15)` |
| 4 | 365 | weak_R6_B3 | `not E_R6(5, 19) OR R(5, 6, 19)` |
| 5 | 420 | weak_R6_B3 | `not E_R6(5, 14) OR R(5, 6, 14)` |
| 6 | 891 | weak_R6_B3 | `not E_R6(1, 15) OR R(1, 14, 15)` |
| 7 | 933 | weak_R6_B3 | `not E_R6(1, 11) OR R(1, 10, 11)` |
| 8 | 959 | weak_R6_B3 | `not E_R6(1, 7) OR R(1, 6, 7)` |
| 9 | 1283 | weak_R5_B4 | `R(9, 10, 14) OR not E_R5(9, 15) OR R(10, 14, 15)` |
| 10 | 2318 | weak_R5_B4 | `R(6, 10, 11) OR not E_R5(5, 11) OR R(5, 6, 10)` |
| 11 | 16474 | packet | `R(16, 17, 19) OR not R(16, 18, 19) OR not R(16, 17, 18) OR not R(17, 18, 19)` |
| 12 | 16475 | packet | `not R(16, 17, 19) OR R(16, 18, 19) OR not R(16, 17, 18) OR not R(17, 18, 19)` |
| 13 | 16480 | no_R7 | `not R(10, 14, 15) OR not R(17, 18, 19) OR not R(15, 16, 17) OR not R(14, 15, 16) OR not R(16, 17, 18)` |
| 14 | 16484 | no_R7 | `not R(6, 14, 15) OR not R(17, 18, 19) OR not R(15, 16, 17) OR not R(14, 15, 16) OR not R(16, 17, 18)` |
| 15 | 16489 | no_R7 | `not R(1, 14, 15) OR not R(17, 18, 19) OR not R(15, 16, 17) OR not R(14, 15, 16) OR not R(16, 17, 18)` |
| 16 | 16503 | R6_endpoint_implication | `not R(13, 15, 16) OR E_R6(13, 19) OR not R(15, 16, 17) OR not R(16, 17, 18) OR not R(17, 18, 19)` |
| 17 | 17058 | packet | `R(16, 17, 19) OR R(16, 18, 19) OR not R(16, 17, 18) OR not R(17, 18, 19)` |
| 18 | 17158 | late_R6_no_T_second | `not R(15, 17, 18) OR not R(13, 15, 17) OR not R(12, 13, 15) OR not R(17, 18, 19)` |
| 19 | 19072 | packet | `R(15, 16, 19) OR not R(15, 18, 19) OR not R(16, 18, 19) OR not R(15, 16, 18)` |
| 20 | 19073 | packet | `R(15, 18, 19) OR not R(15, 16, 19) OR not R(16, 18, 19) OR not R(15, 16, 18)` |
| 21 | 19550 | packet | `R(15, 18, 19) OR R(15, 16, 19) OR not R(16, 18, 19) OR not R(15, 16, 18)` |
| 22 | 23094 | packet | `R(15, 16, 18) OR not R(15, 17, 18) OR not R(15, 16, 17) OR not R(16, 17, 18)` |
| 23 | 23095 | packet | `not R(15, 16, 18) OR R(15, 17, 18) OR not R(15, 16, 17) OR not R(16, 17, 18)` |
| 24 | 23572 | packet | `R(15, 16, 18) OR R(15, 17, 18) OR not R(15, 16, 17) OR not R(16, 17, 18)` |
| 25 | 25496 | late_R6_no_T_second | `not R(15, 18, 19) OR not R(13, 15, 18) OR not R(12, 13, 15) OR not R(11, 12, 13)` |
| 26 | 44649 | no_R7 | `not R(13, 14, 15) OR not R(14, 15, 16) OR not R(12, 13, 14) OR not R(11, 12, 13) OR not R(10, 11, 12)` |
| 27 | 54276 | no_R7 | `not R(13, 14, 19) OR not R(6, 10, 11) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(12, 13, 14)` |
| 28 | 54281 | no_R7 | `not R(1, 10, 11) OR not R(13, 14, 19) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(12, 13, 14)` |
| 29 | 54291 | R6_endpoint_implication | `not R(9, 11, 12) OR E_R6(9, 19) OR not R(13, 14, 19) OR not R(12, 13, 14) OR not R(11, 12, 13)` |
| 30 | 70151 | R6_endpoint_implication | `not R(6, 10, 11) OR not R(12, 13, 15) OR not R(10, 11, 12) OR not R(11, 12, 13) OR E_R6(6, 15)` |
| 31 | 70166 | R6_endpoint_implication | `not R(1, 10, 11) OR not R(12, 13, 15) OR not R(10, 11, 12) OR not R(11, 12, 13) OR E_R6(1, 15)` |
| 32 | 70204 | R5_endpoint_implication | `E_R5(9, 15) OR not R(9, 11, 12) OR not R(12, 13, 15) OR not R(11, 12, 13)` |
| 33 | 70745 | no_R7 | `not R(7, 10, 11) OR not R(6, 7, 10) OR not R(10, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 34 | 80169 | no_R7 | `not R(8, 9, 11) OR not R(9, 11, 13) OR not R(11, 13, 14) OR not R(7, 8, 9) OR not R(6, 7, 8)` |
| 35 | 101701 | no_R7 | `not R(9, 10, 19) OR not R(1, 6, 7) OR not R(7, 8, 9) OR not R(6, 7, 8) OR not R(8, 9, 10)` |
| 36 | 101707 | R6_endpoint_implication | `not R(5, 7, 8) OR not R(9, 10, 19) OR not R(7, 8, 9) OR not R(8, 9, 10) OR E_R6(5, 19)` |
| 37 | 102701 | no_R7 | `not R(9, 10, 14) OR not R(1, 6, 7) OR not R(7, 8, 9) OR not R(6, 7, 8) OR not R(8, 9, 10)` |
| 38 | 102707 | R6_endpoint_implication | `not R(9, 10, 14) OR not R(5, 7, 8) OR not R(7, 8, 9) OR not R(8, 9, 10) OR E_R6(5, 14)` |
| 39 | 110830 | R6_endpoint_implication | `not R(1, 6, 7) OR not R(8, 9, 11) OR E_R6(1, 11) OR not R(7, 8, 9) OR not R(6, 7, 8)` |
| 40 | 110842 | R5_endpoint_implication | `not R(5, 7, 8) OR not R(8, 9, 11) OR E_R5(5, 11) OR not R(7, 8, 9)` |
| 41 | 126020 | no_R7 | `not R(5, 7, 10) OR not R(4, 5, 7) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 42 | 126131 | no_R7 | `not R(5, 6, 19) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 43 | 126336 | no_R7 | `not R(5, 6, 14) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 44 | 126482 | no_R7 | `not R(5, 6, 10) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 45 | 126589 | early_R6_no_T_penultimate | `not R(5, 6, 7) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4)` |
| 46 | 130406 | R6_endpoint_implication | `E_R6(1, 7) OR not R(4, 5, 7) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 47 | 140666 | frozen_red_path_or_redundant_red_fan | `R(1, 2, 3)` |
| 48 | 150030 | frozen_red_path_or_redundant_red_fan | `R(2, 3, 4)` |
| 49 | 156770 | frozen_red_path_or_redundant_red_fan | `R(3, 4, 5)` |
| 50 | 161505 | frozen_red_path_or_redundant_red_fan | `R(4, 5, 6)` |
| 51 | 161824 | A_no_in_B4 | `R(4, 5, 7) OR R(5, 7, 8)` |
| 52 | 161938 | T_no_B5_endpoints | `R(5, 7, 10) OR R(4, 5, 7) OR R(7, 10, 11)` |
| 53 | 164852 | A_no_in_B4 | `R(6, 7, 10) OR R(5, 6, 7)` |
| 54 | 166877 | frozen_red_path_or_redundant_red_fan | `R(6, 7, 8)` |
| 55 | 168936 | frozen_red_path_or_redundant_red_fan | `R(7, 8, 9)` |
| 56 | 170259 | frozen_red_path_or_redundant_red_fan | `R(8, 9, 10)` |
| 57 | 170384 | no_T_to_T_B4 | `R(8, 9, 11) OR R(9, 11, 12)` |
| 58 | 170413 | no_T_to_T_B4 | `R(9, 11, 13) OR R(8, 9, 11)` |
| 59 | 171544 | frozen_red_path_or_redundant_red_fan | `R(10, 11, 12)` |
| 60 | 171881 | frozen_red_path_or_redundant_red_fan | `R(11, 12, 13)` |
| 61 | 171973 | B_no_out_B4 | `R(11, 13, 14) OR R(13, 14, 15)` |
| 62 | 172064 | frozen_red_path_or_redundant_red_fan | `R(12, 13, 14)` |
| 63 | 172090 | B_no_out_B4 | `R(13, 15, 16) OR R(12, 13, 15)` |
| 64 | 172097 | B_no_out_B4 | `R(13, 15, 17) OR R(12, 13, 15)` |
| 65 | 172197 | frozen_red_path_or_redundant_red_fan | `R(14, 15, 16)` |
| 66 | 172217 | frozen_red_path_or_redundant_red_fan | `R(15, 16, 17)` |
| 67 | 172218 | frozen_red_path_or_redundant_red_fan | `R(16, 17, 18)` |
| 68 | 172219 | frozen_red_path_or_redundant_red_fan | `R(17, 18, 19)` |
