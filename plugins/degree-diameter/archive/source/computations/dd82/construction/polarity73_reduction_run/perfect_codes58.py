"""One bounded exact-cover diagnostic for the saved two-fiber58 sample."""
import json
from pathlib import Path
import time

HERE = Path(__file__).resolve().parent
MAX_NODES = 1_000_000
MAX_CPU_SECONDS = 5.0
# Leave a small part of the total CPU allowance for the finite output receipt.
SEARCH_CPU_SECONDS = 4.5


def main():
    started_cpu, started_wall = time.process_time(), time.monotonic()
    output = HERE / 'perfect_codes58.json'
    assert not output.exists(), 'Preserve the one authorized diagnostic'
    examples = json.loads((HERE / 'two_fiber_examples.json').read_text())
    sample = next(row for row in examples['samples'] if row['n'] == 58)
    survivors, outside = set(sample['survivors']), sorted(sample['external_survivors'])
    adjacency = [set() for _ in range(73)]
    with (HERE / 'geometry.edges').open() as source:
        assert source.readline().split() == ['73', '324']
        for line in source:
            a, b = map(int, line.split())
            if a in survivors and b in survivors:
                adjacency[a].add(b)
                adjacency[b].add(a)
    assert len(outside) == 49
    position = {vertex: index for index, vertex in enumerate(outside)}
    outside_set = set(outside)
    masks = []
    for vertex in outside:
        closed = {vertex} | (adjacency[vertex] & outside_set)
        assert len(closed) == 7
        masks.append(sum(1 << position[x] for x in closed))
    centers_for = [[center for center, mask in enumerate(masks) if mask & (1 << point)]
                   for point in range(49)]
    assert all(len(row) == 7 for row in centers_for)
    bad_partners = {x: {y for y in outside_set - {x}
                       if y not in adjacency[x] and not (adjacency[x] & adjacency[y])}
                    for x in outside}
    full_mask = (1 << 49) - 1
    codes, seen, nodes, truncated, stop_reason = [], set(), 0, False, None

    def visit(covered, selected):
        nonlocal nodes, truncated, stop_reason
        if truncated:
            return
        if nodes >= MAX_NODES:
            truncated, stop_reason = True, 'NODE_LIMIT'
            return
        if time.process_time() - started_cpu >= SEARCH_CPU_SECONDS:
            truncated, stop_reason = True, 'CPU_LIMIT_WITH_OUTPUT_RESERVE'
            return
        nodes += 1
        if covered == full_mask:
            assert len(selected) == 7
            code = tuple(sorted(outside[center] for center in selected))
            assert code not in seen, 'Smallest-uncovered-point branching should have unique leaves'
            seen.add(code)
            code_set = set(code)
            counts = {c: len(bad_partners[c] - code_set) for c in code}
            unresolved = all(count <= 6 for count in counts.values())
            codes.append(dict(vertices=list(code), old_bad_partners_outside_code=counts,
                              passes_six_matching_incidence_necessary_bound=unresolved))
            return
        assert len(selected) < 7
        uncovered = full_mask ^ covered
        least = (uncovered & -uncovered).bit_length() - 1
        for center in centers_for[least]:
            if masks[center] & covered:
                continue
            visit(covered | masks[center], selected + (center,))
            if truncated:
                return

    visit(0, ())
    codes.sort(key=lambda row: row['vertices'])
    unresolved_codes = [row['vertices'] for row in codes
                        if row['passes_six_matching_incidence_necessary_bound']]
    result = dict(status='TRUNCATED' if truncated else 'EXHAUSTIVE_COMPLETE',
        scope='Only the saved n58 sample D=C_a union C_b union {a}; no other deletion set',
        a=sample['a'], b=sample['b'], deletion=sample['deletion'],
        outside=outside, closed_neighborhoods=49, neighborhood_size=7,
        algorithm='Exact cover: smallest uncovered point, every containing center whose '
                  'closed neighborhood is disjoint from the covered set; depth seven; no symmetry assumptions',
        node_limit=MAX_NODES, cpu_limit_seconds=MAX_CPU_SECONDS,
        search_cpu_limit_with_output_reserve=SEARCH_CPU_SECONDS,
        nodes=nodes, truncated=truncated, stop_reason=stop_reason,
        codes=codes, perfect_codes_found=len(codes),
        unresolved_codes=unresolved_codes, unresolved_code_count=len(unresolved_codes),
        necessary_test='For each code center c, at most six old bad partners in O minus code: '
                       'only the new matching edges at its six old O-neighbors can cover these pairs',
        full_graph_constructed=False, solver_calls=0, automatic_continuations=0,
        cpu_seconds_before_output=time.process_time() - started_cpu,
        wall_seconds_before_output=time.monotonic() - started_wall)
    output.write_text(json.dumps(result, indent=2) + '\n')
    elapsed_cpu, elapsed_wall = time.process_time() - started_cpu, time.monotonic() - started_wall
    assert elapsed_cpu < MAX_CPU_SECONDS, 'The diagnostic exceeded its total CPU allowance'
    print(json.dumps(dict(status=result['status'], nodes=nodes, perfect_codes_found=len(codes),
        unresolved_code_count=len(unresolved_codes), cpu_seconds=elapsed_cpu,
        wall_seconds=elapsed_wall, stop_reason=stop_reason, solver_calls=0), indent=2))


if __name__ == '__main__':
    main()
