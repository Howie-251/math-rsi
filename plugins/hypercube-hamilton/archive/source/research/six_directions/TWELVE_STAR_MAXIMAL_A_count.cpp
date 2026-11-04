#include <bits/stdc++.h>
using namespace std;using U=uint64_t;
vector<int> E,O,T;int ei[32],oi[32];vector<vector<int>> adj;
vector<array<int,32>> groupMaps;vector<int> partner,order;
array<U,12> bysize{};map<pair<int,int>,U> bySizeStab;U total=0;
void search(int step,int used,int required,int size){
 if(__builtin_popcount(unsigned(required&~used))>int(O.size())-step)return;
 if(step==(int)O.size()){
  if(required&~used)return;
  int stab=0;
  for(auto&g:groupMaps){bool fixed=true;for(int i=0;i<(int)O.size();++i){
    int j=oi[g[O[i]]];int p=partner[i];int image=p<0?-1:ei[g[E[p]]];
    if(partner[j]!=image){fixed=false;break;}
   }if(fixed)++stab;
  }
  assert(stab>0&&groupMaps.size()%stab==0);++total;++bysize[size];++bySizeStab[{size,stab}];return;
 }
 int i=order[step],x=O[i];
 for(int e:adj[i])if(!(used>>e&1)){partner[i]=e;search(step+1,used|(1<<e),required,size+1);}
 if(find(T.begin(),T.end(),x)==T.end()){
  partner[i]=-1;int all=0;for(int e:adj[i])all|=1<<e;
  search(step+1,used,required|all,size);
 }
 partner[i]=-2;
}
int main(int argc,char**argv){
 if(argc!=3)return 2;int which=stoi(argv[1]);vector<vector<int>> Ts={{7,11,13,19,21},{7,11,13,19,31},{7,11,13,22,31},{7,11,19,28,31},{7,11,21,25,31},{7,11,21,26,31}};
 T=Ts.at(which);fill(ei,ei+32,-1);fill(oi,oi+32,-1);
 for(int x=1;x<32;++x){if(__builtin_popcount(unsigned(x))%2==0){ei[x]=E.size();E.push_back(x);}else if(__builtin_popcount(unsigned(x))>=3){oi[x]=O.size();O.push_back(x);}}
 assert(E.size()==15&&O.size()==11);adj.resize(11);partner.assign(11,-2);
 for(int i=0;i<11;++i)for(int j=0;j<15;++j)if(__builtin_popcount(unsigned(O[i]^E[j]))==1)adj[i].push_back(j);
 for(int x:T)order.push_back(oi[x]);for(int i=0;i<11;++i)if(find(order.begin(),order.end(),i)==order.end())order.push_back(i);
 array<int,5> perm{0,1,2,3,4};
 do{array<int,32> m{};for(int x=0;x<32;++x)for(int d=0;d<5;++d)m[x]|=((x>>perm[d])&1)<<d;
  vector<int> image;for(int x:T)image.push_back(m[x]);sort(image.begin(),image.end());auto sortedT=T;sort(sortedT.begin(),sortedT.end());if(image==sortedT)groupMaps.push_back(m);
 }while(next_permutation(perm.begin(),perm.end()));
 search(0,0,0,0);
 U orbits=0;map<int,U> orbitSizes;
 for(auto[key,n]:bySizeStab){int orbit=groupMaps.size()/key.second;assert(n%orbit==0);orbits+=n/orbit;orbitSizes[orbit]+=n/orbit;}
 ofstream f(argv[2]);f<<"{\"status\":\"PRODUCER_EXACT_LOCAL_MAXIMAL_MATCHING_COUNT\",\"star_orbit\":"<<which<<",\"T\":[";
 for(int i=0;i<5;++i){if(i)f<<',';f<<T[i];}f<<"],\"group_order\":"<<groupMaps.size()<<",\"maximal_matchings\":"<<total<<",\"stabilizer_orbits\":"<<orbits<<",\"by_edge_count\":{";bool comma=false;
 for(int i=0;i<12;++i)if(bysize[i]){if(comma)f<<',';comma=true;f<<'"'<<i<<"\":"<<bysize[i];}f<<"},\"orbits_by_size\":{";comma=false;
 for(auto[sz,n]:orbitSizes){if(comma)f<<',';comma=true;f<<'"'<<sz<<"\":"<<n;}f<<"},\"star_Q6_closed\":false,\"monotonic_extension_lemma_accepted\":false}\n";
 cout<<which<<" maximal="<<total<<" group="<<groupMaps.size()<<" orbits="<<orbits<<endl;
}
