# 六／八／九元展示更新

本次展示值为 k=5…12：35、67、131、267、543、1112、2275、4664；相对原共同参考包络增益为3、3、3、4、5、27、30、31。

更新源：`../plot_small_updates.json`、`proofs/propertyb-general/RESULTS_FIGURE.md`、`figures/propertyb_bounds/plot_bounds.py`、`context/rendering/render_propertyb_general.py`。既有生成器已同步根 `PROPERTY_B_GENERAL_BOUND.md` 与 `PROPERTY_B_GENERAL_BOUND.html`，并重建 delta/small/overview/gain 四组 SVG、PNG、PDF及整组矢量PDF。

数值检查覆盖首屏摘要、主图红色点与增益、小参数点标签、正文表格和图片alt。四份数学规范与此前保存的源快照逐字相同；共同参考包络、蓝色统一Lean曲线及紫色C.2数值未改。

实际离线浏览器检查使用1440×1000桌面与390×844手机视口，所有HTTP/HTTPS请求均阻断：1049个公式全部为内嵌SVG，三图均内嵌并加载成功，无页面横向溢出、脚本错误、缺失本地链接或数学错误。手机图像保留既有内部横向滑动。14张截图已保存于本目录；生成执行者已目检桌面／手机顶部、差值主图及小参数图。

检查结果：`NUMERICAL_DISPLAY_CHECK.json`、`browser-check.json`、`canonical-math-check.json`、`math-build.json`。此为数值展示和实际渲染检查，不是fresh展示审阅或数学终审；最新跨模型review文案由主代理收尾。

复现：

```sh
.tools/math-python/bin/python figures/propertyb_bounds/plot_bounds.py
python3 context/rendering/render_propertyb_general.py --trace-dir context/propertyb-small-updates-20261029/render-6-8-9
```

绘图环境使用现有math-python；HTML生成使用已安装Playwright的系统python3。没有增加依赖、hash或额外验算平台。
