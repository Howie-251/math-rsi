# Assignment→shift：同K19 case最终UNKNOWN

本批是从原60s全CNF反馈改变算法的结构化分解，不是继续该timer。原73,800vars/172,800clauses的60s UNKNOWN历史保持。继承已保存B(i,j;r,s)低19bit exactpointmask，m=popcountB；没有重旧endpointDP/sourceparse/BFS或H233928枚举。

一次nativeHiGHS只解轨道排列bottleneck：1296个sigma binary＋整数z，72rowcol等式与1296条Σm*x≥z，maximize z；matrix504144nnz与m/MIP原始矩阵均已保存。identity暖开始actualmin18，setSolutionkOk。configured5s、实际solver5.149360753CPU，TimeLimit/nodes0；返回另一个sigma，独立整型核出/入各1以及全部1296容量，actualmin19。该值不是已证最优或图成果；rawdual−668/巨大gap也不是有用的最优界。只冻结这一个真实返回sigma，不sigma2。

固定sigma后直接实际pointOR，所有24624(i,j,k)义务保留：684shiftvars，36exact-one，每组18Sinzaux，共1332vars/26586clauses（24624OR+36ALO+1908AMO+18合法t0gauge）。实际819432pointliterals/823950总literals，CNF3223120bytes，point长度19..50，空clause0。每条的支持数就是选中36个B的popcount和，而实际覆盖依赖19个坐标的OR，不能用min19替代。

唯一CaDiCaL argv分离“-t”“20”与固定sigmaCNF，实际stdout“c UNKNOWN”、exit0/无s状态行；733139conflicts、1107747decisions、28991118propagations、15090restarts。native实际19.961063CPU；没有SAT或UNSAT。即使未来该固定sigma得到rawUNSAT也只关该sigma的未经proofcheck模型，不能升级K19族NO；本轮连该sigma是否可行也仍UNKNOWN。

未进入正例分支：source literal parse0、1368候选0、producer BFS0，f9 fresh草稿不运行。A/B/m及完整矩阵/冻结sigma/整数capacity核/CNF/native原始输出都保存，可供有新依据的后续问题复用；不将其计为图、参数或Lean。

原prior64.297950855含上轮63.697950855＋fresh草稿prep.5＋root只读处置.1。新增prep.5、MIPchild5.62724、shiftbuild.425342、SAT19.961063、parent约.010712，执行累计90.822314663；最后只读stdout/摘要保守.1，最终90.922314663/100CPU。MIP/shift各唯一窗口，无失败，无重置。全部终态，停止，不sigma2/第二solver/seed/自动续时；剩余预算不是续算许可。K19完整匹配族仍UNKNOWN/未排；0旧sourceD4/DP/field/Lean/付费，0新图/参数/Lean。
