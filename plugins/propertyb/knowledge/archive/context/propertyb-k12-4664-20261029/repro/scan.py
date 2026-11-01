import sys,time,json,resource,argparse
from pathlib import Path
from itertools import combinations_with_replacement
SRC=Path('context/collaborator-small-k-20261019/m10-m11').resolve()
sys.path.insert(0,str(SRC))
from propertyB_k10_k11_verified import FastExact,CEIL,triple_D,S,C
OUT=Path(__file__).resolve().parent

def domain(m):
    return [v for v in range(23,12*m+1) if v*CEIL(v-1,11)<=12*m and m*(C(v//2,12)+C(v-v//2,12))>=C(v,12)]
def getD(m,v):
    # Search complete feasible D domain, rather than assume d0+50 enough.
    d0=CEIL(v-1,11)
    return next((D for D in range(d0,m+1) if (D+1)*v>12*m and 22*((D+1)*v-12*m)>(11*(D+1)-v+2)**2),None)
def parameters(m,v,mode):
    d0=CEIL(v-1,11)
    if mode=='none':return [()]
    if mode=='one':return [(d,) for d in range(d0,12*m//v+1)]
    if mode=='two':
        out=[]
        for d in range(d0,12*m//v+1):
            sd=2*(v-1)-11*d
            if sd<=0:return None
            B=max(d,(12*m-v*d)//sd+d)
            assert v*d+sd*(B+1-d)>12*m
            assert B==d or v*d+sd*(B-d)<=12*m
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
    t=time.monotonic();vs=domain(o.M);res={'M':o.M,'S':S,'candidate_v':vs,'rows':[],'failures':[],'complete':False,'int64_checks':'FastExact.table exact m^2 max WH and m max endpoint assertions, every used (v,s)'}
    print('DOMAIN',o.M,min(vs),max(vs),len(vs),flush=True)
    if o.screen:
        for v in sorted(set([vs[0],vs[-1],vs[-1]-1,(vs[0]+vs[-1])//2])):
            cal=FastExact(12,o.M);D=getD(o.M,v)
            if D is not None:
                for flag in (False,True):
                    p=((D,D,D),flag);z=cal.three(v,*p)
                    res['rows'].append({'v':v,'mode':'three-screen','D':D,'profile':p,'z':z,'gap':S-z})
                    print('SCREEN',res['rows'][-1], 'sec',time.monotonic()-t,flush=True)
    else:
        for v in vs:
            if time.monotonic()-t>o.seconds:break
            cal=FastExact(12,o.M)
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
