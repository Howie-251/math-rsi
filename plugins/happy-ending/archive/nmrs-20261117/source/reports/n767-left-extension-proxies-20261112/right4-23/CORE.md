# Independently checked trimmed core

These are clauses of the original literal twenty-three-point private-gap model; this is not a new mathematical extraction assumption. Both the original proof and the trimmed proof were checked.

| Core | Original | Predicate | Physical literals (disjunction) |
|---:|---:|---|---|
| 1 | 1015 | left_extension_no_B4_to_S | `R(9, 16, 17) OR R(7, 9, 16) OR not Src_R6(17)` |
| 2 | 1057 | left_extension_no_B4_to_S | `R(6, 9, 15) OR not Src_R6(16) OR R(9, 15, 16)` |
| 3 | 1072 | left_extension_no_B4_to_S | `R(6, 14, 15) OR not Src_R6(16) OR R(14, 15, 16)` |
| 4 | 1085 | left_extension_no_B4_to_S | `R(7, 9, 15) OR not Src_R6(16) OR R(9, 15, 16)` |
| 5 | 1261 | weak_R6_B3 | `not E_R6(17, 23) OR R(17, 18, 23)` |
| 6 | 1325 | weak_R6_B3 | `not E_R6(14, 23) OR R(14, 15, 23)` |
| 7 | 1362 | weak_R6_B3 | `not E_R6(13, 23) OR R(13, 15, 23)` |
| 8 | 1408 | weak_R6_B3 | `not E_R6(12, 23) OR R(12, 15, 23)` |
| 9 | 1464 | weak_R6_B3 | `not E_R6(11, 23) OR R(11, 15, 23)` |
| 10 | 1786 | weak_R6_B3 | `not E_R6(8, 14) OR R(8, 9, 14)` |
| 11 | 2057 | weak_R6_B3 | `not E_R6(5, 23) OR R(5, 6, 23)` |
| 12 | 2132 | weak_R6_B3 | `not E_R6(5, 18) OR R(5, 6, 18)` |
| 13 | 2174 | weak_R6_B3 | `not E_R6(5, 14) OR R(5, 6, 14)` |
| 14 | 2337 | weak_R6_B3 | `not E_R6(4, 14) OR R(4, 6, 14)` |
| 15 | 2518 | weak_R6_B3 | `not E_R6(3, 14) OR R(3, 6, 14)` |
| 16 | 2875 | weak_R6_B3 | `not E_R6(1, 19) OR R(1, 18, 19)` |
| 17 | 2925 | weak_R6_B3 | `not E_R6(1, 15) OR R(1, 6, 15)` |
| 18 | 2928 | weak_R6_B3 | `R(1, 9, 15) OR not E_R6(1, 15)` |
| 19 | 2983 | weak_R6_B3 | `not E_R6(1, 10) OR R(1, 9, 10)` |
| 20 | 3001 | weak_R6_B3 | `R(1, 6, 7) OR not E_R6(1, 7)` |
| 21 | 3222 | weak_R5_B4 | `not E_R5(13, 23) OR R(13, 14, 15) OR R(14, 15, 23)` |
| 22 | 4289 | weak_R5_B4 | `not E_R5(9, 19) OR R(15, 18, 19) OR R(9, 15, 18)` |
| 23 | 6535 | weak_R5_B4 | `not E_R5(5, 19) OR R(5, 6, 18) OR R(6, 18, 19)` |
| 24 | 6731 | weak_R5_B4 | `not E_R5(5, 16) OR R(6, 15, 16) OR R(5, 6, 15)` |
| 25 | 6806 | weak_R5_B4 | `R(6, 9, 14) OR not E_R5(5, 14) OR R(5, 6, 9)` |
| 26 | 6812 | weak_R5_B4 | `R(7, 9, 14) OR R(5, 7, 9) OR not E_R5(5, 14)` |
| 27 | 6817 | weak_R5_B4 | `R(5, 8, 9) OR not E_R5(5, 14) OR R(8, 9, 14)` |
| 28 | 7646 | weak_R5_B4 | `not E_R5(4, 16) OR R(4, 5, 15) OR R(5, 15, 16)` |
| 29 | 7740 | weak_R5_B4 | `not E_R5(4, 14) OR R(5, 9, 14) OR R(4, 5, 9)` |
| 30 | 7753 | weak_R5_B4 | `R(4, 7, 9) OR not E_R5(4, 14) OR R(7, 9, 14)` |
| 31 | 11769 | weak_R5_B4 | `not E_R5(1, 11) OR R(1, 5, 7) OR R(5, 7, 11)` |
| 32 | 11807 | weak_R5_B4 | `R(1, 6, 9) OR not E_R5(1, 10) OR R(6, 9, 10)` |
| 33 | 45521 | no_R7 | `not R(15, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 34 | 45530 | no_R7 | `not R(6, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 35 | 45535 | no_R7 | `not R(1, 18, 19) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(18, 19, 20) OR not R(20, 21, 22)` |
| 36 | 45554 | R6_endpoint_implication | `not R(17, 19, 20) OR E_R6(17, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR not R(21, 22, 23)` |
| 37 | 45602 | R6_endpoint_implication | `not R(14, 19, 20) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR E_R6(14, 23)` |
| 38 | 45616 | R6_endpoint_implication | `not R(13, 19, 20) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR E_R6(13, 23)` |
| 39 | 45629 | R6_endpoint_implication | `not R(12, 19, 20) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR E_R6(12, 23)` |
| 40 | 45641 | R6_endpoint_implication | `not R(11, 19, 20) OR not R(21, 22, 23) OR not R(19, 20, 21) OR not R(20, 21, 22) OR E_R6(11, 23)` |
| 41 | 46491 | R5_endpoint_implication | `not R(13, 20, 21) OR E_R5(13, 23) OR not R(20, 21, 22) OR not R(21, 22, 23)` |
| 42 | 47036 | no_R7 | `not R(19, 21, 22) OR not R(17, 19, 21) OR not R(16, 17, 19) OR not R(21, 22, 23) OR not R(15, 16, 17)` |
| 43 | 65240 | packet | `R(19, 20, 22) OR not R(19, 21, 22) OR not R(19, 20, 21) OR not R(20, 21, 22)` |
| 44 | 65241 | packet | `not R(19, 20, 22) OR R(19, 21, 22) OR not R(19, 20, 21) OR not R(20, 21, 22)` |
| 45 | 66392 | packet | `R(19, 20, 22) OR R(19, 21, 22) OR not R(19, 20, 21) OR not R(20, 21, 22)` |
| 46 | 99773 | packet | `not R(13, 19, 21) OR R(13, 20, 21) OR not R(19, 20, 21) OR R(13, 19, 20)` |
| 47 | 172917 | no_R7 | `not R(17, 18, 23) OR not R(6, 15, 16) OR not R(1, 6, 15) OR not R(16, 17, 18) OR not R(15, 16, 17)` |
| 48 | 172924 | R6_endpoint_implication | `not R(5, 15, 16) OR not R(17, 18, 23) OR not R(15, 16, 17) OR not R(16, 17, 18) OR E_R6(5, 23)` |
| 49 | 173350 | no_R7 | `not R(9, 16, 17) OR not R(7, 9, 16) OR not R(17, 18, 23) OR not R(16, 17, 18) OR not R(6, 7, 9)` |
| 50 | 173362 | no_R7 | `not R(9, 16, 17) OR not R(1, 6, 9) OR not R(17, 18, 23) OR not R(6, 9, 16) OR not R(16, 17, 18)` |
| 51 | 173369 | R6_endpoint_implication | `not R(9, 16, 17) OR not R(5, 9, 16) OR not R(17, 18, 23) OR not R(16, 17, 18) OR E_R6(5, 23)` |
| 52 | 236231 | R6_endpoint_implication | `not R(6, 15, 16) OR not R(1, 6, 15) OR not R(16, 17, 19) OR not R(15, 16, 17) OR E_R6(1, 19)` |
| 53 | 236248 | R5_endpoint_implication | `not R(5, 15, 16) OR not R(16, 17, 19) OR not R(15, 16, 17) OR E_R5(5, 19)` |
| 54 | 237881 | R6_endpoint_implication | `not R(1, 6, 9) OR not R(9, 16, 17) OR not R(16, 17, 19) OR not R(6, 9, 16) OR E_R6(1, 19)` |
| 55 | 237898 | R5_endpoint_implication | `not R(9, 16, 17) OR not R(5, 9, 16) OR not R(16, 17, 19) OR E_R5(5, 19)` |
| 56 | 238620 | no_R7 | `not R(8, 15, 16) OR not R(7, 8, 15) OR not R(15, 16, 17) OR not R(16, 17, 18) OR not R(6, 7, 8)` |
| 57 | 239060 | no_R7 | `not R(14, 16, 17) OR not R(1, 6, 9) OR not R(9, 14, 16) OR not R(16, 17, 18) OR not R(6, 9, 14)` |
| 58 | 239067 | R6_endpoint_implication | `not R(14, 16, 17) OR not R(5, 9, 14) OR not R(9, 14, 16) OR not R(16, 17, 18) OR E_R6(5, 18)` |
| 59 | 334582 | necessary_blue_fan | `not R(14, 15, 23)` |
| 60 | 341792 | necessary_blue_fan | `not R(14, 15, 18)` |
| 61 | 344669 | necessary_blue_fan | `not R(14, 15, 16)` |
| 62 | 376290 | necessary_blue_fan | `not R(13, 15, 23)` |
| 63 | 393413 | no_R7 | `not R(13, 14, 15) OR not R(12, 13, 14) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 64 | 399232 | packet | `not R(12, 20, 21) OR R(13, 20, 21) OR R(12, 13, 21) OR R(12, 13, 20)` |
| 65 | 401605 | packet | `not R(12, 19, 21) OR R(13, 19, 21) OR R(12, 13, 21) OR R(12, 13, 19)` |
| 66 | 416535 | necessary_blue_fan | `not R(12, 15, 23)` |
| 67 | 431350 | a4_R6_terminal_cut | `not R(12, 13, 21) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 68 | 432128 | a4_R6_terminal_cut | `not R(12, 13, 20) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 69 | 432905 | a4_R6_terminal_cut | `not R(12, 13, 19) OR not R(11, 12, 13) OR not R(10, 11, 12) OR not R(9, 10, 11)` |
| 70 | 436776 | no_R7 | `not R(6, 9, 10) OR not R(12, 13, 14) OR not R(10, 11, 12) OR not R(9, 10, 11) OR not R(11, 12, 13)` |
| 71 | 436781 | no_R7 | `not R(1, 9, 10) OR not R(12, 13, 14) OR not R(10, 11, 12) OR not R(9, 10, 11) OR not R(11, 12, 13)` |
| 72 | 436791 | R6_endpoint_implication | `not R(8, 10, 11) OR not R(12, 13, 14) OR not R(10, 11, 12) OR not R(11, 12, 13) OR E_R6(8, 14)` |
| 73 | 436812 | R6_endpoint_implication | `not R(5, 10, 11) OR E_R6(5, 14) OR not R(10, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 74 | 436817 | R6_endpoint_implication | `not R(4, 10, 11) OR E_R6(4, 14) OR not R(10, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 75 | 436821 | R6_endpoint_implication | `E_R6(3, 14) OR not R(3, 10, 11) OR not R(10, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 76 | 436921 | R6_endpoint_implication | `not R(5, 7, 11) OR not R(7, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14) OR E_R6(5, 14)` |
| 77 | 436973 | R5_endpoint_implication | `E_R5(5, 14) OR not R(5, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 78 | 436983 | R5_endpoint_implication | `E_R5(4, 14) OR not R(4, 11, 12) OR not R(11, 12, 13) OR not R(12, 13, 14)` |
| 79 | 453361 | necessary_blue_fan | `not R(11, 15, 23)` |
| 80 | 456161 | necessary_blue_fan | `not R(11, 15, 18)` |
| 81 | 465047 | packet | `not R(11, 13, 19) OR R(11, 12, 19) OR not R(11, 12, 13) OR R(12, 13, 19)` |
| 82 | 468316 | no_R7 | `not R(3, 4, 11) OR not R(4, 11, 13) OR not R(11, 13, 14) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 83 | 470562 | packet | `not R(11, 12, 20) OR R(11, 12, 19) OR R(11, 19, 20) OR R(12, 19, 20)` |
| 84 | 470610 | R5_endpoint_implication | `not R(11, 12, 19) OR E_R5(9, 19) OR not R(9, 10, 11) OR not R(10, 11, 12)` |
| 85 | 487508 | necessary_blue_fan | `not R(10, 15, 18)` |
| 86 | 503612 | packet | `R(5, 11, 15) OR not R(5, 10, 15) OR not R(10, 11, 15) OR R(5, 10, 11)` |
| 87 | 513884 | necessary_blue_fan | `not R(9, 15, 18)` |
| 88 | 514419 | necessary_blue_fan | `not R(9, 15, 16)` |
| 89 | 515877 | R6_endpoint_implication | `not R(7, 9, 14) OR not R(1, 6, 7) OR not R(6, 7, 9) OR not R(9, 14, 19) OR E_R6(1, 19)` |
| 90 | 515894 | R5_endpoint_implication | `not R(7, 9, 14) OR not R(5, 7, 9) OR not R(9, 14, 19) OR E_R5(5, 19)` |
| 91 | 515917 | packet | `not R(6, 14, 19) OR R(6, 9, 19) OR not R(9, 14, 19) OR not R(6, 9, 14)` |
| 92 | 515918 | packet | `R(6, 14, 19) OR not R(6, 9, 19) OR not R(9, 14, 19) OR not R(6, 9, 14)` |
| 93 | 515955 | packet | `R(6, 14, 19) OR R(6, 9, 19) OR not R(9, 14, 19) OR not R(6, 9, 14)` |
| 94 | 516712 | packet | `R(6, 9, 16) OR not R(6, 14, 16) OR not R(9, 14, 16) OR not R(6, 9, 14)` |
| 95 | 516749 | R5_endpoint_implication | `E_R5(1, 16) OR not R(1, 6, 9) OR not R(9, 14, 16) OR not R(6, 9, 14)` |
| 96 | 516752 | packet | `not R(5, 14, 16) OR R(5, 9, 16) OR not R(5, 9, 14) OR not R(9, 14, 16)` |
| 97 | 537351 | packet | `R(5, 14, 15) OR not R(5, 8, 14) OR not R(8, 14, 15) OR not R(5, 8, 15)` |
| 98 | 537352 | packet | `R(5, 14, 15) OR R(5, 8, 14) OR not R(8, 14, 15) OR not R(5, 8, 15)` |
| 99 | 542511 | packet | `R(10, 11, 15) OR not R(8, 10, 15) OR R(8, 10, 11) OR not R(8, 11, 15)` |
| 100 | 546630 | R5_endpoint_implication | `E_R5(5, 16) OR not R(5, 7, 8) OR not R(8, 9, 16) OR not R(7, 8, 9)` |
| 101 | 546640 | R5_endpoint_implication | `not R(4, 7, 8) OR E_R5(4, 16) OR not R(8, 9, 16) OR not R(7, 8, 9)` |
| 102 | 546759 | packet | `R(7, 8, 15) OR not R(7, 9, 15) OR not R(7, 8, 9) OR not R(8, 9, 15)` |
| 103 | 546795 | R6_endpoint_implication | `not R(5, 7, 8) OR not R(1, 5, 7) OR E_R6(1, 15) OR not R(8, 9, 15) OR not R(7, 8, 9)` |
| 104 | 546861 | packet | `R(5, 9, 15) OR not R(5, 8, 15) OR not R(8, 9, 15) OR not R(5, 8, 9)` |
| 105 | 546925 | necessary_blue_fan | `not R(8, 9, 14)` |
| 106 | 559802 | no_R7 | `not R(3, 5, 7) OR not R(5, 7, 9) OR not R(7, 9, 15) OR not R(2, 3, 5) OR not R(1, 2, 3)` |
| 107 | 559817 | no_R7 | `not R(4, 7, 9) OR not R(3, 4, 7) OR not R(7, 9, 15) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 108 | 565752 | R6_endpoint_implication | `not R(3, 6, 14) OR not R(6, 14, 19) OR not R(2, 3, 6) OR not R(1, 2, 3) OR E_R6(1, 19)` |
| 109 | 566071 | no_R7 | `not R(4, 6, 14) OR not R(3, 4, 6) OR not R(6, 14, 15) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 110 | 570383 | packet | `not R(1, 9, 15) OR not R(1, 6, 9) OR R(1, 6, 15) OR not R(6, 9, 15)` |
| 111 | 570386 | packet | `R(1, 9, 15) OR not R(1, 6, 9) OR R(1, 6, 15) OR not R(6, 9, 15)` |
| 112 | 571353 | no_R7 | `not R(4, 6, 8) OR not R(6, 8, 15) OR not R(3, 4, 6) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 113 | 575960 | no_R7 | `not R(4, 5, 14) OR not R(5, 14, 15) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 114 | 577716 | no_R7 | `not R(4, 5, 11) OR not R(5, 11, 15) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 115 | 579035 | no_R7 | `not R(4, 5, 9) OR not R(5, 9, 15) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 116 | 579991 | no_R7 | `not R(4, 5, 8) OR not R(5, 8, 9) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 117 | 580756 | no_R7 | `not R(5, 6, 23) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 118 | 581001 | no_R7 | `not R(5, 6, 18) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 119 | 581136 | no_R7 | `not R(5, 6, 15) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 120 | 581179 | no_R7 | `not R(5, 6, 14) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 121 | 581379 | no_R7 | `not R(5, 6, 9) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 122 | 581416 | no_R7 | `not R(5, 6, 8) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 123 | 581452 | no_R7 | `not R(5, 6, 7) OR not R(4, 5, 6) OR not R(3, 4, 5) OR not R(2, 3, 4) OR not R(1, 2, 3)` |
| 124 | 588538 | R6_endpoint_implication | `not R(4, 5, 15) OR E_R6(1, 15) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 125 | 588673 | R6_endpoint_implication | `not R(4, 5, 10) OR E_R6(1, 10) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 126 | 588742 | R6_endpoint_implication | `E_R6(1, 7) OR not R(4, 5, 7) OR not R(2, 3, 4) OR not R(1, 2, 3) OR not R(3, 4, 5)` |
| 127 | 588760 | packet | `R(3, 4, 6) OR not R(3, 5, 6) OR not R(3, 4, 5) OR not R(4, 5, 6)` |
| 128 | 595335 | R5_endpoint_implication | `E_R5(1, 11) OR not R(3, 4, 11) OR not R(1, 2, 3) OR not R(2, 3, 4)` |
| 129 | 595348 | packet | `R(3, 10, 11) OR not R(3, 4, 11) OR R(3, 4, 10) OR R(4, 10, 11)` |
| 130 | 595352 | R5_endpoint_implication | `not R(3, 4, 10) OR E_R5(1, 10) OR not R(1, 2, 3) OR not R(2, 3, 4)` |
| 131 | 595407 | packet | `R(2, 3, 6) OR not R(2, 4, 6) OR not R(2, 3, 4) OR not R(3, 4, 6)` |
| 132 | 595419 | packet | `R(2, 3, 5) OR not R(2, 4, 5) OR not R(2, 3, 4) OR not R(3, 4, 5)` |
| 133 | 607960 | frozen_red_path | `R(1, 2, 3)` |
| 134 | 636129 | frozen_red_path | `R(2, 3, 4)` |
| 135 | 641569 | A_no_in_B4 | `R(2, 4, 5) OR R(4, 5, 8)` |
| 136 | 642293 | A_no_in_B4 | `R(2, 4, 6) OR R(4, 6, 8)` |
| 137 | 657925 | frozen_red_path | `R(3, 4, 5)` |
| 138 | 659516 | A_no_in_B4 | `R(3, 4, 7) OR R(4, 7, 8)` |
| 139 | 661351 | no_B6 | `R(3, 4, 11) OR R(4, 11, 12) OR R(11, 12, 19) OR R(12, 19, 21)` |
| 140 | 661400 | no_B6 | `R(4, 11, 13) OR R(3, 4, 11) OR R(11, 13, 19) OR R(13, 19, 21)` |
| 141 | 662705 | A_no_in_B4 | `R(3, 5, 6) OR R(5, 6, 15)` |
| 142 | 662796 | A_no_in_B4 | `R(5, 7, 8) OR R(3, 5, 7)` |
| 143 | 674550 | frozen_red_path | `R(4, 5, 6)` |
| 144 | 675386 | A_no_in_B4 | `R(4, 5, 7) OR R(5, 7, 9)` |
| 145 | 676270 | T_no_B5_endpoints | `R(5, 8, 15) OR R(4, 5, 8) OR R(8, 15, 16)` |
| 146 | 676986 | no_B6 | `R(5, 10, 15) OR R(4, 5, 10) OR R(10, 15, 18) OR R(15, 18, 19)` |
| 147 | 677113 | no_B6 | `R(5, 11, 12) OR R(4, 5, 11) OR R(11, 12, 20) OR R(12, 20, 21)` |
| 148 | 677642 | T_no_B5_endpoints | `R(5, 14, 16) OR R(4, 5, 14) OR R(14, 16, 17)` |
| 149 | 687140 | A_no_in_B4 | `R(6, 7, 9) OR R(5, 6, 7)` |
| 150 | 688023 | A_no_in_B4 | `R(6, 8, 15) OR R(5, 6, 8)` |
| 151 | 689396 | T_no_B5_endpoints | `R(14, 16, 17) OR R(6, 14, 16) OR R(5, 6, 14)` |
| 152 | 696227 | frozen_red_path | `R(6, 7, 8)` |
| 153 | 704825 | frozen_red_path | `R(7, 8, 9)` |
| 154 | 709228 | left_extension_no_out_B5 | `R(7, 11, 12) OR R(11, 12, 19) OR R(12, 19, 20)` |
| 155 | 712123 | no_T_to_T_B4 | `R(9, 14, 16) OR R(8, 9, 14)` |
| 156 | 712190 | T_no_B5_endpoints | `R(9, 14, 19) OR R(14, 19, 20) OR R(8, 9, 14)` |
| 157 | 712210 | frozen_red_path | `R(8, 9, 15)` |
| 158 | 712298 | no_T_to_T_B4 | `R(8, 9, 16) OR R(9, 16, 17)` |
| 159 | 713285 | no_T_to_T_B4 | `R(8, 10, 15) OR R(10, 15, 18)` |
| 160 | 714018 | no_T_to_T_B4 | `R(8, 11, 15) OR R(11, 15, 18)` |
| 161 | 715083 | no_T_to_T_B4 | `R(8, 14, 15) OR R(14, 15, 18)` |
| 162 | 715504 | frozen_red_path | `R(9, 10, 11)` |
| 163 | 718582 | frozen_red_path | `R(10, 11, 12)` |
| 164 | 719945 | frozen_red_path | `R(11, 12, 13)` |
| 165 | 720298 | A_no_in_B4 | `R(11, 13, 14) OR R(13, 14, 15)` |
| 166 | 720776 | frozen_red_path | `R(12, 13, 14)` |
| 167 | 721639 | frozen_red_path | `R(15, 16, 17)` |
| 168 | 721822 | frozen_red_path | `R(16, 17, 18)` |
| 169 | 721848 | B_no_out_B4 | `R(17, 19, 20) OR R(16, 17, 19)` |
| 170 | 721855 | B_no_out_B4 | `R(17, 19, 21) OR R(16, 17, 19)` |
| 171 | 721955 | frozen_red_path | `R(18, 19, 20)` |
| 172 | 721972 | frozen_red_path | `R(19, 20, 21)` |
| 173 | 721973 | frozen_red_path | `R(20, 21, 22)` |
| 174 | 721974 | frozen_red_path | `R(21, 22, 23)` |
| 175 | 721979 | known_R6_source | `Src_R6(16)` |
| 176 | 721980 | known_R6_source | `Src_R6(17)` |
