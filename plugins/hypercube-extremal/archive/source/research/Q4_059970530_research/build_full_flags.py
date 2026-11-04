from pathlib import Path
import numpy as np,itertools,subprocess,json,time
from scipy import sparse
P=Path(__file__).resolve().parent
# Q2 edges in binary vertex order.
edges=[(0,1),(0,2),(1,3),(2,3)];ei={e:i for i,e in enumerate(edges)}
trans=[]
for p in [(0,1),(1,0)]:
 for t in range(4):
  vm=[t^sum(((x>>j)&1)<<p[j] for j in range(2)) for x in range(4)]
  em=[ei[tuple(sorted((vm[x],vm[y])))] for x,y in edges]
  conn=np.array([sum(((m>>x)&1)<<vm[x] for x in range(4)) for m in range(16)])
  edge=np.array([sum(((m>>x)&1)<<em[x] for x in range(4)) for m in range(16)])
  trans.append((vm,em,conn,edge))
canon=[]
for s in range(256):canon.append(min(int(c[s&15]+16*e[s>>4]) for vm,em,c,e in trans))
reps=sorted(set(canon[s] for s in range(240)));idx={r:i for i,r in enumerate(reps)}
emptycode=np.array([idx.get(canon[s],-1) for s in range(256)],dtype=np.int32);assert len(reps)==45
# Vertex-root Q2 states, modulo interchange of the two directions only.
rootswap=trans[4][3];vcanon=np.minimum(np.arange(16),rootswap);vreps=sorted(set(vcanon[:15]));vi={r:i for i,r in enumerate(vreps)}
vcode=np.array([vi.get(vcanon[s],-1) for s in range(16)],dtype=np.int32);assert len(vreps)==9
emptycode.tofile(P/'empty_flag_codes.bin');vcode.tofile(P/'vertex_flag_codes.bin')
np.savez(P/'new_flags_meta.npz',empty_codes=emptycode,vertex_codes=vcode,empty_reps=reps,vertex_reps=vreps)
subprocess.run(['g++','-O3','-std=c++17',str(P/'full_flags.cpp'),'-o',str(P/'full_flags')],check=True)
subprocess.run([str(P/'full_flags')],cwd=P,check=True)
sh=np.fromfile(P/'full_flags_shadows.bin',dtype=np.int32).reshape(-1,4);g=np.fromfile(P/'full_flags_graphs.bin',dtype=np.uint32)
ptr=np.fromfile(P/'new_flags_ptr.bin',dtype=np.int64);ix=np.fromfile(P/'new_flags_cols.bin',dtype=np.int32);v=np.fromfile(P/'new_flags_vals.bin',dtype=np.int16)
C=sparse.csr_matrix((v,ix,ptr),shape=(len(sh),45*46//2+9*10//2));sparse.save_npz(P/'new_flags_C.npz',C)
np.save(P/'full_flags_shadows.npy',sh);np.save(P/'full_flags_graphs.npy',g)
print('Full graphs (with harmless automorphic duplicates)',len(g),'new flags',C.shape,'nnz',C.nnz,flush=True)
(P/'new_flags_summary.json').write_text(json.dumps({'represented_marked_graphs':len(g),'new_matrix_dimensions':[45,9],'coefficient_denominator':48,'nnz':C.nnz},indent=2))
