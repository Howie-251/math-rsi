# Execution version of the 2,567-vertex result

**The new (10,4) result was obtained with MathRSI v2 and its degree–diameter plugin, including the handoff repair subsequently merged as [PR #7](https://github.com/lisresearchgroup/math-rsi/pull/7).**

The research launcher selected the `math-rsi-publish` checkout on branch `fix/agent-handoff-instructions`. Its local branch history and reflog, checked on 5 November 2026, identify the research checkout; the repository PR history supplies the remote merge times. All times below are UTC.

| 4 November 2026 | Event |
| --- | --- |
| 08:41 | Research branch created from the then-current `origin/main`, the v2 implementation. |
| 08:44 | Local repair committed: “Clarify agent dispatch, artifact handoff, and recovery snapshots.” |
| 13:20 | PR #7 merged remotely. |
| 14:07 | The v3 upgrade, [PR #8](https://github.com/lisresearchgroup/math-rsi/pull/8), merged remotely. |
| 18:22 | The complete 2,567-vertex graph was independently accepted; the selected research checkout still used its 08:44 repair. |

The selected checkout was clean and had received no later local update during this research run. Its repair changes the existing research, prove and handoff skills and workspace instructions; the degree–diameter plugin is present in that checkout. Here **v2** identifies that v2 implementation with the handoff repair, rather than asserting execution from the untouched fixed `v2` tag.

The [v3 release notes](../../../docs/V3_CHANGES.md) explicitly classify PR #7 as a small repair to the existing v2 workflow, integrated into v3, rather than a separate research-driven iteration. The publication worktree was subsequently updated to current `main` with v3; that is the version used to prepare this publication. The research result retains its actual v2 execution attribution.

The earlier **153 graph instances** retain their original ARIS research attribution. The new ten-version (10,4) sequence belongs to the later MathRSI v2 run. This version record establishes execution provenance; it does not measure a speedup or relabel the earlier examples as v2 experiments. The [construction package](../reproduce/d10_d4/) preserves the resulting graphs, replay and verification records.
