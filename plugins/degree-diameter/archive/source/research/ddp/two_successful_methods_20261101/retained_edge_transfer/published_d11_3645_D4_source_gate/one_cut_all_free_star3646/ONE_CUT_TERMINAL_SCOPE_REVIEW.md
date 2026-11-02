# 单cut完整NO；两cut非base-base子域的缓存推论

**支持RESULT的精确scope，不新增数值。** 已读 [run.cpp](run.cpp)、driver、[RESULT](RESULT.json) 及 `CACHE_BINDING.json`。源3645/20044、7个free点及旧743 holes继承；代码逐条检查全部20044实际edges，分类阈值严格为label<3444的base与其余inserted，不假定edge/vertex transitivity。

程序以 `holes & ~(B3(u)|B3(v))` 计算最大star遗漏，完整域无新根pass；1993个R3 roots复用、1652个新的半径3支持查询，best cut(108,1643)仍缺305。不存在partial/raw score冒完整通过。原sourceD4未重验，candidate旧根BFS和旧旧检查均0，准确含义是**后阶段未进入**，不是旧旧已安全。原RESULT caseCPU2.893111119/15及输入适配失败计账保持原文。

固定一cut的唯一合法spoke pool为 `P=F∪{u,v}`，大小≤9，最大star合法并支配所有子star；全部cutends在P，使源多源距离与删边后距离相同。因此这20044个最大star的新根失败足以关闭同源**任意单cut、单新点、仅new-old spokes、无其它改边**，不限某个spoke子集。旧“插入层至少一edge可补全”的预测已反驳；不排一般3646图或其它手术。

## 分类上界接成两cut必要条件

root对保存 [ALL_EDGES.tsv](ALL_EDGES.tsv) 的一次后处理给出下表；本review不重算分类maxima。

| 原edge类别 | 完整edge数 | 对743 holes的最大覆盖 | 保存的见证 |
|---|---:|---:|---|
| base-base | 18485 | 438 | (108,1643) |
| base-inserted | 914 | 356 | (1568,3510) |
| inserted-inserted | 645 | 338 | (3505,3510) |

现只作纸面推论：删除两条distinct原edges `e1,e2`，允许共享端点，添一个z，仅加z-old spokes。删边后的可用pool恰为 `P=F∪ends(e1)∪ends(e2)`，大小≤11。每个原满度端点至少失1再补1，原free端点只更低，所以最大star仍合法；所有合法子star均被它支配。

所有被删边两端都在P，故同一重启引理适用。新根≤4必须用两edge端点球补齐原holes。若两edge都非base-base，每条最多覆盖356，于是

`|holes∩B3(ends(e1)∪ends(e2))| ≤ 356+356=712 <743`。

重叠与共享端点只会减少union，不能破坏这个上界；最大star至少还缺31个old targets，任何子star更不可能。因此：**同源two-cut-onlystar若想成功，至少一条cut必须是base-base。** 这不是已枚举两cuts，也不表示含base-base就通过；对应的old-old距离仍另验。结论只含删至多两原edges+一个新star，不含旧旧repair、其它helpers/source或一般11D4。

本review未parse源、读二进制球、重算TSV、枚cut、BFS或求解；两只读metadata/code进程CPU合计0.001110001秒。没有新图、参数、Lean、外审或下一次数值授权，完成即停。
