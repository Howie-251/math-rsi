# One controlled degree15 allfree batch

Keep the D14 algorithm fixed and change only the actual source and degree cap: current100132/749732,2498 free pins, at most15 chosen. Reuse the20 cached roots in their saved interface order; compute the other2478 balls once. Profile the first100 new balls without replay.

The first-pin ranking and rarest-target/full-gain rule are frozen in PREDICTION.json. Use at most64 distinct first pins. No coordinate swaps, extra starts, random seeds, solver or continuation from a smallest miss count.

A complete cover must export the full100133 edge list with every old edge retained, legal actual degrees and one new-root BFS. Root performs the one independent acceptance for the new parameter. If no hit or budget expiry, save the exact cursor, full union/supports and terminal scope, then stop. Shared budget20CPU seconds includes compilation and cache construction.
