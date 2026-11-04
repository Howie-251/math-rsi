from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'SIXTEEN_NEW_TYPES_profile.py').read_text().replace('SIXTEEN_NEW_TYPES','FOURTEEN_MID_TYPES').replace('SIXTEEN_POST12_FORCED_remaining','FOURTEEN_STAR_B_GLOBAL35_remaining')
s=s.replace('%15','%13').replace('//15','//13').replace('len(raw),15','len(raw),13').replace('off+7','off+6').replace('off+15','off+13').replace('if h not in (12,14)','if h not in (8,10)')
(R/'FOURTEEN_MID_TYPES_profile.py').write_text(s)
