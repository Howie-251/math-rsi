"""Run the original stdlib-only checker with output writes redirected away from frozen evidence."""
from pathlib import Path
import contextlib,hashlib,io,json,os,runpy,sys,time
R=Path(__file__).resolve().parent
work=R/'verification_runs'/('p6-'+time.strftime('%Y%m%d-%H%M%S'))
work.mkdir(parents=True,exist_ok=True)
checker=R/'research/six_directions/P6_FULL_REVIEW_check.py'
old=Path.write_text
def isolated(self,data,*a,**kw):
 if self.name=='P6_FULL_REVIEW_check.json':return old(work/self.name,data,*a,**kw)
 raise RuntimeError('Unexpected evidence write blocked: '+str(self))
Path.write_text=isolated
sys.argv=[str(checker),'--final'];stream=io.StringIO()
try:
 with contextlib.redirect_stdout(stream):runpy.run_path(str(checker),run_name='__main__')
finally:
 Path.write_text=old
 (work/'stdout.txt').write_text(stream.getvalue(),encoding='utf-8')
 print(stream.getvalue())
report=json.loads((work/'P6_FULL_REVIEW_check.json').read_text(encoding='utf-8'))
summary={k:report[k] for k in ('errors','bound_files_rehashed','transitive_review_nodes','report_dependency_edges','dependency_DAG_acyclic','large_local_certificate_computations_rerun')}
summary['output']=str(work.relative_to(R));summary['original_checker_sha256']=hashlib.sha256(checker.read_bytes()).hexdigest()
(R/'verification_runs/FINAL_REPLAY.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
assert not report['errors'];print('Final assembly replay passed; large local computations were NOT rerun.')
