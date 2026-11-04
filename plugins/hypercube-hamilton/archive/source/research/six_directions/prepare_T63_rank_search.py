"""Adapt frozen generic forest search to six same-parity holes, three omissions."""
from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'Q5_T26_RANK_search.cpp').read_text()
for old,new in [('N=24,R=2048','N=26,R=4096'),('char,24>','char,26>'),('char,36>','char,32>'),('edges.size()!=18','edges.size()!=16'),('i<8;++i','i<6;++i'),('i<2;++i','i<3;++i'),('K.size()!=24','K.size()!=26'),('data(),36','data(),32'),('data(),24','data(),26'),('basis2048','basis4096')]:
    assert old in s,old;s=s.replace(old,new)
(R/'Q5_T63_RANK_search.cpp').write_text(s)
print('Q5_T63_RANK_search.cpp prepared without modifying the T26 source')
