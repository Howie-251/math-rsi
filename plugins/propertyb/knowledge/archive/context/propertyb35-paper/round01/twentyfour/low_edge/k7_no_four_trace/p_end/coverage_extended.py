from pathlib import Path
from collections import Counter
from itertools import combinations
import json,time
HERE=Path(__file__).parent

def extra(r):
 e=r['edges'];s=r['degrees'];co=Counter(tuple(t) for t in e)
 covers=[list(t) for t in combinations(range(7),2) if all(set(t)&set(z) for z in e)]
 missing={(0,1),(0,2),(3,4),(5,6)}
 E=[t for t in covers if tuple(t) not in missing]
 F=[list(t) for t in combinations(range(1,7),2) if tuple(t) in missing and s[t[0]]==s[t[1]]==3 and co[tuple(t)]==3]
 G=[list(t) for t in combinations(range(1,7),2) if tuple(t) not in missing and sorted((s[t[0]],s[t[1]]))==[2,3] and co[tuple(t)]==2]
 return dict(two_vertex_covers=covers,E_nonmissing_cover=E,F_missing_three_three_shared_three=F,G_three_two_shared_two=G)

def main():
 st=time.time();d=json.loads((HERE/'DOMAIN.json').read_text());cnt=Counter();cells={};survivors={k:[] for k in ('ABCDE','ABCDEF','ABCDEFG')};covertypes=Counter()
 for r in d['orbits']:
  q=extra(r);r.update(q);old=any(r['callers'].values());e=bool(q['E_nonmissing_cover']);f=bool(q['F_missing_three_three_shared_three']);g=bool(q['G_three_two_shared_two']);r['extended_callers']={'E':e,'F':f,'G':g}
  for name,covered in [('ABCDE',old or e),('ABCDEF',old or e or f),('ABCDEFG',old or e or f or g)]:
   cnt[name+'_covered_orbits']+=covered;cnt[name+'_covered_labelled']+=r['labelled_count']*covered
   if not covered:
    survivors[name].append(r);key=(r['num_degree3'],r['num_degree2']);z=cells.setdefault(name,Counter());z[str(key)]+=1
  if not old and not e:
   covertypes['no_two_cover' if not q['two_vertex_covers'] else 'all_two_covers_missing']+=1
 out=dict(complete=True,scope='Same full necessary P multigraph domain; E=nonmissing two-vertex cover; F=missing 3/3 sharing3, using separately supplied strong88 caller; G=nonmissing 3/2 sharing2.',counts=dict(cnt),uncovered_cell_orbit_counts={k:dict(v) for k,v in cells.items()},ABCDE_uncovered_cover_types=dict(covertypes),survivors=survivors,elapsed_seconds=time.time()-st)
 for name,rs in survivors.items():
  p=Counter();l=Counter()
  for r in rs:p[str(r['degree_profile'])]+=1;l[str(r['degree_profile'])]+=r['labelled_count']
  out[name+'_degree_profile_orbits']=dict(p);out[name+'_degree_profile_labelled']=dict(l)
  out[name+'_uncovered_cover_types']=dict(Counter('all_two_covers_missing' if r['two_vertex_covers'] else 'no_two_cover' for r in rs))
 (HERE/'EXTENDED_COVERAGE.json').write_text(json.dumps(out,indent=2)+'\n')
 out['baseline']=json.loads((HERE/'BASELINE_COVERAGE.json').read_text())
 (HERE/'P_GRAPH_CALLER_COVERAGE.json').write_text(json.dumps(out,indent=2)+'\n')
 print({k:v for k,v in out.items() if k not in ('survivors','baseline')})
 for name,rs in survivors.items():
  print(name,'first representatives',[(r['edges'],r['degrees'],r['two_vertex_covers']) for r in rs[:12]])
if __name__=='__main__':main()
