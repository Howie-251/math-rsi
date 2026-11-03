"""Run the sole predetermined native profile; stream raw passers immediately."""

import json
from pathlib import Path
import resource
import subprocess
import time


HERE = Path(__file__).resolve().parent


def limit_search():
    resource.setrlimit(resource.RLIMIT_CPU, (87, 87))


def main():
    wall, cpu = time.monotonic(), time.process_time()
    before = resource.getrusage(resource.RUSAGE_CHILDREN)
    with (HERE / "production.log").open("w") as log:
        process = subprocess.Popen([str(HERE / "search"), str(HERE)],
                                   stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   text=True, bufsize=1, preexec_fn=limit_search)
        for line in process.stdout:
            log.write(line)
            log.flush()
            print(line, end="", flush=True)
        returncode = process.wait()
    after = resource.getrusage(resource.RUSAGE_CHILDREN)
    terminal_path = HERE / "terminal.json"
    terminal = json.loads(terminal_path.read_text()) if terminal_path.exists() else {
        "status": "SEARCH_PROCESS_TERMINATED_PARTIAL_UNKNOWN"}
    compilation = json.loads((HERE / "compile.json").read_text())
    terminal.update({
        "process_returncode": returncode,
        "child_process_CPU_seconds": after.ru_utime + after.ru_stime - before.ru_utime - before.ru_stime,
        "compile_CPU_seconds": compilation["CPU_seconds"],
        "driver_CPU_seconds": time.process_time() - cpu,
        "total_CPU_seconds_including_compile": after.ru_utime + after.ru_stime - before.ru_utime
            - before.ru_stime + compilation["CPU_seconds"] + time.process_time() - cpu,
        "wall_seconds_this_driver": time.monotonic() - wall,
        "restarts": 0, "architecture_variants": 1,
        "source_local_rule": "wave4/mizuno_d3_source/q3_local_patterns.json; all18 two-matchings",
        "best_graph": "best.json", "pending": [],
    })
    terminal_path.write_text(json.dumps(terminal, indent=2) + "\n")
    print(json.dumps(terminal, indent=2), flush=True)


if __name__ == "__main__":
    main()
