# 旧blocking profiles的单次分组预测

不重新读取source、degree、load或packing。原完整profiles中所有未选center至少有四个不同责任clone；因此在同一二元冻结N模型中，任何引入非旧center的选择至少须真正移除四个当前clone，直接关闭k≤3 out／k+1 in改进范围。

对342个恰四blocking owners的未选center，按完整 `blocking_old_roles` 排序四元组分组。

**可推翻正预测：** 至少一组包含≥5个不同实际center。这只提供4out5in的必要入口；即使命中也不测试它们的同时余度，不产图、不判成功。

若max group size<5，则同一二元域的4out5in也不可能：任何新center至少需移除四个blockers；四个真正被移除的角色固定后，全部五个新增center都必须为非旧center且拥有完全同一四元组。重新加入任何已移除旧center会使真正移除数少于四，已被min4阻挡。因此必要组不足五即NO。未选center具有五个以上blockers也不可能进入四移除域。

输出每组完整责任roles／对应旧center、组内实际新center、组大小hist/max、预测结果和精确scope。只读旧profiles一次，保留其实际tab或literal-backslash-t格式，不复写旧文件。

继承同D4 case累计2.783706889 CPU，新准备0.10，授权postprocess自身≤1 CPU，全部进程成本计入，不重置。完成停止，不运行4out5in候选、pair、solver或更大局部阶梯。
