# Public Lean source inventory — 2026-10-27

Read-only source navigation and receipt inventory. No new theorem claim, semantic transfer, proof review, compilation, solver, network, replay, acceptance or assurance upgrade. Writes are isolated to this source_map directory. Source line numbers are one-based; declarations and helper references below are textual locations, not a verified dependency graph. Literal/Data bodies were excluded; they are only hashed or described through existing receipts/interface excerpts.

Requested child configuration: native gpt-6.1-sol/high. Backend identity and actual effort are not independently reported by these file operations. Active task metadata observed: nr7-structure-capacity, in_progress, completedAt null.

## Reading entry points

- Closure rule dispatch: ES7ClosureRules.lean:11 (Schema), :40 (sound); codec tags: ES7ClosureCodec.lean:99 (schema), :124 (checked_sound).
- Closure ambient model: ES7ClosureFrame.lean:16; shared named model: ES7NamedGeometry.lean:34.
- Through14 model: ES7ThroughMeaning.lean:11; soundness: ES7ThroughRules.lean:55, ES7ThroughCodec.lean:65.
- Terminal20 contract: ES7OrderedContract.lean:136; soundness :154 and ES7OrderedSourceCodec.lean:77.
- Joint17 hypotheses: ES7JointRules.lean:9; soundness :63 and ES7JointCodec.lean:62; model construction: ES7JointRealization.lean.

## Closure wire tags and rule groups

| Outer wire tag | Schema constructor | Group semantic source |
|---|---|---|
| 0 | base | ES7ClosureBaseRules |
| 1 | ambient | ES7ClosureAmbientRules |
| 2 | core | ES7ClosureCoreRules |
| 3 | low | ES7ClosureLowRules |
| 4 | counting | ES7ClosureCounting |
| 5 | packet | ES7ClosurePacket |
| 6 | terminal | ES7ClosureTerminal |
| 7 | prefixRule | ES7PrefixSchema |

Every group has a sound theorem. Note packet precedes terminal in codec tags, although terminal precedes packet in the inductive declaration.

## Exact source paths, imports, declarations and constructors

### ES7ClosureRules

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureRules.lean`

Direct imports: ES7ClosureBaseRules:1; ES7ClosureAmbientRules:2; ES7ClosureCoreRules:3; ES7ClosureLowRules:4; ES7ClosureCounting:5; ES7ClosureTerminal:6; ES7ClosurePacket:7; ES7PrefixSchema:8.

Declarations: `Schema:11`, `clause:21`, `Valid:30`, `sound:40`.

Inductive constructors (all inductives in this file): `base:12`, `ambient:13`, `core:14`, `low:15`, `counting:16`, `terminal:17`, `packet:18`, `prefixRule:19`.

### ES7ClosureMeaning

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureMeaning.lean`

Direct imports: ES7ClosureCorePaths:1.

Declarations: `PrefixPattern:6`, `pairs:12`, `triples:14`, `Prefix:18`, `Ambient:23`, `Core:27`, `Witness:31`, `lowPoints:34`, `Low:38`, `Internal:42`, `internalNames:44`, `Variable:48`, `meaning:60`, `yes:71`, `no:72`, `lift:73`, `lift_spec:77`, `active:80`, `before:81`, `color:83`, `active_spec:85`, `before_core_spec:91`, `before_spec:98`, `color_spec:106`.

Inductive constructors (all inductives in this file): `named:49`, `ambient:50`, `core:51`, `witness:52`, `low:53`, `internal:54`, `last:55`, `internalCount:56`, `prefix:57`.

### ES7ClosureCodec

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCodec.lean`

Direct imports: ES7ClosureRules:1; ES7OrderedSourceCodec:2; ES7JointCodec:3.

Declarations: `pattern:9`, `name:10`, `base:21`, `ambient:38`, `core:50`, `low:63`, `counting:72`, `terminal:80`, `prefixRule:87`, `schema:99`, `names:109`, `schemas:111`, `good:113`, `checked:120`, `checked_sound:124`.

### ES7ClosureBaseRules

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureBaseRules.lean`

Direct imports: ES7ClosurePopulation:1.

Declarations: `boundedDistinct:8`, `Schema:11`, `guards:27`, `conclusion:42`, `clause:57`, `Valid:60`, `two_valid:78`, `three_valid:80`, `sound:86`.

Inductive constructors (all inductives in this file): `order:12`, `pairActive:13`, `pairOrder:14`, `pairChoice:15`, `pairUnique:16`, `firstPair:17`, `forward:18`, `endpoint:19`, `pathActive:20`, `pathOrder:21`, `base:22`, `growth:23`, `polygon:24`.

### ES7ClosureAmbientRules

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbientRules.lean`

Direct imports: ES7ClosureBaseRules:1; ES7ClosureAmbient:2.

Declarations: `Schema:8`, `guards:20`, `conclusion:30`, `clause:40`, `Valid:42`, `ambient_nontrivial:54`, `sound:62`.

Inductive constructors (all inductives in this file): `activation:9`, `order:10`, `nesting:11`, `pairBudget:12`, `vertexBudget:13`, `base:14`, `growth:15`, `selectedRank:16`, `throughCap:17`.

### ES7ClosureCoreRules

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCoreRules.lean`

Direct imports: ES7ClosureAmbientRules:1.

Declarations: `witnessTerms:7`, `successors:9`, `Schema:11`, `guards:24`, `conclusion:35`, `clause:46`, `Valid:48`, `witness_terms:61`, `core_nontrivial:81`, `sound:89`.

Inductive constructors (all inductives in this file): `activation:12`, `order:13`, `witnessNeg:14`, `witnessPos:15`, `forward:16`, `attainment:17`, `extension:18`, `capPair:19`, `sourceForward:20`, `sourceAttain:21`.

### ES7ClosureLowRules

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureLowRules.lean`

Direct imports: ES7ClosureCoreRules:1.

Declarations: `Schema:6`, `guards:15`, `conclusion:22`, `clause:29`, `Valid:31`, `sound:40`.

Inductive constructors (all inductives in this file): `activation:7`, `order:8`, `extension:9`, `impossible:10`, `base:11`, `growth:12`.

### ES7ClosureCounting

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCounting.lean`

Direct imports: ES7ClosureNameFacts:1; ES7ClosurePopulation:2.

Declarations: `throughList:6`, `pool:7`, `term:9`, `counter:10`, `term_spec:14`, `counter_spec:24`, `core_count:34`, `through_count:41`, `internal_count:47`, `Schema:55`, `clause:63`, `Valid:77`, `sound:83`.

Inductive constructors (all inductives in this file): `recurrence:56`, `coreBound:57`, `throughBound:58`, `internalBound:59`, `mandatory:60`.

### ES7ClosureTerminal

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureTerminal.lean`

Direct imports: ES7ClosureCounting:1; ES8PlanarChains:2.

Declarations: `terminal_all:7`, `Schema:21`, `guards:28`, `conclusion:33`, `clause:38`, `Valid:40`, `sound:47`.

Inductive constructors (all inductives in this file): `active:22`, `maximum:23`, `cup:24`, `cover:25`.

### ES7ClosurePacket

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosurePacket.lean`

Direct imports: ES7ClosureBaseRules:1; ES7PacketSemantics:2.

Declarations: `triples:9`, `packetColor:10`, `four_bool:14`, `packet_color_spec:25`, `guards:46`, `clause:50`, `sound:53`.

### ES7PrefixSchema

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7PrefixSchema.lean`

Direct imports: ES7PrefixRules:1.

Declarations: `Schema:6`, `guards:18`, `conclusion:26`, `clause:36`, `Valid:38`, `sound:51`.

Inductive constructors (all inductives in this file): `activation:7`, `order:8`, `exhaustion:9`, `sign:10`, `attainment:11`, `unique:12`, `implies:13`, `baseCover:14`, `sectorCover:15`.

### ES7ClosureFrame

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureFrame.lean`

Direct imports: ES7JointPopulations:1; ES7BalancedSelection:2; ES7TerminalPopulation:3.

Declarations: `coreStates:8`, `box:10`, `Model:14`, `coreNames:33`, `corePoints:34`, `owner_inj:36`, `corePoints_eq:43`, `core_bounded:57`, `core_card:62`, `core_no_five_cap:69`, `low_starts_cap:74`, `through_ends:82`.

Model/Hypotheses fields (verbatim):

- `base : ES7NamedGeometry.Model c 40 realStates:15`
- `active_bound : ∀i∈base.active,i < 39:16`
- `core_states : ∀i < 35,realStates i=coreStates i:17`
- `tail_active : ∀i,35 ≤ i → i < 39 → i∈base.active:18`
- `tail_order : ∀i∈base.active,∀j∈base.active,:19`
- `core_starts : ∀i∈base.active,i < 35 → StartsFive c.cup true (Finset.range 50) (base.owner i):21`
- `core_cover : ∀v : Fin 50,v∈starters c true → ∃i < 35,i∈base.active ∧ base.owner i=v.val:22`
- `normalized : c.cup 0 1 2=true:23`
- `last : Nat:24`
- `last_active : last∈base.active:25`
- `last_core : last < 35:26`
- `last_max : ∀i∈base.active,i < 35 → base.owner i ≤ base.owner last:27`
- `terminal : (ES8ActualRanks.colorConfig c.cup true).Cup:28`

### ES7ClosureDomains

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureDomains.lean`

Direct imports: ES7ClosureMeaning:1.

Declarations: `PairAllowed:5`, `labels:10`, `maxLength:12`, `PathAllowed:14`, `path:18`, `ambient:21`, `core:24`, `low:27`, `pair_allowed:30`, `label_mem:40`, `ending_bound:59`, `path_holds:71`, `ambient_maximum:87`, `ambient_holds:91`, `ambient_of_holds:100`.

### ES7ClosureCoreSemantics

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCoreSemantics.lean`

Direct imports: ES7ClosureDomains:1.

Declarations: `owner_in_core:6`, `name_of_core:9`, `core_maximum:14`, `core_holds:28`, `core_of_holds:37`, `witness_forward:52`, `core_attainment:63`, `core_extension:75`, `lowPoint_starts_cap:85`, `low_extension:91`, `low_maximum:95`, `low_holds:98`, `low_base:104`, `low_base_end:109`, `low_step:120`, `internal_of_core:125`, `internal_attainment:136`.

### ES7ClosureCorePaths

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCorePaths.lean`

Direct imports: ES7ClosureFrame:1.

Declarations: `extend_start:6`, `start_of_cup:18`, `LowPath:28`, `low_bounds:32`, `low_extend:37`, `low_maximum:47`.

Inductive constructors (all inductives in this file): `pair:29`, `step:30`.

### ES7ClosureAmbient

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbient.lean`

Direct imports: ES7ClosureCoreSemantics:1.

Declarations: `ambient_base:6`, `ambient_step:13`, `ambient_nesting:18`, `same_pair_budget:21`, `vertex_budget:31`, `selected_rank:52`, `through_cap:59`.

### ES7ClosurePopulation

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosurePopulation.lean`

Direct imports: ES7ClosureCoreSemantics:1.

Declarations: `throughNames:6`, `through_card:9`, `through_range:31`, `internal_card:35`, `six_internal:60`.

### ES7ClosureNameFacts

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureNameFacts.lean`

Direct imports: ES7ClosureConstruction:1; ES7FiniteRanks:2.

Declarations: `core_catalog_check:8`, `core_injective:12`, `owner_of_state:15`, `first_two:27`.

### ES7ClosureConstruction

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureConstruction.lean`

Direct imports: ES7ClosureFrame:1.

Declarations: `baseModel:9`, `name:51`, `activeCore:52`, `coreOwner:53`, `name_bound:57`, `coreOwner_spec:59`, `activeCore_bound:67`, `coreOwner_name:71`, `coreStates_actual:78`, `coreStates_size:95`, `incoming_size:104`, `selectedOwner:110`, `selectedActive:112`, `selectedStates:113`, `selectedOwner_core:116`, `selectedOwner_tail:119`, `selectedActive_bound:124`, `selectedOwner_bound:129`, `selected_tail_order:133`, `selectedOwner_inj:167`, `selectedBase:184`, `frame:208`.

### ES7ClosureExistence

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureExistence.lean`

Direct imports: ES7ClosureConstruction:1.

Declarations: `exists_frame:5`.

### ES7PrefixRules

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7PrefixRules.lean`

Direct imports: ES7PrefixExistence:1; ES7ClosureBaseRules:2.

Declarations: `ownerAt:7`, `records:8`, `pairRecords:9`, `coordinate:10`, `Disagree:12`, `Extends:15`, `PairComplete:20`, `prefix_disagree:23`, `prefix_extends:30`, `prefix_position:39`, `prefix_order:42`, `prefix_exhaustion:51`, `prefix_color:67`, `label_predecessor:81`, `prefix_attainment:88`.

### ES7PrefixGeometry

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7PrefixGeometry.lean`

Direct imports: ES7PrefixCoverage:1; ES7ClosureNameFacts:2.

Declarations: `triples_mem:6`, `pairs_mem:16`, `zip_graph:26`, `completion_actual:31`, `row_actual:48`.

### ES7PrefixExistence

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7PrefixExistence.lean`

Direct imports: ES7PrefixGeometry:1.

Declarations: `Fixed:6`, `fixed_exists:9`, `prefix_agrees:19`, `fixed_of_prefix:24`, `base_exists:33`, `actual_good:45`, `good_congr:59`, `fixed_four_all:76`, `extended_exists:82`.

### ES7PrefixCoverage

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7PrefixCoverage.lean`

Direct imports: ES7PrefixData:1.

Declarations: `cube:7`, `mem_cube:11`, `freeTriples:18`, `completion:19`, `packets:23`, `agrees:32`, `Good:35`, `sectorPatterns:38`, `coverageCheck:40`, `extended_coverage:45`, `base_checked:46`, `sector_checked:50`.

### ES7ThroughMeaning

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ThroughMeaning.lean`

Direct imports: ES7CorePaths:1; ES7AmbientRemap:2.

Declarations: `coreSet:9`, `Model:11`, `core_mem:21`, `core_bounded:24`, `order_reflect:29`, `Variable:36`, `CoreRank:42`, `predecessor:45`, `turnValue:48`, `meaning:51`, `positive:57`, `negative:58`, `color:59`, `notColor:60`, `preVar:61`, `witnessLit:63`, `negLit:66`, `predecessors:67`, `LitTrue:70`, `Satisfied:72`, `color_spec:74`, `neg_spec:77`, `pos_spec:82`, `negative_spec:84`, `PairValid:87`, `RankValid:88`, `PreValid:89`, `predecessor_mem:94`, `rank_base:97`, `rank_step:104`, `witness_forward:114`, `rank_attain:130`, `rank_nesting:158`, `ambient_extension:164`, `pair_extension:179`, `core_maximum:189`.

Inductive constructors (all inductives in this file): `ambient:37`, `core:38`, `witness:39`.

Model/Hypotheses fields (verbatim):

- `ordered : ∀ a b, a < b → b < 22 → f a < f b:12`
- `bounded : ∀ a, a < 22 → f a < n:13`
- `noSix : NoSix c.cup (Finset.range n):14`
- `noGon : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point):15`
- `through : Through c.cup (Finset.range n) (coreSet f):16`
- `cups : ∀ i j k, i < j → j < k → k < 22 → (k ≤ 4 ∨ 17 ≤ i) → c.cup (f i) (f j) (f k)=true:17`

### ES7ThroughRules

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ThroughRules.lean`

Direct imports: ES7ThroughMeaning:1.

Declarations: `turnLit:7`, `Schema:9`, `Schema.clause:22`, `Schema.Valid:34`, `pre_spec:48`, `turn_spec:51`, `sound:55`.

Inductive constructors (all inductives in this file): `base:10`, `witnessNeg:11`, `witnessPos:12`, `forward:13`, `attain:14`, `nesting:15`, `extension:16`, `pair:17`, `maximum:18`, `actualCup:19`.

### ES7ThroughCodec

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ThroughCodec.lean`

Direct imports: ES7ThroughRules:1; ES7OrderedSourceCodec:2.

Declarations: `name:8`, `schema:14`, `names:27`, `schemas:29`, `decoded:32`, `good:35`, `checked:38`, `assignment:42`, `decoded_sound:48`, `checked_sound:65`.

### ES7ThroughSelection

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ThroughSelection.lean`

Direct imports: ES7Through14Data:1; ES7TerminalPopulation:2.

Declarations: `selected:7`, `selected_strict:14`, `selection:31`, `fourteen_impossible:37`, `through_population_le_thirteen:96`.

### ES7OrderedContract

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedContract.lean`

Direct imports: ES7OrderedPaths:1.

Declarations: `Var:8`, `Meaning:16`, `Sat:24`, `pos:26`, `neg:27`, `turn:28`, `notTurn:29`, `pathVar:30`, `notPath:32`, `rankVar:35`, `turn_spec:38`, `not_turn_spec:42`, `path_three_iff:47`, `path_spec:58`, `not_path_spec:64`, `packetBits:72`, `Rule:78`, `Rule.clause:95`, `Rule.Valid:117`, `Hypotheses:136`, `packet_sound:142`, `sound:154`.

Inductive constructors (all inductives in this file): `C:9`, `P:10`, `E:11`, `L:12`, `R:13`, `pathExtend:79`, `pathMax:80`, `endpoint:81`, `weak:82`, `packet:83`, `base:84`, `extend:85`, `maximum:86`, `triple:87`, `suffix:88`, `pair:89`, `pathRank:90`, `core:91`, `terminal:92`.

Model/Hypotheses fields (verbatim):

- `noSix : NoSix c.cup (Finset.range n):137`
- `noGon : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point):138`
- `core : ∀ b, ¬(colorConfig c.cup b).HasNCup 5 (Finset.range m):139`
- `terminal : ∀ i j k, m - 1 ≤ i → i < j → j < k → k < n → c.cup i j k=true:140`

### ES7OrderedSourceCodec

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedSourceCodec.lean`

Direct imports: ES7OrderedContract:1; ES7LRAT:2.

Declarations: `bit:7`, `name:12`, `rule:20`, `rows:37`, `names:39`, `rules:41`, `decoded:44`, `good:47`, `checked:50`, `assignment:54`, `decoded_sound:60`, `checked_sound:77`.

### ES7OrderedSelection

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedSelection.lean`

Direct imports: ES7Terminal20Data:1; ES7BalancedPopulations:2.

Declarations: `reindex:7`, `enumerate:12`, `enumerate_bound:15`, `enumerate_order:19`, `cup_eq:24`, `cup_map:29`, `noSix_reindex:43`, `noGon_reindex:53`, `selected:62`, `selected_strict:67`, `selection:80`, `terminal_twenty_impossible:87`, `twenty_starters_have_internal_cup:129`.

### ES7TerminalPopulation

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7TerminalPopulation.lean`

Direct imports: ES7OrderedSelection:1.

Declarations: `hasCup_mono:6`, `natSet_mono:12`, `starter_free_subset_bound:20`, `internalStarters:29`, `deletion_no_cup:36`, `internal_source_budget:51`, `six_internal_sources:64`.

### ES7JointRules

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7JointRules.lean`

Direct imports: ES7NamedPacket:1.

Declarations: `lowNames:6`, `highNames:7`, `Hypotheses:9`, `Schema:15`, `clause:23`, `Valid:40`, `counter_sound:48`, `sound:63`.

Inductive constructors (all inductives in this file): `named:16`, `packet:17`, `counter:18`, `population:19`, `mandatory:20`.

Model/Hypotheses fields (verbatim):

- `low : ES7NamedCounting.count m.active lowNames=17:10`
- `high : ES7NamedCounting.count m.active highNames=17:11`
- `first : 0∈m.active:12`
- `second : 1∈m.active:13`

### ES7JointCodec

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7JointCodec.lean`

Direct imports: ES7JointRules:1; ES7OrderedSourceCodec:2.

Declarations: `labelPairs:8`, `name:13`, `named:23`, `schema:39`, `names:47`, `schemas:49`, `good:51`, `checked:58`, `checked_sound:62`.

### ES7JointPopulations

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7JointPopulations.lean`

Direct imports: ES7JointCatalogProof:1; ES7Joint17Data:2; ES7BalancedEquality:3.

Declarations: `state_height_four_iff_ends:9`, `low_of_L:28`, `high_of_R:39`, `index:45`, `index_spec:49`, `index_low:61`, `index_high:67`, `lowAvailable:73`, `highAvailable:74`, `low_population:76`, `high_population:91`, `first_two_available:106`, `joint_seventeen_impossible:125`, `through_range:173`.

### ES7NamedGeometry

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedGeometry.lean`

Direct imports: ES7UnorderedColor:1.

Declarations: `ending_length_first:6`, `rank_first_bound:11`, `initial_label:14`, `incoming_zero:21`, `incoming_one:24`, `Model:34`, `Pair:49`, `NamedPath:52`, `NamedEndpoint:56`, `Cup:59`, `cup_ordered:61`, `pair_exists:65`, `pair_forward:73`, `owner_zero:82`, `owner_one:89`, `pair_first:95`, `pair_second:102`, `maxLength:112`, `ending_bound:115`, `PairAllowed:124`, `PathAllowed:125`, `pair_allowed:131`, `path_allowed:136`, `path_bound:149`, `path_maximum:159`, `path_endpoint:163`, `path_base:166`, `path_step:172`, `endpoint_exclusion:179`.

Model/Hypotheses fields (verbatim):

- `active : Finset Nat:35`
- `active_bound : ∀ i∈active, i < N:36`
- `owner : Nat→Nat:37`
- `owner_bound : ∀ i∈active, owner i < n:38`
- `key : Nat→Nat:39`
- `key_injective : Set.InjOn key (Set.Iio N):40`
- `actual_order : ∀ i∈active, ∀ j∈active, key i < key j ↔ owner i < owner j:41`
- `actual_state : ∀ i∈active, ∀ q, q∈states i ↔ Incoming c.cup (owner i) q:42`
- `inclusion_order : ∀ i j, i < N → j < N → states i ⊂ states j → key i < key j:43`
- `noSix : NoSix c.cup (Finset.range n):44`
- `noGon : ¬ES7Geometry.HasConvexHeptagon (Set.range c.point):45`

### ES7ActualState

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ActualState.lean`

Direct imports: ES7Final:1.

Declarations: `Below:8`, `label:11`, `Incoming:15`, `label_positive:18`, `label_growth:24`, `label_difference:33`, `incoming_injective:42`, `inclusion_order:51`, `incoming_downclosed:58`, `restricted_bounds:64`, `incoming_bounds:73`, `corner_attained:82`, `rank_predecessor:93`, `cup_predecessor:107`, `cap_predecessor:116`.

### ES7JointRealization

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7JointRealization.lean`

Direct imports: ES7JointCatalog:1.

Declarations: `grid:6`, `incoming:7`, `incoming_bound:11`, `mem_incoming:20`, `incoming_subset_order:26`, `incoming_inj:33`, `available:38`, `owner:42`, `owner_spec:45`, `cut:53`, `key:57`, `cut_mono:60`, `cut_actual:71`, `key_inj:85`, `key_inclusion:93`, `key_actual:100`, `realize:127`.

### ES7NamedRules

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedRules.lean`

Direct imports: ES7NamedVariables:1.

Declarations: `boundedDistinct:7`, `Schema:10`, `guards:26`, `conclusion:41`, `clause:56`, `Valid:59`, `two_valid:77`, `three_valid:79`, `sound:85`.

Inductive constructors (all inductives in this file): `order:11`, `pairActive:12`, `pairOrder:13`, `pairChoice:14`, `pairUnique:15`, `firstPair:16`, `forward:17`, `endpoint:18`, `pathActive:19`, `pathOrder:20`, `base:21`, `growth:22`, `polygon:23`.

### ES7NamedPacket

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedPacket.lean`

Direct imports: ES7NamedRules:1; ES7PacketSemantics:2.

Declarations: `triples:8`, `packetColor:9`, `four_bool:13`, `packet_color_spec:24`, `guards:45`, `clause:49`, `sound:52`.

### ES7PacketSemantics

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7PacketSemantics.lean`

Direct imports: ES7ActualState:1.

Declarations: `fan_identity:8`, `fan:13`, `packet_clauses:44`.

### ES7UnorderedColor

Path: `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7UnorderedColor.lean`

Direct imports: ES7ThroughSelection:1.

Declarations: `low:5`, `high:6`, `middle:7`, `color:8`, `ordered:10`, `swap_first:17`, `swap_last:23`, `sorted_names:29`.

## Geometric helper references inside proofs

The following are source-text references, with proof command fragments retained for navigation. Unqualified helper names resolve using the open namespaces shown in each source; no Lean resolution was run.

### ES7ClosureBaseRules

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureBaseRules.lean:121` — `· exact (bad (pair_first m.base p (by rw [m.core_states i valid.2.1]; exact empty))).elim`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureBaseRules.lean:122` — `· have bound := pair_second m.base p (by rw [m.core_states i valid.2.1]; exact singleton)`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureBaseRules.lean:129` — `have grow := pair_forward m.base p q`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureBaseRules.lean:135` — `exact ⟨yes (.named (.endpoints b k s j)),by simp [conclusion],path_endpoint m.base p⟩`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureBaseRules.lean:157` — `exact ⟨_,by simp [conclusion],path_holds m (by omega) (path_base m.base hs hi hj ord ord' turn)⟩`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureBaseRules.lean:171` — `exact ⟨_,by simp [conclusion],path_holds m (by have := valid.2; omega) (path_step m.base p hj ord turn)⟩`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureBaseRules.lean:175` — `exact (endpoint_exclusion m.base a b valid.2.1 valid.2.2.1 valid.2.2.2 cup cap).elim`

### ES7ClosureAmbientRules

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbientRules.lean:77` — `exact ⟨_,by simp [conclusion],ambient_holds m (ambient_nesting m p valid.2)⟩`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbientRules.lean:81` — `exact (same_pair_budget m p b valid.2 a).elim`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbientRules.lean:95` — `exact ⟨_,by simp [conclusion],ambient_holds m (ambient_base m hi hj hk a d col)⟩`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbientRules.lean:102` — `exact ⟨_,by simp [conclusion],ambient_holds m (ambient_step m p hi a col)⟩`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbientRules.lean:106` — `have a := selected_rank m p q`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbientRules.lean:111` — `exact (through_cap m p valid.2.1 valid.2.2.1 valid.2.2.2.1 valid.2.2.2.2).elim`

### ES7ClosureCoreRules

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCoreRules.lean:131` — `exact ⟨_,by simp [conclusion],ambient_holds m (core_extension m p)⟩`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCoreRules.lean:138` — `exact ⟨ambient false 3 i j,by simp [conclusion],ambient_holds m (core_extension m p)⟩`

### ES7ClosureLowRules

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureLowRules.lean:55` — `exact ⟨_,by simp [conclusion],ambient_holds m (low_extension m p)⟩`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureLowRules.lean:58` — `exact (low_base_end m p valid.2).elim`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureLowRules.lean:64` — `exact ⟨yes (.low 2 i j),by simp [conclusion],low_base m hi hj valid.2.1 valid.2.2.1 ij valid.2.2.2⟩`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureLowRules.lean:71` — `exact ⟨_,by simp [conclusion],low_holds m (low_step m p ha valid.2 ord col)⟩`

### ES7ClosureCounting

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCounting.lean:103` — `have h := ES7ClosurePopulation.through_range m`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCounting.lean:106` — `simpa only [clause,Satisfied,List.mem_singleton,exists_eq_left,counter_spec,pool,if_true,internal_count] using ES7ClosurePopulation.six_internal m`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCounting.lean:108` — `have h := ES7ClosureNameFacts.first_two m`

### ES7ClosureTerminal

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureTerminal.lean:10` — `apply ES8PlanarChains.chain3_all (fun a b d=>c.cup a b d=true) (Set.Iio 50) _ _ _ _ _`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureTerminal.lean:12` — `exact ES8ThreeChain.four c ab bd de he true left right`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureTerminal.lean:58` — `have hj := (active_spec m (by have := valid.2.1; omega : j < 39)).mp (all (ES7ClosureMeaning.active j) (by simp [guards]))`

### ES7ClosurePacket

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosurePacket.lean:71` — `have geom := ES7PacketSemantics.packet_clauses c`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosurePacket.lean:74` — `have first := (packet_color_spec m a b d e aa bb dd ee ab bd de i (by omega) v).mp (all _ (by simp [guards]))`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosurePacket.lean:75` — `have last := (packet_color_spec m a b d e aa bb dd ee ab bd de k kh v).mp (all _ (by simp [guards]))`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosurePacket.lean:76` — `exact ⟨_,by simp,(packet_color_spec m a b d e aa bb dd ee ab bd de j (by omega) v).mpr`

### ES7ClosureCoreSemantics

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCoreSemantics.lean:20` — `exact ES7OrderedPaths.starting_forbidden (m.base.noSix true) (ES8ResidualRanks.truncate amb 6 (by omega) (by omega))`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCoreSemantics.lean:80` — `apply ES7ClosureCorePaths.extend_start (core_bounded m) m.base.noSix _ p.2.2.2.2.2`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCoreSemantics.lean:93` — `exact ES7ClosureCorePaths.low_extend (core_bounded m) m.base.noSix (fun w hw=>lowPoint_starts_cap m hw) p.2.2.2.2.2`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCoreSemantics.lean:99` — `have lo := (ES7ClosureCorePaths.low_bounds p.2.2.2.2.2).2.2.2`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCoreSemantics.lean:114` — `| step prior _ _ _ => have := (ES7ClosureCorePaths.low_bounds prior).2.2.2; omega`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureCoreSemantics.lean:139` — `have p := ES7ClosureCorePaths.start_of_cup [b,d,e] chain inside`

### ES7ClosureAmbient

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbient.lean:24` — `have past := ES8ActualRanks.rank_attained c.cup b (m.base.owner i) (m.base.owner j) order`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbient.lean:26` — `have positive := (ES8ActualRanks.length_bounds past).1`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbient.lean:27` — `have total : ES8ActualRanks.rank c.cup b (m.base.owner i) (m.base.owner j)+k=8 := by`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbient.lean:38` — `have ab := ES7BalancedAmbient.rank_le_five c m.base.noSix true ui (m.base.owner_bound i a.1)`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbient.lean:39` — `have bb := ES7BalancedAmbient.rank_le_five c m.base.noSix false ui (m.base.owner_bound i a.1)`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbient.lean:44` — `have past := ending_truncate (ES8ActualRanks.rank_attained c.cup true u (m.base.owner i) ui)`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbient.lean:48` — `have past := ending_truncate (ES8ActualRanks.rank_attained c.cup false u (m.base.owner i) ui)`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbient.lean:55` — `have rank := ES8ActualRanks.rank_ge actual`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureAmbient.lean:70` — `exact ES7BalancedExtensions.no_four_between_through c.cup _ m.base.noSix true`

### ES7ClosureFrame

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureFrame.lean:65` — `rw [corePoints_eq,ES8Subset.natSet,Finset.card_image_of_injective _ Fin.val_injective] at image`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureFrame.lean:66` — `have h := ES7BalancedPopulations.starter_card c true m.base.noSix m.base.noGon`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureFrame.lean:72` — `exact ES7BalancedPopulations.starter_no_opposite_five c true m.base.noSix`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureFrame.lean:79` — `exact (mem_starters c false _).mp (ES7BalancedAmbient.low_starter_starts_cap c m.base.noSix m.base.noGon`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureFrame.lean:84` — `apply (ES7BalancedAmbient.state_width_four_iff_ends c m.base.noSix ⟨m.base.owner i,m.base.owner_bound i hi⟩).mp`

### ES7NamedGeometry

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedGeometry.lean:9` — `| step prior uv turn => have bound := ES8ActualRanks.length_bounds prior; omega`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedGeometry.lean:17` — `have al := (length_bounds (rank_attained cup true 0 v positive)).1`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedGeometry.lean:18` — `have bl := (length_bounds (rank_attained cup false 0 v positive)).1`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedGeometry.lean:139` — `have ep := ES7OrderedPaths.selected_path_rank p`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedGeometry.lean:140` — `have upper := ES7BalancedAmbient.rank_le_five c m.noSix b (length_bounds ep).2.2 (m.owner_bound j hj)`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedGeometry.lean:151` — `have ep := ES7OrderedPaths.selected_path_rank p`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedGeometry.lean:160` — `exact ES7OrderedPaths.ending_forbidden (m.noSix b) (m.owner_bound j path.2.2.1)`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedGeometry.lean:168` — `refine ⟨hs,hi,hj,si,ij,ES7PathSemantics.path_three c.cup b _ _ _`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedGeometry.lean:175` — `refine ⟨hs,hi,hj,sh.trans hi',ij,ES7PathSemantics.path_extension c.cup b _ _ _ _ k p`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7NamedGeometry.lean:181` — `exact m.noGon (ES7OrderedPaths.weak_heptagon c (m.owner_bound j cup.2.1) ha hb total cup.2.2 cap.2.2)`

### ES7ActualState

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ActualState.lean:20` — `have r := (length_bounds (rank_attained cup true u v uv)).1`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ActualState.lean:21` — `have b := (length_bounds (rank_attained cup false u v uv)).1`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ActualState.lean:27` — `have r := (length_bounds (rank_attained cup true t u tu)).1`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ActualState.lean:28` — `have b := (length_bounds (rank_attained cup false t u tu)).1`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ActualState.lean:96` — `have path := rank_attained cup color u v uv`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ActualState.lean:113` — `have low := (length_bounds (rank_attained cup true t u tu)).1`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ActualState.lean:122` — `have low := (length_bounds (rank_attained cup false t u tu)).1`

### ES7OrderedContract

- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedContract.lean:56` — `· exact ES7PathSemantics.path_three c.cup b s i j si ij`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedContract.lean:145` — `have hp := ES7PacketSemantics.packet_clauses c ij jk kl ln`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedContract.lean:160` — `have extension := ES7PathSemantics.path_extension c.cup b s h i j k`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedContract.lean:168` — `have maximum : ES7PathSemantics.Path c.cup b s h i 5 → c.cup h i j=b → False := by`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedContract.lean:170` — `exact ending_forbidden (hyp.noSix b) jn (selected_path_rank (ES7PathSemantics.path_extension c.cup b s h i j 5 p ij turn))`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedContract.lean:176` — `have h := ES7PathSemantics.path_endpoint c.cup b s i j k`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedContract.lean:180` — `have h := fun cup cap => hyp.noGon (weak_heptagon c (s:=s) jn ha hb total cup cap)`
- `D:/科研/math agent/erdos-szekeres-sat-main/tmp/schroeder_comparison_20261021/selected_sources/es7_es8_bounds_81_319_v1/formal/sources/ES7OrderedContract.lean:184` — `| packet i j k l t => exact packet_sound c i j k l t valid`

## Literal/Data wrapper locations (from pre-existing interface excerpt only)

Evidence for the following is the existing file `D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_transfer_20261026/source_interfaces.txt`, lines 139–300. This inventory did not print or read Literal/Data bodies.

| Exact file path | Wrapper interface | Direct imports |
|---|---|---|
| `D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES7Terminal20Data.lean:19` | `impossible (c : Configuration 24) (hyp : Hypotheses c 20)` | ES7OrderedSourceCodec:1; ES7Terminal20Literal:2 |
| `D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES7Through14Data.lean:19` | `impossible (c : Configuration n) (f : Nat→Nat) (m : Model c f)` | ES7ThroughCodec:1; ES7Through14Literal:2 |
| `D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES7Joint17Data.lean:16` | `impossible (m : Model c 40 ES7JointCatalog.states) (hyp : Hypotheses m)` | ES7JointCatalog:1; ES7Joint17Literal:2 |
| `D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES7ClosureData.lean:16` | `impossible (m : Model c realStates)` | ES7ClosureCodec:1; ES7ClosureLiteral:2 |

Wrapper theorem names named accepted/impossible in acquired public source are declarations, not a claim that a local run compiled them or that this project accepted their semantic transfer.

## Existing receipt inventory

All statuses here are historical file contents observed locally, not fresh process checks. Absence statements concern the inspected local balanced49 source/port directories.

| Stage | Receipt and recorded result | Scope |
|---|---|---|
| Through14 | `D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_abstract_port_20261026/through14_replay_result.json:129–143`: replay exit 0; status PASS; unchanged literal hash 640acebb5128073f1731f88893fe4178fb73d9259577fc562f4579c66650e250 | Fixed-byte finite strict RUP only; no semantic transfer or mathematical acceptance |
| Terminal20 | `D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_abstract_port_20261026/small_literals_execution_02.json:4` embedded stdout records literal PASS, replay exit 0, source_unchanged true; 12722 vars, 25074 clauses, 79173 additions | Outer two-literal job status FAILED after Joint17 network failure; do not turn that aggregate failure into Terminal20 failure or Joint17 success |
| Joint17 | `D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_abstract_port_20261026/joint17_transport_result.json:16–19`: source_identity_verified, SHA256 22950a14595f72b93a769261738d029b2aa27d04aa27e1f44fa2dce77775da2a | Transport identity only. No local Joint17 replay completion receipt found in inspected directory |
| Closure | `D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_transfer_20261026/retrieval_receipt_network.json` defers ES7ClosureLiteral: 732220946 uncompressed bytes, manifest-declared SHA only | No local Closure replay completion receipt found in inspected directories; public README completion statements remain source claims |
| Lean binary | `D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_abstract_port_20261026/lean_windows_resume_result.json:11–12`: downloaded_hash_verified, 564056221 bytes, SHA256 ce6e79dd19ea03c0bc17f9d565c3bac20cd2884561e3b431e5b293c1fbb2b5b3 | Binary transport, not installation/compilation; lean_setup_execution.json records historical timeout exit 124. No Lean compile completion receipt found |
| Source retrieval | `D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_transfer_20261026/retrieval_receipt_network.json`: source_text_acquisition_complete; retrieved_code_executed=false, lean_compiled=false, certificate_replayed=false, full_archive_sha256_checked=false | Selected-source identity, not a build/replay receipt |

`dependency_audit_result.json` is a historical metadata-only import audit. Its then-missing Joint17/Terminal20 literal entries precede later transport evidence and are not current absence claims. The audit still usefully identifies transitive modules and records that it performed no compilation.

Manifest-only upstream evidence names include formal/audit/full_clean_build.json, audit/heptagon_strict_replay.json, audit/joint_rebuild/* and verification.json. Their presence as manifest keys is not evidence those files were locally acquired or rerun.

## Configuration type and snapshot checks

ES8BalancedGeometry.Configuration is a real-point configuration (source interface: point : Fin n → Point; xOrder : StrictMono (fun i => (point i).1); generalPosition : orientation nonzero for ordered distinct triples). Exact definition: D:/科研/math agent/erdos-szekeres-sat-main/tmp/balanced49_transfer_20261026/sources/es7_es8_bounds_81_319_v1/formal/sources/ES8BalancedGeometry.lean:7; cup definition :12. This is a textual type inventory only.

Current file hashes are recorded in source_hashes.json (81 records). manifest_hash_comparison.json compares 49 acquired formal source paths against the locally held public package MANIFEST.json: 49 matches, 0 mismatches. Literal/Data records were hashed without reading their bodies. The remaining records are receipt/interface snapshots; the large Lean binary archive was neither opened nor rehashed.
