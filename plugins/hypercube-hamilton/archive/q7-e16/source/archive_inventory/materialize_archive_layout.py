"""Check or create the original RAR's directory structure beside this package."""

import argparse
import json
import re
import stat
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / 'archive_inventory' / 'ARCHIVE_STRUCTURE.json'
WINDOWS_RESERVED = re.compile(r'(?i)(?:CON|PRN|AUX|NUL|COM[1-9]|LPT[1-9])')
INVALID_CHAR = re.compile(r'[\x00-\x1f<>:"\\|?*]')


def components(path):
    parts = path.split('/')
    for part in parts:
        if (not part or part.casefold() in {'.', '..', '.git'} or part.endswith(('.', ' '))
                or INVALID_CHAR.search(part) or WINDOWS_RESERVED.fullmatch(part.partition('.')[0])):
            raise ValueError(f'Unsafe archive directory: {path}')
    return parts


def exists_as_directory(path):
    try:
        info = path.lstat()
    except FileNotFoundError:
        return False
    reparse = getattr(info, 'st_file_attributes', 0) & stat.FILE_ATTRIBUTE_REPARSE_POINT
    if not stat.S_ISDIR(info.st_mode) or reparse:
        raise ValueError(f'Archive directory conflicts with an existing file, link or reparse point: {path}')
    if not any(child.name == path.name for child in path.parent.iterdir()):
        raise ValueError(f'Archive directory has different existing capitalization: {path}')
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--create', action='store_true', help='Create missing directories in the package root')
    args = parser.parse_args()
    structure = json.loads(INVENTORY.read_bytes())
    names = sorted(structure['directories'], key=lambda path: (path.count('/'), path))
    if len(names) != structure['directory_count'] or len(names) != len({path.casefold() for path in names}):
        raise ValueError('Archive directory inventory has inconsistent counts or case collisions.')
    expected = {ROOT.joinpath(*components(name)) for name in names}
    if any(folder.parent != ROOT and folder.parent not in expected for folder in expected):
        raise ValueError('Archive directory inventory is missing a parent path.')
    paths = [ROOT.joinpath(*components(name)) for name in names]
    missing = [folder for folder in paths if not exists_as_directory(folder)]
    if args.create:
        for folder in missing:
            if folder.parent != ROOT and not exists_as_directory(folder.parent):
                raise ValueError(f'Archive parent directory disappeared: {folder.parent}')
            folder.mkdir()
        print(f'Archive directory layout complete: {len(paths)} paths ({len(missing)} created).')
    else:
        print(f'Archive directory layout: {len(paths) - len(missing)}/{len(paths)} present, {len(missing)} missing.')
        if missing:
            print('Run with --create to restore the structure.')
            return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
