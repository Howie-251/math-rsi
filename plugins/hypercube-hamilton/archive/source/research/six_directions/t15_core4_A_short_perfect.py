import json
from pathlib import Path
p=Path(__file__).parent
def shortpairs(v):
 if not v:yield ();return
 a=min(v)
 for j in range(4):
  b=a^(1<<j)
  if b in v:
   for q in shortpairs(v-{a,b}):yield ((a,b),)+q
x=list(shortpairs(set(range(16))))
assert len(x)==272
(p/'t15_core4_A_short_perfect.json').write_text(json.dumps(x))
print(len(x))
