from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
r=ROOT/'formal/Aris4Math/ThirtyFour'
source=(r/'TwentyOneSevenFourCatalogueData.lean').read_text()
for i in [0,1,3,4,5,6,7,8]:
 line=next(x for x in source.splitlines() if x.startswith(f'def rows{i} :'))
 body=line.split(' := ',1)[1][1:-1]
 pieces=[];depth=0;start=0
 for j,c in enumerate(body):
  if c in '([':depth+=1
  elif c in ')]':depth-=1
  elif c==',' and depth==0:pieces.append(body[start:j]);start=j+1
 pieces.append(body[start:]);chunks=[pieces[j:j+32] for j in range(0,len(pieces),32)]
 pre='import Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogueData\nnamespace Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue\nopen TwentyOneSevenFourActualCore (catalogue Valid)\nset_option maxHeartbeats 0\nset_option maxRecDepth 100000\n'
 suffix='end Aris4Math.ThirtyFour.TwentyOneSevenFourCatalogue\n'
 for j,ch in enumerate(chunks):
  n=f'chunk{i}_{j}'
  text=pre+f'def {n} : List Row := ['+','.join(ch)+']\n'
  text+=f'theorem checked_{n} : {n}.all (fun row => decide (Valid {i} row.1 → Matched {i} row.1 row.2.1 row.2.2))=true := by decide +kernel\n'
  (r/f'TwentyOneSevenFourRows{i}Chunk{j}.lean').write_text(text+suffix)
 text=''.join(f'import Aris4Math.ThirtyFour.TwentyOneSevenFourRows{i}Chunk{j}\n' for j in range(len(chunks)))+pre.split('\n',1)[1]
 text+=f'theorem rows_eq{i} : rows{i}.map Prod.fst = catalogue {i} := by decide +kernel\n'
 text+=f'theorem rows_chunks{i} : rows{i}='+'++'.join(f'chunk{i}_{j}' for j in range(len(chunks)))+' := by decide +kernel\n'
 text+=f'theorem rows_checked{i} : rows{i}.all (fun row => decide (Valid {i} row.1 → Matched {i} row.1 row.2.1 row.2.2))=true := by\n  rw [rows_chunks{i}]\n  simp only [List.all_append,'+','.join(f'checked_chunk{i}_{j}' for j in range(len(chunks)))+',Bool.and_self]\n'
 (r/f'TwentyOneSevenFourCatalogueChecked{i}.lean').write_text(text+suffix)
 print(i,len(pieces),len(chunks))
