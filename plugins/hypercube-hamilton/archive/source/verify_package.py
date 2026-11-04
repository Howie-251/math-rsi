"""Offline integrity validation; no third-party dependencies."""
from pathlib import Path
import hashlib,json,sys
R=Path(__file__).resolve().parent
manifest=json.loads((R/'PACKAGE_MANIFEST.json').read_text(encoding='utf-8'))
errors=[];total=0
for i,e in enumerate(manifest['files']):
 p=R/e['path']
 if not p.is_file():errors.append([e['path'],'missing']);continue
 if p.stat().st_size!=e['bytes']:errors.append([e['path'],'size']);continue
 h=hashlib.sha256()
 with p.open('rb') as f:
  for chunk in iter(lambda:f.read(8*1024*1024),b''):h.update(chunk)
 if h.hexdigest()!=e['sha256']:errors.append([e['path'],'sha256'])
 total+=p.stat().st_size
 if (i+1)%1000==0:print('Checked',i+1,flush=True)
out={'scope':'all manifest-bound files; not a mathematical proof check','files_checked':len(manifest['files']),'bytes_checked':total,'errors':errors,'pass':not errors}
(R/'verification_runs').mkdir(exist_ok=True)
(R/'verification_runs/integrity.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2));sys.exit(bool(errors))
