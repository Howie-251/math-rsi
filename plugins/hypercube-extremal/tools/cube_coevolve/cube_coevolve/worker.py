"""Internal subprocess entry; imports here are trusted harness code."""
import builtins
import json
from pathlib import Path
import resource
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from cube_coevolve.runtime import ALLOWED_IMPORTS, SearchAPI, vet_source


def limited_import(name, globals=None, locals=None, fromlist=(), level=0):
    if name not in ALLOWED_IMPORTS or level:
        raise ImportError(name)
    return builtins.__import__(name, globals, locals, fromlist, level)


def main():
    source_path, input_path, seconds, memory_mb = sys.argv[1:]
    resource.setrlimit(resource.RLIMIT_CPU, (max(1, int(float(seconds))), max(2, int(float(seconds)) + 1)))
    try:
        resource.setrlimit(resource.RLIMIT_AS, (int(memory_mb) * 1024**2,) * 2)
    except (ValueError, OSError):
        if sys.platform != "darwin":
            raise
    resource.setrlimit(resource.RLIMIT_FSIZE, (4_000_000,) * 2)
    source = Path(source_path).read_text()
    context = json.loads(Path(input_path).read_text())
    tree = vet_source(source)
    names = "abs all any bool dict enumerate filter float frozenset int isinstance len list map max min next range reversed round set sorted str sum tuple zip Exception ValueError TypeError StopIteration".split()
    safe = {name: getattr(builtins, name) for name in names}
    safe["__import__"] = limited_import
    namespace = {"__builtins__": safe, "api": SearchAPI(context)}
    exec(compile(tree, str(source_path), "exec"), namespace)
    result = namespace["generate"](context)
    sys.stdout.write(json.dumps(result, allow_nan=False))


if __name__ == "__main__":
    main()
