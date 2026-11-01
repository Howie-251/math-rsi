"""Produce compact tables and the weakest recorded source key from saved choices."""
import json
from pathlib import Path
from collections import Counter

HERE=Path(__file__).resolve().parent
choices=[json.loads(s) for s in (HERE/'ALL_NINE_CHOICES.jsonl').read_text().splitlines()]
inputs=[json.loads(s) for s in (HERE/'INPUT_GEOMETRY.jsonl').read_text().splitlines()]
out={
 'blue_size':dict(Counter(len(x['blue']) for x in choices)),
 'group_private_counts':dict(Counter(str(tuple(sorted(g['private_edges'] for g in x['groups']))) for x in choices)),
 't_b':dict(Counter(str(tuple(x['signature'][6:8])) for x in choices)),
 'weakest':min(inputs,key=lambda x:(x['best_union'],x['best_6sub_union'],x['input_id'])),
 'star_full_size_max':max(g['private_edges'] for x in choices for g in x['groups']),
}
(HERE/'SUPPLEMENT.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS',len(choices),len(inputs))
