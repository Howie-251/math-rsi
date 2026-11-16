# 从收件到下一次任务输入

沿用项目已有 STATE.json。若已有同等短视图/生成器，直接用它；本 helper 不要求所有题采用 JSON。父调度只在接纳或更正事实后写 `current_context`；旧字段仍是历史原件，`status` 由真实宿主状态维护。worker 不直接写共享状态。

`base/tools/current_context.py` 提供 `write_current(path, current)`，原子替换这个区块而保留历史和 Goal 状态。原 STATE 若设置 `current_context_view` 指向已有阅读视图（相对 STATE 所在目录或绝对路径），每次写回会自动再生成该视图；领域收据适配器也走同一个调用，不依赖事后手工补写。没有配置时保持原行为。

调用者组织与本次研究相关的已知结果、当前对象、在途、未闭义务和停止范围；不能仅凭文件存在填“成功”。已消费的终态过程、旧恢复指令与过时 next 留在原状态的历史区或原件中，current 只保留其对当前决定的结论和证据链接，不把整条历史不断追加进短视图。领域已有收据可用适配器读取，DD 的实例见 [D5 批次接口](../../../../plugins/degree-diameter/references/d5-blocking-batches.md)。

收件时用终态结论替换同任务的准备/运行摘要，勿把完整 RESULT、编译重试及每轮
review逐份嵌进 current；细节沿原件或原状态历史取用。`current_question`、
`next_action` 与实际在途须表达同一当前决定，避免旧的并列下一题继续被当作待办。
这是同一次收件的整理，不增加独立归档阶段或按字数拦截正常研究。

收件顺序：读取作者与所需核验原件 → 父调度决定实际接受范围 → 更新 current → 生成下一输入 → 再按原授权派工或发 review。暂停时允许整理已有事实，不启动数学。

任务已有只在结束时写出的最终 JSON 时，在派工前把它的路径登记为
`current_work.in_flight.<任务名>.terminal_result`，READY 任务也登记；不要指向运行中更新的进度文件。
生成任务或 review 输入时，helper 若发现该最终文件已经存在，会要求父调度先收件写回，
防止把已结束的 UNKNOWN 仍当作尚未开跑。父调度可以记录“作者已返回、独验待做”，
移出这项在途后派独验或其它独立工作；不必等到数学验收才更新事实。
它不解释结果、不自动加成果或改 Goal，也不拦截已经运行的其它任务。
路径可以是绝对路径；CLI 中相对路径以 STATE 所在目录为基准，Python 调用传 `state_dir`。
没有登记最终路径的旧任务仍沿原收件契约；这个薄检查不能约束绕过 helper 的直接派工。

```bash
python3 /path/to/MathRSI/base/tools/current_context.py \
  --state /task/STATE.json --output /task/CURRENT_RESULTS.txt
python3 /path/to/MathRSI/base/tools/current_context.py \
  --state /task/STATE.json --request /task/next-request.json --output /task/next-input.txt
```

`next-request.json` 的最小例子：

```json
{
  "review_mode": "reuse",
  "question": "把已经审过的保边归纳用于下一有界批次，回交每步真实检查。",
  "reuse_scope": "同一源图合法性进口与保边引理；不含未生成实例的检查",
  "changes": [],
  "prior_reviews": [{"path": "/task/review-original.txt", "scope": "保边＋当前新根覆盖推出全点对上界"}]
}
```

`review_mode` 为 `task`、`reuse`、`delta` 或 `new`；有承重变化时用 `delta` 并列出具体变化。`routes` 可选，指定 current 中相关停止条目；不填或空列表时全部带入，不能只给“请参考历史”。误填路线名会报错，避免默默漏掉证据。`reuse` 需要原件与准确范围且不能同时声明变化；`delta` 未提供旧审阅时不声称复用。代码不判断声明是否数学上正确，也不发模型请求。输出写明继续保留实例验证及最终审阅要求。

NEXT_SESSION 只指向此当前视图和必要下一动作；旧报告标明覆盖时段。生成视图可再生，不手工维护另一套数字。审阅者原文/Memory 仍独立保存，当前事实不能伪装成其观点。
