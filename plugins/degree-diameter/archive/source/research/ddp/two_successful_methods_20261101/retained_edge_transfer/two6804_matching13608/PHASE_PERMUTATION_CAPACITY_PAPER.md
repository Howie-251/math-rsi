# 非translation phase permutation：容量矩阵与π(0)=0归一化

状态：纯paper确认模型接口；没有运行矩阵、卷积、source/field/BFS、solver、Lean或外审。常数offset的root实际328回执另存，本文件不重算。root唯一8秒native HiGHS/15CPU批次独占数值，后续normal/fibre阶段不在本批。

## 1. 实际scope与一次cross

两份给定6804源的每个相位均有567点，旧degree13，相位邻接矩阵Q为12×12 circulant，增量±1/±4各权3、6权1，故Q行和13且Q对称。新增perfect matching从copy0的相位i整体映到copy1的相位π(i)，其中π是任意C12标签排列；相位内部仍可任意bijection。

π不必是involution。一个copy0→copy1的bijection已经定义无向perfect matching；反向是π^−1，而不是要求π²=id。也不要求它是source图automorphism。

`CONSTANT_PHASE_PAPER.md`的一次cross化简仍适用：≤4跨copy路有1或3cross，3cross加至多1旧边必有相邻两cross并沿同一matching边回退。因此任何≤4可达点都有一次cross/至多3旧步路线；没有漏掉3cross的潜在收益。

## 2. C(π)是每root的精确普通walk计数，不是distinct覆盖

采用row-source convention：Q[i,j]是旧一步从相位i到j的邻点数，Pπ[i,π(i)]=1。对a步旧prefix和b步旧suffix，实际跨copy相位walk计数是

    Q^a Pπ Q^b。

因为同一相位内每个实际顶点有相同旧phase row-profile，匹配怎样安排该相位的567个点不会改变suffix计数。每个具体prefix端点跨到phaseπ(k)后，再走b旧步到phase j的数量都是Q^b[π(k),j]。故

    C(π)=sum_(a,b≥0,a+b≤3) Q^a Pπ Q^b

逐项就是每个sourcephase root到目标phase的普通一次cross walk总数，包含旧回退/重复target。真实shortest routes是其中子集，因此D≤4的必要条件是所有144项C[i,j]≥567；这不是充分条件，允许很多walk落到同一实际target。

变量P[u,v]∈{0,1}，12个row-sum=1与12个column-sum=1恰表达permutation。各capacity系数为

    sum_(a+b≤3) Q^a[i,u]·Q^b[v,j]，

所以144容量行都线性。不能以浮点fractional doubly-stochastic矩阵代替实际binary π后称相位门可行。

因Q行和13，P是permutation，任何π的每row计数和固定为

    sum_(l=0..3) (l+1)13^l = 9322。

这比12·567大，仅说明total walk预算没立即不足，不能由总量推出每个targetphase或每个实际point被覆盖。

## 3. π(0)=0对容量可行性是严格WLOG

令T_k为输出phase平移：T_k[r,r+k]=1，取k=−π(0)，定义π'=T_k∘π。于是π'(0)=0，且row convention下

    Pπ'=Pπ T_k。

circulant Q与T_k可交换，因此

    C(π')=sum Q^a Pπ T_k Q^b
          =sum Q^a Pπ Q^b T_k
          =C(π)T_k。

这只重排目标列；144项下界均为相同567，所以可行性完全不变。每个原π都能如此归一化，故固定P[0,0]=1不丢**容量模型**的解；反向显然是原全域的子域。这个论证无需输出phase平移在实际6804 fibre图上成为automorphism，不能借商模型的对称性宣称两实际point匹配图必同构。

如果phase classes大小不相等、目标阈值不统一或Q非circulant，这种WLOG不自动成立；当前给定接口正好满足。copy0/1互异，所以π(0)=0也不产生graph selfloop。

## 4. 反方向不必另加144行

反向perfect matching为Pπ^T。Q对称，且全部a+b≤3的求和域交换a,b不变，所以

    C(π^−1)=sum Q^a Pπ^T Q^b=C(π)^T。

因此检查forward全部144项≥567，也等价保证reverse同一**容量必要门**。无需额外强制P对称或π自逆；那会不当缩小原whole-phase-permutation matching域。

## 5. 输出含义与停止边界

若找到feasible π，只得到普通walk容量必要条件，没有distinct567-target覆盖、normal/fibre兼容、实际simple13608/degree14/D4图或新纪录。必须保存actualbinary π并明确capacity-only，不能把0objective success写成图验收。

若此必要binary模型INFEASIBLE，数学范围只排固定源上**每个整相位映到一个整相位π(i)**的全部point匹配；π(0)=0不丢其容量域，故不能再用换输出shift或常数offset逃避。native rawstatus与其证据按实际回执保留；time-limit/无incumbent是UNKNOWN，不作INFEASIBLE。

matching若把同一个sourcephase内不同points分到多个输出phase，则没有一个12×12 permutation P代表它，不在此scope；其它source、更多cross边、改旧边及一般14/D4也未排。root批次之外不枚normal/fibre、换πseed或重开窗口，完成paper即停。
