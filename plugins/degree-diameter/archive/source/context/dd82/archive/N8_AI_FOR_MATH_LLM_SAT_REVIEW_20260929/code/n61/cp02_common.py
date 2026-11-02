#!/usr/bin/env python3
"""Paths and exact scope of the minimal I12/CP02 increment."""
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROUND = Path(__file__).resolve().parents[1]
REPO = ROUND.parent.parent / 'degree_diameter_sat'
CP01 = ROUND.parent / 'N61_I12_CP01_PRO_TO_CODEX_manual-v1.2-feedback-loop_r1'
SNAPSHOT = ROUND / 'dependencies/CP01_RUNNING_SNAPSHOT/dependencies/implementation'
sys.path.insert(0, str(CP01 / 'code'))
from i12_compile import CNF, Graph, neg, CONSTRAINTS as INHERITED_CONSTRAINTS

VERSION = 'n61_i12_cp02_r1_increment_v1'
CONSTRAINTS = [*INHERITED_CONSTRAINTS, 'I12.18_exact_global_W_le_5']
QUESTION = ('Does the complete I10 INSIDE backbone with all CP01 constraints and '
            'I12.18 (the actual W count over all 61 vertices is at most 5) admit '
            'a graph? This preserves H & G & B_INSIDE & global not-O; it does not '
            'encode full not-O or decide MATCH or O15.')


def add_W_le5(c, literals):
    """The supplied literals already define W from the same graph, exactly."""
    if len(literals) != 61:
        raise ValueError('I12.18 counts all 61 graph vertices')
    ge6 = c.thresholds(literals, 6, 'CP02_I12.18_all61_W')[6]
    c.add(neg(ge6))
    return ge6
