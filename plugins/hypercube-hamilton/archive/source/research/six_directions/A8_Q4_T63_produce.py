exec(open('A8_Q4_T63_probe.py',encoding='utf-8-sig').read().split('rows=[]')[0])
rows=[]
for (h,f),size in sorted(orb.items()):
 out=bytearray();pos=neg=0
 for F in pairings(tuple(v for v in range(16) if v not in h)):
  m=bytearray([255]*16)
  for a,b in F:m[a]=b;m[b]=a
  cycle=solve(F,h,f)
  out.extend(m);out.extend(cycle if cycle else [255]*13)
  if cycle:pos+=1
  else:neg+=1
 name='A8_Q4_T63_'+('_'.join(map(str,h)))+'__'+('_'.join(map(str,f)))+'.bin'
 (P/name).write_bytes(out)
 rows.append(dict(holes=h,forbidden=f,orbit=size,positive=pos,negative=neg,file=name))
(P/'A8_Q4_T63_manifest.json').write_text(json.dumps({'status':'CERTIFICATES_PRODUCED_NOT_VERIFIED','rows':rows},indent=2))
print('produced',sum(r['positive'] for r in rows),'positive',sum(r['negative'] for r in rows),'negative')
