"""Reuse the existing exporter on the saved complete four-low certificate set.
No search is repeated. Generated modules still require Lean kernel checking.
"""
from pathlib import Path
import importlib.util
import json
from fractions import Fraction as F

ROOT = Path(__file__).resolve().parents[4]
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('four_export', ROOT / 'context/propertyb34/round01/middle-lean/generate_few_low_four.py')
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
raw = json.loads((ROOT / 'context/propertyb34/round01/middle-math/FOUR_LOW_23.json').read_text())
pure = [r for r in raw['results'] if F(r['bound']) < 1]
joint = [r for r in raw['results'] if F(r['bound']) >= 1 and F(r['joint']['bound']) < 1]
residual = [r['group'] for r in raw['results'] if F(r['bound']) >= 1 and F(r['joint']['bound']) >= 1]
data = mod.export_pure('TwentyThreeFourLowStrict', pure, [6]*4)
summary = dict(source='FOUR_LOW_23.json', pure=[r['group'] for r in pure], joint=[], residual=residual,
               numeric_status='exported, not Lean checked')
for row in joint:
    summary['joint'].append(mod.export_joint(f'TwentyThreeFourLowJoint{row["group"]}', row, [6]*4))
(HERE/'FOUR_LOW_CERTIFICATE_EXPORT.json').write_text(json.dumps(summary,indent=2)+'\n')
(HERE/'FOUR_LOW_PURE_REPLAY.json').write_text(json.dumps(mod.json_value(data),indent=2)+'\n')
print(json.dumps(summary,indent=2))
