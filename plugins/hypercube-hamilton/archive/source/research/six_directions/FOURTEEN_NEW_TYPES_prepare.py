"""Separate twenty-endpoint rank probes for new actual fourteen-hole inputs."""
from pathlib import Path
R=Path(__file__).resolve().parent
base=(R/'Q5_T37_INDEPENDENT_search.cpp').read_text()
for typ,u in [('T39',3),('T2_10',4),('T1_11',5),('T0_12',6)]:
    s=base
    for old,new in [('N=22,R=1024','N=20,R=512'),('char,22>','char,20>'),
                    ('char,38>',f'char,{2*(22-u)}>'),('edges.size()!=19',f'edges.size()!={22-u}'),
                    ('i<10;++i','i<12;++i'),('i<2;++i',f'i<{u};++i'),
                    ('K.size()!=22','K.size()!=20'),('data(),38',f'data(),{2*(22-u)}'),
                    ('data(),22','data(),20'),('basis1024','basis512')]:
        assert old in s,old;s=s.replace(old,new)
    (R/f'FOURTEEN_NEW_{typ}_search.cpp').write_text(s)
print('Prepared four independent N20/R512 generators.')
