"""Prepare a separate 22-endpoint, 19-short-edge search for independent T37."""
from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'Q5_T26_RANK_search.cpp').read_text()
for old,new in [('N=24,R=2048','N=22,R=1024'),('char,24>','char,22>'),('char,36>','char,38>'),('edges.size()!=18','edges.size()!=19'),('i<8;++i','i<10;++i'),('K.size()!=24','K.size()!=22'),('data(),36','data(),38'),('data(),24','data(),22'),('basis2048','basis1024')]:
    assert old in s,old;s=s.replace(old,new)
(R/'Q5_T37_INDEPENDENT_search.cpp').write_text(s)
print('Prepared independent T37 rank source without changing old inputs.')
