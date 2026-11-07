# ES7PrefixData source acquisition — stopped before SSH connection

The single transport invocation failed while opening the SSH connection: PermissionError / WinError 10013 (socket access denied). Existing transport pattern and dependencies were used; no dependency installation occurred.

Raw evidence: transport_receipt.json. Recorded retrieval_runs = 0. No Linux command was run, no HTTP range request was issued, no source was acquired, and no retry or whole-archive download was attempted.

Requested exact entry: es7_es8_bounds_81_319_v1/formal/sources/ES7PrefixData.lean.
Declared uncompressed size: 29724 bytes; compressed size: 2033 bytes; ZIP offset: 199105299.
Declared SHA256: 3aba553125c23cc817d8d1ba7e98fc62f9517b2ac7a8466890c000224af72777.
These are pre-existing index/manifest declarations, not newly verified source identity. Data declarations cannot be summarized because source acquisition did not occur.

request_metadata.json records the exact existing archive/index binding. acquire_prefix_linux.py and transport.py are prepared acquisition/transport inputs only. All files are confined to prefix_source/; prior artifacts were not modified. No SAT, scientific execution, proof checking, compilation, replay, mathematical analysis, acceptance or assurance upgrade occurred.
