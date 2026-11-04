"""Narrow staging/recheck entry points for the frozen172 evidence package.

No discovery model is imported. No full traversal runs without full-f --run.
"""
import argparse
from collections import Counter
from functools import reduce
import json
from pathlib import Path
if not __debug__: raise RuntimeError("Do not disable assertions with Python -O")
import shutil
import subprocess
import time
from common import load_manifest, ROOT

def read(p):return json.loads(Path(p).read_text())
def write(p,data):Path(p).write_text(json.dumps(data,indent=2)+'\n')
def fresh(p):
    p=Path(p).expanduser().resolve()
    p.mkdir(parents=True,exist_ok=False)
    return p
def words(G):
    cols=[sum(((g>>j)&1)<<i for i,g in enumerate(G)) for j in range(40)]
    return [sum(((u&c).bit_count()%2)<<j for j,c in enumerate(cols)) for u in range(128)]
def permute(w,p):return sum(((w>>i)&1)<<j for i,j in enumerate(p))

def catalogue(args):
    import pynauty
    start=time.process_time();out=fresh(args.output_dir);data=read(args.snapshot)
    keys=set();hulls=Counter();checks=[]
    for r in data['representatives']:
        G=r['generator_rows_40bit_int'];C=words(G)
        assert len(G)==7 and len(set(C))==128
        assert all(0<=g<1<<40 for g in G)
        W=[w.bit_count() for w in C[1:]]
        assert W==r['all127_nonzero_weights'] and min(W)==18 and all(w%2==0 for w in W)
        assert C==r['all128_words']
        assert reduce(int.__or__,G,0)==(1<<40)-1
        H=[w for w in C if all((w&g).bit_count()%2==0 for g in G)]
        h=len(H).bit_length()-1;assert len(H)==1<<h and h==r['hull_dimension'];hulls[h]+=1
        adj={i:[] for i in range(168)}
        for node,w in enumerate(C,40):
            for j in range(40):
                if w>>j&1:adj[node].append(j);adj[j].append(node)
        graph=pynauty.Graph(168,adjacency_dict=adj,
            vertex_coloring=[set(range(40)),set(range(40,168))])
        key=pynauty.certificate(graph);assert key not in keys;keys.add(key)
        checks.append(dict(snapshot172_index=r['snapshot172_index'],rank=7,
            even=True,distance=18,full_support=True,hull_dimension=h))
    assert len(keys)==172 and hulls=={1:33,3:62,5:77}
    result=dict(status='PASS',actual_distinct_codes=172,nonzero_weight_checks=21844,
        all_full_support=True,hull_distribution=dict(hulls),graph_colors='coordinates/all128words only',
        classification_count172_is_external_input=True,source=str(Path(args.snapshot).resolve()),
        CPU_seconds=time.process_time()-start,checks=checks)
    write(out/'catalogue_check.json',result)
    print(json.dumps({k:v for k,v in result.items() if k!='checks'}))

def full_f(args):
    stage=Path(args.output_dir).expanduser().resolve()
    if args.run:
        stage.mkdir(parents=True,exist_ok=False);(stage/'bin').mkdir()
        for name in ('even_scan','literal_gray_replay'):
            command=[args.cxx,'-std=c++17','-O3',str(Path(__file__).parent/(name+'.cpp')),'-o',str(stage/'bin'/name)]
            subprocess.run(command,check=True)
    manifest=load_manifest(args.manifest)
    selected=[r for r in manifest['records'] if args.all or r['case']==args.case]
    assert selected and (args.all or len(selected)==1), 'Unknown or ambiguous case name'
    all_results=[]
    for r in selected:
        name=r['case'];out=stage/'full_f'/name
        inp=read(r['original_scan']['input_path']);gi=read(r['independent_full_F']['input_path'])
        assert inp['rows']==gi['rows'] and inp['pivots']==gi['pivots'] and inp['free']==gi['free']
        C=words(r['actual_generator_rows_40bit_int']);p=r['original_scan']['coordinate_permutation_actual_to_input']
        assert {permute(w,p) for w in C}==set(words(inp['rows']))==set(words(gi['original_rows']))
        jobs=[]
        for impl in ('bitparallel','gray'):
            if args.implementation not in ('both',impl):continue
            d=out/impl
            if impl=='bitparallel':
                text='40 7 16 0\n'+' '.join(map(str,inp['rows']))+'\n'+' '.join(map(str,inp['free']))+'\n'
                command=[stage/'bin/even_scan',d/'input.txt',d/'result.json',d/'F.txt',str(args.cpu_seconds)]
            else:
                text='40 7\n'+'\n'.join(' '.join(map(str,x)) for x in [gi['original_rows'],inp['rows'],inp['pivots'],inp['free']])+'\n'
                command=[stage/'bin/literal_gray_replay',d/'input.txt',d/'result.json',d/'accepted.txt','full',str(args.cpu_seconds),'0']
            jobs.append((impl,d,text,list(map(str,command))))
        if not args.run:
            print(json.dumps(dict(case=name,mode='DRY_RUN_NO_FILES_OR_SCAN',
                expected_F=r['original_scan']['accepted_count'],commands=[j[3] for j in jobs])))
            continue
        original_set={int(s) for s in Path(r['original_scan']['F_path']).read_text().splitlines()}
        for impl,d,text,command in jobs:
            fresh(d);(d/'input.txt').write_text(text);shutil.copyfile(r['original_scan']['input_path'],d/'original_input.json')
            with (d/'stdout.txt').open('w') as stdout,(d/'stderr.txt').open('w') as stderr:
                process=subprocess.run(command,stdout=stdout,stderr=stderr)
            write(d/'process.json',dict(command=command,returncode=process.returncode))
            assert process.returncode==0, 'Incomplete/error run preserved; use a fresh stage to rerun with an adequate CPU budget'
            result=read(d/'result.json')
            if impl=='bitparallel':
                assert not result['sample'] and result['processed_complete']
                assert result['processed_blocks']==1<<27 and result['eligible_representatives']==1<<32
                found=[int(s) for s in (d/'F.txt').read_text().splitlines()]
            else:
                assert result['full_domain_complete'] and result['processed_representatives']==1<<32
                found=[int(s.split()[2]) for s in (d/'accepted.txt').read_text().splitlines()]
            assert len(found)==len(set(found))==result['accepted_count']==len(original_set)
            assert set(found)==original_set
            check=dict(case=name,implementation=impl,status='PASS',full_domain_complete=True,
                F_count=len(found),exact_agreement_with_archived_F=True,result_path=str(d/'result.json'))
            write(d/'comparison.json',check);all_results.append(check);print(json.dumps(check),flush=True)
    if args.run:
        summary=stage/'full_f/SUMMARY.json';assert not summary.exists()
        write(summary,dict(status='PASS',cases=len(selected),implementations=args.implementation,
            runs=all_results,all172_cases=len(selected)==172))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest='action',required=True)
    p=sub.add_parser('catalogue',help='Cheap actual172 rank/parity/distance/support/inequivalence check')
    p.add_argument('--snapshot',default=str(ROOT/'data/actual172_matrices.json'))
    p.add_argument('--output-dir',required=True);p.set_defaults(func=catalogue)
    p=sub.add_parser('full-f',help='Print exact full-scan commands; execute only with explicit --run')
    p.add_argument('--output-dir',required=True)
    p.add_argument('--manifest',default=str(ROOT/'evidence/manifest.json'))
    p.add_argument('--cxx',default='c++')
    select=p.add_mutually_exclusive_group(required=True)
    select.add_argument('--case');select.add_argument('--all',action='store_true')
    p.add_argument('--implementation',choices=['both','bitparallel','gray'],default='both')
    p.add_argument('--cpu-seconds',type=float,required=True)
    p.add_argument('--run',action='store_true');p.set_defaults(func=full_f)
    args=parser.parse_args()
    if hasattr(args,'cpu_seconds') and args.cpu_seconds<=0:parser.error('--cpu-seconds must be positive')
    args.func(args)

if __name__=='__main__':main()
