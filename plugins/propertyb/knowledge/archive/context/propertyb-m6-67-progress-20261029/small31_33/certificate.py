"""M=66 complete31/32 certificate and exact partial33 obligations."""
from diagnose import *
from avoided import triple
OUT=Path(__file__).resolve().parent

def save_case(rows,label,v,ell,menu):
 best=min((c.profile_bound(v,tuple(p),ell),tuple(p)) for p in menu)
 row=dict(branch=label,v=v,ell=ell,positions=best[1],U=str(best[0]),strict=best[0]<1)
 rows.append(row);return row

def main():
 start=time.process_time();rows=[]
 # Complete v31: min6..11, then two12 whose codegree<=6.
 for d in range(6,12):save_case(rows,'v31_min6_11',31,{0:66-d,1:d},[(15,)])
 for l in range(1,7):save_case(rows,'v31_min12',31,two(31,12,12,l),[(15,16),(14,16),(10,18)])
 # Complete v32 min7..11: actual minimum and unitpartner degreebudget.
 for d in range(7,12):
  n=62-5*d;upper=d+(396-32*d)//n
  for e in range(d,upper+1):save_case(rows,'v32_min7_11',32,two(32,d,e),[(16,17),(15,10),(10,11),(15,17),(15,16)])
 # Complete v32 min12 three-way actualselection.
 for e in [12,*range(14,25)]:save_case(rows,'v32_min12_pair',32,two(32,12,e),[(16,17),(15,10),(10,11)])
 for l in (1,2):
  for t in (0,1):save_case(rows,'v32_min12_wedge',32,triple((13,12,12),l,t),[(11,12,13),(15,16,17),(12,13,14)])
 # v33 main actualminimum/unitpartner, except exactly e14 atdelta9..11.
 for d in range(7,13):
  n=64-5*d;upper=d+(396-33*d)//n
  for e in range(d,upper+1):
   if d in(9,10,11) and e==14:continue
   save_case(rows,'v33_adaptive_pass',33,two(33,d,e),[(16,17),(16,10),(10,11),(15,16),(15,17)])
 # Delta9,e14 is replaced by actual degree9 partner of codegree2.
 save_case(rows,'v33_delta9_special',33,two(33,9,9,2),[(16,18)])
 # For delta10/11 lastdegree14 partners, pick twoactualdegree14unitneighbors.
 for d in (10,11):
  for l in range(1,15):
   for t in (0,1):
    if 13-l+t<0:continue
    save_case(rows,f'v33_delta{d}_two14',33,triple((d,14,14),l,t),[(19,20,21),(11,12,13),(15,16,19),(11,12,19),(14,15,19),(16,17,18),(11,13,20),(10,11,19)])
 quota_table=[dict(support=N,f=f,q=quota(N+1,f)) for N in range(28,33) for f in range(0,25)]
 result=dict(M=66,complete_vertex_branches=[31,32,33],partial33=False,rows=rows,failures=[r for r in rows if not r['strict']],quotas=quota_table,cpu_seconds=time.process_time()-start)
 (OUT/'CERTIFICATE.json').write_text(json.dumps(result,indent=2))
 print(json.dumps({k:v for k,v in result.items() if k not in('rows','quotas')},indent=2))
if __name__=='__main__':main()
