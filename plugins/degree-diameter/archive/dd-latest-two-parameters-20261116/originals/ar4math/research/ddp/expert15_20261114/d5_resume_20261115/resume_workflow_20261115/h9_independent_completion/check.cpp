// Independent raw-adjacency distances and an exact single z-anchor completion.
// Core-core D5 still needs the separately inspected true-sigma binding theorem.
#include <algorithm>
#include <chrono>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using namespace std;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
void ints(ostream&f,const vector<int>&a){f<<'[';for(size_t i=0;i<a.size();++i){if(i)f<<',';f<<a[i];}f<<']';}
int main(int argc,char**argv){try{
 if(argc!=5)throw runtime_error("graph outputdir pins.txt native_CPU_seconds");
 const int core=37471,expected_n=37632,z=37631;double start=cpu(),deadline=start+stod(argv[4]);
 ifstream in(argv[1]);int n,m;if(!(in>>n>>m)||n!=expected_n)throw runtime_error("expected actual37632 header");
 vector<vector<int>>adj(n);int a,b,edges=0;while(in>>a>>b){if(a<0||b<0||a>=n||b>=n||a==b)throw runtime_error("invalid edge");adj[a].push_back(b);adj[b].push_back(a);++edges;}
 if(edges!=m)throw runtime_error("edge header mismatch");int maxdeg=0;
 for(auto&r:adj){sort(r.begin(),r.end());if(adjacent_find(r.begin(),r.end())!=r.end())throw runtime_error("duplicate edge");maxdeg=max(maxdeg,int(r.size()));}
 if(maxdeg>11)throw runtime_error("degree exceeds11");
 ifstream pinfile(argv[3]);int k;pinfile>>k;vector<int>pins(k);for(int&v:pins)pinfile>>v;sort(pins.begin(),pins.end());
 if(!pinfile||k>11||k<1||adjacent_find(pins.begin(),pins.end())!=pins.end()||adj[z]!=pins)throw runtime_error("new root exact pins mismatch");
 string out=argv[2];filesystem::create_directories(out);ofstream roots(out+"/ROOT_RESULTS.jsonl");
 vector<vector<int>>dist(n-core);vector<int>queue(n);vector<pair<int,int>>bad;int checked=0;bool interrupted=false;long long adjacency_visits=0;
 auto bfs=[&](int root,vector<int>&d,int radius)->bool{
  d.assign(n,-1);int h=0,t=0;d[root]=0;queue[t++]=root;
  while(h<t){int u=queue[h++];if((h&2047)==0&&cpu()>=deadline)return false;if(d[u]>=radius)continue;
   for(int v:adj[u]){++adjacency_visits;if(d[v]<0){d[v]=d[u]+1;queue[t++]=v;}}}
  return true;
 };
 // z first gives every d(z,v), then all160 old exterior roots.
 vector<int>order{z};for(int u=core;u<z;++u)order.push_back(u);
 for(int u:order){if(cpu()>=deadline||!bfs(u,dist[u-core],n)){interrupted=true;break;}
  auto&d=dist[u-core];int ecc=0,unreachable=0,miss=0;
  roots<<"{\"root\":"<<u<<",\"eccentricity\":";for(int v=0;v<n;++v){if(d[v]<0)++unreachable;else ecc=max(ecc,d[v]);if(d[v]<0||d[v]>5){++miss;if(v<core||u<v)bad.emplace_back(u,v);}}
  if(unreachable)roots<<"null";else roots<<ecc;
  roots<<",\"max_finite_distance\":"<<ecc<<",\"unreachable_count\":"<<unreachable<<",\"beyond5_count\":"<<miss<<",\"missing\":[";
  bool first=true;for(int v=0;v<n;++v)if(d[v]<0||d[v]>5){if(!first)roots<<',';first=false;roots<<"["<<v<<','<<d[v]<<']';}roots<<"]}\n";roots.flush();++checked;
 }
 const bool complete=checked==161;
 vector<int>anchors;for(int v=0;v<z;++v)if(adj[v].size()<11&&!binary_search(pins.begin(),pins.end(),v))anchors.push_back(v);
 int anchor_start=anchors.size(),constraints_done=0,extra_balls=0;string tail="NOT_CHECKED_ROOTS_INCOMPLETE";pair<int,int>witness{-1,-1};
 auto far=[](int d){return d<0||d>=5;};
 if(complete){
  if(bad.empty())tail="UNNEEDED_ALREADY_ALL161_ROOTS_PASS";
  else if(k==11){tail="NO_FREE_NEW_ROOT_SLOT";anchors.clear();}
  else if(k!=10)tail="NOT_THIS_EXACT_ONE_EDGE_INTERFACE";
  else{
   tail="UNKNOWN_BUDGET";auto&dz=dist[z-core];
   // One exact bad-pair witness can already disprove all one-edge completions.
   for(auto uv:bad)if(far(dz[uv.first])&&far(dz[uv.second])){tail="NO_ONE_EDGE_BOTH_ENDPOINTS_FAR_FROM_Z";witness=uv;anchors.clear();break;}
   if(!anchors.empty()){
    vector<int>ball;
    for(auto uv:bad){if(cpu()>=deadline)break;int u=uv.first,v=uv.second;auto&du=dist[u-core];
     // The second orientation is known from root u; only otherwise-live anchors
     // may need the radius (4-d(z,u)) ball around a core endpoint v.
     bool need_ball=false;int radius=dz[u]<0?-1:4-dz[u];
     for(int q:anchors)if(!(du[q]>=0&&dz[v]>=0&&du[q]+1+dz[v]<=5)&&radius>=0){need_ball=true;break;}
     const vector<int>*dv=nullptr;
     if(need_ball){if(v>=core)dv=&dist[v-core];else{if(!bfs(v,ball,radius))break;dv=&ball;++extra_balls;}}
     vector<int>kept;for(int q:anchors){bool via_a_z=du[q]>=0&&dz[v]>=0&&du[q]+1+dz[v]<=5;
      bool via_z_a=dv&&dz[u]>=0&&(*dv)[q]>=0&&dz[u]+1+(*dv)[q]<=5;
      if(via_a_z||via_z_a)kept.push_back(q);}
     anchors.swap(kept);++constraints_done;
     if(anchors.empty()){tail="NO_COMMON_ONE_EDGE_ANCHOR";witness=uv;break;}
    }
    if(!anchors.empty()&&constraints_done==int(bad.size()))tail="EXACT_COMMON_ONE_EDGE_ANCHORS_FOUND";
   }else if(tail=="UNKNOWN_BUDGET")tail="NO_LEGAL_OLD_ANCHOR";
  }
 }
 ofstream result(out+"/RAW_CHECK_RESULT.json");result<<"{\"status\":\""<<(complete?(bad.empty()?"ALL161_ROOTS_PASS":"COMPLETE_REMAINING_PAIR_FAILURES"):"UNKNOWN_ROOT_BUDGET")<<"\",\"n\":"<<n<<",\"m\":"<<m<<",\"simple\":true,\"maximum_degree\":"<<maxdeg<<",\"roots_checked\":"<<checked<<",\"required_roots\":161,\"roots_complete\":"<<(complete?"true":"false")<<",\"unique_bad_pairs_touching_checked_roots\":"<<bad.size()<<",\"core_core_proof\":\"REQUIRES_SEPARATELY_INSPECTED_TRUE_SIGMA_BINDING\",\"tail_status\":\""<<tail<<"\",\"initial_legal_anchor_count\":"<<anchor_start<<",\"bad_pair_constraints_checked\":"<<constraints_done<<",\"extra_core_radius_balls\":"<<extra_balls<<",\"tail_witness\":["<<witness.first<<','<<witness.second<<"],\"surviving_anchors\":";ints(result,anchors);result<<",\"adjacency_visits\":"<<adjacency_visits<<",\"CPU_seconds\":"<<cpu()-start<<"}\n";
 cout<<"raw roots "<<checked<<"/161 badpairs="<<bad.size()<<" tail="<<tail<<" CPU="<<cpu()-start<<endl;return 0;
 }catch(const exception&e){cerr<<e.what()<<endl;return 1;}}
