from pathlib import Path
import hashlib,json
R=Path(__file__).resolve().parent
names=['A8_TYPED_SPECTRUM_REPORT.md','A8_ORBIT4_FOUR_CUT_SIGNATURES.md','A8_orbit4_four_cut_bad_signatures.py','A8_orbit4_four_cut_bad_signatures.json','A8_typed_spectrum.cpp','A8_typed_spectrum_verify.py','A8_typed_spectrum_verified.json']
for c in (1,3,5):
 names += [f'A8_typed_c{c}_{s}' for s in ['A.bin','B.bin','result.json','zero_examples.txt']]
 names += [f'A8_three_bridge_low_B_c{c}.bin']
rows=[dict(file=n,bytes=(R/n).stat().st_size,sha256=hashlib.sha256((R/n).read_bytes()).hexdigest()) for n in names]
out=dict(status='VERIFIER_PASS_FRESH_PROOF_CHECKER_REVIEW_PENDING',scope='Exact emptiness of the fixed low-gap three-bridge pairing spectrum and four-cut restricted matching signatures',full_A8_proved=False,all_A_masks_independently_recomputed=True,files=rows)
(R/'A8_TYPED_SPECTRUM_MANIFEST.json').write_text(json.dumps(out,indent=2)+'\n')
print(sum(r['bytes'] for r in rows),'bytes',len(rows),'files')
