"""Check frozen binding, exact full-domain dimensions and every DIMACS line."""
import hashlib
import json
from pathlib import Path
import platform
import time

assert platform.system()=='Linux'
HERE=Path(__file__).resolve().parent
OUT=HERE/'h13-physical-all02'


def sha(path):
    h=hashlib.sha256()
    with path.open('rb') as source:
        for block in iter(lambda:source.read(1<<20),b''):
            h.update(block)
    return h.hexdigest()


def main():
    began=time.monotonic()
    manifest=json.loads((OUT/'manifest.json').read_text())
    for binding in manifest['sources']:
        assert sha(Path(binding['snapshot']))==binding['sha256']
    assert sha(Path(manifest['prior_query'])/'formula.cnf')==manifest['prior_cnf_sha256']
    assert sha(OUT/'formula.cnf')==manifest['cnf_sha256']
    assert sha(OUT/'extension.cnf')==manifest['extension_sha256']
    assert sha(OUT/'structure.json')==manifest['structure_sha256']
    structure=json.loads((OUT/'structure.json').read_text())
    assert len(structure['orders'])==721 and len(structure['labels'])==3136
    assert sum(len(choices) for pair,choices in structure['labels'])==11440
    assert len(structure['colors'])==54740 and len(structure['reach4'])==2*108696
    assert len(structure['reach5'])==2*3136
    counts=manifest['categories']
    assert counts['all-physical-packet']==8*3127356
    assert counts['all-physical-path4-forward']==2*3127356
    assert counts['all-physical-path5-forward']==2*3127356
    assert counts['all-physical-no-same-end-five']==3136
    clauses=upper=0
    maximum=0
    with (OUT/'formula.cnf').open() as source:
        assert source.readline().strip()==f"p cnf {manifest['variables']} {manifest['clauses']}"
        for line in source:
            row=list(map(int,line.split()))
            assert row and row[-1]==0 and all(row[:-1])
            clauses+=1
            maximum=max(maximum,max(map(abs,row[:-1])))
            upper+=row==[-70229,0]
    assert maximum==manifest['variables'] and clauses==manifest['clauses'] and upper==1
    result={'status':'PASS_PHYSICAL_FULL_DIMENSIONS_BINDING_AND_EVERY_DIMACS_LINE',
            'variables':maximum,'clauses':clauses,'cnf_sha256':manifest['cnf_sha256'],
            'all_ordered_triples':108696,'all_ordered_quads':3127356,
            'all_packet_clauses':counts['all-physical-packet'],'upper_budget_literal':-70229,
            'seconds':time.monotonic()-began,
            'semantic_rebuild':'Separate independent reconstruction is not claimed by this author dimension audit.'}
    (OUT/'audit.json').write_text(json.dumps(result,indent=2))
    print(json.dumps(result),flush=True)


if __name__=='__main__':
    main()
