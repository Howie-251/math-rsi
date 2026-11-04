"""Create a separate positive-search producer with low-onward-degree ordering.
The original producer and its accepted certificates remain untouched.
"""
from pathlib import Path
R=Path(__file__).resolve().parent
s=(R/'a8_full_cycle_certifier.cpp').read_text()
old=''' for(uint64_t bits=neighbor_entries[end]&options;bits;bits&=bits-1){
  int id=__builtin_ctzll(bits),k=id/2;route.emplace_back(k,id%2);'''
new=''' array<pair<int,int>,8> choices{};int nc=0;
 for(uint64_t bits=neighbor_entries[end]&options;bits;bits&=bits-1){
  int id=__builtin_ctzll(bits),k=id/2;
  auto next_options=options&~(3ull<<(2*k));
  int score=__builtin_popcountll(neighbor_entries[exit_v[id]]&next_options);
  choices[nc++]={score,id};
 }
 sort(choices.begin(),choices.begin()+nc);
 for(int ci=0;ci<nc;ci++){
  int id=choices[ci].second,k=id/2;route.emplace_back(k,id%2);'''
assert old in s
(R/'a8_full_cycle_certifier_ordered.cpp').write_text(s.replace(old,new))
