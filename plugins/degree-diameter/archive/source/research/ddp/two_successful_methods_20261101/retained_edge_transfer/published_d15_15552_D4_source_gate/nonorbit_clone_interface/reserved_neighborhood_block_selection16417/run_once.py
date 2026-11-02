"""One reserved-N0 structured MIP; no API probe and no source validation/BFS."""
import argparse
import collections
import csv
import json
import math
import os
from pathlib import Path
import resource
import subprocess
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p/'formal/lean-toolchain').is_file())
CASE = HERE.parent.parent
N = 15552
PRIOR = 68.299114264 + 0.5
CAP = 120.0


def save(name, value):
    p=HERE/name; q=p.with_suffix(p.suffix+'.tmp')
    q.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n'); q.replace(p)


def clean(v):
    if isinstance(v,(str,bool,int)) or v is None:return v
    if isinstance(v,float):return v if math.isfinite(v) else str(v)
    return str(v)


def stage(name,**kw):
    d=dict(stage=name,pid=os.getpid(),**kw);save('CHECKPOINT.json',d)
    print(json.dumps(d,allow_nan=False),flush=True)


def export(adj, degrees, blocks, offsets, A, y, N0):
    centers=[81*i+x for i in blocks for x in offsets]+[0]
    if len(centers)!=865 or len(set(centers))!=865:
        raise RuntimeError('Selected32blocks+extra0 not865distinct')
    baseload=A@y
    if any(int(degrees[w])+int(baseload[w])>15 for w in N0):
        raise RuntimeError('ProtectedN0 not available beforelastclone')
    loads=baseload.copy()
    for w in N0:loads[w]+=1
    if any(int(degrees[w])+int(loads[w])>16 for w in range(N)):
        raise RuntimeError('Finalalloldcapacitycheckfailed')
    byold=[[]for _ in range(N)];added=0
    with (HERE/'ALL865_ROLE_BINDINGS.tsv').open('w',newline='')as f:
        wr=csv.writer(f,delimiter='\t')
        wr.writerow(['j','block_or_extra','old_center_label','new_label','literal_N_size','frozen_old_simple_neighbors'])
        for j,c in enumerate(centers):
            ns=adj[c];added+=len(ns)
            for w in ns:byold[w].append(N+j)
            wr.writerow([j,str(blocks[j//27])if j<864 else 'extra_source0',c,N+j,len(ns),' '.join(map(str,ns))])
    m=116316+added;graph=HERE/'graph_d16_D4_n16417.edges';old=ne=0
    with graph.open('w')as f:
        f.write(f'16417 {m}\n')
        for u in range(N):
            for v in adj[u]:
                if u<v:f.write(f'{u} {v}\n');old+=1
            for v in byold[u]:f.write(f'{u} {v}\n');ne+=1
    if old!=116316 or ne!=added:raise RuntimeError('Exportedgecountmismatch')
    with (HERE/'PROTECTED_N0.tsv').open('w',newline='')as f:
        wr=csv.writer(f,delimiter='\t');wr.writerow(['old_vertex','source_degree','block_load','degree_before_extra0','degree_after_extra0'])
        for w in N0:wr.writerow([w,int(degrees[w]),int(baseload[w]),int(degrees[w]+baseload[w]),int(degrees[w]+loads[w])])
    hist=collections.Counter(int(degrees[w]+loads[w])for w in range(N))
    hist.update(int(degrees[c])for c in centers)
    pars=dict(n=16417,m=m,maxdegree=max(hist),source_n=N,source_m=116316,
              source_literal='research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt',
              selected_blocks=blocks,ordered_offsets=offsets,source_center_labels=centers,
              source_v0=0,source_N0=N0,source_N0_size=len(N0),
              recipe='j<864:center=81*selected_blocks[j//27]+offsets[j%27];j864:center0;newlabel15552+j',
              all865centers_distinct=True,all_protected_degree_before_extra_at_most15=True,
              all_old_capacity_handchecked=True,newnew_edges=0,oldsource_edges_retained=old,
              added_edges=added,degree_histogram=dict(sorted(hist.items())),
              old_load_histogram=dict(sorted(collections.Counter(map(int,loads)).items())),
              new_center_degree_histogram=dict(sorted(collections.Counter(int(degrees[c])for c in centers).items())),
              frozen_simple_oldN=True,private16416_edges_not_a_retention_claim=True,
              fresh_acceptance='PENDING_ROOT',global_priority='UNKNOWN',new_graph_parameter_Lean_count=[0,0,0])
    save('PARAMETERS.json',pars)
    (HERE/'PROOF.md').write_text('# Reserved-N0 full-neighborhood clone candidate\n\n'
        'The only retainedsource is the original15552 simple graph; all116316 oldedges remain. '
        'The32selected wholeW27 blocks may differ from oldI32; no claim preserves old16416cloneedges. '
        'Each newj copies exactly originalsimpleN(centerj), with virtualself alreadyremoved at OLDcenter. '
        'There are no newnew edges. All15552capacities were checked and PROTECTED_N0 shows the '
        'lastsource0clone pins had degree<=15 before insertion.\n\n'
        'SourceD4/nonD3/noisolated are alreadyclosed. FullNeighborhoodClones lifts oldcenter '
        'Walks length>=2 by replacing endpoints with oldinteriors; adjacentcenters use '
        'clone_c--old_d--old_c--clone_d in3 steps, samecenters use anoldneighbor in2. '
        'This works for allprefixes. Collapse to originalsource is a graphhomomorphism '
        'fixing oldvertices, so source nonD3 persists. These inherited arguments and '
        'literaldata do not substitute for root/fresh acceptance or newconcreteLean.\n')
    return pars


def child(hard,limit):
    resource.setrlimit(resource.RLIMIT_CPU,(hard,hard));started=time.process_time()
    stage('IMPORT_SINGLETHREAD',hard_CPU=hard,time_limit=limit)
    import numpy as np
    import scipy
    from scipy.optimize._highspy import _core as h
    source=ROOT/'research/ddp/more_graphs_20261027/d15_D4_current15552/source15552.author.adjlist.txt'
    adj=[]
    with source.open()as f:
        for row in f:
            z=list(map(int,row.split()))
            if z[0]!=len(adj):raise RuntimeError('Acceptedsource labelorderchanged')
            adj.append(sorted(z[1:]))
    if len(adj)!=N:raise RuntimeError('Acceptedsource rowcountchanged')
    degrees=np.array([len(r)for r in adj],dtype=np.int32)
    accepted=json.loads((CASE/'degree16_plane864/PARAMETERS.json').read_text())
    offsets=accepted['ordered_offsets']
    formula=[a+9*b+27*c for c in range(3)for b in range(3)for a in range(3)]
    if offsets!=formula:raise RuntimeError('Actualacceptedoffsetorderdiffers')
    A=np.zeros((N,192),dtype=np.int32)
    for i in range(192):
        for x in offsets:
            for w in adj[81*i+x]:A[w,i]+=1
    N0=adj[0]
    protected=np.zeros(N,dtype=np.int32);protected[N0]=1
    cap=16-degrees-protected
    groups={};coeffs=[];caps=[];rowgroup=[];owners=[]
    for w in range(N):
        key=tuple((int(i),int(A[w,i]))for i in np.flatnonzero(A[w]))
        if key not in groups:
            groups[key]=len(coeffs);coeffs.append(key);caps.append(int(cap[w]));owners.append([])
        g=groups[key];caps[g]=min(caps[g],int(cap[w]));owners[g].append(w);rowgroup.append(g)
    oldblocks=accepted['selected_controller_labels']
    reserved15=[w for w in N0 if degrees[w]==15]
    dropped=[i for i in oldblocks if i==0 or any(A[w,i]>0 for w in reserved15)]
    warmblocks=[i for i in oldblocks if i not in dropped]
    warm=np.zeros(192,dtype=np.int32);warm[warmblocks]=1
    warmloads=A@warm
    if not bool(np.all(warmloads<=cap))or int(warm.sum())>32 or warm[0]:
        raise RuntimeError('Reservedwarmalloldrowhandcheckfailed')
    wr=[]
    for key in coeffs:wr.append(sum(value*int(warm[i])for i,value in key))
    if any(v>c for v,c in zip(wr,caps)):raise RuntimeError('Compressionwarmmismatch')
    save('WARM_START_INPUT.json',dict(oldI32=oldblocks,dropped_blocks=dropped,warm_blocks=warmblocks,
         warm_count=int(warm.sum()),full192column_vector=warm.tolist(),
         all15552rows_handchecked=True,compressedrows_handchecked=True,
         future_source0_reserved=True,N0=N0,protected_old15=reserved15))
    with (HERE/'ALL15552_ROW_MAPPING.tsv').open('w',newline='')as f:
        out=csv.writer(f,delimiter='\t');out.writerow(['old_vertex','group','source_degree','protected_N0','actual_cap','compressed_tightest_cap'])
        for w,g in enumerate(rowgroup):out.writerow([w,g,int(degrees[w]),int(protected[w]),int(cap[w]),caps[g]])
    save('ROW_GROUPS.json',dict(groups=[dict(group=g,coefficients=list(key),tightest_cap=caps[g],oldrows=owners[g])for g,key in enumerate(coeffs)]))
    nr=len(coeffs)+1;indptr=[0];indices=[];data=[]
    for i in range(192):
        for g,key in enumerate(coeffs):
            for col,val in key:
                if col==i:indices.append(g);data.append(val);break
        indices.append(nr-1);data.append(1);indptr.append(len(indices))
    indptr=np.array(indptr,dtype=np.int32);indices=np.array(indices,dtype=np.int32);data=np.array(data,dtype=np.float64)
    rhs=np.array(caps+[32],dtype=np.float64)
    np.savez(HERE/'MODEL_INPUT.npz',indptr=indptr,indices=indices,data=data,rhs=rhs,
             warm=warm,row_group=np.array(rowgroup,dtype=np.int32),source_degree=degrees,
             actual_old_cap=cap,protected_N0=np.array(N0,dtype=np.int32))
    save('MODEL.json',dict(variables=192,compressed_capacity_rows=len(coeffs),cardinality_rows=1,
         nonzeros=len(indices),objective='minimize -sumy',sumy_upper32=True,y0_upper0=True,
         column_rule='accepted27 offsets peractualcontroller',row_rule='16-dG-1_N0;identicalcoefftightestcap',
         all15552rows_bound=True,source_literal=str(source.relative_to(ROOT)),source_literal_parses=1,
         source0_N_size=len(N0),warm_count=int(warm.sum()),threads=1,time_limit=limit,
         scipy_version=scipy.__version__,no_field_oldD4_BFS_Lean=True))
    stage('MODEL_READY',capacity_groups=len(coeffs),warm_count=int(warm.sum()),source0_N_size=len(N0))
    lp=h.HighsLp();lp.num_col_=192;lp.num_row_=nr
    lp.col_cost_=-np.ones(192,dtype=np.float64);lp.col_lower_=np.zeros(192,dtype=np.float64)
    upper=np.ones(192,dtype=np.float64);upper[0]=0;lp.col_upper_=upper
    lp.row_lower_=np.full(nr,-h.kHighsInf,dtype=np.float64);lp.row_upper_=rhs
    lp.integrality_=[h.HighsVarType.kInteger]*192
    lp.a_matrix_.num_col_=192;lp.a_matrix_.num_row_=nr;lp.a_matrix_.format_=h.MatrixFormat.kColwise
    lp.a_matrix_.start_=indptr;lp.a_matrix_.index_=indices;lp.a_matrix_.value_=data
    highs=h._Highs()
    for name,val in [('threads',1),('time_limit',limit)]:
        if highs.setOptionValue(name,val)!=h.HighsStatus.kOk:raise RuntimeError('Requiredoptionfailed')
    ps=highs.passModel(lp);save('PASS_MODEL_RETURN.json',dict(status=str(ps),Highs_version=highs.version()))
    if ps!=h.HighsStatus.kOk:raise RuntimeError('passModelnotkOk_NO_RETRY')
    sol=h.HighsSolution();sol.col_value=warm.astype(float).tolist();sol.row_value=wr+[int(warm.sum())]
    sol.value_valid=True;sol.dual_valid=False
    ss=highs.setSolution(sol);save('WARM_START_RETURN.json',dict(status=str(ss),count=int(warm.sum()),allrows_handchecked=True))
    if ss!=h.HighsStatus.kOk:raise RuntimeError('setSolutionnotkOk_NO_RETRY')
    stage('RUN_ACTIVE',warm_set_status=str(ss),warm_count=int(warm.sum()))
    before=time.process_time();rs=highs.run();solve_cpu=time.process_time()-before
    info=highs.getInfo();ms=highs.getModelStatus();best=highs.getSolution();x=np.asarray(best.col_value,dtype=np.float64)
    raw=dict(run_status=str(rs),model_status=str(ms),message=highs.modelStatusToString(ms),
             solver_CPU_seconds=solve_cpu,HiGHS_version=highs.version(),value_valid=bool(best.value_valid))
    for name in ['objective_function_value','mip_dual_bound','mip_gap','mip_node_count','primal_solution_status']:
        raw[name]=clean(getattr(info,name,None))
    save('RAW_SOLVER_RETURN.json',dict(**raw,column_values=[clean(float(z))for z in x]))
    valid=bool(best.value_valid)and x.size==192
    selected=[];bestcount=None;pars=None
    if valid:
        y=np.rint(x).astype(np.int32)
        valid=bool(np.all(np.abs(x-y)<=1e-6)and np.all(y>=0)and np.all(y<=1)and y[0]==0 and int(y.sum())<=32)
        if valid:
            loads=A@y;valid=bool(np.all(loads<=cap))
            if valid:selected=np.flatnonzero(y).tolist();bestcount=len(selected)
    save('BEST_HANDCHECK.json',dict(binary_and_all15552reservedcaps_valid=valid,
         selected_count=bestcount,selected_blocks=selected,source0_not_in_blockcenters=valid))
    if valid and bestcount==32:
        stage('FOUND32_HANDCHECKED_EXPORTING',selected_blocks=selected)
        pars=export(adj,degrees,selected,offsets,A,y,N0)
    result=dict(status='CANDIDATE16417_WRITTEN_PENDING_FRESH'if pars else
                ('NO32_RAW_OPTIMAL_UNVERIFIED_FIXED_LOOKAHEAD_SCOPE'if ms==h.HighsModelStatus.kOptimal else'UNKNOWN_NO32_IN_SINGLE_WINDOW'),
                selected_count=bestcount,returned_binary_allrows_handchecked=valid,
                selected_blocks=selected,raw_solver=raw,warm_count=int(warm.sum()),
                warm_set_status=str(ss),candidate_generated=pars is not None,candidate=pars,
                actual_child_CPU_before_finalwrite=time.process_time()-started,
                source_literal_parses=1,passModel_calls=1,setSolution_calls=1,run_calls=1,retries=0,
                field_sourceD4_BFS_Lean_ARIS_runs=0,new_graph_parameter_Lean_count=[0,0,0],global_priority='UNKNOWN')
    save('RESULT.json',result);stage('CHILD_TERMINAL',status=result['status'])


def parent():
    started=time.process_time()
    if (HERE/'ATTEMPT.json').exists():raise RuntimeError('Existingoneshotattempt;NO_RESTART')
    hard=min(45,math.floor(CAP-PRIOR-2));limit=min(30.0,hard-4.0)
    if limit<=0:raise RuntimeError('Cumulativebudgetinsufficient')
    packet=dict(status='STARTING',driver_pid=os.getpid(),running=True,prior_CPU_seconds=PRIOR,
                cumulative_CPU_cap_seconds=CAP,child_hard_CPU_seconds=hard,solver_time_limit_seconds=limit)
    save('ATTEMPT.json',packet);save('HANDLE.json',packet)
    env=dict(os.environ)
    for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','NUMEXPR_NUM_THREADS']:env[k]='1'
    cmd=[sys.executable,'-u',str(Path(__file__).resolve()),'--child','--hard',str(hard),'--limit',str(limit)]
    with (HERE/'SOLVER_STDOUT.log').open('w')as out,(HERE/'SOLVER_STDERR.log').open('w')as err:
        p=subprocess.Popen(cmd,env=env,stdout=out,stderr=err)
        packet.update(status='CHILD_ACTIVE',child_pid=p.pid,command=cmd);save('HANDLE.json',packet)
        _,status,usage=os.wait4(p.pid,0);p.returncode=os.waitstatus_to_exitcode(status)
    cpu=usage.ru_utime+usage.ru_stime;driver=time.process_time()-started
    result=json.loads((HERE/'RESULT.json').read_text())if(HERE/'RESULT.json').exists()else dict(status='UNKNOWN_CHILD_FAILURE_NO_RESTART',candidate_generated=False)
    terminal=dict(status=result['status'],child_exit_code=p.returncode,driver_pid=os.getpid(),child_pid=p.pid,
                  running=False,all_processes_terminal=True,prior_CPU_seconds=PRIOR,actual_child_CPU_seconds=cpu,
                  actual_driver_CPU_seconds=driver,cumulative_CPU_seconds=PRIOR+cpu+driver,
                  cumulative_CPU_cap_seconds=CAP,candidate_generated=result.get('candidate_generated',False),
                  selected_count=result.get('selected_count'),retries=0,new_graph_parameter_Lean_count=[0,0,0])
    if not(HERE/'RESULT.json').exists():save('RESULT.json',terminal)
    save('TERMINAL.json',terminal);save('HANDLE.json',terminal);print(json.dumps(terminal),flush=True)


if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--child',action='store_true');ap.add_argument('--hard',type=int);ap.add_argument('--limit',type=float)
    args=ap.parse_args()
    if args.child:
        try:child(args.hard,args.limit)
        except Exception as exc:
            save('FAILURE.json',dict(error=type(exc).__name__,message=str(exc),traceback=traceback.format_exc()))
            save('RESULT.json',dict(status='UNKNOWN_EXECUTION_FAILURE_NO_RESTART',candidate_generated=False,message=str(exc)))
            raise
    else:parent()
