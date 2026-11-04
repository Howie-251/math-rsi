"""Floating diagnostics only; does not replace integer certification."""
import argparse, json
import numpy as np
from model import Model, P

ap=argparse.ArgumentParser()
ap.add_argument('--input',required=True)
ap.add_argument('--output',default='candidate_diagnostics.json')
args=ap.parse_args()
M=Model()
x=np.load(P/args.input)['x']
scores=M.evaluate(x)
empty=(M.fi<M.fs[1]).sum(axis=1)
graphs=np.memmap(P/'graphs.bin',dtype=np.uint32,mode='r')
groups=[]
for k in range(25):
    rows=np.flatnonzero(empty==k)
    if not len(rows):
        continue
    i=int(rows[np.argmax(scores[rows])])
    groups.append(dict(empty_faces=k,representatives=len(rows),
                       floating_max=float(scores[i]),worst_mask=int(graphs[i]),
                       edges=round(32*float(M.dd[i]))))
result=dict(source=args.input,scope='all 3312331 Q4 representatives',
            groups=groups,note='Floating diagnostic; group counts are not isomorphism class counts.')
(P/args.output).write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(sorted(groups,key=lambda x:x['floating_max'],reverse=True)[:8],indent=2))
