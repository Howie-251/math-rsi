"""Verify the local E16 archive and optionally assemble its frozen imports."""

import argparse
import hashlib
import json
import shutil
import subprocess
import tempfile
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'archive_inventory' / 'E16_PACKAGE.json'
INVENTORIES = ('baseline.jsonl', 'source_map.jsonl', 'release_files.jsonl')


def relative_path(value):
    path = PurePosixPath(value)
    if not path.parts or path.is_absolute() or '..' in path.parts or ':' in value or '\\' in value:
        raise ValueError(f'Invalid relative path: {value}')
    return Path(*path.parts)


def digest(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def check(path, record):
    if not path.is_file() or path.is_symlink():
        raise ValueError(f'Missing ordinary file: {path}')
    if 'size' in record and path.stat().st_size != record['size']:
        raise ValueError(f'Different byte count: {path}')
    if digest(path) != record['sha256']:
        raise ValueError(f'Different SHA-256: {path}')


def collect_inventory(inventories, listing):
    archive_paths = set()
    for line in listing.splitlines():
        # Strip the old archive's first component before decoding its localized name.
        prefix, separator, member = line.partition(b'/')
        if not separator or not member or member.endswith(b'/'):
            continue
        try:
            member = member.decode('utf-8')
        except UnicodeDecodeError:
            member = member.decode('gb18030', errors='replace')
        archive_paths.add(member)
    by_path = {}
    for name in INVENTORIES:
        for row in map(json.loads, inventories[name].splitlines()):
            member = row.get('archive_path')
            if member in archive_paths:
                by_path[member] = row
    return by_path


def baseline_inventory(archive, manifest):
    inventories = {}
    for name in INVENTORIES:
        raw = subprocess.check_output(['tar', '-xOf', str(archive), f'*/archive_inventory/{name}'])
        if hashlib.sha256(raw).hexdigest() != manifest['baseline_inventory_sha256'][name]:
            raise ValueError(f'The archive inventory {name} differs from the required baseline.')
        inventories[name] = raw
    listing = subprocess.check_output(['tar', '-tf', str(archive)])
    by_path = collect_inventory(inventories, listing)
    for record in manifest['baseline_imports']:
        archived = by_path[record['archive_path']]
        if archived['sha256'] != record['sha256']:
            raise ValueError(f'Archive inventory mismatch for {record["path"]}')
    existing = {row['sha256'] for row in by_path.values()}
    for record in manifest['payload']:
        if record['sha256'] in existing:
            raise ValueError(f'Payload duplicates an archived file: {record["path"]}')


def extract_baseline(archive, scratch, imports):
    scratch.mkdir()
    listing = scratch / 'archive-members.txt'
    members = sorted({record['archive_path'] for record in imports})
    for member in members:
        relative_path(member)
    listing.write_text(''.join(f'*/{member}\n' for member in members), encoding='utf-8', newline='\n')
    subprocess.run(['tar', '-xf', str(archive), '-C', str(scratch), '--strip-components', '1',
                    '-T', str(listing)], check=True)
    for record in imports:
        check(scratch / relative_path(record['archive_path']), record)


def compose(out, manifest, archive):
    if out == ROOT or ROOT in out.parents:
        raise ValueError('Output directory must be outside the distributable tree.')
    if out.exists() and (not out.is_dir() or any(out.iterdir())):
        raise ValueError(f'Output directory must be empty: {out}')
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='e16_restore_', dir=out.parent) as temp:
        scratch = Path(temp)
        result = scratch / 'result'
        result.mkdir()
        imports = manifest['baseline_imports']
        extract_baseline(archive, scratch / 'imports', imports)
        for record in manifest['payload'] + imports:
            relative = relative_path(record['path'])
            destination = result / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            if 'archive_path' in record:
                source = scratch / 'imports' / relative_path(record['archive_path'])
            else:
                source = ROOT / relative
            shutil.copyfile(source, destination)
            check(destination, record)
        shutil.copyfile(MANIFEST, result / MANIFEST.relative_to(ROOT))
        if out.exists():
            out.rmdir()
        result.rename(out)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--baseline', type=Path, help='Path to the original n=7 RAR for verification or composition')
    parser.add_argument('--compose', type=Path, help='Empty output directory for local files and exact imports')
    args = parser.parse_args()
    if args.compose and not args.baseline:
        parser.error('--compose requires --baseline with the path to the original RAR')
    manifest = json.loads(MANIFEST.read_bytes())
    if manifest['format_version'] != 3:
        raise ValueError('This verifier expects the native v3 E16 manifest.')
    for record in manifest['payload']:
        check(ROOT / relative_path(record['path']), record)
    print(f'Local file SHA-256 verified: {len(manifest["payload"])} files', flush=True)
    if args.baseline:
        archive = args.baseline.resolve(strict=True)
        check(archive, manifest['baseline_archive'])
        baseline_inventory(archive, manifest)
        print(f'Original RAR references verified: {len(manifest["baseline_imports"])}', flush=True)
        if args.compose:
            out = args.compose.resolve()
            compose(out, manifest, archive)
            print(f'Local files and exact baseline imports assembled at {out}', flush=True)


if __name__ == '__main__':
    main()
