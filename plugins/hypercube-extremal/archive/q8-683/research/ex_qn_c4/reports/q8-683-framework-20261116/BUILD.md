# Q8 上界 683 框架说明页

主交付：`Q8_683_FRAMEWORK.html`，单文件、无外部字体或脚本依赖。直接用浏览器打开即可。图示、公式和样式均已内嵌；页末本地证明链接需保留原工作区。

内容重点：MathRSI 五阶段及贯穿的 wiki 读写、用户提出的上下界协同、近极值工作带和残差奖励、从候选到精确证书的衔接、683 定理关键中间值及真实审查范围。未收入完整证明。

源稿：`Q8_683_FRAMEWORK.md`。修改源稿或 `templates/academic.html` 后运行 `python3 render.py`。渲染器调用 MathRSI 仓内的 ARIS helper；可用 `--helper /path/to/render_html.py` 指定其位置。无需修改 MathRSI 本身。

`SOURCE_MANIFEST.json` 绑定本次读取的研究原件；`STATIC_CHECKS.json` 检查链接、源码哈希和离线依赖；`BROWSER_CHECKS.json` 记录 Chrome 中 320、390、768、1440 像素宽度的显示检查和证据折叠交互。

`Q8_683_FRAMEWORK.html.review.json` 是渲染审查；其审查范围不包含重新验证原数学证明。原定理的审查链接位于页面第六节。
