"""Fixed final accounting, independently reconstructed from cube coordinates.

No dynamic ledger, producer or prior checker module is imported. Whole core
theorems are explicit semantic imports; their frozen proof/data hashes are checked.
"""
from pathlib import Path
from itertools import permutations
from collections import Counter
import hashlib,json,subprocess
R=Path(__file__).resolve().parent
HASHES={}
def load(n):return json.loads((R/n).read_text(encoding='utf-8'))
def sha(n):
    if n not in HASHES:
        h=hashlib.sha256()
        with (R/n).open('rb') as f:
            while b:=f.read(8*1024*1024):h.update(b)
        HASHES[n]='sha256:'+h.hexdigest()
    return HASHES[n]
def put(n,x):(R/n).write_text(json.dumps(x,indent=2)+'\n',encoding='utf-8')
CORE={**{k:'T15_SINGLE_AVOIDED_FACE_REVIEW.json' for k in [13,14,19,31,32,35,37,38]},
      **{k:'T15_BALANCED_BRIDGE_REVIEW.json' for k in [2,7,10,44]},
      **{k:f'T15_CORE{k}_FULL_REVIEW.json' for k in [0,1,4,5,8,15,23,24,27]},
      **{k:'T15_ALTERNATIVE_GROUP_REVIEW.json' for k in [18,21,25]}}
EXTRA={0,1,4,5,8,15,18,21,23,24,25,27}
OLD=set(CORE)-EXTRA
REPORTS=sorted(set(CORE.values())|{
 'SIX_HOLE_CLOSURE_CONSEQUENCES_REVIEW.json','CANONICAL_COMPLETION_REVIEW.json',
 'A6_CLOSURE_REVIEW.json','A6_FINITE_INPUTS_REVIEW.json',
 'EIGHT_HOLE_CONDITIONAL_REDUCTION_REVIEW.json','EIGHT_DOUBLE_BRIDGE_REVIEW.json',
 'EIGHT_T15_CORE_MAP_REVIEW.json','EIGHT_HOLE_A1B4_REVIEW.json',
 'T15_NEW_CONSEQUENCES_REVIEW.json','T15_BALANCED_BRIDGE_CONSEQUENCES_REVIEW.json',
 'Q4_NEIGHBOR_ABUNDANCE_REVIEW.json','EIGHT_ALL_EP0_CONSEQUENCES_REVIEW.json'})
def main():
    checked={}
    # Context snapshots are deliberately not theorem premises. Audit hashes are
    # binding proof inputs; auxiliary artifact hashes are checked when R-relative.
    for n in REPORTS:
        report=load(n);assert report.get('verdict',report.get('status'))=='PASS',n
        sha(n);count=0
        for field in ['audited_input_hashes','protected_core_hashes','audit_artifact_hashes',
                      'imported_dependency_hashes','supporting_input_hashes',
                      'checker_artifact_hashes','optional_certificate_hashes']:
            for path,digest in report.get(field,{}).items():
                assert sha(path)==('sha256:'+digest.removeprefix('sha256:')),(n,path)
                count+=1
        if n=='A6_FINITE_INPUTS_REVIEW.json':
            for entry in report['files']:
                assert sha(entry['file'])=='sha256:'+entry['sha256'].removeprefix('sha256:')
                count+=1
        checked[n]={'sha256':sha(n),'bound_inputs_checked':count}
        print('bound',n,count,flush=True)
    geo=load('t15_analytic_geometry.json')['T15']['residual_orbits']
    marked={k:{'holes':sorted([0]+geo[k]['avoided']+geo[k]['included']),
               'omitted':geo[k]['avoided'],'review':CORE[k]} for k in sorted(CORE)}
    # These are the source theorems' explicit marked statements, not counts.
    exact={0:([1,2],[7,11,13]),1:([1,2],[7,11,19]),4:([1,2],[7,11,31]),
      5:([1,2],[7,13,14]),8:([1,2],[7,13,31]),15:([1,2],[13,22,31]),
      18:([1,7],[11,14,28]),21:([1,7],[11,22,28]),23:([1,7],[14,22,26]),
      24:([1,7],[14,22,31]),25:([1,7],[14,26,28]),27:([1,7],[26,28,31])}
    for k,(a,b) in exact.items():assert geo[k]['avoided']==a and geo[k]['included']==b
    lookup={}
    for k,g in enumerate(geo):
        for p in permutations(range(5)):
            def tr(x):return sum(((x>>j)&1)<<p[j] for j in range(5))
            key=(tuple(sorted(map(tr,g['avoided']))),tuple(sorted(map(tr,g['included']))))
            assert key not in lookup or lookup[key][0]==k
            lookup.setdefault(key,(k,p))
    def projections(v,z,w,consume=None):
        out=[]
        for i in range(6):
            za=[x for x in z if (x^v)&(1<<i)==0]
            wa=[x for x in w if (x^v)&(1<<i)==0]
            if len(za)!=2 or len(wa)!=(1 if consume is None else 0):continue
            a=next(x for x in z if (x^v)&(1<<i))
            def pr(x):
                x^=a;assert x&(1<<i)==0
                return (x&((1<<i)-1))|((x>>(i+1))<<i)
            av=tuple(sorted(pr(x^(1<<i)) for x in za))
            inc=tuple(sorted(pr(x) for x in w if x not in wa and x!=consume))
            k,p=lookup[av,inc]
            out.append(dict(cut=i,minority_translation=a,avoided=list(av),included=list(inc),core=k,canonical_to_local_permutation=list(p)))
        return out
    base=load('eight_after_balanced_bridge_candidates.json')
    assert len(base['rows'])==21350
    basekeys={(r['target'],tuple(r['Z']),tuple(r['W'])) for r in base['rows']}
    assert len(basekeys)==21350
    ep=load('EIGHT_ALL_EP0_CONSEQUENCES_REVIEW.json')
    epkeys={(r['target'],tuple(r['Z']),tuple(r['W'])) for r in ep['closed_geometries']}
    assert len(epkeys)==len(ep['closed_geometries'])==50
    rows=[];hist=Counter();nochoices=set()
    for index,r in enumerate(base['rows']):
        v,z,w=r['target'],r['Z'],r['W'];ps=projections(v,z,w)
        assert sorted({p['core'] for p in ps})==r['core_choices'],index
        choices=[p for p in ps if p['core'] in EXTRA]
        row=dict(base_row=index,target=v,Z=z,W=w)
        if ps:
            assert choices,index
            selected=min(choices,key=lambda p:(p['core'],p['cut']))
            row.update(method='a2b1',witness=selected,review=CORE[selected['core']]);hist[selected['core']]+=1
        else:
            key=(v,tuple(z),tuple(w));nochoices.add(key);assert key in epkeys
            row.update(method='EP0',review='EIGHT_ALL_EP0_CONSEQUENCES_REVIEW.json')
        rows.append(row)
    assert nochoices==epkeys
    assert sum(hist.values())==21300
    # Independently rerun complete 27,850,641 eligible covered geometries.
    census=json.loads(subprocess.check_output([str(R/'EIGHT_HOLE_FULL_REVIEW_census.exe')],cwd=R,text=True))
    assert [x['residual'] for x in census['targets']]==[19530,22472,24125]
    put('EIGHT_HOLE_FULL_REVIEW_census.json',census)
    # Directly reconstruct the entire historical elimination chain, without saved
    # choices or historical intermediate binary sets as generating inputs.
    earlier=Counter();retained=set()
    for v in [1,7,31]:
        raw=(R/f'covered_eight_residual_{v}.bin').read_bytes();assert len(raw)%7==0
        for off in range(0,len(raw),7):
            z=list(raw[off:off+3]);w=list(raw[off+3:off+7]);key=(v,tuple(z),tuple(w))
            if any(sum((x^v)&(1<<i)==0 for x in z)==1 and sum((x^v)&(1<<i)==0 for x in w)==4 for i in range(6)):
                earlier['a1b4']+=1;continue
            ps=projections(v,z,w);cs={p['core'] for p in ps}
            if cs&{13,14,19,31,32,35,37,38}:earlier['single_face']+=1
            elif cs&{2,7,10,44}:earlier['balanced_bridge']+=1
            else:retained.add(key)
    assert earlier==dict(a1b4=24669,single_face=7820,balanced_bridge=12288)
    assert retained==basekeys
    # Independent EP0 sufficient-port and optional-edge projection census.
    ginput=load('eight_ep0_three_neighbor_geometry.json')['reports'];projected=[];images=set();orbits=[]
    for rep in ginput:
        v,z,w=rep['target'],rep['Z'],rep['W'];holes={0,*z,*w};deleted=set();suff=[]
        for i in range(6):
            za=[x for x in z if (x^v)&(1<<i)==0]
            if len(za)!=2 or any((x^v)&(1<<i)==0 for x in w):continue
            S={x^(1<<i) for x in w}
            for q in range(64):
                if q==v or q in holes or q^(1<<i) in holes or q.bit_count()%2!=1 or (q^v)&(1<<i):continue
                ns=sorted(S&{q^(1<<j) for j in range(6) if j!=i})
                if len(ns)<3:continue
                deleted.add(tuple(sorted([q,q^(1<<i)])))
                suff.append(dict(cut=i,q=q,mirror=q^(1<<i),S_neighbors=ns))
                for s in ns:
                    t=s^(1<<i);p=next(p for p in projections(v,z,w,t) if p['cut']==i)
                    assert p['core'] in {1,4}
                    projected.append(dict(target=v,Z=z,W=w,cut=i,port=q,selected_edge=[q,s],consumed_odd_hole=t,
                      T15_avoided=p['avoided'],T15_included=p['included'],core=p['core']))
        assert suff==rep['sufficient_crossing_edges']
        isolated=[x for x in range(64) if x not in holes and x.bit_count()%2==0 and
          all(x^(1<<i) in holes or tuple(sorted([x,x^(1<<i)])) in deleted for i in range(6))]
        assert isolated
        orbit=set()
        for p in permutations(range(6)):
            def tr(x):return sum(((x>>j)&1)<<p[j] for j in range(6))
            if tr(v)!=v:continue
            orbit.add((v,tuple(sorted(map(tr,z))),tuple(sorted(map(tr,w)))))
        assert not images&orbit;images|=orbit;orbits.append(dict(target=v,Z=z,W=w,size=len(orbit),isolated=isolated))
    assert images==epkeys
    saved=load('eight_ep0_three_neighbor_projection.json')['rows']
    def serial(x):return json.dumps(x,sort_keys=True)
    assert sorted(map(serial,projected))==sorted(map(serial,saved))
    assert Counter(p['core'] for p in projected)=={4:174,1:60}
    put('EIGHT_HOLE_FULL_REVIEW_witness.json',dict(base_file='eight_after_balanced_bridge_candidates.json',base_sha256=sha('eight_after_balanced_bridge_candidates.json'),
      complete_core_registry=marked,rows=rows))
    # Bind all actual assembly inputs plus the deterministic evidence generated.
    for n in ['EIGHT_HOLE_FULL_CLOSURE.md','A6_AND_EIGHT_FREE_CLOSED.md','SIX_HOLE_CLOSED.md','COVERED_EIGHT_GEOMETRY_CENSUS.md',
      'EIGHT_HOLE_FULL_REVIEW_check.py','EIGHT_HOLE_FULL_REVIEW_census.cpp','EIGHT_HOLE_FULL_REVIEW_census.exe',
      'EIGHT_HOLE_FULL_REVIEW_census.json','EIGHT_HOLE_FULL_REVIEW_witness.json',
      'eight_after_balanced_bridge_candidates.json','eight_ep0_three_neighbor_geometry.json','eight_ep0_three_neighbor_projection.json']:
        sha(n)
    summary=dict(status='PASS',base_rows=21350,a2b1=21300,EP0=50,remaining=0,complete_core_registry=marked,
      selected_core_histogram=dict(sorted(hist.items())),historical_chain=dict(earlier),census=census,
      exact_ep0_orbit_witnesses=orbits,ep0_projection_histogram={'1':60,'4':174},
      imported_reviews=checked,audited_input_hashes=dict(sorted(HASHES.items())),dynamic_ledger_read=False,
      transitive_certificate_rerun=False,whole_core_semantics_imported=True)
    put('EIGHT_HOLE_FULL_REVIEW_check.json',summary)
    print(json.dumps({k:summary[k] for k in ['status','base_rows','a2b1','EP0','remaining','historical_chain','selected_core_histogram']}))
if __name__=='__main__':main()
