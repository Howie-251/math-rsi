import json
from pathlib import Path
P=Path(__file__).resolve().parent;O=P.parent
old=json.loads((O/'COMPLETE.json').read_text());new=json.loads((P/'COMPLETE.json').read_text())
keys=['M','S','candidate_v','rows','failures','complete']
checks={k:old[k]==new[k] for k in keys}
a=json.loads((O/'SUMMARY.json').read_text());b=json.loads((P/'SUMMARY.json').read_text());ignored=['scalar_replay_cpu_seconds','accepted_driver_cpu_seconds']
summary_checks={k:a[k]==b[k] for k in a if k not in ignored}
assert all(checks.values()) and all(summary_checks.values())
conditional=json.loads((P/'CONDITIONAL.json').read_text());tail=json.loads((P/'TAIL.json').read_text())
assert conditional['rows'][-1]['v']==693 and tail['start_v']==694 and new['complete']
result={'status':'PASS','scope':'Single complete rerun after replacing the original CPU stopping condition by fixed mathematical cut v=693. Original raw files were preserved. Every complete mathematical row and every non-timing summary value agrees exactly.','original_directory':str(O),'rerun_directory':str(P),'fixed_prefix_last_v':693,'fixed_tail_first_v':694,'complete_checks':checks,'summary_checks':summary_checks,'ignored_duration_fields':ignored,'candidate_vertex_count':len(new['candidate_v']),'profile_count':b['total_profiles'],'conditional_cpu_seconds':conditional['cpu_seconds'],'conditional_wall_seconds':conditional['wall_seconds'],'tail_cpu_seconds':tail['cpu_seconds'],'tail_wall_seconds':tail['wall_seconds'],'total_certificate_cpu_seconds':conditional['cpu_seconds']+tail['cpu_seconds'],'scalar_replay_cpu_seconds':b['scalar_replay_cpu_seconds'],'original_files_rewritten':False,'review_independence':'same-family','acceptance_status':'provisional','full_second_probability_implementation':False}
(O/'REPRODUCIBILITY.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
