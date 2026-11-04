// Independent complete-domain subset DP plus direct physical A-certificate check.
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
void req(bool b,string s){if(!b)throw runtime_error(s);}int pc(U x){return __builtin_popcountll(x);}U bit(int x){return U(1)<<x;}
struct DS{int p[32];DS(){iota(p,p+32,0);}int root(int x){while(x!=p[x]){p[x]=p[p[x]];x=p[x];}return x;}bool add(int a,int b){a=root(a);b=root(b);if(a==b)return false;p[a]=b;return true;}};
vector<unsigned char> read(string n){ifstream f(n,ios::binary|ios::ate);req(bool(f),"open "+n);size_t size=f.tellg();vector<unsigned char>a(size);f.seekg(0);if(size)f.read((char*)a.data(),size);req(bool(f),"read "+n);return a;}
int main(int argc,char**argv){try{
 req(argc==2,"directory");string dir=argv[1];vector<int>E,O;int ei[32],oi[32];fill(ei,ei+32,-1);fill(oi,oi+32,-1);U G=0,J=0,units=0,evens=0;
 for(int x:{1,2,4,8,14,16,22})J|=bit(x);for(int x:{1,2,4,8,16})units|=bit(x);
 for(int x=0;x<32;x++){if(pc(x)%2==0)evens|=bit(x);if(x&&!(J&bit(x))){G|=bit(x);if(pc(x)%2==0){ei[x]=E.size();E.push_back(x);}else{oi[x]=O.size();O.push_back(x);}}}
 req(E.size()==15&&O.size()==9,"G sizes");int ns[9]={};U actualN[32]={};
 for(int j=0;j<9;j++)for(int i=0;i<15;i++)if(pc(O[j]^E[i])==1){ns[j]|=1<<i;actualN[O[j]]|=bit(E[i]);}
 array<array<int,7>,1> Ts{{{7,11,13,19,21,25,31}}};U TM[1]={},TO[1]={};
 for(int k=0;k<1;k++)for(int x:Ts[k]){TM[k]|=bit(x);TO[k]|=bit(oi[x]);}
 // Partition by exact unmatched odds. Used-even-mask injections count short
 // partner assignments; maximality is exactly N(unmatched) subset used.
 U counts[1][11]={};vector<U>dp(1<<15),nxt(1<<15);int evaluated=0,pruned=0;
 for(int unmatched=0;unmatched<(1<<9);unmatched++){
  if((U(unmatched)&TO[0]))continue;
  int m=9-__builtin_popcount(unsigned(unmatched)),required=0;
  for(int j=0;j<9;j++)if(unmatched>>j&1)required|=ns[j];
  if(__builtin_popcount(unsigned(required))>m){pruned++;continue;}
  fill(dp.begin(),dp.end(),0);dp[0]=1;
  for(int j=0;j<9;j++)if(!(unmatched>>j&1)){
   fill(nxt.begin(),nxt.end(),0);
   for(int used=0;used<(1<<15);used++)if(dp[used]){int available=ns[j]&~used;while(available){int b=available&-available;available-=b;nxt[used|b]+=dp[used];}}
   dp.swap(nxt);
  }
  U total=0;for(int used=0;used<(1<<15);used++)if((used&required)==required)total+=dp[used];
  for(int k=0;k<1;k++)if(!(U(unmatched)&TO[k]))counts[k][m]+=total;evaluated++;
 }
 array<array<int,32>,120>maps;array<int,5>perm{0,1,2,3,4};int pn=0;
 do{for(int x=0;x<32;x++){maps[pn][x]=0;for(int d=0;d<5;d++)maps[pn][x]|=((x>>perm[d])&1)<<d;}pn++;}while(next_permutation(perm.begin(),perm.end()));
 array<vector<unsigned char>,5>pools;for(int c:{0,3}){pools[c]=read(dir+"/TWELVE_ROOT_STAR_OPENING_case_0"+to_string(c)+"_forests.bin");req(pools[c].size()%32==0,"pool alignment");}
 // Rebuilt common-map B table includes the actual PAIR, not just hole types.
 set<tuple<B,B,B,int>>Bkeys;ifstream table(dir+"/SIXTEEN_STAR_REVIEW_B_registry.txt");req(bool(table),"B table");B bm,bu,br;int bi;while(table>>bm>>bu>>br>>bi)Bkeys.insert({bm,bu,br,bi});req(!Bkeys.empty(),"B table empty");
 set<tuple<int,int,int,int,int,int,int>>options;ifstream opt(dir+"/SIXTEEN_STAR_REVIEW_options.txt");req(bool(opt),"checked options");int oq,ot,ow,ob,oc,opi,oid;while(opt>>oq>>ot>>ow>>ob>>oc>>opi>>oid)options.insert({oq,ot,ow,ob,oc,opi,oid});req(options.size()==160,"options count");
 U grand=0;cout<<"{\"status\":\"PASS\",\"domain_method\":\"exact_unmatched_odd_subset_used_even_injection_DP\",\"DP_evaluated\":"<<evaluated<<",\"DP_pruned_necessary_neighborhood_bound\":"<<pruned<<",\"reports\":[";
 for(int k=0;k<1;k++){
  auto raw=read(dir+"/SIXTEEN_STAR_A_full_certificates.bin");req(raw.size()%32==0,"A frame");vector<U>codes;U hist[11]={};U Buse[42]={};
  for(size_t off=0;off<raw.size();off+=32){auto a=&raw[off];int m=a[22],q=a[23],t=a[24],w=a[25],b=a[26],c=a[27],row=int(a[28])+(int(a[29])<<8),pi=a[30];
   req(m<=9&&q<32&&t<32&&w<32&&b<32&&(c==0||c==3)&&pi<120&&a[31]==1,"A header");
   req(size_t(row+1)*32<=pools[c].size(),"forest index");U covered=0,code=0;int last=-1,h=-1;vector<pair<int,int>>L;
   for(int j=0;j<2*m;j+=2){int x=a[j],y=a[j+1];req(x<y&&y<32&&(G&bit(x))&&(G&bit(y))&&pc(x^y)==1&&x*32+y>last,"original edges sorted/short/G");last=x*32+y;
    req(!(covered&bit(x))&&!(covered&bit(y)),"original repeated vertex");covered|=bit(x)|bit(y);int odd=pc(x)%2?x:y,ev=odd==x?y:x;req(oi[odd]>=0&&ei[ev]>=0,"original bipartite");code|=U(ei[ev]+1)<<(4*oi[odd]);L.push_back({x,y});if(y==31)h=x;
   }
   for(int j=2*m;j<22;j++)req(a[j]==255,"A padding");req((covered&TM[k])==TM[k]&&h>=0,"mandatory T / internal target");
   for(int x:O)if(!(covered&bit(x)))req(!(actualN[x]&~covered),"not inclusion-maximal");
   req(ei[q]>=0&&!(covered&bit(q))&&(TM[k]&bit(t))&&t!=31&&pc(q^t)==1,"q/t roles");req(w!=b&&(units&bit(w))&&(units&bit(b)),"w/b unit roles");
   DS ds;int deg[32]={};bool opening=false;
   for(int j=0;j<32;j+=2){int rx=pools[c][row*32+j],ry=pools[c][row*32+j+1];req(rx<32&&ry<32,"source forest labels");int x=maps[pi][rx],y=maps[pi][ry];req(pc(x^y)==1&&ds.add(x,y),"physical forest short/labelcycle");deg[x]++;deg[y]++;if((x==q&&y==t)||(x==t&&y==q))opening=true;}
   for(int x=0;x<32;x++)req(deg[x]==((x==0||x==31)?0:(x==q||x==b)?2:1),"physical forest degree");req(opening,"physical q-t absent");
   U LAused=0;for(auto[x,y]:L){if(y==31)y=w;req(x!=0&&y!=0&&x!=31&&y!=31&&pc(x)%2!=pc(y)%2&&!(LAused&bit(x))&&!(LAused&bit(y)),"modified matching");LAused|=bit(x)|bit(y);req(ds.add(x,y),"P plus LA labelled cycle");deg[x]++;deg[y]++;}
   U ends=0;for(int x=0;x<32;x++){req(deg[x]==0||(deg[x]>=1&&deg[x]<=2),"union degree");if(deg[x]==1)ends|=bit(x);}
   U S=J&~bit(w)&~bit(b),Q=((G&~covered)&~bit(q))|S;
   req(ends==Q&&pc(ends&evens)==14-m&&pc(ends&~evens)==14-m&&pc(ends)>=10,"exact balanced endpoints");req((ends&bit(14))&&(ends&bit(22))&&!(ends&bit(q))&&!(ends&bit(t)),"holes14,22/q/t endpoint roles");
   B major=B((TM[k]&~bit(t))|S),omit=B(S),Rpair=B(bit(w)|bit(b));req(!(Rpair&(major|1))&&pc(major)==11&&pc(omit)==5,"actual B / protected pair");
   int found=-1;for(int idx:{5,6,7})if(Bkeys.count({major,omit,Rpair,idx})){found=idx;break;}req(found>=0,"actual B common marked map absent");req(options.count({q,t,w,b,c,pi,found}),"record not among verified simultaneous options");Buse[found]++;
   codes.push_back(code);hist[m]++;
  }
  sort(codes.begin(),codes.end());req(adjacent_find(codes.begin(),codes.end())==codes.end(),"duplicate maximal matching");U total=0;for(int m=0;m<=10;m++){req(hist[m]==counts[k][m],"DP/valid unique cardinality histogram mismatch");total+=hist[m];}
  req(total==U(120463),"domain total");grand+=total;if(k)cout<<",";
  cout<<"{\"orbit\":"<<0<<",\"complete_domain\":"<<total<<",\"size8\":"<<hist[8]<<",\"size9\":"<<hist[9]<<",\"size10\":"<<hist[10]<<",\"all_positive_witnesses_and_actual_B_maps_verified\":true,\"B_class_counts\":{";
  bool comma=false;for(int idx=0;idx<42;idx++)if(Buse[idx]){if(comma)cout<<",";comma=true;cout<<"\""<<idx<<"\":"<<Buse[idx];}cout<<"}}";
 }
 req(grand==120463,"total domain");cout<<"],\"all_certificates_verified\":"<<grand<<",\"complete_by_independent_DP_and_legal_unique_equal_cardinality\":true}\n";
}catch(exception&e){cerr<<e.what()<<endl;return 1;}}
