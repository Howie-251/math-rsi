# 十二元案例：同一 H 上自适应选锁与完整必要域

这是M4663、结论m(12)≥4664的既有计算机辅助候选，不研究更高参数。完整作者证书664355参数实例严格；独核重建全部域/trace并Fraction复算20例，未做全表第二概率实现，也无本参数Lean。

## 输入与覆盖

原输入任意有限简单12元H、≤4663边。最小顶点nonB商化得paircover与总度≤55956。均衡染色和整数覆盖约束留下91…782共692个v，补边到恰4663。旧M4660起点93失效，必须包含91/92。

91…497零锁。498…693对每个实际最低度d枚举ceil((v−1)/11)…floor(55956/v)，先算一锁；不strict才取单位伙伴。池大小s_d=2(v−1)−11d，伙伴完整范围d≤e≤B=d+floor((55956−vd)/s_d)。s_d≤0不能视作排除，driver会报failure；所有采用分支有正池。

若实际d,e双锁不strict，在同一H取共同单位邻点池

    t=v−2−[11d−(v−1)]−[11e−(v−1)]，
    R=55956−vd−(e−d)，d≤f≤d+floor(R/t)。

全部f及两种真实三锁迹都要算。排序是重标同一三点并同步位置/trace；f可小于e，不能丢掉。694…782用独立低度三锁存在引理统一收尾，D满足Z=(D+1)v−55956>0、22Z>[11(D+1)−v+2]²，枚举δ…D排序三元组与两迹。固定693/694是数学分支，不能让运行到多少CPU决定切点。

全部计数：零锁407、一锁3914、双锁94640、条件三锁489700、统一三锁75694，总664355。不同父分支可能给同一排序三元组，这不是互异型数/超图数。

## 概率、舍入和成功输出

使用固定布局与同一失败事件的Σmin(A,B,C−D)。作者S=2^52，正概率系数ceil、删除权floor，再按floor权重重排最低q成本，保证定向上界。非负int64收缩先检查完整和上限，最终Python整数求和。最紧v659、双锁(63,82)，4503599103886333/4503599627370496<1，差523484163。

独核不导入scanner/概率模块，自己恢复全部d/e/f区间、两迹、count总M、度数/单位共度、693/694无缝分流；然后用原始Fraction概率另算20个tight/分界/池端点型，检查exact≤保存定向界<1。它没有重新求全部664355概率，域PASS与算术PASS必须分开报告。

## 可执行独核

从仓根复制所需目录到工作副本；脚本会写`DOMAIN_CHECK.json`与`RESULTS.json`。输入仅三份JSON（若归档压缩交付，先在副本解压为原名）：

```sh
PB_ARCHIVE="$PWD/plugins/propertyb/knowledge/archive"
PB_REPLAY=$(mktemp -d "${TMPDIR:-/tmp}/mathrsi-k12-XXXXXX")
cp -R "$PB_ARCHIVE/context/propertyb-k12-4664-20261029" "$PB_REPLAY/k12"
python3 -B "$PB_REPLAY/k12/independent/check.py"
```

必要输入`COMPLETE.json`、`CONDITIONAL.json`、`TAIL.json`；程序比较prefix+tail与complete的数学行。预期`COVERAGE PASS 664355`、20次独立Fraction replay及`PASS_MODULO_IMPORTS`，结果保留`complete_second_probability_replay:false`。历史独核2.926CPU秒；作者72.44秒，固定切点补跑70.61秒。检查器可执行不意味着依赖文献/概率见证/选点定理已被它形式证明。

原源：[独核check.py](../../../knowledge/archive/context/propertyb-k12-4664-20261029/independent/check.py)、[覆盖与舍入全文](../../../knowledge/archive/context/propertyb-k12-4664-20261029/independent/COVERAGE_REVIEW.md)、[完整证明](../../../knowledge/archive/context/propertyb-k12-4664-20261029/PROOF_M12_GE4664.md)。有效Grok静态审阅在声明进口下未发现实质问题，未执行程序，不补齐全表第二概率或Lean。

## 失败应导向哪一层

缺JSON是搬运缺依赖，恢复精确输入，不重跑研究。域键/trace/参数端点不等是覆盖或driver错误，先保留第一个差异与完整旧记录；不从表里删掉坏型。Fraction高于定向界是舍入/公式/排序方向问题，保存h与A/B/C/D。只有某个必要概率型不strict，而选择/覆盖都正确，才回到新真实结构或更好布局；不得用“没找到H实现”删除它。全表已strict且有效原题连接已有，研究在M4663收卷，不自动追更高参数。
