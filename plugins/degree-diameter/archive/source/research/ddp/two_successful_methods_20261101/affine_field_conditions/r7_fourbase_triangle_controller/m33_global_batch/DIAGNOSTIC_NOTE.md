# Read-only branch diagnostic

The completed2,000,000-candidate batch was not resumed. This diagnostic read its24MB record file once, performed no bulk support replay and drew no new parameters. It reused the saved full signature and evaluated only the other two already sampled deep candidates, once each with the existing single-candidate checker. CPU0.587981923seconds under the separate2-second diagnostic budget.

Each branch had400,000 actual candidates. The following entries count candidates passing through the named gate, including every preceding gate in the saved check order. Reverse classes20,10,21 add no failures after their forward classes.

| a0 | after33 | after02 | after11 | after01 | after12 / reached03 |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 7010 | 76 | 18 | 1 | 0 |
| 2 | 7202 | 91 | 22 | 6 | 0 |
| 3 | 7014 | 89 | 21 | 4 | 1 |
| 11 | 8165 | 112 | 20 | 3 | 0 |
| 22 | 8043 | 120 | 21 | 4 | 2 |

The full depth histogram and pass count after every checked class are in `DIAGNOSTIC_RESULT.json`.

Exactly three existing candidates reached03. Their voltage order is(a0,a1,a2,a3,sigma01,sigma23,tau02,tau13,rho03,rho12).

| Attempt | Parameters |
| ---: | --- |
| 777398 | (3,25,27,0,17,21,32,25,12,2) |
| 867355 | (22,26,31,0,25,17,21,21,4,27) |
| 1180635 | (22,29,21,0,5,0,9,2,15,30) |

Their full support-size matrices, in that order, are

```
33 33 33 31       33 33 33 32       31 33 33 32
33 33 33 32       33 33 33 32       33 33 33 32
33 33 33 32       33 33 31 33       33 33 33 30
31 32 32 33       32 32 33 33       32 32 30 33
```

All three miss some shifts at base pairs03 and13, and consequently their inverse pairs30 and31. No other incomplete base pair is common to all three. The literal common-pair deficits are

| Attempt | 03 missing shifts | 13 missing shifts |
| ---: | --- | --- |
| 777398 | {2,8} | {29} |
| 867355 | {5} | {8} |
| 1180635 | {25} | {27} |

There is no common missing residue class modulo3 in these normalized coordinates:03 has phases2,2,1 and13 has phases2,2,0. There is also no common literal missing shift. These are three sampled examples in different a0 branches; raw shift comparisons are coordinate dependent and do not establish a family obstruction. All remaining missing shifts, including the differing00/22 diagonal or23 deficits, are explicitly preserved in the diagnostic JSON.

The shared03/13 defect is evidence for root's next mechanism decision only. It has not triggered a hillclimb, new seed, extra sample allocation, modulus change or new controller construction. Both the global batch and this diagnostic have no active process.
