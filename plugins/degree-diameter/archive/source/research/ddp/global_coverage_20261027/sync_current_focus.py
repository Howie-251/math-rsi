"""Incremental execution-entry revision; no historical import or experiments."""
from pathlib import Path
from datetime import datetime, timezone
import importlib.util

ROOT = Path(__file__).resolve().parents[3]
NOW = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
spec = importlib.util.spec_from_file_location('capture', ROOT/'aris_repo/tools/capture_filter.py')
capture = importlib.util.module_from_spec(spec)
spec.loader.exec_module(capture)
focus = '''当前唯一主线改为H9整体覆盖对照：已有41699与42342图共享41356点部分折叠核心K。固定K的普通克隆及任何包含完整核心星的新增点总数至多343，整类上限41699；当前986个新增点中实测176个含完整星、810个不含。root已从K对全部986点逐步R4覆盖检验通过，得到已有42342图的完整D≤5归纳证书；不是新纪录。静态独立整批假设被推翻，实际helper会缩短旧图内部距离。P4支持一个helper的具体捷径；P5仅部分支持，不能称两点均能独立安全加入；P6固定两个helpers的全163点通用层被推翻，不加第三helper、不修剩余遗漏。下一步只研究810 non-star的几何line-image/锚点生成规则及所有新类间覆盖，代理围绕同一问题互补。停止完整星数量搜索、旧S/c/MIP复跑及1152局部边修补，不横向大筛。新图0、新下界0；已有构造理解与最终新图分账。证据research/ddp/global_coverage_20261027/REPORT.md。'''
assert not capture.screen(focus)

def edit(rel, transform):
    path = ROOT/rel
    before = path.read_text()
    after = transform(before)
    if before != after:
        path.write_text(after)

old72 = '当前主线固定为同一72点控制器：对照已成功的F3^4/5832路由与已关闭的F2^4/global线性/offset0模型，研究多条短路线产生的子空间怎样互补，以及在固定线性部分上非零offset能否修复覆盖。先提出可被推翻的覆盖预测，使用推导、既有数据、反例或针对性小实验检验，再说明结果改变了哪项生成或选题规则。不得把“未被排除”作为正向成功依据。旧108通用chart、2419200规范输入与1024个offset0图不重跑。'
edit('AGENTS.md', lambda s:s.replace(old72, focus+'\n\n已完成并收束的上一轮：同72控制图F3/F2路线互补对照，原预测、两张受控图和反例保留；已闭108通用chart、2419200输入及1024个offset0图不重跑。'))

goal = ROOT/'context/DD_PORTFOLIO_START_20261026/RESEARCH_GOAL.md'
s = goal.read_text()
marker = '### 2026-10-27 较早广度指导（历史；本阶段暂缓）'
revision = '### 2026-10-27 H9执行修订：整类容量与有序全覆盖\n\n'+focus+'\n\n此前第2节的同72控制器选题为已完成、现已收束的历史对照，不是并行任务。有效覆盖认识保留于wave12证据，后续动作以本段为准。\n\n'
if '### 2026-10-27 H9执行修订' not in s:
    s = s.replace(marker, revision+marker)
s = s.replace('当前选择同一72点控制器作对照：','上一轮已完成的对照（现已收束）：选择同一72点控制器，')
s = s.replace('当前72控制器问题应区分唯一四路slot的必要满秩与多路低秩子空间并的覆盖：前者通过不能替代后者。固定线性部分时offset只改变相应仿射位置，不改变每条路线的方向秩；具体能否使所有起点与目标同时覆盖需真实检验。', '当前H9问题应区分完整核心星复制、独立整批充分条件与按实际更早图的有序R4覆盖；P3已对已有986步全通过，P1与P6静态层猜测被推翻。每次改变生成规则必须处理所有新类间覆盖与度负载，不按零散遗漏继续加helper。上一轮72控制器中秩与子空间并的区别保留为历史经验。')
s = s.replace('当前先完成同72控制器的覆盖对照，不自动开启offset搜索、旧输入重枚举或新的横向支线。','当前执行H9几何line-image/锚点和全类路由的针对性研究；不继续已闭核心星数量优化、旧S/c/MIP、两helper猜测或1152局部修补。每批仍有明确预算和返回对象，不按坏对减少无限加算。')
s = s.replace('当前置顶应围绕同72控制器上F3^4成功与F2^4零offset失败的子空间互补/offset问题；','当前置顶应围绕H9的整类343上界、810 non-star生成缺项、有序全覆盖与静态互助预测；')
goal.write_text(s)

edit('RESEARCH_BRIEF.md',lambda s:s.replace('## What I\'m Looking For\n','## What I\'m Looking For\n\n'+focus+'\n\n### 上一轮72控制图对照（已完成且已收束，不再派发）\n').replace('当前只研究同一72控制图：','上一轮研究同一72控制图：').replace('下一生成规则同时保护468紧路与72同fiber闭路并集，再研究多路槽；','所得保护468紧路与72self闭路并集的认识保留，但不继续局部修补；'))

next_path='context/DD_PORTFOLIO_START_20261026/NEXT_SESSION.md'
edit(next_path,lambda s:s.replace('Updated 2026-10-27 09:20:08 UTC. Goal ACTIVE, zero new lower bounds.',f'Updated {NOW}. Goal ACTIVE, zero new lower bounds.',1).replace('\n## 最新纠偏：','\n## 当前恢复入口：H9整体覆盖\n\n'+focus+'\n\n先读该REPORT与唯一Wiki exp:ddp-h9-global-coverage-20261027；ledger160条记录，新增一项研究归并变体，不是160种独立方法。不要重新导入Wiki或启动旧历史pending。P6已终态，几何规则代理仅围绕同一问题工作；不把派发当运行。\n\n## 最新纠偏：',1).replace('## 当前steering — 2026-10-27人工策略修订','## 较早steering与已收束72对照（历史）').replace('## Latest checkpoint: focused route-complementarity prediction cycle','## Historical checkpoint: focused route-complementarity prediction cycle'))

edit('research-wiki/gap_map.md',lambda s:s.replace('# Gap Map\n','# Gap Map\n\n'+focus+'\n\n检索[当前H9实验节点](experiments/ddp-h9-global-coverage-20261027.md)与[统一方法账本](DDP_METHOD_LEDGER.md#家族目录)，不全量重载。\n\n## 已收束的72控制器对照（历史，不派发）\n',1).replace('- 当前同一72控制图：','- 上一轮同一72控制图：'))

comments = ROOT/'research-wiki/DD82_PROGRESS_AND_COMMENTS_20261018.md'
text = '\n\n## '+NOW+' — 纠偏后的实际执行与整体覆盖研究\n\n用户“不深陷几百个点对”的指导继续有效。以下是研究执行结果，不是新的用户原话：\n\n'+focus+'\n\nP6为冻结两helpers的一次全范围对照：全部pinset pair条件成立，但6个R4条件仍失败，按事先约定停止该猜测，未开启第三helper或pin修复。当前几何规则研究有明确问题和返回对象；尚未恢复可泛化的新规则。旧专家07:58快照、全部历史证据及Gemini回执保持原截点。\n'
assert not capture.screen(text)
if '纠偏后的实际执行与整体覆盖研究' not in comments.read_text():
    with comments.open('a') as f:
        f.write(text)
print('Original execution entries and existing human-comments record revised:', NOW)
