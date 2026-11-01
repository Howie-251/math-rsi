"""Compare independently generated support patterns only after literal replay."""
import csv,json
from pathlib import Path
from time import process_time
start=process_time();here=Path(__file__).resolve().parent
own=json.loads((here/'RESULT.json').read_text());prod=json.loads((here.parent/'RESULT.json').read_text())
assert own['complete'] and own['checked_matrices']==264
assert len(prod['matrices'])==264 and prod['complete']
def read(path):
 result={}
 with path.open() as f:
  for x in csv.DictReader(f,delimiter='\t'):
   col=x.get('col_by_row',x.get('col_by_row_0_to_4'))
   key=(int(x['id']),int(x['omit_row']),int(x['omit_col']),tuple(map(int,col.split(','))))
   assert key not in result
   result[key]=int(x['K'])
 return result
op=read(here/'LITERAL_PATTERNS.tsv');pp=read(here.parent/'PATTERNS.tsv')
assert len(op)==len(pp)==17304 and op==pp
labelled=0
for a,b in zip(own['matrices'],prod['matrices']):
 assert a['id']==b['id']
 assert a['J']==b['J'] and a['maxK']==b['maxK']
 assert a['support_patterns']==b['feasible_markings']
 assert a['J_minus_15_maxK']==b['J_minus_15_maxK']
 w=b['maximizer'];key=(b['id'],w['omit_row'],w['omit_col'],tuple(w['col_by_row']))
 assert op[key]==a['maxK']
 # Check the producer's row-major first-label witness metadata as well.
 bit=0;T=0
 for r in range(5):
  for c in range(5):
   if w['col_by_row'][r]==c:
    assert b['matrix'][r][c]>0
    T|=1<<bit
   bit+=b['matrix'][r][c]
 assert bit==20 and T==w['point_mask']
 labelled+=a['labelled_transversals']
res={'status':'PASS','scope':'all 264 imported frozen matrices/J values; new full positive-support generation and literal K replay',
     'matrices_compared':264,'support_patterns_compared':len(op),'all_pattern_keys_equal':True,
     'all_pattern_counts_equal':True,'all_matrix_maxima_equal':True,'all_producer_maximizers_replayed':True,
     'all_producer_first_label_masks_verified':True,'labelled_transversals_across_domain':labelled,
     'support_pattern_count_is_not_labelled_point_choice_count':labelled!=len(op),
     'literal_red_six_subsets':own['literal_red_six_subsets'],
     'minimum_J_minus_15_maxK':own['minimum_J_minus_15_maxK'],
     'minimum_source_id':own['minimum_source_id'],'literal_cpu_seconds':own['cpu_seconds'],
     'compare_cpu_seconds':process_time()-start}
(here/'COMPARISON.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
