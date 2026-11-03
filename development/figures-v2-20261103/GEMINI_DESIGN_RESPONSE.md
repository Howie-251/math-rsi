这里为您提供一套可直接发给 **GPT Image** 的双图定稿方案（含空间构图、精简英文文案、关键箭头方向、冗余删减说明及可直接复制的生成 Prompt）。

---

### 一、 冗余删减与防歧义设计（对比旧图）

1. **图 1（`01-evolution.png`）删减与修正**
   - **删去虚假历史回路**：移除旧图中 `mathrsi-base-v1 → Specialize by problem → Task workspace → Research experience` 的分支回路（该画法会把 Property B / ECC 误导为由 `v1` 解出，若直接塞入 DD 更会误导为 `v1` 解出了 DD）。
   - **删去重复节点**：移除旧图中上下两个完全重复的 `Task workspace (Proofs · Checks · Wiki)` 卡片。
   - **实线化 `v2`**：旧图中 `v2` 是虚线框 `Next iteration`，现改为实线已发布版本卡片。
   - **用拓扑位置替代免责声明**：`Property B` 与 `ECC` 放在第 1 列 `v0`（散装 ARIS 研究期）；`DD research evidence` 作为独立绿色输入卡片放在第 2 列下方（无任何来自 `v1` 的输入箭头），与 `v1` 一起汇入 `mathrsi-meta-evolve` 产出 `v2`。

2. **图 2（`02-workflows.png`）删减与压缩**
   - **压缩插件条高度**：旧图底部插件区有 5 个橙色子框 + 5 根双向虚线 + 2 个大徽章，占用了过多纵向空间。现将 5 个阶段接口文案精简为紧凑单行标签，下方并排放置 **3 个插件徽章（Property B / Degree–diameter / ECC draft）**，腾出底部空间给独立紫色的 `mathrsi-meta-evolve` 外层带。
   - **不堆砌 v2 四条增量细则**：`Verify` 卡片仅将原 `Lean when useful` 精炼为 `Direct Lean or full audit`，不在图内堆砌参数、定理名或防御性长句。
   - **视觉隔离外层进化与单题求解**：底部紫色 `mathrsi-meta-evolve` 带用清晰分隔线（`Offline between runs · never mutates active task`）与上方 5 个解题阶段隔开，杜绝“第 6 阶段”误读。

---

### 二、 图 1 设计：`01-evolution.png`（三列演进构图：`v0 → v1 → v2`）

#### 1. 空间布局（3 列纵向对齐 + 跨列演进箭头）
* **标题区（左上）**
  * Title: `MathRSI: from ARIS runs to an evolving math harness`
  * Subtitle: `Standalone research origins (v0), unified workflow & plugins (v1), and evidence-driven evolution (v2)`
* **第 1 列（左，`x ≈ 18%`）：`v0 · Pre-Harness Origins`**（浅灰青底框，无统一 harness）
  * 顶部小标签：`Standalone ARIS skills · No unified harness`
  * 内含胶囊：`research-lit` · `proof-writer` · `proof-checker` · `lean-formalize`
  * 下方并列两张研究来源卡片：
    * 橙色卡（`#C86D3B`）：`Property B research` / `Hypergraph coloring proofs & checks`
    * 蓝色卡（`#5364A6`）：`ECC research` / `Error-correcting code bounds`
* **第 2 列（中，`x ≈ 50%`）：上半部 `v1` + 下半部独立 `DD research evidence`**
  * **上半部（青色主框 `#0F4C5C`）**：`MathRSI v1`
    * 核心卡：`mathrsi-base (v1)` / `5 subworkflows · Embedded ARIS skills`
    * 插件组：`Property B plugin`（橙色实线） + `ECC plugin [draft]`（蓝色带 `draft` 胶囊）
  * **下半部（独立绿色输入卡 `#2E7D5B`，与上方 `v1` 留白断开、无连接线）**：
    * `DD research evidence` / `Historical degree–diameter archive · proofs, failed routes & checks`
* **第 2→3 列桥接（中右上方，紫色卡 `#8060A6`）**：`mathrsi-meta-evolve`
  * 副文：`Classify · Modify in place · Review & use`
* **第 3 列（右，`x ≈ 83%`）：`MathRSI v2`（深青实线大框 `#0F4C5C`）**
  * 核心卡：`mathrsi-base (v2)` / `In-place upgrade on v1 · Formal target & transfer updates`
  * 外层技能卡（紫色 `#8060A6`）：`mathrsi-meta-evolve` / `Outer-loop harness evolution`
  * 插件区（3 张紧凑卡片）：
    * 绿色卡（`#2E7D5B`）：`Degree–diameter plugin` / `Constructions · Transfer · Obstructions`
    * 橙色卡（`#C86D3B`）：`Property B plugin`
    * 蓝色卡（`#5364A6`）：`ECC plugin [draft]`
* **底部图注**：`Historical research evidence informs plugins and reviewed in-place base upgrades across versions.`

#### 2. 关键箭头方向（严禁画反或画串）
1. `v0 (Property B & ECC research)` $\xrightarrow{\text{Distill workflows \& plugins}}$ `MathRSI v1`（实线青色箭头，水平向右）。
2. `MathRSI v1` $\xrightarrow{\text{Existing v1 base}}$ `mathrsi-meta-evolve` $\rightarrow$ `MathRSI v2`（上方主干演进箭头）。
3. `DD research evidence`（中列下方独立绿卡）分出两条清晰箭头：
   - 向右上入 `mathrsi-meta-evolve`（紫/绿箭头，标签：`Workflow lessons`）；
   - 向右直入 `v2` 的 `Degree–diameter plugin`（绿色箭头，标签：`Domain methods & archive`）。
   - **严禁**画任何从 `MathRSI v1` 指向 `DD research evidence` 的箭头。

#### 3. 图 1 直接可用 GPT Image Prompt

```text
Create ONE high-resolution 16:9 landscape architecture infographic (3840x2160) for a mathematics research agent framework. All visible text must be English with exact spelling. Clean editorial research diagram, crisp near-vector boxes, thin precise arrows, generous whitespace, no 3D, no gradients, no watermark.

COLOR PALETTE:
- Background: warm off-white #FAF8F5
- Core harness (v1/v2): deep teal #0F4C5C
- Meta-evolution: restrained purple #8060A6
- Property B: copper orange #C86D3B
- ECC: muted indigo #5364A6
- Degree-diameter (DD): forest green #2E7D5B

TITLE (upper left): "MathRSI: specialize, learn, evolve"
SUBTITLE: "From standalone ARIS runs (v0) to unified workflows (v1) and evidence-evolved v2"

THREE-COLUMN LEFT-TO-RIGHT EVOLUTION LAYOUT (v0 -> v1 -> v2):

COLUMN 1 (Left, x=17%): "v0 · Pre-Harness Origins"
A light neutral container with header "v0 · Standalone ARIS runs" and sublabel "No unified MathRSI harness".
Inside top, compact monospace skill pills: "research-lit · proof-writer · proof-checker · lean-formalize".
Inside below, two stacked source cards:
1. Copper orange card (#C86D3B): "Property B research" | "Hypergraph coloring proofs & checks"
2. Muted indigo card (#5364A6): "ECC research" | "Error-correcting code bounds"

ARROW v0 -> v1:
One clean horizontal teal arrow from Column 1 to the upper container of Column 2, labeled "Distill 5 subworkflows & plugins".

COLUMN 2 (Center, x=50%), split into TWO SEPARATE vertical zones with clear whitespace and NO arrow between them:
- UPPER ZONE (Teal container #0F4C5C): "MathRSI v1"
  - Main teal card: "mathrsi-base (v1)" | "5 subworkflows · Embedded ARIS skills"
  - Below it inside v1, two plugin cards:
    - Copper orange card: "Property B plugin" | "Hypergraph coloring"
    - Muted indigo card: "ECC plugin" with small pill "draft" | "Error-correcting codes"
- LOWER ZONE (Independent forest-green source card #2E7D5B, completely separate from v1, NO arrow from v1):
  - Title: "DD research evidence"
  - Subtitle: "Historical degree–diameter archive · proofs, failed routes & checks"

BRIDGE BETWEEN COLUMN 2 AND COLUMN 3 (Upper-middle right, x=67%, y=30%):
A compact purple card (#8060A6) titled "mathrsi-meta-evolve" with subtitle "Classify · Modify in place · Review & use".
- A horizontal teal arrow goes from "MathRSI v1" into "mathrsi-meta-evolve".
- An upward purple/green arrow goes from "DD research evidence" into "mathrsi-meta-evolve", labeled "Workflow lessons".

COLUMN 3 (Right, x=85%): "MathRSI v2" (Solid deep-teal outer container #0F4C5C, representing the released v2):
Inside stacked cleanly:
1. Deep teal card: "mathrsi-base (v2)" | "In-place upgrade on v1"
2. Purple card (#8060A6): "mathrsi-meta-evolve" | "Outer-loop evolution skill"
3. Domain plugin group at bottom of Column 3:
   - Forest green card (#2E7D5B): "Degree–diameter plugin" | "Constructions · Transfer · Obstructions"
   - Compact copper badge (#C86D3B): "Property B plugin"
   - Compact indigo badge (#5364A6): "ECC plugin (draft)"

ARROWS INTO COLUMN 3:
- Short arrow from the purple bridge card into "MathRSI v2".
- Direct horizontal green arrow from "DD research evidence" (Column 2 lower zone) into "Degree–diameter plugin" (Column 3 lower zone), labeled "Domain methods & archive".
- Do NOT draw any arrow from MathRSI v1 to DD research evidence.

BOTTOM CAPTION: "Historical research evidence informs domain plugins and reviewed in-place base upgrades across versions."
```

---

### 三、 图 2 设计：`02-workflows.png`（五阶段内层工作流 + 底部独立 `mathrsi-meta-evolve` 外层带）

#### 1. 空间布局（自上而下 4 层结构）
* **标题区（左上）**
  * Title: `Inside MathRSI v2`
  * Subtitle: `Five adaptive problem-solving subworkflows and an independent outer evolution loop`
* **第 1 层（顶部双窄横幅，保持原图精华）**
  * 深青总控条（`#0F4C5C`）：`mathrsi-research` | `Select entry · Consume evidence · Choose the next step`
  * 浅青共享记忆条：`Research wiki & evidence — reused and updated throughout` | 右侧胶囊 `research-wiki` · `wiki-enrich`
* **第 2 层（中部主干：5 张等宽阶段卡 `01`–`05` + 3 条稀疏回流弧线）**
  * **01 Prepare**：`Clarify the problem` / `Survey sources & errata` / `Fix the formal target` | 胶囊：`research-lit`
  * **02 Route loop**（紫边框强调）：`Propose → Challenge` / `Probe → Revise → Recheck` / `Cross-model discussion` | 胶囊：`auto-review-loop (math)` · `research-review`
  * **03 Prove**：`Derive · Construct · Compute` / `Delegate focused tasks` / `Connect to original target` | 胶囊：`formula-derivation` · `proof-writer`
  * **04 Verify**：`Assemble the argument` / `Check coverage & evidence` / `Direct Lean or full audit` | 胶囊：`proof-checker` · `lean-formalize (optional)`
  * **05 Handoff**：`Readable complete proof` / `Reproducible materials` / `Wiki & recovery notes` | 胶囊：`render-html`
  * **回流箭头（保持原图 3 条）**：
    * 卡上方长弧（`Prove → Prepare`）：`Targeted literature lookup`
    * 卡下方短弧 1（`Prove → Route loop`）：`Rethink the route`
    * 卡下方短弧 2（`Verify → Prove`）：`Repair / local return`
* **第 3 层（中下部：紧凑版 `Domain plugins` 横幅）**
  * 顶行标题与接口：`Domain plugins — specialize each stage`（右侧：`Task + obligation ⇄ Result + scope + evidence`）
  * 5 个对齐微标签（对应 01–05 虚线双向箭头）：`Sources & baselines` | `Transfer & probes` | `Domain constructions` | `Domain certificates` | `Reproduction inputs`
  * 底行并排 **3 个彩色插件徽章**：
    * 橙色（`#C86D3B`）：`Property B — locks, traces, bad pairs`
    * 绿色（`#2E7D5B`）：`Degree–diameter — constructions, transfer, obstructions`
    * 蓝色（`#5364A6`）：`ECC (draft) — codes, cosets, distance`
* **第 4 层（底部新增：独立紫色外层带 `mathrsi-meta-evolve`，`#8060A6`）**
  * 与上方解题层之间有一条清晰虚线分隔，微标签：`Independent outer maintenance · never silently edits base during a run`
  * 带内从左到右 4 个紧凑节点（水平箭头串联）：
    1. **起点**：`Workspace evidence`（`Successes · Failures · Corrections`）
    2. **分类（Classify）**：4 个分流标签
       - `Base`（青色标）
       - `Plugin`（绿/橙标）
       - `Task → stays in workspace wiki`（浅青标，就地指向任务 Wiki）
       - `Defer`（浅灰淡化胶囊，无出边）
    3. **执行链**：`Modify in place → Review → Use → Adopt`
    4. **回馈终点**：`Next base & plugin version`（引出一条干净的左侧外沿上行箭头，指向 `mathrsi-research` / `Domain plugins` 并标明 `Next version`，不混入当前题目的阶段箭头）。

#### 2. 关键箭头方向（图 2）
1. **五阶段内层**：`01 → 02 → 03 → 04 → 05` 实线正向箭头；上方 1 条文献回流弧（`03 → 01`），下方 2 条局部回流弧（`03 → 02`、`04 → 03`）；与插件层保持 5 对短双向虚线。
2. **外层 `mathrsi-meta-evolve`（绝不画在 `05 Handoff` 右侧充当 `06`）**：
   - 输入：从工作区证据进入底部紫色带左端 `Workspace evidence`；
   - 内部水平流：`Workspace evidence → Classify (Base / Plugin / Task / Defer) → Modify in place → Review → Use → Adopt`；
   - 输出分流：
     - `Task` 分支：短标直接指明 `Stays in task wiki`（不进 base）；
     - `Defer` 分支：浅灰静默胶囊，无输出箭头；
     - `Adopt` 终点：沿图右侧/左侧边缘画一条紫色虚线/细实线箭头回馈至 `Next base & plugins`，明确标注 `Upgrades next version`。

#### 3. 图 2 直接可用 GPT Image Prompt

```text
Create ONE high-resolution 16:9 landscape technical workflow infographic (3840x2160) for a mathematics research agent framework. Figure 2 of a coordinated two-figure set. All visible text must be English with exact spelling. Clean editorial diagram, crisp thin arrows, soft tinted cards, monospace skill pills, generous whitespace, no 3D, no gradients, no watermark.

COLOR PALETTE:
- Background: warm off-white #FAF8F5
- Core workflow: deep teal #0F4C5C
- Adversarial review & outer meta-evolution: restrained purple #8060A6
- Property B plugin: copper orange #C86D3B
- Degree-diameter plugin: forest green #2E7D5B
- ECC draft plugin: muted indigo #5364A6

TITLE (upper left): "Inside MathRSI v2"
SUBTITLE: "Five adaptive subworkflows with domain plugins, plus an independent outer evolution loop"

FOUR-TIER VERTICAL LAYOUT:

TIER 1 (Top bars):
1. Narrow deep-teal orchestrator bar (#0F4C5C): "mathrsi-research" on left; "Select entry · Consume evidence · Choose the next step" on right.
2. Directly below, light teal shared-memory band: "Research wiki & evidence — reused and updated throughout" on left; monospace pills "research-wiki · wiki-enrich" on right.

TIER 2 (Upper-middle main row — FIVE equal-width stage cards 01 to 05 connected by short solid right arrows):
- Above the cards: ONE thin purple curved arrow from 03 Prove back to 01 Prepare, labeled "Targeted literature lookup".
- Inside the row:
  - 01 Prepare: "Clarify the problem" / "Survey sources & errata" / "Fix the formal target" | Pill: "research-lit"
  - 02 Route loop (purple border): "Propose → Challenge" / "Probe → Revise → Recheck" / "Cross-model discussion" | Pills: "auto-review-loop (math)" · "research-review"
  - 03 Prove: "Derive · Construct · Compute" / "Delegate focused tasks" / "Connect to original target" | Pills: "formula-derivation" · "proof-writer"
  - 04 Verify: "Assemble the argument" / "Check coverage & evidence" / "Direct Lean or full audit" | Pills: "proof-checker" · "lean-formalize (optional)"
  - 05 Handoff: "Readable complete proof" / "Reproducible materials" / "Wiki & recovery notes" | Pill: "render-html"
- Below cards 02-04: TWO short backward curved arrows:
  - 03 Prove -> 02 Route loop, labeled "Rethink the route"
  - 04 Verify -> 03 Prove, labeled "Repair / local return"

TIER 3 (Lower-middle compact strip — "Domain plugins — specialize each stage"):
Connected to the 5 stage cards above via 5 short vertical dashed bidirectional arrows, with right-side interface label "Task + obligation ⇄ Result + scope + evidence".
- Top compact row of 5 aligned role cells: "Sources & baselines" | "Transfer & probes" | "Domain constructions" | "Domain certificates" | "Reproduction inputs"
- Bottom row of THREE equal colored plugin badges side by side:
  1. Copper (#C86D3B): "Property B — locks, traces, bad pairs"
  2. Forest green (#2E7D5B): "Degree–diameter — constructions, transfer, obstructions"
  3. Muted indigo (#5364A6): "ECC (draft) — codes, cosets, distance"

TIER 4 (Bottom independent purple band #8060A6 — separated from Tier 3 by a clean horizontal divider labeled "Separate outer loop · never silently modifies base during an active run"):
Left header badge: "mathrsi-meta-evolve".
Inside the band, a clean left-to-right flow of three compact boxes:
1. "Workspace evidence" ("Successes · Failures · Corrections")
2. "Classify": four compact tags inside:
   - "Base" (teal tag)
   - "Plugin" (green/copper tag)
   - "Task -> stays in workspace wiki" (light teal note)
   - "Defer" (muted light-gray faded pill, no outgoing arrow)
3. "Modify in place → Review → Use → Adopt"
From "Adopt", route a clean purple feedback arrow up along the outer margin pointing to the Base & Domain plugins tiers, labeled "Upgrades next base & plugins".

BOTTOM CAPTION: "Inner workflows solve the current problem; outer meta-evolution upgrades future versions from verified evidence."
```

