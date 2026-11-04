"""Prepare a force-edge mixed-omission exploratory search."""
from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'TWELVE_ROOT_STAR_MIXED_probe_search.cpp').read_text()
old='vector<pair<int,int>> edges;enumerate(need,p,edges);'
new='int forceA,forceB;cfg>>forceA>>forceB;if(!cfg||forceA<0||forceA>=32||forceB<0||forceB>=32||__builtin_popcount(unsigned(forceA^forceB))!=1||!need[forceA]||!need[forceB])return 9;--need[forceA];--need[forceB];p[forceA]=forceB;vector<pair<int,int>> edges{{forceA,forceB}};enumerate(need,p,edges);'
assert old in s;s=s.replace(old,new)
(R/'TWELVE_ROOT_STAR_OPENING_probe_search.cpp').write_text(s)
(R/'TWELVE_ROOT_STAR_OPENING_probe_config.txt').write_text('0 1 3 31 0 31 3 7\n')
print('Prepared H0,1,3,31/U0,31 with required new short edge3-7.')
