// Apply actual marked T15 projections, then exact short-matching feasibility.
// Reads only raw residual geometry files. No full-layer theorem claim.
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <unordered_map>
#include <vector>
using namespace std;using U=uint64_t;
int pc(int x){return __builtin_popcount(unsigned(x));}
unordered_map<uint32_t,int> lookup,allhard;int oi[32];
vector<int>Z,W;int V,K;U holes;
int project(int x,int m,int d){x^=m;assert(!(x>>d&1));return (x&((1<<d)-1))|((x>>(d+1))<<d);}
uint32_t key(const vector<int>&av,const vector<int>&inc,int m,int d){
 uint32_t r=0;for(int x:av){int q=project(x,m,d);assert(pc(q)%2);r|=1u<<oi[q];}
 for(int x:inc){int q=project(x,m,d);assert(pc(q)%2);r|=1u<<(16+oi[q]);}return r;
}
int route(map<int,U>&miss){
 for(int d=0;d<6;d++){
  vector<int>za,zb,wa,wb;
  for(int x:Z)(((x^V)>>d&1)?zb:za).push_back(x);
  for(int x:W)(((x^V)>>d&1)?wb:wa).push_back(x);
  vector<int>sel,inc;int m=-1;
  if(int(za.size())==K-2&&int(wa.size())==K-3){sel=za;inc=wb;assert(zb.size()==1);m=zb[0];}
  if(int(za.size())==K-4&&int(wa.size())==K-1){
   for(int x:wa)if(x!=V&&x!=(1<<d))sel.push_back(x);
   inc=zb;assert(wb.size()==1);m=wb[0];
  }
  if(m<0)continue;assert(inc.size()==3);
  for(size_t i=0;i<sel.size();i++)for(size_t j=i+1;j<sel.size();j++){
   vector<int>av={sel[i]^(1<<d),sel[j]^(1<<d)};uint32_t q=key(av,inc,m,d);
   auto f=lookup.find(q);if(f!=lookup.end())return f->second;
   auto g=allhard.find(q);if(g!=allhard.end())++miss[g->second];else ++miss[-1];
  }
 }
 return -1;
}
array<vector<int>,64> adj;int mate[64];U seen;
bool dfs(int x){for(int y:adj[x])if(!(seen>>y&1)){seen|=U(1)<<y;if(mate[y]<0||dfs(mate[y])){mate[y]=x;return true;}}return false;}
bool feasible(){
 vector<int>es;fill(mate,mate+64,-1);
 for(int x=0;x<64;x++)if(pc(x)%2==0&&!(holes>>x&1)){
  es.push_back(x);adj[x].clear();for(int d=0;d<6;d++){int y=x^(1<<d);if(!(holes>>y&1))adj[x].push_back(y);}
 }
 sort(es.begin(),es.end(),[](int a,int b){return adj[a].size()<adj[b].size();});
 for(int x:es){seen=0;if(!dfs(x))return false;}return true;
}
int main(int argc,char**argv){
 if(argc!=3)return 2;string dir=argv[1];K=stoi(argv[2]);if(K!=5&&K!=6)return 3;
 int n=0;for(int x=0;x<32;x++)if(pc(x)%2)oi[x]=n++;
 for(auto name:{"higher_hole_t15_lookup.txt","higher_hole_t15_all_hard.txt"}){
  ifstream f(dir+"/"+name);if(!f)return 4;uint32_t q;int id;
  while(f>>q>>id)(name==string("higher_hole_t15_lookup.txt")?lookup:allhard)[q]=id;
 }
 ofstream out(dir+"/higher_hole_t15_filter_h"+to_string(2*K)+".json");
 out<<"{\"scope\":\"Conservative marked T15 filtering and exact bipartite feasibility; unaudited producer\",\"full_p6_proved\":false,\"targets\":[";
 bool comma=false;
 for(int v:{1,7,31})for(int fre=0;fre<2;fre++){
  V=v;string stem="h"+to_string(2*K)+"_v"+to_string(v)+"_"+(fre?"free":"covered");
  ifstream f(dir+"/higher_hole_residual_"+stem+".bin",ios::binary);if(!f)return 5;
  ofstream residual(dir+"/higher_hole_after_t15_"+stem+".bin",ios::binary);
  U total=0,pass=0,infeasible=0,left=0;map<int,U>missing,used;array<unsigned char,17>g{};
  while(f.read(reinterpret_cast<char*>(g.data()),2*K-1)){
   ++total;Z.assign(g.begin(),g.begin()+K-1);W.assign(g.begin()+K-1,g.begin()+2*K-1);
   holes=1;for(int x:Z)holes|=U(1)<<x;for(int x:W)holes|=U(1)<<x;
   assert(pc(int(holes))+pc(int(holes>>32))==2*K);assert(bool(holes>>v&1)==bool(fre));
   map<int,U>miss;int r=route(miss);if(r>=0){++pass;++used[r];continue;}
   if(!feasible()){++infeasible;continue;}
   ++left;for(auto [id,c]:miss)missing[id]+=c;
   residual.write(reinterpret_cast<char*>(g.data()),2*K-1);
  }
  if(f.gcount()!=0)return 6;
  if(comma)out<<',';comma=true;
  out<<"{\"v\":"<<v<<",\"free_target\":"<<(fre?"true":"false")<<",\"input\":"<<total<<",\"known_T15\":"<<pass<<",\"infeasible\":"<<infeasible<<",\"remaining\":"<<left<<",\"missing_core_occurrences\":{";
  bool sep=false;for(auto [id,c]:missing){if(sep)out<<',';sep=true;out<<'"'<<id<<"\":"<<c;}out<<"},\"used_core_occurrences\":{";
  sep=false;for(auto [id,c]:used){if(sep)out<<',';sep=true;out<<'"'<<id<<"\":"<<c;}out<<"}}";out.flush();
  cout<<stem<<" input="<<total<<" known_T15="<<pass<<" infeasible="<<infeasible<<" remaining="<<left<<endl;
 }
 out<<"]}\n";
}
