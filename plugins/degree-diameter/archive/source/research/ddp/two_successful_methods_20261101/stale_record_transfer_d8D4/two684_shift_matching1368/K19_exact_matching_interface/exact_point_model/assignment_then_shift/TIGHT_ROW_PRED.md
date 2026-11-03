# 事前预测：一个非平凡紧轨道对的packet平移拼接

旧full60s与fixed-sigma20s均终态UNKNOWN，绝不重启。不σ2，不新source/DP/BFS/field。仅读已保存B和冻结sigma；同case上限100，继承90.922314663，新prep保守.2，实际诊断soft1CPU/hard3。

选sum packet sizes恰19、且至少2个non-singleton packets的(i,j)，按nonempty packet数最少、再i,j字典序冻结一个。若无这种行就记录，不改选另一宽松题。可推翻预测：此代表紧行虽总数19，仍因必然重叠不能铺满C19。

先查是否某两packet差集A-B=C19；若是则任意相对平移都有重叠，total19⇒union<=18，严格排该冻结sigma。否则精确不交拼接：largest packet shift0作为全行旋转gauge，依size降序枚剩余non-singletons的19shifts；memo(index,occupied)，singletons可任填剩点。total19使disjoint packing恰等point cover。找到解只证该行，可反驳本预测，不是globalmatching；完整无解才排fixedsigma。预算未完域则UNKNOWN。各阶段原solverstatus不改，K19全族始终不能由单行/单sigmaNO外推。
