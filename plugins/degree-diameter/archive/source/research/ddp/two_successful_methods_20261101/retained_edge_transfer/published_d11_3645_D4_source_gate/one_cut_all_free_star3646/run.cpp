#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <vector>
using namespace std;
int main(){
 ifstream in("SOURCE.header.edges");int n,m;in>>n>>m;assert(n==3645&&m==20044);vector<vector<int>> g(n);vector<pair<int,int>> edges;int u,v;while(in>>u>>v){edges.emplace_back(u,v);g[u].push_back(v);g[v].push_back(u);}assert((int)edges.size()==m);int W=(n+63)/64;
 vector<int> F={3456,3489,3564,3571,3583,3603,3643};vector<bool> freep(n,false);for(int x:F)freep[x]=true;vector<uint64_t> holes(W);ifstream hi("HOLES.txt");int count;hi>>count;assert(count==743);for(int i=0;i<count;i++){int x;hi>>x;holes[x/64]|=1ULL<<(x%64);}
 vector<vector<uint64_t>> balls(n,vector<uint64_t>(W));vector<bool> cached(n,false);ifstream meta("CACHED_ROOTS.txt"),bin("CACHED_R3.bin",ios::binary);int cachedN,words;meta>>cachedN>>words;assert(words==W);for(int i=0;i<cachedN;i++){int r;meta>>r;assert(!cached[r]);cached[r]=true;bin.read((char*)balls[r].data(),8*W);assert(bin);}
 int newqueries=0;vector<int> dist(n),q(n);for(int r=0;r<n;r++)if(!cached[r]){newqueries++;fill(dist.begin(),dist.end(),-1);int a=0,b=0;dist[r]=0;q[b++]=r;balls[r][r/64]|=1ULL<<(r%64);while(a<b){int x=q[a++];if(dist[x]==3)continue;for(int y:g[x])if(dist[y]<0){dist[y]=dist[x]+1;q[b++]=y;balls[r][y/64]|=1ULL<<(y%64);}}}
 ofstream bc("ALL_SOURCE_R3_SUPPORTS.bin",ios::binary);for(auto& row:balls)bc.write((char*)row.data(),8*W);bc.close();ofstream stats("ALL_EDGES.tsv");stats<<"edge_index\tu\tv\ttype\tnewroot_missing\toldold_status\n";
 int pass=0,fail=0,bfs=0,sourcepair=0,bestmissing=n,bu=-1,bv=-1;bool hit=false,savedfirst=false;vector<int> d(n+1),parent(n+1),queue(n+1);map<string,array<int,4>> cls;
 for(int ei=0;ei<m;ei++){
  auto [cu,cv]=edges[ei];string type=(cu>=3444&&cv>=3444)?"inserted_inserted":(cu<3444&&cv<3444)?"base_base":"base_inserted";auto& z=cls[type];z[0]++;int missing=0;for(int w=0;w<W;w++)missing+=__builtin_popcountll(holes[w]&~(balls[cu][w]|balls[cv][w]));if(missing<bestmissing){bestmissing=missing;bu=cu;bv=cv;}
  if(missing){z[1]++;stats<<ei<<'\t'<<cu<<'\t'<<cv<<'\t'<<type<<'\t'<<missing<<"\tNOT_ENTERED\n";continue;}
  pass++;z[2]++;vector<int> P=F;P.push_back(cu);P.push_back(cv);sort(P.begin(),P.end());P.erase(unique(P.begin(),P.end()),P.end());vector<bool> pin(n,false);for(int x:P)pin[x]=true;vector<int> roots={cu,cv};for(int x:F)roots.push_back(x);for(int x=0;x<n;x++)roots.push_back(x);vector<bool> done(n,false);bool valid=true;
  for(int r:roots){if(done[r])continue;done[r]=true;bfs++;fill(d.begin(),d.end(),-1);fill(parent.begin(),parent.end(),-1);int a=0,b=0;d[r]=0;queue[b++]=r;
   auto put=[&](int y,int x){if(d[y]<0){d[y]=d[x]+1;parent[y]=x;queue[b++]=y;}};
   while(a<b){int x=queue[a++];if(d[x]==4)continue;if(x==n){for(int y:P)put(y,x);}else{for(int y:g[x])if(!((x==cu&&y==cv)||(x==cv&&y==cu)))put(y,x);if(pin[x])put(n,x);}}
   if(b<n+1){valid=false;fail++;z[3]++;if(!savedfirst){savedfirst=true;int t=0;while(d[t]>=0)t++;sourcepair++;vector<int> sd(n,-1),sp(n,-1),sq(n);int aa=0,bb=0;sd[r]=0;sq[bb++]=r;while(aa<bb&&sd[t]<0){int x=sq[aa++];for(int y:g[x])if(sd[y]<0){sd[y]=sd[x]+1;sp[y]=x;sq[bb++]=y;}}assert(sd[t]==4);vector<int> op;for(int x=t;x>=0;x=sp[x])op.push_back(x);reverse(op.begin(),op.end());vector<int> np;bool replaced=false;for(int i=0;i<(int)op.size();i++){np.push_back(op[i]);if(i+1<(int)op.size()&&((op[i]==cu&&op[i+1]==cv)||(op[i]==cv&&op[i+1]==cu))){np.push_back(n);replaced=true;}}assert(replaced&&np.size()==6);ofstream ce("FIRST_OLD_FAILURE.json");ce<<"{\"cut\":["<<cu<<','<<cv<<"],\"root\":"<<r<<",\"target\":"<<t<<",\"source_distance\":4,\"new_distance\":5,\"source_path\":[";for(int i=0;i<(int)op.size();i++)ce<<op[i]<<(i+1==(int)op.size()?']':',');ce<<",\"new_path\":[";for(int i=0;i<(int)np.size();i++)ce<<np[i]<<(i+1==(int)np.size()?']':',');ce<<"}\n";}break;}
  }
  stats<<ei<<'\t'<<cu<<'\t'<<cv<<'\t'<<type<<"\t0\t"<<(valid?"FULL_D4_HIT":"OLDOLD_FAIL")<<'\n';
  if(valid){hit=true;ofstream out("CANDIDATE3646.edges");out<<n+1<<' '<<m-1+P.size()<<'\n';for(auto [a,b]:edges)if(!((a==cu&&b==cv)||(a==cv&&b==cu)))out<<a<<' '<<b<<'\n';for(int x:P)out<<x<<' '<<n<<'\n';break;}
 }
 ofstream out("NATIVE_RESULT.json");out<<"{\"source_n\":"<<n<<",\"source_m\":"<<m<<",\"domain_edges\":"<<m<<",\"cached_R3_roots_reused\":"<<cachedN<<",\"new_R3_queries\":"<<newqueries<<",\"newroot_pass\":"<<pass<<",\"oldold_fail\":"<<fail<<",\"candidate_oldroot_BFS\":"<<bfs<<",\"source_singlepair_diagnostic_queries\":"<<sourcepair<<",\"best_missing_holes\":"<<bestmissing<<",\"best_cut\":["<<bu<<','<<bv<<"],\"full_D4_hit\":"<<(hit?"true":"false")<<",\"complete_domain\":"<<(!hit?"true":"false")<<",\"classes\":{";bool sep=false;for(auto [type,z]:cls){if(sep)out<<',';sep=true;out<<'\"'<<type<<"\":{\"edges\":"<<z[0]<<",\"newroot_fail\":"<<z[1]<<",\"newroot_pass\":"<<z[2]<<",\"oldold_fail\":"<<z[3]<<'}';}out<<"}}\n";
}
