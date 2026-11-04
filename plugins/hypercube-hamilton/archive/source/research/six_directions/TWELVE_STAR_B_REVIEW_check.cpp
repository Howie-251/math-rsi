#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <iterator>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Bits=array<uint64_t,16>;
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
vector<unsigned char> load(const string&f,size_t n){
 ifstream in(f,ios::binary);need(bool(in),"missing "+f);
 vector<unsigned char> a((istreambuf_iterator<char>(in)),{});
 need(a.size()==n,"size "+f);return a;
}
struct DSU{
 array<int,32> p; int components;
 DSU(int n=32):components(n){iota(p.begin(),p.end(),0);}
 int find(int x){while(p[x]!=x){p[x]=p[p[x]];x=p[x];}return x;}
 bool join(int a,int b){a=find(a);b=find(b);if(a==b)return false;p[a]=b;--components;return true;}
};
Bits decode(const vector<unsigned char>&a,int row){
 Bits b{};for(int j=0;j<128;++j)b[j/8]|=uint64_t(a[row*128+j])<<(8*(j%8));return b;
}
vector<pair<int,int>> pairs(const unsigned char*a,const vector<int>&K,int count=11){
 uint32_t seen=0,expected=0;for(int x:K)expected|=uint32_t(1)<<x;
 vector<pair<int,int>> ans;
 for(int i=0;i<count;++i){int x=a[2*i],y=a[2*i+1];need(x<32&&y<32&&x!=y,"pair domain");
  uint32_t m=(uint32_t(1)<<x)|(uint32_t(1)<<y);need(!(seen&m),"pair repeated endpoint");seen|=m;
  ans.push_back(minmax(x,y));
 }need(seen==expected,"pair endpoint set");sort(ans.begin(),ans.end());return ans;
}
int main(){try{
 ifstream table("TWELVE_STAR_B_REVIEW_geometries.txt");need(bool(table),"geometry table");
 int idx,number=0;long long forests=0,bits=0,comboChecks=0;
 cout<<"{\"rows\":[";
 while(table>>idx){
  vector<int> H(8),U(3);int fp,fq;for(int&x:H)need(bool(table>>x),"geometry H");for(int&x:U)need(bool(table>>x),"geometry U");need(bool(table>>fp>>fq),"forced pair");
  string sn=to_string(idx);if(sn.size()==1)sn="0"+sn;string pre="TWELVE_STAR_B_orbit_"+sn;
  ifstream cfg(pre+"_config.txt");vector<int> got;int z;while(cfg>>z)got.push_back(z);
  vector<int> want=H;want.insert(want.end(),U.begin(),U.end());want.push_back(fp);want.push_back(fq);need(got==want,"config geometry "+sn);
  array<int,32> degrees{};array<int,32> pos;pos.fill(-1);vector<int>K;
  for(int x=0;x<32;++x){if(find(H.begin(),H.end(),x)==H.end()){pos[x]=K.size();K.push_back(x);degrees[x]=1;}
   else degrees[x]=find(U.begin(),U.end(),x)==U.end()?2:0;
  }need(K.size()==24,"K size");vector<int>Kminus;for(int x:K)if(x!=fp&&x!=fq)Kminus.push_back(x);need(Kminus.size()==22,"reduced K size");pos.fill(-1);for(int i=0;i<22;++i)pos[Kminus[i]]=i;
  auto fs=load(pre+"_forests.bin",1024*34),ps=load(pre+"_pairs.bin",1024*22),cs=load(pre+"_columns.bin",1024*22);
  auto fullpairs=load(pre+"_full_pairs.bin",1024*24);
  auto mat=load(pre+"_matrix.bin",1024*128),piv=load(pre+"_pivots.bin",1024*128),comb=load(pre+"_combos.bin",1024*128);
  vector<vector<pair<int,int>>> derived(1024),cols(1024);
  for(int i=0;i<1024;++i){
   DSU d;array<int,32> deg{};bool used[32][32]{};
   for(int j=0;j<17;++j){int a=fs[i*34+2*j],b=fs[i*34+2*j+1];need(a<32&&b<32&&__builtin_popcount(unsigned(a^b))==1,"nonshort forest");
    need(!used[a][b],"duplicate edge");used[a][b]=used[b][a]=true;need(d.join(a,b),"forest cycle");++deg[a];++deg[b];
   }need(deg==degrees,"forest degrees");
   vector<vector<int>> ends(32);for(int x:K)ends[d.find(x)].push_back(x);
   vector<pair<int,int>> actual;
   for(auto &v:ends)if(!v.empty()){need(v.size()==2,"component terminal count");actual.push_back(minmax(v[0],v[1]));}
   need(actual.size()==12,"component number");sort(actual.begin(),actual.end());
   need(used[0][fp]&&used[0][fq],"forced physical cherry missing");need(actual==pairs(&fullpairs[i*24],K,12),"full endpoint matching mismatch");auto forced=minmax(fp,fq);auto it=find(actual.begin(),actual.end(),pair<int,int>(forced));need(it!=actual.end(),"forced pair absent");actual.erase(it);need(actual==pairs(&ps[i*22],Kminus),"reduced endpoint matching mismatch");
   for(auto [a,b]:actual)derived[i].push_back({pos[a],pos[b]});
   auto cp=pairs(&cs[i*22],Kminus);for(auto[a,b]:cp)cols[i].push_back({pos[a],pos[b]});
   ++forests;
  }
  vector<Bits> rebuilt(1024);
  for(int i=0;i<1024;++i){DSU base(22);for(auto[a,b]:derived[i])base.join(a,b);
   for(int j=0;j<1024;++j){DSU d=base;for(auto[a,b]:cols[j])d.join(a,b);
    bool v=d.components==1;bool stored=(mat[i*128+j/8]>>(j%8))&1;
    need(v==stored,"connectivity mismatch "+sn+" "+to_string(i)+" "+to_string(j));
    if(v)rebuilt[i][j/64]|=uint64_t(1)<<(j%64);++bits;
   }
  }
  // Independent rank: ascending pivots on reconstructed rows, not supplied pivots.
  array<Bits,1024> basis{};array<bool,1024> active{};int rank=0;
  for(auto row:rebuilt){for(int w=0;w<16;++w){while(row[w]){
    int j=w*64+__builtin_ctzll(row[w]);
    if(!active[j]){basis[j]=row;active[j]=true;++rank;goto nextrow;}
    for(int q=w;q<16;++q)row[q]^=basis[j][q];
   }}nextrow:;}
  need(rank==1024,"rank deficient "+sn);
  // Also validate all producer combination equations and highest-pivot positions.
  for(int i=0;i<1024;++i){Bits b=decode(piv,i),co=decode(comb,i),sum{};
   need((b[i/64]>>(i%64))&1,"pivot missing");
   for(int j=i+1;j<1024;++j)need(!((b[j/64]>>(j%64))&1),"pivot leading position");
   for(int w=0;w<16;++w)while(co[w]){int j=w*64+__builtin_ctzll(co[w]);co[w]&=co[w]-1;for(int q=0;q<16;++q)sum[q]^=rebuilt[j][q];}
   need(sum==b,"combo mismatch "+sn);++comboChecks;
  }
  if(number++)cout<<",";cout<<"{\"index\":"<<idx<<",\"rank\":"<<rank<<",\"forests\":1024,\"connectivity_bits\":1048576}";
  cerr<<"verified "<<idx<<" rank "<<rank<<"\n";
 }
 need(number==10,"claimed row count");cout<<"],\"rows_checked\":"<<number<<",\"forests_checked\":"<<forests<<",\"connectivity_bits_checked\":"<<bits<<",\"combination_equations_checked\":"<<comboChecks<<",\"pass\":true}\n";
}catch(const exception&e){cerr<<"CHECK FAILED: "<<e.what()<<"\n";return 1;}return 0;}
