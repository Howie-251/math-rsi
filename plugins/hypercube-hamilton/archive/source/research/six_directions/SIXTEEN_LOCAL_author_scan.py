"""Producer-only nine-selected rescan, redirected to author files; root evidence immutable."""
from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
evidence=['SIXTEEN_LOCAL_profile.py','SIXTEEN_LOCAL_candidate_classes.json','SIXTEEN_LOCAL_coverage.json','SIXTEEN_LOCAL_witnesses.bin','SIXTEEN_LOCAL_all_hit_sets.json']+[f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin' for v in (1,7,31)]
before={n:hashlib.sha256((R/n).read_bytes()).hexdigest() for n in evidence}
code=(R/'SIXTEEN_LOCAL_profile.py').read_text()
line="summary=json.loads((R/'SIXTEEN_NEW_TYPES_summary.json').read_text())"
code=code.replace(line,line+"\nsummary['reports']=[r for r in summary['reports'] if r['index'] in {9,11,1,2,33,7,12,14,15}]")
for a,b in [('SIXTEEN_LOCAL_candidate_classes.json','SIXTEEN_LOCAL_author_scan_classes.json'),('SIXTEEN_LOCAL_remaining_v','SIXTEEN_LOCAL_author_scan_remaining_v'),('SIXTEEN_LOCAL_witnesses.bin','SIXTEEN_LOCAL_author_scan_witnesses.bin'),('SIXTEEN_LOCAL_all_hit_sets.json','SIXTEEN_LOCAL_author_scan_all_hit_sets.json'),('SIXTEEN_LOCAL_coverage.json','SIXTEEN_LOCAL_author_scan_coverage.json')]:code=code.replace(a,b)
exec(compile(code,'<producer nine-selected rescan>','exec'),{'__file__':__file__})
for n,h in before.items():assert hashlib.sha256((R/n).read_bytes()).hexdigest()==h,n
for v in (1,7,31):assert (R/f'SIXTEEN_LOCAL_author_scan_remaining_v{v}_covered.bin').read_bytes()==(R/f'SIXTEEN_LOCAL_remaining_v{v}_covered.bin').read_bytes()
all16=json.loads((R/'SIXTEEN_LOCAL_all_hit_sets.json').read_text());nine=json.loads((R/'SIXTEEN_LOCAL_author_scan_all_hit_sets.json').read_text());assert len(all16)==len(nine)==1012
assert all(a['v']==b['v'] and a['index']==b['index'] and bool(a['local_indices'])==bool(b['local_indices']) for a,b in zip(all16,nine))
out={'status':'PRODUCER_AUTHOR_RESCAN_NOT_INDEPENDENT_ACCEPTANCE','selected_nine_predicate_union_equals_all16_record_by_record':True,'all_three_remaining_bytes_equal_root':True,'source_records':1012,'covered':864,'remaining':148,'root_evidence_unchanged_hashes':before,'full_sixteen_hole_proved':False,'full_P6_proved':False}
(R/'SIXTEEN_LOCAL_author_scan.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
