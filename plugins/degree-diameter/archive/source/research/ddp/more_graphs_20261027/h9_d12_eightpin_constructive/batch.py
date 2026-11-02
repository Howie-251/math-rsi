"""Bounded constructive four-anchor covers; no MIP or repeated base audit."""
from pathlib import Path
import argparse
import json
import resource
import subprocess
import time

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
CAMPAIGN = OUT.parent
NATIVE = CAMPAIGN / 'h9_d12_eightpin_extensions/cover'


def cover_four(masks, targets, seconds):
    """Choose two greedy prefixes and exactly complete each with <=two masks.

    This is a bounded constructive search, not an infeasibility decision.
    """
    start = time.process_time()
    full = (1 << targets) - 1
    count = len(masks)
    coverers = [0] * targets
    for i, mask in enumerate(masks):
        bit = 1 << i
        while mask:
            low = mask & -mask
            coverers[low.bit_length() - 1] |= bit
            mask -= low
    order = sorted(range(targets), key=lambda j: coverers[j].bit_count())
    all_candidates = (1 << count) - 1
    firsts = sorted(range(count), key=lambda i: (-masks[i].bit_count(), i))[:32]
    prefixes = 0
    third_trials = 0
    for first in firsts:
        left = full & ~masks[first]
        seconds_list = sorted(range(count), key=lambda i: (-(masks[i] & left).bit_count(), i))[:16]
        for second in seconds_list:
            if second == first:
                continue
            prefixes += 1
            left2 = left & ~masks[second]
            if not left2:
                return [first, second], prefixes, third_trials, False
            pivot = next(j for j in order if (left2 >> j) & 1)
            # One of the two final masks must cover this pivot. Completeness
            # holds for each tested prefix; prefix selection is heuristic.
            thirds = coverers[pivot] & ~(1 << first) & ~(1 << second)
            while thirds:
                if third_trials % 64 == 0 and time.process_time() - start > seconds:
                    return None, prefixes, third_trials, True
                low = thirds & -thirds
                thirds -= low
                third = low.bit_length() - 1
                third_trials += 1
                left3 = left2 & ~masks[third]
                if not left3:
                    return [first, second, third], prefixes, third_trials, False
                fourths = all_candidates & ~(1 << first) & ~(1 << second) & ~low
                for j in order:
                    if (left3 >> j) & 1:
                        fourths &= coverers[j]
                        if not fourths:
                            break
                if fourths:
                    return [first, second, third, (fourths & -fourths).bit_length() - 1], prefixes, third_trials, False
    return None, prefixes, third_trials, False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, required=True)
    args = parser.parse_args()
    resource.setrlimit(resource.RLIMIT_CPU, (48, 50))
    start = time.process_time()
    source = args.source.resolve()
    with source.open() as stream:
        initial_n, initial_m = map(int, stream.readline().split())
        adj = [[] for _ in range(initial_n)]
        for line in stream:
            u, v = map(int, line.split())
            adj[u].append(v)
            adj[v].append(u)
    current_file = source
    current_m = initial_m
    frozen = json.loads((CAMPAIGN / 'h9_d12_eightpin_extensions/PREDICTION.json').read_text())
    prediction = dict(source_graph=str(source.relative_to(ROOT)), source_n=initial_n,
        prediction='At least one retained eight-pin Q-line may admit four anchors found by greedy-prefix/exact-two-tail search; complete actual R4 is required before accepting.',
        rule='Frozen 13 eight-pin sets; at most32 first anchors and16 second anchors, each followed by exact two-tail. Four CPU seconds per eligible item. No MIP.',
        no_hit_meaning='Only this finite constructive search failed; four-anchor feasibility remains open.',
        scope_items=13, per_item_search_CPU_seconds=4, old_base_reaudited=False)
    (OUT / 'PREDICTION.json').write_text(json.dumps(prediction, ensure_ascii=False, indent=2) + '\n')
    (OUT / 'items').mkdir(exist_ok=True)
    (OUT / 'graphs').mkdir(exist_ok=True)
    rows, accepted = [], []
    for item in frozen['items']:
        pins = item['mandatory_pins']
        row = dict(pool_index=item['pool_index'], source_n=len(adj), mandatory_pins=pins)
        if any(len(adj[v]) >= 12 for v in pins):
            row['status'] = 'CURRENT_DEGREE_BLOCKED'
            rows.append(row)
            continue
        prefix = OUT / 'items' / f"pool{item['pool_index']}_n{len(adj)}"
        pinfile = Path(str(prefix) + '.pins.txt')
        pinfile.write_text(' '.join(map(str, pins)) + '\n')
        subprocess.run([str(NATIVE), 'prepare', str(current_file), str(pinfile), str(prefix)], check=True)
        prepared = json.loads(Path(str(prefix) + '.json').read_text())
        row['mandatory_R4_missing_count'] = prepared['missing_count']
        anchors = prepared.get('exact_anchors') if prepared.get('exact_one_or_two_found') else None
        if prepared['missing_count'] == 0:
            anchors = []
        if anchors is None:
            word_bytes = 8 * prepared['mask_words_per_row']
            raw = Path(str(prefix) + '.masks.u64.bin').read_bytes()
            masks = [int.from_bytes(raw[i:i + word_bytes], 'little') for i in range(0, len(raw), word_bytes)]
            search_start = time.process_time()
            chosen, prefixes, trials, limited = cover_four(masks, prepared['missing_count'], 4)
            row.update(search_CPU_seconds=time.process_time() - search_start, tested_prefixes=prefixes,
                       third_masks_tested=trials, search_CPU_limit_reached=limited)
            if chosen is not None:
                anchors = [prepared['representatives'][j] for j in chosen]
        if anchors is None:
            row['status'] = 'NO_HIT_BOUNDED_CONSTRUCTIVE_SEARCH_FEASIBILITY_OPEN'
        else:
            neighbors = sorted(pins + anchors)
            assert len(neighbors) == len(set(neighbors)) <= 12
            pinfile.write_text(' '.join(map(str, neighbors)) + '\n')
            selected = Path(str(prefix) + '_selected')
            subprocess.run([str(NATIVE), 'verify', str(current_file), str(pinfile), str(selected)], check=True)
            check = json.loads(Path(str(selected) + '.json').read_text())
            assert check['status'] == 'FULL_SELECTED_R4_CHECK_COMPLETE' and check['missing_count'] == 0
            row.update(status='ACCEPTED_BY_COMPLETE_CURRENT_R4', source_m=current_m, new_vertex=len(adj),
                full_neighbor_set=neighbors, anchors=anchors, new_n=len(adj) + 1,
                old_degrees=[len(adj[v]) for v in neighbors], covered_count=len(adj), missing_count=0)
            adj.append(neighbors)
            for v in neighbors:
                adj[v].append(len(adj) - 1)
            current_m += len(neighbors)
            current_file = OUT / 'graphs' / f'graph_d12_D5_n{len(adj)}.edges'
            with current_file.open('w') as stream:
                stream.write(f'{len(adj)} {current_m}\n')
                for u, ns in enumerate(adj):
                    for v in ns:
                        if u < v:
                            stream.write(f'{u} {v}\n')
            row['graph_file'] = str(current_file.relative_to(ROOT))
            accepted.append(row)
            print('HIT ' + json.dumps(row), flush=True)
        rows.append(row)
    child = resource.getrusage(resource.RUSAGE_CHILDREN)
    result = dict(initial_n=initial_n, initial_m=initial_m, final_n=len(adj), final_m=current_m,
        final_graph=str(current_file.relative_to(ROOT)), accepted_extensions=len(accepted), records=accepted,
        rows=rows, status='COMPLETE_FROZEN_CONSTRUCTIVE_PASS', pending=[],
        CPU_seconds=time.process_time() - start + child.ru_utime + child.ru_stime,
        old_base_reaudited=False, all_source_BFS_executed=0, full_coverage_acceptance=True,
        general_family_excluded=False)
    (OUT / 'RESULT.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n')
    print('TERMINAL ' + json.dumps({k: v for k, v in result.items() if k not in ['rows', 'records']}), flush=True)


if __name__ == '__main__':
    main()
