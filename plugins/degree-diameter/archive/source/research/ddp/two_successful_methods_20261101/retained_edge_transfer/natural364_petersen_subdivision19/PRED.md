# 新合作规则：Petersen10骨架的9条边细分，先检助手metric

自然364保边合作k≤14已闭；不能自动开始k15梯。本规则另有连接依据：所有helper都有oldspokes，避免tree叶＋无port父点的旧容量障碍；Petersen原diam2提供短内部路线。固定15条edge中9条各细分一次，H19/m24；10个原3度helper各接1oldport、9个2度细分helper各接2oldports，正好28。若可分配，目标364+19=383、全4regular。

旧freeports彼此source距5，≤5路径不可经两个port穿旧图回H。每helper须距每portowner≤4；此H的每点都是owner，故Hdiam≤4是必要条件。Petersen原diam2不保证细分后也过门。

预测：至少一个9细分pattern仍有Hdiam≤4；若无则关闭此固定Petersen/9single-subdivision合作族，不能靠28端口assign修复。若有，保存全部survivor Hadj，选第一个作后续精确assignment模型，不因此声称target383存在。

完整5005=choose(15,9) labelled patterns，允许同构重复但不漏，不计成5005图成果。Python一次helpermetric全19root BFS/每pattern；不解析source、不重旧balls/Hall/旧Petersen3D6、无target383 BFS/portassign/solver/Lean/ARIS。历史限定read未找到same helper规则终态，普通Petersen覆盖不同。

native CPU3s硬限，wholecase5CPU，read保守.5/prepare.25。输出每pattern exactdiam、直方图、survivoradjacency、首反例helper-to-oldport必要证据。无hit STOP此族，不换细分数/seed/骨架自动续试。
