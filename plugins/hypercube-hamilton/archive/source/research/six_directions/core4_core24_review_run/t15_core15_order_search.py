from pathlib import Path
s=Path('t15_core15_residual_fast.cpp').read_text()
a=s.index(' for(unsigned bits=mask&neighborBlocks[end]');b=s.index('\n dead.insert(key);return false;',a)
s=s[:a]+''' struct Candidate{int score,k,rev,exit;};vector<Candidate> candidates;
 for(unsigned bits=mask&neighborBlocks[end];bits;bits&=bits-1){int k=__builtin_ctz(bits);
  for(int rev=0;rev<(blocks[k].size()==1?1:2);rev++){
   int entry=rev?blocks[k].back():blocks[k].front();if(!shortedge(end,entry))continue;
   int exit=rev?blocks[k].front():blocks[k].back();unsigned rem=mask&~(1u<<k);
   int score=__builtin_popcount(neighborBlocks[exit]&rem)+shortedge(exit,0);
   if(rem&&score==0)continue;candidates.push_back({score,k,rev,exit});
  }
 }
 stable_sort(candidates.begin(),candidates.end(),[](const Candidate&a,const Candidate&b){return a.score<b.score;});
 for(auto t:candidates){route.emplace_back(t.k,t.rev);if(dfs(t.exit,mask&~(1u<<t.k)))return true;route.pop_back();if(timeout)return false;}
'''+s[b:]
Path('t15_core15_residual_ordered.cpp').write_text(s)
