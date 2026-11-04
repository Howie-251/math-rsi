// Exact geometry census; no matching feasibility assumption or full P6 claim.
// argv: output directory, k_min, k_max, optional write_residual(0/1).
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
using U=uint64_t;
int pc(U x){return __builtin_popcountll(x);}
U choose(int n,int k){if(k<0||k>n)return 0;U r=1;for(int i=1;i<=k;i++)r=r*(n-i+1)/i;return r;}
struct Count{U eligible=0,basic=0,adjacent_root=0,residual=0;vector<int> firstZ,firstW;};
vector<int> ev,od,Z,W,allow;
array<U,64> nbr;
array<array<int,6>,3> aa;
array<array<Count,2>,3> stats;
array<array<ofstream,2>,3> bins;
const int targets[3]={1,7,31};
int K; bool writebin;
bool basic(int a,int b){int d=b-a;return (d==0&&b>=1)||d==1||d==2;}
void consume(){
 array<int,6> ones{}; U wm=0;
 for(int w:W){wm|=U(1)<<w;for(int d=0;d<6;d++)ones[d]+=(w>>d)&1;}
 for(int j=0;j<3;j++){
  int v=targets[j];bool free=wm>>v&1;auto&s=stats[j][free];++s.eligible;
  // Only the 10->8 adjacent free-target reduction is currently unconditional.
  if(free&&(wm&((U(1)<<1)|(U(1)<<2)|(U(1)<<4)|(U(1)<<8)|(U(1)<<16)|(U(1)<<32)))){++s.adjacent_root;continue;}
  bool good=false;
  for(int d=0;d<6;d++)if(basic(aa[j][d],(v>>d&1)?ones[d]:K-ones[d])){good=true;break;}
  if(good){++s.basic;continue;}
  ++s.residual;
  if(s.firstZ.empty()){s.firstZ=Z;s.firstW=W;}
  if(writebin){for(int x:Z)bins[j][free].put(char(x));for(int x:W)bins[j][free].put(char(x));}
 }
}
void enumW(int start,int need){
 if(!need){consume();return;}
 for(int j=start;j+need<=int(allow.size());j++){W.push_back(allow[j]);enumW(j+1,need-1);W.pop_back();}
}
void finishZ(U allowed){
 allow.clear();for(int w:od)if(allowed>>w&1)allow.push_back(w);
 for(int j=0;j<3;j++)for(int d=0;d<6;d++){
  int ones=0;for(int z:Z)ones+=(z>>d)&1;
  aa[j][d]=(targets[j]>>d&1)?ones:K-1-ones;
 }
 enumW(0,K);
}
void enumZ(int start,int need,U allowed){
 if(pc(allowed)<K)return;
 if(!need){finishZ(allowed);return;}
 for(int j=start;j+need<=int(ev.size());j++){
  Z.push_back(ev[j]);enumZ(j+1,need-1,allowed&~nbr[ev[j]]);Z.pop_back();
 }
}
void arr(ostream&o,const vector<int>&v){o<<'[';for(size_t i=0;i<v.size();i++){if(i)o<<',';o<<v[i];}o<<']';}
int main(int argc,char**argv){
 if(argc<4)return 2;string dir=argv[1];int lo=stoi(argv[2]),hi=stoi(argv[3]);
 if(lo<5||hi>9||lo>hi)return 3;writebin=argc>=5&&stoi(argv[4]);
 U oddmask=0;
 for(int x=0;x<64;x++){
  if(pc(x)%2){od.push_back(x);oddmask|=U(1)<<x;}else if(x)ev.push_back(x);
  for(int d=0;d<6;d++)nbr[x]|=U(1)<<(x^(1<<d));
 }
 ofstream out(dir+"/HIGHER_Q5_FULL_census_"+to_string(lo)+"_"+to_string(hi)+".json");
 if(!out)return 4;
 out<<"{\"scope\":\"Exact root-normalized independent hole geometries. All balanced Q5 inputs used. Reduced-independent-domain producer only; predecessor reductions conditional. No realizability or full-layer proof claim.\",\"full_p6_proved\":false,\"levels\":[";
 for(K=lo;K<=hi;K++){
  stats={};
  if(writebin)for(int j=0;j<3;j++)for(int f=0;f<2;f++){
   bins[j][f].open(dir+"/HIGHER_Q5_FULL_residual_h"+to_string(2*K)+"_v"+to_string(targets[j])+"_"+(f?"free":"covered")+".bin",ios::binary);
   if(!bins[j][f])return 5;
  }
  enumZ(0,K-1,oddmask);
  if(K>lo)out<<',';out<<"{\"holes\":"<<2*K<<",\"record_bytes\":"<<2*K-1<<",\"targets\":[";
  for(int j=0;j<3;j++)for(int f=0;f<2;f++){
   auto&s=stats[j][f];
   if(j||f)out<<',';
   out<<"{\"v\":"<<targets[j]<<",\"free_target\":"<<(f?"true":"false")<<",\"eligible\":"<<s.eligible
      <<",\"known_cut\":"<<s.basic<<",\"free_root_adjacent_to_predecessor\":"<<s.adjacent_root<<",\"residual\":"<<s.residual;
   out<<",\"first_Z\":";arr(out,s.firstZ);out<<",\"first_W\":";arr(out,s.firstW);out<<'}';
   cout<<"holes="<<2*K<<" v="<<targets[j]<<" free="<<f<<" eligible="<<s.eligible<<" basic="<<s.basic<<" adjacent="<<s.adjacent_root<<" residual="<<s.residual<<endl;
   if(writebin)bins[j][f].close();
  }
  out<<"]}";out.flush();
 }
 out<<"]}\n";
}
