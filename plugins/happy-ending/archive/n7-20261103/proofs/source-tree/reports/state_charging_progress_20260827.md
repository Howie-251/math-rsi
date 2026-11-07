# State-charging progress checkpoint — 2026-08-27

This checkpoint records the exact proof boundary after the Qlt decomposition and
triple-only localization runs. It is an index, not a replacement for:

- `reports/state_charging_transition_q_relaxations.md`
- `reports/state_charging_triple_only_localization.md`

## Repository state

- Branch: `main`
- Relevant commits:
  - `7e2d151` — decompose Qlt by minimum-cup branches
  - `fd8c58e` — certify the triple-only recursive core
  - `028c83d` — record the D-drive AE solver location
- Default local proof-producing solver:
  `D:/科研/math agent/erdos-szekeres-sat-main/AE_kissat2025_MAB`
- Server solver:
  `/data/ktqiu_hdd/math_agent/AE_kissat2025_MAB/build/kissat`
- Server solver SHA-256:
  `c2e44161cd142694f2b612e0be2dcc59cb656df6d42f8713adc4d05b9a22f5fa`
- Independent checker SHA-256:
  `2f01df83916c158d7da43deefde1ea3ea60b19f5d636ae03f31042e88ef179e9`
- Large proof bodies remain on the server. The local workspace retains
  lightweight evidence, while the reports index its statuses and hashes.

## Qlt line: proved boundary

The direct relaxation results are:

- `A0`: `AUDITED_SAT_N25`
- `Aeq1`: `AUDITED_SAT_N25`
- `Agt1`: `UNKNOWN` after 3600 seconds

Taken alone, these direct-relaxation results do **not** prove that every such
`A_v` witness has `q_v = 1`, and they do not settle Qlt.  The later fixed-q
decomposition recorded below closes Qlt separately without changing the
retained `Agt1=UNKNOWN` result.

The typed scopes used below are
`A_v = TF[E411,path6_before_path5](v)`,
`B_w = T[E421,path6_before_path5](w)`, and
`P(v,w) = A_v and B_w and v<w and not F(t) for every v<t<w`.

For the endpoint-only branch `A_v and q_v = 2`:

- Endpoint-only suite (`v = 6..25`): 13 verified UNSAT cases
  (`v = 6..9` and `v = 17..25`) and 7 UNKNOWN cases (`v = 10..16`).

For the exact-pair branch `P(v,w)`, `q_v = 2`, and `q_w = 1`:

- Exact adjacent-event suite (`w-v = 1`): 19/19
  `VERIFIED_UNSAT_N25`, closed.
- Exact distance-two suite (`w-v = 2`): 18/18
  `VERIFIED_UNSAT_N25`, closed.
- Exact gaps 3 through 15: all 143 pairs are closed by mixed direct and
  endpoint-derived evidence. The 70 pairs whose first endpoint lies in the
  unresolved direct frontier were run as standalone target CNFs; the other 73
  rows were freshly derived by same-`v` clause inclusion from proof-verified
  qv2 endpoint sources.
- Exact gaps 16 through 19: all 10 pairs are endpoint-derived, so these gaps
  were closed without launching additional target-pair solvers.
- Complete aggregate: all 190 canonical pairs are negative, with 107 direct
  `VERIFIED_UNSAT_N25` rows and 83 `DERIVED_UNSAT_N25` rows, zero audited SAT,
  and zero UNKNOWN. Its theorem status is
  `qv2_qw1_partition_excluded`, and the qv3 follow-up gate passed.

The established fixed-coordinate conclusion is:

> Under the encoded exact-pair semantics, every `q_v = 2`, `q_w = 1`
> pair `6<=v<w<=25` is impossible.

The gated `q_v=3,q_w in {1,2}` partition is now also closed. Its 18-case
endpoint-source family
`T0 and selector_A(v) and MinCup(v,3)`, `v=7..24`, ended with 17
proof-verified UNSAT rows (`v=7..12` and `v=14..24`) and one UNKNOWN row
(`v=13`, 900-second budget). Thus the endpoint wave itself is not closed and
does not establish `qv3_endpoint_source_wave_excluded`. The 17 verified
sources nevertheless support 318 same-`v` clause-inclusion derivations. The
24 complementary rows at `v=13`, with `w=14..25` for each of `q_w=1,2`, were
run directly.

The fixed-pair campaign completed all 36 exact-gap shards and all 342 canonical
pairs. Every row is negative: 24 are direct proof-verified UNSAT rows and 318
are endpoint-derived rows, with zero SAT and zero UNKNOWN. Each `q_w` partition
contributes 171 rows, split as 12 direct plus 159 derived. The exact theorem
status is `qv3_qw1_qw2_pair_partitions_excluded`.

At this intermediate qv3 checkpoint, combining this result with
`qv2_qw1_partition_excluded` restricted any remaining Qlt witness to
`q_v>=4`.  The later qv2..qv20 prefix below separately excludes Qlt.  Neither
the qv3 checkpoint nor that eventual fixed-q closure establishes an endpoint
wave theorem or monolithic `Agt1` UNSAT.

On 2026-08-28 the retained qv2 aggregate and qv3 summary/audit were replayed
into the create-only cumulative `prefix[3]` record at
`/data/ktqiu_hdd/math_agent/res/state_charging/20260828_transition_qlt_fixed_q_prefix/qv03/prefix_qv03.json`.
It contains exactly 532 negative pairs in closed-q order `[2,3]`, has theorem
status `qlt_qv2_to_3_partitions_excluded`, and opens only `next_fixed_q=4`;
`qlt_excluded` remains false. Its serialized-file SHA-256 is
`4a6c819191c1b9f45a7a7cc7406b00bd6b28bc22577581bc1368a8e6aa2db530`,
its semantic `final_sha256` is
`e5d8a90cfa3fdd222eaf94e257b169d6be23f00e4292ae6682c0be0ec61ce70a`,
and the validated qv4 gate SHA-256 is
`6a492f88010daa4df7b96cd721e071b85f6fb5cdf55672f52fef466e8dd60e87`.
No qv4 solver had been launched at the time this gate was created.

Selected evidence identities (entries labelled semantic are `final_sha256`
or equivalent semantic self-hashes; entries labelled serialized are hashes of
the JSON files themselves):

- qv2 endpoint suite semantic SHA-256:
  `1537ee1c94f84bca5ed3e901e687ad7087feaa410129ed920b6b5e7659805b98`
- qv2 gap-one semantic SHA-256:
  `97b6dd12edc50bd14c63acb71a8c8b351dc1f3b6ace0de8dae7714ecc6f888df`
- qv2 gap-two semantic SHA-256:
  `a8fc6607c9a937a5a08add1439c0b9d31e2d4a83fb8658b11e349f23d8a16366`
- fresh qv2 endpoint-replay semantic SHA-256 (13 verified UNSAT, 7 UNKNOWN):
  `d7e43a96c89bc801fc20fcd5adce340a9e75d9032c21a2071d7989a18c459ea8`
- qv2 gap-three direct-frontier semantic SHA-256:
  `28f8c8010df1dbc509c5ba6e0d9092338627c53cd334fcb87c7714691f2b7d10`
- qv2 gap-three mixed-closure semantic SHA-256:
  `1c04ba11a2d9f3c7702a2a467fa4e7ff3b9ac7ab7efa36f603092e73daed6110`
- complete qv2/qw1 190-pair aggregate semantic SHA-256:
  `84c9dd644a8aa05fbe7b95ecd3878255890ffdca86040b648b6184dee64e722f`
- complete aggregate serialized-file SHA-256:
  `8b582426f93aa8b2fff913fc98f3accb2e08c4aa2c8a1d607c7d26c411826461`
- qv3 endpoint fresh-replay semantic SHA-256:
  `ab9ded09428a7ea7e11e6814ea29ba400d03602096652923e5d6332dfe370026`
- qv3 endpoint fresh-replay serialized-file SHA-256:
  `ac7e787bf3a2016c9d1ac69bfb9edeb1d53845f8a3534cf0b2afc016bb099790`
- qv3 pair-campaign seal file SHA-256:
  `972c08216c315e505d326593d59d49bc0818875a2b9008190d1038ccb690e184`
- qv3 pair-campaign sealed configuration semantic SHA-256:
  `6545f0279044e069d075618ae1a921a86e5da61783dae3b511cd240fb5166c3b`
- qv3 pair-campaign progress serialized/semantic SHA-256:
  `f4ea72bad0c0cf5ab1171f300ebf28da7196cddaa3fee4c081452cf92dcff79d` /
  `6701d6ec37fcb14132407276d15818e210644cfc259e6b677d3ca81621e95ecd`
- qv3 pair-campaign summary serialized/semantic SHA-256:
  `4df2ca1fa01a25a9b6a96f974d4ec484cbacf1283cd5c1215cc4984dc34247b3` /
  `2abce4483335957c845297140c89a42ade00e0fee5ba4bf2d53a121fb2424e96`
- independent qv3 campaign audit serialized/semantic SHA-256:
  `78d35a9a012484d9090ed85f7f7ad022afe590aa3d195cffa47290ff0498e408` /
  `3966162c30afea98179eb7ccddc9b7da258f8cffc3e5e6e89c0fc094fef57217`

The accepted independent audit covered 604 bound files totalling
6,264,934,534 bytes and 17 unique endpoint proofs. It checks the sealed
campaign, evidence bindings, closure accounting, and proof/checker
attestations. As a deliberately lower-cost independent audit, it does not
rebuild the `T0` CNF and does not rerun the solver or checker; the campaign's
fresh per-shard executions remain the primary proof runs.

The exact-gap registry contains all 153 gap-at-least-three pairs exactly once.
Its semantic SHA-256 is
`e7d8bb551aefe8735b1a60b26cd1d935768273ca266eeab57c8a0f61f69b630f`;
the serialized file SHA-256 is
`97b58ff2aee270bdb76e58efcea82d16ba33ce114abcbd34b2db8a4980f8aeeb`.

## Triple-only line: proved boundary

- In the standalone order-19 triple-only encoding, each of the 28 hypotheses
  `Fan(18) and Fan(19) and blue-path [9,a,b,18]`,
  `10 <= a < b <= 17`, was independently `VERIFIED_UNSAT` in the
  condensed reference encoding.
- For `[9,10,11,18]`, the first semantic-object-closed core had 10,966
  objects and 18,267 clauses and was independently checked
  `VERIFIED_UNSAT`, closed.
- Recursive complete-object closure produced a smaller certified core with:
  - 8,396 semantic objects;
  - 14,142 clauses;
  - 969 variables;
  - CNF SHA-256
    `e0c24b8688757fc4e4f6204212380d22647e8c9972c432f8cdc3bdf63e3968eb`;
  - proof SHA-256
    `f774ac309835cacca005ce701ebf2b63b04d8e28d7e508d4b320f3888d2bb334`;
  - independently checked status `VERIFIED_UNSAT`, closed;
  - semantic final-record `final_sha256`
    `83b4830a7f39220f3581cee71adce28fb569b52a510cba71ebb986fb61321782`.

All seven leave-one-family-out variants of the 14,142-clause parent were
`AUDITED_SAT`, with a closed finalizer suite. Each row is a counterexample to
deleting that one whole family from this exact fixed parent. It proves no
global or member-level family necessity and is not a MUS, joint-deletion
theorem, one-minimality result, or semantic minimality proof.

The current core also does not yet establish complete weak-7 semantics or a
projection theorem from the original global encoding.

## Validation status

- Last recorded combined regression run (2026-08-26): 83/83 passed in
  243.466 seconds.
- Current qv2 regression gate: 75 passed, with one Windows-only symlink
  capability test skipped; the exact-gap campaign runner self-test passed.
- Current qv3 endpoint, pair, remote-tool, fresh-replay, campaign, and
  independent-auditor gate: 94 passed, with two Windows-only symlink
  capability tests skipped; the campaign-runner and auditor self-tests passed.
  The earlier wider independent qv2/qv3 quality gate recorded 123 passes with
  two Windows symlink skips before the later focused runtime regressions.
- Sixteen changed source/test modules passed AST and compile checks.
- SAT rows were model-audited.
- Promoted UNSAT rows required an AE proof, independent checker acceptance,
  and successful finalization.

## Qlt fixed-q continuation update (2026-08-28)

- The cumulative create-only `prefix[3]` closes qv2/qv3 at 532/532 negative
  pairs and opens only qv4.  Its file/semantic/gate SHA-256 values are
  `4a6c819191c1b9f45a7a7cc7406b00bd6b28bc22577581bc1368a8e6aa2db530`,
  `e5d8a90cfa3fdd222eaf94e257b169d6be23f00e4292ae6682c0be0ec61ce70a`,
  and `6a492f88010daa4df7b96cd721e071b85f6fb5cdf55672f52fef466e8dd60e87`.
- qv4 endpoint sources `v=8..24` are 17/17 independently proof-checked UNSAT,
  zero SAT, zero UNKNOWN.  Endpoint-final file/semantic SHA-256 values are
  `985341301cbe1cba0a2ddf555c1cf804118628bc2052ad2f5ab5059b8dac1de8`
  and `4cdd580f6d722914d2921d22f2ec68724f170e64e555a64ea8268f61fcbb876b`.
  This makes all 459 qv4 pair rows endpoint-derived and leaves no direct solve
  complement.
- The first generic pair attempt was deliberately interrupted with exit 130
  after 7/51 shards and 98/459 rows when review found a base-vs-overlay package
  initializer mismatch and a missing shared-lock `suite_sha256`.  It has no
  summary or aggregate and is rejected from every prefix gate; its partial
  tree and old runtime remain preserved.
- The repaired `contract_v2` runner/auditor passed 126 combined tests, with
  three Windows-only symlink skips.  The new attempt-00 seal binds 29 runtime
  files, has file SHA-256
  `208467fc7adf3b2fce33b4e8631bc24c7622299ffab76fe26e0a4263f5e9863a`
  and semantic SHA-256
  `6beb5c1407408b675de30ea029644e949858f39efc9dd7597eb3efb99bd21392`.
  Its run completed with exit 0, no lock/partial residue, and 51/51 shards,
  459/459 negative rows, zero SAT/UNKNOWN, 459 derived rows, and zero direct
  rows.  The aggregate file/semantic SHA-256 values are
  `763add5208c8816171f436eac48d896117ad2aa8215d69f849ef705eb43c58bb`
  and `68cd23dd56eb97e542d608b70bdd2b5bae10fdc28891ffc8dfced09f4ca51821`.
- The independent qv4 acceptance audit replayed 193 files and 1,996,483,727
  bytes, accepted `qv4_qw1_to_3_partitions_excluded`, and has file/semantic
  SHA-256 values
  `bf1ff1d1ca25e487747fa5267c9120e142f834ec0d3018a0410e900620a60a10`
  and `609ee9fa28cfc654da91ab8502173ec659a97af2661aafbb1586d3898191845a`.
- Create-only `prefix[4]` now closes qv2..qv4 at 991/991 negative pairs.  Its
  file/semantic/gate SHA-256 values are
  `ffb51c8b0224bd18a4d87c615c9678786266b18bd5ea7b5d47656d476b3f5c62`,
  `6e64971815c65de515e33b6105a375195acca411a417459fd53f1b386e6cc3aa`,
  and `87042fe487190588ffaa95140df835cd550cf984bce6ae372451df19583cea01`.
  It does not exclude Qlt and opens only qv5.
- qv5 is now independently accepted complete all-negative.  All 16 endpoint
  sources `v=9..24` are proof-checked UNSAT, so all 544 fixed pairs across
  64 canonical `(q_w,exact_gap)` shards are endpoint-derived; direct=0,
  SAT=0, and UNKNOWN=0.  Endpoint-final file/semantic SHA-256 values are
  `bd8797622878cd333e4b8e835d7f321b92e9970d31cfbb9f0fca07e5cf288dac`
  and `1c4dbb03d52357c29cd54a684e617077a474eff3b4ab4d3105288fc4702d8669`.
  Pair seal file/semantic values are
  `37279362d8ca234f7ab8e8737421caed289876b287c411b5f10f1ea0a4750742`
  and `f12d24ec87b8c61f38ee0b250366176ec03b791593207d51e43af640bb48bd0d`;
  progress file/semantic values are
  `17462a228b8289f4d11c576abbe8f99bfceca0baa20a8fc427ec368c15f905f0`
  and `332b0dd8201ce321cecd39038607bb74e3d3cab81e7031fea259bbdbc1d9dea8`.
  Summary file/semantic values are
  `d2fb0e1d33005a70aee9f9ddad256a7d7984b783874027413e048acc11942a91`
  and `f06cc27d3ce2a8e606c78bff8242e5cf7ac099d326e0ef43dae3507adce9ff3f`;
  aggregate file/semantic values are
  `fbc6432ceb515e3f959aabe57285835f96f49373eb410978f33f5e7c5a345c0b`
  and `e28877800c8ac5be2c11e8e12e39b18ce6d523fd55b4614d31140eac1faace6e`.
  The independent audit accepted 200 files totalling 1,569,177,106 bytes and
  has file/semantic SHA-256 values
  `4eeb22dd1715798d01fc4daf22453a9821bb3bcd24c1f0d70dce80f68b914e92`
  and `cbbac71646a7ca070add3c2820e64522dcbe328b22c7a3e793561b4347dbe42d`.
  Create-only `prefix[5]` closes qv2..qv5 at 1535/1535 negative pairs and
  opens only qv6; its file/semantic/gate SHA-256 values are
  `83097cb379a3d0e14a407a80609ae9e2723c3ca5f926fcd4ba6682e8c6cf18e4`,
  `14128e7c5a57f6f002a42f0aa5abf632b39f6aba61ff5d19621864ebf77cdab1`,
  and `bc874239d9f9582888333992d7a7f3965d2ef39171608579e16461d092be1da2`.
- qv6 is likewise independently accepted complete all-negative.  Its 15/15
  endpoint sources are proof-checked UNSAT, deriving all 600 pairs across 75
  shards with direct=0, SAT=0, and UNKNOWN=0.  Endpoint-final file/semantic
  SHA-256 values are
  `0d6ff97a8a0de53feb36672974692c6d5de0c9da2b3604f58331b4a6e5084aea`
  and `df9229f8ec213f872653db2fd257f590cdbb6b7450de192dd58f8c7307b11152`.
  Pair seal file/semantic values are
  `bd8af41bb13fd0f54518c401bd8aff2b96f81f85f0f529ab756b4d3a53c6ad73`
  and `d450f8810694e671157609a2208d992560a10206173219f7f4a5e0466c26d940`;
  terminal progress file/semantic values are
  `021028a440be01c7671da03b9a7789b887ca3741db56491af9b1356d17fecc1c`
  and `eb1fc8f6879e617675762ddc7a8db140ff693a60e7a4a5ed4515365aa6c72e6d`.
  Summary file/semantic values are
  `258ab42d01a6694c70ccd0f47fb997bf1a088cbbbb2f83dac1546808907a2dda`
  and `bbfb6dddcff4f73ff331d359193e77ed966829ec714c54820de903de59aa212a`;
  aggregate file/semantic values are
  `b552222a58bace2d6fbe74af12cfebdac9e60dd04d3fbe5f481034ca4a181f48`
  and `d5b75187f55e371b1692125507955ec33b1d0c16f7ab053618371e37a2456b3c`.
  The independent audit accepted 205 files totalling 1,306,196,854 bytes and
  has file/semantic values
  `978fc133ae9bbc3f63cd9eae9ede3de634961a01cfac691f2a5eedd6381c152f`
  and `24540145298563b38478b9c5dd737035af033d21fd69b2537b6635c78b9daaa0`.
  Create-only `prefix[6]` closes qv2..qv6 at 2135/2135 negative pairs and
  opens only qv7; its file/semantic/gate SHA-256 values are
  `c2a6c2f81a12c237860971b7523c5ef38eb087c5d6347001c9f47acadbd334fc`,
  `fc269be871c77b3e2e7844440746bbcbe4395b777a154f2bc33b34ad293c1cb1`,
  and `bec4efa5ad78b3cde55bb54a6e07ca6e27a8edcde14e79f7cf20d98473261570`.
- qv7 endpoint generation, proof checking, finalization, and pair execution are
  complete.  All 14 endpoint sources are proof-checked UNSAT, and all 630
  pairs across 84 shards are endpoint-derived negative rows; direct=0, SAT=0,
  and UNKNOWN=0.  Endpoint-final file/semantic SHA-256 values are
  `833fd9fda25e17b5db2f589b58c67a864ad2f8c39d167eac007b9af97b7ed133`
  and `5daabb28600df4084f85d9fd1c894557b5a929eeae4a656d9136ab3bb6db0bcf`.
  Pair seal file/semantic values are
  `5620998b3d3d780849ca388a2501a0e5c58cf015ca12a9f384263d2127cf78d2`
  and `0ea609eeea0764aaeeac40491f4b085be9d1b135f180a0d71ae0200ccab2af1d`;
  terminal progress file/semantic values are
  `6be0428ae5b4cf922f63a783548f4f24efc9af382c64fff758aa0b8442a2cd9d`
  and `6217b3a23d37e43c5e475e813f7758c62867b8edb7d6134873e2c12d658ea0f8`.
  Summary file/semantic values are
  `8e8a12926309b8518762d58a5b209cd151a76cf188e6dcc1508c052c7a6842a9`
  and `11519ea6b01c21146fabffdc7f60a9a9da573825c9c9804372c786bc31ea1a0f`;
  aggregate file/semantic values are
  `eefad84d1cdc81a23f58f9b26492fbfda41b96329e610c2723445936b8fdcd81`
  and `9604b3e79aced8b9320090fee533024db3d60bb05f248c47a16fd350670874ab`.
  The independent audit accepted all 84 shards and 630 rows, 208 byte-bound
  files totalling 1,184,823,807 bytes, and 14 unique endpoint proofs.  Its
  file/semantic SHA-256 values are
  `9f8754a1cc2611976c818c7d55e66e256dd2b8a062a24589bbf359703d080aae`
  and `c97aa21a3b8b14bfa8bebf05b649766efc81aabad1273bebeff594c616a15ab7`.
  Create-only `prefix[7]` closes qv2..qv7 at 2765/2765 negative pairs and
  opens only qv8; its file/semantic/gate SHA-256 values are
  `23f6c723a4eb3ab40d0193e4ef888e8bc3284b4855cca1dda407b34f22c996b4`,
  `19c6f0898e5802d848f0b3b381040fe972b5dab1b926662032951daf448d4f9d`,
  and `f0853d29054bd1a5b37f05f81e26e88bc39451a4e89164b66fad433024f46797`.
- At the user's requested pause boundary, one SIGINT was sent only to the
  parent controller while qv7 pair-run stage 5 was active.  The controller
  deferred it until the child returned 0, fsynced and validated all terminal
  artifacts, and wrote a successful stage receipt with
  `interrupted_signals=[2]`.  Receipt file/semantic SHA-256 values are
  `c351daa2a875a18a891b25acedbc26d3ce56995b76e9015ed8c71566ef12da45`
  and `058864df6425fa209e5bc9bf52530474f351d9aae383b32f1b23bc5df59833f9`.
  At that pause, the controller/launcher/child had exited, both evidence locks
  were unheld, all partial counts were zero, and qv7 audit, `prefix[7]`, and
  every qv8 artifact were absent.  The top-level launcher exit was the expected
  deferred pause value 1, not a qv7 pair failure.
- The independently reviewed qv5-to-qv20 serial controller (file SHA-256
  `354de6e59ef040cb5053f02d9b99a0d2114d947783922915a3b5e0d101ac7e3b`)
  resumed on 2026-08-31 from a new create-only launcher with SHA-256
  `2a8edcb55531a515675c9bf246e8dbe01234e9bc78162088b88bfe767dbfefd8`.
  It replay-validated all 19 retained qv5..qv7-stage5 receipts, completed qv7
  audit/prefix, and entered qv8 only through the accepted next gate.  Its
  immutable runtime registry SHA-256 remains
  `20556331cfa304ffd607af93ad3ed96886663f195bd48aad87e8cad385f0ed28`;
  it enforces endpoint, pair, audit, and prefix gates separately at every q.
- qv8 is complete and independently accepted.  All 13 endpoint sources are
  proof-checked UNSAT, so all 637 pairs across 91 shards are same-v derived;
  direct=0, SAT=0, and UNKNOWN=0.  Endpoint-final file/semantic values are
  `99683a7842798773a59c68256ec3b9688f0a80ecc0e6aad28fd8a560aaeb2807`
  and `484baba54280fc5de753a98b1d4bb5376d174b460e21e22262fd3e2fe23f93d1`.
  Pair seal file/semantic values are
  `b919e6d1d1a4fe75a8b09f74cb46688c111b50413eb0ffba19db06ba45df3939`
  and `913053b3865bba6b8e5ac9dfcebc1ead7509d0b3266f41f4f3c43c8202a02031`;
  terminal progress file/semantic values are
  `e0d390bd92185e44d5c8198a421a731f6f1a9e2f7e9723b1eef26a22864fce09`
  and `7ea55d36b22445bbb309e2f28b40c32c735c0efc0ffdec79032ff360bddbf03c`.
  Summary file/semantic values are
  `8239eeff638ab52da56ec4d3af3b0bca3d24e35462ce9e04c20d8d721d866f8d`
  and `dad9c2866f009825586e9b5fdbadc4aff541749409b089f425369918e0f332db`;
  aggregate file/semantic values are
  `a1b35ebbff7739f900a1e77cdadcad57de963bc272cb53789ecade7f1f46314f`
  and `81a4662d144ecd803bd541f647207a99ddf08808e747e2a173ec458da009de9b`.
  The independent audit accepted 209 files totalling 1,081,953,003 bytes and
  13 unique endpoint proofs; its file/semantic values are
  `5bacea87b28187e666327f0fe366f78cae92c40cc911970b68ae1b36b1ddee4e`
  and `15abe9d7aad15522ca4f500527895a34223c3f6bd4dc0249e3f6041834054056`.
  Create-only `prefix[8]` closes qv2..qv8 at 3402/3402 negative pairs and
  opens only qv9; its file/semantic/gate SHA-256 values are
  `df15d17f13c3811933822a5071f88a62d7948fdad1b1c17a336180034cff44b1`,
  `11a15e7af55598c2daf992c2ea6d9537c9091e05ac23995b8e7a4630215476d4`,
  and `11869b1d2857adda248487dbcfef0955bb0e26b46d5347f6122fc152bcee609a`.
- qv9 is complete and independently accepted.  All 12 endpoint sources are
  proof-checked UNSAT, and all 624/624 pairs across 96 shards are same-v
  derived; direct=0, SAT=0, and UNKNOWN=0.  Endpoint-final file/semantic
  SHA-256 values are
  `6bba300806fb760f13f458ac9d33dd592df948325f571e1daa7706d1d276b543`
  and `ac0d1a566e97c11729b858b2a4ea2dbf28fa01e0b3b2726aabcb25498abfd640`.
  Pair-seal file/semantic values are
  `93b117358e8caf1d3d94867bc54b36bc4989d1506fa963edc4d2712deb4c1f93`
  and `fd6f469d5237cec8746404209a296e8b397aba3b45008944ae299c79491c7811`;
  summary file/semantic values are
  `4fcdc0313531019a2ecb4881950ada9225b016d9ca98e24a9925eb0923d4d122`
  and `760f3bdef9066e8c7b7992a8246071711d4197f3acca04cf729767eb20ab3e27`;
  aggregate file/semantic values are
  `2b6291e4a727d301981b213667373fbf4d5ea452da59c84739dfd1efbab03f83`
  and `83378a8caf496315856ddc3d248e5c5b6604dbe48379a391da4a122e54e21115`.
  The successful stage-5 receipt has file/semantic values
  `b6d22a636987e56637b15f6f3a0682c52be808edc2acb6a9b74b77599310e43f`
  and `939b57a5c7dd0d83a7f56e579737e96e3a82528578d0bef07515bce2a20fbe0f`.
  The independent audit accepted the complete qv9 pair campaign; its
  file/semantic values are
  `ca06fb32e99700e87ba85fe93177eef08099d83fbcb8082c04d3e567ad81c602`
  and `c7ab11042a6faecad0adb8ef92fe3f9e57198fd74985378e3cba1694e920c16f`,
  while the stage-6 receipt file/semantic values are
  `ed50eb85c56e9e12e70c80d4f5f1a0ad676a5fe5667448954ce0efb0b4e11eb0`
  and `d56001beff99cc660d9479c2d741db3fdda0d196c8a214e95ec358cb69b791d1`.
  Create-only `prefix[9]` closes qv2..qv9 at 4026/4026 negative pairs with
  `closed_fixed_q_order=[2..9]`, `next_fixed_q=10`, and
  `qlt_excluded=false`; its file/semantic values are
  `9ec843253dce3456cc188ca774453f18233d9aea9851784df868b087ca31e011`
  and `feb3a1c34b701350d44af43475a63c347b28b02823cfb363fa733e7f43138140`.
  The stage-7 receipt file/semantic values are
  `663cccbe12d9b1003f241e6c5cbcbdcd179ed5d44b3e867e30362c4edc6c3830`
  and `33a0cd28fbf797b30c65860677d77a066415dbe2c5a04e1cf252886a71ff1b87`;
  only after this prefix was accepted did the controller open qv10.
- qv10 is complete and independently accepted.  All 11 endpoint sources are
  proof-checked UNSAT, and all 594/594 negative pairs across 99/99 shards are
  same-v derived; direct=0, SAT=0, UNKNOWN=0, and open=0.  Endpoint-final
  file/semantic SHA-256 values are
  `493ee12e41dfb81e127d52be0062113c09eee7ab497276a3803c2c76dbcc48ec`
  and `8a1e41b6070e78dff833014e6aff63422d4d3580227fd41430db5ed250a58efd`.
  Pair-seal file/semantic values are
  `2eb98884c6cf7d221180e45f1fba884c620bdecac697055c9043acbd04698878`
  and `4a2b74eef20b95a4bc57ec6840fcd1f16a54216db451b9f2e188a2c68ecb5827`;
  summary file/semantic values are
  `26fbcb84f3f608fbf5cfdc09aaf14ab44ad02367271eff16d69e88efdca74567`
  and `acd8ddbc223ba8db1823deb21c7ae269a01ede62fb6e678f56cd558e44eaf0d4`;
  aggregate file/semantic values are
  `b7c771c1e52b6dc9bfdad1fcd1a49933df9fee0faeac60f3ba2f266a1a65120f`
  and `9e09a3ba3cf47de37c28fdc23e6e2b09e4b13817a195d6acc9b7acf771501550`.
  The successful stage-5 receipt has file/semantic values
  `e76407bf732d6d2d31f2215fd25117dfdde3ee240d936a271bf2433ca0e7df57`
  and `b21f9f951103f495a1e0fc1b7087664d62ed4b44e567c7c890831f9a29ad4d89`.
  The independent audit accepted the complete qv10 pair campaign; its
  file/semantic values are
  `dd1ae02d655b473f63a50fe3da6d0b3ee0cc569586610e5ea4dcb30702c81b86`
  and `7a1dd0cff48f36ad4f5a226dbf24a7e3f94355745196db42d19de730ba69f89c`,
  while the stage-6 receipt file/semantic values are
  `8ebe32c81e38d00d2aad7e46f3fe2700324311d24f5c5520ce8119eb5d2188d6`
  and `c9c0fab259968d7175143d674a62af8f0844f887ead758bb5ca9f7d27b1a4bc5`.
  Create-only `prefix[10]` closes qv2..qv10 at 4620/4620 negative pairs with
  `closed_fixed_q_order=[2..10]`, `next_fixed_q=11`, and
  `qlt_excluded=false`; its file/semantic values are
  `8fb092d385636a4b0dce66460d6b48ab1abdc3b4c2a20085795e3ae971bda10d`
  and `290e4d93d43192cd1d2f075a95e4706f6cebaf7ad80dc41ec15d79368fbc7e55`.
  The stage-7 receipt file/semantic values are
  `e4ae0e11358fbffcf359478342c6e23f97a410fc7cc725a3526babefd87a0ba0`
  and `4c211c003eff464a889820ff5df40099c72884acf51517ab56acaf8592f78168`;
  only after this prefix was accepted did the controller enter qv11 stage 2.
- qv11 is complete and independently accepted.  All 10 endpoint sources are
  proof-checked UNSAT, and all 550/550 negative pairs across 100/100 shards are
  same-v derived; direct=0, SAT=0, UNKNOWN=0, and open=0.  Endpoint-final
  file/semantic SHA-256 values are
  `3b8cd14907e64e67ae6f6515f406ce79bc2b6cbd8bead560a015e43aea73535c`
  and `103749cc4cd29683ab38536b60d7798652edf36944b1c18adb04e74b4438fa9e`.
  Pair-seal file/semantic values are
  `d91ca77407af52a41e9ddc05c8245d02bc4c11c86acfaff25703b4ca5eb1f9ab`
  and `89de03b7d563d99f2d8cc81a4d198d85c636ac3e4fcd173514c63cc62930f086`;
  summary file/semantic values are
  `e4402fa5877e15589429ebe6e993e2bd71b71c71c59841a0f89f8ea99916511d`
  and `562a681964200dca92620067917f35e10589b7131c87497eb39b23d2d86d4c60`;
  aggregate file/semantic values are
  `f7b243867d7eaaacd67d65b609ac7152435fb525905c5b34dfdca8625860049a`
  and `2ecde0026ef02e92e67ba4ed55136561383fb4f654246beed7fec485ef24245e`.
  The successful stage-5 receipt has file/semantic values
  `26115d1ae123cb753f518659a0afe6c114a978179dc47d9ca4b130a46ab69392`
  and `e57c29490745d8d4e91c29d42d9e38423f369185e0276c5426df7ba72c79682b`.
  The independent audit accepted the complete qv11 pair campaign; its
  file/semantic values are
  `db0c2ae384fc582d4075b5daa504ff8209781ee8ca12ae1734738653babb4510`
  and `f34c5d98953eb2aabbeaaaab7e34158882319906deec2dac81b7577d04742898`,
  while the stage-6 receipt file/semantic values are
  `39c19381ee5ea2531a67ba16d9a35edd85559ac365389498009eeb20fd716ed6`
  and `35f4a2f31929eeb55bfc31fb39933a5e606172c558b6ce40d4c2542c481cfd34`.
  Create-only `prefix[11]` closes qv2..qv11 at 5170/5170 negative pairs with
  `closed_fixed_q_order=[2..11]`, `next_fixed_q=12`, and
  `qlt_excluded=false`; its file/semantic values are
  `9770bab4b45d66ed21b465aa62002fcf11b4969ef19d2197e62a967e0cb49bb1`
  and `3668319996c1eba9256d58312610ba73bbf585bc2388e038962852401e894cf8`.
  The stage-7 receipt file/semantic values are
  `d8d033857d12a7ca4ed738e5ad75f3525267e21cd8c7d9915ba463adedf93f2d`
  and `a141a6cc78276021ba74b773e359fae161d312fe9649490c06bb872b00630ec0`;
  only after this prefix was accepted did the controller enter qv12.
- qv12 is complete and independently accepted.  All 9 endpoint sources are
  proof-checked UNSAT, and all 495/495 canonical negative pairs across 99/99
  shards are same-v derived; direct=0, SAT=0, UNKNOWN=0, and open=0.
  Endpoint-final file/semantic SHA-256 values are
  `b99df1741f43a9cccb25b6f8f9600a754a11450586c5ac02109c218dd49c3220`
  and `07ed23299ebf377cf344bf9882cc6e0302799765a43599e397ece4a3f16c2929`.
  Pair-seal file/semantic values are
  `482276c1c0805becdf82f3ca657202af72bd43b33f866cd541d41c5f33a0b15b`
  and `2180fdf97e2a1e825f4e6e70b2bf806a0739152fca6c06dc287dfec32f48b15f`;
  summary file/semantic values are
  `2b7cf2d7c3cf20650081f3c1106954e9032983607203d9adec8b566fd393542a`
  and `9bb80a000474876701949d64507d97dfda5e8d42052fea83d00947e56b7cc431`;
  aggregate file/semantic values are
  `bc8e79ee77086b6d81b528d8770d7a7412a6b2c6bccb898a5ae13fbf5aa4881b`
  and `2dd4cf93f36d30750db78bc24ae2d3927cbf26957a6519a27f86d0f674fa703e`.
  The successful stage-5 receipt has file/semantic values
  `0976a148faacae8a472ead17c06b59bf5ca1c9ec3ff394101ac1a416a94f2fe8`
  and `8e4c13507f1f1cd7800fe5a2e9d3b06099002f1ad230037762cb6677f1166f8f`.
  The independent audit accepted the complete qv12 pair campaign; its
  file/semantic values are
  `ebb9aa449994e23bd07d9e317c5311f9e3fe44b4b7fa53a7a5c749ecd117fcf6`
  and `b08fdede6f53bddd897c6312ab19972a1b47260317e4cc68f208d0f324f191b4`,
  while the stage-6 receipt file/semantic values are
  `eb0ab0cd1fed00db9ec5bf940b350fcec61d253b2c7c816d7426b4aa5dbe891f`
  and `2d8a33b334330e61767da5db91470569fae75ce495c0bbf42897b462314867ba`.
  Create-only `prefix[12]` closes qv2..qv12 at 5665/5665 negative pairs with
  `closed_fixed_q_order=[2..12]`, `next_fixed_q=13`, and
  `qlt_excluded=false`; its file/semantic values are
  `0da85881406d6abed19d8893299155b23026827eed358194b8aa00f7e3821cba`
  and `1e64432d1ad60282e56fd0d79b5e4828e711aba07ce913bead221312396efe7e`.
  The stage-7 receipt file/semantic values are
  `861cfa327ed1938449b519903ad87264dba327777455ed76cc9bfcc3e03d6b81`
  and `e879391a6edd84e75addef8c129eb43022e8849b90c3ce3ec80a0e7da0755f00`;
  only after this prefix was accepted did the controller enter qv13.
- qv13 is complete and independently accepted.  All 8 endpoint sources are
  proof-checked UNSAT, and all 432/432 canonical negative pairs across 96/96
  shards are same-v derived; direct=0, SAT=0, UNKNOWN=0, and open=0.
  Endpoint-final file/semantic SHA-256 values are
  `e45fa797043b5cfd296e36912e483983665741393c06a4e2e3f0341a65e3f57d`
  and `a99eccddc3857fa9e762981a260b9bbf9c49db6d7aa11a1e60f3ca538bd8af7c`.
  Pair-seal file/semantic values are
  `b26e86751a51199ba01d364539aaa2b1066006744ca441ea365f0af428a8b903`
  and `8a0a08bd78932c4db3baaa784ef963d049fb7f9d1715b0db799376ba0bca37ae`;
  summary file/semantic values are
  `5c28d705831a2d23fe513f59e877141560ddb9ad2603bd8d6a592af6225fa64c`
  and `f113622bb37e0dcdee40d99100e28cffcb61e68655d8ba9d1109f1baba81b69e`;
  aggregate file/semantic values are
  `f100573d841642838323ac752917cdc3876dc510aac0752498e3ccd1f84fd866`
  and `01d20f93e15c6c0cdff77abbe5ae255dc36a4900df23d7918e863fe9556818b6`.
  The successful stage-5 receipt has file/semantic values
  `4e503082c65aa6415d1588415bff97c4e8e2200e9246f4c918d02942fb739f96`
  and `dc7f16874f07354b7831e3d23756a0bcb5f429bf5afc4823224492947b790a66`.
  The independent audit accepted the complete qv13 pair campaign; its
  file/semantic values are
  `99c571d93748d56f026aa24ab5cdf225a7ed6a9f821bb978333bae8cb04e8149`
  and `c3316fc38056bad67365f9ebc42160cf8676abca2f2eb5f9be11c5bb662f7ca2`,
  while the stage-6 receipt file/semantic values are
  `e4d10d67d129ec9ca35e393e263a2de78bda316890e990bf4784bbfa154e18a1`
  and `4090c6f70b3211ebfc204853d804d95a8b467238ac39ffaf8ae2e17fa4844ff1`.
  Create-only `prefix[13]` closes qv2..qv13 at 6097/6097 negative pairs with
  `closed_fixed_q_order=[2..13]`, `next_fixed_q=14`, and
  `qlt_excluded=false`; its file/semantic values are
  `4006db64cec65b4bdc86de7785f2b6b2b9c014383f30f1d5f63bc61492122f38`
  and `fd1e1fd09c98e07787def66fd795eabbba5a9be9ad32ebacb523d43ff917f4eb`.
  The stage-7 receipt file/semantic values are
  `01abce4fd9bbdee42c18c1f2bca22fcd1b526755fcf914374b8dbc094818ff67`
  and `177c2f8034ef1ad92a5f20bde0821309f4569b8c0d29c47ec69e23e585d50ef4`;
  only after this prefix was accepted did the controller enter qv14.
- qv14 is complete and independently accepted.  All 7 endpoint sources are
  proof-checked UNSAT, and all 364/364 canonical negative pairs across 91/91
  shards are same-v derived; direct=0, SAT=0, UNKNOWN=0, and open=0.
  Endpoint-final file/semantic SHA-256 values are
  `092ab22d19c82ae70173fb57cb0c0725f7f99028e25fe69a23c6bdfd3f0c629c`
  and `36fb049bb809e926fc3e55664dd23b9f7dff3b0264fd28ad26033f3d46d43edd`.
  Pair-seal file/semantic values are
  `a91777b580193e69f284baf8433c00c36806c89ae77e994733795339b4ee6b4c`
  and `774963603449d361bbbd7067fd6eb54e37e0588fceb432fbf9ceceb270afd813`;
  summary file/semantic values are
  `114300fd5b205896d6502a4de987a1ed1c5235b92df4911a0c5f301bf5689a34`
  and `c11d3a09eded4e1d0fb171c04b3fdbef891bb156f904e67c818380c267a928f3`;
  aggregate file/semantic values are
  `e069645f1d736ed1e0c64b04a49bc7ba04649243887721aea7913d3cb21d543f`
  and `a8987a5eeeb00ba4c728b71f0203f6ce10c192b5309975df69cdbb6624e4f963`.
  The successful stage-5 receipt has file/semantic values
  `4aad40aa7d4232adf007e19361d6bd3e6d993610447050569e9a8f5386d32358`
  and `197c38f170f7fc39bcbcf8afec7540deb8f85c1252e17d68741d5390168b2129`.
  The independent audit accepted the complete qv14 pair campaign; its
  file/semantic values are
  `f4aac53869df48d3b037aaf81bb6780144e0ba39b200750f77afc745fe2eca30`
  and `f8f319ac5e6ea85b6bc9de62fe64f267b6ee417f3a410b3c4ca4302cb9d692fd`,
  while the stage-6 receipt file/semantic values are
  `5ece864e0db66f8cb49b12bc1f0a89ffd3ef8c1bb0edfe0eeee26c1edd0dbfe3`
  and `6204b4b3496e5e5a3aee56678ff0073648bd42793aeb172f6a2ee357cbf731c3`.
  Create-only `prefix[14]` closes qv2..qv14 at 6461/6461 negative pairs with
  `closed_fixed_q_order=[2..14]`, `next_fixed_q=15`, and
  `qlt_excluded=false`; its file/semantic values are
  `964ac84ad2ab0b609a9be3c01f42f7fd8d63aa0e0bcccc74418919982bc1f842`
  and `e7b17baa33ffa6063bc03901b8c355bc0592a46ba612d56bd3f739923d4d3085`.
  The stage-7 receipt file/semantic values are
  `384628e9c6e625abc5f95b34853c9d887c968abd20b731975b0d9bf0ab4d67f3`
  and `bdc8144ef0964854b2d2f732248684dd675eae289821fd70c3a1a46c13692a76`;
  only after this prefix was accepted did the controller enter qv15.
- qv15 is complete and independently accepted.  All 6 endpoint sources are
  proof-checked UNSAT, and all 294/294 canonical negative pairs across 84/84
  shards are same-v derived; direct=0, SAT=0, UNKNOWN=0, and open=0.
  Endpoint-final file/semantic SHA-256 values are
  `3cbc323e9156bc1852dc4d5c270f7c3b4b6d250dedd712fe3a345f17193fa25c`
  and `44eee3d46a5fa1b77dfb8831cb10d83c6e728b9f45fde0b29844ec33930ef2bb`.
  Pair-seal file/semantic values are
  `34adf0ae0384c38e17607ee436c9238413f664da2f2173e99e91112a037daebb`
  and `9d1a555e124ec9e3df3452c29134eb4f2a2f7b50ab13213b23c14a91ddbf0b2c`;
  summary file/semantic values are
  `06dc2eae6a95ba836a552e2f900bd749ed10b88d58c8846ee09a204cf4a3052f`
  and `98ec5f117e1fbf403fb08c694c28df867904160717494c2ce082f220cf456d92`;
  aggregate file/semantic values are
  `87a43ab0ac023c40ea79d9078eca86138e41e3ff6b90d91e0149d8da1b10efe5`
  and `09b66ba40f3625051f195aece398152a123988515dc93e981fb40da5838b13a8`.
  The successful stage-5 receipt has file/semantic values
  `62ddb41850ba2fca56537fe71c300cd92245d6a1dca7b4d88f5629a4fe9bb50a`
  and `6f7fe09d0407295f31cb60bdaf6e496f2aa28a5f73740c319c188dafee0aff12`.
  The independent audit accepted the complete qv15 pair campaign; its
  file/semantic values are
  `33ba84fbdfe5bb0b6676719e00393baf6da03c282d7b405c9f90d9b3130a5a75`
  and `75223f1aa1c49bb749756ce90873d30d5291b1f2ca76c1270eaf190b5719d4e0`,
  while the stage-6 receipt file/semantic values are
  `8b8f5fc46ab0d98f6cc41811a4de3f1213959530eb0e9d7c7a1a6a54845c3feb`
  and `5657dad6b954ff1047d65bb73c39c0c367d1c1a6fa6df9846ae7d5e9fa7fbc4b`.
  Create-only `prefix[15]` closes qv2..qv15 at 6755/6755 negative pairs with
  `closed_fixed_q_order=[2..15]`, `next_fixed_q=16`, and
  `qlt_excluded=false`; its file/semantic values are
  `3cef4d06bc172827a874395745a23f50aa0ac72c4d566e67fc1219099fb8dfc6`
  and `27692a6e6c873722ad874e7a5f6773d53746430171332befa5422a21644b7d5d`.
  The stage-7 receipt file/semantic values are
  `882bc2376c105a7d5f0a11a4910f001e806725d8834fe41601f8eb287914f6df`
  and `d8b2497070d3bddeb97d365f0a3d5790e856211435c0b1cfc4bc4d13f06ad3e2`;
  only after this prefix was accepted did the controller enter qv16.
- qv16 is complete and independently accepted.  All 5 endpoint sources are
  proof-checked UNSAT, and all 225/225 canonical negative pairs across 75/75
  shards are same-v derived; direct=0, SAT=0, UNKNOWN=0, and open=0.
  Endpoint-final file/semantic SHA-256 values are
  `f84bb6d17e091efc046259bf4ab07c9b65e9f478d3e148bbf68d65f9c3d64fc4`
  and `2884971e69d6adcf36f7fd489c6d8674e4187d9003e384ffc6c6cd1694907587`.
  Pair-seal file/semantic values are
  `d9a9e97153c026391461ca06a6bb596f1e951cba3323a90f5ea526d209ea7cf9`
  and `bf00ca15c2aefce02218f6475b24469d4637595ed4f2d380c8ff96475353ca41`;
  summary file/semantic values are
  `54f9389198abeb19dbbd63204d22b02ce1417e953fd0884563a39dcde85c55fa`
  and `6aea4af49ebbb9afdf27149dc744c5e29958bb437d6c679f607c1395059339ac`;
  aggregate file/semantic values are
  `cede1fe8ed6422166ba665b4a9efbe41bcadf6625944b0e4a95ecc2bb76ae8ef`
  and `dcad04f6303911b5f3804b176b272d66b917ad981e8cb035dff246684d1049f8`.
  The successful stage-5 receipt has file/semantic values
  `c33c49f9474d62603b99c030bc8380555555ed7b86e1b0621215ef9e02b8a698`
  and `c81381a8a2bfdc3cb9c09a3081120671e2145448263802044208ef111fbb51d6`.
  The independent audit accepted the complete qv16 pair campaign; its
  file/semantic values are
  `994416ca5794fced36088faec3dcbe35698445574be02cb860afb967a3f89398`
  and `73d4f01feac6b01ad83d3c7ffcfd161af12e1e84f32beaf8477183b5941eea08`,
  while the stage-6 receipt file/semantic values are
  `98ef1e21b71ed2a7deac5504d423d3c611d96416f05b3c1e353da03fda983e29`
  and `43438eed20ca10b717903f1bfa886f449708e2cea12313c74b8af29b02656f36`.
  Create-only `prefix[16]` closes qv2..qv16 at 6980/6980 negative pairs with
  `closed_fixed_q_order=[2..16]`, `next_fixed_q=17`, and
  `qlt_excluded=false`; its file/semantic values are
  `2b563d21a224926fcc73fea81bea7100e6e9584d9962ba7c17d72d6761ad5c43`
  and `6085c592df5471787b0c96156090db61155b9b3ecf275475f24c9887529c0e30`.
  The stage-7 receipt file/semantic values are
  `fb3a2f41f050017316b1280c2449b11731a420fe1fddec3b62631bbf1bee1c06`
  and `73cbe7f0e0cf450e6814021cadeabf64114a8a0a0e154c574f501c70df34f43a`;
  only after this prefix was accepted did the controller enter qv17.  Thus the
  previously emphasized qv10..qv16 interval is now fully closed.
- qv17 is complete and independently accepted.  All 4 endpoint sources are
  proof-checked `VERIFIED_UNSAT`, and all 160/160 canonical negative pairs
  across 64/64 shards are same-v derived; direct=0, SAT=0, UNKNOWN=0, and
  open=0.  Endpoint-final file/semantic SHA-256 values are
  `f3328633c0dda0008f4b8a1f5df13c7498dd7b41db4aaa970fb7fb661200d8b0`
  and `f6edc73bc09a621d57440210283ff3d7e1404ad38c17c8863715e1a67e84a39d`.
  Pair-seal file/semantic values are
  `f2fd3b22826f997542b770129afe8c44116a42e61b87e82901b7245fdab53b9a`
  and `f02be6c6113ede9e577c72033aa05b13f3d80fc12b0d99dad9f888b1f300516e`;
  summary file/semantic values are
  `55e35065beaa12a54d02620a66752d34b6f6ee0af01ab91fd7d8712fe44db074`
  and `a9698a3c4671f14b8a0ac768f243532e66c80a03056679e4770f75dfdfcf56ff`;
  aggregate file/semantic values are
  `1a829f057fc1e5eb689cc0ba8091ef4a0c375c33b53b717e4fc8602c78dd938e`
  and `67483d1808d0a051db523025c127905ed1b4be90aaed1d7d2884b3a2aab86694`.
  The successful stage-5 receipt has file/semantic values
  `5568061d819badfbf7487b082165c81b9b8f171132cb6d3e8056ddde0a0b6b45`
  and `74980002a89e8d6038adc87720007e65de65e7c980634d4387ebd9642303ec88`.
  The independent audit accepted the complete qv17 pair campaign; its
  file/semantic values are
  `e55f70c6e5c127e7b686c1cdd7b5eb2ce08aefe2c408e5f4016edac73565791c`
  and `aefebcff9c6cec684ed16b498902ebd8e5eadc66d65347f256de74b297bd42d4`,
  while the stage-6 receipt file/semantic values are
  `1dd6fcace6557db8288cd8251627a760f5e34f9a94abfcede0e1d7d49af23e29`
  and `de8954bb56fe0971813de0fee15589bf062542b0c1cd178e29d1639eb815176f`.
  Create-only `prefix[17]` closes qv2..qv17 at 7140/7140 negative pairs with
  `closed_fixed_q_order=[2..17]`, `next_fixed_q=18`, and
  `qlt_excluded=false`; its file/semantic values are
  `cf364b8291a850a94f708eba86f2d9e05948bcaae3845ecd7ca5c07134c398cc`
  and `2dfffc495c162845819633c9d0e3875e13bb0fd9fdb14549d65301eec32fd9d5`.
  The stage-7 receipt file/semantic values are
  `d574706b8a0ad8f24ccbade337455a684758e33095029e234e73c4d731776777`
  and `3ef79add49948306655cda129c7110670a49e9af23336eb007b17f87ff1a516e`;
  only after this prefix was accepted did the controller enter qv18.
- qv18 is complete and independently accepted.  All 3 endpoint sources are
  proof-checked `VERIFIED_UNSAT`, and all 102/102 canonical negative pairs
  across 51/51 shards are same-v derived; direct=0, SAT=0, UNKNOWN=0, and
  open=0.  Endpoint-final file/semantic SHA-256 values are
  `19583c73ddec2b024d9843f3c6eb07c81f9080bed726b906c6c889f8a9fe0e3d`
  and `ed94441bbcdfd387be3ef0d50cb8ed896832d285f2a7b4c864f21eb0acd088d9`.
  Pair-seal file/semantic values are
  `1ae5507582a0faba70f5726b3b2665c37683ccbdf319aac3bc186d58e59df383`
  and `f335d247865a1b5ffd209c7cd9d928a8ba9be7c77e27da38b91569744150452b`;
  summary file/semantic values are
  `fd370757a883af1caf5e0125a81611ab717710ae8af333ad57948755893baa20`
  and `94bef3a38ca6b5a955dae23d67ee4ec17cb63375624e6a43f7c6a9deffd2152c`;
  aggregate file/semantic values are
  `a15420cb229eb99c9f50218700519b3fe7e29de69730ab76f930cdf4b6749697`
  and `8e1d1424b971422627986161e0fcfce177b09c25d4c24c7d5b9a85937ebe7be1`.
  The successful stage-5 receipt has file/semantic values
  `e67ca954c618d89b644b274f7b93a9af7ffa9b23cfd78ea31abfcac4746a8967`
  and `83ef2d619afd0741c1a5a2b5f62d00f89b562d8bf44e998e7fa0f662d2a3ef57`.
  The independent audit accepted the complete qv18 pair campaign and
  byte-verified 109 files totaling 202787724 bytes; its file/semantic values
  are `ee9d5c60a356769afbb20366a8391e9f1e0931dea6fbe5df916e8a34a46a1cb0`
  and `7e85cc2384f1822ad070617e7ae9bc6faf977887e0b9d9c49e6d6dbbae2df837`,
  while the stage-6 receipt file/semantic values are
  `0f9f2fb7c1372038ce87d9d854c3bff42cebaa80fd7113b78e2d030bc1af8099`
  and `cc5be07dad1512fea2aa29de9c92667a35f326cd31d14643705b1b66a74e54e5`.
  Create-only `prefix[18]` closes qv2..qv18 at 7242/7242 negative pairs with
  `closed_fixed_q_order=[2..18]`, `next_fixed_q=19`, and
  `qlt_excluded=false`; its file/semantic values are
  `a496417e97298bfbe4b2a37fb0661828cfcabaecd860d467ec84cfcee2b0b054`
  and `03cca18ef22b0755650c6ba8fb0003013645b220e049f735bd06f2d4ce1d972e`.
  The stage-7 receipt file/semantic values are
  `0d7da40c6c5d3c76608e22dd565efef005ce992b9d35a52076411e82903045ab`
  and `4042589e02ad12e969e3cf09beef0d6792cce954d59b2a8fde83fad541bb1172`;
  only after this prefix was accepted did the controller enter qv19.
- qv19 is complete and independently accepted.  Both endpoint sources are
  proof-checked `VERIFIED_UNSAT`, and all 54/54 canonical negative pairs
  across 36/36 shards are same-v derived; direct=0, SAT=0, UNKNOWN=0, and
  open=0.  Endpoint-final file/semantic SHA-256 values are
  `c702a2ef2e528b9c3c6522fede16d5d66dc937b476c8321369736d712b862821`
  and `1a45026c6676c1c118fa320f0e451d889cfe39a6490a535ddde78a8efd8ae409`.
  Pair-seal file/semantic values are
  `a41053202346be6b3bac2f90027aced3e4d774cd854f2f459e24adca43709870`
  and `fceb8315ef8e229bc459d014ac8f2c73c14eaaff2a662d4a25dc9165e202ed7e`;
  summary file/semantic values are
  `31c8d7d127020ddb964e2cb5b00a69610f3ba620626decf9264c552ea6261d96`
  and `8c4242f5ced74ba7b9844023270eab6ccdac2d1a0aad976d67dc0341a9abc0fb`;
  aggregate file/semantic values are
  `10f7f4da3844553685b0241c69c0a6286baae2c013b704590d6f293fd81cf5a6`
  and `adfb7b287a67b333edf776ac56225744bafebc6d2f67f0f574b1ccece131c743`.
  The successful stage-5 receipt has file/semantic values
  `819414b2771cd511bbb980ae3ebcea7521d896028ee9fe265dffb73c2b094f4c`
  and `6116cbb9d3b714cace2d75a7b39142cab724607c27c129955bd1be5b7d361efb`.
  The independent audit accepted the complete qv19 pair campaign and
  byte-verified 88 files totaling 114608172 bytes; its file/semantic values
  are `394a5290f98955295cff56381e5b39062522684dd31464adfc6c88a6f2ad4644`
  and `0a6c79f81e1b2b92ac016d9522a19628bd56b5561daf0e9836878c7e477bf842`,
  while the stage-6 receipt file/semantic values are
  `c9fe56fb098a0047b22b21a86e9b8bb3c6e2865bc8ee3afb2efa2b8d809825cf`
  and `b0470b5a3bd6070253682d47b51203176a09c07967d6624d37db6f2a12f878b3`.
  Create-only `prefix[19]` closes qv2..qv19 at 7296/7296 negative pairs with
  `closed_fixed_q_order=[2..19]`, `next_fixed_q=20`, and
  `qlt_excluded=false`; its file/semantic values are
  `29446a46ccf2e879b8545e5262adb77e6c260b303237f9c4cde616407c5f9a8e`
  and `23b03462dfd02331fd1b80c55c66ad2ea2ae1b417876eb4a6b70481d24c4b553`.
  The stage-7 receipt file/semantic values are
  `0a09c1b4269b269d0853577f32675154ec5bf056eabd37da7dc0182d0ca500b6`
  and `c1065b6c091e543e068d905b3a11497efa3b2e0b31c02cf4d693cf5aa4432701`;
  only after this prefix was accepted did the controller enter the final qv20
  partition.
- qv20 is complete and independently accepted.  Its sole endpoint source is
  proof-checked `VERIFIED_UNSAT`; all 19/19 canonical pairs across 19/19 shards
  are negative and same-v derived, with direct=0, SAT=0, UNKNOWN=0, and open=0.
  Endpoint-final file/semantic SHA-256 values are
  `93692e709a0c562ecf8a426cb18f432daa09cd2adfcda8c96ca5965d3ccd68ad`
  and `9b9e5707e66a497923aec5587ef569469802365505fea9a169681ff8cd623f79`.
  Pair-seal file/semantic values are
  `bf305ee20b593eb55d9b07f00a84d5ea28a400e576b5460e6f95357b6d0e3346`
  and `776bd6af63d2bdfb6d718fb20af93433c6548de2077011d0da5dcc6f1b4b8d49`;
  summary file/semantic values are
  `9b1eb4116b08dbd8a97cb37b0408e4f7a3b1048065ca04279728c3357fb55dd3`
  and `c1a1d591f3c3c8348a666321590f8bd74e7f295887b172345ec362be6bc1dd86`;
  aggregate file/semantic values are
  `3f8a916fac8c6fcd66b8b0279d96bbcef769c24bad622e9f9ff04da2c365ef7c`
  and `c28532cf1ce7317ef408b3a0f3b21f56d259770070aaa56a3a495d385562ad47`.
  The successful stage-5 receipt file/semantic values are
  `b4b709e088e9310674eaa00ffd5321658da6e8007461e834f201700d9c31f641`
  and `3bd933abf88aedb7ede1bf86497daa8a5e0bba0bc239c669e9ad429a21ee2204`.
  The independent audit accepted the complete qv20 pair campaign and
  byte-verified 65 files totaling 26485614 bytes; its file/semantic values are
  `1427015df81ba5f631e04c21b660a610de98d4561f69643f0197e961e48e5f65`
  and `3c2f3c46b8cbc4e794ee9e3f26e3d330c4ecba178b950828886159d3fc32a96c`,
  while the stage-6 receipt file/semantic values are
  `3bd5095fc2b887885c5b6c5dc2e9b21509c98b0823bbf27057fb00c4c348987b`
  and `49b6b09de30e84531e2d37e365dfa573688991fd054213606251249355b0e746`.
- Create-only `prefix[20]` closes all 7315/7315 canonical pairs negative with
  `closed_fixed_q_order=[2..20]`, `level_count=19`, `qlt_excluded=true`,
  `next_fixed_q=null`, and `next_gate=false` because the finite fixed-q range is
  complete.  Its theorem status is exactly
  `Qlt_excluded_by_fixed_qv2_to_qv20_partitions`, with theorem limit exactly
  `contiguous q_v=2..20 fixed-pair partitions exhaust the nonvacuous Qlt coordinate range`.
  Prefix file/semantic SHA-256 values are
  `fab29aa1408f31db1999af64b7841ac92d04480de099a591604ec346a0507f54`
  and `9663bd0916cbf5cb2cae4c533d62c3aa5fab6218ca1e736ba2f82b26eb863cc4`;
  stage-7 receipt file/semantic values are
  `b39292c8da0bb7dc0ac2fe5e97d6950301319393e05698e0d7340d19c6131fa3`
  and `ef017ca988c0b670f41754d42e645582ada8ebc4aeb93624382514a3ed9ad53b`.
- The serial controller finished with `status=complete_qlt_excluded` and
  7315/7315 negative pairs.  The `series_final` serialized/self SHA-256 values
  are `a7e54ace52d90cfd97666d5a33b51d6bec2c060a7e86a265169908ed8a6e4c8f`
  and `6f214674c0649b209fed93953005ba596dbe5142c758e12304281f6992b24d8a`.
  All 112/112 stage receipts match their live file and self hashes and report
  success with rc=0.  The resume launcher SHA-256 is
  `2a8edcb55531a515675c9bf246e8dbe01234e9bc78162088b88bfe767dbfefd8`;
  its exit file contains `0` and has SHA-256
  `9a271f2a916b0b6ee6cecb2426f0b3206ef074578be55d9bc94f6f3fe3ab86aa`,
  while its log has SHA-256
  `e3d0782346f4a0c0a607bd948cfc93b623bfe93c1c72c9780435484984eecc13`
  and a tail that binds both `series_final` and `prefix[20]`.  The earlier
  first-launcher exit 1 records only the requested safe deferred pause at qv7;
  the resume launcher exited 0 after completing qv7..qv20.  Controller and qv20
  processes have exited, and active locks, open lock file descriptors, and
  partial artifacts are all zero.
- No monolithic `Agt1` solve was launched.

## Transition-conditioned ordinary matrix (2026-09-01)

The strict-N25 `Qeq/Qgt x 25 ordinary states` campaign under the canonical
first-to-next predicate `P(v,w)` is complete and independently accepted.  Each
cell is exactly `P and mode and O[G]`, where `O[G]` is global ordinary-state
occupancy.  Both mode premises are nonvacuous audited SAT: the retained `Qeq`
anchor is `v=16,w=17,gap=1,q:1->1`, while the retained `Qgt` anchor is
`v=11,w=14,gap=3,q:1->2`.

| mode | SAT | verified UNSAT | UNKNOWN | forced missing | novel forced missing |
|---|---:|---:|---:|---|---|
| `Qeq` | 24 | 1 | 0 | `G410` | none |
| `Qgt` | 23 | 2 | 0 | `G410`, `G420` | `G420` |
| total | 47 | 3 | 0 | - | `G420` under `Qgt` |

The three direct proof/checker cells are `Qeq/G410`, `Qgt/G410`, and
`Qgt/G420`, with proof sizes 238038498, 221387597, and 473470540 bytes.  The
checker SHA-256 is
`2f01df83916c158d7da43deefde1ea3ea60b19f5d636ae03f31042e88ef179e9`.
In contrast, `Qeq/G420` is audited SAT with witness
`v=9,w=11,gap=2,q:1->1`; thus the new exclusion is genuinely conditioned on
the strict-increase mode, not on all nondecreasing transitions.

Let `H_Qgt := exists v,w [P(v,w) and q_w > q_v]`.  The accepted exact-cell
proofs establish, at strict N25 only,

`H_Qgt -> not O[G410] and not O[G420]`.

Since the two state tokens are distinct, every `H_Qgt` model globally omits at
least two distinct ordinary-state types.  This is the requested second charge
for the `Qgt` first-to-next pattern.  The matrix artifact itself did not package
these cells as a Hall evidence chain; the subsequent campaign recorded below
closes the strict-N25 `Qgt` two-slot Hall relation.  Neither artifact proves a
result for `Qeq`, an arbitrary exceptional pair, arbitrary N, or arbitrary
multiple exceptional occurrences.

The runner processed all 50 cells without early stop using 31 retained model
replays and 19 external solves, exited 0, and left no lock or partial/fresh
residue.  The independent receipt reports `accepted_fresh_replay`, byte-equal
fresh finalization, `qlt_evidence_mutated=false`,
`monolithic_Agt1_claim=false`, and `Hall_composition_claim=false`.  The last
field is a historical statement about the matrix receipt itself, not about the
later dedicated Hall campaign.

Key terminal hashes are:

- manifest file / suite:
  `90541f9155c257cfa3dcd99e9b17f9780e39d4b79ed5f5dec93182c2c074fde3` /
  `03a93ec3fad67aef3f8ac5291377d293911cc356754a486f1683f53ef3fa5fe5`;
- remote-run file:
  `9eaafb7a2de0f7777a7a5a613abe4258615b8ac8af7cd2dafe74530d7f74e7c2`;
- campaign-summary file / semantic:
  `da6142a8fa8f486b996f9bac3dc8bcded321cd1bf02ece99ab81a1c13b156409` /
  `713f7140c9824186ea8d255e340a75e8064384d3097b6804b37cb485ed1c0908`;
- matrix-final file / semantic:
  `5dabfc807ce0d8c7d7f87d7c70a6df3b18f1a0b6a10ba81bbb8889c8247a5868` /
  `441354cb22b6b123de0e80809b222953dbddc75f620fbc01c9b7fa70765ceaed`;
- acceptance-receipt file / semantic:
  `baa2685ac63a339c2e662821899bf635ccdce71718f778346119609c2a65c638` /
  `bdb68aea11c0621bb8f92e5c35c5f24d8689809ae0a35fc423de1b3e2912a625`.

The full theorem, 2-by-25 matrix, proof bindings, and scope limits are in
[`state_charging_transition_ordinary_matrix_20260901.md`](state_charging_transition_ordinary_matrix_20260901.md).

## Strict-N25 `Qgt` two-slot Hall closure (2026-09-01)

The dedicated Hall campaign is complete and independently accepted.  It uses
the same exact typed first-to-next antecedent

`H_Qgt := exists v,w [P(v,w) and q_w > q_v]`

and the fixed two-slot map

`e1 -> G410`, `e2 -> G420`.

All three nonempty Hall masks are proof-qualified:

| mask | exact complement | terminal class | provenance |
|---|---|---|---|
| `1` | `H_Qgt and O[G410]` | `IMPORTED_VERIFIED_UNSAT_N25` | frozen matrix `Qgt/G410` proof |
| `2` | `H_Qgt and O[G420]` | `IMPORTED_VERIFIED_UNSAT_N25` | frozen matrix `Qgt/G420` proof |
| `3` | `H_Qgt and (O[G410] or O[G420])` | `VERIFIED_UNSAT_N25` | sole new direct solve |

The joint mask was encoded by the single positive clause
`(333070, 333072)`, never by two occupancy units.  The two singleton solvers
and checkers were not rerun.  The fresh nonvacuity replay is
`AUDITED_SAT_N25` with witness `(v,w,gap,q_v,q_w)=(11,14,3,1,2)`.

The sole new AE solve returned UNSAT with code 20 in
`604.9714680723846` seconds.  Its 446,580,577-byte proof has SHA-256
`9a36350c0644914db725d385034c60f64d3231bc109322d8a7cb74dee74b8d40`;
the pinned checker returned the unique verdict `s VERIFIED`, and its log has
SHA-256
`ef90f0d4de994f0f67b268c24b3aadcad40220d58f7bb71c7d903a7a8da56663`.

The finalizer reports zero UNKNOWN masks and
`hall_conclusion_proof_qualified=true`.  The independent receipt reports
`fresh_replay_byte_equal=true` and `external_evidence_unchanged=true`; a
separate terminal filesystem inspection found zero lock/partial/fresh or
singleton-action residue.  Key terminal bindings are:

- final file / semantic SHA-256:
  `386ae292b05df13e71ebae26c85b7fb296ca331403ff5b5b34f4da58a34b5bf0` /
  `9970b66fd5336665f470d283c7878dd003f12f548ef4986ba108f21527640ba2`;
- acceptance receipt file / semantic SHA-256:
  `f3e1a2fb5fd9aa2401710ba7c86cb2ade8035b1843af27118a8ee75b276fe001` /
  `18d5b476f5eb3ca671a667722e17a08a6196d9e1f463ffaa750100ece6670653`;
- authoritative root:
  `/data/ktqiu_hdd/math_agent/res/state_charging/20260901_qgt_two_slot_hall_v1`.

Therefore, at strict N25 and only for this typed first-to-next `Qgt` pattern,

`H_Qgt -> not O[G410] and not O[G420]`,

and the fixed two-slot map satisfies every nonempty Hall mask.  This gives at
least two distinct globally missing ordinary-state types for this pattern.  It
does not prove `Qeq`, exact-q/gap, a third slot, arbitrary exceptional
occurrences, arbitrary N, or the global charging inequality.  The complete
formal statement and proof graph are in
[`state_charging_qgt_two_slot_hall_20260901.md`](state_charging_qgt_two_slot_hall_20260901.md).

## Exact continuation point

1. Qlt fixed-q work remains complete and frozen through `prefix[20]`.  There
   is no qv21 or next fixed-q partition.  Do not rerun `Agt1` or any accepted
   Qlt source/pair/aggregate layer.
2. The strict-N25 two-slot `Qgt` Hall evidence chain is complete and frozen:
   fresh nonvacuity, both imported singleton masks, the direct joint mask,
   finalizer, and independent receipt are all accepted.  Do not rerun it.
3. The next research gate is a choice, not an experiment already started:
   refine `Qeq` or exact `(q_v,q_w,gap)` to seek a dynamic charging mechanism,
   or open a separately scoped three-slot/multi-event campaign.  The accepted
   two-slot theorem does not decide between these routes.
4. Keep triple-only paused unless a new verified UNSAT edge needs compression
   into a readable lemma.  Do not claim a multi-event Hall injection, a global
   charging inequality, arbitrary-N generalization, or monolithic `Agt1`
   UNSAT until those distinct claims receive their own evidence chains.

## Frozen Qlt theorem artifact (2026-09-01)

The paper-level fixed-pair exhaustion theorem, proof-layer distinctions, full
7,315-coordinate count, and proof dependency graph are frozen in
[`qlt_fixed_pair_partition_theorem_20260901.md`](qlt_fixed_pair_partition_theorem_20260901.md).
The terminal evidence remains `prefix[20]`; qv21 is vacuous and no closed Qlt
layer or monolithic `Agt1` run is to be restarted.

## Strict-N25 `Qeq` exact-q/gap vocabulary stopping result (2026-09-02)

The empirical exact-partition campaign is complete and independently
accepted.  It reused the 24 accepted coarse-`Qeq` SAT rows without rerunning
the frozen 50-cell matrix.  Validation before deduplication produced nine
unique complete assignments and exactly two observed coordinates:

| `(k,d)` | source rows | unique assignments | audited SAT cells for `G != G410` | empirical zeroes |
|---|---:|---:|---:|---:|
| `(1,1)` | 20 | 5 | 24/24 | 0 |
| `(1,2)` | 4 | 4 | 24/24 | 0 |

Each coordinate has audited-SAT nonvacuity gates.  For each one and every
ordinary state `G != G410`, a retained complete assignment freshly replays
against the exact aggregate formula

`P(v,w) and q_v=q_w=k and w-v=d and O[G]`.

Thus no unmarked ordinary-state token other than `G410` is uniformly absent
in either realized aggregate partition.  A total current-vocabulary dynamic
second-charge map `(k,d) -> G` is impossible, and the accepted terminal class
is exactly

```text
CURRENT_25_STATE_VOCABULARY_INSUFFICIENT_FOR_EXACT_Q_GAP_CHARGING
```

The 50-formula suite consists of two gates and 48 occupancy cells.  Its
canonical evidence chain consists of 24 source records, nine gate-audit
records, and 48 cell-audit records, for 81 records total.  The independent
auditor regenerated all 81 records and the final payload byte-for-byte.
Solver, proof-producer, and checker invocation counts for this Qeq campaign
are `0/0/0`.

The other 208 coordinates in the 210-coordinate combinatorial registry are
labelled only `NOT_RUN_AFTER_EXISTENTIAL_BLOCKER`; no SAT, UNSAT,
realizability, or impossibility claim is made for them.  The frozen 50-cell
matrix, Qgt singleton/joint-Hall chain, and Qlt-through-qv20 envelopes are
sealed/hash-registered inputs and were not rerun by this Qeq campaign.  qv21,
monolithic `Agt1`, and triple-only are prohibited or out of scope rather than
sealed inputs; no qv21 campaign/result is asserted.  This campaign did not
start a new Hall or three-event/three-slot campaign.

Terminal evidence identities are:

- final file / semantic SHA-256:
  `37006eb316dfeda9a4bcdf4480fba2f56bfe0a11f742af813adc38797c035968` /
  `ebf5d7fcdb4bfae971c5b777e6fdef519b25aad0b2058fd57d5d1c21a8f947ff`;
- acceptance receipt file / semantic SHA-256:
  `b2bc865d1095fa82d153294a8518d00b1385ee254c8e2527ecd27a27bc238c81` /
  `09f5411c147db8649cb7bb23d7e9c299a08b565e2bc902c3ef20a9666c1176d9`;
- authoritative root:
  `/data/ktqiu_hdd/math_agent/res/state_charging/20260902_qeq_exact_partition_replay_v2`;
- read-only compact metadata archive, containing 221 entries and no CNF:
  `/data/ktqiu_hdd/math_agent/tmp/qeq_exact_partition_server_20260902_v2_metadata.tar.gz`,
  SHA-256
  `0850a5533913c4487ac0ef3a64eda6e339bec2c0e853c84503ec94e2e1d3f7fb`.

The complete theorem, formula construction, proof graph, acceptance truth
gate, and nonclaims are in
[`state_charging_qeq_exact_partition_20260902.md`](state_charging_qeq_exact_partition_20260902.md).
The next supported scientific step is to enrich ordinary states with
position, prefix, or suffix information, or to replace the invariant; the
current exact-q/gap vocabulary should not be extended into a three-slot Hall
campaign as-is.

## `Qeq` position-marked v1 single-coordinate obstruction (2026-09-03)

The position-marked v1 screen reused the nine accepted strict-N25 `Qeq`
models and tested six realized context branches, one for each of the three
single-coordinate families in both exact partitions:

| exact partition | context branch | retained-state union | empirical zeroes refuted by audited SAT |
|---|---|---:|---:|
| `(k,d)=(1,1)` | `open_gap_trace=EMPTY` | 24/24 | 0 |
| `(k,d)=(1,1)` | `right_anchor=G332` | 20/24 | 4 |
| `(k,d)=(1,1)` | `left_anchor=G331` | 18/24 | 6 |
| `(k,d)=(1,2)` | `open_gap_trace=G321` | 19/24 | 5 |
| `(k,d)=(1,2)` | `right_anchor=G331` | 22/24 | 2 |
| `(k,d)=(1,2)` | `left_anchor=G311` | 18/24 | 6 |

P0 contained 11 empirical-zero cells and P1 contained 12.  All 23 produced
complete audited SAT counterexamples.  Together with the ordinary states
already occupied in the retained branch models, this gives all 24 secondary
states `G != G410` on each displayed branch.  The quantifiers are
`for every G there exists a witness X_G`: different states may, and generally
do, use different witnesses.  This is not a claim that one model contains all
24 states simultaneously.

There was no persistent zero, so no AE proof production or independent proof
checker was run.  Hall also remained frozen.  The exact terminal conclusion is

```text
SINGLETON_CHARGE_OBSTRUCTION_FOR_V1_SINGLE_COORDINATE_FAMILIES
```

Namely, none of `left_anchor`, `open_gap_trace`, or `right_anchor`, when used
alone, can name a fixed branch-dependent singleton `G != G410` that is always
globally missing.  This does not exclude a set-valued Hall neighbourhood, a
joint missing-state/cardinality statement, a Cartesian context signature, or
another non-singleton rule.  Under the state-injection premise, the two
exceptional endpoints already guarantee that some second ordinary state
besides `G410` is missing; what failed is the stronger request for a fixed
singleton that can be named from one v1 branch coordinate.  Consequently no
two-event or three-event Hall campaign is resumed from these singleton cells.
The detailed counting contract, branch census, and SAT-first evidence are in
[`state_charging_qeq_position_marked_20260902.md`](state_charging_qeq_position_marked_20260902.md).

The accepted v3 finalizer anchors are:

- authoritative server root:
  `/data/ktqiu_hdd/math_agent/res/state_charging/20260903_qeq_position_context_singleton_obstruction_final_v3`;
- final file / semantic SHA-256:
  `07c3fdb552e50c636bcf01269236f2339ad45e4a89bbeab3cef26dcb9b5e997e` /
  `56e9340f20affed0f5317713064318bb3f1de47e50208653b64d446a91297229`;
- acceptance file / audit-semantic SHA-256:
  `f2ecd71f20a5dd9ffc70e6e96555a9c9fd56db5ff7571695e66f82b498a45b57` /
  `0c675b82771d87334aea112675a7b1c461830d90c07130194dacac1ec149ed04`.

The finalizer invocation counts for solver, proof producer, checker, Hall, and
source-model re-decoding are all zero.
