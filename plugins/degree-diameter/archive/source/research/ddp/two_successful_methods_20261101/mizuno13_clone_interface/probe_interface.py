from pathlib import Path
from collections import Counter
import json,time,resource

D=Path(__file__).resolve().parent
T=time.process_time();resource.setrlimit(resource.RLIMIT_CPU,(120,121))
def save(name,x):(D/name).write_text(json.dumps(x,indent=2)+'\n')
def dot(a,b):return sum(x*y for x,y in zip(a,b))%3
def mv(A,x):return tuple(dot(row,x) for row in A)
def rref(A):
    M=[list(map(lambda x:x%3,row)) for row in A];piv=[];r=0
    for c in range(len(M[0])):
        z=next((k for k in range(r,len(M)) if M[k][c]),None)
        if z is None:continue
        M[r],M[z]=M[z],M[r];v=pow(M[r][c],-1,3);M[r]=[x*v%3 for x in M[r]]
        for k in range(len(M)):
            if k!=r and M[k][c]:
                v=M[k][c];M[k]=[(a-v*b)%3 for a,b in zip(M[k],M[r])]
        piv.append(c);r+=1
        if r==len(M):break
    return M,piv
def nullvector(A):
    M,piv=rref(A);free=[j for j in range(len(A[0])) if j not in piv];assert len(free)==1
    z=[0]*len(A[0]);z[free[0]]=1
    for row,p in zip(M,piv):z[p]=-row[free[0]]%3
    return z
def rank(A):return len(rref(A)[1])
raw=list(map(int,(D/'source/data/controller_affine_chart.txt').read_text().split()));assert raw[0]==364 and len(raw)==1+364*4*31
chart=[];i=1
for u in range(364):
    row=[]
    for p in range(4):
        v=raw[i];i+=1;A=[raw[i+5*j:i+5*j+5] for j in range(5)];i+=25;b=raw[i:i+5];i+=5
        assert any(b);kernel=nullvector([a+[z] for a,z in zip(A,b)]);assert any(kernel[:5])
        row.append({'target':v,'A':A,'b':b,'source_line_kernel':kernel[:5],'relation_kernel':kernel,'matrix_rank':rank(A)})
    chart.append(row)
V=[tuple((x//3**j)%3 for j in range(5)) for x in range(243)]
Fmask=[0]*364;selfports=[]
for u,row in enumerate(chart):
    for p,e in enumerate(row):
        if e['target']==u:
            F=[];span={tuple(z*t%3 for z in e['b']) for t in range(3)}
            for code,x in enumerate(V):
                y=mv(e['A'],x)
                if tuple((a-b)%3 for a,b in zip(x,y)) in span:F.append(code);Fmask[u]|=1<<code
            selfports.append({'controller':u,'port':p,'self_loop_vectors':F,'count':len(F)})
assert sum(x.bit_count() for x in Fmask)==756
M=list(map(int,(D/'source/data/main_matching.txt').read_text().split()));assert len(M)==88452
assert all(0<=v<88452 and v!=u and M[v]==u for u,v in enumerate(M))
Mtarget=[];Maffine=[];Mdata=[]
for u in range(364):
    targets={M[243*u+x]//243 for x in range(243)};assert len(targets)==1
    v=targets.pop();assert v!=u;Mtarget.append(v)
    vals=[M[243*u+x]%243 for x in range(243)];assert len(set(vals))==243
    base=V[vals[0]];cols=[tuple((a-b)%3 for a,b in zip(V[vals[3**j]],base)) for j in range(5)]
    affine=all(tuple((base[k]+sum(x[j]*cols[j][k] for j in range(5)))%3 for k in range(5))==V[vals[code]] for code,x in enumerate(V))
    Maffine.append(affine);Mdata.append(vals)
assert all(Mtarget[Mtarget[u]]==u for u in range(364))
P=[-1]*88452;Pedges=[]
for line in (D/'source/data/spare_matching.txt').read_text().splitlines():
    a,b=map(int,line.split());assert P[a]<0 and P[b]<0 and a!=b
    P[a]=b;P[b]=a;Pedges.append([a,b])
assert len(Pedges)==378
assert all((P[243*u+x]>=0)==bool(Fmask[u]>>x&1) for u in range(364) for x in range(243))
normals=[v for v in V[1:] if next(x for x in v if x)==1];assert len(normals)==121
normal_mask=[]
for h in normals:
    normal_mask.append([sum(1<<x for x,v in enumerate(V) if dot(h,v)==c) for c in range(3)])
allowed=[]
for row in chart:allowed.append([j for j,h in enumerate(normals) if all(dot(h,e['source_line_kernel']) for e in row)])
common=set.intersection(*(set(x) for x in allowed))
Pfiber=[]
for u in range(364):
    co=Counter(P[243*u+x]//243 for x in range(243) if P[243*u+x]>=0)
    if co:Pfiber.append({'source':u,'target_fiber_counts':dict(sorted(co.items()))})
summary={'status':'STRUCTURE_READ_AND_AFFINE_LINE_KERNELS_CHECKED','source_n':88452,'ordinary_ports':1456,'ordinary_target_distinct_histogram':dict(Counter(len({e['target'] for e in row}) for row in chart)),'A_rank_histogram':dict(Counter(e['matrix_rank'] for row in chart for e in row)),'self_port_count':len(selfports),'self_port_fixedpoint_count_histogram':dict(Counter(x['count'] for x in selfports)),'ordinary_degree11_vertices':756,'self_ports':selfports,'main_matching_fiber_pairs':182,'main_matching_affine_fibers':sum(Maffine),'main_matching_nonaffine_fibers':364-sum(Maffine),'main_matching_controller_target':Mtarget,'main_matching_target_also_ordinary_neighbor_controllers':[u for u in range(364) if Mtarget[u] in {e['target'] for e in chart[u]}],'spare_matching_edges':378,'spare_matching_controller_structure':Pfiber,'transverse_normals_per_controller_histogram':dict(Counter(map(len,allowed))),'zero_transverse_controllers':[u for u,x in enumerate(allowed) if not x],'common_transverse_normal_indices':sorted(common),'common_transverse_normal_vectors':[normals[j] for j in sorted(common)],'preprocessing_CPU_seconds':time.process_time()-T,'BFS_runs':0,'full_graph_generated':False,'full_graph_edge_list_read':False,'source_generator_executed':False}
save('STRUCTURE.json',summary)
save('LINE_KERNELS.json',{'chart':chart,'projective_normals':normals,'allowed_normal_indices':allowed,'normal_fiber_masks':normal_mask})
save('MAPPING_DATA.json',{'main_fiber_target':Mtarget,'main_fiber_coordinate_maps':Mdata,'spare_vertex_map':P,'self_loop_masks':Fmask})
print(json.dumps({k:v for k,v in summary.items() if k not in ['self_ports','main_matching_controller_target','spare_matching_controller_structure','common_transverse_normal_indices','common_transverse_normal_vectors']}))
print('common normals',summary['common_transverse_normal_vectors'])
