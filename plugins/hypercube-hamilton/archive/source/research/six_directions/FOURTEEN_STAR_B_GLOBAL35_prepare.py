from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'FOURTEEN_STAR_B_GLOBAL_profile.py').read_text().replace('FOURTEEN_STAR_B_GLOBAL','FOURTEEN_STAR_B_GLOBAL35')
s=s.replace("for row in summary['reports']:","for row in summary['reports']:\n if row['index']!=35:continue")
(R/'FOURTEEN_STAR_B_GLOBAL35_profile.py').write_text(s)
