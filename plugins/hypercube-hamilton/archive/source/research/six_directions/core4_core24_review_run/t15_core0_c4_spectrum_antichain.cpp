// c4 diagnostic: complete A forest spectra, closed under all crossing bijections.
#include <array>
#include <vector>
#include <map>
#include <set>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <cassert>
#include <cstdint>
using namespace std;
using Edges=vector<pair<int,int>>;
struct DSU{int p[40];bool ok=true;DSU(){for(int i=0;i<40;++i)p[i]=i;}int root(int v){return p[v]==v?v:p[v]=root(p[v]);}void add(int a,int b){int x=root(a),y=root(b);if(x==y)ok=false;else p[x]=y;}};
array<vector<Edges>,3> pats;
array<int,16> fa;array<int,4> ports;
array<int,6> rm;vector<array<int,6>> matchings;map<unsigned,int> mi;
map<uint64_t,long long> types;ofstream witnesses;
unsigned code(const array<int,6>& m){unsigned x=0;for(int i=0;i<6;++i)x|=unsigned(m[i])<<(3*i);return x;}
void genR(unsigned mask){if(!mask){mi[code(rm)]=matchings.size();matchings.push_back(rm);return;}int a=__builtin_ctz(mask);for(int b=a+1;b<6;++b)if(mask>>b&1){rm[a]=b;rm[b]=a;genR(mask&~(1u<<a)&~(1u<<b));}}
void genN(unsigned mask,Edges cur,int f){if(!mask){pats[f].push_back(cur);return;}int a=__builtin_ctz(mask);for(int b=a+1;b<16;++b)if((mask>>b&1)&&__builtin_popcount(unsigned(a^b))==1){auto n=cur;n.emplace_back(a,b);genN(mask&~(1u<<a)&~(1u<<b),n,f);}}
void assess(){int us[3]={3,5,6};uint64_t signature=0;
 for(int f=0;f<3;++f){array<int,6> ep;for(int i=0;i<4;++i)ep[i]=ports[i];int k=4;for(int v:us)if(v!=us[f])ep[k++]=v;
  for(auto& n:pats[f]){DSU g;for(int a=1;a<16;++a)if(fa[a]>a)g.add(a,fa[a]);for(auto [a,b]:n)g.add(a,b);if(!g.ok)continue;array<int,6> m;for(int i=0;i<6;++i){m[i]=-1;for(int j=0;j<6;++j)if(i!=j&&g.root(ep[i])==g.root(ep[j])){assert(m[i]<0);m[i]=j;}assert(m[i]>=0);}signature|=1ull<<(15*f+mi.at(code(m)));}
 }
 ++types[signature];witnesses<<signature;for(int v:ports)witnesses<<' '<<v;for(int a=1;a<16;++a)if(fa[a]>a)witnesses<<' '<<a<<' '<<fa[a];witnesses<<'\n';
}
void pairA(unsigned mask){if(!mask){assess();return;}int a=__builtin_ctz(mask);for(int b=a+1;b<16;++b)if(mask>>b&1){fa[a]=b;fa[b]=a;pairA(mask&~(1u<<a)&~(1u<<b));fa[a]=fa[b]=-1;}}
void portChoose(vector<int> base,int pos,int at,unsigned mask){if(at==4){pairA(mask);return;}for(int i=pos;i<(int)base.size();++i){ports[at]=base[i];portChoose(base,i+1,at+1,mask&~(1u<<base[i]));}}
int main(int argc,char**argv){assert(argc==2);genR(63u);assert(matchings.size()==15);int us[3]={3,5,6};
 for(int f=0;f<3;++f){int u=us[f];for(int i=0;i<4;++i)for(int j=i+1;j<4;++j){int a=u^(1<<i),b=u^(1<<j);genN(65534u&~(1u<<u)&~(1u<<a)&~(1u<<b),{{u,a},{u,b}},f);}assert(pats[f].size()==116);}
 fa.fill(-1);witnesses.open(argv[1]);vector<int> base;unsigned mask=0;for(int v=1;v<16;++v)if(v!=3&&v!=5&&v!=6){base.push_back(v);mask|=1u<<v;}portChoose(base,0,0,mask);witnesses.close();
 set<uint64_t> expanded;array<int,4> perm={0,1,2,3};do{int transform[15];for(int r=0;r<15;++r){array<int,6> m;for(int i=0;i<6;++i){int ni=i<4?perm[i]:i;int oldmate=matchings[r][i];m[ni]=oldmate<4?perm[oldmate]:oldmate;}transform[r]=mi.at(code(m));}for(auto [sig,count]:types){uint64_t s=0;for(int f=0;f<3;++f)for(int r=0;r<15;++r)if(sig>>(15*f+r)&1ull)s|=1ull<<(15*f+transform[r]);expanded.insert(s);}}while(next_permutation(perm.begin(),perm.end()));
 vector<uint64_t> sorted(expanded.begin(),expanded.end());sort(sorted.begin(),sorted.end(),[](uint64_t a,uint64_t b){int x=__builtin_popcountll(a),y=__builtin_popcountll(b);return x!=y?x<y:a<b;});vector<uint64_t> minimal;
 for(uint64_t s:sorted){bool dominated=false;for(uint64_t t:minimal)if((t&s)==t){dominated=true;break;}if(!dominated)minimal.push_back(s);}
 long long total=0;for(auto [s,n]:types)total+=n;assert(total==51975);
 cout<<"{\"scope\":\"c4 A spectrum producer diagnostic\",\"A_partials\":"<<total<<",\"A_spectrum_types\":"<<types.size()<<",\"expanded_types\":"<<expanded.size()<<",\"minimal_antichain_count\":"<<minimal.size()<<",\"minimal_masks\":[";for(int i=0;i<(int)minimal.size();++i){if(i)cout<<",";cout<<minimal[i];}cout<<"]}\n";
}
