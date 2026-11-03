# 可证伪预测P1得到具体支持：bestID68的offset无法修复0→10

在计算路线像之前已冻结 `PREDICTION.json`：缓存bestID68应存在某个controller slot，即使让每条真实短路线的像独立任意平移，最大并集仍不足16。实际找到了最简单的一类证据：**0→10的全部长度≤4路线恰为两条异向rank3超平面路线，任意平移的并集恒为12。** 因而固定此best的四个global矩阵和branch向量，不论添加何种逆一致global或edge-local offsets，都不可能达到D4。没有扩查其他1023项、重新BFS或优化offset。

## 预测、输入与完整路线范围

输入仅为 `wave11/binary72_tight_words/best_parameters.json` 的passer68：四label的矩阵列依次

`[2,4,8,1]`、`[14,4,8,9]`、`[12,7,2,4]`、`[8,1,2,4]`，

branch vectors为 `[1,3,11,8]`，inverse labels `[3,2,1,0]`，现有offset为零。原source controller与缓存controller邻接相同；本次没有加载其他passer。

对所有341个长度0至4的labelword（含立即回退）先计算其total linear map及controllable columns/image，再从全部72根确定对应controller endpoint，共24552条路线。每个controller pair都保留所有真实route及其multiplicity，没有只保留最短路、去掉backtracking或仅统计rank。

5184个controller slots中，1188个没有任何单条rank4路线。以每根fiber的零向量为起点、offset0时，414个controller slots仍漏点；这些是72个指定input rows的slot计数，**不是**缓存全图12384个普通无序坏对。逐slot详表在 `controller_pair_routes.json`；全部word的矩阵/列/像/法向量在 `word_images.json`。

## 最小证据slot 0→10

完整≤4walk枚举给出的两条路线为：

| labelword | 长度 | controller顶点路线 | 可控列（向量用四bit整数） | 像空间 |
|---|---:|---|---|---|
| 0020 | 4 | 0–18–37–64–10 | [14,9,7,1] | U={0,1,6,7,8,9,14,15} |
| 322 | 3 | 0–54–29–10 | [2,15,11] | V={0,2,4,6,9,11,13,15} |

没有长度0/1/2路线，没有第三条长度3/4路线。U和V均有8点、rank3。按坐标x=x0+2x1+4x2+8x3，

`U=ker(6·x)={x:x1+x2=0}`，

`V=ker(9·x)={x:x0+x3=0}`。

法向量6和9不同，在F2上即独立。共同core为K={0,6,9,15}，维数二、大小四。任意两个affine translates U+s、V+t的两个独立线性方程总有四个共同解，故

`|(U+s) ∪ (V+t)|=8+8−4=12<16`，对任意s,t成立。

改变edge offsets或source fiber初值只会分别平移这两个像空间，不改变方向。因此这不是offset0当前并集碰巧差四点：**所有offset都恰差四个目标**。固定两个controller fibers之间至少有16×4=64个无序坏对；只此slot已足够排除固定T/b的offset修复，不需要扫描其余slot。

offset0、输入零向量时，未覆盖点恰为{3,5,10,12}。假如有第三条路线给出法向量6 XOR 9=15的超平面（offset与前两者形成同一pencil），三个超平面即可盖满16；但当前controller slot没有这条额外路线。这个观察是解释现有缺口，不是已经实现的新route或搜索计划。其他矩阵/branch向量可改变0020的rank或两条路线的方向，本证据没有排除它们。

## 成功对照说明缺的是互补覆盖结构

root的已继承F3成功fixture在同一controller的另一个slot 0→1：reduced word BD，其四个修补路线ADBD/BADD/BBCD/BDCB给四个rank3超平面，各27点，共同core9点，且所有81个source fiber输入均覆盖81目标。证据为父目录 `ternary_success_fixture.json`，本次只读取，没有重复运行。

F3 fixture的四个不同方向在二维商空间形成完整pencil：`9+4*(27−9)=81`。本binary失败slot有两个不同方向，只有 `4+2*(8−4)=12`；在F2中完整pencil需三个方向。这里不是“rank3路线很多所以应当覆盖”的计数直觉，而是具体方向的数量及交集结构。两个fixture的controller pair不同，未声称它们是同一word集合的逐项域变换。

## 成本、范围与后续状态

本次纯cached-best路线代数CPU0.110552秒，单worker，1CPU秒进程硬限未触及。未生成新图、未BFS、未重枚举规范chart、未扩1024、未搜索offset。实际best的D5/12384仍只复用root旧检查，不当作本次新增距离测量。

P1被这个slot证实；反驳条件没有发生。结论只覆盖固定controller、固定bestID68的T和b、任意合法offset；不是所有1024个global候选或整个edge-local family排除。`candidate_slots.json`提供少量全部真route展开，供另一个代理独立做translation-cover上界；当前两异向超平面公式已给自包含证明。下一步由root据成功/失败对照决定，不自动扩展。
