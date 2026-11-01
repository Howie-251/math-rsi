"""Center8, actual unit neighbors8/9. Reuse old888 and newly certified889 triples;
only the eight genuinely new899 triple profiles are solved. Common partition is retained.
"""
from pathlib import Path
from itertools import combinations
from fractions import Fraction as Q
import json,sys,time
HERE=Path(__file__).parent;ROOT=HERE.parents[5];sys.dont_write_bytecode=True
sys.path[:0]=[str(ROOT/'context/propertyb35-paper/round01/twenty-single-seven'),str(ROOT/'context/propertyb34/round01/high-math'),str(ROOT/'computations'),str(ROOT/'context/propertyb34/round01/middle-math'),str(ROOT/'context/propertyb34-hour1-20261013/high-math')]
from pilot import parts,recover
from subset_position_dp import SubsetEngine
from joint_layout_lp import solve_profile
from fast_position_dp import Engine
from multilock import json_value
