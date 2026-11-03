# Whole saturated-component copying: all five sources blocked

Each of the five specified accepted/reportedD5 sources has exactly one connected component of saturated vertices. For degrees11,12,13,14,15 their sizes are35160,28545,38333,90501,101250. Each fails all three necessary gates: at least one free boundary vertex lacks slots for its full copy load; at least one saturated vertex has no outside exit; and the component exceeds the degree-specific diameter3 Moore bound.

All five complete saturated-component classes were scanned once. No component reached the internal all-root R3 stage, so there were zero distance BFS, R4 checks, solver calls or graph exports. The original sourceD5 facts were inherited; the degree15 source used its saved102060 CSR, and the other four existing edge tables were read once.

The sufficient rule copies a complete saturated component internally and reconnects each new copy to the same old free boundary. If degree loads fit, every copied vertex has an outside exit and internal diameter is at most3, then new-old distances inside the component are at most2+3; other old targets follow an old shortest path up to the first exit. New-new distance is at most3 and all old-old paths remain. Here degree legality already rules out every complete component, independently of the diameter gate.

WorkerCPU0.274693, compile1.278946, aggregate1.557719699seconds within15CPU. PID785931/session54233 ended exit0. Complete component membership and first boundary-capacity witnesses are in COMPONENTS_D11..D15.jsonl. This closes only the fixed complete-saturated-component copy rule on these sources, not arbitrary subsets including unsaturated vertices, other rewiring or other collaborative extensions. No increasing component-size search was run.
