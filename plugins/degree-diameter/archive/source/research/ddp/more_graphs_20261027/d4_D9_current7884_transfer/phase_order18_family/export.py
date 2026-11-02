"""Four ABF1 streams for the four new valid phase-orbit representatives."""
from collections import Counter
from pathlib import Path
import json
import resource
import struct
import time

started=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(5,5))
out=Path(__file__).resolve().parent
roots=[4,34,43,71,82,93]
phasepairs=[(2,10),(2,14),(2,34),(10,22)]
P=109
zero=(0,0,0)
total_words=total_triples=0
summaries=[]
for phaseA,phaseB in phasepairs:
    folder=out/f'frame_{phaseA}_{phaseB}'
    folder.mkdir(exist_ok=True)
    forward=[(0,1,0,zero),(0,2,0,zero),(1,2,6,(0,0,1)),
             (0,1,phaseA,(1,0,0)),(0,1,phaseB,(0,1,0)),(2,2,3,zero)]
    actions=[]
    frame_words=frame_triples=0
    binary=folder/'generic_ab109.forms.bin'
    with binary.open('wb') as f:
        f.write(b'ABF1')
        f.write(struct.pack('<IIII',1,P,6,324))
        for r in roots:
            darts=[]
            for u,v,j,c in forward:
                darts.append((u,v,j,c))
                factor=-pow(r,-j,P)
                darts.append((v,u,(-j)%36,tuple(factor*x%P for x in c)))
            outgoing=[[k for k,d in enumerate(darts) if d[0]==u] for u in range(3)]
            rotations=[[tuple(pow(r,j,P)*x%P for x in d[3]) for d in darts] for j in range(36)]
            f.write(struct.pack('<I',r))
            rows=[]
            for root in range(3):
                slots=[[set() for j in range(36)] for t in range(3)]
                def visit(v,j,a,b,c,last,depth):
                    global total_words,frame_words
                    total_words+=1
                    frame_words+=1
                    slots[v][j].add((a,b,c))
                    if depth==9:return
                    for k in outgoing[v]:
                        if k!=(last^1):
                            d=darts[k]
                            x,y,z=rotations[j][k]
                            visit(d[1],(j+d[2])%36,(a+x)%P,(b+y)%P,(c+z)%P,k,depth+1)
                before=total_words
                visit(root,0,0,0,0,-1,0)
                assert total_words-before==39365
                for target in range(3):
                    for j in range(36):
                        triples=sorted(slots[target][j])
                        f.write(struct.pack('<IIII',root,target,j,len(triples)))
                        offset=f.tell()
                        f.write(bytes(x for c in triples for x in c))
                        rows.append({'slot_id':root*108+target*36+j,'root_base':root,'target_base':target,
                                     'phase':j,'count':len(triples),'coefficient_byte_offset':offset})
                        total_triples+=len(triples)
                        frame_triples+=len(triples)
            actions.append({'r':r,'slots':rows,
                            'priority_slot_ids':[x['slot_id'] for x in sorted(rows,key=lambda x:(x['count'],x['slot_id']))],
                            'minimum_forms':min(x['count'] for x in rows),
                            'count_histogram':dict(Counter(x['count'] for x in rows))})
    meta={'status':'READY_COMPLETE_GENERIC_PHASE_FRAME','phaseA':phaseA,'phaseB':phaseB,
          'p':109,'M':36,'C':1,'Cphase':6,'Dtranslation':0,'Dphase':3,
          'binary_file':binary.name,'header':'ABF1 then LEuint32[1,109,6,324]',
          'action_stream':'uint32r,then324slots:uint32[root,end,phase,count]+count*3u8[ua,ub,uc]',
          'coefficient_semantics':'endpoint=(ua*A+ub*B+uc)mod109',
          'roots':roots,'actions':actions,'triples_total':frame_triples,
          'words_enumerated':frame_words,'parameter_domain':71286,
          'parameter_search':False,'graph_generation':False,'BFS':0}
    (folder/'generic_ab109.meta.json').write_text(json.dumps(meta,indent=2)+'\n')
    summaries.append({'phaseA':phaseA,'phaseB':phaseB,'folder':folder.name,
                      'minimum_forms_by_action':[{'r':a['r'],'minimum':a['minimum_forms']} for a in actions],
                      'words':frame_words,'triples':frame_triples,'parameter_domain':71286})
    print('FRAME_READY',phaseA,phaseB,'min',min(a['minimum_forms'] for a in actions),flush=True)

assert total_words==4*6*3*39365
result={'status':'READY_ALL_24_NEW_PHASE_ACTION_FRAMES','new_phasepairs':phasepairs,
        'frames':summaries,'action_frames':24,'slots':4*6*324,
        'total_named_words':total_words,'total_triples':total_triples,
        'new_parameter_domain':285144,'old_orbit_exported':False,
        'CPU_seconds':time.process_time()-started,'parameter_search':False,
        'graph_generation':False,'BFS':0,'running':False,'pending':[]}
(out/'EXPORT_RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
(out/'FORMS_TERMINAL.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
