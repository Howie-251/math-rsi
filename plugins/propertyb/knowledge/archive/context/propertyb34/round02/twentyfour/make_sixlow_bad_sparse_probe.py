from pathlib import Path
import json,re
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[3];BASE=ROOT/'formal/Aris4Math/ThirtyFour'
s='''import Aris4Math.ThirtyFour.TwentyFourNoLowCoverageData
import Aris4Math.ThirtyFour.TwentyFourSparseDecode
namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadData
abbrev Case := Fin 181
'''
s+=next(line for line in (BASE/'TwentyFourSixLowBadData.lean').read_text().splitlines() if line.startswith('def badCount :'))+'\n'
s+='''def upper (i : Case) (T : Finset (Fin 6)) : ℕ :=
  if T=∅ then 34 else if T.card=1 then 6 else
  if T={0,1} ∨ (2≤badCount i ∧ T={2,3}) ∨ (3≤badCount i ∧ T={4,5}) then 2 else 1
end Aris4Math.ThirtyFour.TwentyFourSixLowBadData
'''
cd=(BASE/'TwentyFourSixLowBadCoverageData.lean').read_text();cd=cd[cd.index('namespace Aris4Math'):cd.index('def choices :')]
s+=cd+'\nend Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage\n'
s+='\n'.join((BASE/'TwentyFourSixLowBadSparseData.lean').read_text().splitlines()[2:])+'\n'
# Use five real catalogue entries with the largest high support and greatest case index.
old=HERE/'generate_sixlow_bad_coverage.py';env={'__file__':str(old)}
exec(compile(old.read_text().split("s='''import")[0],str(old),'exec'),env)
chosen=sorted(env['lookup'][2].items(),key=lambda kv:(kv[0].bit_count(),kv[1][0],kv[0]),reverse=True)[:5]
s+='''namespace Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage
set_option maxHeartbeats 0
set_option maxRecDepth 100000
'''
for j,(code,(i,perm)) in enumerate(chosen):
 s+=f'theorem pilot{j} : CheapMatch 2 (rowValues ({code},({i},{perm}))) ({i},{perm}) := by decide +kernel\n'
s+='end Aris4Math.ThirtyFour.TwentyFourSixLowBadCoverage\n'
(HERE/'SixLowBadSparsePilot.lean').write_text(s)
fragment=(BASE/'TwentyFourSixLowBadSparseBridge.lean').read_text();fragment=fragment[fragment.index('namespace Aris4Math'):]
a=fragment.index('private theorem profile_high_correct');b=fragment.index('private theorem low_support',a)
fragment=fragment[:a]+'''variable (mu : TwentyFourSixLowBadData.Case→Finset (Fin 6)→ℕ)
variable (profile_high_correct : ∀i T,3≤T.card→mu i T=if T∈profileHigh i then 1 else 0)
'''+fragment[b:]
fragment=re.sub(r'/--.*?-/', '', fragment, flags=re.S)
fragment=fragment.replace('theorem cheap_correct','include mu profile_high_correct in\ntheorem cheap_correct').replace('=μ selected.1 T','=mu selected.1 T')
(HERE/'SixLowBadSparseBridgeAPIProbe.lean').write_text(s+fragment)
(HERE/'SIX_LOW_BAD_SPARSE_PILOT.json').write_text(json.dumps({'cases':[{'code':c,'case':i,'perm':p,'high_blocks':c.bit_count()} for c,(i,p) in chosen]},indent=2)+'\n')
