// Independent W-first enumeration and exhaustive raw membership/uniqueness audit.
// Never writes producer files. args: directory k. Output JSON to stdout.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std; using U=uint64_t;
int pop(U x){return __builtin_popcountll(x);} int K;
U faces[6],near0,evmask,wm; int targets[3]={1,7,31};
vector<int> odd; U forbid[64];
U countrow[3][2][4]={}; // eligible, root-adjacent, nearbalanced, residual
int base[3][6]; bool freev[3],rootadj;
bool cut(U z,int j){for(int d=0;d<6;d++){
 int a=pop(z&faces[d]); if(!(targets[j]>>d&1))a=K-1-a;
 int b=base[j][d]; if(b>=1 && b>=a && b<=a+2)return true;
 }return false;}
void takeZ(U z){for(int j=0;j<3;j++){
 auto &r=countrow[j][freev[j]]; r[0]++;
 if(freev[j]&&rootadj){r[1]++;continue;}
 if(cut(z,j))r[2]++;else r[3]++;
}}
void zsets(U remaining,int need,U z){if(!need){takeZ(z);return;}
 while(pop(remaining)>=need){U bit=remaining&-remaining;remaining-=bit;zsets(remaining,need-1,z|bit);}}
void takeW(U w,U allowed){wm=w; rootadj=(w&near0)!=0;
 for(int j=0;j<3;j++){freev[j]=(w>>targets[j])&1;
 for(int d=0;d<6;d++){int b=pop(w&faces[d]);base[j][d]=(targets[j]>>d&1)?b:K-b;}}
 zsets(allowed,K-1,0);
}
void wsets(int start,int need,U w,U allowed){if(pop(allowed)<K-1)return;
 if(!need){takeW(w,allowed);return;}
 for(int i=start;i+need<=32;i++)wsets(i+1,need-1,w|(U(1)<<odd[i]),allowed&~forbid[odd[i]]);
}
U auditRaw(string dir,int j,int f){string fn=dir+"/HIGHER_Q5_FULL_residual_h"+to_string(2*K)+"_v"+to_string(targets[j])+"_"+(f?"free":"covered")+".bin";
 ifstream in(fn,ios::binary); if(!in)throw runtime_error("open "+fn);
 int n=2*K-1; vector<unsigned char> rec(n),prev;U total=0;
 while(in.read((char*)rec.data(),n)){
  if(!prev.empty() && !(prev<rec))throw runtime_error("duplicate/order "+fn);prev=rec;
  U z=0,w=0;
  for(int i=0;i<n;i++){
   int x=rec[i];if(x>=64)throw runtime_error("vertex");
   if(i<K-1){if(!x||pop(x)%2||(i&&rec[i-1]>=x))throw runtime_error("Z shape");z|=U(1)<<x;}
   else {if(pop(x)%2!=1||(i>K-1&&rec[i-1]>=x))throw runtime_error("W shape");w|=U(1)<<x;}
  }
  if(bool(w>>targets[j]&1)!=bool(f))throw runtime_error("target status");
  for(int d=0;d<6;d++){
   U tmp=z;while(tmp){int x=__builtin_ctzll(tmp);tmp&=tmp-1;if(w>>(x^(1<<d))&1)throw runtime_error("independence");}
   int a=pop(z&faces[d]),b=pop(w&faces[d]);
   if(!(targets[j]>>d&1)){a=K-1-a;b=K-b;}
   if(b>=1&&b>=a&&b<=a+2)throw runtime_error("raw admits cut");
  }
  if(f&&(w&near0))throw runtime_error("raw admits predecessor");
  total++;
 }
 if(in.gcount()!=0)throw runtime_error("partial record");
 if(total!=countrow[j][f][3])throw runtime_error("cardinality mismatch");
 return total;
}
int main(int argc,char**argv){try{
 if(argc!=3)return 2;K=stoi(argv[2]);if(K<6||K>9)return 3;
 for(int x=0;x<64;x++){
  if(pop(x)%2)odd.push_back(x);else if(x)evmask|=U(1)<<x;
  if(pop(x)==1)near0|=U(1)<<x;
  for(int d=0;d<6;d++){if(x>>d&1)faces[d]|=U(1)<<x;forbid[x]|=U(1)<<(x^(1<<d));}
 }
 wsets(0,K,0,evmask);
 cout<<"{\"holes\":"<<2*K<<",\"enumeration\":\"independent_W_first\",\"targets\":[";
 for(int j=0;j<3;j++)for(int f=0;f<2;f++){
  U n=auditRaw(argv[1],j,f);auto&r=countrow[j][f];
  if(j||f)cout<<',';
  cout<<"{\"v\":"<<targets[j]<<",\"free_target\":"<<(f?"true":"false")<<",\"eligible\":"<<r[0]<<",\"free_root_adjacent_to_predecessor\":"<<r[1]<<",\"known_cut\":"<<r[2]<<",\"residual\":"<<r[3]<<",\"raw_membership_unique_count\":"<<n<<'}';
 }
 cout<<"],\"status\":\"PASS\"}\n";
 }catch(exception&e){cerr<<e.what()<<endl;return 1;}}
