from pathlib import Path
R=Path(__file__).resolve().parent
base=(R/'FOURTEEN_FORCED_profile.py').read_text()
for k,stem in ((8,'SIXTEEN_POST12'),(9,'EIGHTEEN_POST12')):
 s=base.replace('FOURTEEN_FORCED',stem+'_FORCED').replace('FOURTEEN_HALL',stem+'_HALL')
 s=s.replace('%13','%'+str(2*k-1)).replace('//13','//'+str(2*k-1)).replace('len(raw),13','len(raw),'+str(2*k-1)).replace('off+13','off+'+str(2*k-1))
 s=s.replace('rec[:6],rec[6:]',f'rec[:{k-1}],rec[{k-1}:]')
 s=s.replace('full_fourteen_hole_proved',f'full_{"sixteen" if k==8 else "eighteen"}_hole_proved')
 (R/(stem+'_FORCED_profile.py')).write_text(s)
print('Prepared conditional higher-layer forced projections')
