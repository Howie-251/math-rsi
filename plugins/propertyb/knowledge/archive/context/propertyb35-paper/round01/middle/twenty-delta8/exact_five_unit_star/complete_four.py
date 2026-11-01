"""Complete the190 shared four-neighbor domain, reuse18 fixed pilots; bounded120-order joint only at fixed failures."""
from common import *
start=time.time();rs=json.loads((HERE/'FOUR_DOMAIN.json').read_text())['orbits'];cache={r['id']:r for r in json.loads((HERE/'FOUR_PILOT.json').read_text())['cases']};out=[]
for r in rs:
 if r['id'] in cache:z=cache[r['id']];z['bound']=Q(z['bound'])
 else:en=SubsetEngine(20,5,r['counts']);z=en.verify(en.solve());z.update(r);z['strict']=z['bound']<1
 out.append(z)
(HERE/'FOUR_DP.json').write_text(json.dumps(json_value(dict(scope=__doc__,complete=True,cases=out,pilot_reused=len(cache),elapsed_seconds=time.time()-start)),indent=2)+'\n');print('fixed',sum(z['strict'] for z in out),'of',len(out),'seconds',time.time()-start,flush=True)
js=[];eng=Engine(20,5)
for r in out:
 if r['strict']:continue
 jj=solve_profile(eng,dict(r,counts={t:n for t,n in r['counts'].items() if n},graph='star8four',group=r['id']),permutation_limit=120);jj['source_id']=r['id'];js.append(jj);print('joint',r['id'],jj.get('bound',jj.get('status')),flush=True)
(HERE/'FOUR_JOINT.json').write_text(json.dumps(json_value(dict(scope=__doc__,results=js,elapsed_seconds=time.time()-start)),indent=2)+'\n');strictjs={j['source_id'] for j in js if Q(j.get('bound','2'))<1};res=[r for r in out if not r['strict'] and r['id'] not in strictjs];(HERE/'FOUR_REMAINDERS.json').write_text(json.dumps(json_value(dict(count=len(res),cases=res,elapsed_seconds=time.time()-start)),indent=2)+'\n');print('strictjoint',len(strictjs),'res',len(res),'seconds',time.time()-start)
