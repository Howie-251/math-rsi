from pathlib import Path
R=Path(__file__).resolve().parent
rows=[]
for line in (R/'t15_r3_small_core5_c1_B_exceptions.txt').read_text().splitlines():
 t=line.split();fi=t.index('F');rows.append(tuple(map(int,t[1:fi]+t[fi+1:])))
assert len(rows)==len(set(rows))==5
(R/'t15_core5_c1_B_inputs.txt').write_text('\n'.join(' '.join(map(str,t)) for t in rows)+'\n')
s=(R/'t15_r3_small_core0_c1_residual.cpp').read_text()
s=s.replace('6 B inputs times 135135 A partials','5 B inputs times 135135 A partials').replace('bs.size()!=6','bs.size()!=5').replace('blocks={{0},{7},{11},{14}}','blocks={{0},{7},{13},{14}}').replace('ap!=5','ap!=6').replace('~(1u<<5)','~(1u<<6)')
(R/'t15_core5_c1_residual.cpp').write_text(s)
s=(R/'verify_t15_r3_small_core0_c1_residual.cpp').read_text().replace('cases.size()==6','cases.size()==5').replace('port!=5','port!=6').replace('v!=5','v!=6').replace('count==810810','count==675675')
(R/'verify_t15_core5_c1_residual.cpp').write_text(s)
