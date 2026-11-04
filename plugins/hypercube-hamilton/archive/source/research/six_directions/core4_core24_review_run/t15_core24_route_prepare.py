from pathlib import Path
from r4_boundary_blocking_probe import negative_table
R=Path('.')
us=(6,10,15);lines=[]
for f in range(3):
 s,t=[z for z in us if z!=us[f]]
 for L in negative_table(s,t,1):lines.append(str(f)+' '+' '.join(str(z) for e in sorted(L) for z in e))
(R/'t15_core24_route_negative.txt').write_text('\n'.join(lines)+'\n')
s=(R/'t15_core1_route_spectra.cpp').read_text().replace('Core1','Core24').replace('core1','core24').replace('int us[3]={3,5,9}','int us[3]={6,10,15}').replace('for(int a=1;a<16;a++)if(a!=3&&a!=5&&a!=9)','for(int a=0;a<16;a++)if(a!=3&&a!=6&&a!=10&&a!=15)').replace('if(!a||!b)continue;','if(a==3||b==3)continue;').replace('genN(65534u&','genN((65535u&~(1u<<3))&').replace('genA(65534u&~(1u<<3)&~(1u<<5)&~(1u<<9),c)','genA(65535u&~(1u<<3)&~(1u<<6)&~(1u<<10)&~(1u<<15),c)')
(R/'t15_core24_route_spectra.cpp').write_text(s)
