#!/usr/bin/env python3
"""Replay one of the 50 saved graph constructions from the bundled small inputs.

The dispatch uses the original delivery wrappers and production programs. The
saved_f9_centers_copy branch only copies immutable source neighbor rows selected
by the original PARAMETERS; it introduces no search or new field/GQ rule.
No BFS, Lean build, network request, package installation, or hash is performed.
"""
import argparse
import csv
import importlib.util
import itertools
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True

HERE = Path(__file__).resolve().parent
STAGE = Path('research/ddp/two_successful_methods_20261101')
TRANSFER = STAGE / 'retained_edge_transfer'
F9 = STAGE / 'affine_field_conditions/r6_schreier78_controller/f9_degree54'
Q8 = TRANSFER / 'even_q8_gq_source80_81'
Q8_COPY = Q8 / 'balanced_full_ovoid_copy82'
Q8_DELTA = Q8_COPY / 'diagonal_fill_reallocation'
GQ7 = TRANSFER / 'opposite_gq77_spread64'


def read_json(path):
    return json.loads(path.read_text())


def cases():
    with (HERE / 'cases.csv').open(encoding='utf-8', newline='') as stream:
        return {row['case']: row for row in csv.DictReader(stream)}


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class Replayer:
    def __init__(self, root, cxx, budget):
        self.root, self.cxx, self.budget = root, cxx, budget
        self.rows = cases()
        self.modules = {}

    def wrapper(self, name):
        if name not in self.modules:
            module = load_module(HERE / 'original_wrappers' / (name + '.py'), name)
            # Adapt only original wrapper path constants to the new output tree.
            module.HERE = self.root
            module.STAGE = self.root / STAGE
            module.BASE = self.root / TRANSFER
            module.G64 = self.root / GQ7
            module.G54 = self.root / F9
            self.modules[name] = module
        return self.modules[name]

    def wrapper_main(self, name, order, output):
        saved = sys.argv
        try:
            sys.argv = [name, '--order', str(order), '--output', str(output)]
            self.wrapper(name).main()
        finally:
            sys.argv = saved

    def cpp(self, source):
        folder = self.root / '.compiled'
        folder.mkdir(exist_ok=True)
        binary = folder / ('_'.join(Path(source).parts[-4:]).replace('.', '_'))
        if not binary.exists():
            subprocess.run([self.cxx, '-O3', '-std=c++17', str(self.root / source),
                            '-o', str(binary)], check=True)
        return binary

    def execute(self, command, cwd=None):
        subprocess.run([str(part) for part in command], cwd=cwd, check=True)

    def order(self, n, degree=None):
        matches = [row for row in self.rows.values()
                   if int(row['vertices']) == n and
                   (degree is None or int(row['degree']) == degree)]
        if len(matches) != 1:
            raise ValueError('Use the full case ID for an ambiguous order: ' + str(n))
        return matches[0]

    def ensure_order(self, n, degree=None):
        return self.ensure(self.order(n, degree)['case'])

    def ensure(self, key):
        row = self.rows[key]
        n = int(row['vertices'])
        output = self.root / row['source_edge_file']
        if output.is_file():
            return output
        output.parent.mkdir(parents=True, exist_ok=True)
        adapter = row['adapter']

        if adapter == 'original_f5':
            source = self.root / 'research/ddp/refresh_20261029/f5_full_d20_D3/generate.py'
            module = load_module(source, 'saved_f5_generator')
            module.generate(output, source.parent / 'PARAMETERS.json', None)
        elif adapter == 'original_two_methods':
            if n in (3900, 4125):
                self.ensure_order(3750)
            elif n in (3984, 4192, 4336):
                self.ensure_order(3840)
            self.wrapper_main('two_methods', n, output)
        elif adapter == 'original_gq_spread':
            self.wrapper_main('gq_spread', n, output)
        elif adapter == 'original_affine_clone':
            self.wrapper_main('affine_clone', n, output)
        elif adapter == 'original_d4_producer':
            self.execute([sys.executable, output.parent / 'produce.py'])
        elif adapter == 'original_d17_producer':
            source = self.root / TRANSFER / 'published_d16_1920_source_transfer_gate/produce_degree17_plane96.py'
            self.execute([sys.executable, source])
        elif adapter == 'original_q4_delta_producer':
            self.ensure_order(7531)
            self.execute([sys.executable, output.parent / 'produce.py'])
        elif adapter == 'saved_f9_centers_copy':
            source = self.ensure_order(56862)
            parameters = read_json(self.root / row['parameters'])
            if n == 57834:
                centers = parameters['base_center_labels'] * 2
            else:
                centers = parameters['base_center_labels'] * (int(row['degree']) - 54)
            self.saved_neighbor_copy(source, 56862, centers, output, row)
        elif adapter == 'original_p33_producer':
            source = self.ensure_order(160050)
            folder = output.parent.parent
            (folder / 'graphs').mkdir(exist_ok=True)
            self.execute([self.cpp(folder.relative_to(self.root) / 'produce.cpp'),
                          source, self.budget], cwd=folder)
        elif adapter == 'original_q8_source_producer':
            mode = 'derived' if n == 327744 else 'balanced'
            self.execute([self.cpp(Q8 / 'produce_sources.cpp'), mode,
                          output.parent / 'TABLES_INPUT.txt', output.parent,
                          self.budget])
        elif adapter == 'original_q8_copy_producer':
            source = self.ensure_order(342290)
            self.execute([self.cpp(Q8_COPY / 'produce.cpp'), source, self.budget],
                         cwd=self.root / Q8_COPY)
        elif adapter == 'original_q8_delta_producer':
            source = self.ensure_order(346515)
            self.execute([self.cpp(Q8_DELTA / 'produce.cpp'), source, output,
                          self.root / Q8_DELTA / 'DELTA_INPUT.txt'])
        elif adapter == 'original_q8_second_copy_producer':
            source = self.ensure_order(346516)
            self.execute([self.cpp(Q8_DELTA / 'multiplicity2_degree83/produce_once.cpp'),
                          source, output])
        elif adapter == 'original_q8_endpoint_batch':
            source = self.ensure_order(346516)
            pair = (363420, 414132) if n in (363420, 414132) else (380324, 397228)
            folder = 'replication86_98_batch' if pair[0] == 363420 else 'replication90_94_batch'
            destinations = [self.root / self.order(value)['source_edge_file'] for value in pair]
            for destination in destinations:
                destination.parent.mkdir(parents=True, exist_ok=True)
            self.execute([self.cpp(Q8_DELTA / folder / 'produce_once.cpp'), source,
                          *destinations])
        else:
            raise ValueError('Unsupported saved adapter: ' + adapter)
        if not output.is_file():
            raise FileNotFoundError('The original producer did not create ' + str(output))
        return output

    def saved_neighbor_copy(self, source, source_n, centers, output, row):
        """The immutable-N emit loop used in the original affine clone wrapper.

        Only center labels and copy order come from saved PARAMETERS. The source
        F9 edge body is read without a header, matching the original file format.
        No finite-field evaluation, center search, BFS, or solver is added here.
        """
        pins = {center: [] for center in centers}
        with source.open() as stream:
            for line in stream:
                u, v = map(int, line.split())
                if u in pins:
                    pins[u].append(v)
                if v in pins:
                    pins[v].append(u)
        extra = {}
        for index, center in enumerate(centers):
            for pin in pins[center]:
                extra.setdefault(pin, []).append(source_n + index)
        written = 0
        with source.open() as stream, output.open('x') as target:
            current = next(stream, None)
            edge = tuple(map(int, current.split())) if current else None
            for u in range(source_n):
                while edge is not None and edge[0] == u:
                    target.write(f'{edge[0]} {edge[1]}\n')
                    written += 1
                    current = next(stream, None)
                    edge = tuple(map(int, current.split())) if current else None
                for v in extra.get(u, ()):
                    target.write(f'{u} {v}\n')
                    written += 1
        if written != int(row['edges']):
            raise ValueError('Saved recipe edge count differs: ' + str(written))


def compare_rows(rebuilt, original):
    """Compare the complete integer row stream, including its original header.

    These are saved deterministic, lexicographically ordered edge files, so a
    stream comparison checks the literal labeled edge set without hashes/BFS.
    """
    sentinel = object()
    with rebuilt.open() as left, original.open() as right:
        for line, (a, b) in enumerate(itertools.zip_longest(left, right, fillvalue=sentinel), 1):
            if a is sentinel or b is sentinel:
                raise ValueError('Different number of rows at row ' + str(line))
            if tuple(map(int, a.split())) != tuple(map(int, b.split())):
                raise ValueError('Different integer rows at row ' + str(line))
    print('PASS: complete labeled integer rows equal the supplied saved graph.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--list', action='store_true', help='List all 50 saved case IDs.')
    parser.add_argument('--case', help='Full case ID, for example d20_D3_n3840.')
    parser.add_argument('--output', type=Path, help='New output edge-file path.')
    parser.add_argument('--workspace', type=Path, help='Output tree for generated prerequisites; defaults to a new temporary directory.')
    parser.add_argument('--compare', type=Path, help='Optional exact row comparison against an existing original edge file.')
    parser.add_argument('--cxx', default='g++', help='Existing C++17 compiler for P33/Q8 original producers.')
    parser.add_argument('--producer-cpu', type=float, default=120.0, help='CPU budget supplied to original parameterized producers.')
    args = parser.parse_args()
    rows = cases()
    if args.list:
        for key, row in rows.items():
            print(key, row['Lean'], row['adapter'])
        return
    if args.case not in rows or args.output is None:
        parser.error('Supply a listed --case and a new --output path.')
    output = args.output.resolve()
    if output.exists():
        raise FileExistsError(output)
    workspace = args.workspace.resolve() if args.workspace else Path(tempfile.mkdtemp(prefix='ar4math_graph_replay_'))
    workspace.mkdir(parents=True, exist_ok=True)
    shutil.copytree(HERE / 'materials', workspace, dirs_exist_ok=True)
    # This directory is only an original producer's repository-root locator.
    (workspace / 'formal').mkdir(exist_ok=True)
    print('Saved-input workspace:', workspace, flush=True)
    generated = Replayer(workspace, args.cxx, args.producer_cpu).ensure(args.case)
    output.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(generated, output)
    print('Rebuilt:', args.case, '->', output)
    if args.compare:
        compare_rows(output, args.compare.resolve())


if __name__ == '__main__':
    main()
