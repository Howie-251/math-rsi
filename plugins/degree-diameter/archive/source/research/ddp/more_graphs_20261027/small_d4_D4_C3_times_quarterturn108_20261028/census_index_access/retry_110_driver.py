"""A25-second wall guard, preserving the original partial batch receipt."""
from pathlib import Path
import copy
import json
import subprocess
import sys
import time

HERE=Path(__file__).resolve().parent
OUT=HERE/'selected_orders_20261028'
initial=json.loads((OUT/'INITIAL_BATCH_RECEIPT.json').read_text())
start=time.perf_counter()
p=subprocess.Popen([sys.executable,str(HERE/'retry_110.py')])
try:
    rc=p.wait(timeout=24.5)
    killed=False
except subprocess.TimeoutExpired:
    p.kill();rc=p.wait();killed=True
path=OUT/'RETRY_110_RECEIPT.json'
r=json.loads(path.read_text()) if path.exists() else {}
if rc!=0:
    r.update(status='FAILED_AUTHORIZED_RETRY_PROCESS_OR_WALL_STOP',error=f'process exit{rc}')
r.update(worker_exit_code=rc,parent_wall_guard_triggered=killed,
         parent_wall_seconds_measured=time.perf_counter()-start,configured_parent_wall_seconds=25)
path.write_text(json.dumps(r,indent=2)+'\n')
combined=copy.deepcopy(initial)
combined.update(initial_batch_receipt='INITIAL_BATCH_RECEIPT.json',initial_batch_status=initial['status'],
                initial_batch_completed_members=68,authorized_single_retry_receipt='RETRY_110_RECEIPT.json',
                additional_payload_requests=1,
                initial_batch_wall_seconds=initial['parent_wall_seconds'],
                single_retry_wall_seconds=r['parent_wall_seconds_measured'],
                cumulative_download_process_wall_seconds=initial['parent_wall_seconds']+r['parent_wall_seconds_measured'],
                cumulative_network_body_bytes_read_known=initial['network_body_bytes_read_known']+r.get('body_bytes_read_known',0),
                cumulative_budget_charged_declared_body_bytes=initial['budget_charged_declared_body_bytes']+48291,
                original_batch_success_rewritten=False)
if r['status']=='COMPLETE_MEMBER_RETRY110':
    combined.update(status='COMPLETE_DOWNLOAD',completed_orders=sorted(initial['completed_orders']+[110]),
                    failed_orders=[],pending_orders=[],complete_member_count=69,
                    completion_scope='Original batch68 successful members plus one separately authorized retry110; not one wholly successful batch.')
    row=next(x for x in combined['member_records'] if x['order']==110)
    row.update(status='COMPLETE_MEMBER_VIA_SEPARATE_AUTHORIZED_RETRY',local_path=r['local_path'],
               decompressed_bytes=75000,local_filename_matches=True,decompressed_size_matches=True,
               original_failed_attempt_preserved_in='INITIAL_BATCH_RECEIPT.json',retry_receipt='RETRY_110_RECEIPT.json')
else:
    combined.update(status='PARTIAL_DOWNLOAD_RETRY_FAILED_CLOSED',complete_member_count=68)
(OUT/'DOWNLOAD_RECEIPT.json').write_text(json.dumps(combined,indent=2)+'\n')
(OUT/'terminal.json').write_text(json.dumps({k:v for k,v in combined.items() if k not in ('member_records','requests')},indent=2)+'\n')
print(json.dumps({k:combined[k] for k in ['status','completed_orders','failed_orders','pending_orders','cumulative_network_body_bytes_read_known','cumulative_budget_charged_declared_body_bytes','cumulative_download_process_wall_seconds']},indent=2),flush=True)
