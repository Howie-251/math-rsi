"""Rebuild the complete40-type34/min10 certificate; no layout search."""
from maxr import *
if __name__=='__main__':
 start=time.process_time();source=json.loads((P.parent/'root/NONUNIT_LOW_PROBE.json').read_text());repairs={r['tau']:r for r in json.loads((P/'MAXR.json').read_text())['rows']};rows=[]
 for row in source['rows']:
  if not row['strict']:row=repairs[row['tau']]|dict(deduction='component_max_R')
  else:row=row|dict(deduction='component_full_pool')
  ell={int(T):n for T,n in row['ell'].items()};c.bad_pair_deletion=deletion if row['deduction']=='component_max_R'else d.strengthened
  u=c.profile_bound(34,tuple(row['pos']),ell);assert u==F(row['U'])<1
  rows.append(row)
 c.bad_pair_deletion=d.strengthened
 ell={0:46,1:9,2:10,3:1};u=c.profile_bound(34,(16,17),ell);assert u<1
 rows.append(dict(v=34,ds=[10,11],lam=1,ell=ell,U=str(u),pos=[16,17],strict=True,deduction='component_full_pool'))
 assert len(rows)==40
 out=dict(status='complete minimumdegree10 candidate',v=34,M=66,rows=rows,profiles=len(rows),maximum=str(max(F(r['U'])for r in rows)),cpu_seconds=time.process_time()-start,independent_status='pending')
 (P/'CERTIFICATE.json').write_text(json.dumps(out,indent=2));print(json.dumps({k:v for k,v in out.items()if k!='rows'},indent=2))
