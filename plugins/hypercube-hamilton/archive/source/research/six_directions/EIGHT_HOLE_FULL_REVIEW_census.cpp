// Independent full covered-target geometry census. No producer code imported.
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <vector>
using Rec=std::array<unsigned char,7>;
int main(){
 const std::set<std::pair<int,int>> good={{0,1},{0,2},{1,1},{1,2},{1,3},{2,2},{2,3},{2,4},{3,3}};
 std::vector<int> ev,od;
 for(int x=1;x<64;x++) if(__builtin_popcount((unsigned)x)%2==0)ev.push_back(x);
 for(int x=0;x<64;x++) if(__builtin_popcount((unsigned)x)%2)od.push_back(x);
 std::cout<<"{\"status\":\"PASS\",\"targets\":[";
 bool first=true;
 for(int v:{1,7,31}){
  std::ifstream in("covered_eight_residual_"+std::to_string(v)+".bin",std::ios::binary);assert(in);
  std::set<Rec> expected;Rec rr;while(in.read((char*)rr.data(),7))assert(expected.insert(rr).second);assert(in.eof());
  uint64_t total=0,residual=0;
  for(size_t a=0;a<ev.size();a++)for(size_t b=a+1;b<ev.size();b++)for(size_t c=b+1;c<ev.size();c++){
   int z[3]={ev[a],ev[b],ev[c]};std::vector<int>w;
   for(int x:od){if(x==v)continue;bool ok=true;for(int y:z)if(__builtin_popcount((unsigned)(x^y))==1)ok=false;if(ok)w.push_back(x);}
   for(size_t i=0;i<w.size();i++)for(size_t j=i+1;j<w.size();j++)for(size_t k=j+1;k<w.size();k++)for(size_t l=k+1;l<w.size();l++){
    ++total;int ww[4]={w[i],w[j],w[k],w[l]};bool solved=false;
    for(int d=0;d<6;d++){int na=0,nb=0;for(int x:z)na+=((x^v)&(1<<d))==0;for(int x:ww)nb+=((x^v)&(1<<d))==0;if(good.count({na,nb})){solved=true;break;}}
    if(!solved){++residual;Rec r={(unsigned char)z[0],(unsigned char)z[1],(unsigned char)z[2],(unsigned char)ww[0],(unsigned char)ww[1],(unsigned char)ww[2],(unsigned char)ww[3]};assert(expected.erase(r)==1);}
   }
  }
  assert(expected.empty());if(!first)std::cout<<",";first=false;
  std::cout<<"{\"target\":"<<v<<",\"eligible\":"<<total<<",\"residual\":"<<residual<<"}";
 }
 std::cout<<"]}\n";
}
