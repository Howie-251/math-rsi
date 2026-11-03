"""Separate preparation/self-check and one explicitly invoked search episode."""
from pathlib import Path
import argparse
import json
import os
import resource
import subprocess
import sys
import time

from hs_augmentation import ROOT, dump

BASE=ROOT/"computations/dd82/construction"
OUT=BASE/"full_matching58_anneal_run"
SOURCE=BASE/"full_matching58_anneal.cpp"
BINARY=OUT/"search"
SEED=BASE/"full_matching58_run/seed.edges"
RUN_ID="dd82-v3-f9-c7-20261013-0749"


def execute(command, log, cpu_limit, wall_limit):
    pin=min(os.sched_getaffinity(0))
    def limits():
        os.sched_setaffinity(0,{pin})
        resource.setrlimit(resource.RLIMIT_CPU,(cpu_limit,cpu_limit+1))
        resource.setrlimit(resource.RLIMIT_AS,(4*1024**3,4*1024**3))
    before=resource.getrusage(resource.RUSAGE_CHILDREN);start=time.monotonic()
    with log.open("w") as stream:
        try:
            rc=subprocess.run(command,stdout=stream,stderr=subprocess.STDOUT,
                              preexec_fn=limits,timeout=wall_limit).returncode
        except subprocess.TimeoutExpired:
            rc=None
    after=resource.getrusage(resource.RUSAGE_CHILDREN)
    return dict(command=command,exit_code=rc,
        child_cpu_seconds=after.ru_utime+after.ru_stime-before.ru_utime-before.ru_stime,
        wall_seconds=time.monotonic()-start,pinned_cpu=pin,threads=1,
        cpu_limit_seconds=cpu_limit,wall_limit_seconds=wall_limit)


def prepare():
    OUT.mkdir(exist_ok=True)
    assert not (OUT/"preparation.json").exists(),"Do not repeat unchanged preparation"
    compile_result=execute(["g++","-O3","-std=c++17",str(SOURCE),"-o",str(BINARY)],
                           OUT/"compile.log",20,30)
    assert compile_result["exit_code"]==0
    check=execute([str(BINARY),"selfcheck",str(SEED),str(OUT/"selfcheck.json")],
                  OUT/"selfcheck.log",5,10)
    assert check["exit_code"]==0
    result=dict(parent_run_id=RUN_ID,status="PREPARED_NOT_RUN",optimization_runs=0,
        source=str(SOURCE.relative_to(ROOT)),seed=str(SEED.relative_to(ROOT)),
        random_seed=2026101301,compile=compile_result,selfcheck_process=check,
        selfcheck=json.loads((OUT/"selfcheck.json").read_text()),
        planned_scope="All 21 independent S6 interfaces after seven root matchings are gauged to identity",
        proposed_search_command=[sys.executable,str(Path(__file__).resolve()),"run"],
        proposed_cpu_seconds=120,search_authorized_at_preparation=False,
        target_zero_requires_independent_bfs=True)
    dump(OUT/"preparation.json",result);print(json.dumps(result))


def run():
    assert (OUT/"preparation.json").exists()
    assert not (OUT/"launch.json").exists(),"One search episode only"
    # One CPU second of the 120-second child budget is reserved for final
    # edge/parameter/state files. This does not create another episode.
    command=[str(BINARY),"search",str(SEED),"119",str(OUT)]
    dump(OUT/"launch.json",dict(parent_run_id=RUN_ID,command=command,optimization_runs=1,
         random_seed=2026101301,chain_restarts=0,cpu_limit_seconds=120,
         internal_search_seconds=119,memory_limit_bytes=4*1024**3))
    process=execute(command,OUT/"search.log",120,240)
    result=dict(parent_run_id=RUN_ID,optimization_runs=1,process=process,
                search_report_complete=(OUT/"search.json").exists())
    if result["search_report_complete"]:
        result["search"]=json.loads((OUT/"search.json").read_text())
    if (OUT/"candidate.best.json").exists():
        check=execute([sys.executable,str(BASE/"verify_hs_candidate.py"),str(OUT/"candidate.best.json")],
                      OUT/"independent_bfs.log",5,10)
        assert check["exit_code"]==0
        result["independent_bfs_process"]=check
        bfs=json.loads((OUT/"candidate.best.verification.json").read_text())
        saved=json.loads((OUT/"candidate.best.json").read_text())
        assert bfs["bad_pair_count"]==saved["bad_pairs"]
        result["independent_bfs"]={k:v for k,v in bfs.items() if k not in ("degrees","bad_pairs")}
    dump(OUT/"resources.json",result);print(json.dumps(result),flush=True)


if __name__=="__main__":
    parser=argparse.ArgumentParser();parser.add_argument("action",choices=["prepare","run"])
    args=parser.parse_args()
    {"prepare":prepare,"run":run}[args.action]()
