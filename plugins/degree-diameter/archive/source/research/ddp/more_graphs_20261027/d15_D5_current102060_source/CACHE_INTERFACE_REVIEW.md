# Current102060 cache interface review

Read-only checks pass. No ball, source distance, model or solver was recomputed. The existing builder parses `source102060.author.adjlist.txt`; one marking operation writes both the radius-four ball and its transposed target support, and the same adjacency object writes CSR. This is the actual102060 source, not the historical100132 graph.

All810 columns follow `monotone_R4_cover/eligible.txt`. Its order exactly matches `SOURCE_PROFILE.json` free_vertices and `PREFLIGHT.json` eligible_labels. CSR confirms degree14 for every eligible label.

`radius4.u64le.bin` is810×1595 little-endian uint64 words,10335600 bytes. A row is an eligible column; a bit is an old vertex ID. The last word has44 valid low bits and20 padding bits. All810 padding tails are zero. `target_rows.u64le.bin` is102060×13 words,10614240 bytes. A row is an old target ID; bit r is eligible column r. Its last word has42 valid low bits and22 padding bits; all102060 padding tails are zero.

`source.csr.u32le.bin` has little-endian uint32 header[102060,1530090], followed by102061 offsets and1530090 neighbor IDs. Offsets begin at byte8; neighbor data begin at byte408252. The total size is6528612 bytes, offsets run0..1530090, and eligible degrees are14.

The full static model is exactly102060 real cover inequalities plus sum(x)<=15 over810 binaries. It must not inherit the old active/rare/spread row subset or constraint-generation loop. Existing memmap shapes, selected-ball OR with the44-bit tail mask, and eligible-label mapping can be reused. Known distinctness results need not be recomputed. Exact full coverage and degree checks turn an incumbent into a concrete candidate; solver status alone does not.

The new worker/driver implementation, thread count and aggregate budget were subsequently checked in `full_static_R4_cover/CODE_REVIEW.md/json`, with no blocker. This cache note makes no claim about the solver outcome.
