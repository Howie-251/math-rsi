# 实际G1新角色的full-neighborhood复制：独立all-pair/prefix依据

2026-11-01。本suite仅处理degree86与98，source固定为actual accepted G1／346516，不读取原H边表、不使用83链源、不依赖producer邻域生成逻辑。

## 独立实际输入接口

从G1 literal一次全流读得到其全部边E、各点degree和J={342290+h:h=0..4225}的完整邻域。J独立，全部N(J_h)落在原H label<342290，且这些4226个非空邻域两两不交、union大小342225。J的实际度数分为65个80度diagonal role、4160个81度off role及1个65度hub role。这里不靠GF表或原GQ坐标推出这些输入事实，也不重新测试G1的旧根D3；G1数学D3与具体kernel是已接受前提。

模板PARENT_4226_ROLE_ACTUAL_NEIGHBORS.tsv保存全部实际邻居。对每case，每条literal新增边必须属于其指定模板，simple＋每newrole实际degree等于模板长度，严格推出其完整邻域相等。这个证明不只比较Nsize：实际每条边先作了模板成员检查，随后才用cardinality完成双向绑定。

## Full-neighborhood端点替换给所有点对的真Walk

记newcopy x的parent center为c∈J，且N(x)=N_G1(c)。old–old继承保留的完整G1。对old目标v≠c，取G1的c到v最短路≤3并替换首端点；到c本身，取任意u∈N_G1(c)，x–u–c给真Walk2。

两newcopies若center相同，使用一个共同parent邻点，长度2。center不同且parent距离2／3时，替换最短路两端点即可；若parent距离1，可用x_c–d–c–x_d三步。这些都是实际old G1内点，不含未来copy。当前具体J还独立且N两两不交，因此不同role的parent centers实际距离3，所有不同role copies也没有1／2步捷径。

这些类别覆盖每个case所有点对，而不是从68个roots外推。每个newrole的完整邻域都已绑定到此接口，故未做BFS的新增根也有逐端点证明。

## 每个prefix与degree

从同一G1出发，以任意顺序添加当前case的newroles。每次新增点到parent及此前copies的路线仅用parent内点；其所需路线在插入时已存在，future vertices不会被当作内点。所有old G1边保留，所以每prefix已经D≤3。

source角色邻域实际load≤1。每role最多复制r次，使每old source点new load≤r；source degree≤82，所以maxdegree≤82+r。newvertexdegree就是其source role的实际65／80／81，不超cap。实际每顶点degree与全部新邻域/保旧body绑定后得到两个case的精确hist，不把G1的演化原GQ中心邻域错当新的pins。

## exact D3与未测范围

无new–new边。不同role模板不交，同role模板非空，所以同role copies之间距离恰2，不同role copies之间距离恰3。old J不会获得任何新边，因为全部newpins都在old H而非J。

最后newhub复制parent hub的N，其邻域与parent first-clone J_0的N不交，也不包含J_0；old J_0的邻域未改变。因此该pair无1／2walk，D≤3给距离恰3。本次原定last-hub BFS直接保存了三步Walk，无额外old-root BFS或source geometry验证。

degree86只测16904新增点中的68个，余16836不测；degree98只测67616新增点中的68个，余67548不测。每case的preselection在candidate读取前由parent literal role Nsizes确定，last-new-block的65diag＋两个first actual off＋hub，不据结果换root，不假轨道或坐标平移。测量和全部点对证明分别保存。

此为两图独立数学验收依据，不是新的公开优先权声明或本agent的Lean运行记录。root状态、Wiki与旧冻结包不修改，不派其他multiplicity。
