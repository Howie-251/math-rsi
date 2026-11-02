"""Normalize fresh incidence/spread IDs only; no field or projection checks."""
import csv,json
from pathlib import Path

def prepare(root):
    pilot=root.parent/'even_q8_gq_geometry_pilot'
    metadata=json.loads((pilot/'PARAMETERS.json').read_text())
    specs=[dict(case='derived',np=512,nl=640,a=8,b=10,j=64,degree=80,oldn=327680,oldm=13104640,n=327744,m=13109760,
                incidence=metadata['derived']['incidence'],spread=metadata['derived']['spread64'],spread_column='derived_line',
                point_ids=metadata['derived']['points'],line_ids=metadata['derived']['lines']),
           dict(case='balanced',np=585,nl=585,a=9,b=9,j=65,degree=81,oldn=342225,oldm=13857480,n=342290,m=13862745,
                incidence=metadata['PG3']['incidence'],spread=metadata['spread65']['line_binding'],spread_column='original_line',
                point_ids=metadata['PG3']['points'],line_ids=metadata['PG3']['all_RREF_2D_subspaces'])]
    for s in specs:
        lp=[[]for _ in range(s['nl'])];pl=[[]for _ in range(s['np'])]
        for row in csv.DictReader((pilot/s['incidence']).open(),delimiter='\t'):
            l,p=int(row['line']),int(row['point']);lp[l].append(p);pl[p].append(l)
        for row in lp:row.sort();assert len(row)==s['a']
        for row in pl:row.sort();assert len(row)==s['b']
        records=list(csv.DictReader((pilot/s['spread']).open(),delimiter='\t'))
        assert [int(r['spread'])for r in records]==list(range(s['j']))
        spread=[int(r[s['spread_column']])for r in records];owner=[-1]*s['np']
        for j,l in enumerate(spread):
            for p in lp[l]:
                assert owner[p]==-1;owner[p]=j
        assert all(j>=0 for j in owner)
        directory=root/s['case'];directory.mkdir(exist_ok=True)
        with(directory/'TABLES_INPUT.txt').open('w')as f:
            f.write(' '.join(map(str,[s[k]for k in ['np','nl','a','b','j','oldn','oldm','n','m','degree']]))+'\n')
            for rows in [lp,pl]:
                for row in rows:f.write(' '.join(map(str,row))+'\n')
            f.write(' '.join(map(str,spread))+'\n');f.write(' '.join(map(str,owner))+'\n')
        s['old_label_formula']='p*nl+l';s['point_id_order']='fresh '+s['point_ids'];s['line_id_order']='fresh '+s['line_ids']
        (directory/'PARAMETERS.json').write_text(json.dumps(s,indent=2)+'\n')
    return specs
