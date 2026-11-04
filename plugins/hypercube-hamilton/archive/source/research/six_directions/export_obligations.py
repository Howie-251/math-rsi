"""CNF for still-uncovered rooted matchings; SAT does not mean counterexample."""
import json,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/'pilot_results_retry.json').read_text(encoding='utf8'))
n=6;es=[(a,a^(1<<i)) for a in range(1,64) for i in range(n) if not a&(1<<i)]
assert len(es)==186
incident={v:[i+1 for i,e in enumerate(es) if v in e] for v in range(1,64)}
base=[]
for ids in incident.values():
    for j,x in enumerate(ids):
        for y in ids[j+1:]:base.append([-x,-y])
for a,b in es:base.append(sorted(set(incident[a]+incident[b])))
metadata={'edge_variables':{str(i+1):e for i,e in enumerate(es)},'base_clauses':len(base),'branches':{}}
for terminal in (1,7,31):
    clauses=list(base);witnesses=[]
    for c in data['cases']:
        if c['n']!=6 or c['v']!=terminal or c['status']!='FOUND':continue
        path_edges={tuple(sorted(e)) for e in zip(c['path'],c['path'][1:])}
        clauses.append([i+1 for i,e in enumerate(es) if e not in path_edges]);witnesses.append(c['path'])
    filename=f'remaining_v{terminal}.cnf'
    (ROOT/filename).write_text('c Relative maximal matchings in Q6 minus vertex 0; excludes certified paths\n'
        +f'p cnf 186 {len(clauses)}\n'+'\n'.join(' '.join(map(str,c))+' 0' for c in clauses)+'\n',encoding='ascii')
    metadata['branches'][str(terminal)]={'file':filename,'clauses':len(clauses),'covering_paths':witnesses,'solver_status':'NOT_RUN'}
(ROOT/'obligations.json').write_text(json.dumps(metadata,indent=2),encoding='utf8')
print(json.dumps({'variables':186,'base_clauses':len(base),'branches':{v:{k:x for k,x in b.items() if k!='covering_paths'} for v,b in metadata['branches'].items()}}))
