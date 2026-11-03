// Complete one-voltage neighborhood of one fixed seed. No accepted moves or trajectory.
#include <algorithm>
#include <array>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
using namespace std;
struct Edge { int u,v,z; };
struct Evaluation { int score=0; vector<int> misses; vector<vector<unsigned char>> reached; };
int main(int argc,char**argv){
 if(argc!=3){cerr<<"usage BASE OUTPUT_PREFIX\n";return 2;}
 auto started=chrono::steady_clock::now();clock_t cpu_started=clock();
 ifstream in(argv[1]);int p,k,m;in>>p>>k>>m;vector<Edge>edges(m);for(auto&e:edges)in>>e.u>>e.v>>e.z;
 if(p!=37||k!=18||m!=45)return 2;int n=p*k;string prefix=argv[2];
 auto mod=[&](int x){return (x%p+p)%p;};
 auto id=[&](int b,int x){return (b/9)*333+x*9+b%9;};
 auto legal=[&](){
  for(auto e:edges)if(e.u==e.v&&e.z==0)return 1;
  for(int i=0;i<m;i++)for(int j=i+1;j<m;j++){
   auto a=edges[i],b=edges[j];if(min(a.u,a.v)!=min(b.u,b.v)||max(a.u,a.v)!=max(b.u,b.v))continue;
   int za=a.u<=a.v?a.z:mod(-a.z),zb=b.u<=b.v?b.z:mod(-b.z);
   if(za==zb||(a.u==a.v&&za==mod(-zb)))return 2;
  }return 0;
 };
 vector<array<int,5>>adj(n);
 auto build=[&](){vector<int>degree(n);for(auto e:edges)for(int x=0;x<p;x++){
   int u=id(e.u,x),v=id(e.v,mod(x+e.z));if(degree[u]>=5||degree[v]>=5)throw runtime_error("degree overflow");
   adj[u][degree[u]++]=v;adj[v][degree[v]++]=u;
  }for(int d:degree)if(d!=5)throw runtime_error("degree mismatch");};
 auto evaluate=[&](){
  Evaluation e;e.reached.assign(k,vector<unsigned char>(n));vector<int>queue(n);
  for(int root=0;root<k;root++){
   int head=0,end=1;queue[0]=id(root,0);e.reached[root][queue[0]]=1;
   for(int depth=0;depth<5&&end<n;depth++){
    int boundary=end;while(head<boundary){int u=queue[head++];for(int v:adj[u])if(!e.reached[root][v]){
      e.reached[root][v]=1;queue[end++]=v;
    }}
   }e.misses.push_back(n-end);e.score+=n-end;
  }return e;
 };
 auto save_edges=[&](string name){set<pair<int,int>>es;for(int u=0;u<n;u++)for(int v:adj[u])if(u<v)es.emplace(u,v);
  ofstream f(name);f<<n<<" "<<es.size()<<"\n";for(auto[u,v]:es)f<<u<<" "<<v<<"\n";
 };
 if(legal())return 2;build();Evaluation baseline=evaluate();if(baseline.score!=36)return 2;
 int valid=0,invalid_loop=0,invalid_parallel=0,improving=0,neutral=0,worsening=0,identical=0;
 int min_score=100000,best_distinct=100000,best_eid=-1,best_z=-1,best_fixed=0,best_created=0;
 map<int,int>histogram;vector<int>best_misses;
 ofstream moves(prefix+".moves.jsonl");
 for(int eid=0;eid<m;eid++){
  int old=edges[eid].z;
  for(int z=0;z<p;z++){
   if(z==old)continue;edges[eid].z=z;int invalid=legal();
   if(invalid){if(invalid==1)invalid_loop++;else invalid_parallel++;continue;}
   valid++;build();Evaluation trial=evaluate();int delta=trial.score-baseline.score;
   histogram[delta]++;if(delta<0)improving++;else if(delta==0)neutral++;else worsening++;
   bool same=edges[eid].u==edges[eid].v&&z==mod(-old);identical+=same;
   int fixed=0,created=0;for(int r=0;r<k;r++)for(int v=0;v<n;v++){
    fixed+=!baseline.reached[r][v]&&trial.reached[r][v];
    created+=baseline.reached[r][v]&&!trial.reached[r][v];
   }if(created-fixed!=delta)return 2;
   min_score=min(min_score,trial.score);
   moves<<"{\"edge\":"<<eid<<",\"old_voltage\":"<<old<<",\"new_voltage\":"<<z
        <<",\"score\":"<<trial.score<<",\"delta\":"<<delta<<",\"fixed_representative_misses\":"<<fixed
        <<",\"created_representative_misses\":"<<created<<",\"same_lifted_edge_set\":"<<(same?"true":"false")<<"}\n";
   if(!same&&trial.score<best_distinct){best_distinct=trial.score;best_eid=eid;best_z=z;best_fixed=fixed;best_created=created;best_misses=trial.misses;save_edges(prefix+".best_distinct.edges");}
  }edges[eid].z=old;
 }
 double cpu=double(clock()-cpu_started)/CLOCKS_PER_SEC;
 double wall=chrono::duration<double>(chrono::steady_clock::now()-started).count();
 ofstream out(prefix+".summary.json");
 out<<"{\"status\":\"COMPLETE_NEIGHBORHOOD_ONLY\",\"baseline_score\":36,\"baseline_root_misses\":[";
 for(int i=0;i<k;i++)out<<(i?",":"")<<baseline.misses[i];
 out<<"],\"voltage_changes_considered\":"<<m*(p-1)<<",\"valid_changes\":"<<valid
    <<",\"illegal_zero_loops\":"<<invalid_loop<<",\"illegal_parallel_collisions\":"<<invalid_parallel
    <<",\"improving\":"<<improving<<",\"neutral\":"<<neutral<<",\"worsening\":"<<worsening
    <<",\"identical_graph_loop_reversals\":"<<identical<<",\"minimum_delta\":"<<min_score-36
    <<",\"minimum_distinct_graph_delta\":"<<best_distinct-36<<",\"best_distinct_score\":"<<best_distinct
    <<",\"best_distinct_bad_pairs\":"<<p*best_distinct/2<<",\"best_distinct_edge\":"<<best_eid
    <<",\"best_distinct_old_voltage\":"<<edges[best_eid].z<<",\"best_distinct_new_voltage\":"<<best_z
    <<",\"best_distinct_fixed_misses\":"<<best_fixed<<",\"best_distinct_created_misses\":"<<best_created
    <<",\"best_distinct_root_misses\":[";
 for(int i=0;i<k;i++)out<<(i?",":"")<<best_misses[i];out<<"],\"delta_histogram\":{";
 bool comma=false;for(auto[d,count]:histogram){out<<(comma?",":"")<<"\""<<d<<"\":"<<count;comma=true;}
 out<<"},\"cpu_seconds\":"<<cpu<<",\"wall_seconds\":"<<wall<<"}\n";
 cout<<"complete valid "<<valid<<" improving "<<improving<<" neutral "<<neutral<<" worsening "<<worsening
     <<" identical "<<identical<<" minimum_delta "<<min_score-36<<" minimum_distinct_delta "<<best_distinct-36
     <<" cpu "<<cpu<<" wall "<<wall<<endl;
}
