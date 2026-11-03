"""One fixed generic linear-form export. No A/B enumeration or graph."""
from collections import Counter
from pathlib import Path
import json
import resource
import struct
import time

started=time.process_time()
resource.setrlimit(resource.RLIMIT_CPU,(3,3))
out=Path(__file__).resolve().parent
base=out.parents[1]
roots=[4,34,43,71,82,93]
P=109
zero=(0,0,0)
# Coordinate order: coefficient of A, coefficient of B, constant(C=1).
forward=[(0,1,0,zero),(0,2,0,zero),(1,2,6,(0,0,1)),
         (0,1,10,(1,0,0)),(0,1,14,(0,1,0)),(2,2,3,zero)]
producer=json.loads((base/'root0_missing_by_slot.json').read_text())
producer={(x['end_base'],x['phase']):x['missing_field_elements'] for x in producer['slots']}
action_meta=[]
total_words=0
total_triples=0
canonical_matched=False
binary=out/'generic_ab109.forms.bin'
with binary.open('wb') as f:
    f.write(b'ABF1')
    f.write(struct.pack('<IIII',1,P,6,324))
    for r in roots:
        assert pow(r,18,P)==1 and all(pow(r,d,P)!=1 for d in [1,2,3,6,9])
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
            def visit(v,j,c,last,depth):
                global total_words
                total_words+=1
                slots[v][j].add(c)
                if depth==9:return
                for k in outgoing[v]:
                    if k!=(last^1):
                        d=darts[k]
                        q=tuple((a+b)%P for a,b in zip(c,rotations[j][k]))
                        visit(d[1],(j+d[2])%36,q,k,depth+1)
            before=total_words
            visit(root,0,zero,-1,0)
            assert total_words-before==39365
            for target in range(3):
                for j in range(36):
                    triples=sorted(slots[target][j])
                    f.write(struct.pack('<IIII',root,target,j,len(triples)))
                    offset=f.tell()
                    f.write(bytes(x for c in triples for x in c))
                    local_id=root*108+target*36+j
                    rows.append({'slot_id':local_id,'root_base':root,'target_base':target,'phase':j,
                                 'count':len(triples),'coefficient_byte_offset':offset})
                    total_triples+=len(triples)
                    if r==4 and root==0:
                        image={(a*29+b*92+c)%P for a,b,c in triples}
                        assert sorted(set(range(P))-image)==producer[target,j]
        if r==4:canonical_matched=True
        action_meta.append({'r':r,'slots':rows,
                            'priority_slot_ids':[x['slot_id'] for x in sorted(rows,key=lambda x:(x['count'],x['slot_id']))],
                            'minimum_forms':min(x['count'] for x in rows),
                            'count_histogram':dict(Counter(x['count'] for x in rows))})

assert total_words==6*3*39365
metadata={'status':'READY_COMPLETE_GENERIC_ENDPOINT_FORMS',
          'binary_file':binary.name,
          'header':'20bytes: ASCII ABF1; then LEuint32[version1,p109,action_count6,slots_per_action324]',
          'action_stream':'LEuint32r; then324slots orderedroot,end,phase. EachslotLEuint32[root,end,phase,count],followedbycount*3 unsigned8bytes[ua,ub,uc].',
          'coefficient_semantics':'translationendpoint=(ua*A+ub*B+uc)mod109; standardrightvoltagelift, C=1,looptranslation0.',
          'slot_id':'108root+36end+phase,localtoaction',
          'roots':roots,'p':P,'phase_order':36,'slot_count_total':1944,
          'actions':action_meta,'triples_total':total_triples,'named_words_enumerated':total_words,
          'all_NB_lengths_included':[0,9],
          'producer_parameter_domain':71286,
          'canonical_r4_A29_B92_control':'All108root0 slots exactmissing sets MATCH existingactualproducer; noBFS.',
          'canonical_control_matched':canonical_matched,
          'family_validity':'Parentproof: all are simple4regular. C/D commutator is nonzerotranslation(1-r^3) inprimeF109 andphasegcd(3,10)=1, givingconnected108phasecover. Voltageorders18/18/6/12 retained.',
          'CPU_seconds':time.process_time()-started,'parameter_search':False,
          'graph_generation':False,'BFS':0,'running':False,'pending':[]}
(out/'generic_ab109.meta.json').write_text(json.dumps(metadata,indent=2)+'\n')
summary={k:v for k,v in metadata.items() if k!='actions'}
summary['action_minimum_forms']=[{'r':a['r'],'minimum':a['minimum_forms']} for a in action_meta]
(out/'RESULT.json').write_text(json.dumps(summary,indent=2)+'\n')
(out/'terminal.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
