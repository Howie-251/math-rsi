from pathlib import Path
R=Path(__file__).resolve().parent
base=(R/'Q5_T37_INDEPENDENT_search.cpp').read_text()
for u in (6,7):
 e=23-u;s=base
 for old,new in [('N=22,R=1024','N=18,R=256'),('char,22>','char,18>'),('char,38>',f'char,{2*e}>'),('edges.size()!=19',f'edges.size()!={e}'),('i<10;++i','i<14;++i'),('i<2;++i',f'i<{u};++i'),('K.size()!=22','K.size()!=18'),('data(),38',f'data(),{2*e}'),('data(),22','data(),18'),('basis1024','basis256')]:
  assert old in s,old;s=s.replace(old,new)
 (R/f'SIXTEEN_NEW_H14_U{u}_search.cpp').write_text(s)
print('Prepared two N18/R256 generators')
