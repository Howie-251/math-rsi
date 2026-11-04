"""Reuse our producer author-check interfaces, never touching frozen source/output files."""
from pathlib import Path
R=Path(__file__).resolve().parent
cert=(R/'FOURTEEN_FORCED_author_check.py').read_text().split('coverage=')[0]
cert=cert.replace('FOURTEEN_FORCED_summary.json','SIXTEEN_LOCAL_CERT_summary.json')
cert+='''\nout={'status':'PRODUCER_AUTHOR_CHECK_NOT_INDEPENDENT_ACCEPTANCE','local_reports':results,'totals':dict(tot),'full_sixteen_hole_proved':False,'full_P6_proved':False}\n(R/'SIXTEEN_LOCAL_author_cert.json').write_text(json.dumps(out,indent=2)+'\\n');print(json.dumps(out,indent=2))\n'''
(R/'SIXTEEN_LOCAL_author_cert.py').write_text(cert)
actual=(R/'FOURTEEN_FORCED_application_author_check.py').read_text()
for a,b in [('FOURTEEN_FORCED_summary.json','SIXTEEN_LOCAL_CERT_summary.json'),('FOURTEEN_HALL_remaining_v','SIXTEEN_POST12_FORCED_remaining_v'),('FOURTEEN_FORCED_witnesses.bin','SIXTEEN_LOCAL_witnesses.bin'),('FOURTEEN_FORCED_remaining_v','SIXTEEN_LOCAL_remaining_v'),('FOURTEEN_FORCED_application_author_check.json','SIXTEEN_LOCAL_author_actual.json'),('full_fourteen_hole_proved','full_sixteen_hole_proved')]:actual=actual.replace(a,b)
actual=actual.replace('13','15').replace('Z,W=rec[:6],rec[6:]','Z,W=rec[:7],rec[7:]').replace('==14','==16').replace('s in (3,4,5)','s in (3,4,6)')
(R/'SIXTEEN_LOCAL_author_actual.py').write_text(actual)
print('Generated producer-only local/actual author checks; no frozen evidence changed.')
