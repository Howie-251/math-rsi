"""Prepare/check, then one separately invoked collision-energy construction run."""
from pathlib import Path
import argparse
import json
import sys

from hs_augmentation import ROOT, dump
from full_matching58_anneal_run import execute

BASE=ROOT/"computations/dd82/construction"
OUT=BASE/"full_matching58_collision_anneal_run"
SOURCE=BASE/"full_matching58_collision_anneal.cpp"
BINARY=OUT/"search"
SEED=BASE/"full_matching58_anneal_run/candidate.best.edges"
SEED_JSON=BASE/"full_matching58_anneal_run/candidate.best.json"
RUN_ID="dd82-v3-f9-c7-20261013-0749"


def prepare():
    OUT.mkdir(exist_ok=True)
    assert not (OUT/"preparation.json").exists(),"One preparation of this changed objective"
    compile_result=execute(["g++","-O3","-std=c++17",str(SOURCE),"-o",str(BINARY)],
                           OUT/"compile.log",20,30)
    assert compile_result["exit_code"]==0
    check=execute([str(BINARY),"selfcheck",str(SEED),str(OUT/"selfcheck.json")],
                  OUT/"selfcheck.log",5,10)
    assert check["exit_code"]==0
    result=dict(parent_run_id=RUN_ID,status="PREPARED_NOT_RUN",optimization_runs=0,
        source=str(SOURCE.relative_to(ROOT)),seed=str(SEED.relative_to(ROOT)),random_seed=2026101302,
        compile=compile_result,selfcheck_process=check,selfcheck=json.loads((OUT/"selfcheck.json").read_text()),
        objective="F=sum_{i<j,a,b} binom(Kij[a,b],2)-168; acceptance uses F alone",
        scope="All 21 free S6 interfaces, root identities only; no fixed HS core or extra K restriction",
        proposed_search_command=[sys.executable,str(Path(__file__).resolve()),"run"],
        proposed_cpu_seconds=60,internal_search_seconds=59,wall_limit_seconds=150,
        launch_waits_for_parent_source_review=True,independent_bfs_deduplicates_identical_best_graphs=True)
    dump(OUT/"preparation.json",result);print(json.dumps(result))


def run():
    assert (OUT/"preparation.json").exists()
    assert not (OUT/"launch.json").exists(),"One collision-energy episode only"
    command=[str(BINARY),"search",str(SEED),"59",str(OUT)]
    dump(OUT/"launch.json",dict(parent_run_id=RUN_ID,command=command,optimization_runs=1,
         random_seed=2026101302,cpu_limit_seconds=60,internal_search_seconds=59,
         wall_limit_seconds=150,chain_restarts=0))
    process=execute(command,OUT/"search.log",60,150)
    result=dict(parent_run_id=RUN_ID,optimization_runs=1,process=process,
                search_report_complete=(OUT/"search.json").exists(),independent_bfs=[])
    if result["search_report_complete"]:
        result["search"]=json.loads((OUT/"search.json").read_text())
    known=[(json.loads(SEED_JSON.read_text())["edges"],
            SEED_JSON.with_suffix(".verification.json"))]
    new_bfs_count=0
    for name in ("candidate.best_energy","candidate.best_bad"):
        path=OUT/(name+".json")
        if not path.exists():continue
        saved=json.loads(path.read_text());edges=saved["edges"]
        matching=[p for es,p in known if es==edges]
        if matching:
            verification=matching[0]
            bfs=json.loads(verification.read_text())
            evidence=dict(candidate=name,process=None,reused_exact_same_edges=True,
                          verification_source=str(verification.relative_to(ROOT)))
        else:
            check=execute([sys.executable,str(BASE/"verify_hs_candidate.py"),str(path)],
                          OUT/(name+".bfs.log"),5,10)
            assert check["exit_code"]==0
            verification=path.with_suffix(".verification.json");bfs=json.loads(verification.read_text())
            evidence=dict(candidate=name,process=check,reused_exact_same_edges=False,
                          verification_source=str(verification.relative_to(ROOT)))
            known.append((edges,verification));new_bfs_count+=1
        assert bfs["bad_pair_count"]==saved["bad_pairs"]
        assert (saved["F"]==0)==bfs["valid_target"]
        if verification!=path.with_suffix(".verification.json"):
            dump(path.with_suffix(".verification.json"),bfs)
        evidence["F"]=saved["F"]
        evidence["graph_check"]={k:v for k,v in bfs.items() if k not in ("degrees","bad_pairs")}
        result["independent_bfs"].append(evidence)
    result["new_independent_bfs_runs"]=new_bfs_count
    dump(OUT/"resources.json",result);print(json.dumps(result),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("action",choices=["prepare","run"])
    args=parser.parse_args();{"prepare":prepare,"run":run}[args.action]()
