#!/usr/bin/env python3
"""Apply the parent's one fixed Q64 phase selection, without generating graphs."""
from pathlib import Path
import ast
import json
import random
import time

begin = time.process_time()
here = Path(__file__).resolve().parent
assert not (here / 'run.json').exists()
source = here.parent / 'nonabelian4_256_capacity' / 'q64' / 'survivors.json'
topology = json.loads((source.parent.parent / 'topology.json').read_text())
rows = json.loads(source.read_text())
pool = sorted(row['phase_mask'] for row in rows if row['minimum_capacity'] == 52)
assert len(pool) == len(set(pool)) == 324 and 1205 in pool
codes = [1205] + random.Random(20261027064).sample([c for c in pool if c != 1205], 63)
policy = {k: topology[k] for k in ['edge_u', 'edge_v', 'tree_edge_indices', 'free_edge_indices']}
policy.update(group_name='Q64', capacity_source=str(source.relative_to(here.parent)),
              required_minimum_capacity=52, eligible_mask_count=len(pool), eligible_masks_in_order=pool,
              selection='mask1205 first; sample63 without replacement from remaining ascending masks',
              selection_seed=20261027064, initial_phase_codes=codes,
              translation_seed=20261027066, kick_seed=20261027065)
(here / 'start_policy.json').write_text(json.dumps(policy, indent=2) + '\n')
(here / 'group_definition.json').write_text(json.dumps({
    'name': 'Q64', 'twist': 16, 'encoding': 'x+32*s',
    'product': '(x+(-1)^s*y+16*s*t mod32,s xor t)',
    'inverse': '(-x,0) if s=0; (x+16,1) if s=1',
    'parent_selection': 'Q64 only, no D64 actual search',
}, indent=2) + '\n')
ast.parse((here / 'run.py').read_text())
preparation = json.loads((here / 'preparation.json').read_text())
preparation.update(status='SELECTED_READY_TO_RUN', group_selected=True, selected_group='Q64',
                   starts_generated=False, compiled=False, search_started=False,
                   CPU_seconds=preparation['CPU_seconds'] + time.process_time() - begin)
(here / 'preparation.json').write_text(json.dumps(preparation, indent=2) + '\n')
print(json.dumps({'status': 'SELECTED_READY_TO_RUN', 'group': 'Q64', 'eligible_masks': len(pool),
                  'ordered_initial_phase_codes': codes, 'CPU_seconds': preparation['CPU_seconds']}))
