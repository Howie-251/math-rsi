"""Decode actual Lean literals and compare small physical/independent pin tables.
This script neither reads graph edges nor proves a Lean ASCII parser theorem.
"""
import csv,json,os,re,time
from pathlib import Path
T=time.process_time();D=Path(__file__).resolve().parent
R=next(p for p in D.parents if(p/'formal/DegreeDiameter/Portfolio').is_dir())
S=D.parent;G=S.parent/'even_q8_gq_geometry_pilot'
text=(R/'formal/DegreeDiameter/Portfolio/EvenQ8SourceDefinitions.lean').read_text()
def parse_literal(line):
    tokens=re.findall(r'\(|\)|\.leaf|\.node|[0-9]+',line);at=0
    def expr():
        nonlocal at
        assert tokens[at]=='(';at+=1;tag=tokens[at];at+=1
        if tag=='.leaf':v=int(tokens[at]);at+=1
        else:assert tag=='.node';v=(expr(),expr())
        assert tokens[at]==')';at+=1;return v
    ans=expr();assert at==len(tokens);return ans
def lookup(t,i):
    while isinstance(t,tuple):t=t[i%2];i//=2
    return t
def literal(section,name):
    line=next(x for x in section.splitlines()if x.startswith('def '+name+' : NatTable := '))
    return parse_literal(line.split(':=',1)[1])
results=[]
for case,C,incfile,spreadfile,spreadkey in[
 ('derived','Derived','DERIVED_INCIDENCE.tsv','DERIVED_SPREAD64.tsv','derived_line'),
 ('balanced','Balanced','ORIGINAL_INCIDENCE.tsv','SPREAD65.tsv','original_line')]:
    section=text.split('namespace '+C+'\n',1)[1].split('\nend '+C,1)[0]
    raw=list(map(int,(S/case/'TABLES_INPUT.txt').read_text().split()))
    np,nl,a,b,j,oldn,oldm,n,m,delta=raw[:10];at=10
    physical_lp=[raw[at+i*a:at+(i+1)*a]for i in range(nl)];at+=nl*a
    physical_pl=[raw[at+i*b:at+(i+1)*b]for i in range(np)];at+=np*b
    physical_spread=raw[at:at+j];at+=j;physical_owner=raw[at:at+np]
    lr,pr,sr,orr=[literal(section,x)for x in['lineRows','pointRows','spreadRows','ownerRows']]
    lp=[[(lookup(lr,l)//1024**i)%1024%np for i in range(a)]for l in range(nl)]
    pl=[[(lookup(pr,p)//1024**i)%1024%nl for i in range(b)]for p in range(np)]
    spread=[lookup(sr,h)%nl for h in range(j)];owner=[lookup(orr,p)%j for p in range(np)]
    assert(lp,pl,spread,owner)==(physical_lp,physical_pl,physical_spread,physical_owner)
    fresh_lp=[[]for _ in range(nl)];fresh_pl=[[]for _ in range(np)]
    with(G/incfile).open()as f:
        for row in csv.DictReader(f,delimiter='\t'):
            l,p=int(row['line']),int(row['point']);fresh_lp[l].append(p);fresh_pl[p].append(l)
    assert lp==fresh_lp and pl==fresh_pl
    with(G/spreadfile).open()as f:
        fresh_spread=[int(row[spreadkey])for row in csv.DictReader(f,delimiter='\t')]
    assert spread==fresh_spread
    expected=[]
    for h,l0 in enumerate(spread):
        pins=sorted((p*nl+l,p,l)for p in lp[l0]for l in pl[p])
        for k,(v,p,l)in enumerate(pins):
            assert owner[p]==h
            expected.append((h,oldn+h,l0,k,v,p,l))
    pinpath=S/'independent_acceptance'/case/'ORDERED_HELPER_PIN_BINDING.tsv'
    with pinpath.open()as f:
        actual=[tuple(map(int,row))for row in list(csv.reader(f,delimiter='\t'))[1:]]
    assert actual==expected
    results.append(dict(case=case,LP_entries=nl*a,PL_entries=np*b,spread_entries=j,owner_entries=np,ordered_helper_pin_rows=len(actual),LP_PL_exact_fresh_incidence_order=True,spread_exact_fresh_geometry_order=True,owner_exact_independently_bound_pins=True,labels_old_formula='p*nl+l',labels_new_formula='oldn+helper',actual_source_Definitions_literal_decoded=True))
result=dict(status='PASS_BOTH_ACTUAL_PACKED_TABLE_ENCODINGS_AND_EXTERNAL_PIN_RECIPES',CPU_seconds=time.process_time()-T,cases=results,large_graph_files_read=0,BFS=0,field_or_geometry_rechecks=0,Lean_parser_theorem_claim=False)
p=D/'EXTERNAL_TABLE_BINDING.json';tmp=p.with_suffix('.json.tmp');tmp.write_text(json.dumps(result,indent=2)+'\n');os.replace(tmp,p)
(D/'EXTERNAL_TABLE_BINDING.md').write_text('''# Actual packed-table binding

The standalone small-table decoder read the actual `EvenQ8SourceDefinitions.lean`
NatTable literal trees and reproduced their parity lookup and base-1024 slot
decoding. Both LP and PL sequences equal the fresh physical incidence order;
spread and owner equal the producer input and independent ordered helper-pin
recipe. Every 5120/5265 pin row has the same helper, old point/line label, new
label and slot order as the independently checked complete literal graph.

No large edge file, BFS, field or geometry test was rerun. This is an external
encoding/binding receipt, not a theorem about parsing ASCII graph files in Lean.
See EXTERNAL_TABLE_BINDING.json for actual entry counts and measured CPU.
''')
print(json.dumps(result),flush=True)
