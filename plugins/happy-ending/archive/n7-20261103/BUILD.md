# 重生成报告正文

在此目录运行 `python draw_figures.py`，再运行 `python render_report.py`。需要 Python 3、Matplotlib 和已安装的 Times New Roman（普通、斜体、粗体及粗斜体）。数学公式转为 SVG 轮廓，报告打开时不加载网络依赖。

source/report.md 是正文源，source/report.json 是标题配置，report-template.html 是版式，figures 是图源生成结果，rendering/aris_render_html.py 是随包提供的 Markdown 渲染辅助模块。重生成可能改变生成时间元数据和文件散列。

proofs/source-tree 是原始证明档案，不参与正文生成。collect_sources.py 与 package_delivery.py 保存本次仓库资料清点与封装逻辑，其读取路径以原仓库为环境。包内科研核验源码如需运行，应按各自说明在 Linux 执行。
