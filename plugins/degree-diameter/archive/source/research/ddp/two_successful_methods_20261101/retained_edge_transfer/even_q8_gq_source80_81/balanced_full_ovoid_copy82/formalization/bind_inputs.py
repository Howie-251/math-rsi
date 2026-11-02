import csv,json,os,re,time
from pathlib import Path
T=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir());S=D.parent;G=S.parent.parent/'even_q8_gq_geometry_pilot'
code=(R/'formal/DegreeDiameter/Portfolio/EvenQ8BalancedFullOvoidCopy82Definitions.lean').read_text()
def table(name):
    line=next(x for x in code.splitlines()if x.startswith('def '+name+' : NatTable := '))
    ts=re.findall(r'\(|\)|\.leaf|\.node|[0-9]+',line.split(':=',1)[1]);at=0
    def parse():
        nonlocal at
        assert ts[at]=='(';at+=1;tag=ts[at];at+=1
        if tag=='.leaf':ans=int(ts[at]);at+=1
        else:assert tag=='.node';ans=(parse(),parse())
        assert ts[at]==')';at+=1;return ans
    return parse()
def get(t,i):
    while isinstance(t,tuple):t=t[i%2];i//=2
    return t
o,owner,lo=map(table,['ovoidRows','ovoidOwnerRows','lineOvoidRows'])
O=[get(o,i)%585 for i in range(65)];owners=[get(owner,p)for p in range(585)];lines=[get(lo,l)%65 for l in range(585)]
with(G/'OVOID65.tsv').open()as f:fresh=list(csv.DictReader(f,delimiter='\t'))
assert O==[int(row['point'])for row in fresh]
expected=[65]*585
for i,p in enumerate(O):expected[p]=i
assert owners==expected
with(G/'OVOID65_LINE_INTERSECTIONS.csv').open()as f:
    intersections=list(csv.DictReader(f))
assert lines==[owners[int(row['ovoid_point'])]for row in intersections]
raw=list(map(int,(S.parent/'balanced/TABLES_INPUT.txt').read_text().split()));np,nl,a,b,j=raw[:5];at=10+nl*a+np*b;spread=raw[at:at+j]
inherited=json.loads((S.parent/'formalization_full/EXTERNAL_TABLE_BINDING.json').read_text());assert inherited['status'].startswith('PASS_')
receipt=json.loads((S/'independent_acceptance/RESULT.json').read_text());assert receipt['status'].startswith('PASS_')and receipt['all4225_source_N81_lists_bound']
path=S/'independent_acceptance/ORDERED_SOURCE_N81_BINDING.tsv';count=0
with path.open()as f:
    for row in csv.DictReader(f,delimiter='\t'):
        h=int(row['h']);i,k=divmod(h,65)
        assert h==count and i==int(row['ovoid_index'])and k==int(row['spread_index'])
        assert int(row['center_oldlabel'])==585*O[i]+spread[k]
        assert int(row['newlabel'])==342290+h
        count+=1
assert count==4225
result=dict(status='PASS_ACTUAL_TYPED_OVOID_OWNER_TABLES_AND_ALL4225_ORDERED_CENTER_LABELS',CPU_seconds=time.process_time()-T,actual_ovoid_ids=O,ovoid_owner_entries=585,line_owner_entries=585,ordered_center_rows=count,source_packed_table_binding_inherited=True,full_N81_literal_binding_inherited_from_fresh_receipt=True,new_pin_list_revalidation=False,large_graph_reads=0,BFS=0,field_projection_geometry_rechecks=0,Lean_ASCII_parser_theorem_claimed=False)
p=D/'EXTERNAL_INPUT_BINDING.json';tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,p)
print(json.dumps(result),flush=True)
