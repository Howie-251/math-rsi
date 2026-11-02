#include <algorithm>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;using U=uint64_t;
int main(int argc,char**argv){
 clock_t begin=clock();string dir=argv[2];ifstream in(argv[1],ios::binary);uint32_t n,m2;in.read((char*)&n,4);in.read((char*)&m2,4);assert(n==20400&&m2==122400);
 vector<uint32_t>off(n+1),adj(m2);in.read((char*)off.data(),4*(n+1));in.read((char*)adj.data(),4*m2);
 for(uint32_t u=0;u<n;u++)assert(off[u+1]-off[u]==6);
 vector<int>neighbors(adj.begin()+off[0],adj.begin()+off[1]);sort(neighbors.begin(),neighbors.end());vector<int>sources{0};sources.insert(sources.end(),neighbors.begin(),neighbors.end());
 int W=(n+63)/64;vector<vector<U>>r6(7,vector<U>(W)),r3(7,vector<U>(W));vector<int>sizes;
 for(int k=0;k<7;k++){
  vector<int>d(n,-1),q(n);int lo=0,hi=0;d[sources[k]]=0;q[hi++]=sources[k];
  while(lo<hi){int u=q[lo++];if(d[u]==6)continue;for(uint32_t z=off[u];z<off[u+1];z++){int v=adj[z];if(d[v]<0){d[v]=d[u]+1;q[hi++]=v;}}}
  sizes.push_back(hi);for(uint32_t u=0;u<n;u++)if(d[u]>=0){r6[k][u/64]|=U(1)<<(u%64);if(d[u]<=3)r3[k][u/64]|=U(1)<<(u%64);}
 }
 ofstream cache(dir+"/source_R6_R3.u64le.bin",ios::binary);for(int k=0;k<7;k++){cache.write((char*)r6[k].data(),W*8);cache.write((char*)r3[k].data(),W*8);}cache.close();
 struct Row{int v,covered,firstmiss,roots,br,bt;};vector<Row>rows;long long bfses=0;bool hit=false;
 for(int k=1;k<=6;k++){
  int v=neighbors[k-1],covered=0,first=-1;for(int w=0;w<W;w++){U bits=r6[0][w]|r6[k][w];covered+=__builtin_popcountll(bits);}
  for(uint32_t u=0;u<n;u++)if(!((r6[0][u/64]|r6[k][u/64])>>(u%64)&1)){first=u;break;}
  Row row{v,covered,first,0,-1,-1};if(covered!=int(n)){rows.push_back(row);continue;}
  vector<int>roots{int(n)};for(uint32_t u=0;u<n;u++)if((r3[0][u/64]|r3[k][u/64])>>(u%64)&1)roots.push_back(u);
  assert(roots.size()<=375);
  for(int root:roots){
   vector<int>d(n+1,-1),q(n+1);int lo=0,hi=0;d[root]=0;q[hi++]=root;
   while(lo<hi){int u=q[lo++];if(d[u]==7)continue;
    if(u==int(n)){for(int y:{0,v})if(d[y]<0){d[y]=d[u]+1;q[hi++]=y;}}
    else for(uint32_t z=off[u];z<off[u+1];z++){int y=adj[z];if((u==0&&y==v)||(u==v&&y==0))y=n;if(d[y]<0){d[y]=d[u]+1;q[hi++]=y;}}
   }
   ++row.roots;++bfses;for(uint32_t t=0;t<=n;t++)if(d[t]<0){row.br=root;row.bt=t;break;}if(row.br>=0)break;
  }
  rows.push_back(row);
  if(row.br<0){
   hit=true;ofstream file(dir+"/graph_d6_D7_n20401.edges");file<<n+1<<' '<<m2/2+1<<'\n';
   for(uint32_t u=0;u<n;u++)for(uint32_t z=off[u];z<off[u+1];z++){int y=adj[z];if(int(u)>=y||(u==0&&y==v))continue;file<<u<<' '<<y<<'\n';}
   file<<0<<' '<<n<<'\n'<<v<<' '<<n<<'\n';
   ofstream params(dir+"/FIRST_HIT.json");params<<"{\"source_n\":20400,\"source_m\":61200,\"new_n\":20401,\"new_m\":61201,\"deleted_edge\":[0,"<<v<<"],\"new_neighbors\":[0,"<<v<<"],\"new_degree\":2,\"old_degrees\":6,\"complete_affected_roots_checked\":"<<row.roots<<",\"all_checked_R7_cover\":true,\"global_D\":7,\"D_exact_reason\":\"SourceexactD7 inherited; subdividinganedgedoesnotshortenoldpairdistances; completeaffectedrootproofgivesD<=7.\",\"root_independent_check_pending\":true}\n";
   break;
  }
 }
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"FIRST_COMPLETE_HIT":"SIX_REPRESENTATIVES_COMPLETE_NO_HIT")<<"\",\"source_n\":20400,\"source_m\":61200,\"source_R6_roots\":7,\"source_D7_BFS_repeated\":0,\"source_R6_sizes\":[";
 for(size_t i=0;i<sizes.size();i++){if(i)out<<',';out<<sizes[i];}out<<"],\"cases\":[";
 for(size_t i=0;i<rows.size();i++){auto&r=rows[i];if(i)out<<',';out<<"{\"deleted_edge\":[0,"<<r.v<<"],\"source_R6_union\":"<<r.covered<<",\"newroot_R7_missing\":"<<n-r.covered<<",\"first_missing_target\":"<<r.firstmiss<<",\"modified_roots_checked\":"<<r.roots<<",\"oldpair_failure_root\":"<<r.br<<",\"oldpair_failure_target\":"<<r.bt<<'}';}
 out<<"],\"cases_evaluated\":"<<rows.size()<<",\"actual_modified_root_BFS\":"<<bfses<<",\"hit\":"<<(hit?"true":"false")<<",\"native_CPU_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC<<"}\n";
 cout<<(hit?"HIT":"SIX_NO_HIT")<<" cases "<<rows.size()<<" BFS "<<bfses<<endl;
}
