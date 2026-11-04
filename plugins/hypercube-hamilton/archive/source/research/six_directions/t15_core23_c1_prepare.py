from pathlib import Path
R=Path(__file__).resolve().parent
rows=[]
for line in (R/'t15_r3_small_core23_c1_B_exceptions.txt').read_text().splitlines():
 t=line.split();fi=t.index('F');rows.append(tuple(map(int,t[1:fi]+t[fi+1:])))
assert len(rows)==len(set(rows))==20
(R/'t15_core23_c1_B_inputs.txt').write_text('\n'.join(' '.join(map(str,t)) for t in rows)+'\n')
s=(R/'t15_r3_small_core0_c1_residual.cpp').read_text().replace('6 B inputs times 135135 A partials','20 B inputs times 135135 A partials').replace('bs.size()!=6','bs.size()!=20').replace('for(int a=0;a<16;++a)','for(int a=0;a<16;++a)').replace('for(ap=1;ap<16;++ap)if(ap!=3&&ap!=5)','for(ap=0;ap<16;++ap)if(ap!=9&&ap!=3&&ap!=5)').replace('enumerate(65534u&','enumerate(65535u&~(1u<<9)&')
(R/'t15_core23_c1_residual.cpp').write_text(s)
s=(R/'verify_t15_r3_small_core0_c1_residual.cpp').read_text().replace('cases.size()==6','cases.size()==20').replace('count==810810','count==2702700').replace('0xffffffffu^2u^4u','0xffffffffu^(1u<<19)^(1u<<16)').replace('for(port=1;port<16;port++)if(port!=3&&port!=5)','for(port=0;port<16;port++)if(port!=9&&port!=3&&port!=5)').replace('for(int v=1;v<16;v++)if(v!=3&&v!=5&&v!=port)','for(int v=0;v<16;v++)if(v!=9&&v!=3&&v!=5&&v!=port)')
(R/'verify_t15_core23_c1_residual.cpp').write_text(s)
