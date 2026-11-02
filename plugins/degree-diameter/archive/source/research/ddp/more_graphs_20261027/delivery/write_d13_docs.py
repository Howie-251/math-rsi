"""Write compact current delivery docs; no graph computation."""
from pathlib import Path
import argparse,json
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--review-disposition',type=Path)
    args=parser.parse_args()
    data=json.loads((HERE/'families.json').read_text())
    f13=data['families']['13'];total=data['distinct_explicit_examples']
    n13,m13,count=f13['strongest_n'],f13['strongest_m'],f13['example_count']
    for current,old in [(HERE/'README.md',HERE/'README_history_63.md'),
                        (HERE.parent/'FINAL_RESULTS_PROOF.md',HERE.parent/'FINAL_RESULTS_PROOF_63.md')]:
        if not old.exists():old.write_text(current.read_text())
    review_zh=review_en=''
    if args.review_disposition:
        path=args.review_disposition.resolve()
        assert path.exists()
        rel=str(path.relative_to(ROOT))
        review_zh=f'本轮D13集中审阅的实际处置记录见[{path.name}](../../../../{rel})。'
        review_en=f'The focused D13 review disposition is [{path.name}](../../../{rel}).'
    pins=json.dumps(f13['steps'][0]['pins'],separators=(',',':'))
    readme=f"""# {total}个完整图：三个参数的确定性生成包

| 最大度 | 直径 | 完整例子的阶数 | 例子数 |
|---:|---:|---|---:|
| 11 | 5 | 37629至37631，每个整数 | 3 |
| 12 | 5 | 42343至42402，每个整数 | 60 |
| 13 | 5 | 51418至{n13}，每个整数 | {count} |

当前数学下界为N(11,5)≥37631、N(12,5)≥42402、N(13,5)≥{n13}；公开基线分别为37628、42342、51417，核对日期2026-10-27。这是{total}个不同阶数完整例子、3个参数格，不是{total}种独立方法或最优值声明。完整Lean图实例仍0，Goal保持ACTIVE。

## 生成任意例子

在解压目录或项目root运行，仅Python标准库，没有搜索或BFS：

~~~bash
python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 13 --order {n13} --output graph{n13}.edges
python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 12 --order 42402 --output graph42402.edges
python research/ddp/more_graphs_20261027/delivery/family_generator.py --degree 11 --order 37631 --output graph37631.edges
~~~

order可取表内任何整数。输出首行为n m，其后每行u v一条无向边。独立放置程序和families.json时，可用--source指定对应原作者raw adjacency。专家包包含三个完整原始源、字面序列及生成器。

[families.json](families.json)保存每步完整pins、mandatory_pins、anchors、实际旧degree、当前source_n/m及证据路径。D13续批actual_base字段已归一化为生成器source_n/m，旧11/12步骤没有改动。D13最强图为{n13}/{m13}；边数为324451加所用字面步骤实际邻集大小之和。

首D13实例51418只做了一次统一生成器dry-run边集比较：header及全部边完全一致，missing/extra/repeated均0；见[dry_run_d13_51418.json](dry_run_d13_51418.json)。该交付检查没有运行BFS，没有重验旧11/12实例。

## D13新邻域规则及完整性

原型51013的10邻点中，11352因已满degree13不进入拟新增邻集。保留其余9点，加入free guard50577，得到首个新点51417的完整邻集：

    {pins}

这没有删除旧图任何边。该规则为near-complete old-star加guard，不是Q-line或Baer/Rédei blocking set，也不假设当前D13 raw点映射已经证明。原51417图D≤5作为公开完整基图继承。root独立重建官方raw边集并读取新边表，确认旧边全部保留、max13、newroot偏心率5；见[首图独立检查](../d13_D5_h9_transfer/singlefault_star_probe/independent_newroot51418.json)。

后续{count-1}步每次检查实际current图的degree与完整R4覆盖，包括此前所有新点。旧旧路径保留，新旧距离≤5，逐步归纳得到全部前缀；不从最大图删点推断中间图合法，也不逐图重复source全源BFS。[accepted_family40.json](../d13_D5_h9_transfer/singlefault_star_probe/accepted_family40.json)及families.json保存完整字面序列。

三个族分别超过D4 Moore上界12222、17569、24506，所以直径恰5。完整桥接证明见[FINAL_RESULTS_PROOF.md](../FINAL_RESULTS_PROOF.md)。

## 原作者、验证与审阅范围

三个完整原作者基图属于Dharunish Yugeswardeenoo，H9 duality/partial-fold基础归Rishabh Rajiv；公开表及原作者链接归F.Comellas。source_urls、完整原图和署名在families.json。本项目新增的是明确邻域、增点及实际whole-current覆盖构造；已知基图与经典blocking理论不计新成果。

历史独立全源代表检查包含37631、42377；后续按适量验证要求复用基图，每步验新增degree与完整currentR4。新机制或新参数首次命中做一次必要独立新root检查。历史reviewed_example_count保留38；早先Rédei15有一次集中规则审阅，不表示全部{total}例逐图互审或重复全源验收。{review_zh}

完整Lean实例仍0。较早63例说明保存在README_history_63.md，旧图及原证据保留。ZIP在root当前HTML和集中处置齐备后更新，不声称外部发表、表格采用或最优性。
"""
    (HERE/'README.md').write_text(readme)
    proof=f"""# Three improved parameter cells, {total} complete graph examples

The complete lower bounds are **N(11,5)≥37631**, **N(12,5)≥42402**, and **N(13,5)≥{n13}**. There are3 degree11 prefixes37629..37631,60 degree12 prefixes42343..42402, and{count} degree13 prefixes51418..{n13}. These are{total} different-order examples in3 cells, without optimality, public-adoption or completed-Lean claims.

The fixed public source orders are37628,42342 and51417, checked on2026-10-27. Original complete source graphs are credited to Dharunish Yugeswardeenoo; H9 duality/partial-fold foundations to Rishabh Rajiv. Degree13 uses the actual official51417 adjacency, not an assumed reconstruction of its raw geometry.

## Common extension lemma

Let B be simple with maximum degree≤Δ and diameter≤5. Choose distinct existing pins S with |S|≤Δ and degree_B(s)<Δ for all s∈S. Retain every old edge and add z adjacent exactly to S. If closedR4_B(S) covers all vertices of B, the new graph has maximum degree≤Δ and diameter≤5.

Old-old paths remain. For every old v, some s∈S has distance_B(s,v)≤4; the edge z-s followed by that old path has length≤5. Distinct old pins introduce no loops or repeated edges. Apply the lemma in the actual successive graph, including all prior additions.

Every saved step satisfies this complete-currentR4/degree obligation. Induction proves each literal prefix; no prefix validity is inferred by deleting vertices from the largest graph. The corresponding D4 Moore bounds are12222,17569 and24506. All listed orders exceed them, so their diameters are exactly5.

## First degree13 graph

The published51417 source has324451 edges, maximum degree13 and diameter5. At prototype51013, omit saturated neighbor11352 from the proposed new star, while retaining the old edge itself. Keep the other9 neighbors and add guard50577. The new vertex51417 has neighbor set

    {pins}

The ten original degrees, in this pin order, are11,12,11,12,12,12,12,12,11,11. The expanded graph has51418 vertices,324461 edges and maximum degree13.

Root independently rebuilt the original official raw edge set and read the complete new edge list. It checked simplicity, exact retention of all324451 old edges, ten new edges and actual degrees, then one complete new-root BFS. The eccentricity was5; distance counts were1,10,99,1032,9840,40436, totaling51418. See [independent_newroot51418.json](d13_D5_h9_transfer/singlefault_star_probe/independent_newroot51418.json).

Old-old diameter≤5 is inherited from the published valid source; new-old diameter≤5 is independently checked. This is the complete graph argument without rerunning old-source allpairs, proving a new raw-point map, or invoking a line/blocking-set theorem.

## Remaining degree13 prefixes

The finite continuation accepts{count-1} further steps, ending at{n13} vertices and{m13} edges. Each checks actual current degree and completeR4, including all earlier new points. Literal source_n/m uses actual_base_n/m, not frozen original-source metadata.

[accepted_family40.json](d13_D5_h9_transfer/singlefault_star_probe/accepted_family40.json) and [families.json](delivery/families.json) contain the{count} steps. Added cardinalities sum to{m13-324451}, giving324451+{m13-324451}={m13} final edges. Later steps are accepted by production complete-currentR4 induction, not described as separate independent new-root or allsource verifications.

The degree13 neighbor rule is near-complete old-star plus available guards. It differs from degree12 Q-line, Baer13 and Rédei15 pin selection; all share the retained-edge complete-R4 proof principle.

## Existing families and delivery scope

Degree11/12 literal steps remain unchanged. Degree12 orders42399..42402 use saved Rédei15 blocking neighborhoods plus actual whole-currentR4 completion; the inherited polar lemma gives a core guarantee, while actual coverage discharges extra vertices. Earlier full-allsource checkpoints include37631 and42377. Later steps follow the user's once-only degree/coverage policy.

[family_generator.py](delivery/family_generator.py) reproduces each listed example using only the three original sources and literal steps. The only new option is degree13; its first51418 dry-run matched the saved edges exactly without BFS. See [dry_run_d13_51418.json](delivery/dry_run_d13_51418.json).

Historicalreviewed_example_count remains38. Focused new-rule review does not claim all{total} graphs were individually reviewed or every old root rerun. {review_en} Complete Lean graph instances remain0; generic extension interfaces and concrete graph binding remain separate. Goal stays active.

Historical63- and59-example proofs are retained as [FINAL_RESULTS_PROOF_63.md](FINAL_RESULTS_PROOF_63.md) and [FINAL_RESULTS_PROOF_59.md](FINAL_RESULTS_PROOF_59.md).
"""
    (HERE.parent/'FINAL_RESULTS_PROOF.md').write_text(proof)
    print(json.dumps({'documents_written':True,'examples':total,'cells':3,'strongest13':n13,'graphs_computed':0,'BFS':0,'archive_rebuilt':False}))

if __name__=='__main__':
    main()
