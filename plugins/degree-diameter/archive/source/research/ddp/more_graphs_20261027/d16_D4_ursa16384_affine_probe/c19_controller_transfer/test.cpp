#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
int main(int argc,char**argv){
 clock_t start=clock();rlimit limit{24,24};setrlimit(RLIMIT_CPU,&limit);
 assert(argc==3);ifstream in(argv[1]);string out=argv[2];int C,F,K;in>>C>>F>>K;assert(C%4==0&&F==256&&K==4);int modulus=C/4;
 vector<array<int,4>>p(C);for(auto&r:p)for(int&v:r)in>>v;
 vector<vector<array<int,4>>>rel(K,vector<array<int,4>>(F));for(auto&t:rel)for(auto&r:t)for(int&v:r)in>>v;
 int N=C*F;vector<vector<int>>adj(N);bool simple=true;map<int,int>degrees;
 for(int c=0;c<C;c++)for(int x=0;x<F;x++){
  int u=F*c+x;auto&r=adj[u];for(int s=0;s<K;s++)for(int y:rel[s][x])r.push_back(F*p[c][s]+y);
  sort(r.begin(),r.end());r.erase(unique(r.begin(),r.end()),r.end());simple&=!binary_search(r.begin(),r.end(),u);degrees[r.size()]++;
 }
 for(int u=0;u<N;u++)for(int v:adj[u])assert(binary_search(adj[v].begin(),adj[v].end(),u));
 int source=-1,target=-1,first_ecc=-1,first_reached=-1,missing_count=0,roots=0;bool hit=true,budget=false;
 vector<int>d(N),parent(N),q(N),witness;vector<vector<int>>bad;vector<int>ecc;
 for(int base=0;base<4&&hit&&!budget;base++)for(int x=0;x<F&&hit;x++){
  if(double(clock()-start)/CLOCKS_PER_SEC>23){budget=true;hit=false;break;}
  int s=F*(modulus*base)+x;fill(d.begin(),d.end(),-1);fill(parent.begin(),parent.end(),-1);int lo=0,hi=1;q[0]=s;d[s]=0;int e=0;
  while(lo<hi){int u=q[lo++];for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;e=max(e,d[v]);parent[v]=u;q[hi++]=v;}}
  roots++;ecc.push_back(e);if(roots==1){first_ecc=e;first_reached=hi;}
  int first=-1;for(int v=0;v<N;v++)if(d[v]<0||d[v]>4){if(first<0)first=v;missing_count++;}
  if(first>=0){hit=false;source=s;target=first;bad.assign(C,{});for(int v=0;v<N;v++)if(d[v]<0||d[v]>4)bad[v/F].push_back(v%F);
   if(d[first]>=0){for(int v=first;v!=s;v=parent[v])witness.push_back(v);witness.push_back(s);reverse(witness.begin(),witness.end());}
  }
 }
 long long twice=0;for(auto&r:adj)twice+=r.size();
 if(hit){ofstream edges(out+"/candidate"+to_string(N)+".edges");for(int u=0;u<N;u++)for(int v:adj[u])if(u<v)edges<<u<<' '<<v<<'\n';}
 ofstream f(out+"/NATIVE_RESULT.json");f<<"{\"status\":\""<<(hit?"FULL_D4_GRAPH":budget?"UNKNOWN_BUDGET":"FIRST_ROOT_COUNTEREXAMPLE")<<"\",\"n\":"<<N<<",\"m\":"<<twice/2<<",\"simple\":"<<(simple?"true":"false")<<",\"degree_histogram\":{";
 bool sep=false;for(auto[k,v]:degrees){if(sep)f<<',';sep=true;f<<'\"'<<k<<"\":"<<v;}f<<"},\"roots_checked\":"<<roots<<",\"representatives_required\":1024,\"first_root_eccentricity\":"<<first_ecc<<",\"first_root_reached\":"<<first_reached<<",\"actual_global_D\":";
 if(hit)f<<*max_element(ecc.begin(),ecc.end());else f<<"null";
 f<<",\"counterexample_source\":"<<source<<",\"counterexample_target\":"<<target<<",\"counterexample_distance\":"<<(target>=0?d[target]:-1)<<",\"single_root_R4_missing_targets\":"<<missing_count<<",\"shortest_path\":[";
 for(size_t i=0;i<witness.size();i++){if(i)f<<',';f<<witness[i];}f<<"],\"missing_by_controller\":[";sep=false;
 for(int c=0;c<(int)bad.size();c++)if(!bad[c].empty()){if(sep)f<<',';sep=true;f<<"{\"controller\":"<<c<<",\"base\":"<<c/modulus<<",\"phase\":"<<c%modulus<<",\"missing_count\":"<<bad[c].size()<<",\"missing_fiber_ids\":[";for(size_t i=0;i<bad[c].size();i++){if(i)f<<',';f<<bad[c][i];}f<<"]}";}
 f<<"],\"CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"graph_exported\":"<<(hit?"true":"false")<<",\"old_source_BFS\":0,\"parameter_candidates\":1}\n";
 cout<<(hit?"FULL_D4":"NO_HIT")<<" roots="<<roots<<" firstecc="<<first_ecc<<" miss="<<missing_count<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}
