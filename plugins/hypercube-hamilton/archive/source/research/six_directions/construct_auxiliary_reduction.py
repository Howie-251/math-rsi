"""Construct R1/R2 paths, retaining and then deleting exactly the input uv auxiliary edge."""
import json
from pathlib import Path
from split_transfer import construct
from single_bridge_probe import verify
ROOT=Path(__file__).resolve().parent

def main():
    candidates=json.loads((ROOT/'auxiliary_reduction_candidates.json').read_text(encoding='utf8'))
    out=[]
    for c in candidates:
        result=construct(c['transformed_matching'],c['new_root'],c['new_target'],c['split_certificate'],allow_original_long=True)
        item=dict(c,intermediate=result,status=result['status'])
        if result['status']=='FOUND':
            k=result['path'];u,v=c['u'],c['v']
            if c['kind']=='covered_target_rotation':
                assert k[-2:]==[u,v]
                final=k[:-1][::-1]+[v]
            else:
                assert (k[0]^k[-1]).bit_count()==1
                start=k.index(u);step=-1 if k[(start+1)%64]==v else 1
                assert k[(start-step)%64]==v
                final=[k[(start+step*j)%64] for j in range(64)]
            verify(6,c['matching'],u,v,final)
            item['path']=final
        out.append(item)
        (ROOT/'auxiliary_reduction_results.json').write_text(json.dumps(out,indent=2),encoding='utf8')
        print(len(out),c['kind'],c['v'],item['status'],flush=True)
    print('TOTAL',len(out),'FOUND',sum(c['status']=='FOUND' for c in out))

if __name__=='__main__':main()
