from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'SIXTEEN_LOCAL_profile.py').read_text().replace('SIXTEEN_LOCAL','FOURTEEN_MID_LOCAL').replace('SIXTEEN_NEW_TYPES','FOURTEEN_MID_TYPES').replace('SIXTEEN_POST12_FORCED_remaining','FOURTEEN_STAR_B_GLOBAL35_remaining')
s=s.replace('%15','%13').replace('//15','//13').replace('15*idx','13*idx').replace('15*(idx+1)','13*(idx+1)').replace('rec[:7],rec[7:]','rec[:6],rec[6:]')
s=s.replace("if pairs and len({x.bit_count()%2", "if pairs and len(U)<3:continue\n if pairs and len({x.bit_count()%2")
(R/'FOURTEEN_MID_LOCAL_profile.py').write_text(s)
