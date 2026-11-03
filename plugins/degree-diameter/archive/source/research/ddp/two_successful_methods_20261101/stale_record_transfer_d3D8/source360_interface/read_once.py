"""Source availability only. No graph parse, construction, BFS, or enumeration."""
from pathlib import Path
from urllib.parse import urljoin
from urllib.request import Request, urlopen
from html.parser import HTMLParser
import json, resource, time

START = time.process_time()
PREP = 1.0  # conservative charge for preceding bounded filename/scope/cache reads
BUDGET = 5.0
resource.setrlimit(resource.RLIMIT_CPU, (4, 4))
OUT = Path(__file__).resolve().parent
R = next(p for p in OUT.parents if (p/'research-wiki').is_dir())
CACHE = 'research/ddp/two_successful_methods_20261101/public_baseline_audit/STALE_MAIN_D6_D10_primary_cache/desc_g8.html'
BASE = 'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g8.html'

class Links(HTMLParser):
    def __init__(self):
        super().__init__(); self.active=False; self.links=[]
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='a' and a.get('name')=='38': self.active=True
        elif tag=='a' and self.active and a.get('name'): self.active=False
        if tag=='a' and self.active and a.get('href'): self.links.append(a['href'])

cache=(R/CACHE).read_text()
links=Links(); links.feed(cache)
exact=[x for x in links.links if x.endswith('/360-deg3-D8_adjlist.txt')]
assert len(exact)==1
url=urljoin(BASE,exact[0])
rawpath=OUT/'PRIMARY_360_ADJLIST.txt'
assert not rawpath.exists(), 'Do not repeat a previous source download'
http_calls=0
result=dict(status='SOURCE_INTERFACE_UNRESOLVED',source_n=360,
    source_degree=3,source_D=8,source_facts='Inherited primary; not revalidated',
    primary_description=BASE+'#38',cached_primary_description=CACHE,
    found_date='2018-10-16',Moore_bound=766,Moore_space=406,
    source_identity='Chen360, not the q5/q7 transferred graph',
    old_strict_scopes_consulted=[
      'ddp-current360-q8-orbit-q5q7-field-controls-20261027',
      'ddp-q8-source360-free-semi3-q5-critical-gate-20261027'],
    strict_same_subdivision_rule_NO_found=False,
    prior_source_literal_cached=False,download_url=url,
    numerical_candidate_budget_authorized=False,
    graph_parse_count=0,source_BFS=0,source_degree_check=0,
    candidate_graphs_generated=0,edge_enumeration=0,search=0,Lean=0)
try:
    http_calls=1
    with urlopen(Request(url,headers={'User-Agent':'DegreeDiameterResearchSourceRead/1.0'}),timeout=25) as response:
        data=response.read()
        result['HTTP_status']=response.status
        result['response_final_url']=response.url
    rawpath.write_bytes(data)
    text=data.decode('utf-8-sig')
    first=next(line for line in text.splitlines() if line.strip() and not line.lstrip().startswith('#'))
    # Read only the first adjacency row to name one future prediction; never build adjacency.
    fields=first.split()
    edge=[int(fields[0]),int(fields[1])]
    result.update(status='SOURCE_LITERAL_AVAILABLE_UNTESTED',literal=str(rawpath.relative_to(R)),
        downloaded_bytes=len(data),first_adjacency_row=first,one_fixed_edge_for_prediction=edge,
        raw_labels_preserved=True,format='Primary NetworkX adjacency text; only first row read, no graph parsed',
        prediction='For the first explicit source edge, the subdividing newroot reaches every old vertex within8; no old-old D8 prediction.')
except Exception as exc:
    result.update(status='STOP_SOURCE_LITERAL_UNAVAILABLE',error=type(exc).__name__+': '+str(exc),
        next='STOP, no guessed filename, second HTTP request, alternate source or template')
result['HTTP_download_calls']=http_calls
(OUT/'RESULT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
if result['status']=='SOURCE_LITERAL_AVAILABLE_UNTESTED':
    u,v=result['one_fixed_edge_for_prediction']
    pred=f'''# One explicit, untested prediction

For the first edge in the primary raw adjacency row, e={{{u},{v}}}, predict that
the new degree2 vertex z produced by replacing e with u-z-v has eccentricity at
most8 to all360 old vertices. This is the single concrete prediction, not a
claim of an accepted361 graph. Confidence is low: the degree2 rooted ball bound
511 leaves room for361 vertices, and the source provides alternate incidence
and edge-pairing routes, but neither fact proves simultaneous coverage.

The exact falsification is an old vertex x outside R7_(G-e)({{u,v}}). A failure
only rejects this edge. A pass requires a separate final-candidate old-old D8
check; sourceD8 alone permits a stretched distance9 after subdivision. No such
numerical gate or graph generation was run in this source-read scope.

If root later authorizes a bounded numerical batch, test this fixed prediction
first and report the actual missed target/path or full newroot coverage before
deciding whether any other edge is justified. Do not change source or template.
'''
else:
    pred='# Source gate stopped\n\nNo literal is available from the single exact primary download; no candidate prediction was numerically evaluated and no alternate template starts.\n'
(OUT/'PRED.md').write_text(pred)
note=f'''# Chen360 source interface; no numerical construction yet

Status: {result['status']}. The cached primary entry at desc_g8#38 names Jianxiang
Chen,2018-10-16,(degree3,diameter8,order360),Moore766. It constructs H from the
144-vertex symmetric diameter7/girth8 graph by replacing each edge with an edge
vertex and adding a complete pairing among the216 edge vertices. The published
H has three vertex orbits. These source properties are inherited, not checked.

The exact NetworkX adjacency link was extracted from the cached primary entry:
{url}
There was one HTTP download attempt and no guessed filename. The literal is
only retained as input for a possible later batch; no adjacency structure was
built. The existing Q8 lift recipe is an alternative description of the same
360 graph, not an additional source or result.

The old canonical strict scopes close the two frozen q5/q7 field controls and
the q5 free-semi3-normal variant. They do not close edge surgery on the original
360 literal. The consulted method ledger and source scope notes contain no
same-rule single-edge-subdivision exclusion. This is a scoped history finding,
not proof that no such fact exists anywhere.

For e={{u,v}}, put K=G-e and H=K+{{uz,zv}} with newlabel z. For every oldx,

    d_H(z,x)=1+min(d_K(u,x),d_K(v,x)).

Any simple path starting at z chooses u or v and cannot revisit z, so this is
exact, including infinite distances. Therefore the newroot condition is

    ecc_H(z)<=8  iff  R7_K({{u,v}})=V(G).

Also d_K({{u,v}},x)=d_G({{u,v}},x): a shortest path from the endpoint set can
never benefit from traversing e, because starting at its other endpoint would
shorten it. Thus the newroot condition may equivalently use R7_G({{u,v}}).
This equivalence does not apply to an individual endpoint distance or old-old
distances after deletion. A full D8 candidate needs both this newroot condition
and every old-old distance in H at most8. The sourceD8 certificate alone only
gives old-old distance at most9 after replacing one edge by a length2 route.

Degree accounting would be n361,m541,oldvertices degree3,newz degree2,max3;
the degree sum1082 is even. A degree2 root in a max3 graph has B8 size at most
1+2(1+2+...+2^7)=511, so the simple rooted-capacity obstruction does not exclude
361. Compare(3,6): its corresponding bound127 is below133. The classical
Moore766 and this511 rooted capacity are upperbounds, not existence evidence.

No sourceD8/degree/BFS check, graph construction, edge enumeration, search,
solver, field, Lean, ARIS, install or hash was performed. The source-read budget
is5CPU including a conservative1CPU preparation charge; no automatic numerical
continuation is authorized. Root owns any next numerical budget and global
acceptance. Same Goal remains active; no new graph count is made.
'''
(OUT/'NOTE.md').write_text(note)
elapsed=time.process_time()-START
terminal=dict(status=result['status'],running=False,all_processes_terminal=True,
    actual_interface_process_CPU_seconds=elapsed,
    conservative_prior_preparation_charge_seconds=PREP,
    cumulative_charged_CPU_seconds=PREP+elapsed,CPU_budget_seconds=BUDGET,
    HTTP_download_calls=http_calls,source_graph_parse_BFS_degree_checks=0,
    graph_construction_edge_enumeration_search_Lean=0,
    no_timer_reset=True,no_automatic_numeric_continuation=True,
    writes_limited_to_this_source_interface=True)
(OUT/'TERMINAL.json').write_text(json.dumps(terminal,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(terminal,ensure_ascii=False,indent=2))
