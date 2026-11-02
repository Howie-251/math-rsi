#include <bits/stdc++.h>
#include <sys/resource.h>
using namespace std;
int main(int argc,char**argv){
 rlimit lim{30,30};setrlimit(RLIMIT_CPU,&lim);clock_t st=clock();string dir=argv[1];ifstream in(dir+"/degree10_source.edges");int n,m;in>>n>>m;vector<vector<int>>adj(n);for(int i=0,u,v;i<m;i++){in>>u>>v;adj[u].push_back(v);adj[v].push_back(u);}vector<int>P;map<int,int>dh;for(int u=0;u<n;u++){dh[adj[u].size()]++;if(adj[u].size()<10)P.push_back(u);}int c=P.size(),W=(n+63)/64;vector<vector<uint64_t>>balls(c,vector<uint64_t>(W));vector<vector<int>>support(n);vector<int>ballsize,seen(n),depth(n),q(n);int stamp=0;
 for(int i=0;i<c;i++){++stamp;int b=0,e=1;q[0]=P[i];seen[P[i]]=stamp;depth[P[i]]=0;while(b<e){int u=q[b++];balls[i][u>>6]|=1ULL<<(u&63);support[u].push_back(i);if(depth[u]==4)continue;for(int v:adj[u])if(seen[v]!=stamp){seen[v]=stamp;depth[v]=depth[u]+1;q[e++]=v;}}ballsize.push_back(e);}
 vector<vector<int>>bucket(c+1);map<int,int>ch;vector<int>uncovered;map<int,int>forced;for(int u=0;u<n;u++){int z=support[u].size();ch[z]++;bucket[z].push_back(u);if(!z)uncovered.push_back(u);if(z==1)forced.emplace(P[support[u][0]],u);}
 vector<int>cum(c),bestcounts;int size=0,bestLB=0,bestK=-1,bestSize=0,bestMax=0;
 for(int k=1;k<=c;k++){for(int u:bucket[k]){size++;for(int a:support[u])cum[a]++;}int mx=*max_element(cum.begin(),cum.end());if(mx){int lb=(size+mx-1)/mx;if(lb>bestLB||(lb==bestLB&&k<bestK)){bestLB=lb;bestK=k;bestSize=size;bestMax=mx;bestcounts=cum;}}}
 vector<int>order(n);iota(order.begin(),order.end(),0);sort(order.begin(),order.end(),[&](int a,int b){return make_pair(support[a].size(),a)<make_pair(support[b].size(),b);});vector<bool>used(c);vector<int>disjoint;
 for(int u:order){if(support[u].empty())continue;bool ok=true;for(int a:support[u])if(used[a]){ok=false;break;}if(ok){disjoint.push_back(u);for(int a:support[u])used[a]=true;}}
 ofstream bf(dir+"/degree10_radius4.u64.bin",ios::binary);for(auto&r:balls)bf.write((char*)r.data(),W*8);bf.close();
 ofstream out(dir+"/degree10_capacity.json");out<<"{\n\"n\":"<<n<<",\"m\":"<<m<<",\"max_degree\":10,\"available_pins\":"<<c<<",\"pin_cap\":10,";
 auto vec=[&](auto&r){out<<'[';bool first=true;for(auto x:r){if(!first)out<<',';first=false;out<<x;}out<<']';};auto mp=[&](auto&r){out<<'{';bool f=true;for(auto[k,v]:r){if(!f)out<<',';f=false;out<<'"'<<k<<"\":"<<v;}out<<'}';};
 out<<"\n\"degree_histogram\":";mp(dh);out<<",\n\"available_vertices\":";vec(P);out<<",\n\"R4_ball_sizes\":";vec(ballsize);out<<",\n\"coverage_count_histogram\":";mp(ch);out<<",\n\"all_available_R4_union_missing\":";vec(uncovered);
 out<<",\n\"forced_pin_count\":"<<forced.size()<<",\n\"forced_pins_and_witness_targets\":[";bool f=true;for(auto[p,t]:forced){if(!f)out<<',';f=false;out<<"{\"pin\":"<<p<<",\"target\":"<<t<<'}';}out<<']';
 out<<",\n\"hard_target_capacity\":{\"threshold\":"<<bestK<<",\"target_count\":"<<bestSize<<",\"max_targets_per_pin\":"<<bestMax<<",\"required_pins_lower_bound\":"<<bestLB<<",\"counts_per_pin\":";vec(bestcounts);out<<"},\n\"disjoint_coverer_targets\":";vec(disjoint);
 bool impossible=!uncovered.empty()||forced.size()>10||bestLB>10||disjoint.size()>10;
 out<<",\n\"whole_one_point_extension_excluded\":"<<(impossible?"true":"false")<<",\n\"bounded_R4_ball_computations\":"<<c<<",\"all_source_diameter_BFS\":0,\"new_graphs\":0,\"solver_calls\":0,\"CPU_seconds\":"<<setprecision(10)<<double(clock()-st)/CLOCKS_PER_SEC<<"\n}\n";out.close();
 cout<<"available="<<c<<" unionmissing="<<uncovered.size()<<" forced="<<forced.size()<<" capacityLB="<<bestLB<<" disjointLB="<<disjoint.size()<<" excluded="<<impossible<<" CPU="<<double(clock()-st)/CLOCKS_PER_SEC<<'\n';
}
