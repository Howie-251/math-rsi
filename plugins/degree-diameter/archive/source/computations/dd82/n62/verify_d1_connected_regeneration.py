"""Regenerate actual saved CNFs from the inspected sources; compare bytes, no hashes."""
from pathlib import Path
import importlib.util,json,os,sys,tempfile,time
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"computations/dd82/n62/d1_connected_diagnostic"
os.sched_setaffinity(0,{min(os.sched_getaffinity(0))})
def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    mod=importlib.util.module_from_spec(spec);sys.modules[name]=mod;spec.loader.exec_module(mod);return mod
def equal(a,b):
    n=0
    with a.open("rb") as f,b.open("rb") as g:
        while True:
            x=f.read(1024*1024);y=g.read(1024*1024)
            assert x==y,(str(a),str(b),n)
            n+=len(x)
            if not x:return n
start=time.monotonic()
reports=[]
with tempfile.TemporaryDirectory(prefix=".dd82-cnf-regeneration-",dir=ROOT) as td:
    temp=Path(td)
    old=load("dd82_old_reproduction",ROOT/"computations/dd82/n62/d1_hard_diagnostic.py")
    old.OUT=temp/"old"
    sys.argv=["d1_hard_diagnostic.py","--prepare-only"]
    old.main()
    new=load("dd82_new_reproduction",ROOT/"computations/dd82/n62/d1_connected_diagnostic.py")
    new.OLD=old.OUT;new.OUT=temp/"new"
    new.prepare()
    savedold=ROOT/"computations/dd82/n62/d1_hard_diagnostic"
    for rel in ["cnf/D1_MATCH.cnf","D1_HARD_b_28.cnf","D1_HARD_b_41.cnf"]:
        reports.append({"layer":"base_or_canonical","saved":str((savedold/rel).relative_to(ROOT)),"bytes":equal(old.OUT/rel,savedold/rel),"exact_byte_agreement":True})
    for case in ["D1_HARD_b_28","D1_HARD_b_41"]:
        for suffix in [".cnf",".added.cnf"]:
            rel=case+suffix
            reports.append({"layer":"connected","saved":str((OUT/rel).relative_to(ROOT)),"bytes":equal(new.OUT/rel,OUT/rel),"exact_byte_agreement":True})
    assert json.loads((old.OUT/"maps/D1_MATCH.map.json").read_text())==json.loads((savedold/"maps/D1_MATCH.map.json").read_text())
report={"status":"EXACT_SOURCE_REGENERATION_MATCH","seconds":time.monotonic()-start,"pinned_cpu":next(iter(os.sched_getaffinity(0))),"solver_runs":0,"checker_runs":0,"hashes_generated":False,"method":"Regenerated full base and canonical formulas via old driver prepare-only and full connected formulas via new prepare; compared all bytes including DIMACS headers, clause order and added clause files. Temporary outputs removed.","full_variable_map_equal":True,"files":reports}
(OUT/"regeneration_verification.json").write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps(report),flush=True)
