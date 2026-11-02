请独立审查一个具体数学构造规则，而非查新或评价一般研究策略。不要修改项目文件，不运行新搜索。请读取以下文件：

research/ddp/refresh_20261029/f5_complementary_triples/PROOF_SCOPE.md
research/ddp/refresh_20261029/f5_complementary_triples/check_local.py
research/ddp/refresh_20261029/f5_complementary_triples/RESULT.json
research/ddp/breadth_20261027_wave4/mizuno_d3_source/construction.json
research/ddp/breadth_20261027_wave4/mizuno_d3_source/bfs_certificate.json

要检查的承重命题：在该30顶点四正则控制器上，将纤维改成F5^3，并使用所列四个互为真实逆的port矩阵与四条方向，是否确实给出简单20正则、3750点、D≤3的完整关系构造？本次没有导出3750边表，也没有绑定degree20的公开下界，不声称新纪录。

重点攻击：
1. 中央edge的36种三列秩检查是否真的涵盖所有三步非回退路径，是否缺共享边/环乘积条件。
2. 相邻控制器的六平面pencil是否给每个源坐标全部125终点，尤其反向归一化与中心平移是否一致。
3. 对非相邻/相同控制器，继承的缓存路径存在性数据是否足够，原标签/port是否有错配风险。
4. 明确区分此规则成立、完整图已独立边表核验、以及纪录新颖性三个结论。

请给出：ACCEPT / ACCEPT_WITH_QUALIFICATIONS / REVISE；至多三个关键问题或反例，或明确可接受的证明范围。报告实际读取的文件与是否执行代码；模型同意不当作独立确定性证明。不要要求重验103个旧图或恢复D2。
