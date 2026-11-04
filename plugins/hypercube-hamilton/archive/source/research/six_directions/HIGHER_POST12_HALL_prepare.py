from pathlib import Path
R=Path(__file__).resolve().parent
base=(R/'FOURTEEN_HALL_filter.py').read_text()
for k,stem in ((8,'SIXTEEN_POST12'),(9,'EIGHTEEN_POST12')):
 s=base.replace('FOURTEEN_HALL',stem+'_HALL').replace('FOURTEEN_CACHED_remaining_h14',stem+f'_REUSE_remaining_h{2*k}')
 s=s.replace('==25',f'=={32-k}').replace('%13','%'+str(2*k-1)).replace('//13','//'+str(2*k-1)).replace('13*idx',str(2*k-1)+'*idx').replace('13*(idx+1)',str(2*k-1)+'*(idx+1)')
 s=s.replace('full_fourteen_hole_proved',f'full_{"sixteen" if k==8 else "eighteen"}_hole_proved')
 (R/(stem+'_HALL_filter.py')).write_text(s)
print('Prepared conditional higher-layer positive Hall witness filters')
