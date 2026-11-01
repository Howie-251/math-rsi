from pathlib import Path
p=Path(__file__).with_name('generate_nolow_coverage.py');env={'__file__':str(p.resolve())};exec(compile(p.read_text().split("s='''import")[0],str(p),'exec'),env)
ROOT=env['ROOT'];rows=env['rows'];vec=env['vec'];fs=env['fs']
s='import Aris4Math.ThirtyFour.TwentyFourNoLowCoverageData\n'
s+='\n'.join((ROOT/'formal/Aris4Math/ThirtyFour/TwentyFourSparseDecode.lean').read_text().splitlines()[1:])+'\n'
s+='''namespace Aris4Math.ThirtyFour.TwentyFourNoLowCoverage
open TwentyFourNoLowSixData
open TwentyFourSparseDecode
set_option maxHeartbeats 0
set_option maxRecDepth 100000
'''
s+='def profileHigh : Case→Finset (Finset (Fin 6)) := '+vec('{'+','.join(fs(int(t)) for t,v in r['counts'].items() if int(t).bit_count()>=3 and v)+'}' if any(int(t).bit_count()>=3 and v for t,v in r['counts'].items()) else '∅' for r in rows)+'\n'
s+='''def CheapMatch (b : Bool) (values : List ℕ) (selected : Case×Perm) : Prop :=
  (∀k∈values,k≤1) ∧ extraPair selected.1=b ∧
  (b=true→({0,1} : Finset (Fin 6)).map (perm selected.2).toEmbedding={0,1}) ∧
  support entries values=(profileHigh selected.1).image (fun T=>T.map (perm selected.2).toEmbedding)
instance (b : Bool) (values : List ℕ) (selected : Case×Perm) : Decidable (CheapMatch b values selected) := by unfold CheapMatch;infer_instance
'''
for j,(key,(i,pi)) in enumerate(list(sorted(env['lookup'][1].items()))[-5:]):
 vals=[(key>>k)&1 for k in range(41)]
 s+=f'def sparseValues{j} : List ℕ := '+str(vals)+'\n'
 s+=f'theorem cheap{j} : CheapMatch true sparseValues{j} ({i},{pi}) := by decide +kernel\n'
s+='end Aris4Math.ThirtyFour.TwentyFourNoLowCoverage\n'
Path(__file__).with_name('NoLowSparsePilot.lean').write_text(s)
