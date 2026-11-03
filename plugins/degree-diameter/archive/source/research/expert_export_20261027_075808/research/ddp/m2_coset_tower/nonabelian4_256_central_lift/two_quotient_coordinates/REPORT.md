# Complete two-coordinate quotient range

The complete 74,958-projection scope finished with no D3 graph. The source was the original independently checked Q64 graph with 832 bad pairs. Exactly two distinct free quotient coordinates were changed, both to a different value; this scope is disjoint from the original projection and the previously completed 403 one-coordinate projections.

Of these projections, 74,603 had an empty radius-three quotient target slot. The remaining 355 were quotient-complete and each had a nonempty legal center-assignment space, but every one had at least one target slot with only one distinct affine form (mask,b). Such a slot can reach only one of its two central lifts for every center assignment. All 355 were therefore rejected by this necessary condition. The minimum number of these constant bad slots was 12.

No projection entered joint center scoring. Thus there were **zero central assignments enumerated, zero graphs generated, and zero BFS runs**. The conditional first-formal-center calibration was inapplicable; no substitute sample was created. There is no saved best or pending final verification. This completes the D3 exclusion for exactly this two-coordinate lift range, not for arbitrary Q64 voltage graphs.

The actual group-word/GF2 scoring core was copied from the completed and calibrated parent-directory implementation. The only changes were the two-coordinate traversal and the singleton-form filter, which ignores path lengths when determining whether affine forms are identical. Parallel projected edges retain their distinct base-edge IDs and true inverse darts; their legal center constraints are checked before this new filter. No stronger joint-condition filter was added. See [SCOPE.md](SCOPE.md) and prepare.py.

| Constant bad slots | Number of quotient-complete projections |
|---:|---:|
| 12 | 1 |
| 13 | 1 |
| 14 | 3 |
| 15 | 8 |
| 16 | 2 |
| 17 | 7 |
| 18 | 4 |
| 19 | 5 |
| 20 | 5 |
| 21 | 9 |
| 22 | 8 |
| 23 | 26 |
| 24 | 13 |
| 25 | 18 |
| 26 | 17 |
| 27 | 21 |
| 28 | 21 |
| 29 | 25 |
| 30 | 10 |
| 31 | 14 |
| 32 | 16 |
| 33 | 16 |
| 34 | 12 |
| 35 | 11 |
| 36 | 11 |
| 37 | 7 |
| 38 | 13 |
| 39 | 6 |
| 40 | 7 |
| 41 | 1 |
| 42 | 8 |
| 43 | 5 |
| 44 | 2 |
| 45 | 3 |
| 46 | 4 |
| 47 | 2 |
| 48 | 2 |
| 49 | 5 |
| 50 | 2 |
| 52 | 1 |
| 54 | 2 |
| 55 | 1 |

The minimum 12 occurs for 1 projections. Their exact cursors, two changed edges, and replacement quotient codes are retained in summary.json; every projection and terminal reason is retained in projections.jsonl.

CPU: source preparation 0.000740732 s, driver preparation and compilation 1.136050000 s, production 0.994118000 s; total 2.133851732 s, below the 180-second budget. Session 61479, worker PID 3788992, and driver PID 3788017 terminated with exit code 0. All 74,958 cursors are present exactly once. There was no restart, extension, independent full-root check, or new candidate queue. terminal.json has pending=[].
