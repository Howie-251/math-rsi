# 独立数学审阅

**PASS_WITH_APPLICATION_SCOPE。** 已全文核 `PROOF.md`：三交的四pair共同成本、四交matching计数、三份C4上界均正确。新加强 `a4<=tau-r` 也成立，其中 `r=max(0,4Delta-40)` 明确用于本项目的**21点**域。语义审阅same-family/provisional；没有运行81谱、18谱或其他全矩域，未改主稿。

## 核心无序计数

固定不同点u,v，由它们作exclusive pair的四交外边对唯一写成

    G=T+u，J=T+v，T避u,v。

以u-only边为左部、v-only边为右部，该关系确为matching：一条G确定唯一T，因H简单，其partner只能是T+v。故

    h_uv<=min(d(u)-lambda(u,v),d(v)-lambda(u,v))<=D2-lambda(u,v)。

每个无序外边对只有一个exclusive无序pair；固定uv后用u-only角色定向并不会产生第二个外边对，因此sum h_uv=n4，没有因子二。若同一四核还属于其他边，也不会增加固定G/uv的partner数。

合法middle必须含u,v且避T，故c(G,J)<=lambda(u,v)只是安全上界；没有把所有含uv的边反向当成合法middle。

记t=n4。相对基线二，lambda1的负差被丢弃，得

    C4<=2t+(D2-3)a3+2(D2-4)a4
       =2t+(D2-3)tau-(D2-1)a4
       <=2t+(D2-3)tau。

相对基线三只有lambda4留下正差，得

    C4<=3t+(D2-4)a4
       <=3t+(D2-4)floor(tau/3)。

本次实际应用D2>=7，所需系数非负均已满足。第二行用floor替换时应保留D2>=4的使用范围；不应把这个特定替换的推导无说明地用于D2<4的其他参数。正文已说明当前应用D2>=7，所以这不影响本项目调用。

再与4t及ell_max(tau)*t取min合法：它们都是同一H的独立安全上界，不要求各自松弛优化器能同时实现。

## 三交的共同成本

G,J三交时，每个合法middle有唯一两个不同attachments，分别位于A=G\J及B=J\G。这给唯一cross pair；每份middle只计一次，所归属类别容量至多该pair的lambda。四个cross pair彼此不同，所以其非负tau成本总和确<=全局tau，g4定义正确。

独立重算全部256个整数向量，得到g4(tau0…12)：

    8,9,10,11,12,12,13,13,14,14,15,15,16。

特别，不能因为某个特殊度域有容量十二就把C3<=12n3推广到一般H；当前g4松弛只按显示的tau给上界。

## 最高度行给a4新界

现在明确设原顶点数21，取最高度点v。令a1_on、a4_on分别为v行共度一／四的邻点数。对每个lambda=1,2,3,4，逐值精确恒等式为

    C(lambda-1,2)=lambda-2+1_{lambda=1}+1_{lambda=4}。

paircover使该行恰含20个不同邻点，五元性给行共度和4Delta。因此

    tau_row=4Delta-40+a1_on+a4_on。

若4Delta-40>=0，令r=4Delta-40，行外lambda4点对数为a4_off，则

    tau=tau_row+tau_off
       >=r+a4_on+3a4_off
       >=r+(a4_on+a4_off)=r+a4。

行与行外pointpair域不重叠，没有把其他最高度点的行再加一次。若4Delta-40<0，则r=0，而全部lambda4各花三份tau，直接有a4<=floor(tau/3)<=tau。综上

    a4<=min(floor(tau/3),tau-r)。

故在当前D2>=7应用，可把四交baseline三项进一步改为

    C4<=3t+(D2-4)*min(floor(tau/3),tau-r)。

一般n点对应行常数是2(n-1)，即4Delta-2(n-1)；40来自n=21，不能脱离该范围照搬。新界不需要最高度点唯一，也不要求任何pointpair成本在最高度行达到全部tau。

## 明确反例攻击及实际tiny核

尝试了：同一四核产生多个候选partner、把无序外边对数成两个方向、tau全部集中于最高度行、lambda4全部位于行外、r=0的低行预算，以及多个最高度点并列。上述证明分别以H简单的唯一替换、canonical u-only定向、行／行外不交域及r分支处理；未发现当前应用范围的反例。

`TINY_CHECK.py` 实际exit0、CPU0.009098秒：

- 穷尽g4的256个输入；
- 穷尽20邻点行的degree整除直方图，加0…8份行外lambda4与lambda3，36126个抽象行／行外配置均满足行恒等式及新a4界；
- 20个实际paircover简单五元H样例（11点14边，lambda<=4，D2>=7）直接枚举无序外边和合法middle，核h matching、sum h=n4、C4各界及一般n版行界；包含实际C4=2的非零例。它们是反例攻击，不替代上面的普遍证明，也没有冒称21/35实例复现。

完整样例与计数在 `TINY_CHECK.json`。新a4界及主稿原容量均可交由root继续应用；此审阅没有宣称任何谱已经染色或全局新下界已经完成。
