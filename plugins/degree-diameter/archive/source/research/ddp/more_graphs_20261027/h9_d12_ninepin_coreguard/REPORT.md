# Coreguard-first：120项已访问，无新增

current42397/245877边；原126项跳已接受pool43，当前mandatory度阻5项，冻结120项，包含此前44个limited。全部canonical访问，0新图、family58保持，未改delivery/Wiki/HTML/最终证明。

- 96项没有单个eligible anchor覆盖全部missingcore：restrictedrule不适用，**不判一般三anchor无解**。
- 19项枚举全部deduplicated coreguards后，exact≤2 extra-tail无解，仅关闭coreguard-first受限模式。
- 5项单项CPU窗口未完：pool20、67、161、536、37，保留UNKNOWN，不续时。

全部120项prepare完整成功，prepare UNKNOWN为0。实际有guard的24项；guardmask去重不损失≤3 unioncover。pool196仍有唯一guard42277覆盖3376coreholes，但其后两个extra-tail已完整判无解，故不能凭有guard或core洞总量判断成功。无guard的项和未完5项均不作通用三anchor排除。

前10项计时1.842CPU；运行计数22.611575CPU，含冻结、父进程（NumPy启动后）及全部120原生child，初始NumPy导入CPU未单列，未另跑校准。单项最大0.613458CPU，小于0.7；没有MIP、seed、额外预算、全源BFS、互审或Lean。

完整结果与每项guard/extra-tail计数在RESULT.json及items/。P“本批coreguard-first会产出至少一张完整新图”被本批0图结果反驳，停止这一有限restrictedrule；不声明五个UNKNOWN均不可行或整个九pin三anchor族无解。到此停止。

