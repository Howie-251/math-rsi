from pathlib import Path
import sys
root=Path(__file__).resolve().parents[4];base=root/'formal/Aris4Math/ThirtyFour';name='TwentyFourSixLowUnitAverage'+sys.argv[1]
names=['TwentyFourActualSlotAverage','TwentyFourSlotAverageTable','TwentyFourSlotAverageCache','TwentyFourCachedCongruence','TwentyFourSixLowUnitData',name+'Data'];out=[]
for n in names:
 lines=(base/(n+'.lean')).read_text().splitlines()
 if n=='TwentyFourSixLowUnitData':
  start=next(i for i,x in enumerate(lines) if x.startswith('theorem small_case'))
  lines=lines[:start]+[lines[-1]]
 out+=lines
p=(base/(name+sys.argv[2]+'.lean')).read_text()
if len(sys.argv)>3:
 start=p.index('theorem ');nxt=p.find('\ntheorem ',start+1)
 if nxt>0:p=p[:nxt]+f'\nend Aris4Math.ThirtyFour.{name}\n'
out+=p.splitlines();imp=[];body=[]
for line in out:
 if line.startswith('import '):
  if line.split('.')[-1] not in names: imp.append(line)
 else: body.append(line)
target=Path(__file__).parent/(name+sys.argv[2]+'Probe.lean');target.write_text('\n'.join(dict.fromkeys(imp))+'\n'+'\n'.join(body))
print(target)
