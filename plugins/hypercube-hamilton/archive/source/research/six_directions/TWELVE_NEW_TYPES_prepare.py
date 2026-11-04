"""Separate rank generators for new twelve-hole local geometry types."""
from pathlib import Path
R=Path(__file__).resolve().parent
base=(R/'Q5_T37_INDEPENDENT_search.cpp').read_text()
specs={'T28':(22,1024,10,3,18),'T19':(22,1024,10,4,17),
       'T84':(24,2048,8,4,16),'T105':(22,1024,10,5,16)}
for typ,(n,r,h,u,e) in specs.items():
    src=base
    substitutions=[('N=22,R=1024',f'N={n},R={r}'),('char,22>',f'char,{n}>'),
        ('char,38>',f'char,{2*e}>'),('edges.size()!=19',f'edges.size()!={e}'),
        ('i<10;++i',f'i<{h};++i'),('i<2;++i',f'i<{u};++i'),
        ('K.size()!=22',f'K.size()!={n}'),('data(),38',f'data(),{2*e}'),
        ('data(),22',f'data(),{n}'),('basis1024',f'basis{r}')]
    for old,new in substitutions:
        assert old in src,old
        src=src.replace(old,new)
    (R/f'TWELVE_NEW_{typ}_search.cpp').write_text(src)
print('Prepared separate T28/T19/T84/T105 positive-certificate sources.')
