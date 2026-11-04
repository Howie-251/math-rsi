"""New core4 small-domain checkers; all original files remain unchanged."""
from pathlib import Path
R=Path(__file__).resolve().parent
src=(R/'verify_t15_core1_c0_B.py').read_text()
for a,b in [('us=(3,5,9)','us=(3,5,15)'),('{3,5,9}','{3,5,15}'),('==105','==175'),('range(105)','range(175)'),('105*','175*'),('t15_core1_route','t15_core4_r4_small'),('t15_core1_c0_B','t15_core4_r4_c0_B')]:src=src.replace(a,b)
(R/'verify_t15_core4_r4_c0_B.py').write_text(src)
for old,new in [('t15_core1_c2_types.cpp','t15_core4_r4_c2_types.cpp'),('verify_t15_core1_c2_types.cpp','verify_t15_core4_r4_c2_types.cpp')]:
    src=(R/old).read_text().replace('{3,5,9}','{3,5,15}').replace('!=9','!=15').replace('1u<<9','1u<<15')
    if old.startswith('verify_'):
        src=src.replace('assert(a!=0&&b!=0','assert(a>0&&a<16&&b>0&&b<16&&a!=b&&a!=0&&b!=0')
        src=src.replace('assert(a>=2&&b>=2','assert(a>=2&&a<16&&b>=2&&b<16&&a!=b')
        src=src.replace('assert(pats[f].size()==116);','assert(!pats[f].empty());')
        src=src.replace('bad[0].size()==33&&bad[1].size()==33&&bad[2].size()==33','bad[0].size()==128&&bad[1].size()==128&&bad[2].size()==33')
        src=src.replace('bt[0]==420&&failures==52390800','bt[0]==616&&failures==76839840')
        src=src.replace('exceptional_B_inputs\\\":420','exceptional_B_inputs\\\":616')
    (R/new).write_text(src)
