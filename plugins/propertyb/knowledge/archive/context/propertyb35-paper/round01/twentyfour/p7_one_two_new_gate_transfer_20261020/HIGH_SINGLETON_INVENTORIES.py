from pathlib import Path
import json
rows=[]
for I in (1,2):
    E=21-4*I
    for n2 in range(E+1):
        for n3 in range(E//2+1):
            for n4 in range(E//3+1):
                if n2+2*n3+3*n4!=E:continue
                n1=35-I-n2-n3-n4
                assert n1==14+3*I+n3+2*n4
                rows.append(dict(I=I,n1=n1,inventory=[n2,n3,n4]))
assert len(rows)==54 and max(r['n1'] for r in rows)==28
high=sorted([r for r in rows if r['n1']>=27],key=lambda r:(r['n1'],r['I'],r['inventory']))
assert len(high)==9
result=dict(total_integer_inventories=54,counts_by_I=[sum(r['I']==i for r in rows) for i in (1,2)],
            maximum_n1=28,n1_ge27=high,all_integer_inventories=rows)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='all_integer_inventories'},indent=2))
