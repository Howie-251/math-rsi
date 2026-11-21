"""Linux full physical order, true pair ranks/P, all packets and weak8 DP."""
import collections
import hashlib
import itertools as it
import json
from pathlib import Path
import platform
import shutil
import time

assert platform.system() == 'Linux'
HERE = Path(__file__).resolve().parent
PRIOR = HERE / 'h13-exact-wlog-third01'
OUT = HERE / 'h13-physical-all02'


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def main():
    began = time.monotonic()
    OUT.mkdir(exist_ok=False)
    prior = json.loads((PRIOR / 'manifest.json').read_text())
    assert sha(PRIOR / 'formula.cnf') == prior['cnf_sha256'] == '2c61758537b7820b7afca5888c59f7c19cc6a0447994a8f8cd953d032b2fc3a1'
    meta = json.loads((PRIOR / 'inputs/base-metadata.json').read_text())
    shapes = meta['universe']['column_heights']
    cells = [{(x,y) for x in range(1,5) for y in range(1,s[x-1]+1)} for s in shapes]
    lt = {(a,b) for a in range(70) for b in range(70) if cells[a] < cells[b]}
    old_labels = {tuple(r['pair']):{tuple(c['cell']):c['variable'] for c in r['choices']} for r in meta['labels']}
    old_colors = {tuple(r['triple']):r['variable'] for r in meta['colors']}
    variables = prior['variables']
    orders, labels, colors, coordinates, witnesses, reach4, reach5 = {}, {}, {}, {}, {}, {}, {}
    counts = collections.Counter()
    extra = OUT / 'extension.cnf'
    stream = extra.open('w')

    def fresh():
        nonlocal variables
        variables += 1
        return variables

    def neg(literal):
        return not literal if type(literal) is bool else -literal

    def emit(clause, category):
        if any(x is True for x in clause):
            return
        clause = [x for x in clause if x is not False]
        assert clause and all(type(x) is int and x for x in clause)
        if any(-x in clause for x in clause):
            return
        clause = list(dict.fromkeys(clause))
        stream.write(' '.join(map(str,clause))+' 0\n')
        counts[category] += 1

    for a,b in it.combinations(range(70),2):
        if (a,b) not in lt and (b,a) not in lt:
            orders[a,b] = fresh()
    assert len(orders) == 721

    def order(a,b):
        if (a,b) in lt:
            return True
        if (b,a) in lt:
            return False
        return orders[a,b] if a < b else -orders[b,a]

    def compatible(group):
        return all((group[j],group[i]) not in lt for i in range(len(group)) for j in range(i+1,len(group)))

    def extensions(size):
        for group in it.combinations(range(70),size):
            for permutation in it.permutations(group):
                if compatible(permutation):
                    yield permutation

    for a,b,c in it.combinations(range(70),3):
        emit([neg(order(a,b)),neg(order(b,c)),order(a,c)],'total-order-no-cycle')
        emit([order(a,b),order(b,c),neg(order(a,c))],'total-order-no-cycle')
    for a in range(70):
        for b in range(70):
            difference = cells[b]-cells[a]
            if a == b or not difference:
                continue
            choices = labels[a,b] = {cell:fresh() for cell in sorted(difference)}
            emit([a+1,b+1,neg(order(a,b))]+list(choices.values()),'physical-pair-exists')
            for first,second in it.combinations(choices.values(),2):
                emit([-first,-second],'physical-pair-unique')
            for cell,flag in choices.items():
                emit([-flag,-a-1],'physical-pair-occupied')
                emit([-flag,-b-1],'physical-pair-occupied')
                emit([-flag,order(a,b)],'physical-pair-order')
                if (a,b) in old_labels:
                    emit([-flag,old_labels[a,b][cell]],'physical-old-pair-bridge')
            for col in range(2):
                for value in range(1,5):
                    group = [flag for cell,flag in choices.items() if cell[col] == value]
                    if not group:
                        continue
                    coordinate = coordinates[a,b,col,value] = fresh()
                    emit([-coordinate]+group,'coordinate-exists')
                    for flag in group:
                        emit([-flag,coordinate],'coordinate-forward')
    assert len(labels) == 3136 and sum(map(len,labels.values())) == 11440
    for group in it.combinations(range(70),3):
        colors[group] = old_colors[group] if group in old_colors else fresh()

    def color(a,b,c):
        return colors[tuple(sorted((a,b,c)))]

    for b in range(70):
        corners = [cell for cell in cells[b] if not any(cell != other and cell[0] <= other[0] and cell[1] <= other[1] for other in cells[b])]
        for cell in corners:
            flags = [choices[cell] for (a,target),choices in labels.items() if target == b and cell in choices]
            emit([b+1]+flags,'true-P-corner-generator')

    support = collections.defaultdict(list)
    triple_count = 0
    for a,b,c in extensions(3):
        triple_count += 1
        colvar = color(a,b,c)
        for first,p in labels[a,b].items():
            for second,q in labels[b,c].items():
                if second[0] <= first[0]:
                    emit([-p,-q,colvar],'all-physical-blue-growth')
                if second[1] <= first[1]:
                    emit([-p,-q,-colvar],'all-physical-red-growth')
        for col in range(2):
            for value in range(1,4):
                incoming = coordinates.get((a,b,col,value))
                outgoing = coordinates.get((b,c,col,value+1))
                if incoming is None or outgoing is None:
                    continue
                flag = witnesses[a,b,c,col,value] = fresh()
                emit([-flag,incoming],'exact-rank-witness-prior')
                emit([-flag,colvar if col else -colvar],'exact-rank-witness-color')
                support[b,c,col,value+1].append(flag)
        for col in range(2):
            reach4[a,b,c,col] = fresh()
    assert triple_count == 108696
    for key,coordinate in coordinates.items():
        if key[3] > 1:
            emit([-coordinate]+support[key],'exact-rank-max-attainment')
    for a,b in labels:
        for col in range(2):
            reach5[a,b,col] = fresh()
    for a,b in labels:
        emit([-reach5[a,b,0],-reach5[a,b,1]],'all-physical-no-same-end-five')
    valid = {(0,0,0,0),(0,0,0,1),(0,0,1,1),(0,1,1,1),
             (1,1,1,1),(1,1,1,0),(1,1,0,0),(1,0,0,0)}
    invalid = [bits for bits in it.product((0,1),repeat=4) if bits not in valid]
    quad_count = 0
    for a,t,u,v in extensions(4):
        quad_count += 1
        gate = [a+1,t+1,u+1,v+1,neg(order(a,t)),neg(order(t,u)),neg(order(u,v))]
        quartet = [color(*triple) for triple in ((a,t,u),(a,t,v),(a,u,v),(t,u,v))]
        for bits in invalid:
            emit(gate+[-flag if bit else flag for flag,bit in zip(quartet,bits)],'all-physical-packet')
        for col in range(2):
            c1,c2 = color(a,t,u),color(t,u,v)
            emit(gate+[-c1 if col else c1,-c2 if col else c2,reach4[a,u,v,col]],'all-physical-path4-forward')
            emit([v+1,neg(order(u,v)),-reach4[a,t,u,col],-c2 if col else c2,reach5[a,v,col]],'all-physical-path5-forward')
        if quad_count % 250000 == 0:
            print(json.dumps({'building_quads':quad_count,'clauses_now':sum(counts.values()),'seconds':time.monotonic()-began}),flush=True)
    assert quad_count == 3127356
    stream.close()
    clauses = prior['clauses']+sum(counts.values())
    cnf = OUT / 'formula.cnf'
    with cnf.open('w') as target, (PRIOR / 'formula.cnf').open() as source:
        target.write(f'p cnf {variables} {clauses}\n')
        assert source.readline().startswith('p cnf ')
        shutil.copyfileobj(source,target)
        with extra.open() as extension:
            shutil.copyfileobj(extension,target)
    structure = {'orders':[[list(k),v] for k,v in orders.items()],
                 'labels':[[list(k),[[list(cell),flag] for cell,flag in choices.items()]] for k,choices in labels.items()],
                 'colors':[[list(k),v] for k,v in colors.items()],
                 'coordinates':[[list(k),v] for k,v in coordinates.items()],
                 'witnesses':[[list(k),v] for k,v in witnesses.items()],
                 'reach4':[[list(k),v] for k,v in reach4.items()],
                 'reach5':[[list(k),v] for k,v in reach5.items()]}
    (OUT / 'structure.json').write_text(json.dumps(structure,separators=(',',':')))
    (OUT / 'source').mkdir()
    sources = []
    for name in ['physical_build.py','physical_calibrate.py','physical_audit.py','physical_run.py','physical_launch.py','physical_prepare.py','physical_status.py']:
        path = OUT / 'source' / name
        shutil.copy2(HERE/name,path)
        sources.append({'source':str(HERE/name),'snapshot':str(path),'sha256':sha(path)})
    manifest = {'status':'PREPARED_H13_FULL_PHYSICAL_ORDER_TRUE_P_PACKET_WEAK8',
                'prior_query':str(PRIOR),'prior_cnf_sha256':prior['cnf_sha256'],
                'prior_clauses':prior['clauses'],'prior_variables':prior['variables'],
                'variables':variables,'clauses':clauses,'categories':dict(counts),
                'cnf_sha256':sha(cnf),'extension_sha256':sha(extra),
                'structure_sha256':sha(OUT/'structure.json'),'sources':sources,
                'oriented_pairs':len(labels),'physical_triples':triple_count,'physical_quads':quad_count,
                'upper_budget_literal':-70229,'build_seconds':time.monotonic()-began,
                'scope':'All13 holes free; one common physical total order; all pairs/colors/packets; exact max ranks; canonical P corners; actual same-end5/5 DP'}
    (OUT/'manifest.json').write_text(json.dumps(manifest,indent=2))
    print(json.dumps(manifest),flush=True)


if __name__ == '__main__':
    main()
