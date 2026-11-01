# 310域中304份原固定严格证书的补验

旧 `VERIFY_DOMAIN.json`已核完整310必要库存，但旧pilot只独立重放最坏非严格项。本次补齐其余304份严格固定证书的实际原索引算术，旧源文件均未改。

`VERIFY_304.py`先用六个inclusive点对共度的独立Möbius生成法，重建选中原度10^4、outer exact mu3/mu12>=1、exactcross>=13的完整310库存，并与冻结 `RESULT.json`逐键绑定。随后对其中全部304份已存严格固定位置展开35个不同原边索引，独立计算1190个有序异边对、21个pivot位置，所有6384行的精确总界等于原存值且严格。

回执 `VERIFY_304.json`：`PASS_COMPLETE310_BINDING_AND304_STRICT_FIXED_REPLAYS`；最大严格界187/195；实际CPU1.995784秒，低于五秒预算。每份保存原35迹、位置、零quota及A/B/C行。

本次没有把剩六份原非严格项记作严格；它们在实际S2原度谱下由[共同column新局部门](../../c13_four_ten_seven_pool_20261020/SHARED_COLUMN_CLOSURE.md)的两轨及六源运输另行闭合。原310必要域与新的S2真实点池接口仍保持分离。
