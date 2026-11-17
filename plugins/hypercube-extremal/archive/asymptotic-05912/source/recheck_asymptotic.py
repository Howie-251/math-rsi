from pathlib import Path
import os, runpy

base = Path(__file__).resolve().parent
script_path = base / "asymptotic_05912_flag_algebra" / "verify_05912.py"
runpy.run_path(str(script_path), run_name="__main__")
