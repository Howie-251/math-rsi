import pathlib,json,hashlib,itertools,collections
R=pathlib.Path(__file__).resolve().parent
def load(n):return json.loads((R/n).read_text(encoding='utf-8-sig'))
def sha(n):return hashlib.sha256((R/n).read_bytes()).hexdigest()
assert sha('TWELVE_STAR_MAXIMAL_A_FINITE_PROOF.md')=='61bf17243ace72e72529e36afda62c3ba7a2acd6eca59149ecc5af1710bf1575'
assert sha('TWELVE_STAR_MAXIMAL_A_FINITE_MANIFEST.json')=='991ce23f7e59d1ef91aaaa81aa07583883e49a8ea8437b72e7580d1bc3b75f7b'
m=load('TWELVE_STAR_MAXIMAL_A_FINITE_MANIFEST.json')
for n,h in m['hashes'].items():assert sha(n)==h and (R/n).stat().st_size==m['sizes'][n],n
names=['TWELVE_STAR_B_REVIEW.json','Q5_T17_RANK_BATCH_REVIEW.json','TWELVE_EXTRA_FORCED_REVIEW.json','TWELVE_STAR_MAXIMAL_A_REVIEW.json']
for n in names:assert load(n)['verdict']=='PASS'
accepted={}
for row in load('TWELVE_STAR_B_REVIEW.json')['accepted_marked_inputs']:accepted[('starB10',row['index'])]=row
for row in load('TWELVE_EXTRA_FORCED_REVIEW.json')['details']['accepted_marked_local_rows']:accepted[('extra15',row['index'])]=row
old=load('Q5_T17_RANK_BATCH_REVIEW.json');assert sha('Q5_T17_RANK_BATCH_PROOF.md')==old['audited_input_hashes']['Q5_T17_RANK_BATCH_PROOF.md'].removeprefix('sha256:')
for line in (R/'Q5_T17_RANK_BATCH_PROOF.md').read_text().splitlines():
 t=[x.strip() for x in line.strip('|').split('|')]
 if line.startswith('|') and t[0].isdigit() and 'absent' in t[3]:
  accepted[('old7',int(t[0]))]={'minority':[0],'majority':list(map(int,t[1].replace('$','').split(','))),'omitted':list(map(int,t[2].replace('$','').split(','))),'forced_pair':[8,16]}
perms=list(itertools.permutations(range(5)));maps=[tuple(sum(((x>>p[d])&1)<<d for d in range(5)) for x in range(32)) for p in perms]
for tr in maps:
 assert tr[0]==0 and tr[31]==31 and len(set(tr))==32
 assert all((tr[x]^tr[x^(1<<d)]).bit_count()==1 for x in range(32) for d in range(5))
options=load('TWELVE_STAR_MAXIMAL_A_options.json');gates=load('TWELVE_STAR_MAXIMAL_A_B_gates.json');assert options['coordinate_permutation_output_reads_input']
Ts=[(7,11,13,19,21),(7,11,13,19,31),(7,11,13,22,31),(7,11,19,28,31),(7,11,21,25,31),(7,11,21,26,31)]
assert len(options['rows'])==len(gates['rows'])==6
checked=0;types=collections.Counter();grouporders=[]
for i,(row,grow,T) in enumerate(zip(options['rows'],gates['rows'],Ts)):
 assert row['orbit']==grow['star_orbit']==i and row['T']==list(T)
 grouporders.append(sum({tr[t] for t in T}==set(T) for tr in maps))
 assert len(row['options'])==len(grow['options'])
 byindex={g['option_index']:g for g in grow['options']};assert set(byindex)==set(range(len(row['options'])))
 raw=bytearray()
 for j,op in enumerate(row['options']):
  q,t,w,b,case,pi=[op[k] for k in ['q','t','w','b','case','permutation_index']];tr=maps[pi]
  assert tuple(op['vertex_map'])==tr and case in (0,3)
  assert q and q.bit_count()%2==0 and t in set(T)-{31} and (q^t).bit_count()==1
  assert w in {1,2,4,8,16} and b in {1,2,4,8,16} and w!=b
  seed={0:(3,4,7),3:(15,1,7)}[case];assert tuple(tr[x] for x in seed)==(q,b,t)
  g=byindex[j];canon=accepted[(g['B_registry'],g['B_row'])];btr=maps[g['coordinate_permutation_index_canonical_to_actual']]
  S={1,2,4,8,16}-{w,b};J=(set(T)-{t})|S;pair={w,b}
  assert set(canon['minority'])=={0} and {btr[x] for x in canon['majority']}==J and {btr[x] for x in canon['omitted']}==S and {btr[x] for x in canon['forced_pair']}==pair
  assert set(g['actual_B_majority'])==J and set(g['actual_B_omitted'])==S and set(g['actual_B_pair'])==pair
  assert t not in {0}|J and not pair&({0}|J)
  raw.extend(bytes((q,t,w,b,case,pi)));checked+=1;types[g['B_registry']]+=1
 assert bytes(raw)==(R/f'TWELVE_STAR_MAXIMAL_A_options_{i}.bin').read_bytes()
assert checked==657
out={'status':'PASS','frozen_hashes_sizes_checked':len(m['hashes']),'verified_options':checked,'B_registry_counts':dict(types),'T_stabilizer_orders':grouporders,'all_options_actual_B_marked_transports_accepted':True,'all120_coordinate_maps_preserve_cube_and_omissions':True,'accepted_review_hashes':{n:sha(n) for n in names},'finite_A_premise_proved':False,'full_twelve_hole_proved':False,'full_P6_proved':False}
(R/'TWELVE_STAR_MAXIMAL_A_FINITE_REVIEW_prepare.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
