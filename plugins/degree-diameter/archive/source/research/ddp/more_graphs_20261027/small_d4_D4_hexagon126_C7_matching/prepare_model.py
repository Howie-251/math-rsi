"""Exact C7-equivariant girth>=6 perfectmatching + D4 CNF; no solver/BFS."""
import resource
resource.setrlimit(resource.RLIMIT_CPU,(18,18))
from pathlib import Path
from collections import Counter
from itertools import combinations
import json,time
OUT=Path(__file__).resolve().parent;START=time.process_time()
def save(n,x):(OUT/n).write_text(json.dumps(x,indent=2)+'\n')
class CNF:
 def __init__(self):self.n=0;self.vars=[];self.clauses=[];self.seen=set();self.counts=Counter();self.duplicates=Counter();self.ands={}
 def var(self,kind,**kw):self.n+=1;self.vars.append({'id':self.n,'kind':kind,**kw});return self.n
 def add(self,lits,kind):
  out=set()
  for x in lits:
   if x is True:return False
   if x is False:continue
   if -x in out:return False
   out.add(x)
  clause=tuple(sorted(out,key=lambda x:(abs(x),x)))
  if clause in self.seen:self.duplicates[kind]+=1;return False
  self.seen.add(clause);self.clauses.append(clause);self.counts[kind]+=1;return True
 def conj(self,a,b):
  if a is False or b is False:return False
  if a is True:return b
  if b is True:return a
  if a==b:return a
  key=tuple(sorted((a,b)))
  if key not in self.ands:
   z=self.var('and_witness',arguments=key);self.ands[key]=z;self.add([-z,a],'AND_soundness');self.add([-z,b],'AND_soundness')
  return self.ands[key]
cnf=CNF();src=json.loads((OUT/'SOURCE_LCF_PRIMARY.json').read_text());adj=src['adjacency'];oldedges=[(u,v) for u in range(126) for v in adj[u] if u<v];assert len(oldedges)==189
D=(OUT/'old_distance_to4.u8.bin').read_bytes();assert len(D)==126*126
# One atom pairs two different odd7orbits; no selforbit invariant matching exists.
atoms=[];edge_selector={};incident=[[] for _ in range(18)]
for r,s in combinations(range(18),2):
 for delta in range(7):
  edges=[tuple(sorted((r+18*k,s+18*((k+delta)%7)))) for k in range(7)]
  if not all(D[u*126+v]==255 for u,v in edges):continue
  v=cnf.var('matching_selector',orbit_pair=[r,s],shift=delta)
  atom={'variable':v,'orbit_pair':[r,s],'shift':delta,'actual_edges':edges,'inherited_old_distance':5 if(r%2)!=(s%2) else 6}
  atoms.append(atom);incident[r].append(v);incident[s].append(v)
  for e in edges:assert e not in edge_selector;edge_selector[e]=v
for r,vs in enumerate(incident):
 cnf.add(vs,'orbit_ALO')
 for a,b in combinations(vs,2):cnf.add([-a,-b],'orbit_AMO')
selector_n=cnf.n

def conflict(e,f):
 u,v=e;x,y=f;a=D[u*126+x];b=D[v*126+y]
 if 1<=a<=2 and 1<=b<=2 and a+b<=3:return {'endpoint_pairing':[[u,x],[v,y]],'old_connector_lengths':[a,b]}
 a=D[u*126+y];b=D[v*126+x]
 if 1<=a<=2 and 1<=b<=2 and a+b<=3:return {'endpoint_pairing':[[u,y],[v,x]],'old_connector_lengths':[a,b]}
 return None
self_bad=[];pair_bad=[];pairs_checked=0
for a in atoms:
 e=a['actual_edges'][0]
 for f in a['actual_edges'][1:]:
  w=conflict(e,f)
  if w:
   self_bad.append({'variable':a['variable'],'actual_edges':[e,f],**w});cnf.add([-a['variable']],'girth_self_unit');break
for ia,a in enumerate(atoms):
 e=a['actual_edges'][0]
 for b in atoms[ia+1:]:
  pairs_checked+=1
  for f in b['actual_edges']:
   w=conflict(e,f)
   if w:
    added=cnf.add([-a['variable'],-b['variable']],'girth_pair')
    pair_bad.append({'variables':[a['variable'],b['variable']],'actual_edges':[e,f],**w,'new_distinct_clause':added});break
save('MATCHING_SELECTORS.json',{'selectors':atoms,'count':len(atoms),'orbit_incident_variables':incident,'domain':'all7 atomedges lie beyondoldR4; no sameodd7orbit pair','new_matching_graphs_generated':0})
save('GIRTH_CONSTRAINTS.json',{'self_conflicts':self_bad,'pair_conflicts':pair_bad,'pairs_checked':pairs_checked,'method':'Fixfirstatomfirstactualedge,comparesecondatomall7translates; bothendpointpairings,positiveconnectorssum<=3. Sameatomother6translates checked.','source_girth12':'inherited primary','singleMshortcycles':'excluded byoldR4domain','twoMshortcycles':'exactly4/5cycle conflicts above underperfectmatching','threeMshortcycle':'impossible length<=5 for matching'})
# Canonical unordered pair under simultaneous translation+18.
def canonical(u,v):
 assert u!=v
 return min(tuple(sorted(((u+18*k)%126,(v+18*k)%126))) for k in range(7))
pairmap={e:canonical(*e) for e in combinations(range(126),2)}
pairs=sorted(set(pairmap.values()));assert len(pairs)==1125
far=[e for e in pairs if D[e[0]*126+e[1]]==255];assert len(far)==720
closed1=[set([u]+adj[u]) for u in range(126)]
def support(u,v):
 out=set()
 for x in closed1[v]:
  if x!=u:
   q=edge_selector.get(tuple(sorted((u,x))))
   if q is not None:out.add(q)
 for x in closed1[u]:
  if x!=v:
   q=edge_selector.get(tuple(sorted((v,x))))
   if q is not None:out.add(q)
 return sorted(out)
Y={};ymap=[]
for index,(u,v) in enumerate(pairs):
 dist=D[u*126+v]
 if dist<=2:Y[u,v]=True;ymap.append({'pair_orbit':index,'representative':[u,v],'literal':True,'reason':'fixedoldB2'});continue
 ss=support(u,v)
 # All simultaneousC7translates must have exactly the same selector support.
 assert all(support((u+18*k)%126,(v+18*k)%126)==ss for k in range(7))
 if not ss:Y[u,v]=False;ymap.append({'pair_orbit':index,'representative':[u,v],'literal':False,'reason':'noactual<=2support'});continue
 y=cnf.var('closed_R2',representative=[u,v],support=ss);Y[u,v]=y;cnf.add([-y]+ss,'Y2_soundness');ymap.append({'pair_orbit':index,'representative':[u,v],'literal':y,'support':ss})
def ylit(u,v):return True if u==v else Y[pairmap[tuple(sorted((u,v)))]]
farrows=[]
for u,v in far:
 terms=[cnf.conj(ylit(u,w),ylit(w,v)) for w in range(126)]
 cnf.add(terms,'D4_far_pair')
 farrows.append({'representative':[u,v],'witness_literals':[x for x in sorted(set(x for x in terms if x is not False),key=lambda x:(0 if x is True else x))]})
save('Y2_MAP.json',{'pair_orbits':ymap,'canonical_count':1125,'oldB2_true':sum(y is True for y in Y.values()),'no_support_false':sum(y is False for y in Y.values()),'variable_count':sum(isinstance(y,int) and not isinstance(y,bool) for y in Y.values()),'diagonal_literal':True,'closedB1_support':True,'full_pair_canonicalization':'min sorted(p+18k,q+18k) mod126, k0..6'})
save('D4_FAR_ROWS.json',{'count':720,'canonical_far_pairs':far,'rows':farrows,'middle_vertices':'all0..125 including endpoints','clause_witnesses_sound':'ANDz implies bothR2claims; R2claims require actualedge selector support'})
save('VARIABLE_MAP.json',cnf.vars)
save('INPUT.json',{'source_file':'SOURCE_LCF_PRIMARY.json','source_edges':oldedges,'source_n':126,'source_m':189,'sigma':'v+18 mod126','orbit_encoding':'r+18*k r0..17,k0..6','orbit_count':18,'vertices_per_orbit':7,'selector_count':selector_n,'orbit_exactly1':incident,'matching_selectors_file':'MATCHING_SELECTORS.json','Y2_map_file':'Y2_MAP.json','old_distance_cache':'old_distance_to4.u8.bin','target_n':126,'target_m':252,'target_degree':4,'target_D':4,'additional_family_restriction':'perfectmatchingC7equivariant and augmentedgirth>=6','source_BFS_repeated':False,'matching_graphs_generated':0})
with (OUT/'model.cnf').open('w') as f:
 f.write('c C7matching on directprimary126GH2, exactgirth6 andD4\n');f.write(f'p cnf {cnf.n} {len(cnf.clauses)}\n')
 for c in cnf.clauses:f.write(' '.join(map(str,c))+' 0\n')
stats={'status':'PREPARED_EXACT_CNF_NOT_SOLVED','source_n':126,'source_m':189,'target_n':126,'target_m':252,'target_degree':4,'target_D':4,'C7_orbits':18,'matching_selectors':selector_n,'orbit_incident_counts':[len(v) for v in incident],'girth_self_forbidden_selectors':len(self_bad),'girth_pair_conflicts':len(pair_bad),'selector_pairs_tested':pairs_checked,'canonical_unordered_pair_orbits':1125,'canonical_oldfar_pair_orbits':720,'Y2_oldB2_true':sum(y is True for y in Y.values()),'Y2_no_support_false':sum(y is False for y in Y.values()),'Y2_variables':sum(isinstance(y,int) and not isinstance(y,bool) for y in Y.values()),'AND_shared_variables':len(cnf.ands),'CNF_variables':cnf.n,'CNF_clauses':len(cnf.clauses),'CNF_bytes':(OUT/'model.cnf').stat().st_size,'empty_clauses':sum(not c for c in cnf.clauses),'clause_kind_counts':dict(cnf.counts),'duplicate_clause_counts':dict(cnf.duplicates),'preparation_body_CPU_seconds':time.process_time()-START,'source_or_candidate_BFS_this_preparation':0,'solver_calls':0,'matching_graphs_generated':0}
save('MODEL_STATS.json',stats);save('PREPARATION_RECEIPT.json',stats);print(json.dumps(stats),flush=True)
