# Projection-bound descent completed, best L=4

The complete authorized 16-start profile found a projection with **L=4**, zero empty quotient slots, and four singleton-distinct-form slots. No evaluated projection had L=0. Accordingly no central masks were enumerated and no full graph was generated; this is not a new diameter-three construction.

The original 832-bad-pair source projection scored L=18, consisting of two empty slots and fourteen singleton slots. Its four representative roots' 1,024 radius-three distances exactly matched the previously saved independent distance matrix. This check used the short-walk representation and ran no new BFS or source-center enumeration.

The actual start list was the original source, the completed two-coordinate cursor-52852 projection, and fourteen fresh legal projections with seed 20261027080. It was fixed before launch and is retained in `starts.json`. The final execution counts were:

| Quantity | Actual count |
|---|---:|
| Starts completed | 16 / 16 |
| Segments completed | 144 / 144 |
| Complete 403-neighbor inspections | 576 |
| Strict descent moves | 432 |
| Raw neighbor trials | 232,128 |
| Illegal neighbor projections | 12 |
| Accepted two-coordinate kicks | 128 |
| Legal projection evaluations, including starts and kicks | 232,260 |
| L=0 projections / center masks / new BFS calls | 0 / 0 / 0 |

The best saved projection, in the fixed 16-edge order, is

`[0,4,10,0,15,8,0,18,16,1,11,8,13,4,28,25]`.

It was first scored at evaluation 82,959, start 5, segment 7. `best_projection.json` labels it explicitly as a projection rather than a graph. Its L=4 implies a lower bound of four on the summed root deficit of **every** central lift of that projection, equivalently at least 128 bad unordered pairs in a simple full lift. It does not assert that this lower bound is attainable or that any particular center assignment was scored.

The single process was session 3673, PID 3849115, with driver PID 3848456. Preparation and compilation used 1.688076 CPU seconds, production used 8.397814, and total measured CPU was 10.088651 seconds. The runtime limit was 177.311924 seconds after preparation and reserve; the profile finished normally well before the overall 180-second budget. There was no restart, scope extension, added seed, or three-coordinate source-ball search.

`terminal.json` is `COMPLETE_16_START_PROFILE_NO_D3`, with a null next cursor and no pending validation. `source_calibration.json` records the reused-distance comparison; `events.jsonl` records completed neighborhoods and kicks; `metadata.json` and `SCOPE.md` define the precise objective and coverage. No `best.edges` file was produced because no L=0 projection entered center optimization. This finite profile does not exhaust the Q64 projection family.


## Saved best projection: exact remaining obstruction

root对保存的L4投影作短词诊断：四个单一形式目标恰好分别是四个轨道的商单位元，而且每个只有空路径。因此四类中心反点都无法在三步内到达；任何合法中心提升至少留下128坏对。这不是声称128可达到，也不是一张已验完整图。继续只改中心位不能修复该商。下一步应把中心反点的短闭路条件纳入构造，例如保证覆盖四轨道的三角路径具有正确中心值，再优化其他目标；具体新批次尚未启动。

The independent root short-word diagnosis in best_projection.diagnosis.json used 0.002710304 CPU seconds and no graph or BFS. It reads one saved projection, not another search range.
