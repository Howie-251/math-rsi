"""Bind the accepted degree13 literal sequence without changing degree11/12 steps."""
from datetime import datetime,timezone
from pathlib import Path
import argparse,copy,json

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
STUDY=HERE.parent/'d13_D5_h9_transfer'
PROBE=STUDY/'singlefault_star_probe'

def rel(p):
    return str(p.relative_to(ROOT))

def normalized_step(record,index,evidence):
    oldn=record['actual_base_n'] if 'actual_base_n' in record else record['source_n']
    oldm=record['actual_base_m'] if 'actual_base_m' in record else record['source_m']
    literal=record['full_neighbor_set']
    olddegrees=dict(zip(literal,record['selected_old_degrees']))
    pins=sorted(literal)
    assert len(pins)==len(set(pins))==len(record['selected_old_degrees'])
    mandatory=sorted(record['mandatory_pins'])
    guards=sorted(record['guards'])
    assert sorted(mandatory+guards)==pins
    newdegree=record.get('new_degree',record.get('new_vertex_degree'))
    assert record['new_vertex']==oldn and record['new_n']==oldn+1
    assert newdegree==len(pins)<=13 and record['new_m']==oldm+len(pins)
    assert record['actual_complete_current_R4_missing']==0
    assert record['actual_complete_current_R4_covered']==oldn
    return {'step':index,'source_n':oldn,'source_m':oldm,
            'source':record.get('actual_source_graph','Originalofficial51417rawadjacency; every oldedge retained'),
            'new_vertex':oldn,'pins':pins,'mandatory_pins':mandatory,'anchors':guards,
            'old_pin_degrees':[olddegrees[v]for v in pins],
            'new_vertex_degree':newdegree,'new_n':record['new_n'],'new_m':record['new_m'],
            'neighbor_type':'near-complete old-neighborhood with saturatedpin omitted, plus free guards',
            'prototype':record['prototype'],'prototype_degree':record['prototype_degree'],
            'full_prototype_neighbors':record['full_star_neighbors'],
            'omitted_saturated_pin':record['deleted_saturated_pin'],
            'old_graph_edges_deleted':0,'raw_geometry_used':False,'rawmapping_assumed':False,
            'complete_currentbase_R4_certificate':True,'actual_current_R4_covered':oldn,
            'actual_current_R4_missing':0,'source_evidence':rel(evidence),
            'native_R4_evidence':record['selected_R4_evidence'],'graph_file':record['graph_file'],
            'genericproof_source':'Retainedoldedges plus actualcurrentdegree and completeR4; single-extension induction',
            'accepted_by_parent':True,'parent_pending':False,
            'verification_scope':'First51418hasfreshindependentedge-backednewroot and originalrawedge-retention check. Latersteps use freshactualcurrentdegree/fullR4 induction; no oldallsource repeat.'}

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--include-continuation',action='store_true')
    args=parser.parse_args()
    path=HERE/'families.json'
    data=json.loads(path.read_text())
    preserved={k:copy.deepcopy(data['families'][k])for k in ['11','12']}
    first=json.loads((PROBE/'first_hit.json').read_text())
    records=[first]
    evidence=[PROBE/'first_hit.json']
    if args.include_continuation:
        terminal=json.loads((PROBE/'continuation/terminal.json').read_text())
        assert not terminal.get('running',False)
        sequence=json.loads((PROBE/'continuation/accepted_sequence.json').read_text())
        assert sequence['initial_n']==51418
        records+=sequence['records']
        evidence += [PROBE/'continuation/accepted_sequence.json']*len(sequence['records'])
    steps=[normalized_step(r,i+1,e)for i,(r,e)in enumerate(zip(records,evidence))]
    n,m=51417,324451
    for step in steps:
        assert (step['source_n'],step['source_m'])==(n,m)
        n,m=step['new_n'],step['new_m']
    independent=json.loads((PROBE/'independent_newroot51418.json').read_text())
    family={'degree':13,'diameter_exact':5,
            'base':{'n':51417,'m':324451,'author':'Dharunish Yugeswardeenoo',
                    'project_file':rel(STUDY/'source51417.adjlist.txt'),
                    'source_url':'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/adjacencies/adjD5/deg13_diam5_n51417_adjlist.txt',
                    'description_url':'https://web.mat.upc.edu/francesc.comellas/delta-d/desc_g/desc_g5.html#135',
                    'deposit_url':'https://zenodo.org/records/23653049',
                    'format':'raw adjacency rows, vertex then all neighbors; comment lines allowed',
                    'known_D_at_most':5,
                    'D5_basis':'InheritedpublishedofficialsourceD5, not a newlyprovedrawmapping or repeatedallsourceBFS'},
            'example_orders':[s['new_n']for s in steps],'example_count':len(steps),
            'strongest_n':n,'strongest_m':m,
            'edge_count_formula':'324451+sum(actualnewvertexdegree of appliedliteralsteps)',
            'complete_D5_prefixes_certified':True,'Moore_D4_upper_bound':24506,
            'first_new_parameter_independent_verification':{
                'project_file':rel(PROBE/'independent_newroot51418.json'),**independent},
            'last_independent_newroot_order':51418,'last_independent_allsource_order':None,
            'strongest_complete_verification':{
                'status':'ACCEPTED_BY_CURRENT_BASE_R4_INDUCTION','n':n,'m':m,
                'certificate_file':steps[-1]['native_R4_evidence'],
                'actual_current_R4_covered':steps[-1]['source_n'],'actual_current_R4_missing':0,
                'all_source_BFS_claimed':False},
            'proof_scope':'Eachfullneighbor set covers everyactualcurrentoldvertex atR4. Alloldedges retained, degree<=13, then induction fromofficial51417D5. CurrentD13rawpointmap is not an assumption.',
            'steps':steps}
    data['families']['13']=family
    assert all(data['families'][k]==v for k,v in preserved.items())
    total=sum(f['example_count']for f in data['families'].values())
    data.update(package=f'All{total} explicitretained-edge D5 extensionexamples in degree11,12,13',
                date=datetime.now(timezone.utc).isoformat(),
                distinct_explicit_examples=total,parameter_cells=3)
    data['mathematical_strongest_bounds']['N(13,5)']=n
    data['public_reference_snapshot']['degree13_D5']=51417
    data['public_reference_snapshot']['degree13_source_checked_UTC']='2026-10-27T16:58:01+00:00'
    data['construction_framework_claimed']='Retained-edge completeR4 single-vertex extension induction; distinctneighbor-generation rules.'
    data['neighbor_generation_rules_by_degree']={
        '11':'ExistingQ-line andanchor rules, unchanged literalsteps',
        '12':'ExistingQ-line/Baer13/Redei15 andanchor rules, unchanged literalsteps',
        '13':'Near-complete oldstar, omitted saturatedpin andfreeguards; actualrawadjacency only'}
    data['credits'][0]['role']='Full original37628,42342and51417graphs, plus their authorconstruction'
    data['credits'][-1]['role']=f'ExplicitQ-line/Baer13/Redei15andnear-completeoldstar neighborhoodselection; actualwholecurrentgraphcoverage and{total}literalextensionsteps. Nooriginalityclaimforclassicalblockingtheory.'
    data['proof_schema']+=' Degree13usesactualold-star neighborhoods andguards, with no H9rawpointmap assumption; its first51418freshnewroot check is separate fromlaterproductioninduction.'
    data['latest_degree13_family']={'n':n,'m':m,'examples':len(steps),
        'first_independent_evidence':rel(PROBE/'independent_newroot51418.json'),
        'sequence':rel(PROBE/'continuation/accepted_sequence.json')if args.include_continuation else rel(PROBE/'first_hit.json'),
        'geometric_rawmapping_used':False,'review_status':'Root owns current concentrated Gemini disposition; do not infer all-example review.'}
    assert data['reviewed_example_count']==38
    path.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    status={'status':'D13_LITERAL_FAMILY_BOUND','total_examples':total,'parameter_cells':3,
            'degree13_examples':len(steps),'strongest13_n':n,'strongest13_m':m,
            'old11_and12_families_unchanged':True,'historical_reviewed_example_count':38,
            'BFS_performed':False,'ZIP_rebuilt':False}
    (HERE/'D13_DELIVERY_STATUS.json').write_text(json.dumps(status,indent=2)+'\n')
    print(json.dumps(status,indent=2))

if __name__=='__main__':
    main()
