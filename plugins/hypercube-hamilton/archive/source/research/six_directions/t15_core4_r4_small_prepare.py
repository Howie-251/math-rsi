"""New core4 copy of the small-c full-spectrum producer; sources preserved."""
from pathlib import Path
from r4_boundary_blocking_probe import negative_table
R=Path(__file__).resolve().parent
src=(R/'t15_core1_route_spectra.cpp').read_text()
src=src.replace('t15_core1_route','t15_core4_r4_small')
for a,b in [('int us[3]={3,5,9}','int us[3]={3,5,15}'),('a!=3&&a!=5&&a!=9','a!=3&&a!=5&&a!=15'),('~(1u<<3)&~(1u<<5)&~(1u<<9)','~(1u<<3)&~(1u<<5)&~(1u<<15)')]:
    assert src.count(a)==1,a;src=src.replace(a,b)
src=src.replace('set<E>zeroFs;','set<E>zeroFs,failureFs;')
src=src.replace('if(!it->second.empty())badB++;','if(!it->second.empty()){badB++;failureFs.insert(F);}')
needle='ofstream bz("t15_core4_r4_small_zero_B"'
assert needle in src
src=src.replace(needle,'ofstream failed("t15_core4_r4_small_fail_B"+to_string(c)+".txt");for(auto&F:failureFs){for(auto[x,y]:F)failed<<x<<" "<<y<<" ";failed<<"\\n";}'+needle)
(R/'t15_core4_r4_small_spectra.cpp').write_text(src)
lines=[]
for f in range(3):
    s,t=[v for i,v in enumerate((3,5,15)) if i!=f]
    for F in negative_table(s,t,1):lines.append(str(f)+' '+' '.join(str(v) for e in sorted(F) for v in e))
(R/'t15_core4_r4_small_negative.txt').write_text('\n'.join(lines)+'\n')
print('negative rows',len(lines))
