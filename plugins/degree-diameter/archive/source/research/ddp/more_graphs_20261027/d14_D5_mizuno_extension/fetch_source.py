"""Download the exact official current94186 source once; no graph verification."""
from pathlib import Path
from datetime import datetime, timezone
import json
import time
import urllib.request

P = Path(__file__).resolve().parent
url = 'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD5/N14_D5_94186_FINAL.edges'
assert not (P / 'source94186.edges').exists()
start = time.monotonic()
with urllib.request.urlopen(url, timeout=120) as response:
    raw = response.read()
    receipt = {'requested_url': url, 'returned_url': response.geturl(), 'status': response.status,
               'bytes': len(raw), 'checked_UTC': datetime.now(timezone.utc).isoformat(),
               'wall_seconds': time.monotonic() - start}
(P / 'source94186.edges').write_bytes(raw)
(P / 'SOURCE.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps(receipt))
print(raw[:1800].decode(errors='replace'))
