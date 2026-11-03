"""Read only the official degree-60 records; check pair orbits, not graphs."""
from pathlib import Path
import itertools
import json
import os
import re
import resource
import time
import urllib.request

URL = 'https://raw.githubusercontent.com/gap-packages/primgrp/master/data/gps1.g'
OUT = Path(__file__).resolve().parent / 'primitive60_catalog_run'


def cycle_perm(text, n=60):
    p = list(range(n))
    for cycle in re.findall(r'\(([0-9,]+)\)', text):
        c = [int(x)-1 for x in cycle.split(',')]
        for a, b in zip(c, c[1:]+c[:1]):
            p[a] = b
    assert sorted(p) == list(range(n))
    return p


def pair_orbits(gens):
    remaining = set(itertools.combinations(range(60), 2))
    orbits = []
    while remaining:
        initial = min(remaining)
        orbit, queue = {initial}, [initial]
        for u, v in queue:
            for g in gens:
                pair = tuple(sorted((g[u], g[v])))
                if pair not in orbit:
                    orbit.add(pair)
                    queue.append(pair)
        assert orbit <= remaining
        remaining -= orbit
        degrees = [0]*60
        for u, v in orbit:
            degrees[u] += 1
            degrees[v] += 1
        assert len(set(degrees)) == 1
        orbits.append(dict(representative=initial, size=len(orbit),
                           valency=degrees[0], edges=sorted(orbit)))
    assert sum(x['size'] for x in orbits) == 1770
    return orbits


def main():
    os.sched_setaffinity(0, {min(os.sched_getaffinity(0))})
    resource.setrlimit(resource.RLIMIT_CPU, (5, 6))
    cpu, wall = time.process_time(), time.monotonic()
    OUT.mkdir(exist_ok=True)
    assert not (OUT/'result.json').exists(), 'One catalog check, no repetition'
    full = urllib.request.urlopen(URL, timeout=20).read().decode()
    start = full.index('PRIMGRP[60]:=')
    stop = full.index('\n];', start)+3
    block = full[start:stop]+'\n'
    (OUT/'PRIMGRP_60.records.g').write_text(block)
    lines = block.splitlines()[1:-1]
    assert len(lines) == 9
    groups = []
    for line in lines[:5]:
        split = line.index(',[(')
        metadata = json.loads(line[:split]+']')
        gen_text = line[split+2:-3]
        # Restore parentheses removed by splitting the two permutation entries.
        gens = [cycle_perm('('+x.strip('()')+')') for x in gen_text.split('),(')]
        groups.append(dict(index=metadata[0], name=metadata[6],
                           group_order=metadata[1], source_subdegrees=metadata[4],
                           generator_origin='literal official permutation records',
                           generators=gens))
    assert lines[5:] == ['["PSL",2,59],', '["PGL",2,59],',
                         '["Alt"],', '["Sym"],']
    # Expand the four official family descriptors in their standard actions.
    p = 59
    translation = [(x+1) % p for x in range(p)]+[p]
    inversion = [p]+[(-pow(x, -1, p)) % p for x in range(1, p)]+[0]
    nonsquare = next(a for a in range(2, p) if pow(a, (p-1)//2, p) == p-1)
    scaling = [nonsquare*x % p for x in range(p)]+[p]
    alternating = [cycle_perm('('+','.join(map(str,range(1,60)))+')'),
                   cycle_perm('(58,59,60)')]
    symmetric = [cycle_perm('('+','.join(map(str,range(1,61)))+')'),
                 cycle_perm('(1,2)')]
    for index, name, gens in [(6,'PSL(2,59)',[translation,inversion]),
                             (7,'PGL(2,59)',[translation,inversion,scaling]),
                             (8,'A60',alternating), (9,'S60',symmetric)]:
        groups.append(dict(index=index, name=name, source_subdegrees=[[59,1]],
                           generator_origin='standard expansion of official family descriptor',
                           generators=gens))
    for g in groups:
        orbit = {0}
        queue = [0]
        for x in queue:
            for p in g['generators']:
                if p[x] not in orbit:
                    orbit.add(p[x]); queue.append(p[x])
        assert len(orbit) == 60
        g['pair_orbits'] = pair_orbits(g['generators'])
        g['orbital_valencies'] = sorted(x['valency'] for x in g['pair_orbits'])
        assert min(g['orbital_valencies']) >= 12
    result = dict(complete=True, source_url=URL, records=9, groups=groups,
                  graph_searches=0, cpu_budget_seconds=5, threads=1,
                  cpu_seconds=time.process_time()-cpu, wall_seconds=time.monotonic()-wall)
    (OUT/'result.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k!='groups'}))
    print(json.dumps([dict(index=g['index'],name=g['name'],valencies=g['orbital_valencies']) for g in groups]))


if __name__ == '__main__':
    main()
