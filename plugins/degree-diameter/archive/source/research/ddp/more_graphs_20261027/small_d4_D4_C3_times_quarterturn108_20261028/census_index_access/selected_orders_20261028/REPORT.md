# Selected census members downloaded

**COMPLETE_DOWNLOAD:69 files, from an initial68-file success plus one separately authorized payload retry.** The selected members are Cay4val_42.s6 through Cay4val_53.s6 and Cay4val_105.s6 through Cay4val_161.s6. Filename/order and decompressed byte size match the saved ZIP index for every member. No CRC, hash, or checksum was computed.

The original fixed69-member batch used at most4 parallel network requests and finished in84.976724528 wall seconds with68 complete members and one TLS EOF at order110's payload connection. Its local header had already succeeded. INITIAL_BATCH_RECEIPT.json preserves that PARTIAL result unchanged; there was no automatic restart or member retry.

The parent then authorized exactly one additional request for110's missing48291-byte compressed payload. It returned206 with the exact saved Content-Range, raw-deflated to75000 bytes, and finished in2.517085575 wall seconds. RETRY_110_RECEIPT.json preserves that separate operation. The current DOWNLOAD_RECEIPT.json merges68+1 and explicitly records both stages rather than claiming a wholly successful original batch.

Cumulative body bytes actually read were5,778,941; declared-body budget charges, including the failed request reservation, were5,827,232, below8,000,000. Download-process wall times sum to87.493810102 seconds; this is the sum of the two recorded operations. The full25.27GB archive was never downloaded, no mirror was used, and no further request is running.

There was0 graph decoding, BFS, search, or solver work. The downloader did not count graphs inside the sparse6 files; index metadata has no expected graph-count field. The unique filter owner was notified of COMPLETE_DOWNLOAD and will perform that parsing once. This transfer alone establishes no diameter bound or new graph. DOWNLOAD_SUMMARY.json gives the short handoff; all HTTP receipts and member paths are in DOWNLOAD_RECEIPT.json.
