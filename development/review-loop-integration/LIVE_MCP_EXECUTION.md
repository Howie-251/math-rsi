# 打包桥接的真实模型执行

这是开发期间实际运行记录，不是安装指南。没有改全局MCP配置、读取/复制认证token或重置CLI原生权限；复用本机现有登录。Python桥接是本仓实际`mcp-servers/*/server.py`，并非通过已加载宿主服务名间接假定文件位置。

## 调用办法

在MathRSI根启动临时Python执行，使用`importlib.util`加载随包测试模块中的`Client(env, cwd)`，没有执行其`unittest.setUp`，因此未设置fake CLI。Grok使用`mcp-servers/tests/test_grok_exec_bridge.py`，Antigravity使用对应测试模块；各Client的SERVER明确指本仓server.py。

env继承本地运行环境，CLI路径由`shutil.which`或已有`.local/bin`提供，仅在shell缺少代理时从现有服务注册的代理env取值，未输出这些值或其它配置。两条桥接本次设置600秒上限。依次发`initialize`、`notifications/initialized`和`tools/call`，保留初始化与最终原RPC envelope；使用Client已有队列收取进度和最终ID，在结束时`close()`回收本次服务。没有新增产品客户端或调度程序。

## Grok首轮

调用`grok`，工作目录为本克隆根，显式请求`grok-4.7/xhigh`、read-only、`read_file,grep,list_dir`和50轮上限。prompt为[GROK_BUNDLED_RECHECK_REQUEST](GROK_BUNDLED_RECHECK_REQUEST.md)：核新route适配、RR Step3/4边界及PythonMCP实际接口。创建新会话，旧设计意见通过真实原文文件给它。实际约602.14秒收回`isError=true`，正文为`grok timed out after 600s; no automatic retry`，`stopReason=null`，会话`c595a50a-684c-4720-88b2-961af7b7f0f7`。原envelope见[GROK_BUNDLED_RECHECK_RAW](GROK_BUNDLED_RECHECK_RAW.json)。字段报告`model=grok-4.7`、`effort=xhigh`；没有有效终稿，不能据这些字段计作成功回答或成稿审阅通过。未自动重试。MCP执行器自身成功保存错误并退出零，不等于模型请求成功。

## Antigravity跨进程续接

新的本仓Antigravity服务调用`antigravity-reply`，只传原threadId `1ad5d3b8-d2e7-4d79-8c3a-b2dd65ff5ec9`与[GEMINI_BUNDLED_RECHECK_REQUEST](GEMINI_BUNDLED_RECHECK_REQUEST.md)。它通过已有持久状态和原生conversation恢复原会话的cwd/model/effort；没有在reply中换配置。

实际65.20秒返回`isError=false`、`model=gemini-4-argon-high`、`effort=high`、`status=SUCCESS`，同threadId。原envelope见[GEMINI_BUNDLED_RECHECK_RAW](GEMINI_BUNDLED_RECHECK_RAW.json)，[正文](GEMINI_BUNDLED_RECHECK_RESPONSE.md)完整保存。它重新静态读取八份发生变更的技能段落，逐条确认上轮六组具体关切已解决，未执行程序。reviewer Memory update原文已追加，不由Root代写。

这项实测建立“本仓Python服务→真实CLI→持久原会话→模型回答”的证据，不表示没有CLI/登录的新机器已经自动可用。61项离线测试另覆盖首轮/续接/失败等协议；数学内容核验、模型静态阅读、实际程序测试分别报告。
