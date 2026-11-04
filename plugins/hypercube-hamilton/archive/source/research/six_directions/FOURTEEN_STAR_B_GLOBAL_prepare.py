from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'FOURTEEN_FORCED_profile.py').read_text()
s=s.replace('FOURTEEN_FORCED','FOURTEEN_STAR_B_GLOBAL').replace('FOURTEEN_NEW_TYPES_summary.json','FOURTEEN_STAR_B_EXPAND_summary.json').replace('FOURTEEN_HALL_remaining','FOURTEEN_STAR_EXPANDED_remaining')
s=s.replace('[(3,9,3),(2,10,4),(1,11,5)]','[(1,9,4)]')
(R/'FOURTEEN_STAR_B_GLOBAL_profile.py').write_text(s)
print('Prepared generic fourteen-hole application of expanded B inputs')
