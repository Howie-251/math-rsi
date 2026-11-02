from pathlib import Path
import csv
import html
import json

ROOT = Path(__file__).resolve().parents[3]
BASE = Path(__file__).resolve().parent
AUDIT = BASE / 'public_baseline_audit'
MAIN = 'https://web.mat.upc.edu/francesc.comellas/delta-d/table_degree_diameter.html'
EJC = 'https://web.mat.upc.edu/francesc.comellas/old-files/delta-d/papers/81981341.pdf'


def moore(degree, diameter):
    return 1 + degree * sum((degree - 1) ** j for j in range(diameter))


def correct_url(url):
    return url.replace('/delta-d/old-files/delta-d/', '/old-files/delta-d/')


def esc(value):
    return html.escape(str(value), quote=True)


def local_link(relative, label):
    target = ROOT / relative
    if not target.exists():
        return esc(label) + '（未返回）'
    return f'<a href="../{esc(relative)}">{esc(label)}</a>'


def load_entries():
    d35 = json.loads((AUDIT / 'STALE_MAIN_D3_D5_20261101.json').read_text())
    d610 = json.loads((AUDIT / 'STALE_MAIN_D6_D10_20261101.json').read_text())
    rows = []
    for r in d35['confirmed_at_least10year_entries']:
        rows.append(dict(Delta=r['Delta'], D=r['D'], current_n=r['current_n'],
                         record_date=r['last_record_date'], record_year=r['last_record_year_upper_bound'],
                         date_kind=r['record_date_precision'], age_years_approx=r['calendar_year_age'],
                         author=r['author'], sources=[correct_url(u) for u in r['source_URLs']],
                         source_locator=r['source_locator'], local_scope=r['local_attempt_scope'],
                         age_group='至少约10年'))
    for group, label in [('confirmed_primary_candidates', '至少约10年'),
                         ('confirmed_secondary_candidates', '5–9年备选')]:
        for r in d610[group]:
            rows.append(dict(Delta=r['degree'], D=r['D'], current_n=r['currentN'],
                             record_date=r['date'], record_year=int(r['date'][:4]),
                             date_kind=r['date_kind'], age_years_approx=r['age_completed_years_lower_bound'],
                             author=r['author'], sources=[r['sourceURL'], r['mainURL']],
                             source_locator=r['note'], local_scope={'status': 'NOT_A_CLAIM_OF_UNTRIED'},
                             age_group=label))
    extra_scopes = {
        (4, 3): ('N1/N2/N3三个固定41源的双cut＋4星规则共9225配置完整失败，新根通过3/6/0但无完整图。再从N2六基例定向第三cut/repair，共3048参数，426修好旧pair却全部丢新根覆盖，联合预测被推翻。暂停此局部移端口线；不排其他源或一般三cut。',
                 'research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/ROOT_DISPOSITION.json'),
        (5, 3): ('Exoo72指定删边单hub及干净拆点已排。GQ80任意双匹配仍UNKNOWN；新共同symplectic C5族由完整互补join排除。再固定Q1361、允许P任意且打破C5，一次合法求解返回raw UNSAT，仅此Q、未留UNSAT证书，不外推整个GQ80。',
                 'research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D3/gq80_paired_matching_intuition/ROOT_DISPOSITION.json'),
        (8, 3): ('CM253局部两范围已停止：任意≤5条旧删边＋纯星，以及指定五不交cut＋一原非边repair＋八星（实际耦合24<27）均NO。随后改变为全局256点Cayley：固定C8-action3/Z32循环群、正phase1/2/3/4的全normal域，57344连通规范代表完整检查，含3072个7度及54272个8度案，无一八槽同时满。各phase均能单独满32，但phase0的320组与phase2的1344组无共满参数。停止此固定族，不排其他群/action/phase或一般(8,3)；旧相邻拆点等历史保留。',
                 'research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/global_c8_z32_action3_256/NOTE.md'),
        (9, 3): ('实际585源保边扩张全NO继承。固定p0=0、四条顶点不交corecuts＋八core/p0星＋其余64A任意匹配的整个规则已闭：k=0由1568eligible/3697DFS数值NO；k≥2由derived affine plane给U≤63-k、自由mate≤k、新根A≤63纸面NO；k=1的全部64owner×1568far必要域再经3200DFS完整，0端口packing，P1推翻，P2/corestage未进入。累计2.736CPU/20，无586图。其它p0、非matching cuts、多helper、额外旧旧补边及一般(9,3)未排；停止此固定原型，不换p1或续seed。',
                 'research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/PORT16_NOTE.md'),
        (10, 3): ('原650源的≤5删边、全端点连单hub规则已排。新八FP端点转移：8F/8P各互异，新根接8F+2P，余6P配对；借F-neighborhood twins把新根F覆盖写成原source-R2。一次1170变量/1302行/90480非零项HiGHS feasibility，20秒到时无incumbent，actual UNKNOWN而非INFEASIBLE或整族NO。累计22.085CPU/45；未冻结原型，15配对及新旧根BFS均0。已有PP边允许underdegree9的接口未实际进入。停止本窗口，不第二求解/seed；整族仍开放。',
                  'research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_NOTE.md'),
        (11, 3): ('已完整排除实际715源的全部保旧边扩张：任意新增旧旧、旧新、新新边均不行。core与195eligible预算迫minH3及邻度和12/13；再排任何H度4–7，邻度和只能9或≥14，矛盾。需删改旧边或换源，非一般(11,3)无解。',
                  'research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/HIGHER_DEGREE_CLOSURE_NOTE.md'),
        (8, 4): ('1100源单拆点及旧H342全233928匹配域NO继承。放宽为684源的K19/36轨道实际端点模型后，60/20/5秒三个SAT窗口均UNKNOWN，累计96.357/100CPU已停；不能记NO。另一个Sampels672源的全部672个rightmatching完整NO，六个相对phase各自最多106/112。只关闭这些精确范围，不排任意matching或一般(8,4)。',
                 'research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/K19_exact_matching_interface/ROOT_DISPOSITION.json'),
        (3, 5): ('直接目标至少72，奇数71受度数奇偶阻断。70→72两条指定三cut规则完整检查9030490配置均失败；相邻helper修好新点互距，但168配置仍破坏旧点对路线。',
                  'research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut/adjacent_helpers_repair/NOTE.md'),
        (3, 6): ('132→134指定三cut/repair的10000样本未命中，整族UNKNOWN已停。另Petersen10×14覆盖的64奇偶模式仅21/62过容量门，实际奇轮面冲突排全部order14群覆盖；Petersen标量仿射F16/160亦由17路碰撞与秩排除。其他控制器、一般置换覆盖及一般(3,6)未排。',
                 'research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/petersen_c14_140_route_gate/FINAL_NOTE.md'),
        (4, 5): ('旧保边/九覆盖排除继承；最新合作helper范围已由1–13推进到1–14完整NO。另Petersen19骨架5005细分中235过Hdiam4、分6轨道，完整端口模型六例均rawUNSAT未proofchecked，未产383图。原10000随机matching/cut样本UNKNOWN保历史；新联合端口分析先以24个hardowners对1个nearport关闭固定P，再完整检查196371个不交corecut对。每对hardowners至少21、nearports至多2，全部违反Hall注入条件，故自然364源“两corecuts＋28ports任意perfectmatching＋四端点新星”的整个规则NO。其它删改、源或一般365图未排，不自动加第三cut。',
                 'research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/port_matching_core2_star365/all_two_corecut_Hall_gate/FINAL_PROOF.md'),
        (4, 8): ('旧3243源全4regular，无保边追加余度；普通非平凡cover的D≤9亦已排。新69相位/r6/F139四共享平移族完整19462代表均失败，紧槽最高117/139；不排改变相位或逐相位参数。',
                  'research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/NOTE.md'),
        (3, 9): ('Exoo600→602三cut/四cut相邻helper两样本各10000配置无hit，都未通过双helper覆盖，未进入old-old检查；两整族仍UNKNOWN，停止原样本不续seed。',
                  'research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/NOTE.md'),
        (6, 9): ('旧单细分及F6959固定相位normal族已排。新固定331387源的三删边六星也完整NO：32/21/32项旧路线义务，另两边最多命中22/14/24。支配论证进一步排任意至多三条旧边删除＋单新星（可共享端点、非正则），不含新增旧旧修补；更多删边、其他源及一般(6,9)未排。',
                  'research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/threecut_star331388_gate/FINAL_NOTE.md'),
        (3, 10): ('旧单细分及5614双cut范围直接继承。新固定4536基例、保x1178的三cut移端口全11178配置失败；P3准确预测移0/1会撤走该点覆盖，6例实测距11。改成四helper星保全部六端点后，先1865固定域、再全1743779匹配三cut域，全部中心R10失败；同一中心反例不依赖六端点怎样配三对。只排该源三matchingcuts/K1,3，不排P4、sharedcuts、其它source或一般(3,10)。',
                   'research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D10/source1250_interface/NOTE.md'),
    }
    followup = json.loads((BASE / 'STALE_FOLLOWUP_ROUND_20261101.json').read_text())
    small360 = followup.get('source360_subdivision361', {})
    extra_scopes[(3, 8)] = (small360.get('summary_zh', 'Chen2018实际360源已取得；361点的degree2根容量511不阻断。单边细分新根须由旧两端点R7并覆盖，之后仍须检验旧点对；唯一固定源全部540边有界批次。'),
                           'research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/NOTE.md')
    for r in rows:
        key = (r['Delta'], r['D'])
        bound = moore(*key)
        r.update(moore_bound=bound, moore_gap=bound-r['current_n'],
                 gap_percent=round(100*(bound-r['current_n'])/bound, 2),
                 target_order_threshold=r['current_n']+1,
                 original_scope=4 <= r['Delta'] <= 12 and r['D'] in (3, 4, 5))
        if key in [(3, 5), (3, 6)]:
            r['target_order_threshold'] += 1
        r['method_note'] = r['local_scope'].get('summary', '已列年代和公开源；尚未据此派发构造，不声明从未试过。')
        r['local_evidence'] = r['local_scope'].get('evidence_paths', [])
        if key in extra_scopes:
            r['method_note'], path = extra_scopes[key]
            if path:
                r['local_evidence'] = [path] + r['local_evidence']
        if key == (8, 3):
            r['local_evidence'].append('research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/source253_fourcut_star254_gate/FINAL_PROOF.md')
            r['method_note'] += ' 新binary实际pair对照证实三rank2路线可覆盖全部8点；定向修矩阵同时损其它词，goodword仍24。typedC30插点378450参数/284310simple由普通路线容量全NO（任意8fiber/≤2choices）；三型C11/C33的100规范controller亦全部有投影缺点，不能靠换矩阵修复。这些不排一般8D3。'
            r['local_evidence'].append('research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/controller32_F2_multiroute_readgate/NOTE.md')
        if key == (9, 3):
            r['local_evidence'].append('research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/OWNER_P0_NEXT_INTERFACE.md')
            r['local_evidence'].append('research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/K1_NOTE.md')
        if key == (10, 3):
            r['local_evidence'].append('research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/ROOT_DISPOSITION.json')
            r['local_evidence'].append('research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/FP_MODEL.json')
            r['method_note'] += ' 后续8385个starP对全通过分组容量上界，min surplus46，未排任何对；首上界argmax的实际八包仍漏29，不能作可行见证。再按K8,2作整数精确投影为650变量/652行/50440非零项，唯一18秒窗口仍UNKNOWN、无incumbent。最终42.416CPU/45停止，不第三solve/seed；不是INFEASIBLE，donor/PP配对及651图均未进入。'
            r['local_evidence'].append('research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/NEXT_STRUCTURAL_READ_GATE.md')
            r['local_evidence'].append('research/ddp/two_successful_methods_20261101/stale_record_transfer_d10D3/fp_endpoint_transfer651/STRUCTURAL_AND_PROJECTED_NOTE.md')
        if key == (8, 4):
            r['local_evidence'].append('research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/NOTE.md')
        if key == (3, 10):
            r['local_evidence'].insert(0, 'research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D10/source1250_interface/thirdcut_route_repair1252/NOTE.md')
            r['local_evidence'].append('research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D10/source1250_interface/threecut_fourhelper_star1254/global_three_matching_gate/NOTE.md')
            r['local_evidence'].append('research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D10/source1250_interface/threecut_fourhelper_star1254/GLOBAL_CENTRE_PAIRING_SCOPE_ADDENDUM.md')
        if r['D'] == 3 and r['Delta'] in (8, 9, 10, 11):
            r['method_note'] += ' 旧4q/30q³系列在这些度数最多取q=2，名义240点低于当前表；直接换field不能提高本格。'
        if r['Delta'] in (3, 4, 5):
            r['method_note'] += ' 原4q度数模板的最小合法field为q≥2，不能直接缩到本度数；需拆点、改旧边或另一种连接规则。'
        r['active'] = key in [(4, 3), (5, 3), (8, 3), (9, 3), (10, 3), (8, 4), (3, 5), (4, 5), (11, 3), (4, 8), (3, 9), (6, 9), (3, 6), (3, 8), (3, 10)]
    return sorted(rows, key=lambda r: (r['D'], r['Delta']))


def build():
    rows = load_entries()
    state = json.loads((BASE / 'STAGE_STATE.json').read_text())
    current_graphs = state['accepted_total_named_legal_instances']
    current_pairs = state['accepted_total_parameter_pairs']
    current_Lean = state['complete_concrete_formula_Lean_instances']
    tight = json.loads((AUDIT / 'STALE_MAIN_D2_20261101.json').read_text())['rows']
    for r in tight:
        r.pop('hashes_computed', None)
        m = moore(r['Delta'], 2)
        r.update(moore_bound=m, moore_gap=m-r['current_n'],
                 gap_percent=round(100*(m-r['current_n'])/m, 2))
    status_path = BASE / 'stale_record_transfer_d8D4' / 'ROOT_TRANSFER_STATUS.json'
    transfer = json.loads(status_path.read_text()) if status_path.exists() else {
        'status': 'TWO_BOUNDED_GATES_DISPATCHED',
        'summary_zh': '两个新问题门已派发，各最多10 CPU秒：1100源拆点的R4首步分区；C30/F2规则五重覆盖的路线容量。尚无新图。',
        'new_graphs': 0,
    }
    later_path = BASE / 'STALE_FOLLOWUP_ROUND_20261101.json'
    later = json.loads(later_path.read_text()) if later_path.exists() else {}
    payload = {'date_UTC': state['updated_UTC'].split()[0], 'scope': 'Comellas当前主表的开放格；14格至少约10年，另1格8年备选。',
               'formula': 'M(Delta,D)=1+Delta*sum((Delta-1)^j,j=0..D-1)',
               'date_policy': '当前order在历史来源中已达到的日期；known-by不是首次发现精确日期；同order新复现不重置。',
               'gap_policy': '展示经典Moore上界的绝对和相对差；不当作可实现点数承诺或局部搜索成功概率。',
               'counts': {'main_list': len(rows), 'at_least10_years': sum(r['age_group']=='至少约10年' for r in rows),
                          'secondary5to9': sum(r['age_group']=='5–9年备选' for r in rows),
                          'within_original_parameter_scope': sum(r['original_scope'] for r in rows),
                          'tested_this_round': sum(r['active'] for r in rows),
                          'inherited_scope_only': len(rows)-sum(r['active'] for r in rows),
                          'new_graphs_in_shortlist': 0},
               'rows': rows, 'tight_D2_not_main_priority': tight, 'actual_transfer': transfer,
               'followup_round': later}
    (AUDIT / 'STALE_RECORD_CANDIDATES_AND_MOORE_20261101.json').write_text(json.dumps(payload, ensure_ascii=False, indent=2)+'\n')
    fields = ['Delta', 'D', 'current_n', 'record_date', 'age_years_approx', 'age_group',
              'moore_bound', 'moore_gap', 'gap_percent', 'target_order_threshold', 'method_note']
    with (ROOT / 'research/stale_record_candidates.csv').open('w', encoding='utf-8-sig', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)
    table_rows = []
    for r in rows:
        source_links = ' · '.join(f'<a href="{esc(u)}">出处{i+1}</a>' for i, u in enumerate(dict.fromkeys(r['sources'])))
        evidence = ' · '.join(local_link(p, '已试范围') for p in dict.fromkeys(r['local_evidence']))
        tag = ' <strong>本轮检验</strong>' if r['active'] else ''
        table_rows.append(f'<tr><td>({r["Delta"]},{r["D"]}){tag}</td><td>{r["current_n"]:,}</td>'
                          f'<td>{esc(r["record_date"])}<br>约{r["age_years_approx"]}年</td>'
                          f'<td>{r["moore_bound"]:,}</td><td>{r["moore_gap"]:,}<br>{r["gap_percent"]:.1f}%</td>'
                          f'<td>{r["target_order_threshold"]:,}</td><td>{esc(r["method_note"])}<br>{evidence}<br>{source_links}</td></tr>')
    tight_text = '；'.join(f'({r["Delta"]},2)：{r["current_n"]}，Moore差{r["moore_gap"]}（{r["gap_percent"]:.1f}%）' for r in tight)
    gates = [
        ('loz1100_split_gate', '保留大部分旧图，拆出一个新点',
         '把旧root的8个邻居分给两个相连的新旧root。预测：每个原distance4目标的最短路首步集合，都必须同时碰到A/B两侧；先查这道必要门，过门才考虑完整1101图。'),
        ('c30_f2_fivecover_gate', 'D3仿射规则迁移为D4覆盖',
         '检查C30×F2³字面规则是否适用；若得到240点/8度base，五重覆盖为1200点，超过1100。预测：每对base点至少须有5条长度≤4的非回退walk；容量不足立即停，容量够也仍需实现相容电压。'),
    ]
    gate_html = []
    for name, title, prediction in gates:
        rel = f'research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/{name}'
        links = ' · '.join(local_link(f'{rel}/{fn}', label) for fn, label in [('PRED.md','事前预测'),('RESULT.json','实际结果'),('NOTE.md','解释')])
        gate_html.append(f'<h3>{esc(title)}</h3><p>{esc(prediction)}</p><p>{links}</p>')
    next_rel = 'research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/alternative41_ninecover_gate'
    next_links = ' · '.join(local_link(f'{next_rel}/{fn}', label) for fn, label in [('PRED.md','事前预测'),('RESULT.json','实际结果'),('NOTE.md','解释')])
    gate_html.append('<h3>改变来源：(4,5)的369点九重覆盖入口</h3><p>旧Allwright1(a)源已排，不重跑。新N1/N2/N3三个41点D3源已全部检查：最紧同fiber返回槽分别只有1/3/1条长度≤5的非回退walk（含零步），少于9。任何普通九覆盖的每条base walk只有一个提升终点，因此三源的任意S9置换电压均不可能得到D≤5；无需生成369点图。不是只说某次C9赋值失败。已停止这些源，下一代须改变基图短返回路线或普通覆盖规则。</p><p>'+next_links+'</p>')
    cubic_rel = 'research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D5/two_helper_threecut'
    cubic_links = ' · '.join(local_link(f'{cubic_rel}/{fn}', label) for fn, label in [('PRED.md','事前预测'),('RESULT.json','实际结果'),('NOTE.md','解释')])
    gate_html.append('<h3>(3,5)：70→72的两新点受控改边</h3><p>继承已保存70点D5源，删三条互不相交旧边；六个端点分为两个三元组，各接一个新点，两新点不相邻。度数保持3，最终72点108边。原先“每组三pin的旧R4球必须覆盖旧图”的过滤条件过强，已撤销：A–旧pin–旧pin–B–旧pin–target恰可五步，第二新点能补第一新点的old-only缺口。旧R4只作路线诊断，实际候选以最终72图的helper根和old-old路线判定。本批最多20 CPU秒，找到完整合法图即保存返回，未成不计新图。</p><p>'+cubic_links+'</p>')
    adj_rel = cubic_rel+'/adjacent_helpers_repair'
    adj_links = ' · '.join(local_link(f'{adj_rel}/{fn}', label) for fn, label in [('PRED.md','修改规则的预测'),('RESULT.json','实际结果'),('NOTE.md','解释')])
    gate_html.append('<p><strong>首条规则已全穷尽：166390个三matching、1663900个3+3分割，0达标图。</strong>1663872个配置连helper70到所有旧点的五步覆盖都未达成；剩下28个虽到全部旧点，却到helper71距离6。没有配置进入old-old检验。这个反馈直接改变规则：让两helper相邻，各只接2个旧pin；余2个旧端点加一条修复边。</p><p><strong>第二规则也已全穷尽：7366590个合法配置，0达标图。</strong>168个配置让两helper各到全部旧点均≤5、互距1，但全部破坏了某些旧点对五步路线。首反例旧pair(0,17)，cut为(0,1)/(2,56)/(3,4)，repair(0,4)，新点pins为[1,3]与[2,56]。预测被部分支持：直接helper边确实解决新点互距，却不能同时保住旧路线。两个固定规则已停止；约4.661实测CPU加另预留准备成本仍在原20CPU内，没有清零续时。不能据此排除一般72点图或其他改边规则。</p><p>'+adj_links+'</p>')
    proof715 = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/ARBITRARY_HELPER_NOTE.md', '完整715计数证明')
    phase69 = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D8/loz3243_interface/normalized_parameter_gate/NOTE.md', '归一化与完整19462代表结果')
    sample602 = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_helper_repair602/four_cut_spread_pins/NOTE.md', '两602样本及失败阶段')
    signed2 = local_link('research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/signed_F2_transfer3072/NOTE.md', 'signed-F2反例')
    sub331k = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/single_subdivision_R8_gate/NOTE.md', '三类单细分完整结果')
    tau5155 = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/shared_tau5155_pilot/NOTE.md', '6959个新电压代表完整结果')
    tau_domain = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/shared_tau5155_pilot/PAPER_DOMAIN.md', '参数归一化与倒数action传输')
    tau_batch = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/shared_tau_remaining_actions_batch/RESULT.json', '其余20域完整终态')
    star365 = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/port_matching_core2_star365/NOTE.md', '365改边规则与样本反例')
    repair134 = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/source132_interface/adjacent_helpers_repair134/NOTE.md', '134规则与两阶段反例')
    subdivision361 = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D8/source360_interface/single_subdivision361/NOTE.md', '361全部单细分的实际结果')
    cross715 = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d11D3/cooperative715_interface/cross_old_class_tradeoff/NOTE.md', '跨旧类补边的新路线权衡')
    inherit1250 = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D10/source1250_interface/NOTE.md', '1250旧scope继承')
    star42 = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N1_all_pairs/NOTE.md', 'N1全部3075改边配置与路线诊断')
    star42_comparison = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_N3_all_pairs/ROOT_DISPOSITION.json', 'N2/N3全部6150配置及实际路线对照')
    star42_repair = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d4D3/two_corecut_star42/N2_targeted_threecut_repair42/ROOT_DISPOSITION.json', '依据反例改变规则后的3048参数与预测检验')
    petersen_route = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/petersen_c14_140_route_gate/FINAL_NOTE.md', 'Petersen路线问题、预测与实际结论')
    petersen_proof = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/petersen_c14_140_route_gate/C14_AND_ORDER14_NO_PROOF.md', 'order14群覆盖与实际H20证明')
    affine16_proof = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D6/petersen_c14_140_route_gate/PAPER_AFFINE16_NO_PROOF.md', 'F16仿射路线碰撞与17个秩证据')
    two684_note = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/FINAL_NOTE.md', '两份684源的匹配接口、两次预测与完整有限域结果')
    two684_domain = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/PAPER_EQUIVARIANT_MATCHING_DOMAIN.md', '匹配参数域完备性与一步跨层覆盖公式')
    gq80_proof = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D3/gq80_paired_matching_intuition/FINAL_PROOF.md', 'GQ80三类路线、完整C5互补检索与证明范围')
    gq80_asym = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d5D3/gq80_paired_matching_intuition/ASYM_ROOT_DISPOSITION.json', '打破共同对称后单个固定Q的实际求解结果')
    star331388 = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/threecut_star331388_gate/FINAL_NOTE.md', '331387→331388：预测、数据、旧路线修复上界与停止范围')
    star331388_proof = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d6D9/source_interface/threecut_star331388_gate/FINAL_PROOF.md', '纯删至多三条旧边加星的完整排除证明')
    cm253_note = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/source253_fourcut_star254_gate/COUPLED_NOTE.md', 'CM253三阶段预测、完整耦合域与实际结果')
    cm253_proof = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/source253_fourcut_star254_gate/FINAL_PROOF.md', 'CM253纯星及五删边一repair的完整范围证明')
    global256_note = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/global_c8_z32_action3_256/NOTE.md', '256固定Cayley族的预测、全域结果与停止边界')
    global256_compatibility = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/global_c8_z32_action3_256/COMPATIBILITY.json', '相位0与2的满槽冲突和两个实际参数例子')
    source585_note = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/PORT16_NOTE.md', '585固定p0原型的预测、实际全域和停止边界')
    source585_paper = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/SOURCE585_FOURCUT_PAPER.md', '强制owner匹配、16mask必要门与p0-owner例外')
    source585_owner_paper = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/OWNER_P0_NEXT_INTERFACE.md', 'p0导出affine plane、k≥2纸面排除与当时k=1必要接口')
    source585_k1_note = local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d9D3/actual585_modified_edge_interface/K1_NOTE.md', 'k=1全64owner域与3200DFS实际终态')
    small360 = later.get('source360_subdivision361', {})
    summary360 = esc(small360.get('summary_zh', '实际360源已取得，正在执行同一源最多540条旧边的单点细分有界批次；预测首边的新根R8能覆盖全旧图，尚不能据此宣称达标。'))
    followup_html = f'''<h2>后续一轮：严格范围与UNKNOWN分开记录</h2>
<p><strong>(11,3)：715固定源的保边扩张已完整停止。</strong>实际195个余度点是65个P3三胞类；原“独立度8副本”猜测被字面数据推翻。早先先排旧诱导固定的任意助手块，{proof715}；本轮允许跨类旧旧补边后仍得到完整排除，见下方联合路线预算闭合。没有排除一般(11,3)，未形式化、不声称历史首创，0新图。</p>
<p><strong>(4,8)：路线数够，但共享平移不能实现。</strong>69相位控制器全部4761槽的≤8非回退路线至少160；去除恒等重复后至少159，两个“容量不足”预测均被推翻。随后用坐标平移消去c2、整体缩放归一化，把整个固定r6/F139/四共享参数族化为19462代表。完整评估后最高只覆盖117/139个坐标，故这一族严格停止。另一个r、逐相位参数或新控制器均未排除。{phase69}。0个9591点图被生成，0新增纪录。</p>
<p><strong>(3,9)：600→602两轮仍是UNKNOWN。</strong>三cut＋一repair与四cut分散pins＋两repair各固定样本10000配置均无hit。首批9999先败于helper600，另1败于helper601；第二批10000先败于helper600。两轮都没有进入old-old检验，不能误归因于旧路线损伤，更不能记整族NO。四cut消除了强制同cut双pin，但实际样本没改善新根覆盖；两个规则已停止，累计2.860CPU/20。{sample602}。</p>
<p><strong>熟悉D4源的一次小pilot：</strong>尝试把已成功192×F3⁴的五种字面映射按2→−1→mod2转为3072点/10度规则。实际0→183的唯一反向只到2或13，故无向性失败，未生成图。独立整数计算发现该signedlift的逆关系含−3e1，特征非3时不会消失；这只排指定整数代表，不排重设计矩阵。{signed2}。0新图/BFS，停止换域梯。</p>
<p><strong>(6,9)：已从33万点熟悉源定位真实自由度。</strong>Rodríguez–Canale源为C49⋉F6763，全6正则，cap6没有余度。对三类generator边分别做单点细分的新根必要覆盖门，遗漏14088/13875/14028个旧点；Cayley平移把三类结果推广到每条旧边，因此全部单边细分停止。{sub331k}。</p>
<p>旧F6959的42个action实验只固定了最后电压1512。新域先固定β5155，把三种normal translations用常数坐标gauge和scale化为P¹(F6959)+zero；跳过已知1512NO与zero断连，新查6958个有限τ及infinity。<strong>2302个参数修好了phase0，但phase1…11后共同幸存者为0。</strong>倒数action由群同构与τ→τr⁻⁹传输；{tau5155} · {tau_domain}。</p>
<p><strong>后续20个倒数对代表域已全部跑完：新139180个参数代表全失败、0未决。</strong>连同旧β5155及其倒数、各action的旧1512反例和zero断连，现完整排除F6959、primitive order49、固定相位1/36/45的全normal平移族。每个参数都有失败层及缺坐标；共同参数不能同时覆盖所有层，而不是只数某一层漏几个点。该结论不涉及order7/1、其他field、phase或连接集。累计60.133CPU/90，1次编译，0候选图；已停止，不自动换域。{tau_batch}。</p>
<p><strong>(4,5)：根据旧端口障碍，实际改了连接规则。</strong>自然364点源有28个3度端口、336个4度核心点。配对全部端口增加14条旧旧边，删两条不相交核心旧边，再加一点连四个断边端点；得到365点730边、全4度候选，保留712/714旧边。预测至少一个样本能让新点五步覆盖旧图。10000个不同配置全部败于新根R5，首例新点到旧0距离6；0配置进入旧点对检查。预测被本样本推翻，不能归因于旧点对损伤；整族仍UNKNOWN。累计1.538CPU/20，已停，不换seed续跑。{star365}。</p>
<p><strong>(3,6)：把改边规则转到真实132小图。</strong>133点受degree2根容量127及奇偶约束阻断，故目标134。删三条不交旧边，余端点做一条旧旧repair和两组2pin，连接两个相邻新点。相比D5多一层路线：精确联合条件是R4(A)∪R4(B)∪[R5(A)∩R5(B)]覆盖修改后旧图。预测本批至少一配置可同时通过两新根；10000配置中9997败于首helper，余3败于对侧helper，0旧根检查。额外半径支持尝试但本样本未实现共同覆盖；仍是样本UNKNOWN，累计1.872CPU/20，已停。{repair134}。</p>
<p><strong>(3,8)：改变为单边细分，检验完整有限规则。</strong>361点允许degree2新点，因为根容量511大于361；不能套用(3,6)的127反例。新根R8等价旧边两端点R7并覆盖，但旧点对仍可能被切边延长。{summary360} {subdivision361}。</p>
<p><strong>(3,10)早期历史：旧精确范围直接继承，避免重复。</strong>实际Conder1250是非二分图，“二分图偶直径使新根自动过门”的前提不成立。旧单细分与5614双cut/helper范围已全排，本轮0下载、0BFS。原边(0,1)两端到1178的距离均10，使新点距离11。该快照之后已完成新三cut移端口和四helper星范围，当前终态见本页新增对照。{inherit1250}。</p>
<p><strong>(4,3)：三个41点源的42点最小改造完成对照。</strong>42点max4/D3迫所有度数为4。删两条不交旧边，把4端点接新星点，得42/84全4regular。N1的3075配置中，3个新根过门却都败于旧点对；首nonpin pair1→33原3步变新最短4步。{star42}。随后预言“换成N2/N3至少一源也有新根过门”，实际6150配置完整检验支持：N2有6个新根过门但全败于旧点对，N3没有新根过门。N2首pair0→1只有一端是pin，原路0–37–4–1因删1–4而失效，最终最短4步0–18–8–13–1；未称旧路线唯一。此对照只做14个候选旧根和1个原源单pair诊断，0旧源全根重验。三源共9225配置严格排除同一双cut4star规则，换源本身仍未兼顾新根与旧路线；停止此规则，下次须有旧关键路线补偿。其他源、不同改边和一般(4,3)未排。{star42_comparison}。</p>
<p><strong>(3,6)：从路线容量推进到共享参数冲突。</strong>140=10×14是Petersen10普通覆盖超过132的最小层数。实际≤6非回退词数为同点25、相邻21、非邻17；完整64个奇偶模式只有21/62通过每槽至少7词的必要条件。两实际20点中间图各有12个五边形，每点恰零步加三面正反方向。七层返回覆盖要求相邻面分属三种非零±电压类，但已绑定的“中心面＋五面奇轮”不能三着色，故排全部固定Petersen的order14群覆盖（含C14及order14二面体），不是继续搜索C7电压。另把连接放宽为标量仿射F16，非邻17路逐输入覆盖16值迫至少16路同斜率；实际17个删例外差矩阵在mod3/mod5均rank6，迫斜率全1，再被逆路重复最多13/16返回排除。两个实际H20的F7标量仿射分支也由整数minor−1闭合。全为paper＋小证书，零140/160点图、零BFS/Lean，累计3.688CPU/5；不排一般置换、半线性、其他基底或一般(3,6)。停止此族，下一代须改变短返回路线而非机械换域。{petersen_route} · {petersen_proof} · {affine16_proof}。</p>
<p><strong>(4,3)：反例确实改变了下一次生成规则，但联合预测被推翻。</strong>只取N2已有的六个“新根过门、旧pair失败”基例；从四pin中撤一个p，切第三旧边a–b，添加旧旧补偿p–a，并把新星端口移到b，保持42/84全4度。预测至少一例能修好保存的旧pair并保住新根覆盖。完整3048个允许参数中，426修好旧pair，却426全部新根R3失败，0例进入全部旧根检验。首例把0→1从4步修成直接边1步，但41→1变为最短41–2–15–34–1长4。说明这条局部移端口规则把覆盖责任移走，未同时兼顾；暂停本线，不加第二repair或换seed。跨六基例未做literal去重，3048是参数数，不是独立图数；只关闭指定有限域，不排一般三cut及一般(4,3)。{star42_repair}。</p>
<p><strong>(8,4)：换到低一度的源，实际检验两份旧图之间的路线互补。</strong>保留两份684点7度D4源的全部4788旧边，每点余1口用于684条跨副本完美匹配，若跨层距离≤4即得1368/5472/8regular，可比主表1100多268。核原配方后纠正：684不是Cayley图，它是H342的两轨道right-voltage lift，主表星号也可指前身672。共享右移342参数先完整失败；随后让两个轨道独立右移并允许轨道交换，准确得到所有H左作用等变匹配233928域。旧342严格跳过，新233586全查，均败于首0→0跨层槽，后三槽未测。完整覆盖条件由≤4步只需一次跨层推得，并分解为两类路线集合的bitset并，不逐图生成/BFS。两个正预测均被推翻；停止固定源的完整等变匹配族，不外推为任意匹配或一般(8,4)无解。累计2.924CPU/10，零新增图。{two684_note} · {two684_domain}。</p>
<p><strong>(5,3)：新完成一格实际检验，重点从容量转到路线互补。</strong>保留W(3,3)的80点160条关联边，点侧与线侧各补一个完美匹配，目标80/200/5regular。跨侧和原近点对已≤3，只需覆盖1080个原远点对；精确路线为匹配–关联–关联、关联–关联–匹配、关联–对侧匹配–关联。旧五窗均UNKNOWN且无候选，不重启原timer。新绑定共同五阶对称后，保全部近端匹配块，得到280变量/16度式/216远点对轨道。各侧65625匹配完整枚举：最大贡献114与113，总227，故“容量不足”预测被推翻；两个首argmax合并仅158、重叠69，不能当作joint最优。随后用缺口membership索引，完整检查所有合格10769点匹配与15198线匹配的兼容性，全部为空；精确关闭共同symplectic C5子族，隐式配对域65625²，无显式43亿逐对搜索。原任意配对族仍UNKNOWN。依据此结果实际打破对称：固定经预算筛选的Q1361，让P任意且非C5；515残余覆盖式的一个合法CaDiCaL窗口返回raw UNSAT，仅限此Q，未记录或检查UNSAT证书，不升级成一般排除。两次未开始search的启动错误及费用保留，累计4.886CPU/30，0图/BFS。暂停这一Q，不换Q2或继续timer。{gq80_proof} · {gq80_asym}。</p>
<p><strong>(6,9)：新根覆盖与旧点对修复形成可检验的连接预算。</strong>目标331388由旧331387点6度源加一点得出。最小规则删三条不交旧边、连接六端点，名义全6度。旧实验没存完整缺集，本次只为新问题导出一次identity深8支持/最短路条数，B8=281007；三缺集都遍及49相位，64827相位组合无空交，推翻phase快捷证书，单凭这一步不排normal坐标。随后实际找到三类首删边各32/21/32个旧点对，其所有九步最短路必经过该边；另外四pin必须命中它们端点的B3。完整扫描每类994161源边，先剔首边两端后994150条中，一条边最多命中11/7/12项，因此两条总上界22/14/24不足，严格排尽全部三删边六星参数，包括所有phase/normal选择，不是样本未成。零maskpair OR、零12代表实际检查。进一步支配把上界推广到原先过滤的边，得到任意至多三条旧边删除、再加一点连任意获释端点也失败，允许共享端点及非正则结果，但不含旧旧补边。这样的全端点星至少有一个旧点对距离10。累计4.576CPU/20，新问题supportBFS1/DP1、源D9重验0/旧单细分重跑0/候选图0。纯星继续此源至少要四条旧删边，或实质改规则；本轮停止不自动续。{star331388} · {star331388_proof}。</p>
<p><strong>(8,3)：CM253的局部补点从独立容量推进到实际连接兼容性，现已停止。</strong>继承1012条旧边各一条unique3路线，正确保留首、中、末位置并左平移后，每首边类得到27项义务，三位置各9。四cut八星的余三条边最多命中18，严格排除。改变为五条不交旧cut、一条连接两个非星端点的原非边repair及八星后，repair可补11项、星端口上界24，独立和35并不足以判否；这次预测被推翻。再绑定同一repair与两个半删边邻端，完整扫描四类各30378个repair、1910136个合法半选择，base最多12；加余两完整删边最多12，总24仍小于27，因此指定五cut一repair规则完整NO。repair确能补路线，但其最好效果不能与星端口的独立最好效果同时实现。纸面另用direct hit界排任意至多五条旧边删除（可共享）＋单纯星；不用度数可能达10的全端点星作合法max8图。累计3.686CPU/20，候选图/BFS/源D3或unique3重验均0。停止CM253局部线，不扩cut/repair；不排多repair、其他源或一般(8,3)。随后实际换到C8⋉3Z32的256点全局Cayley规则，结果见下一段；未继续CM局部样本。{cm253_note} · {cm253_proof}。</p>
<p><strong>(8,3)：全局256点Cayley规则也已完整收束。</strong>这不是CM253改边，而是在循环加法Z32上由C8乘3作用，正生成元phase固定1/2/3/4、四normal自由。457个真实逆配对短词按phase给出不同系数形式63/58/58/58/46/58/58/58，八槽均过32容量门，预测支持；形式容量足够没有推出共享参数可实现。完整规范域61440，严格去掉4096个不连通奇偶代表，57344连通代表逐八槽全部完成，含3072个实际7度及54272个8度案，0共同全满。各phase都能单独覆盖32；仅后处理已有结果发现最小冲突对phase0/2：各自320/1344组参数可满，两者共同为0。实际b=[1,1,2,23]覆盖[32,31,31,29,26,29,31,31]，b=[1,0,2,10]覆盖[27,29,32,32,29,32,32,29]，展示冲突而非只报总缺项。累计2.274CPU/20，兼容诊断只读旧57344行、未新增参数；图/BFS/field/solver/Lean均0。停止固定group/action/phase全normal族，不自动换群或相位，不排其他256点群或一般(8,3)。{global256_note} · {global256_compatibility}。</p>
<p><strong>(9,3)：第13格取得新实际检验，仍无新图。</strong>实际585极性源有65个8度绝对点A与520个9度core，不是Cayley；原保边扩张全NO继承、不重跑。新规则选四条core边删除，新点连八core端点与固定p0=actual顶点0，其余64A可任意完美匹配；只限定cut端点owners均避p0。旧A-A唯一3路使每cut的owner pair必须被匹配，因此匹配不能扩大新根已覆盖的A集合；四个16端口mask必须分割其余64A。全2080条core边逐一绑定，必要过滤留下1568边、448core均为7度，域数预测支持；保旧32条sigma边参与新旧混合，仅继承其完整四旧边子域NO。3697DFS状态全部穷尽，无四mask partition，正向存在预测被推翻。累计1.881CPU/20，0新BFS/core-R2/匹配/586候选图。原有限门只排固定p0的k=0原型。随后纸面从p0导出2-(64,8,1) affine plane，任意k≥2个p0-owner cuts迫U≤63-k、自由mate最多补k，新根A覆盖≤63<65，故这部分也严格NO。当时仅剩k=1的必要接口：四个16-mask须两两不交、union64含p0，唯一漏t配自由owner。现已实际完整检验64owner/1568far的skip-one exactcover，3200DFS结束，端口packing0，存在正预测P1被推翻；P2/corestage完全未进入，不能称corefail。k0、k1数值NO与k≥2纸面NO合并，关闭固定p0=0整个四顶点不交corecut／八core+p0星／其他64A任意匹配规则；不排其他p0、非matching cuts、额外repair、多helper或一般(9,3)。累计2.736CPU/20，k1没有再parse源或生成coreR2/BFS/匹配/586图；(10,3) actual650 FP-transfer现亦终态：1170变量覆盖模型单次20秒无incumbent，UNKNOWN；未进入15配对或新旧根检验。{source585_note} · {source585_paper} · {source585_owner_paper} · {source585_k1_note}。</p>
<p><strong>715新认识最终闭合：</strong>允许任意补旧旧边后，联合core/eligible路线预算先迫minH3及邻居H度和12/13。再对任意助手度d=4…7，core覆盖要求54+d≤7d+11，四种度数都不可能。于是所有H度只能3或≥8，min3点的邻度和只能9或≥14，再次矛盾。故实际715源保留全部旧边时，任意新增old-old/new-old/new-new边都不能形成非空有限扩张；包括原P3内部补三角。下一步必须删改旧边或换源。旧mixed-min3开放状态已保留为历史；这是源图范围排除，不是一般(11,3)无解。{cross715}。</p>
<p><strong>这15格的本轮迁移仍0新增达标图；当前全项目{current_graphs}图／{current_pairs}参数／{current_Lean}具体Lean。</strong>并行从熟悉D4源取得了新的16416点完整合法图，对当前主表16384多32点，详见<a href="graph_catalog.html">全图清单</a>及<a href="progress.html">进展页</a>。它不属于这15格老题，不混计老题攻关成果。</p>'''
    latest_html = f'''<h2>最新实际进展：仍0新图，合作路线与全局电压已做完整模型检验</h2>
<p><strong>本轮仍0新增完整达标图；全项目{current_graphs}合法版本／{current_pairs}参数／{current_Lean}具体Lean继承。</strong>以下局部构造、完整范围排除与原始solver结果分开记账。</p>
<table><thead><tr><th>参数／具体问题</th><th>实际证据</th><th>决定</th></tr></thead><tbody>
<tr><td>(8,5)，binary240的C23普通覆盖，目标5520</td><td>66路径的逐边flow差rank65，显式解出单packet全23。全28920packet的2699760flows均不同；32个完整条件电压仍无D5，24例修好首坏diagonal，最佳所有packet至少18</td><td>四全局系数旧NO保留；独立逐边电压仍UNKNOWN，停止无额外全局规则的采样</td></tr>
<tr><td>(11,4)，3645→3646，单cut＋原7freepins</td><td>全部20044edge均newroot失败，最好漏305。复用1993 R3支持、仅补1652，0旧根候选BFS</td><td>关闭固定源singlecut-star；两cuts若都避前3444点内部边，也由712&lt;743上界排除</td></tr>
<tr><td>(4,5)，自然364保边合作，14helpers</td><td>tree用旧容量纸面排；1930单环拓扑中1910败一般距离门、20败外国cell覆盖门，0幸存</td><td>固定source/noaddedoldold的1–14helpers完整NO，不排任意finiteH或一般378图</td></tr>
<tr><td>(4,5)，Petersen细分H19，目标383</td><td>5005pattern有235个Hdiam4，归6轨道；完整28port assignment六模型各rawUNSAT。诊断0..3helper要求raw冲突，0..1为2秒UNKNOWN</td><td>无383图；未proofchecked不冒形式化整族NO，尚不能判单helper不足或多helper兼容失败。停止该骨架</td></tr>
</tbody></table>
<p>{local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d8D5/binary_C30_base240_C23_cover/EDGE_VOLTAGE_NOTE.md','逐边电压的预测与全局检验')} · {local_link('research/ddp/two_successful_methods_20261101/retained_edge_transfer/published_d11_3645_D4_source_gate/one_cut_all_free_star3646/NOTE.md','3645单cut完整结果')} · {local_link('research/ddp/two_successful_methods_20261101/retained_edge_transfer/natural364_cooperative_helpers14_read/NOTE.md','14helper证明与枚举')} · {local_link('research/ddp/two_successful_methods_20261101/retained_edge_transfer/natural364_petersen_subdivision19/NOTE.md','Petersen19完整模型与卡点')}。</p>
<p><strong>下一参数(3,9)：600→602。</strong>两条不交旧cut的四端点分成2+2，分别连两个相邻helper；全部3种分割均保留，静态域1208250配置。旧3/4cut的10000样本不适用。新根覆盖可由原G的R7/R8精确筛，旧旧距离仍另验；本轮只完成原始scope与纸面接口，尚未启动该批。</p>
<p>{local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_cut_adjacent_helpers602_read/READ_GATE.md','600源、旧范围与3种分割')} · {local_link('research/ddp/two_successful_methods_20261101/stale_record_transfer_d3D9/two_cut_adjacent_helpers602_read/WEIGHTED_SOURCE_DISTANCE_INTERFACE.md','权1/2路线精确公式')}。</p>'''
    page = f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>长期未提高的度直径问题：15格候选与Moore差距</title>
<style>body{{max-width:1320px;margin:30px auto;padding:0 20px;font:16px/1.7 system-ui,sans-serif;color:#193047}}h1{{font-size:28px}}h2{{margin-top:30px}}a{{color:#12639c}}.note{{background:#ecf4fa;padding:12px 18px}}.muted{{color:#526576}}.scroll{{overflow-x:auto}}table{{border-collapse:collapse;width:100%;font-size:14px}}th,td{{padding:9px;border-bottom:1px solid #d5dee5;text-align:left;vertical-align:top}}th{{background:#f0f4f7}}td:last-child{{min-width:320px}}input{{font:inherit;padding:7px;width:min(96%,600px)}}code{{background:#eef2f5}}</style></head><body>
<h1>长期未提高的开放问题：15格候选及方法迁移</h1>
<p>同步：{esc(state['updated_UTC'])}。<a href="{MAIN}">当前Comellas主表</a> · <a href="stale_record_candidates.csv">15行CSV</a> · <a href="stale_record_candidates.html.txt">本页完整HTML源码</a> · <a href="progress.html">进展页</a></p>
<div class="note"><strong>14格当前点数至少约10年前已达到，另附1格8年备选；均未被主表标为最优。</strong><p>原范围4≤Δ≤12、D∈{{3,4,5}}中占8格。其余沿用用户后来授权的全部开放主表范围。选题仍结合覆盖接口与已有失败；不会把年代久直接当成更容易。</p></div>
<p>Moore上界采用经典公式 M=1+Δ∑<sub>j=0…D−1</sub>(Δ−1)<sup>j</sup>。“差距”是M−L，占比为(M−L)/M；它是上界余量，并不保证中间点数可实现。“已知不晚于1983”只表示原表截至1983末已有同点数，不冒作精确首次发现日期。2024–2026同点数重构不会清零年龄。</p>
<p>这15格的经典上界余量为11.1%–88.7%；(9,3)只有11.1%，空间相对较紧，保留作结构型备选。不会仅按差距排序，也不会把较大差距解释为容易。已有4q／30q³模板在8–11度最多取q=2、名义240点，低于这些D3格的主表；因此直接换域不足以改善，实际检验须改变端口、控制器或旧边路线。</p>
<p><strong>15格都已有本轮新检验，目前这15格仍0新增达标图。</strong>(3,10)新增实际试验及整族覆盖门见下方；原单细分和双cut严格排除继续继承，不重跑。各项仅按已检验范围记NO或UNKNOWN，15个一般问题均未因此关闭。熟悉D4源此前已有16416点合法图，另列进展页，不混计本轮老题结果。</p>
{latest_html}
<h2>候选清单</h2><p><input id="filter" aria-label="筛选候选" placeholder="筛选参数、年份、方法，例如：1100 或 1983"></p>
<div class="scroll"><table id="candidates"><thead><tr><th>(Δ,D)</th><th>当前主表L</th><th>同点数已存在的日期</th><th>经典Moore上界M</th><th>距上界/比例</th><th>下一点数门槛</th><th>可迁移方法与已停范围</th></tr></thead><tbody>{''.join(table_rows)}</tbody></table></div>
<p class="muted">(3,8)=360为2018年的8年备选，不计入14格十年名单。对(3,5)/(3,6)，71/133点分别超过degree2根的63/127点容量，故必须全3度，再由奇偶约束阻断，表中直接写72/134；其余门槛也不是存在性承诺。</p>
<h2>新增对照：第15格(3,10)与一次D4迁移</h2>
<p><strong>(3,10)：修原缺点会撤走原覆盖责任，随后换结构并检查完整域。</strong>1250点源的固定基例保住1178直连，再用第三cut/repair修1058。9个定向配置全修好1058；移0/1的6例却准确把被撤点推到距离11，支持事前P3；移869保住自身距离10，仍漏其它区域。全11178配置均败于新根；5454例虽修好原缺点，仍无完整覆盖。没有进入旧点对检查，不能把失败归因于old-old损伤。</p>
<p>据此改用四helper星，保全部六个断边端点。初固定1865例均中心失败；推导last-cut精确覆盖后，不再逐图重算，完整1743779个三matchingcuts组合全失败。中心距离恒为2加到六端点的原图距离，且不依赖六端点配对方式，因此排该源整套三matchingcuts/K1,3机制；不是一般(3,10)无解。</p>
<p><a href="ddp/two_successful_methods_20261101/stale_record_transfer_d3D10/source1250_interface/thirdcut_route_repair1252/NOTE.md">预测和逐例对照</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d3D10/source1250_interface/thirdcut_route_repair1252/P3_ADDENDUM.md">撤pin障碍的纸面证明</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d3D10/source1250_interface/threecut_fourhelper_star1254/global_three_matching_gate/NOTE.md">星形全域结果</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d3D10/source1250_interface/threecut_fourhelper_star1254/GLOBAL_CENTRE_PAIRING_SCOPE_ADDENDUM.md">中心反例与配对无关</a></p>
<p><strong>另外(14,4)：两份6804保旧边＋任意跨副本匹配也已排除。</strong>先相位计数328&lt;567否定恒定偏移，再出现普通容量573的排列；去折返后降为547，新NB模型仍UNKNOWN。随后实际点球重叠给出更强结论：全部6804点球大小的最大值产生上界6984，必然重复覆盖至少260，因此某个跨层根至多覆盖6724&lt;6804。任意point matching都失败，不再继续相位/纤维参数；模型本身的UNKNOWN仍如实保留。未生成13608图，0新纪录。</p>
<p><a href="ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/NOTE.md">6804迁移的完整推导与纠正</a> · <a href="ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/POINT_BALL_OVERLAP_PAPER.md">实际球集重叠证明</a> · <a href="ddp/two_successful_methods_20261101/retained_edge_transfer/two6804_matching13608/OVERLAP_RESULT.json">全部点最大值与重叠回执</a></p>
<h2>最新实际检验：停止等变匹配线，保留UNKNOWN边界</h2>
<p><strong>(8,4)／1368：</strong>684源的K19模型已经执行。全模型60秒UNKNOWN；一次排列容量门得到min19后，冻结排列的shift模型20秒仍UNKNOWN。最紧的28→28行能独立铺满19点，推翻“这行自身不可实现”的预测；加入2603条由紧行推出的二元约束，最后5秒仍UNKNOWN。累计96.357/100CPU停止，不判不可行，不再换排列或延长同一窗口。<a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two684_shift_matching1368/K19_exact_matching_interface/NOTE.md">完整预测、检验与范围</a>。</p>
<p><strong>(8,4)／1344：</strong>另一个Sampels672源的全部672个rightmatching已完整排除。保存行诊断显示六个相对phase各自最多106/112，均无局部满覆盖；原“各层可满、共享参数冲突”的预测被反驳。源672的恢复只是已知构造复现，不计新增图。<a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D4/two672_right_matching1344/NOTE.md">结果及单层障碍</a>。</p>
<p><strong>清单外补充(9,4)／2200：</strong>两份已有1100源保旧边加rightmatching，完整1100参数亦无D4图。各层候选endpoint-pairs容量至少66，不能先用计数排除；但相对phase10实际最多43/55，66个候选对至少23个重复映像。因此不是继续磨总坏对数的问题。只排固定源等变匹配，不排任意匹配或一般(9,4)。<a href="ddp/two_successful_methods_20261101/stale_record_transfer_d9D4/two1100_right_matching2200/NOTE.md">有限批与瓶颈</a>。</p>
<h2>本轮新检验：(4,5)联合端口与(8,3)实际多路线</h2>
<p><strong>(4,5)由样本未知推进到完整规则NO。</strong>固定四接点后，有缺口的端口只能配给无缺口端口；相应三个资源集合嵌套，得到三条Hall数量条件。固定首P的24对1反驳存在配对的预测。随后复用4个core R4、补332个必要支持，全部196371不交corecut对均有至少21个β2缺口owner、却至多2个相邻入口；0匹配求解或候选图，关闭整个指定规则。21来自完整有限数据，不冒新的普遍几何定理。<a href="ddp/two_successful_methods_20261101/stale_record_transfer_d4D5/port_matching_core2_star365/all_two_corecut_Hall_gate/FINAL_PROOF.md">完整证明、预测与范围</a>。</p>
<p><strong>(8,3)实际实现了低秩路线互补，尚无新图。</strong>在已有C30真实0→18层对、两套完整逆chart上，对全部8个源坐标检验：ARC三rank2 packet并满8，合法COLLINEAR只并6，全部9条短路也只并7。再改矩阵修唯一0→5路径，4→8且相邻覆盖保住，却同时破坏4类其它词；goodword24→28的预测被推翻，两套实际都24。<a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/controller32_F2_multiroute_readgate/adjacent_packet_controlled_test/RESULT.json">受控逐源检验</a> · <a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/controller32_F2_multiroute_readgate/conjugate_route_repair/RESULT.json">修补与损伤对照</a>。</p>
<p>理解实际改变生成器：typed C30插两点的378450参数有284310个simple控制器，两chart全失败；普通路线容量进一步排284295，剩15个在第二新根全缺路，故这个插点族的任意8fiber/每port至多2choices规则都NO。改为三角单元C33/C11，100规范参数的同层fibres全部通过，但每个控制器至少一类根三步到不了全部33点，投影存活0；这个三型C11族本身D&gt;3，换矩阵无用。停止两族，不继续m12、其它chart或群阶梯。<a href="ddp/two_successful_methods_20261101/stale_record_transfer_d8D3/controller32_F2_multiroute_readgate/NOTE.md">全部数值、图源、生成规则与未排范围</a>。</p>
<p><strong>下一问题：</strong>{esc(later.get('next_computation_decision', {}).get('question_zh', '转(10,3)的650源，先做保存覆盖矩阵的结构诊断，不续原限时solver。'))} 数值是否已授权，以实际状态JSON为准；没有候选图时不启动新图验收。</p>
<h2>此前熟悉D4源(16,4)的覆盖对照</h2>
<p>这部分不属于上方15格。当前(16,4)已接受图为16416点，本次尝试16417，没有新图。先保留当前全图，使用4050个余度pin的实际闭R3支持寻找≤16点覆盖；已知完整覆盖仍29点，单次求解限时UNKNOWN。</p>
<p>再预测“删除四组克隆的阻挡边、让五个受影响点互相连接”能修复路线。342个中心、5886个合法极大连接方式全部失败；进一步即使允许五点形成完整团、忽略其度数限制，342例也全部缺到旧点的路线。因此该局部规则的主要障碍是保留下来的旧邻域覆盖不足，继续调整五点间连边不能修复。</p>
<p>依此改变生成规则：固定预留原source点0的14点邻域，再重选32个整块，最后复制点0。192变量的唯一30秒窗口实际探索7811个分支，返回31块，未找到32块；原始TimeLimit，仍是UNKNOWN。未把31块生成更小的图，也未换中心续算。下一步须换覆盖接口或回到其它候选，不能把这几轮UNKNOWN写成一般(16,4)无解。</p>
<p><a href="ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/cooperative_fourblocker_repair16417/NOTE.md">局部连接的预测与实测</a> · <a href="ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/degree16_plane864/cooperative_fourblocker_repair16417/K5_RELAXATION_POSTPROCESS.json">放开度数后仍失败的逐例数据</a> · <a href="ddp/two_successful_methods_20261101/retained_edge_transfer/published_d15_15552_D4_source_gate/nonorbit_clone_interface/reserved_neighborhood_block_selection16417/NOTE.md">预留邻域的新模型与停止范围</a></p>
{followup_html}
<h2>前一轮的实际检验与历史范围</h2><div class="note">{esc(transfer.get('summary_zh', transfer.get('status','待返回')))}<br>该轮新合法图：{transfer.get('new_graphs',0)}。</div>
{''.join(gate_html)}
<h2>为什么不把D2老题排在前面</h2><p>六个符合年代的D2老格与经典Moore上界仅差约4.7%–12.3%：{esc(tight_text)}。因此本轮主名单优先上方直径≥3的15格；(8,2)/n61旧队列继续暂停。</p>
<h2>避免重复走已经排除的路</h2><p>(9,3)585源全体保边增广已排；(10,3)650源≤5删边的指定单hub模型已排；(4,5)364源保边、无旧旧加边、1–14个helper已排。它们均不等于一般参数无解。新动作必须实质改变连接规则、删旧边范围或来源。仅限时UNKNOWN的模型继续记UNKNOWN，不扩为整族失败。</p>
<p>截至本页状态，全项目{current_graphs}个合法named版本／{current_pairs}组参数／{current_Lean}个具体Lean实例；新纪录须交完整图并适量独立核验，全球优先权另行判断。</p>
<p>当前阶数：{local_link('research/ddp/two_successful_methods_20261101/public_baseline_audit/STALE_MAIN_TABLE_RECHECK_20261102.json','11月2日主表15项阶数回看，全部一致')}；原始年份沿用此前日期证据，未在此次回看中重查。日期证据：{local_link('research/ddp/two_successful_methods_20261101/public_baseline_audit/STALE_MAIN_D3_D5_20261101.json','D3–D5逐项出处')} · {local_link('research/ddp/two_successful_methods_20261101/public_baseline_audit/STALE_MAIN_D6_D10_20261101.json','D6–D10逐项出处')} · <a href="{EJC}">Delorme 1985原表（截至1983末）</a> · {local_link('research/ddp/two_successful_methods_20261101/public_baseline_audit/STALE_RECORD_CANDIDATES_AND_MOORE_20261101.json','完整候选数据与实际迁移状态')}</p>
<script>document.getElementById('filter').addEventListener('input',function(){{const q=this.value.toLowerCase();for(const row of document.querySelectorAll('#candidates tbody tr'))row.hidden=!row.textContent.toLowerCase().includes(q);}});</script></body></html>
'''
    dest = ROOT / 'research/stale_record_candidates.html'
    dest.write_text(page)
    dest.with_suffix('.html.txt').write_text(page)
    print(json.dumps({'rows':len(rows),'at_least10years':14,'secondary':1,'HTML_bytes':dest.stat().st_size,'transfer':transfer['status']},ensure_ascii=False))


if __name__ == '__main__':
    build()
