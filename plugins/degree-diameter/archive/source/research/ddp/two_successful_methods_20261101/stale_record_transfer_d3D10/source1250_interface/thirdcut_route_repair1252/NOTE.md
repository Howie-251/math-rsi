# 固定 object4536 的三 cut + repair：完整有限域终态

本批没有新图。固定 Conder1250 的旧 object4536，保留 x–1178，允许移动 p∈{0,1,869}，第三条旧边避开原四 pins，两个方向且 repair p–h 为原图非边。实际 literal 给出 1865 条可选第三边、11178 个合法参数配置；9 个 g=1058 的 pilot 先跑，其余11169只跑一次。源 parse 成功一次，输入的 simple/cubic/label binding 通过；原源 D10 直接继承，没有原源直径 BFS。

## 预测与实测

P1 的9例全部支持：原 saved 缺点1058到两个 helper 的距离变成1/2，x→1178始终1，y→1178始终2。P2“此冻结域至少一个 both-newroot R10 通过”被完整11178配置推翻：全部都在 NEW_X 失败，both-pass=0，故没有逐旧根候选验收。新x BFS11178次；额外新y BFS只用于9个 pilot 的确定短路对照。不能从这里给整个候选的精确全图直径，也不能称原源验证。

P3 得到6/6对照支持：pilot 移p0三例 x→0=11，移p1三例 x→1=11。这是修原缺点同时撤走旧覆盖责任的具体损失。首反例 cut=(1058,725)、repair=(0,725)，实际最短路为 x–1058–933–635–274–146–82–34–18–6–2–0，长11，见 FIRST_FAILURE.json。移p869三例 x→869=10，因而这三例不是同一个 withdrawn-pin 障碍；但按 config10059/10629/10851，首缺点依次为1057/1056/1057、距离均11。先前“均为1057”的摘要错误在此按已存逐例数据更正，没有新算。P3从未预测p869失败。

整个域有5454配置修好了 x→saved1058，却没有一个完成新x全覆盖。分 moved-pin 的配置数、saved修复数和首失败区域记录于 ROUTE_CLASS_SUMMARY.json；这些是参数配置计数，不宣称互不相同的图，也不是所有缺点分布。实际每配置结果在 CONFIG_RESULTS.tsv，9例完整 withdrawn 最短路在 PILOT_PATHS.jsonl。

## 下一步的改变与停止边界

停止这一个冻结base、保x1178的 pin-transfer 域，不再给它续时或换随机seed。证据表明仅把saved远点变成直接pin，会撤走原pin的短路责任；即使转移p869能保住该pin，也仍遗漏远端区域1056/1057。旧缓存邻接给869–1234–1057的二步联系，1057并非869的直接邻点。若将来改变规则，应明确同时补偿被撤走的覆盖区域，而不是只修一个saved点。其他冻结base、其他保护方式、其他三cut/repair规则、多helper及一般(3,10)都没有被本批排除；也没有自动授权下一批。

## 真实费用与保存

首次编译成功，但 driver 源路径父级索引错误，文件未打开即退出，0候选/0BFS。该次原driver、日志、RESULT、TERMINAL和输入错误均以 INITIAL_PATH_FAILURE_ 前缀保留；其2.282222419 CPU全部继承。修正路径复用已编译binary，不重编译；成功native CPU0.191383，加driver/修正准备和最后只读摘要费用后，本地执行与摘要累计2.674601871 CPU；root随后一次只读旧metadata查询保守计0.1，最终本case累计2.774601871/20 CPU。RESULT/TERMINAL中的2.674601871保留为追加root只读费用前的原始执行历史。SOURCE_PARSE失败打开1次、成功literalparse1次。0 sourceD10验证/field/solver/Lean/ARIS，0新图/参数/Lean。数学严格NO仅针对上述完整11178配置域。
