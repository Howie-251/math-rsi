from pathlib import Path
import sys,runpy,json,time,traceback,contextlib
ROOT=Path('/Users/rfy_naiveai/Desktop/aris4math')
OUT=ROOT/'context/propertyb35-paper/round01/audit-unique-six-two-three-seven-20261020/native'
sys.dont_write_bytecode=True
original_write=Path.write_text
active=''
writes=[]
def redirect(self,data,*args,**kwargs):
    path=self.resolve()
    assert path.is_relative_to(ROOT), str(path)
    target=OUT/(active+'__'+path.name)
    writes.append({'requested':str(path.relative_to(ROOT)),'actual':str(target.relative_to(ROOT))})
    return original_write(target,data,*args,**kwargs)
Path.write_text=redirect
files=[
'middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_FILTER.py',
'middle/a2_a3_min4_cap13_closure_20261020/NO_CRITICAL_CHECK.py',
'middle/three_nonunit_direct_repair_20261020/VERIFY_ASSEMBLY.py',
'middle/four_nonunit_degree_six_center_20261020/VERIFY.py',
'middle/four_nonunit_degree_six_center_20261020/INDEPENDENT_VERIFY.py',
'middle/four_nonunit_degree_six_center_20261020/FIVE_LOCK_FULL5.py',
'middle/generic_c3_fourteen_gate_20261020/VERIFY.py',
'middle/generic_quad_core_multiplicity_three_20261020/FULL_VERIFY.py',
'middle/generic_quad_core_multiplicity_three_20261020/ACTUAL_VERIFY.py',
]
receipts=[]
for i,rel in enumerate(files,1):
    active=f'RUN{i:02d}'
    source=ROOT/'context/propertyb35-paper/round01'/rel
    st=time.monotonic();cpu=time.process_time();record={'id':active,'source':str(source.relative_to(ROOT)),'writes_start':len(writes)}
    with (OUT/(active+'.log')).open('w') as log, contextlib.redirect_stdout(log),contextlib.redirect_stderr(log):
        try:
            runpy.run_path(str(source),run_name='__main__')
            record['status']='PASS'
        except BaseException as e:
            traceback.print_exc();record['status']='FAIL';record['exception']=repr(e)
    record.update(seconds=time.monotonic()-st,cpu_seconds=time.process_time()-cpu,writes=writes[record.pop('writes_start'):])
    receipts.append(record)
    print(record['id'],record['status'],round(record['seconds'],3),rel,flush=True)
Path.write_text=original_write
(OUT/'EXECUTION_RECEIPT.json').write_text(json.dumps(receipts,indent=2)+'\n')
assert all(r['status']=='PASS' for r in receipts)
