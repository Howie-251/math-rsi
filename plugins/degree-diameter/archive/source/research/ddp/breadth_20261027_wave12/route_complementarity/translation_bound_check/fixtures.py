"""Hand-solvable fixtures for the independent-translation bound only."""
from pathlib import Path
import json
import time
from translation_cover import hyperplane, maximum_translated_union

HERE=Path(__file__).resolve().parent


def run():
    started=time.process_time()
    cases=[
        ('F2_two_same_rank3',2,[(1,0,0,0),(1,0,0,0)],16,
         'The two cosets of the same hyperplane partitionF2^4;keep multiplicity.'),
        ('F2_two_distinct_rank3',2,[(1,0,0,0),(0,1,0,0)],12,
         'Every pair of translates intersects in4 points,so8+8-4=12.'),
        ('F2_quotient2_three_directions',2,[(1,0,0,0),(0,1,0,0),(1,1,0,0)],16,
         'All3 quotient-line directions through0 coverF2^2;lift multiplies by4.'),
        ('F3_quotient2_three_directions',3,[(1,0,0,0),(0,1,0,0),(1,1,0,0)],63,
         'Three distinct affine lines inF3^2 cover at most7 quotient points;lift multiplies by9.'),
        ('F3_quotient2_four_directions',3,[(1,0,0,0),(0,1,0,0),(1,1,0,0),(1,2,0,0)],81,
         'All4 quotient-line directions through0 coverF3^2;lift multiplies by9.'),
    ]
    results=[]
    for name,q,normals,expected,reason in cases:
        subspaces=[hyperplane(n,q) for n in normals]
        result=maximum_translated_union(subspaces,q,4)
        assert result['exact_max_union']==expected,(name,result)
        result.update(name=name,normals=normals,hand_expected_max_union=expected,
                      hand_reason=reason,status='MATCH_HAND_CALCULATION',
                      fixture_subspaces=subspaces)
        results.append(result)
    d=dict(status='FIVE_SYNTHETIC_FIXTURES_MATCH_HAND_CALCULATIONS',
           scope='Independent arbitrary affine translations of the given route subspaces only;no actual best1152 slot analyzed yet.',
           fixtures=results,CPU_seconds=time.process_time()-started,
           global_offset_searches=0,best1152_slots_analyzed=0,
           canonical1024_candidates_analyzed=0,graph_BFS_count=0,
           new_graphs=0,new_lower_bounds=0)
    (HERE/'FIXTURES.json').write_text(json.dumps(d,indent=2)+'\n')
    print(json.dumps(dict(status=d['status'],maxima=[r['exact_max_union'] for r in results],CPU_seconds=d['CPU_seconds'])))
    return d


if __name__=='__main__':
    run()
