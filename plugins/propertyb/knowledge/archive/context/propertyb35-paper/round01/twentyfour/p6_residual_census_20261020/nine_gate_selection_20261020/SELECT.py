"""Independent 35-index reconstruction on only the 8569 stored nongated P inputs.
Nine-gate local paper proof and exact certificates accepted by root; cross-family whole-gate review pending.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
import json,time
HERE=Path(__file__).resolve().parent
SOURCE=HERE.parent/'CENSUS_NONGATED.jsonl'
PAIRS=list(combinations(range(6),2));C=set(range(5))
BLUE=[set(c) for k in (2,3) for c in combinations(range(6),k)]
start=time.process_time();seen=set();accepted=0;tail=[];menus={};menudata=[]
accepted_signatures=Counter();accepted_cells=Counter();tail_cells=Counter()
source_menu_nine={};reconstructed=0

def cell(r):return ','.join(map(str,r['inventory']))+';nine='+str(r['nine'])
def key(r):return (tuple(r['inventory']),r['nine'],tuple(map(tuple,r['higher'])),tuple(r['J']))
def clean_nine(sig):
    p4,p3,p2,p1,n1,n2,t,b,lower=sig
    return p4==9 and p3==p2==p1==n1==n2==0 and t<=3 and t+b<=20

def expand(r):
    degree=[8+(i==r['nine']) for i in range(6)]
    internal=C;high=[set(t) for t in r['higher']]
    traces=[set(internal)]+high[:]
    for edge,m in zip(PAIRS,r['J']):traces.extend([set(edge) for j in range(m)])
    subtotal=Counter(v for trace in traces for v in trace)
    singles=[degree[v]-subtotal[v] for v in range(6)]
    assert min(singles)>=0
    for v,m in enumerate(singles):traces.extend([{v} for _ in range(m)])
    assert len(traces)==35 and Counter(v for trace in traces for v in trace)==dict(enumerate(degree))
    assert [sum(len(t)==i for t in traces[1:]) for i in (2,3,4)]==r['inventory']
    assert all(any(set(pair)<=trace for trace in traces) for pair in PAIRS)
    assert all(sum(5-len(trace) for trace in traces if v in trace)>=18 for v in range(6))
    assert not set.intersection(C,*high)
    return traces,singles

def colour(traces,blue):
    pos=Counter();neg=Counter();roles=[]
    for trace in traces:
        if trace<=blue:kind=1;outside=5-len(trace);pos[outside]+=1
        elif trace.isdisjoint(blue):kind=2;outside=5-len(trace);neg[outside]+=1
        else:kind=0;outside=0
        roles.append([sum(1<<v for v in trace),kind,outside])
    assert roles[0][1]==0
    # For each blue point, its original star covers all 18 exterior vertices.
    lower=max(max(0,18-sum(5-len(trace) for trace in traces if v in trace and len(trace)>=2)) for v in blue)
    sig=(pos[4],pos[3],pos[2],pos[1],neg[1],neg[2],neg[3],neg[4],lower)
    return sig,roles

with (HERE/'NINE_CANDIDATE_SOURCES.jsonl').open('w') as out:
    for line in SOURCE.open():
        r=json.loads(line);k=key(r);assert k not in seen;seen.add(k)
        traces,singles=expand(r)
        choices=[];winner=None
        for blue in BLUE:
            sig,roles=colour(traces,blue);reconstructed+=1
            choices.append((sum(1<<v for v in blue),sig))
            if winner is None and clean_nine(sig):winner=(blue,sig,roles)
        possible=winner is not None
        if r['menu_id'] in source_menu_nine:assert source_menu_nine[r['menu_id']]==possible
        source_menu_nine[r['menu_id']]=possible
        if winner:
            blue,sig,roles=winner;accepted+=1;accepted_signatures[str(sig)]+=1;accepted_cells[cell(r)]+=1
            record=dict(r,blue=sorted(blue),signature=sig,single_trace_counts=singles,
                        indexed_source_roles=roles,gate='NINE_POSITIVE_JOINT_NEGATIVE_REPAIR',
                        mathematical_status='PAPER_PROOF_CHECKED_LOCAL_CERTIFICATES')
            out.write(json.dumps(record,separators=(',',':'))+'\n')
        else:
            tail_cells[cell(r)]+=1
            menu=tuple(sorted({sig for _,sig in choices}))
            if menu not in menus:
                menus[menu]=len(menudata);menudata.append(dict(id=menus[menu],signatures=menu,source_count=0,
                                                            example_source=r))
            mid=menus[menu];menudata[mid]['source_count']+=1
            tail.append(dict(r,new_menu_id=mid,own_blue_choices=[dict(blue_mask=b,signature=s) for b,s in choices]))
assert len(seen)==8569 and accepted==8020 and len(tail)==549
with (HERE/'TAIL549.jsonl').open('w') as out:
    for r in tail:out.write(json.dumps(r,separators=(',',':'))+'\n')
sig_sources=Counter()
for m in menudata:
    for sig in m['signatures']:sig_sources[str(tuple(sig))]+=m['source_count']
summary=dict(status='SOURCE_RECONSTRUCTION_PASS_LOCAL_PAPER_GATE_CHECKED',
             source_inputs=len(seen),candidate_nine_sources=accepted,tail_count=len(tail),
             indexed_colourings_reconstructed=reconstructed,tail_menu_classes=len(menudata),
             candidate_by_inventory_nine=dict(accepted_cells),tail_by_inventory_nine=dict(tail_cells),
             accepted_signature_distribution=dict(accepted_signatures),
             tail_signature_source_distribution=dict(sig_sources),tail_menus=menudata,
             cpu_seconds=time.process_time()-start,scope=__doc__)
countmenus=Counter();clean_sources=Counter();neg_counts=Counter()
for r in tail:
    signatures={tuple(c['signature'][:8]) for c in r['own_blue_choices']}
    countmenus[tuple(sorted(signatures))]+=1
    for signature in signatures:
        if signature[2:6]==(0,0,0,0):clean_sources[signature]+=1
for signature,n in accepted_signatures.items():
    import ast
    parsed=ast.literal_eval(signature);neg_counts[(parsed[6],parsed[7])]+=n
summary['tail_count_only_menu_classes']=len(countmenus)
summary['tail_count_only_menus']=[dict(signatures=k,source_count=v) for k,v in sorted(countmenus.items())]
summary['tail_clean_P3_P4_signature_source_counts']=[dict(signature=k,source_count=v) for k,v in sorted(clean_sources.items(),key=lambda kv:(-kv[1],kv[0]))]
summary['accepted_by_negative_counts']=[dict(N3=k[0],N4=k[1],source_count=v) for k,v in sorted(neg_counts.items())]
(HERE/'SUMMARY.json').write_text(json.dumps(summary,indent=2)+'\n')
print({k:v for k,v in summary.items() if k not in ('tail_menus','tail_signature_source_distribution','tail_count_only_menus','tail_clean_P3_P4_signature_source_counts','scope')})
