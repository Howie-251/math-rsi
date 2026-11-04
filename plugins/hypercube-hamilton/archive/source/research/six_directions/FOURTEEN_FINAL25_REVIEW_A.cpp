// Independent complete-domain DP and physical certificate audit.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <numeric>
#include <set>
#include <stdexcept>
#include <string>
#include <tuple>
#include <vector>
using namespace std;using U=uint64_t;using B=uint32_t;
int pc(U a){return __builtin_popcountll(a);}U bit(int a){return U(1)<<a;}
void req(bool a,string s){if(!a)throw runtime_error(s);}
struct DS{int p[32];DS(){iota(p,p+32,0);}int root(int x){while(x!=p[x]){p[x]=p[p[x]];x=p[x];}return x;}bool add(int x,int y){x=root(x);y=root(y);if(x==y)return false;p[x]=y;return true;}};
vector<unsigned char> read(string n){ifstream f(n,ios::binary|ios::ate);req(bool(f),"open "+n);size_t sz=f.tellg();vector<unsigned char>v(sz);f.seekg(0);if(sz)f.read((char*)v.data(),sz);req(bool(f),"read "+n);return v;}
int main(){try{
 array<array<int,32>,120>maps;array<int,5>p{0,1,2,3,4};int pi=0;
 do{for(int x=0;x<32;x++){maps[pi][x]=0;for(int d=0;d<5;d++)maps[pi][x]|=((x>>p[d])&1)<<d;}pi++;}while(next_permutation(p.begin(),p.end()));
 array<vector<unsigned char>,4>pools;for(int c:{0,3}){pools[c]=read("TWELVE_ROOT_STAR_OPENING_case_0"+to_string(c)+"_forests.bin");req(pools[c].size()==8031*32,"pool size");}
 U grand=0;cout<<"{\"status\":\"PASS\",\"method\":\"independent_unmatched_odd_subset_even_mask_DP_and_all_physical_forests\",\"reports\":[";
 for(int orbit=0;orbit<2;orbit++){
  U units=0,T=0,WA=0,G=0,evens=0;for(int x:{1,2,4,8,16})units|=bit(x);WA=units|(orbit==0?bit(14):0);for(int x:{7,11,13,19,21,25})T|=bit(x);
  vector<int>E,O;int ei[32],oi[32];fill(ei,ei+32,-1);fill(oi,oi+32,-1);
  for(int x=0;x<32;x++){if(pc(x)%2==0)evens|=bit(x);if(x&&!(WA&bit(x))){G|=bit(x);if(pc(x)%2==0){ei[x]=E.size();E.push_back(x);}else{oi[x]=O.size();O.push_back(x);}}}
  req(E.size()==15&&O.size()==size_t(10+orbit),"domain vertices");vector<int>ns(O.size());U actualN[32]={};int mandatory=0;
  for(int j=0;j<int(O.size());j++){if(T&bit(O[j]))mandatory|=1<<j;for(int i=0;i<15;i++)if(pc(O[j]^E[i])==1){ns[j]|=1<<i;actualN[O[j]]|=bit(E[i]);}}
  U counts[12]={};vector<U>dp(1<<15),next(1<<15);int subsets=0;
  for(int omitted=0;omitted<(1<<O.size());omitted++){
   if(omitted&mandatory)continue;int m=O.size()-pc(omitted),required=orbit?(1<<ei[30]):0;
   for(int j=0;j<int(O.size());j++)if(omitted>>j&1)required|=ns[j];
   if(pc(required)>m)continue;fill(dp.begin(),dp.end(),0);dp[0]=1;
   for(int j=0;j<int(O.size());j++)if(!(omitted>>j&1)){
    fill(next.begin(),next.end(),0);for(int used=0;used<(1<<15);used++)if(dp[used]){int available=ns[j]&~used;while(available){int b=available&-available;available-=b;next[used|b]+=dp[used];}}dp.swap(next);
   }
   for(int used=0;used<(1<<15);used++)if((used&required)==required)counts[m]+=dp[used];subsets++;
  }
  set<tuple<B,B,B,int>>registry;ifstream reg("FOURTEEN_FINAL25_REVIEW_registry_"+to_string(orbit)+".txt");req(bool(reg),"registry");B major,omit,pairmask;int idx;while(reg>>major>>omit>>pairmask>>idx)registry.insert({major,omit,pairmask,idx});req(!registry.empty(),"empty registry");
  auto raw=read("FOURTEEN_FINAL25_A_full_"+to_string(orbit)+"_certificates.bin");req(raw.size()%32==0,"record framing");vector<U>codes;U hist[12]={},flags[2]={},Buse[102]={};
  for(size_t off=0;off<raw.size();off+=32){auto a=&raw[off];int m=a[22],q=a[23],t=a[24],w=a[25],b=a[26],c=a[27],fi=int(a[28])+256*int(a[29]),ap=a[30];
   req(m<=int(O.size())&&q<32&&t<32&&w<32&&b<32&&(c==0||c==3)&&ap<120&&a[31]<=1,"header");req(size_t(fi+1)*32<=pools[c].size(),"forest index");
   U covered=0,code=0;int last=-1,h=-1;vector<pair<int,int>>L;
   for(int j=0;j<2*m;j+=2){int x=a[j],y=a[j+1];req(x<y&&y<32&&(G&bit(x))&&(G&bit(y))&&pc(x^y)==1&&x*32+y>last,"sorted legal short edge");last=x*32+y;req(!(covered&bit(x))&&!(covered&bit(y)),"repeated endpoint");covered|=bit(x)|bit(y);int odd=pc(x)%2?x:y,ev=odd==x?y:x;req(oi[odd]>=0&&ei[ev]>=0,"bipartition");code|=U(ei[ev]+1)<<(4*oi[odd]);L.push_back({x,y});if(y==31)h=x;}
   for(int j=2*m;j<22;j++)req(a[j]==255,"padding");req((covered&T)==T&&(!orbit||(covered&bit(30))),"mandatory actual internal T/even30");req(a[31]==(h>=0),"maximal target flag");
   for(int x:O)if(!(covered&bit(x)))req(!(actualN[x]&~covered),"maximality");
   req(ei[q]>=0&&!(covered&bit(q))&&(T&bit(t))&&pc(q^t)==1,"q/t roles");req(w!=b&&(units&bit(w))&&(units&bit(b)),"w/b units");
   DS ds;int deg[32]={};bool opening=false;
   for(int j=0;j<32;j+=2){int rx=pools[c][fi*32+j],ry=pools[c][fi*32+j+1];req(rx<32&&ry<32,"forest labels");int x=maps[ap][rx],y=maps[ap][ry];req(pc(x^y)==1&&ds.add(x,y),"forest short/labelled acyclic");deg[x]++;deg[y]++;opening|=(x==q&&y==t)||(x==t&&y==q);}
   for(int x=0;x<32;x++)req(deg[x]==((x==0||x==31)?0:(x==q||x==b)?2:1),"physical forest degrees");req(opening,"opening qt");
   U usedprime=0;for(auto[x,y]:L){if(y==31)y=w;req(x!=0&&y!=0&&x!=31&&y!=31&&pc(x)%2!=pc(y)%2&&!(usedprime&bit(x))&&!(usedprime&bit(y)),"modified matching");usedprime|=bit(x)|bit(y);req(ds.add(x,y),"P+Lstarprime labelled cycle");deg[x]++;deg[y]++;}
   U ends=0;for(int x=0;x<32;x++){req(deg[x]==((x==0||x==31)?0:deg[x])&&deg[x]<=2,"union degrees");if(deg[x]==1)ends|=bit(x);}
   U S=WA&~bit(w)&~bit(b),Gprime=(G&~bit(31))|bit(w),Xprime=Gprime&~usedprime,Q=(Xprime&~bit(q))|S;
   req(ends==Q&&pc(ends&evens)==14-m&&pc(ends&~evens)==14-m&&pc(ends)>=6,"exact balanced endpoints");req(!(ends&bit(q))&&!(ends&bit(t)),"q/t disjoint from completion");
   B actualmajor=(T&~bit(t))|S,actualomit=S,actualpair=bit(w)|bit(b);req(!(actualpair&(actualmajor|bit(0)|(orbit?bit(30):0))),"protected endpoint disjointness");
   int found=-1;for(int i:{0,1,7,100,101})if(registry.count({actualmajor,actualomit,actualpair,i})){found=i;break;}req(found>=0,"no actual marked B common map");Buse[found]++;hist[m]++;flags[h>=0]++;codes.push_back(code);
  }
  sort(codes.begin(),codes.end());req(adjacent_find(codes.begin(),codes.end())==codes.end(),"duplicate matching");U total=0;for(int m=0;m<=11;m++){req(hist[m]==counts[m],"complete DP histogram mismatch");total+=hist[m];}req(total==U(orbit?513263:291743),"domain total");grand+=total;
  if(orbit)cout<<",";cout<<"{\"orbit\":"<<orbit<<",\"domain\":"<<total<<",\"size8\":"<<hist[8]<<",\"size9\":"<<hist[9]<<",\"size10\":"<<hist[10]<<",\"size11\":"<<hist[11]<<",\"target_unmatched_in_maximal\":"<<flags[0]<<",\"target_matched_in_maximal\":"<<flags[1]<<",\"unmatched_subsets_evaluated\":"<<subsets<<",\"mandatory_even30\":"<<(orbit?"true":"false")<<",\"B_class_counts\":{";
  bool comma=false;for(int i=0;i<102;i++)if(Buse[i]){if(comma)cout<<",";comma=true;cout<<"\""<<i<<"\":"<<Buse[i];}cout<<"}}";
 }
 req(grand==805006,"grand total");cout<<"],\"all_certificates_verified\":"<<grand<<",\"complete_by_legal_unique_equal_cardinality\":true}\n";
}catch(exception&e){cerr<<e.what()<<endl;return 1;}}
