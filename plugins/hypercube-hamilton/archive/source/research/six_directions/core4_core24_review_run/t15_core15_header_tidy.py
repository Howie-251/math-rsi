from pathlib import Path
for name in ['t15_core15_residual.cpp','t15_core15_residual_fast.cpp','t15_core15_residual_ordered.cpp','t15_core15_residual_hybrid.cpp']:
 p=Path(name);s=p.read_text();s=s.replace('// Exact r3 c1 residual: 6 B inputs times 135135 A partials.','// Complete core15 residual input enumeration for c=1 and c=3, each with 1621620 cases.');p.write_text(s)
