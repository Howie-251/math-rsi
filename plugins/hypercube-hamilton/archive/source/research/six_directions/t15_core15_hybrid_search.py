from pathlib import Path
s=Path('t15_core15_residual_ordered.cpp').read_text()
s=s.replace('bool timeout;','bool timeout;bool randomized=false;uint32_t rng=1234567;uint32_t draw(){rng^=rng<<13;rng^=rng>>17;rng^=rng<<5;return rng;}')
s=s.replace('int score=__builtin_popcount(neighborBlocks[exit]&rem)+shortedge(exit,0);','int score=__builtin_popcount(neighborBlocks[exit]&rem)+shortedge(exit,0);')
s=s.replace('candidates.push_back({score,k,rev,exit});','candidates.push_back({randomized?score*2+int(draw()%12):score,k,rev,exit});')
s=s.replace('bool ok=dfs(0,((1u<<blocks.size())-1)&~1u);','bool ok=false;uint64_t spent=0;for(int attempt=0;attempt<9;attempt++){randomized=attempt<8;cap=randomized?256:2000000;nodes=0;timeout=false;dead.clear();route={{0,0}};ok=dfs(0,((1u<<blocks.size())-1)&~1u);spent+=nodes;if(ok)break;}nodes=spent;')
Path('t15_core15_residual_hybrid.cpp').write_text(s)
