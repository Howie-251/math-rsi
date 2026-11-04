"""Create a new full-input witness search driver around the fast DFS core."""
from pathlib import Path
R=Path(__file__).resolve().parent
prefix=(R/'t15_core8_residual.cpp').read_text().split('void solve(){')[0]
footer=r'''
#include <cassert>
int main(int argc,char**argv){
 assert(argc==6);int omit1=stoi(argv[4]),omit2=stoi(argv[5]);
 assert(omit1>0&&omit1<32&&omit2>0&&omit2<32&&omit1!=omit2);
 ifstream in(argv[1],ios::binary);assert(in);out.open(argv[2],ios::binary);fail.open(argv[3]);assert(out&&fail);
 unsigned char bytes[26];while(in.read((char*)bytes,26)){
  uint32_t used=0;req.clear();
  for(int j=0;j<26;j+=2){int a=bytes[j],b=bytes[j+1];assert(a<32&&b<32&&a!=b&&!(used>>a&1)&&!(used>>b&1));used|=(1u<<a)|(1u<<b);req.emplace_back(a,b);}
  assert(!(used&1)&&!(used>>omit1&1)&&!(used>>omit2&1));blocks.clear();
  for(int v=0;v<32;v++)if(v!=omit1&&v!=omit2&&!(used>>v&1))blocks.push_back({v});assert(blocks.size()==4&&blocks[0][0]==0);
  for(auto[a,b]:req)blocks.push_back({a,b});nodes=0;timeout=false;route={{0,0}};prepare();
  bool ok=fastdfs(0,((1u<<blocks.size())-1)&~1u,allEntries&~3ull);
  ++total;totalNodes+=nodes;maxNodes=max(maxNodes,nodes);
  if(ok){++positive;out.write((char*)bytes,26);for(auto[k,rev]:route){auto B=blocks[k];if(rev)reverse(B.begin(),B.end());for(int v:B)out.put(char(v));}}
  else{if(timeout)++unknown;else ++negative;fail<<total-1<<' '<<(timeout?"UNKNOWN":"EXHAUSTED");for(auto[a,b]:req)fail<<' '<<a<<' '<<b;fail<<'\n';}
 }
 assert(in.eof()&&in.gcount()==0);
 cout<<"{\"total\":"<<total<<",\"positive\":"<<positive<<",\"unknown\":"<<unknown<<",\"negative\":"<<negative<<",\"nodes\":"<<totalNodes<<",\"max_nodes\":"<<maxNodes<<",\"record_bytes\":56}\n";
}
'''
(R/'q5_full_input_certifier.cpp').write_text(prefix+footer)
