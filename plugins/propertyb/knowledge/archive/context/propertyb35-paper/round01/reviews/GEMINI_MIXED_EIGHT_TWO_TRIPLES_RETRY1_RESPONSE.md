### 审阅结论

**通过（無須修改的實質數學缺陷）。** [EIGHT_MIXED_ONE_SMALL_TWO_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/EIGHT_MIXED_ONE_SMALL_TWO_TRIPLES_REPAIR.md) 關於「$|L|\le 18$、正族恰 8 個大小 3 或 4 的帶索引集合（至多一個 3 集）、負族至多 2 個三集與 19 個四集（無負一／二集）、每點正負總索引出現 $\le 7$」的可修復性證明邏輯閉合，分類與接口無遺漏。

---

### 逐項核對要點

1. **重複索引與預處理接口（第 5–6 行）**
   - 證明開頭先將相同的原負三集邏輯合併：這不改變「$R$ 不包含任何負集」的充要條件，且只減少或保持 $T \le 2$ 與各點總出現次數 $\le 7$。
   - 合併後所有負三集互不相同，因此固定紅點 $x$ 後，含 $x$ 的 $r$ 個負三集刪去 $x$ 必得到 $r$ 個**互不相同**的二元目標，這使第 5 節使用不同二元目標擴展數前 $r$ 項和 $S_3(r), S_4(r)$ 完全合法。
   - 正族與負四集保留全部原始重複索引：正族重集在五標籤多重圖 $J$ 中表現為平行邊（對應不同實際點）；負四集在各節中均按索引線性累加（第 5 節 $(t-r+v)h$ 與 $19-v$、第 6 節無 `upper_bound_weights` 的弱對偶），不要求負四集去重。

2. **純四集 $B \le 19$ 提升（第 1 節）与接口核對**
   - 對照 [EIGHT_POSITIVE_18_TWO_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/EIGHT_POSITIVE_18_TWO_TRIPLES.md)，負四上限從 18 升至 19 時：
     - 最大正出現 $\le 2$：$2(7/16)^3 + 19(7/16)^4 = 56595/65536 < 1$；
     - $k=4$ 四個不交餘組：$2\cdot 16 + 19\cdot 4 = 108 < 256$；
     - $E=3$ 非三角七型統一界 $144 \to 145 < 148$，三角解析界 $56 \to 57 < 144$；
     - $E \ge 4$ 中 $M_2=0$ 為 $56 \to 57 < 80$，舊 86 型為 $134 \to 135 < 178$；
     - 其餘高出現與 $M_2 \ge 6$ 分支僅依賴含 $x$ 的負四集數（由點度 $7-a_x$ 控制），不依賴 $B$ 總數。
   - 第 5 節中若唯一正三集已被 $x$ 命中，餘五正族容量為 $(4,4,4,4,4)$，此時原純四集第 4–6 節只依賴餘五族大小與 $a_x=3$（即 $r+b \le 4$），不依賴已被 $x$ 命中的三個正集大小，複用合法。

3. **低正出現 $\le 2$ 的共同負關聯計費（第 2 節）**
   - 由佔用乘積界與 AM-GM，將每點負四出現控制在 $b_4(v) \le 7 - a_v - b_3(v)$，得到：
     $$\text{badsum} \le \sum_v (7-a_v)\frac{p_v^4}{4} + \sum_v b_3(v)\left(\frac{p_v^3}{3}-\frac{p_v^4}{4}\right)$$
     扣除了負三已佔用的點度，未將同一點容量重複計給負四。
   - 唯一正三集與七個正四集下，正出現 $\ge 1$ 的點僅四類：$(1/3, \text{cap } 6)$ 共 $3-d$ 點、$(1/4, \text{cap } 6)$ 共 $28-d-2e$ 點、$(1/2, \text{cap } 5)$ 共 $d$ 點、$(7/16, \text{cap } 5)$ 共 $e$ 點，其中 $0 \le d \le 3, 0 \le e \le \lfloor(28-d)/2\rfloor$。
   - 手算核對最大值點 $(d=3, e=12)$：6 份負三關聯全分配給邊際最大的 $p=1/2$，總界為
     $$6\cdot\frac{1}{24} + 9\cdot\frac{1}{64} + 60\cdot\frac{2401}{262144} + 6\cdot\frac{1}{1024} = \frac{25600 + 36015 + 384}{65536} = \frac{61999}{65536} < 1.$$

4. **高正出現 $\ge 4$ 與雙三中心 $j=2$ 等號換色（第 3–4 節）**
   - 第 3 節 $k \ge 6, k=5, k=4$（不交或有交點 $y$）的候選數與阻斷界逐一核對無誤。
   - 第 4 節雙三中心 $x, y$（各正出現 3 次且正支持標籤不交）剩 $U$（3 集）、$V$（4 集）時，消去 $j = |U \cap V| \le 2$ 個被迫負三集 $\{x,y,z\}$ 後，餘下 $(3-j)(4-j)$ 個四紅候選 $\{x,y,u,v\}$。
   - 剩餘能阻斷候選的負集僅三類：含雙核負三 $p$ 個、恰含一核負三 $q$ 個、含雙核負四 $d$ 個，滿足 $p+q \le 2-j$ 及雙核負度預算 $2p+q+2d \le 8-2j$。
   - $j=0,1$ 時阻斷上界 $(4-j)p+q+d \le 10 < 12$ 及 $\le 5 < 6$ 嚴格；$j=2$ 時候選數為 2，阻斷上界為 2，取等號的唯一整數解為 $(p,q,d)=(0,0,2)$。
   - 在 $(p,q,d)=(0,0,2)$ 下，兩個被迫負三集 $\{x,y,z_1\},\{x,y,z_2\}$ 與兩個阻斷候選的負四集均同時包含 $x, y$，使 $x, y$ 各自達到正 3 + 負 4 = 7 的滿度，因此**任何其他負索引均不含 $x$ 或 $y$**，且原系統已無其他負三集。
   - 改 $x$ 藍、$y$ 紅後：上述 4 個含藍點 $x$ 的負集自動安全；其餘負集因不含 $y$ 不會縮減為負三集，全部保持為負四集；$x$ 星的 3 個正四集（因唯一正三集為 $U$）刪去 $x$ 成 3 個正三集，連同 $U, V$ 共 5 個大小 $\ge 2$ 的正集，點總出現不增，精確滿足 [FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md) 的調用前提。

5. **餘五族容量 $(3,4,4,4,4)$ 壓縮與星／三角解析界（第 5 節）**
   - $|U| = 19 - E \le 17 \implies E \ge 2$。
   - 二匹配恆等式 $C_3 = \sum_M (c_{w_M} - d_J(w_M)/2) \ge \frac{3}{2} M_2$ 對 $c_{w_M} \in \{3,4\}$ 成立；$M_2 \ge 7 \implies C_3 \ge 11 > 4r + (t-r) + v \le 10$。
   - $M_2 = 0$ 星型：中心外四組互不交，乘積至少 $3\cdot 4^3 = 192$；任取中心兩條圖邊對應的交點，命中率至少 $1 - (3/4)^2 = 7/16$（同組或含容量三組時 $\ge 1/2$ 或 $1 - \frac{2}{3}\cdot\frac{3}{4} = 1/2$），得 $C_4 \ge 192 \cdot 7/16 = 84 > 57$。
   - $M_2 = 0$ 三角型：五種邊重數 $(1,1,1),(1,1,2),(1,1,3),(1,2,2),(2,2,2)$ 在三角外／內含三集時分別給出 $C_4 \ge 9\cdot 12 = 108$ 與 $C_4 \ge 8\cdot 16 = 128$，且每個三角點至多 4 個橫截夥伴，故二／三／四目標擴展上界 $16/4/1$ 保持，總堵界 $\le 57 < 108$。
   - $1 \le M_2 \le 6$ 運輸與完整域：[INDEPENDENT_CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/audit/INDEPENDENT_CHECK.py) 從 10 個標籤對直接枚舉容量 $(3,4,4,4,4)$、$2 \le E \le 8$ 的全部 4,499 個標籤圖，在固定容量三標籤的 $S_4$ 作用下得 270 個規範鍵（259 個 $1 \le M_2 \le 6$ 必要鍵 + 11 個 $E=3, M_2=0$ 額外鍵），與 384 行運輸模板去重後的規範鍵集合完全一致。

6. **兩個 $E=2$ 邊界型的共享預算有理證書（第 6 節）**
   - 四類負來源 `N2`（大小 2，耗 $T, x, \text{total}$）、`T3`（大小 3，耗 $T, \text{total}$）、`Bx3`（大小 3，耗 $x, \text{total}$）、`N4`（大小 4，耗 $\text{total}$）完整覆蓋所有落入 $U$ 的負目標（含 $U \cup \{x\}$ 外點的負集不阻斷任何 $R \subseteq U$）。點負容量上界 $7 - g_p$ 忽略了 $x$ 已命中三正集的額外正出現，屬安全放寬；總數 $21 = 2 + 19$ 亦為安全放寬。
   - 手算核對 [SOLVE_TWO_E2.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/SOLVE_TWO_E2.json) 首份證書 `old59_0_E2`：54 個四點候選各取權重 $\alpha_R = 1/54$（27 個含點 0、27 個含點 1，無同時含 $0,1$ 的候選），對偶乘子 $\beta_T = 1/9, \beta_x = 1/27, \beta_{\text{total}} = 0, h_0 = h_1 = 1/54$（其餘 $h_p = 0$）。四類目標的左端最大值分別為：
     - `N2`：含 $\{0,1\}$ 之一時 $\le 9/54 = \beta_T + \beta_x + 1/54$，避 $\{0,1\}$ 時 $\le 3/54 < 8/54 = \beta_T + \beta_x$；
     - `T3`：恆 $\le 3/54 < 6/54 = \beta_T$；
     - `Bx3`：含 $\{0,1\}$ 之一時 $\le 3/54 = \beta_x + 1/54$，避 $\{0,1\}$ 時 $\le 1/54 < 2/54 = \beta_x$；
     - `N4`：含 $\{0,1\}$ 之一時 $\le 1/54 = h_0$（或 $h_1$），避 $\{0,1\}$ 時 $= 0$。
     總成本 $2(1/9) + 4(1/27) + 5(1/54) + 5(1/54) = 30/54 = 5/9 < 1$。
   - 手算核對第二份證書 `old59_15_E2` 的總權重和 $(107+42+96+65+66+52+1152+792)/2372 = 1$ 及總成本 $(2\cdot 264 + 4\cdot 99 + 5\cdot 32 + 5\cdot 33)/2372 = 1249/2372 < 1$，並核查了 [VERIFY_TWO_E2.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/VERIFY_TWO_E2.py) 與 [INDEPENDENT_CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/audit/INDEPENDENT_CHECK.py) 對全部 $2 \times 3876 = 7752$ 條 typed 目標列不等式的逐項驗證邏輯。

---

### 審閱範圍說明

- **實際閱讀文件**：
  - [proofs/propertyb35/EIGHT_MIXED_ONE_SMALL_TWO_TRIPLES_REPAIR.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/EIGHT_MIXED_ONE_SMALL_TWO_TRIPLES_REPAIR.md)（全文，1–121 行）
  - [proofs/propertyb35/EIGHT_POSITIVE_18_TWO_TRIPLES.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/EIGHT_POSITIVE_18_TWO_TRIPLES.md)（全文，1–125 行）
  - [proofs/propertyb35/FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md](file:///Users/rfy_naiveai/Desktop/aris4math/proofs/propertyb35/FIVE_SMALL_POSITIVE_ZERO_TRIPLE.md)（全文，1–31 行）
  - [context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/audit/REPORT.md](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/audit/REPORT.md)（全文，1–79 行）
  - [context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/audit/INDEPENDENT_CHECK.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/audit/INDEPENDENT_CHECK.py)（全文，1–105 行）
  - [context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/audit/RESULT.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/audit/RESULT.json)（全文，1–87 行）
  - [context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/VERIFY_MARKED_TEMPLATES.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/VERIFY_MARKED_TEMPLATES.py)（全文，1–68 行）
  - [context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/VERIFY_TWO_E2.py](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/VERIFY_TWO_E2.py)（全文，1–37 行）
  - [context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/SOLVE_TWO_E2.json](file:///Users/rfy_naiveai/Desktop/aris4math/context/propertyb35-paper/round01/twentyfour/p6_tail79_common_gate_20261020/SOLVE_TWO_E2.json)（第 1–120、550–1349、1800–2572 行，含兩份對偶證書完整權重與預算）
- **是否執行計算**：未執行外部程序（只讀靜態審閱）；已手算複核關鍵分數界（$56595/65536$、$61999/65536$、$5/9$、$1249/2372$）、`old59_0_E2` 的全部 3,876 條對偶列不等式，以及各驗證腳本的代碼邏輯。
- **未核部分**：按要求未重證舊純四集大域本身（僅核對接口與 $B=19$ 差值），亦未審閱 P6 實際調用方（caller）或全局 $m(5) \ge 36$ 的其餘分支。

