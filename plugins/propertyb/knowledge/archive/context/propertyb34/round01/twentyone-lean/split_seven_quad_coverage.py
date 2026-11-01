from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
p=ROOT/'formal/Aris4Math/ThirtyFour/TwentyOneSevenQuadCoverage.lean';s=p.read_text()
start=s.index('theorem coverage :');end=s.index('theorem residue_readback',start)
if 'def coFn' in s: raise SystemExit('already split')
new='''def coFn (k : Fin 64) (j : Fin 6) : Fin 2:=⟨(k.val/2^j.val)%2,by omega⟩
theorem coFn_surjective : ∀co : Fin 6→Fin 2,∃k : Fin 64,coFn k=co := by decide +kernel

'''
for k in range(64):
 new+=f'''theorem coverage{k:02d} : ∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(coFn {k} j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(coFn {k} j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code (coFn {k}) h)).2).toEmbedding)=μ (choose (code (coFn {k}) h)).1 T) := by decide +kernel

'''
new+='''theorem coverage : ∀co : Fin 6→Fin 2,∀h : Fin 5→Fin 3,
    (∀j,Aris4Math.ThirtyThree.TwentyTwoQuadAssembly.highPairSum (fun z=>(h z).val) j≤(co j).val+1)→
    (∀T,recovered 34 (fun _=>7) (fun j=>(co j).val+1) (fun j=>(h j).val)
      (T.map (perm (choose (code co h)).2).toEmbedding)=μ (choose (code co h)).1 T) := by
  intro co h inventory
  obtain ⟨k,rfl⟩:=coFn_surjective co
  fin_cases k
'''
for k in range(64):new+=f'  · exact coverage{k:02d} h inventory\n'
new+='\n'
s=s[:start]+new+s[end:]
namespace='Aris4Math.ThirtyFour.TwentyOneSevenQuadCoverage'
a=s.index('theorem coverage00');b=s.index('theorem residue_readback')
data=s[:a]+'end '+namespace+'\n'
header='import Aris4Math.ThirtyFour.TwentyOneSevenQuadCoverageData\nnamespace '+namespace+'\nopen scoped BigOperators\nopen Aris4Math.ThirtyThree.QuadProfiles\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
kernel=header+s[a:b]+'end '+namespace+'\n'
actual=header.replace('CoverageData','CoverageKernel')+s[b:]
p.with_name('TwentyOneSevenQuadCoverageData.lean').write_text(data)
p.with_name('TwentyOneSevenQuadCoverageKernel.lean').write_text(kernel)
p.write_text(actual)
