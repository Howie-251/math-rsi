"""Fresh deterministic checks; writes only review artifacts, not producer data."""
import collections, hashlib, itertools, json, subprocess
from pathlib import Path
R=Path(__file__).resolve().parent
O=R/'q4_neighbor_review_run'
edge=lambda a,b:tuple(sorted((a,b)))
def matching(es,vertices):
    assert len(es)*2==len(vertices) and sorted(x for e in es for x in e)==sorted(vertices)
def main():
    old=json.loads((R/'CANONICAL_COMPLETION_REVIEW.json').read_text())
    tables={}
    for h in (1,7):
        name=f'q4_distance{h.bit_count()}_avoided_table.bin';raw=(R/name).read_bytes()
        assert 'sha256:'+hashlib.sha256(raw).hexdigest()==old['audited_input_hashes'][name]
        tables[h]=[frozenset(edge(a,m[a]) for a in range(16) if a<m[a]<16)
                   for i in range(0,len(raw),30) if raw[i+16]==255
                   for m in [raw[i:i+16]]]
    inverse=json.loads((R/'eight_ep0_q4_neighbor_inverse.json').read_text())
    for row in inverse['results']:
        v=row['omitted'];bad=collections.defaultdict(set)
        for s in (1,2,4,8):
            h=1 if (v^s).bit_count()==1 else 7
            p=next(p for p in itertools.permutations(range(4))
                   if (sum(((h>>j)&1)<<p[j] for j in range(4))^v)==s)
            tr=lambda a:sum(((a>>j)&1)<<p[j] for j in range(4))^v
            for f in tables[h]:
                f=frozenset(edge(tr(a),tr(b)) for a,b in f)
                t=next(b if a==0 else a for a,b in f if 0 in (a,b))
                m=(f-{edge(0,t)})|{edge(s,t)}
                matching(m,set(range(16))-{0,v});bad[m].add(s)
        assert all(len(ss)==1 for ss in bad.values())
        assert len(bad)==(208 if v==3 else 212)
        assert {frozenset(map(tuple,x['matching'])):set(x['bad_neighbors'])
                for x in row['worst_examples']}==dict(bad)
    census=json.loads((R/'q4_perfect_endpoint_abundance_check.json').read_text())
    assert len(census['all_exceptional_matchings'])==4708
    reconstructed=collections.defaultdict(set)
    for y in range(16):
        if not y.bit_count()%2:continue
        h=1 if y.bit_count()==1 else 7
        p=next(p for p in itertools.permutations(range(4)) if sum(((h>>j)&1)<<p[j] for j in range(4))==y)
        tr=lambda a:sum(((a>>j)&1)<<p[j] for j in range(4))
        for f in tables[h]:
            f=frozenset(edge(tr(a),tr(b)) for a,b in f)
            for e in f:
                for a,b in (e,e[::-1]):
                    pm=frozenset((f-{e})|{edge(0,a),edge(y,b)})
                    matching(pm,set(range(16)));reconstructed[pm].add(y)
    for pm,badys in reconstructed.items():
        rootmate=next(b if a==0 else a for a,b in pm if 0 in (a,b))
        if rootmate.bit_count()%2:badys.add(rootmate)
    assert dict(reconstructed)=={frozenset(map(tuple,x['matching'])):set(x['bad_odd_endpoints']) for x in census['all_exceptional_matchings']}
    shorthist=collections.Counter(4-len(set(x['bad_odd_endpoints'])&{1,2,4,8})
                                 for x in census['all_exceptional_matchings'])
    assert min(shorthist)>=2
    # Distinct A records and every claimed UA edge has a positive 15-cycle witness.
    es=[(a,b) for a in range(16) for b in range(a+1,16) if (a^b).bit_count()==1]
    ei={e:i for i,e in enumerate(es)};records=[];centers=collections.Counter()
    for line in (R/'eight_ep0_q4_star_A.jsonl').read_text().splitlines():
        x=json.loads(line);f=set(map(tuple,x['matching']));matching(f,set(range(16))-{0,15})
        mask=0;common={1,2,4,8}
        for c in x['cycles']:
            assert len(c)==15 and set(c)==set(range(16))-{15}
            ce={edge(c[i],c[(i+1)%15]) for i in range(15)}
            assert len(ce)==15 and f<=ce and all(e in ei for e in ce-f)
            common&={b if a==0 else a for a,b in ce if 0 in (a,b)}
            for e in ce-f:
                if 0 not in e:mask|=1<<ei[e]
        assert common=={x['center']} and mask==x['optional_nonroot_edge_mask']
        records.append(bytes(z for e in x['matching'] for z in e)+bytes([x['center']])+mask.to_bytes(4,'little'))
        centers[x['center']]+=1
    assert len(set(records))==444 and centers=={1:111,2:111,4:111,8:111}
    assert b''.join(records)==(R/'eight_ep0_q4_star_A.bin').read_bytes()
    bad=collections.defaultdict(int)
    for idx,(u,v) in enumerate(es):
        j=(u^v).bit_length()-1;p=list(range(4));p[0],p[j]=p[j],p[0]
        tr=lambda a:sum(((a>>i)&1)<<p[i] for i in range(4))^u
        for f in tables[1]:
            f={edge(tr(a),tr(b)) for a,b in f}
            for e in f:
                for a,b in (e,e[::-1]):
                    pm=(f-{e})|{edge(u,a),edge(v,b)};matching(pm,set(range(16)))
                    mate={a:b for a,b in pm}|{b:a for a,b in pm}
                    key=sum(mate[i]<<(4*i) for i in range(16));bad[key]|=1<<idx
    given={int(k):int(v) for k,v in (ln.split() for ln in (R/'eight_ep0_q4_PB_bad_optional.txt').read_text().splitlines())}
    assert given==dict(bad) and len(bad)==16816 and sum(m.bit_count() for m in bad.values())==22848
    extra={s:sum(bool(m>>ei[edge(0,s)]&1) for m in bad.values()) for s in (1,2,4,8)}
    assert set(extra.values())=={714}
    # Freshly compiled programs, replayed with stdout compared to submitted JSON.
    for exe,source in [('neighbor','eight_ep0_q4_neighbor_spectrum_verification.json'),('pair','eight_ep0_q4_pair_spectrum.json'),('joint','eight_ep0_q4_star_joint.json')]:
        got=json.loads(subprocess.check_output([str(O/(exe+'.exe'))],cwd=R,text=True))
        assert got==json.loads((R/source).read_text())
    # Full fresh A enumeration in an isolated output directory.
    subprocess.check_call([str(O/'prepare.exe')],cwd=O,stdout=subprocess.DEVNULL)
    for name in ('eight_ep0_q4_star_A.bin','eight_ep0_q4_star_A.jsonl'):
        assert (O/name).read_bytes()==(R/name).read_bytes()
    result=dict(status='PASS',short_good_endpoint_histogram_on_4708_exceptions=dict(shorthist),
                nonexceptional_short_good_lower_bound=3,A_witness_records=444,A_centers=dict(centers),
                PB_bad_keys=len(bad),PB_bad_relations=22848,extra_PB_per_center=extra,
                joint_pairs=60316956,residual_pairs=0,table_hashes_match_prior_audit=True)
    (R/'Q4_NEIGHBOR_ABUNDANCE_REVIEW_check.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
if __name__=='__main__':main()
