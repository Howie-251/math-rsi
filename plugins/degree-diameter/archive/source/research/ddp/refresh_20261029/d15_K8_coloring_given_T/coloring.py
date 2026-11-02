#!/usr/bin/env python3
"""Source-only recovery material. Never invokes a solver or constructs a graph.
Requires a future explicitly supplied, verified BACKBONE_CANDIDATE.json.
"""
import argparse, itertools, json
from pathlib import Path
HERE=Path(__file__).resolve().parent
CACHE=HERE.parent/'d15_D4_K2_route_gate'
N,K,W=15552,648,11

def save(name,obj):
    (HERE/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')

def variable(position,color):return 8*position+color+1

class CNF:
    def __init__(self):self.variables=512;self.clauses=[]
    def fresh(self):self.variables+=1;return self.variables
    def add(self,*lits):self.clauses.append(list(lits))
    def atmost8(self,lits):
        previous={}
        for i,x in enumerate(lits,1):
            current={j:self.fresh()for j in range(1,min(i,8)+1)}
            self.add(-x,current[1])
            for j,s in previous.items():self.add(-s,current[j])
            for j in range(2,min(i,8)+1):self.add(-x,-previous[j-1],current[j])
            if 8 in previous:self.add(-x,-previous[8])
            previous=current

def prepare(path):
    labels=list(map(int,(CACHE/'FREE_ORDER.txt').read_text().split()))
    backbone=json.loads(Path(path).read_text())
    assert backbone['status']=='VALID_INTEGER_BACKBONE_NOT_COLOURED'
    cols=sorted(backbone['selected_columns'],key=lambda p:labels[p])
    assert len(cols)==len(set(cols))==64 and all(0<=p<K for p in cols)
    assert sorted(labels[p]for p in cols)==sorted(backbone['selected_old_labels'])
    old=[labels[p]for p in cols];T=sum(1<<p for p in cols)
    r2=(CACHE/'target_R2_support.u64le.bin').read_bytes()
    r3=(CACHE/'target_R3_support.u64le.bin').read_bytes()
    assert len(r2)==len(r3)==N*W*8
    groups={};targets=[];rowmap=[];joint_R2_count=0
    for t in range(N):
        s2=int.from_bytes(r2[t*W*8:(t+1)*W*8],'little')
        if T&s2:joint_R2_count+=1;rowmap.append(-1);continue
        s3=int.from_bytes(r3[t*W*8:(t+1)*W*8],'little')
        mask=sum(1<<i for i,p in enumerate(cols)if (s3>>p)&1)
        assert mask.bit_count()>=8, 'Supplied T fails the integer backbone necessary condition.'
        if mask not in groups:groups[mask]=len(targets);targets.append([])
        row=groups[mask];targets[row].append(t);rowmap.append(row)
    c=CNF()
    for p in range(64):
        c.add(*(variable(p,a)for a in range(8)))
        for a,b in itertools.combinations(range(8),2):c.add(-variable(p,a),-variable(p,b))
    for a in range(8):c.atmost8([variable(p,a)for p in range(64)])
    # First occurrences order the eight otherwise interchangeable colors.
    # No old point/fiber is anchored; all positions are relative to this supplied T.
    for p in range(64):
        for a in range(1,8):c.add(-variable(p,a),*(variable(q,a-1)for q in range(p)))
    edges=[]
    for mask,row in groups.items():
        positions=[p for p in range(64)if(mask>>p)&1]
        for a in range(8):c.add(*(variable(p,a)for p in positions))
        edges.append(dict(id=row,mask=mask,positions=positions,targets=targets[row]))
    with (HERE/'model.cnf').open('w')as f:
        f.write(f'p cnf {c.variables} {len(c.clauses)}\n')
        for row in c.clauses:f.write(' '.join(map(str,row))+' 0\n')
    save('INPUT_AND_TARGET_MAP.json',dict(backbone=str(Path(path).resolve()),columns=cols,old_labels=old,
        target_to_hyperedge=rowmap,hyperedges=edges,joint_R2_covered_targets=joint_R2_count,
        residual_target_count=N-joint_R2_count))
    save('MODEL.json',dict(status='PREPARED_ONLY',variables=c.variables,clauses=len(c.clauses),
        selectors=512,residual_targets=N-joint_R2_count,unique_hyperedges=len(edges),
        target_rows_complete=True,helper_pin_count=8,colors=8,solver_calls=0,source_graph_reads=0,
        first_occurrence_color_order=True,point_or_fiber_anchor=False))

def decode(path):
    data=json.loads((HERE/'INPUT_AND_TARGET_MAP.json').read_text())
    positive=set()
    for line in Path(path).read_text().splitlines():
        tokens=line.split()
        if not tokens:continue
        if tokens[0]=='v':tokens=tokens[1:]
        elif not tokens[0].lstrip('-').isdigit():continue
        positive.update(int(v)for v in tokens if int(v)>0)
    colors=[]
    for p in range(64):
        chosen=[a for a in range(8)if variable(p,a)in positive]
        assert len(chosen)==1;colors.append(chosen[0])
    assert [colors.count(a)for a in range(8)]==[8]*8
    for edge in data['hyperedges']:
        assert {colors[p]for p in edge['positions']}==set(range(8))
    groups=[[data['old_labels'][p]for p in range(64)if colors[p]==a]for a in range(8)]
    save('COLORED_CANDIDATE.json',dict(status='CACHED_EXACT_K8_COVER_VALID_NEEDS_LITERAL_GRAPH_CHECK',
        old_pin_groups=groups,backbone=data['backbone'],expected_n=15560,expected_m=116408,
        max_degree_bound=15,source_D4_inherited=True,literal_new_graph_checked=False,
        all_residual_targets_verified=True,all64_pins_unique=True,solver_started_by_this_program=False))

if __name__=='__main__':
    p=argparse.ArgumentParser();s=p.add_subparsers(dest='mode',required=True)
    q=s.add_parser('prepare');q.add_argument('--backbone',required=True)
    q=s.add_parser('decode');q.add_argument('--solution',required=True)
    a=p.parse_args()
    if a.mode=='prepare':prepare(a.backbone)
    else:decode(a.solution)
