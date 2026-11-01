from pathlib import Path
import subprocess, sys, json
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).parent
for i in range(2,33):
    subprocess.run([sys.executable,str(HERE/'generate_four_eight_single_cached.py'),'77778',str(i),'16'],check=True)
    name=f'TwentyOneSevenFive77778Batch{i:03d}'
    template=(HERE/'CACHED_SINGLE_NUMERIC_TEMPLATE.txt').read_text().replace('TwentyOneSevenFive77778Batch001',name)
    (ROOT/'formal/Aris4Math/ThirtyFour'/(name+'Numeric.lean')).write_text(template)
