import sys,time,json,resource,argparse
from pathlib import Path
from itertools import combinations_with_replacement
SRC=Path('context/collaborator-small-k-20261019/m10-m11').resolve()
sys.path.insert(0,str(SRC))
from propertyB_k10_k11_verified import FastExact,CEIL,triple_D,S,C
OUT=Path(__file__).resolve().parent
K=13
KM1=K-1

def domain(m):
    return [v for v in range(2*K-1,K*m+1) if v*CEIL(v-1,KM1)<=K*m and m*(C(v//2,K)+C(v-v//2,K))>=C(v,K)]
def getD(m,v):
    # Search complete feasible D domain, rather than assume d0+50 enough.
    d0=CEIL(v-1,KM1)
    return next((D for D in range(d0,m+1) if (D+1)*v>K*m and 2*KM1*((D+1)*v-K*m)>(KM1*(D+1)-v+2)**2),None)
def parameters(m,v,mode):
    d0=CEIL(v-1,KM1)
    if mode=='none':return [()]
    if mode=='one':return [(d,) for d in range(d0,K*m//v+1)]
    if mode=='two':
        out=[]
        for d in range(d0,K*m//v+1):
            sd=2*(v-1)-KM1*d
            if sd<=0:return None
            B=max(d,(K*m-v*d)//sd+d)
            assert v*d+sd*(B+1-d)>K*m
            assert B==d or v*d+sd*(B-d)<=K*m
            out.extend((d,e) for e in range(d,B+1))
        return out
    D=getD(m,v)
    if D is None:return None
    return [(ds,flag) for ds in combinations_with_replacement(range(d0,D+1),3) for flag in (False,True)]
def evaluate(cal,v,mode,p):
    if mode=='none':return cal.unlocked(v)
    return getattr(cal,mode)(v,*p)
def main():
    ap=argparse.ArgumentParser();ap.add_argument('M',type=int);ap.add_argument('--screen',action='store_true');ap.add_argument('--seconds',type=float,default=430);o=ap.parse_args()
    t=time.monotonic();vs=domain(o.M);res={'k':K,'M':o.M,'S':S,'candidate_v':vs,'rows':[],'failures':[],'complete':False,'int64_checks':'FastExact.table exact m^2 max WH and m max endpoint assertions, every used (v,s)'}
    print('DOMAIN',o.M,min(vs),max(vs),len(vs),flush=True)
    if o.screen:
        # All v, adverse endpoints only; local screening is never a certificate.
        for v in vs:
            cal=FastExact(K,o.M);done=False
            for mode in ['none','one','two','three']:
                params=parameters(o.M,v,mode)
                if params is None:continue
                ps=params[-2:] if mode=='three' else params[-1:]
                worst=max((evaluate(cal,v,mode,p),p) for p in ps)
                if worst[0]<S:
                    res['rows'].append({'v':v,'mode':mode+'-screen','worst_z':worst[0],'profile':worst[1]});done=True;break
            if not done:
                res['uncovered_v']=v;print('SCREEN_UNCOVERED',v,flush=True);break
        res['screen_all_v']=len(res['rows'])==len(vs)
    else:
        for v in vs:
            if time.monotonic()-t>o.seconds:break
            cal=FastExact(K,o.M)
            done=False
            for mode in ['none','one','two','three']:
                params=parameters(o.M,v,mode)
                if params is None:continue
                # First a quick adverse-profile screen; no monotonicity assumed.
                screen=params[-2:] if mode=='three' else params[-1:]
                bad=None
                for p in screen:
                    z=evaluate(cal,v,mode,p)
                    if z>=S:bad={'v':v,'mode':mode,'profile':p,'z':z,'gap':S-z};break
                if bad:
                    res['failures'].append(bad);continue
                worst=(-1,None);count=0
                for p in params:
                    z=evaluate(cal,v,mode,p);count+=1
                    if z>worst[0]:worst=(z,p)
                    if z>=S:bad={'v':v,'mode':mode,'profile':p,'z':z,'gap':S-z};break
                if bad:res['failures'].append(bad);continue
                row={'v':v,'mode':mode,'profiles':count,'worst_z':worst[0],'worst_profile':worst[1],'gap':S-worst[0]}
                if mode=='three':row['D']=getD(o.M,v)
                res['rows'].append(row);done=True;break
            if not done:
                res['uncovered_v']=v;print('UNCOVERED',v,flush=True);break
            if v%10==0 or v==vs[-1]:print('PASS',v,mode,'profiles',sum(r.get('profiles',0) for r in res['rows']),'sec',round(time.monotonic()-t,2),'RSS',resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,flush=True)
        res['complete']=len(res['rows'])==len(vs)
    res['wall_seconds']=time.monotonic()-t;res['cpu_seconds']=time.process_time();res['maxrss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    name=f'M{o.M}'+('-screen' if o.screen else '')+'.json';(OUT/name).write_text(json.dumps(res,indent=2))
    print('DONE',name,res['complete'],'seconds',res['wall_seconds'],flush=True)
if __name__=='__main__':main()
