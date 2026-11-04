"""Exploratory mixed-parity two-omission cycle input; no Q6 claim."""
from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'Q5_T37_INDEPENDENT_search.cpp').read_text()
for old,new in [('N=22,R=1024','N=28,R=8192'),('char,22>','char,28>'),
                ('char,38>','char,32>'),('edges.size()!=19','edges.size()!=16'),
                ('i<10;++i','i<4;++i'),('K.size()!=22','K.size()!=28'),
                ('data(),38','data(),32'),('data(),22','data(),28'),
                ('basis1024','basis8192')]:
    assert old in s,old;s=s.replace(old,new)
(R/'TWELVE_ROOT_STAR_MIXED_probe_search.cpp').write_text(s)
(R/'TWELVE_ROOT_STAR_MIXED_probe_config.txt').write_text('0 1 3 31 0 31\n')
print('Prepared one exploratory mixed-omission input H={0,1,3,31}, U={0,31}.')
