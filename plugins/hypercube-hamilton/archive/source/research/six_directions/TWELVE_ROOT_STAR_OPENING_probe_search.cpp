#include <bits/stdc++.h>
using namespace std;
constexpr int N=28,R=8192;
using Bits=bitset<R>;
vector<int> H,U,K;int indexK[32];vector<vector<int>> columns;
array<Bits,R> pivots,combos;vector<Bits> rows;
vector<array<unsigned char,28>> selectedPairs;
vector<array<unsigned char,32>> selectedForests;
vector<long long> selectedIndices;long long examined=0,limitRows=2000000;bool done=false;
vector<vector<int>> basis(int n){
 if(n==2)return {{1,0}};vector<vector<int>> result;
 for(auto a:basis(n-2)){
  auto b=a;int partner=a[n-3];b.resize(n);b[n-2]=partner;b[partner]=n-2;b[n-3]=n-1;b[n-1]=n-3;result.push_back(b);
  a.push_back(n-1);a.push_back(n-2);result.push_back(a);
 }return result;
}
bool conn(const array<unsigned char,N>&a,const vector<int>&b){int x=0;for(int k=1;k<=N/2;++k){x=b[a[x]];if(x==0)return k==N/2;}throw runtime_error("bad pairing");}
int root(array<unsigned char,32>&p,int x){while(p[x]!=x)x=p[x];return x;}
void submit(const vector<pair<int,int>>&edges){
 vector<vector<int>> adj(32);for(auto[a,b]:edges){adj[a].push_back(b);adj[b].push_back(a);}
 array<unsigned char,N> pairing;pairing.fill(255);
 for(int a:K){int previous=a,x=adj[a][0];while(indexK[x]<0){int next=adj[x][0]==previous?adj[x][1]:adj[x][0];previous=x;x=next;}pairing[indexK[a]]=indexK[x];}
 Bits v;for(int j=0;j<R;++j)v[j]=conn(pairing,columns[j]);auto original=v;Bits combo;combo[rows.size()]=1;
 for(int j=R-1;j>=0;--j)if(v[j]){
  if(pivots[j].any()){v^=pivots[j];combo^=combos[j];}
  else{
   pivots[j]=v;combos[j]=combo;rows.push_back(original);selectedIndices.push_back(examined);
   vector<pair<int,int>> pairs;for(int i=0;i<N;++i)if(i<pairing[i])pairs.push_back({K[i],K[pairing[i]]});sort(pairs.begin(),pairs.end());
   array<unsigned char,28> rec;int at=0;for(auto[a,b]:pairs){rec[at++]=a;rec[at++]=b;}selectedPairs.push_back(rec);
   auto sorted=edges;for(auto&e:sorted)if(e.first>e.second)swap(e.first,e.second);sort(sorted.begin(),sorted.end());
   array<unsigned char,32> f;at=0;for(auto[a,b]:sorted){f[at++]=a;f[at++]=b;}selectedForests.push_back(f);
   if(rows.size()%128==0)cerr<<"forests="<<examined+1<<" rank="<<rows.size()<<"\n";
   break;
  }
 }
 ++examined;if(examined%10000==0)cerr<<"forests="<<examined<<" rank="<<rows.size()<<"\n";
 if(rows.size()==R||examined>=limitRows)done=true;
}
void enumerate(array<unsigned char,32>need,array<unsigned char,32>p,vector<pair<int,int>>&edges){
 if(done)return;
 int best=-1,bestCount=100;vector<int> choices;
 for(int x=0;x<32;++x)if(need[x]){
  vector<int> q;for(int d=0;d<5;++d){int y=x^(1<<d);if(need[y]&&root(p,x)!=root(p,y))q.push_back(y);}
  if(q.size()<need[x])return;
  int count=need[x]==1?q.size():q.size()*(q.size()-1)/2;
  if(count<bestCount){best=x;bestCount=count;choices=q;}
 }
 if(best<0){if(edges.size()!=16)throw runtime_error("bad degree total");submit(edges);return;}
 int x=best,n=need[x];
 for(int i=0;i<(int)choices.size();++i)for(int j=(n==1?i:i+1);j<(n==1?i+1:(int)choices.size());++j){
  auto next=need;auto parents=p;vector<int> take{choices[i]};if(n==2)take.push_back(choices[j]);bool legal=true;
  next[x]=0;
  for(int y:take){int a=root(parents,x),b=root(parents,y);if(a==b){legal=false;break;}parents[a]=b;--next[y];}
  if(!legal)continue;
  for(int y:take)edges.push_back({x,y});enumerate(next,parents,edges);for(int y:take)edges.pop_back();
  if(done)return;
 }
}
int main(int argc,char**argv){
 if(argc<3)return 2;ifstream cfg(argv[1]);for(int i=0,x;i<4;++i){cfg>>x;H.push_back(x);}for(int i=0,x;i<2;++i){cfg>>x;U.push_back(x);}
 if(!cfg)return 3;if(argc>3)limitRows=stoll(argv[3]);fill(indexK,indexK+32,-1);
 for(int x=0;x<32;++x)if(find(H.begin(),H.end(),x)==H.end()){indexK[x]=K.size();K.push_back(x);}
 if(K.size()!=28)return 4;columns=basis(N);if(columns.size()!=R)return 5;
 for(int i=0;i<R;++i){array<unsigned char,N>a;copy(columns[i].begin(),columns[i].end(),a.begin());for(int j=0;j<R;++j)if(conn(a,columns[j])!=(j==(i^(R-1))))return 6;}
 cerr<<"basis8192 permutation check PASS\n";
 array<unsigned char,32>need,p;for(int x=0;x<32;++x){p[x]=x;need[x]=find(U.begin(),U.end(),x)!=U.end()?0:indexK[x]>=0?1:2;}
 int forceA,forceB;cfg>>forceA>>forceB;if(!cfg||forceA<0||forceA>=32||forceB<0||forceB>=32||__builtin_popcount(unsigned(forceA^forceB))!=1||!need[forceA]||!need[forceB])return 9;--need[forceA];--need[forceB];p[forceA]=forceB;vector<pair<int,int>> edges{{forceA,forceB}};enumerate(need,p,edges);
 string pre=argv[2];ofstream meta(pre+".json");meta<<"{\"status\":\"PRODUCER_RANK_SEARCH\",\"forests_examined\":"<<examined<<",\"rank_GF2\":"<<rows.size()<<",\"full_rank\":"<<(rows.size()==R?"true":"false")<<",\"selected_indices\":[";
 for(int i=0;i<(int)selectedIndices.size();++i){if(i)meta<<',';meta<<selectedIndices[i];}meta<<"]}\n";
 auto dump=[](ofstream&f,const Bits&b){for(int j=0;j<R/8;++j){unsigned char c=0;for(int k=0;k<8;++k)if(b[8*j+k])c|=1<<k;f.put(char(c));}};
 ofstream mf(pre+"_matrix.bin",ios::binary),ff(pre+"_forests.bin",ios::binary),pf(pre+"_pairs.bin",ios::binary),cf(pre+"_columns.bin",ios::binary),tf(pre+"_pivots.bin",ios::binary),co(pre+"_combos.bin",ios::binary);
 for(int i=0;i<(int)rows.size();++i){dump(mf,rows[i]);ff.write((char*)selectedForests[i].data(),32);pf.write((char*)selectedPairs[i].data(),28);}
 for(int i=0;i<R;++i){dump(tf,pivots[i]);dump(co,combos[i]);for(int j=0;j<N;++j)if(j<columns[i][j]){cf.put(char(K[j]));cf.put(char(K[columns[i][j]]));}}
 cout<<"forests="<<examined<<" rank="<<rows.size()<<"\n";
}
