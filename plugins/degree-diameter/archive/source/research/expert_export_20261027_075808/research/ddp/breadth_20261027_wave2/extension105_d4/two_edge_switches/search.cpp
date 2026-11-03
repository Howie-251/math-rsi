#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
constexpr int N=105,D=4,M=210;
using Edge=array<int,2>;using Bits=array<uint64_t,2>;
array<array<int,D>,N> base,adj;
array<Bits,N> b1,b2,b3;
vector<Edge> edges;
bool linked[N][N]{};
double cpu(clock_t start){return double(clock()-start)/CLOCKS_PER_SEC;}
void replace_neighbor(int u,int old,int now){auto it=find(adj[u].begin(),adj[u].end(),old);assert(it!=adj[u].end());*it=now;}
void make(int i,int j,int kind){
 adj=base;auto [a,b]=edges[i];auto[c,d]=edges[j];if(kind)swap(c,d);
 replace_neighbor(a,b,c);replace_neighbor(b,a,d);replace_neighbor(c,d,a);replace_neighbor(d,c,b);
}
int score(array<int,N>*misses=nullptr){
 for(int v=0;v<N;v++){b1[v].fill(0);b1[v][v/64]|=1ULL<<(v%64);for(int u:adj[v])b1[v][u/64]|=1ULL<<(u%64);}
 for(int v=0;v<N;v++){b2[v]=b1[v];for(int u:adj[v])for(int k=0;k<2;k++)b2[v][k]|=b1[u][k];}
 for(int v=0;v<N;v++){b3[v]=b2[v];for(int u:adj[v])for(int k=0;k<2;k++)b3[v][k]|=b2[u][k];}
 int total=0;for(int v=0;v<N;v++){Bits ball=b3[v];for(int u:adj[v])for(int k=0;k<2;k++)ball[k]|=b3[u][k];int missing=N-__builtin_popcountll(ball[0])-__builtin_popcountll(ball[1]);if(misses)(*misses)[v]=missing;total+=missing;}assert(total%2==0);return total/2;
}
vector<Edge> current_edges(){vector<Edge>e;for(int u=0;u<N;u++)for(int v:adj[u])if(u<v)e.push_back({u,v});sort(e.begin(),e.end());assert(e.size()==M);return e;}
void save(const string&out,int value,int i,int j,int kind){auto e=current_edges();ofstream f(out+"/best.edges");f<<N<<' '<<M<<'\n';for(auto p:e)f<<p[0]<<' '<<p[1]<<'\n';ofstream t(out+"/best.json");t<<"{\"n\":105,\"m\":210,\"degree\":4,\"target_D\":4,\"bad_unordered_pairs\":"<<value<<",\"removed_source_edge_ids\":["<<i<<','<<j<<"],\"pairing\":"<<kind<<",\"diameter\":\"pending root final check if improved\"}\n";}
int main(int argc,char**argv){
 assert(argc==3);string out=argv[1];double budget=stod(argv[2]);clock_t start=clock();
 ifstream f(out+"/source.edges");int n,m;f>>n>>m;assert(n==N&&m==M);array<int,N>deg{};
 for(int k=0;k<M;k++){int u,v;f>>u>>v;assert(u<v);edges.push_back({u,v});linked[u][v]=linked[v][u]=true;base[u][deg[u]++]=v;base[v][deg[v]++]=u;}for(int d:deg)assert(d==4);
 ifstream c(out+"/first.expected.deficits");array<int,N>expected;for(int&d:expected)c>>d;
 ifstream ef(out+"/first.expected.edges");ef>>n>>m;assert(n==N&&m==M);vector<Edge>expected_edges;for(int k=0;k<M;k++){Edge e;ef>>e[0]>>e[1];expected_edges.push_back(e);}sort(expected_edges.begin(),expected_edges.end());
 int best=8,besti=-1,bestj=-1,bestkind=-1,ci=0,cj=0,ck=0;bool first=true,hit=false,limited=false;
 long long pairs=0,overlap=0,pairings=0,existing=0,scored=0,improvements=0;
 for(int i=0;i<M;i++)for(int j=i+1;j<M;j++){
  ci=i;cj=j;pairs++;auto [a,b]=edges[i];auto [c0,d0]=edges[j];
  if(a==c0||a==d0||b==c0||b==d0){overlap++;continue;}
  for(int kind=0;kind<2;kind++){
   ck=kind;pairings++;int c=c0,d=d0;if(kind)swap(c,d);
   if(linked[a][c]||linked[b][d]){existing++;continue;}
   if((scored&255)==0&&cpu(start)>=budget){limited=true;goto finish;}
   make(i,j,kind);array<int,N>misses;int value=score(first?&misses:nullptr);scored++;
   if(first){assert(misses==expected);assert(current_edges()==expected_edges);first=false;ofstream q(out+"/first.cpp_calibration.json");q<<"{\"status\":\"MATCH\",\"complete_edges_equal\":true,\"all105_radius4_deficits_equal\":true,\"first_score_reused\":true,\"bad_pairs\":"<<value<<"}\n";}
   if(value<best){best=value;besti=i;bestj=j;bestkind=kind;improvements++;save(out,best,i,j,kind);if(best==0){hit=true;goto finish;}}
  }
 }
 finish:
 if(!hit&&!limited){assert(pairs==21945);assert(overlap==630);assert(pairings==42630);assert(scored+existing==42630);}
 string status=hit?"FOUND_D4":limited?"CPU_LIMIT_NEIGHBORHOOD_PREFIX_NO_D4":"COMPLETE_TWO_EDGE_SWITCH_NEIGHBORHOOD_NO_D4";
 ofstream t(out+"/terminal.json");t<<"{\"status\":\""<<status<<"\",\"running\":false,\"found_D4\":"<<(hit?"true":"false")<<",\"source_bad_pairs\":8,\"best_bad_pairs\":"<<best<<",\"edge_pairs_seen\":"<<pairs<<",\"overlapping_edge_pairs\":"<<overlap<<",\"disjoint_pairing_proposals\":"<<pairings<<",\"existing_edge_rejections\":"<<existing<<",\"legal_neighbors_scored\":"<<scored<<",\"strict_improvements\":"<<improvements<<",\"best_removed_ids\":["<<besti<<','<<bestj<<"],\"best_pairing\":"<<bestkind<<",\"cursor\":["<<ci<<','<<cj<<','<<ck<<"],\"production_CPU_seconds\":"<<cpu(start)<<",\"scope_exhausted\":"<<(!hit&&!limited?"true":"false")<<",\"general105_graphs_excluded\":false,\"workers\":1,\"restarts\":0}\n";
 cout<<status<<" best "<<best<<" scored "<<scored<<" CPU "<<cpu(start)<<endl;
}
