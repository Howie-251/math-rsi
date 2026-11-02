# 同一个C33共同路线问题 数学反例攻击

请只做静态数学审阅，不运行程序/搜索/安装/改文件。不是回顾全部历史或设计模板清单。

共同目标：C是33点简单4正则图，含指定11个不交K3，其余边为简单2因子F。对任意不同且非邻点对，要求恰3步非回退路线。这比普通直径≤3强，是现有固定F5满秩与六平面覆盖证书的控制器充分条件。尚无合格33控制器/4125主图，所有旧完整SAT为UNKNOWN。

请读以下两份新证明并找错：

1. research/ddp/refresh_20261029/controller33_route_capacity/PROOF.md
   核心：36 NB3条，其中2t(v)回根、2q(v)到邻点，必须覆28非邻，故t+q≤4；每块对两F边的triangle/四圈贡献产生weighted L(v)≤3；同块对m≤3且3必perfectmatching，三重块对在商上构成matching。特别核含弦四圈、shared-endpoint的权2和不同edge-pair不重计。

2. research/ddp/refresh_20261029/controller33_C11_exact/DERIVATION_PACKAGE.md
   固定C11同时平移下1800合法设置已全失败，但请不以数值失败代替证明。核三商分类、loop6<8 exactNB3门、无loop triangle位移a,b,c的10项相位多重集L，ΣL=5a、ΣL²=9a²+4b²+4c²；覆盖9个非邻phase迫冗余6a，故a²=b²+c²，标签旋转矛盾。请重点查漏路线、错误相位规范、把多重集误当集合或把普通D3条件混入。

现有独立小统计：C30成功没有4圈；C33best含3个4圈、t+q≤3，通过全部新必要cuts却仍缺28个非邻有序对。因此不能声称cuts已切掉当前难区或保证提速；新的cuts只改变完整模型传播，不改变合法候选范围。

返回：逐证明PASS或精确反例/缺口；若PASS说清作用域，避免泛泛路线建议。不要声称已核数值、Lean或公开纪录。
