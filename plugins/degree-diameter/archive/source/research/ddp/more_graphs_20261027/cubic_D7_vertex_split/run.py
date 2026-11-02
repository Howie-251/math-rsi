import json
import pathlib
import resource
import subprocess
import time

HERE = pathlib.Path(__file__).resolve().parent
start = time.process_time()
children0 = resource.getrusage(resource.RUSAGE_CHILDREN)
subprocess.run(["g++", "-O3", "-std=c++17", str(HERE / "probe.cpp"),
                "-o", str(HERE / "probe")], check=True)
compiled = resource.getrusage(resource.RUSAGE_CHILDREN)
subprocess.run([str(HERE / "probe"), str(HERE / "source200.edges"), str(HERE)], check=True)
native = json.loads((HERE / "NATIVE_RESULT.json").read_text())
children1 = resource.getrusage(resource.RUSAGE_CHILDREN)
native["compile_CPU_seconds"] = (compiled.ru_utime + compiled.ru_stime
                                - children0.ru_utime - children0.ru_stime)
native["total_CPU_seconds"] = (time.process_time() - start + children1.ru_utime
                              + children1.ru_stime - children0.ru_utime - children0.ru_stime)
native["status"] = ("FIRST_COMPLETE_CANDIDATE" if native["hit_ordinal"] >= 0 else
                    "FIXED_SOURCE_OPERATION_COMPLETE_NO_HIT" if native["unattempted"] == 0 else
                    "PARTIAL_NO_HIT")
native["prediction"] = "SUPPORTED" if native["hit_ordinal"] >= 0 else (
    "REFUTED" if native["unattempted"] == 0 else "UNRESOLVED")
native["actual_n"] = 201 if native["hit_ordinal"] >= 0 else None
native["actual_D"] = None
native["ordinary_bad_unordered_pairs"] = None
native["hypothetical_n"] = 201
native["pending"] = []
(HERE / "RESULT.json").write_text(json.dumps(native, indent=2) + "\n")
(HERE / "terminal.json").write_text(json.dumps({
    "status": native["status"], "pending": [],
    "unattempted": native["unattempted"], "new_graphs": int(native["hit_ordinal"] >= 0),
    "scope": "This source and the 600 labelled adjacent 1+2 vertex splits only."
}, indent=2) + "\n")
print(json.dumps(native, indent=2))
