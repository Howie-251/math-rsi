import json,os,pathlib,resource,subprocess,time
P=pathlib.Path(__file__).resolve().parent; BASE=P.parent
START=time.process_time();WALL=time.monotonic();r0=resource.getrusage(resource.RUSAGE_CHILDREN);C0=r0.ru_utime+r0.ru_stime
pred=json.loads((P/'PREDICTION.json').read_text());assert pred['prototype']==51445
source=BASE/'singlefault_star_probe/continuation/graphs/graph_d13_D5_n51457.edges';native=BASE/'singlefault_star_probe/cover'
pins=pred['mandatory_free_pins']; assert len(pins)==9 and pred['omit_saturated_pin'] not in pins
(P/'mandatory.pins.txt').write_text(' '.join(map(str,pins))+'\n')
assert not (P/'PREPARE_TERMINAL.json').exists(), 'one prepare call already recorded'
with (P/'prepare.log').open('w') as f:
 proc=subprocess.Popen([str(native),'prepare',str(source),str(P/'mandatory.pins.txt'),str(P/'prepared'),'13'],stdout=f,stderr=f)
 (P/'LIVE_HANDLE.json').write_text(json.dumps({'stage':'ONE_PREPARE','pid':proc.pid,'status':'RUNNING','source_n':51457,'mandatory':pins},indent=2)+'\n')
 print(json.dumps({'stage':'ONE_PREPARE','pid':proc.pid}),flush=True)
 try: code=proc.wait(timeout=20)
 except subprocess.TimeoutExpired:proc.kill();code=proc.wait()
r1=resource.getrusage(resource.RUSAGE_CHILDREN); childCPU=r1.ru_utime+r1.ru_stime-C0
term={'stage':'ONE_PREPARE','status':'TERMINAL','pid':proc.pid,'exit_code':code,'child_CPU_seconds':childCPU,'driver_CPU_seconds':time.process_time()-START,'aggregate_CPU_seconds':childCPU+time.process_time()-START,'wall_seconds':time.monotonic()-WALL,'source_allroot_BFS':0,'solver_calls':0}
(P/'PREPARE_TERMINAL.json').write_text(json.dumps(term,indent=2)+'\n');(P/'LIVE_HANDLE.json').write_text(json.dumps(term,indent=2)+'\n');print(json.dumps(term),flush=True)
if code==0:
 r=json.loads((P/'prepared.json').read_text()); print(json.dumps({k:v for k,v in r.items() if k in ['source_n','source_m','status','missing_count','covered_count','eligible_anchors','unique_nonzero_masks','zero_cover_targets','exact_one_or_two_found','exact_two_complete','exact_anchors','CPU_seconds']}),flush=True)
