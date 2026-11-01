#!/usr/bin/env python3
"""Independent filtering, permutation transport and raw ABC replay; no DP/quota."""
import json
import sys
from pathlib import Path
from itertools import combinations
from fractions import Fraction
from collections import Counter
from time import process_time
sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in HERE.parents if (p/'computations/independent_structure_bounds.py').exists())
sys.path.insert(0,str(ROOT/'computations'))
from independent_structure_bounds import independent_rows
SOURCE=HERE.parent
CAT=ROOT/'context/propertyb34/round01/high-math/UNIT_CATALOGUE_9.json'


def read(path):
    return json.loads(path.read_text())


def raw_rows(record):
    stubs=[]
    for mask,multiplicity in record['counts'].items():
        trace=frozenset(i+1 for i in range(9) if int(mask)>>i&1)
        stubs.extend([trace]*multiplicity)
    assert len(stubs)==35
    return independent_rows(25,tuple(record['positions']),stubs)


def stringify(value):
    if isinstance(value,Fraction):return str(value)
    if isinstance(value,dict):return {str(k):stringify(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):return [stringify(v) for v in value]
    return value


def full_block_sets(big):
    # Decode sets first, and remove already covered pairs from K9; no fullblocks import.
    blocks=[frozenset(i for i in range(9) if mask>>i&1) for mask in big]
    assert all(3<=len(block)<=5 for block in blocks)
    used=set()
    for block in blocks:
        for pair in combinations(sorted(block),2):
            assert pair not in used
            used.add(pair)
    blocks.extend(frozenset(pair) for pair in combinations(range(9),2) if pair not in used)
    return blocks


def encode(block):return sum(1<<i for i in block)


def relabel_counts(counts,perm):
    answer=Counter()
    for mask,n in counts.items():
        answer[sum(1<<perm[i] for i in range(9) if mask>>i&1)]+=n
    return dict(answer)


def main():
    started=process_time()
    certs=read(SOURCE/'ALL140_CERTIFICATES.json')
    if '--profile' in sys.argv:
        t=process_time()
        for r in certs[:3]:
            rows=raw_rows(r)
            assert sum((z['bound'] for z in rows),Fraction(0))==Fraction(r['raw_witness_bound'])
        profile={'status':'PASS','profile_labels':3,'cpu_seconds':process_time()-t,
                 'estimated_raw_140_cpu_seconds':(process_time()-t)*140/3,
                 'method':'expanded 35 edge stubs, exact labelled injections, all 25 raw ABC rows',
                 'imports':'only computations/independent_structure_bounds.py; no primary rows, quota or DP'}
        (HERE/'PROFILE.json').write_text(json.dumps(profile,indent=2)+'\n')
        print(json.dumps(profile));return
    catalogue=read(CAT)
    assert catalogue['complete'] and len(catalogue['orbits'])==374
    counts_by_key={}
    excluded_low=excluded_negative=0
    for base,big in enumerate(catalogue['orbits']):
        blocks=full_block_sets(big)
        for low_tuple in combinations(range(9),6):
            low=set(low_tuple)
            if any(len(block&low)>2 for block in blocks):
                excluded_low+=1;continue
            target=[6 if i in low else 7 for i in range(9)]
            singles=[target[i]-sum(i in block for block in blocks) for i in range(9)]
            empty=35-len(blocks)-sum(singles)
            if empty<0 or any(n<0 for n in singles):
                excluded_negative+=1;continue
            counts=Counter({encode(block):1 for block in blocks})
            counts.update({1<<i:n for i,n in enumerate(singles) if n})
            if empty:counts[0]=empty
            assert sum(counts.values())==35
            assert all(sum(n for mask,n in counts.items() if mask>>i&1)==target[i] for i in range(9))
            assert all(sum(n for mask,n in counts.items() if mask>>i&1 and mask>>j&1)==1 for i,j in combinations(range(9),2))
            counts_by_key[base,low_tuple]=dict(counts)
    assert (excluded_low,excluded_negative,len(counts_by_key))==(29485,1791,140)
    assert len({base for base,low in counts_by_key})==81
    bykey={(r['base'],tuple(r['low'])):r for r in certs}
    assert len(bykey)==len(certs)==140 and set(bykey)==set(counts_by_key)
    domain=read(SOURCE/'DOMAIN.json')
    domain_bykey={(r['base'],tuple(r['low'])):r for r in domain['records']}
    assert set(domain_bykey)==set(bykey)
    canonical_counts={};transport_records=[]
    for key,counts in counts_by_key.items():
        record=bykey[key]; dom=domain_bykey[key]
        assert counts=={int(mask):n for mask,n in record['counts'].items()}
        assert counts=={int(mask):n for mask,n in dom['counts'].items()}
        perm=dom['old_to_canonical']
        assert sorted(perm)==list(range(9))
        canonical=tuple(sorted(dom['canonical_large'])),dom['canonical_lowmask']
        assert sorted(sum(1<<perm[i] for i in range(9) if mask>>i&1) for mask in catalogue['orbits'][key[0]])==list(canonical[0])
        assert sum(1<<perm[i] for i in key[1])==canonical[1]
        mapped=relabel_counts(counts,perm)
        if canonical in canonical_counts:assert canonical_counts[canonical]==mapped
        canonical_counts[canonical]=mapped
        repkey=record['representative_base'],tuple(record['representative_low'])
        rep=bykey[repkey];repdom=domain_bykey[repkey]
        repperm=repdom['old_to_canonical']
        assert sorted(repperm)==list(range(9))
        assert (tuple(sorted(repdom['canonical_large'])),repdom['canonical_lowmask'])==canonical
        inverse=[repperm.index(i) for i in range(9)]
        actual_to_rep=[inverse[perm[i]] for i in range(9)]
        assert sorted(actual_to_rep)==list(range(9))
        assert relabel_counts(counts,actual_to_rep)==counts_by_key[repkey]
        assert {actual_to_rep[i] for i in key[1]}==set(repkey[1])
        assert record['positions']==[rep['positions'][actual_to_rep[i]] for i in range(9)]
        assert len(set(record['positions']))==9 and min(record['positions'])>=1 and max(record['positions'])<=25
        transport_records.append({'base':key[0],'low':key[1],'representative_base':repkey[0],
                                  'representative_low':repkey[1],'actual_to_representative':actual_to_rep})
    assert len(canonical_counts)==105
    # Direct raw probability replay on every actual labelled input, not just representatives.
    probability=[];failed=[];strict_values=[];classes=Counter()
    for record in certs:
        assert process_time()-started<60,'60 CPU second limit'
        rows=raw_rows(record)
        value=sum((row['bound'] for row in rows),Fraction(0))
        assert value==Fraction(record['raw_witness_bound'])==Fraction(record['bound'])
        assert record['strict']==(value<1)
        probability.append({'base':record['base'],'low':record['low'],'positions':record['positions'],
                            'raw_bound':value,'rows':rows})
        if value<1:
            strict_values.append(value);continue
        ns=counts_by_key[record['base'],tuple(record['low'])]
        lowmask=sum(1<<i for i in record['low']); high=[i for i in range(9) if not lowmask>>i&1]
        highmask=sum(1<<i for i in high)
        signatures=[]
        for h in high:
            # Reconstruct private lows and paired lows, not their saved projection.
            private=[];matching=[]
            for mask,n in ns.items():
                if not mask>>h&1:continue
                lt=[i for i in record['low'] if mask>>i&1]
                if len(lt)==1:private.extend(lt*n)
                if len(lt)==2:matching.extend([lt]*n)
            assert sorted(private+[i for pair in matching for i in pair])==record['low']
            signatures.append({'high':h,'private_lows':sorted(private),'s':len(private),'matching':matching})
        pattern=sorted(r['s'] for r in signatures)
        purecommon=sum(n for mask,n in ns.items() if mask&highmask==highmask and mask&lowmask==0)
        label=''.join(map(str,pattern))+('/common_pure' if purecommon else '/no_common_pure')
        classes[label]+=1
        failed.append({'base':record['base'],'low':record['low'],'raw_bound':value,
                       's':pattern,'common_pure_count':purecommon,'signatures':signatures})
    assert len(strict_values)==128 and len(failed)==12 and max(strict_values)==Fraction(1429,1430)
    assert classes=={'024/common_pure':1,'222/common_pure':2,'224/no_common_pure':8,'006/common_pure':1}
    zero=[r for r in failed if 0 in r['s']]
    assert [(r['base'],r['low'],r['s'],r['common_pure_count']) for r in zero]==[
        (23,[0,1,3,4,5,6],[0,2,4],1),(314,[1,2,3,4,5,6],[0,0,6],1)]
    archived=read(SOURCE/'FAILED_SIGNATURES.json')
    for r in archived:
        covered=[z for z in failed if z['base']==r['base'] and z['low'] in r['low_labels']]
        assert len(covered)==r['orbit_size']
        assert all(z['s']==r['projection']['private_size_multiset'] and bool(z['common_pure_count'])==r['projection']['same_pure_high_edge'] for z in covered)
    result={'status':'PASS','catalogue_source':str(CAT.relative_to(ROOT)),
            'catalogue_families':374,'candidate_markings':374*84,'excluded_low_trace':excluded_low,
            'excluded_negative_multiplicity':excluded_negative,'labels':140,'families':81,'colored_orbits_verified':105,
            'transported_layouts_checked':140,'raw_labels_checked':140,'raw_position_rows':3500,
            'strict_raw_labels':128,'maximum_strict_raw_bound':max(strict_values),'failed_labels':12,
            'failed_classes':dict(classes),'failed_with_zero':zero,'cpu_seconds':process_time()-started,
            'method':'independent set/pair completion and residual degree filtering; explicit verified permutation composition; 35 edge stubs and falling-factorial injections for raw ABC',
            'not_performed':['DP','quota deductions','layout search','H enumeration','catalogue regeneration','proof of actual-H selection lemma']}
    (HERE/'RESULT.json').write_text(json.dumps(stringify(result),indent=2)+'\n')
    (HERE/'ROWS.json').write_text(json.dumps(stringify(probability),indent=2)+'\n')
    (HERE/'TRANSPORT.json').write_text(json.dumps(stringify(transport_records),indent=2)+'\n')
    print(json.dumps(stringify(result)))

if __name__=='__main__':main()
