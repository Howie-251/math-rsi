"""Extract reduced positive certificates from single forced-cherry full rows."""
from pathlib import Path
import json
R=Path(__file__).resolve().parent
reports=json.loads((R/'TWELVE_EXTRA_TYPES_summary.json').read_text())['reports'];out=[]
def partner(rec):
    p={}
    for a,b in zip(rec[::2],rec[1::2]):p[a]=b;p[b]=a
    return p
def record(p):return bytes(t for a in sorted(p) if a<p[a] for t in (a,p[a]))
def dump_rows(path,rows,width):path.write_bytes(b''.join(x.to_bytes(width,'little') for x in rows))
for row in reports:
    if row['full_rank']:continue
    g=row['geometry'];H=set(g['minority']+g['majority']);U=set(g['omitted']);K=set(range(32))-H
    forced=[]
    for x in sorted(H-U):
        q=[x^(1<<i) for i in range(5) if x^(1<<i) not in U]
        if len(q)==2:forced.append((x,*sorted(q)))
    if len(forced)!=1 or row['rank']!=1024:continue
    h,p,q=forced[0];assert p in K and q in K and len(K)==24
    src=R/row['prefix'];pre=R/f'TWELVE_EXTRA_FORCED_orbit_{row["index"]:03d}'
    matrix=Path(str(src)+'_matrix.bin').read_bytes();assert len(matrix)==1024*256
    fullrows=[int.from_bytes(matrix[i*256:(i+1)*256],'little') for i in range(1024)]
    basis={}
    for original in fullrows:
        x=original
        while x:
            b=x.bit_length()-1
            if b in basis:x^=basis[b]
            else:basis[b]=x;break
        assert x
    chosen=sorted(basis);assert len(chosen)==1024
    fullcols=Path(str(src)+'_columns.bin').read_bytes();reducedcols=[]
    for j in chosen:
        f=partner(fullcols[24*j:24*(j+1)]);assert f[p]!=q
        a,b=f[p],f[q];del f[p];del f[q];f[a]=b;f[b]=a
        assert set(f)==K-{p,q};reducedcols.append(record(f))
    fullpairs=Path(str(src)+'_pairs.bin').read_bytes();reducedpairs=[]
    for i in range(1024):
        f=partner(fullpairs[24*i:24*(i+1)]);assert f[p]==q;del f[p];del f[q]
        reducedpairs.append(record(f))
    smallrows=[sum(((r>>j)&1)<<t for t,j in enumerate(chosen)) for r in fullrows]
    pivots=[0]*1024;combos=[0]*1024
    for i,original in enumerate(smallrows):
        x=original;c=1<<i
        while x:
            j=x.bit_length()-1
            if pivots[j]:x^=pivots[j];c^=combos[j]
            else:pivots[j]=x;combos[j]=c;break
        assert x
    assert all(pivots)
    for suffix in ['_forests.bin','_config.txt']:
        Path(str(pre)+suffix).write_bytes(Path(str(src)+suffix).read_bytes())
    Path(str(pre)+'_full_pairs.bin').write_bytes(fullpairs)
    Path(str(pre)+'_pairs.bin').write_bytes(b''.join(reducedpairs))
    Path(str(pre)+'_columns.bin').write_bytes(b''.join(reducedcols))
    for suffix,vals in [('_matrix.bin',smallrows),('_pivots.bin',pivots),('_combos.bin',combos)]:dump_rows(Path(str(pre)+suffix),vals,128)
    item={'index':row['index'],'prefix':pre.name,'geometry':g,'forced_hole':h,'forced_pair':[p,q],
          'covered_endpoints':24,'reduced_endpoints':22,'rank':1024,'selected_source_columns':chosen,
          'forest_record_bytes':34,'status':'PRODUCER_ONLY'}
    Path(str(pre)+'.json').write_text(json.dumps(item,indent=2)+'\n');out.append(item)
(R/'TWELVE_EXTRA_FORCED_summary.json').write_text(json.dumps({'status':'PRODUCER_ONLY','count':len(out),'reports':out,'full_twelve_hole_proved':False,'full_P6_proved':False},indent=2)+'\n')
print('Extracted',len(out),'single-cherry reduced rank1024 certificates; independent verification pending.')
