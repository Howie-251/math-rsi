"""Regenerate the checked N=16 coefficient literals, without profile/layout search.

Output goes to a caller-chosen directory so existing checked sources are not
silently overwritten. The generated theorem obligations still need Lean checking.
"""
from fractions import Fraction
from math import comb, factorial
from pathlib import Path
import argparse


def choose(n, k):
    return comb(n, k) if 0 <= k <= n else 0


def div(a, b):
    return Fraction(a, b) if b else Fraction(0)


def edge(a, locked, r):
    if locked:
        return div(choose(a, r), choose(16, r))
    return div(r * choose(a, max(r - 1, 0)), 16 * choose(15, max(r - 1, 0)))


def pair(a, locked, r, q):
    b = max((16 if locked else 15) - a, 0)
    if locked:
        return div(choose(a, r) * choose(b, q), choose(16, r) * choose(16 - r, q))
    return div(choose(a, max(r - 1, 0)) * choose(b, max(q - 1, 0)),
               16 * choose(15, max(r - 1, 0)) * choose(16 - r, max(q - 1, 0)))


def vector(xs):
    return '![' + ','.join(xs) + ']'


def rational(x):
    return f'({x.numerator}/{x.denominator})'


def integer(x):
    scaled = x * factorial(16)
    assert scaled.denominator == 1
    return str(scaled.numerator)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output_directory', type=Path)
    args = parser.parse_args()
    args.output_directory.mkdir(parents=True, exist_ok=True)
    for name, formatter in [('rational', rational), ('scaled_integer', integer)]:
        a = vector([vector([formatter(edge(j, locked, r)) for r in range(6)])
                    for locked in (False, True) for j in range(17)])
        c = vector([vector([vector([formatter(pair(j, locked, r, q)) for q in range(6)])
                            for r in range(6)]) for locked in (False, True) for j in range(17)])
        (args.output_directory / f'{name}_edge.txt').write_text(a + '\n')
        (args.output_directory / f'{name}_pair.txt').write_text(c + '\n')
    print('Wrote 204 edge + 1224 pair coefficient literals in each representation.')


if __name__ == '__main__':
    main()
