# Rajiv252两cut／四星：完整域NO

固定actual Rajiv252/630/all5源，删两条顶点不交的原边，四端点接新z；n253/m632，旧点保持5度、新点4度，不改其它边。全部cut端点均在P，最短P路线可在最后cut下游P端点重启，所以d_(G−cuts)(P,t)=dG(P,t)，source closedR3(P)恰好判新根R4。

事前至少一组P通过的预测被完整域反驳：630边的198135无序边对剔除2520共端点对，195615全部完成；四球最大覆盖仅222/252，0newroot pass，因此0candidate旧root BFS/0完整图。252次新问题深3支持不是source D4全验收，原D4继承；没有source单pair诊断。

原RESULT/TERM实测case2.151099672/10CPU保留，编译亦在原账内；本次只补root和Wiki文档，不新数学、不重置预算。共同paper见[核读说明](../../stale_record_transfer_d4D4/source104_two_cut_star105/variants_a_b/TWO_SOURCE_SCOPE_REVIEW.md)。结论仅固定源/two-disjoint-originalcuts/one4star/nootheredits，不排一般253/(5,4)或repair/第三cut/其它源。全STOP，0新图/参数/Lean/独立方法。
