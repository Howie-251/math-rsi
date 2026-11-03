"""Read-only loader for all affine-line joint-cover objects and old ball caches.

No loader or model is executed on import. This module was saved for the unique
joint-cover driver; it does not write files, compute balls, or call a solver.
The driver owns target-support caching and all CPU limits.
"""
from pathlib import Path
import json
import struct


_LOOP = Path(__file__).resolve().parent.parent
_BASE = _LOOP.parent


def load_source(n):
    """Return spec/lines/cache-order IDs/uint64 words/incidence masks/targets.

    Line IDs and bit positions are zero-based. Selector variables are line_id+1.
    Ball row indices are zero-based. Every original affine coset is retained;
    no whole-fibre block-mask equivalence is used here.
    """
    import numpy as np

    assert n in (15552, 102060)
    label = f'source{n}'
    interface = json.loads((_LOOP/'affine_line_block_cover'/
                            f'{label}_JOINT_LINE_INTERFACE.json').read_text())
    free = json.loads((_LOOP/'full_free_directions'/
                      f'{label}_FREE_DIRECTION_GROUPS.json').read_text())
    assert interface['n'] == free['n'] == n
    expected_free, expected_lines = (648, 2808) if n == 15552 else (810, 3510)
    q, k = interface['bin_size'], free['dimension']
    assert q == 3**k and n % q == 0
    cache = interface['cache']
    path = _BASE/cache['file']

    if n == 15552:
        with path.open('rb') as stream:
            header = struct.unpack('<III', stream.read(12))
        assert header == (648, 15552, 243)
        W = 243
        stride = 4 + W*8
        assert path.stat().st_size == 12 + expected_free*stride
        backing = np.memmap(path, dtype='u1', mode='r')
        row_labels = np.ndarray(shape=(expected_free,), dtype='<u4',
                                buffer=backing, offset=12, strides=(stride,))
        ids = [int(v) for v in row_labels]
        # The uint32 label precedes every ball. Rows alternate alignment;
        # NumPy's explicit strides preserve every uint64 word without copying.
        words = np.ndarray(shape=(expected_free, W), dtype='<u8',
                           buffer=backing, offset=16, strides=(stride, 8))
    else:
        W = 1595
        eligible_path = _BASE/'d15_D5_current102060_source/monotone_R4_cover/eligible.txt'
        ids = [int(v) for v in eligible_path.read_text().split()]
        assert len(ids) == expected_free
        assert path.stat().st_size == expected_free*W*8
        words = np.memmap(path, dtype='<u8', mode='r', shape=(expected_free, W))
        backing = words

    assert len(ids) == len(set(ids)) == expected_free
    assert ids == interface['literal_free_ball_row_order']
    assert ids == free['literal_free_ball_row_order']
    assert words.shape == (expected_free, W) and words.dtype == np.dtype('<u8')
    lines = interface['lines']
    assert len(lines) == expected_lines == interface['line_count']
    assert [line['line_id'] for line in lines] == list(range(expected_lines))
    pin_to_line_masks = [0]*expected_free
    for line in lines:
        line_id = line['line_id']
        assert line['selector_variable'] == line_id+1 and line['cost'] == 3
        pins, rows = line['pins'], line['ball_row_indices']
        assert len(pins) == len(set(pins)) == len(rows) == len(set(rows)) == 3
        assert all(0 <= row < expected_free for row in rows)
        assert [ids[row] for row in rows] == pins
        assert all(pin//q == line['controller'] for pin in pins)
        bit = 1 << line_id
        for row in rows:
            pin_to_line_masks[row] |= bit
    assert all(pin_to_line_masks)  # All actual648/810 free points are represented.

    neg = free['neg_local_offsets']
    assert len(neg) == q and all(neg[neg[x]] == x for x in range(q))
    offsets = sorted({0, *(3**i for i in range(k)), *(neg[3**i] for i in range(k))})
    assert len(offsets) == 1+2*k
    initial_targets = [a*q+x for a in range(n//q) for x in offsets]
    assert initial_targets == sorted(initial_targets)
    assert len(initial_targets) == (n//q)*(1+2*k)
    spec = {
        'source': label, 'n': n, 'm': interface['m'], 'D': interface['D'],
        'Delta': interface['Delta'], 'bin_size': q, 'dimension': k,
        'q': q, 'k': k, 'controller_count': n//q,
        'free_count': expected_free, 'line_count': expected_lines,
        'words_per_ball': W, 'W': W, 'radius': interface['D']-1,
        'cache_path': str(path), 'cache_format': cache,
        'line_ids_base': 0, 'selector_variables_base': 1,
        'ball_row_indices_base': 0,
    }
    return {
        'spec': spec,
        'lines': lines,
        'ids': ids,
        'words': words,
        'pin_to_line_masks': pin_to_line_masks,
        'initial_targets': initial_targets,
        'neg_local_offsets': neg,
        '_cache_backing': backing,
    }


def point_support(data, t):
    """Return a Python-int mask of all raw lines whose old ball union covers t.

    This reads the original target bit from the existing candidate-pin rows,
    then unions only the line-incidence masks of those covering pins. It does
    not compute or cache a new ball. The caller owns support memoization.
    """
    import numpy as np

    assert 0 <= t < data['spec']['n']
    bit = np.uint64(1 << (t & 63))
    covered_pins = np.flatnonzero((data['words'][:, t//64] & bit) != 0)
    support = 0
    incidence = data['pin_to_line_masks']
    for row in covered_pins:
        support |= incidence[int(row)]
    return support
