# H9十三度：旧候选缓存、停止范围与v4580路线解释

本报告只读已有邻接、literal、报告及mask缓存。新构图0、solver0、新BFS0，不改主Wiki，也不复验原103图。

## 原40步与joint capacity是否已有可用输入

已有newborn扫描明确记载：40个新增点的所有邻点都在原base标签51417以下；它们在最终图中互不相邻。`accepted_family40.json`保存40个literal邻点集，`frozen91.json`保存原91个star-minus-one mandatory集与剩余guard预算。

但是，现有40个接受证据大多是当时增强后的current graph全R4覆盖，不是“每个集合均在原51417上静态全覆盖”的候选池。原base静态证据直接具备首个51418的完整pin集，以及单独核对的v3962 mandatory控制；不能从后续current覆盖反推所有集合在原base覆盖。旧37失败的完整guard masks则是原51417绑定，续53的mask/证据绑定各自动态base；不存在可以直接混成原51417静态packing的完整池。

原流程是按顺序贪心接受并更新degree，不是joint packing求最优。旧ordinary-clone的63/343全局packing属于不同固定core及完整邻域规则；原51417/fullNv和最终40 newborn的fullNv停止范围只排完整邻域clone，不排star-minus-one加guards。不同helper可以共享旧pin，受剩余度数限制；只禁止同一个helper内重复旧pin造成重边。原native相同mask按最小标签去重也仅针对单个helper覆盖，不能转成全局旧pin互斥。

root的新literal账指出：旧失败中38个mandatory集在最终51457仍全部free，因此不应先把未成功归因于贪心锁端口。当前先做一个真实完整guard预算问题，比立即重排41个新点更直接。

## 原失败v4580到底试过什么

prototype4580的唯一原满邻点是45089；mandatory9为[4628,9574,14663,20519,26997,33721,37436,40798,44310]，因此真实最多可加4guards。原51417缓存漏2752点（2724core、28extras）；13239个eligible guards、13186个不同非零mask，43个uint64/列，每个目标有1828至3985个列支持。旧程序已完整排除零、一、二guard；没有找到这个prototype的三/四guard模型或排除回执。

之前唯一完整四guard MIP属于另一个prototype51445/删35572，current51457上750目标、13026列，最终UNKNOWN；其强proxy否定也只覆盖那个对象。不能以它禁止v4580首次完整<=4覆盖，也不能借此重启51445旧timer。

v4580原缓存仍可用于解释机制，不能冒充当前2755目标/13057列的完整绑定。当前guards还包括新增点，原列去重代表也可能随degree变化失效；需使用root已经准备的实际current完整矩阵。

## 为什么必须多guard联立，而不是寻找一个自由proxy

在mandatory之外，45089没有与其实际core邻域完全相同的eligible old-free guard proxy。旧缓存单列覆盖最大的4个guard恰好是45089的真实free邻点3579、4280、5025、2195，各自覆盖1095、1089、1086、1072个缺项，四者联合却只覆盖1941/2752；它们重叠很强。以3579为首列的最互补二列是2195，联合1820。一次只读mask贪心控制得到[3579,2195,50584,50901]，联合2490，仍非可行证书；不能以262残项作为继续追分的理由，也不是完整四列求解。

真正共同结构是被删首步：对任何mandatory九点的R4缺项，prototype4580到它的任一长度<=5路线都必须先走45089，否则其首个邻点属于mandatory，和缺项定义矛盾。因此新的guards需要替代这个首步之后的多个路线分支，完整联合覆盖模型才在检验正确问题。

更强的直接一阶proxy证书N(45089)包含于closedB1(mandatory∪guards)，在<=4预算下已经不可能：五个原满点137、577、1254、50015、50828均未被mandatory closedB1覆盖，它们的eligible closedB1支持分别为{6209,50795,50889}、{5619}、{10136,50901}、{47095,47679,48482,49163,49460,49879,50584,51298,51323}、{39121,42510}。五组两两不交，至少需5guards。五个目标原degree13，保边40步不能给它们加边，所以当前51457支持只会进一步缩小，不会出现新增点破坏此下界。此结论只排这个强proxy证书；长R4路线可以绕过它，不能据此判四guard主模型无解。

## 当前唯一可证伪问题与停止边界

root已选择`refresh_20261029/d13_v4580_fourguard/`：在实际51457 source上，这9 mandatory加最多4个不同当前free guards，能否覆盖完整2755个当前缺项。当前报告的13115 eligible guards与13057 unique masks都有目标支持，但支持非空并不保证四列联合可行。预算和真实handle以root自己的PREDICTION/回执为准；本代理不另跑solver、BFS、proxy kernel或joint41模型。

若找到guard集合，仍须按保全部旧边、当前degree和完整选邻点R4验证接受51458；若完整UNSAT，只关闭本固定mandatory/current矩阵的<=4域；UNKNOWN不排除它。原base41点joint packing现在既缺统一静态覆盖绑定，又不是38个候选的实际卡点，不应抢先启动。

准确输入和来源路径、缓存覆盖数字、五组proxy支持及限定范围保存在ANALYSIS.json与READ_SCOPE.json。
