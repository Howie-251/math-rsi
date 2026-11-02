# 一个 fixed-Q/free-P 规则的实际结果

新规则确实放开了 P 的 C5 对称，没有重启旧双自由1560变量窗口。保存的65625个 Q 经 full-valid 必要 profile 筛后，41064个合格；23661个仅 i_Q 超界，744个仅 j_Q 超界，156个两项都超界。按覆盖最大、旧编号最小唯一选定 **Q index1361**，old contribution113，blocks `[140,209,262,266]`，含5个 concurrent-Q edges/triangles。Q 未重新生成，全部筛选与8代表/full40 profile已保存。

固定该Q满足565条原 far clauses，剩515条只含自由 P。模型保原780个 P edge variables、40个 matching equations，并加入已读证明的 unrestricted 必要式 `i_P+3j_Q<=3`、`i_Q+3j_P<=3`，不加 girth5。P最初包含所有collinear选择；必要cuts产生450个不同的显式负单位，余330个尚未显式强制false。另用780个 existential boundary variables 表达存在 `x_e=1,x_g(e)=0`，只排已接受为无解的共同C5子域，不施加新WLOG。最终 CNF9750变量、51436子句。

合法的唯一 SAT 搜索调用实际读取并解析全部51436子句，返回 **`s UNSATISFIABLE`，exit20**；18 conflicts、87 decisions，stderr为空。它只支持这个确定Q/Pfree模型的 raw solver UNSAT，不是 timeout；没有记录或核验 formal UNSAT proof。其他41063个合格Q未启动Pfree求解，整个 asymmetric-Q族仍 UNKNOWN，原 unrestricted GQ80也仍 UNKNOWN。

执行接口两次失败透明保留：首次 preexec 试图把继承hard6升为20，CaDiCaL未exec；随后本机不接受单argument `-t19`，即时exit1且未读CNF/search。两次都不是数学UNKNOWN。修正为旧本机worker实际使用的 `['-t','19']` 后，仍复用完全相同Q/CNF，才完成上面唯一实际search窗口。失败结果分别为 `ASYM_INITIAL_LAUNCH_FAILURE_RESULT.json`、`ASYM_COMMAND_FORMAT_FAILURE_RESULT.json`，没有借此重筛Q、重建模型、延长搜索或更换solver。

实际合法solver pid3247844已结束，child CPU0.016967，parent0.004431706；含原read/action/joint、Q筛/模型准备、两次启动失败及保守准备charge后，wholecase **4.886162516/30 CPU秒**。读入/search/result证据在 `ASYM_ACTUAL_SOLVER.stdout`；`ASYM_SOLVER_TERMINAL.json` 和当前 `ASYM_TERMINAL.json` 为实际最终终态。0候选图、0source/candidate BFS、0重C5/sideenum/field/GQ。按授权停止，不Q2、不第二search。
