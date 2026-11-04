"""Prepare literal inputs from final manifest, then run one standalone verifier."""
import argparse
from collections import Counter
import json
from pathlib import Path
if not __debug__: raise RuntimeError("Do not disable assertions with Python -O")
import resource
import subprocess
import time
import math
from common import load_manifest

HERE=Path(__file__).resolve().parent
parser=argparse.ArgumentParser()
parser.add_argument('--manifest',type=Path,default=HERE.parent/'evidence/manifest.json')
parser.add_argument('--output-dir',type=Path,default=HERE/'run_output')
parser.add_argument('--prepare-only',action='store_true')
parser.add_argument('--cpu-seconds',type=float,default=600)
parser.add_argument('--wall-seconds',type=float,default=900)
parser.add_argument('--cxx',default='c++')
args=parser.parse_args()
assert args.cpu_seconds>0 and args.wall_seconds>0
start=time.process_time();out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=False)
assert not (out/'native_result.json').exists(), 'Use a fresh output directory; do not overwrite prior replay'
manifest=load_manifest(args.manifest)
snapshot=json.loads(Path(manifest['actual_matrix_snapshot']).read_text())
actual={r['snapshot172_index']:r for r in snapshot['representatives']}
records=manifest['records'];assert len(records)==172 and sorted(r['snapshot172_index'] for r in records)==list(range(172))
assert manifest['total_F_count']==429024 and manifest['total_unordered_pair_count']==619053789
lines=['LITERAL_PAIR_REPLAY_V1','172 429024 619053789'];bindings=[];formats=Counter()
for rec in sorted(records,key=lambda r:r['snapshot172_index']):
    ident=rec['snapshot172_index'];original=rec['original_scan'];pair=rec['pair_graph']
    inp=json.loads(Path(original['input_path']).read_text());result=json.loads(Path(original['result_path']).read_text())
    assert rec['actual_generator_rows_40bit_int']==actual[ident]['generator_rows_40bit_int']
    assert original['scan_rows']==inp['rows']==result['rows'] and inp['free']==result['free']
    assert len(inp['rows'])==7 and len(inp['free'])==33 and len(inp['pivots'])==7
    assert original['accepted_count']==original['saved_count']==result['accepted_count']==result['saved_count']
    count=result['accepted_count'];assert pair['pair_count']==count*(count-1)//2
    assert pair['compatible_edges']==pair['compatible_triangles']==pair['targets']==0
    fmt=1 if pair['rejection_witness_format'].startswith('TSV') else 0
    assert fmt or pair['rejection_witness_format']=='uint8 base-message per lexicographic pair'
    formats['TSV' if fmt else 'uint8']+=1
    lines += [f"{ident} {count} {pair['pair_count']} {fmt}",rec['case'],
              ' '.join(map(str,rec['actual_generator_rows_40bit_int'])),
              ' '.join(map(str,inp['rows'])),' '.join(map(str,inp['free'])),' '.join(map(str,inp['pivots'])),
              ' '.join(map(str,original['coordinate_permutation_actual_to_input'])),
              original['F_path'],pair['rejection_witness_path']]
    bindings.append(dict(snapshot172_index=ident,case=rec['case'],actual_rows=rec['actual_generator_rows_40bit_int'],
                         input_path=original['input_path'],F_path=original['F_path'],witness_path=pair['rejection_witness_path'],
                         witness_format='TSV' if fmt else 'uint8',expected_F=count,expected_pairs=pair['pair_count'],
                         coordinate_permutation_actual_to_input=original['coordinate_permutation_actual_to_input']))
assert formats=={'TSV':23,'uint8':149}
lines.append('END');(out/'literal_cases.txt').write_text('\n'.join(lines)+'\n')
preparation=dict(manifest=str(args.manifest.resolve()),actual_snapshot=manifest['actual_matrix_snapshot'],
                 cases=bindings,formats=dict(formats),preparation_CPU_seconds=time.process_time()-start,
                 pair_replay_performed=False)
(out/'PREPARATION.json').write_text(json.dumps(preparation,indent=2)+'\n')
if args.prepare_only:
    print(json.dumps(dict(status='PREPARED_ONLY',cases=172,pair_replay_performed=False,plan=str(out/'literal_cases.txt'))));raise SystemExit
binary=out/'replay_certificates'
build_cmd=[args.cxx,'-std=c++17','-O3',str(HERE/'replay_certificates.cpp'),'-o',str(binary)]
build=subprocess.run(build_cmd,capture_output=True,text=True);assert build.returncode==0,build.stderr
(out/'BUILD.json').write_text(json.dumps(dict(command=build_cmd,returncode=build.returncode,stdout=build.stdout,stderr=build.stderr),indent=2)+'\n')
command=[str(binary),str(out/'literal_cases.txt'),str(out/'case_results.jsonl'),str(out/'native_result.json'),str(args.cpu_seconds)]
def hard_limit():resource.setrlimit(resource.RLIMIT_CPU,(math.ceil(args.cpu_seconds)+3,math.ceil(args.cpu_seconds)+3))
before=resource.getrusage(resource.RUSAGE_CHILDREN);wall=time.monotonic()
p=subprocess.run(command,capture_output=True,text=True,preexec_fn=hard_limit,timeout=args.wall_seconds)
after=resource.getrusage(resource.RUSAGE_CHILDREN)
child_CPU=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime
process=dict(command=command,returncode=p.returncode,stdout=p.stdout,stderr=p.stderr,wall_seconds=time.monotonic()-wall,
             child_CPU_seconds=child_CPU,hard_native_CPU_limit=math.ceil(args.cpu_seconds)+3,build_excluded=True,
             preparation_plus_native_CPU=preparation['preparation_CPU_seconds']+child_CPU)
(out/'PROCESS.json').write_text(json.dumps(process,indent=2)+'\n')
assert p.returncode==0,p.stderr
result=json.loads((out/'native_result.json').read_text())
assert result['status']=='PASS' and result['cases_completed']==172
assert result['F_count']==429024 and result['pairs_replayed']==619053789
assert result['all_F_actual_distances_checked']==429024*128 and result['all_streams_exact_EOF']
# Time budgets are operational limits, not mathematical acceptance conditions.
print(json.dumps(dict(result=result,process=process),indent=2))
