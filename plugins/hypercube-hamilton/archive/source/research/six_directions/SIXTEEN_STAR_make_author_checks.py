from pathlib import Path
P=Path(__file__).resolve().parent
s=(P/'FOURTEEN_FORCED_author_check.py').read_text();s=s[:s.index('coverage=json.loads')]
s=s.replace('FOURTEEN_FORCED_summary.json','SIXTEEN_STAR_B_summary.json')
s+="\n(R/'SIXTEEN_STAR_B_author_check.json').write_text(json.dumps({'status':'PRODUCER_AUTHOR_CHECK_SUCCESS_NOT_INDEPENDENT_ACCEPTANCE','totals':dict(tot),'reports':results},indent=2)+'\\n')\n"
(P/'SIXTEEN_STAR_B_author_check.py').write_text(s)
