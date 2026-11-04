"""Read relocated metadata; pair streams are deliberately irrelevant to saved-set checks."""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1] / 'archive/source'
def load_manifest(path):
    m=json.loads(Path(path).read_text())
    def resolve(value):
        p=(ROOT/value).resolve()
        if not p.is_relative_to(ROOT.resolve()) or not p.is_file():
            raise ValueError(f'Missing or escaping input: {value}')
        return str(p)
    m['actual_matrix_snapshot']=resolve(m['actual_matrix_snapshot'])
    for rec in m['records']:
        for part in ('original_scan','independent_full_F'):
            for key,value in rec[part].items():
                if key.endswith('_path'):rec[part][key]=resolve(value)
    return m
