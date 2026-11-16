"""SAT-only independent check against original JSON/bit providers and actual CSR."""
from pathlib import Path
import array,json,time
P=Path(__file__).resolve().parent;G=P.parent;D=G/'current_graph_data'
def words(name,kind):
    x=array.array(kind);x.frombytes((D/name).read_bytes());return x
def main():
    t=time.process_time();c=json.loads((P/'CANDIDATE.json').read_text());pins=c['pins'];chosen=set(pins)
    free=words('FREE_IDS.u32le.bin','I');cap=(D/'CAPACITY.u8.bin').read_bytes()
    assert len(pins)==len(chosen)<=12 and chosen<=set(free) and all(cap[v]>=1 for v in chosen)
    assert [free[i]for i in c['selected_indices']]==pins
    tables=json.loads((G/'LINE_PROVIDER_TABLES.json').read_text());byid={r['plane_global_id']:r for r in tables['planes']}
    retained=set(json.loads((G/'RETAINED_PLANE_IDS.json').read_text()));assert c['open_plane_ids'] and set(c['open_plane_ids'])<=retained
    for pid in c['open_plane_ids']:
        assert all(chosen.intersection(row)for row in byid[pid]['line_free_pin_providers'])
    bits=words('PERIPHERY_R4_FREE.u64le.bin','Q');assert len(bits)==1046*217
    assert all(any(bits[i*217+k//64]>>(k%64)&1 for k in c['selected_indices'])for i in range(1046))
    csr=words('SOURCE_CSR.u32le.bin','I');n,m=csr[0:2];assert(n,m)==(42402,245937)
    assert len(csr)==2+n+1+2*m;offset=csr[2:3+n];adj=csr[3+n:]
    assert offset[0]==0 and offset[-1]==2*m
    for v in pins:assert offset[v+1]-offset[v]==12-cap[v] and offset[v+1]-offset[v]<=11
    seen=bytearray(n);front=list(pins)
    for v in front:seen[v]=1
    layers=[len(front)]
    for depth in range(4):
        nxt=[]
        for v in front:
            for j in range(offset[v],offset[v+1]):
                w=adj[j]
                if not seen[w]:seen[w]=1;nxt.append(w)
        front=nxt;layers.append(len(front))
    missing=[v for v in range(n)if not seen[v]]
    out={'status':'COMPLETE_ACTUAL_R4_COVER'if not missing else'SAT_GEOMETRY_CERTIFICATE_FAILED_ACTUAL_R4',
        'pins':pins,'open_plane_ids':c['open_plane_ids'],'source_n':n,'source_m':m,'candidate_n':n+1,'candidate_m':m+len(pins),
        'original_plane_provider_check':True,'original_all1046_periphery_provider_check':True,'fullchecks':1,
        'actual_CSR_R4_covered':sum(seen),'missing_count':len(missing),'missing':missing,'R4_multisource_layers':layers,
        'source_D5':'Inherited accepted graph; no old all-root revalidation','CPU_seconds':time.process_time()-t}
    (P/'VERIFICATION.json').write_text(json.dumps(out,indent=2)+'\n')
    if not missing:(P/'VALID_NEIGHBORHOOD.txt').write_text(' '.join(map(str,pins))+'\n')
    print(json.dumps({k:v for k,v in out.items()if k!='missing'}),flush=True)
if __name__=='__main__':main()
