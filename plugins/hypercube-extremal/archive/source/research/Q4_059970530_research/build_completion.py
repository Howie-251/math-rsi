"""Generate exact Q4 completion feature sets, invariant under partial-cube automorphisms.
H=(A,B): crossing edges are indexed by S subset of V(Q3).
A completion is C4-free iff S is independent in A & B.
Feature differences, each with expectation zero:
  3 |S| - (|A|+|B|), mixed_empty-visible_empty,
  mixed_opposite2-visible_opposite2, mixed_single-visible_single.
"""
from pathlib import Path
import numpy as np,json,subprocess,time
P=Path(__file__).resolve().parent
b=np.load(P/'base_data.npz');m=np.load(P/'full_meta.npz')
m['keys'].astype(np.int32).tofile(P/'keys.bin');b['edges'].astype(np.int32).tofile(P/'edges.bin')
np.array(b['squares'],dtype=np.int32).tofile(P/'squares.bin')
subprocess.run(['g++','-O3','-std=c++17',str(P/'completion_features.cpp'),'-o',str(P/'completion_features')],check=True)
subprocess.run([str(P/'completion_features')],cwd=P,check=True)
ptr=np.fromfile(P/'feature_ptr.bin',dtype=np.int64);feats=np.fromfile(P/'features.bin',dtype=np.int8).reshape(-1,4)
counts=np.fromfile(P/'completion_counts.bin',dtype=np.int16)
np.savez_compressed(P/'completion_features.npz',ptr=ptr,features=feats,counts=counts)
print('FEATURES',len(feats),'counts',int(counts.sum()),'unique per type',len(feats)/len(counts),flush=True)
(P/'completion_summary.json').write_text(json.dumps({'partial_types':len(counts),'marked_completion_pairs':int(counts.sum()),'distinct_feature_pairs':len(feats),'min_completions':int(counts.min()),'max_completions':int(counts.max())},indent=2))
