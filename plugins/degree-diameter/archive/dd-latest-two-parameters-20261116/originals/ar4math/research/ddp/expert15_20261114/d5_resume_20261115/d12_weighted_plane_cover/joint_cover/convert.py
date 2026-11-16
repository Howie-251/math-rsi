"""Bind all754 planes to the same actual-current free-vertex selectors."""
from pathlib import Path
import array,json,sys,time
P=Path(__file__).resolve().parent;G=P.parent;D=G/'current_graph_data'
def main():
    t=time.process_time();meta=json.loads((D/'PROVIDERS_META.json').read_text())
    free=array.array('I');free.frombytes((D/'FREE_IDS.u32le.bin').read_bytes())
    assert sys.byteorder=='little' and len(free)==meta['free_count']==13857
    assert len(set(free))==len(free) and meta['source_n']==42402 and meta['provider_rows']==1046
    capacity=(D/'CAPACITY.u8.bin').read_bytes();assert len(capacity)==42402
    assert all(capacity[v]>0 for v in free)
    index={v:i+1 for i,v in enumerate(free)}
    tables=json.loads((G/'LINE_PROVIDER_TABLES.json').read_text());byid={r['plane_global_id']:r for r in tables['planes']}
    retained=json.loads((G/'RETAINED_PLANE_IDS.json').read_text());assert len(retained)==len(set(retained))==754
    assert tables['source_binding']['source_n']==42402
    lines=0;literals=0
    with(P/'planes.txt').open('w')as out:
        out.write(f'{len(retained)} {len(free)}\n')
        for pid in retained:
            rows=byid[pid]['line_free_pin_providers'];assert len(rows)==91
            out.write(str(pid)+'\n')
            for row in rows:
                ids=sorted({index[v]for v in row});assert ids
                out.write(str(len(ids))+' '+' '.join(map(str,ids))+'\n');lines+=1;literals+=len(ids)
    words=meta['provider_words_per_row'];raw=(D/'PERIPHERY_R4_FREE.u64le.bin').read_bytes()
    assert words==217 and len(raw)==1046*217*8
    (P/'INPUT.json').write_text(json.dumps({'source_n':42402,'source_m':245937,'free_count':len(free),'plane_count':754,
        'plane_line_rows':lines,'plane_provider_positive_literals':literals,'periphery_rows':1046,'periphery_words_per_row':217,
        'periphery_positive_literals':meta['covered_free_sum'],'selector_variable':'FREE_IDS[k] maps to SAT variable k+1',
        'plane_variable':'free_count+retained_plane_position+1','retained_plane_ids':retained,
        'cardinality_cap':12,'at_least_one_plane':True,'exactly_one_plane':False,
        'fixed_core_guard_counts':False,'extra_search_restrictions':[],
        'conversion_CPU':time.process_time()-t},indent=2)+'\n')
    print('INPUT_READY all754/free13857/periphery1046',flush=True)
if __name__=='__main__':main()
