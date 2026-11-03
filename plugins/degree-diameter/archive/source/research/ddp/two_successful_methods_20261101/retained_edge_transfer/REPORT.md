# 两张升度保边扩张图已生成，公开比较待定

已真实导出graph_d21_D3_n3900.edges（3900点、40500边、max21）及graph_d22_D3_n4125.edges（4125点、45000边、max22）。新增根分别150、375；每次加入前对其20个原始邻域pins做当前完整R2覆盖及度数检查，全部0遗漏，含所有此前新增点。RECIPE_d21/d22.json保存每一步精确pins和完整计数。

两张图由已接受3750源的保边扩张引理保证D≤3，阶数超过D2 Moore界，故D恰3。未重跑旧3750根BFS；root独立字面边表验收待完成，未冒称独验。

固定25中心平面块的30变量容量问题：k1精确opt6，243节点、0.000744361CPU；k2精确opt15，1317节点、0.02934157CPU并达到全容量上界。k2的375克隆更达到任意原始完整20邻域克隆的全局容量界。k1的150只称块规则最优，不称任意中心packing最优。

总实际CPU0.399614746秒，1worker；源edge文件读取1次，旧D3重验0，无旧solver复启。ROOT_REQUIRED_NOTES：comparison pending、confirmed record false；两个新图不得并入confirmed public improvement。参数式推广与来源边界见PROOF.md。

本批已终态。未自动试其它度数、填剩余slots或扩展clone规则；未生成全部前缀。RESULT.json/TERMINAL.json、脚本、controller向量、两份recipe、两张完整边表均已保存。
