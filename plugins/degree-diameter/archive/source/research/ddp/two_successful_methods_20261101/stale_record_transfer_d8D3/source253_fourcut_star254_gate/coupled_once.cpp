#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <tuple>
#include <vector>
using namespace std;
using Mask = uint32_t;
const Mask ALL = (1u << 27) - 1;
struct Edge { int u,v,index; Mask mask; };
struct Repair { int a,b; Mask mask; };
struct Type { int s; array<Mask,253> vertex; vector<Edge> edges; vector<Repair> repairs; };
int main(int argc,char**argv) {
  const string dir=argv[1]; const double limit=stod(argv[2]);
  const clock_t start=clock();
  auto timeout=[&](){return double(clock()-start)/CLOCKS_PER_SEC >= limit;};
  ifstream in(dir+"/COUPLED_INPUT.txt");
  int m; in>>m; vector<pair<int,int>> source(m); array<vector<int>,253> adj;
  for(auto &e:source){in>>e.first>>e.second;adj[e.first].push_back(e.second);adj[e.second].push_back(e.first);}
  for(auto &v:adj)sort(v.begin(),v.end());
  array<Type,4> types;
  for(auto &t:types){
    in>>t.s;for(auto &v:t.vertex)in>>v;
    int n;in>>n;t.edges.resize(n);for(auto&e:t.edges)in>>e.index>>e.u>>e.v>>e.mask;
    in>>n;t.repairs.resize(n);for(auto&r:t.repairs)in>>r.a>>r.b>>r.mask;
  }
  if(!in){cerr<<"input failure\n";return 2;}
  ofstream rtab(dir+"/COUPLED_ALL_REPAIR_HALF_MAXIMA.tsv");
  rtab<<"type\ta\tb\trepair_mask\tvalid_halfchoices\tmax_base_hits\ta_prime\tb_prime\tbase_mask\n";
  array<int,4> maxima;maxima.fill(-1);
  array<long long,4> halves{};array<long long,4> checked_r{};
  array<array<long long,28>,4> hist{};
  int best=-1,bt=-1,ba=-1,bb=-1,bap=-1,bbp=-1;Mask bestmask=0;
  bool scan_complete=true;
  for(int k=0;k<4&&scan_complete;++k){auto&t=types[k];
    for(auto&r:t.repairs){
      if(timeout()){scan_complete=false;break;}
      int local=-1,lap=-1,lbp=-1,count=0;Mask lm=0;
      for(int ap:adj[r.a])for(int bp:adj[r.b]){
        if(ap==0||ap==t.s||ap==r.a||ap==r.b||bp==0||bp==t.s||bp==r.a||bp==r.b||ap==bp)continue;
        Mask mask=r.mask|t.vertex[ap]|t.vertex[bp];int hits=__builtin_popcount(mask);
        ++count;++halves[k];++hist[k][hits];
        if(hits>local){local=hits;lap=ap;lbp=bp;lm=mask;}
      }
      ++checked_r[k];maxima[k]=max(maxima[k],local);
      rtab<<k<<'\t'<<r.a<<'\t'<<r.b<<'\t'<<r.mask<<'\t'<<count<<'\t'<<local<<'\t'<<lap<<'\t'<<lbp<<'\t'<<lm<<'\n';
      if(local>best || (local==best&&make_tuple(k,r.a,r.b)<make_tuple(bt,ba,bb))){best=local;bt=k;ba=r.a;bb=r.b;bap=lap;bbp=lbp;bestmask=lm;}
    }
  }
  rtab.close();
  bool strict_no=scan_complete;
  for(int k=0;k<4;++k)if(maxima[k]+12>=27)strict_no=false;
  long long candidates=0,new_fail=0,new_pass=0,old_fail=0,oldroot_bfs=0,joined_pairs=0,firstedge_queries=0;
  int half_checked=0,half_total=0;
  bool selected_complete=false,hit=false,cap_stop=false,time_stop=!scan_complete;
  string status;
  vector<int> first_new_path,first_old_path;int first_new_target=-1,first_new_dist=-1,first_old_root=-1,first_old_target=-1,first_old_dist=-1;
  vector<pair<int,int>> saved_cuts,first_new_cuts,first_old_cuts;int first_new_id=-1,first_old_id=-1;array<vector<int>,254> hit_adj;
  ofstream parameters(dir+"/COUPLED_CANDIDATE_STAGES.tsv");
  parameters<<"candidate\ttype\trepair_a\trepair_b\ta_prime\tb_prime\tfull_edge1\tfull_edge2\tstage\tfail_root\tfail_target\tdistance\n";
  vector<array<int,6>> hit_stats;
  auto bfs=[&](array<vector<int>,254>&g,int root,array<int,254>&d,array<int,254>&parent){
    d.fill(-1);parent.fill(-1);array<int,254>q;int begin=0,end=1;q[0]=root;d[root]=0;
    while(begin<end){int u=q[begin++];for(int v:g[u])if(d[v]<0){d[v]=d[u]+1;parent[v]=u;q[end++]=v;}}
  };
  auto path=[&](int root,int target,const array<int,254>&d,const array<int,254>&parent){
    vector<int> p;if(d[target]<0)return p;for(int v=target;v!=-1;v=parent[v])p.push_back(v);reverse(p.begin(),p.end());return p;
  };
  if(scan_complete&&!strict_no){
    auto&t=types[bt];Repair frozen;for(auto&r:t.repairs)if(r.a==ba&&r.b==bb)frozen=r;
    vector<pair<int,int>> choices;
    for(int ap:adj[ba])for(int bp:adj[bb]){
      if(ap==0||ap==t.s||ap==ba||ap==bb||bp==0||bp==t.s||bp==ba||bp==bb||ap==bp)continue;
      choices.push_back({ap,bp});
    }
    half_total=choices.size();const int n=t.edges.size(),chunks=(n+63)/64;
    array<vector<uint64_t>,27> membership;for(auto&b:membership)b.assign(chunks,0);
    for(int j=0;j<n;++j)for(int bit=0;bit<27;++bit)if(t.edges[j].mask&(1u<<bit))membership[bit][j/64]|=1ull<<(j%64);
    for(auto [ap,bp]:choices){
      if(hit||cap_stop||time_stop)break;
      if(timeout()){time_stop=true;break;}
      array<bool,253> occupied{};for(int x:{0,t.s,ba,bb,ap,bp})occupied[x]=true;
      vector<uint64_t> valid(chunks,0);
      for(int j=0;j<n;++j)if(!occupied[t.edges[j].u]&&!occupied[t.edges[j].v])valid[j/64]|=1ull<<(j%64);
      const Mask base=frozen.mask|t.vertex[ap]|t.vertex[bp];
      for(int j=0;j<n&&!hit&&!cap_stop&&!time_stop;++j){
        if(!(valid[j/64]&(1ull<<(j%64))))continue;
        if(timeout()){time_stop=true;break;}
        ++firstedge_queries;
        Mask missing=ALL&~(base|t.edges[j].mask);
        vector<uint64_t> possible=valid;
        while(missing){int bit=__builtin_ctz(missing);missing&=missing-1;for(int c=0;c<chunks;++c)possible[c]&=membership[bit][c];}
        for(int c=0;c<chunks&&!hit&&!cap_stop&&!time_stop;++c){
          uint64_t word=possible[c];
          while(word&&!hit&&!cap_stop&&!time_stop){
            int l=c*64+__builtin_ctzll(word);word&=word-1;if(l<=j||l>=n)continue;
            auto&e=t.edges[j];auto&f=t.edges[l];if(e.u==f.u||e.u==f.v||e.v==f.u||e.v==f.v)continue;
            ++joined_pairs;
            vector<pair<int,int>> cuts={{0,t.s},{ba,ap},{bb,bp},{e.u,e.v},{f.u,f.v}};
            for(auto&ce:cuts)if(ce.first>ce.second)swap(ce.first,ce.second);
            sort(cuts.begin(),cuts.end());
            array<vector<int>,254>g;
            auto add=[&](int u,int v){g[u].push_back(v);g[v].push_back(u);};
            for(auto ce:source)if(!binary_search(cuts.begin(),cuts.end(),ce))add(ce.first,ce.second);
            add(ba,bb);for(int x:{0,t.s,ap,bp,e.u,e.v,f.u,f.v})add(253,x);
            for(auto&v:g){sort(v.begin(),v.end());if(v.size()!=8||adjacent_find(v.begin(),v.end())!=v.end()){cerr<<"candidate degree/simple failure\n";return 3;}}
            int id=candidates++;array<int,254>d,parent;vector<array<int,6>>stats;
            bfs(g,253,d,parent);int bad=-1;for(int v=0;v<254;++v)if(d[v]<0||d[v]>3){bad=v;break;}
            if(bad>=0){
              ++new_fail;if(first_new_target<0){first_new_target=bad;first_new_dist=d[bad];first_new_path=path(253,bad,d,parent);first_new_cuts=cuts;first_new_id=id;}
              parameters<<id<<'\t'<<bt<<'\t'<<ba<<'\t'<<bb<<'\t'<<ap<<'\t'<<bp<<'\t'<<e.index<<'\t'<<f.index<<"\tNEWROOT_FAIL\t253\t"<<bad<<'\t'<<d[bad]<<'\n';
            }else{
              ++new_pass;array<int,6>row{};row[0]=253;for(int v:d)++row[v+1];stats.push_back(row);
              int badroot=-1;
              for(int root=0;root<253;++root){
                bfs(g,root,d,parent);++oldroot_bfs;bad=-1;for(int v=0;v<254;++v)if(d[v]<0||d[v]>3){bad=v;break;}
                if(bad>=0){badroot=root;break;}
                row.fill(0);row[0]=root;for(int v:d)++row[v+1];stats.push_back(row);
              }
              if(badroot>=0){
                ++old_fail;if(first_old_root<0){first_old_root=badroot;first_old_target=bad;first_old_dist=d[bad];first_old_path=path(badroot,bad,d,parent);first_old_cuts=cuts;first_old_id=id;}
                parameters<<id<<'\t'<<bt<<'\t'<<ba<<'\t'<<bb<<'\t'<<ap<<'\t'<<bp<<'\t'<<e.index<<'\t'<<f.index<<"\tOLDROOT_FAIL\t"<<badroot<<'\t'<<bad<<'\t'<<d[bad]<<'\n';
              }else{
                hit=true;hit_adj=g;hit_stats=stats;saved_cuts=cuts;
                parameters<<id<<'\t'<<bt<<'\t'<<ba<<'\t'<<bb<<'\t'<<ap<<'\t'<<bp<<'\t'<<e.index<<'\t'<<f.index<<"\tFULL_HIT\t-1\t-1\t-1\n";
              }
            }
            if(candidates>=1000&&!hit)cap_stop=true;
          }
        }
      }
      if(!hit&&!cap_stop&&!time_stop)++half_checked;
    }
    selected_complete=!hit&&!cap_stop&&!time_stop&&half_checked==half_total;
  }
  if(hit){
    ofstream out(dir+"/COUPLED_HIT_graph_d8_D3_n254.edges");out<<"254 1016\n";
    for(int u=0;u<254;++u)for(int v:hit_adj[u])if(u<v)out<<u<<' '<<v<<'\n';
    ofstream out2(dir+"/COUPLED_HIT_ALL254_ROOTS.tsv");out2<<"root\tR0\tR1\tR2\tR3\tR4\n";
    for(auto&row:hit_stats){for(int j=0;j<6;++j)out2<<row[j]<<(j==5?'\n':'\t');}
  }
  if(!scan_complete)status="UNKNOWN_COUPLED_CAPACITY_TIME_CAP";
  else if(strict_no)status="COMPLETE_NO_FIVECUT_REPAIR_8STAR_BY_COUPLED_CAPACITY";
  else if(hit)status="FULL254_D3_CANDIDATE_HIT_PENDING_FRESH_INDEPENDENT_ACCEPTANCE";
  else if(selected_complete)status="COMPLETE_NO_SELECTED_FIRSTTYPE_REPAIR_SUBDOMAIN_FAMILY_OPEN";
  else status="UNKNOWN_SELECTED_FIRSTTYPE_REPAIR_SUBDOMAIN_CAP";
  auto vectorjson=[](ostream&o,const vector<int>&v){o<<'[';for(size_t i=0;i<v.size();++i){if(i)o<<',';o<<v[i];}o<<']';};
  ofstream out(dir+"/COUPLED_NATIVE_RESULT.json");
  out<<"{\"status\":\""<<status<<"\",\"complete_global_coupling_scan\":"<<(scan_complete?"true":"false")<<",\"global_capacity_NO\":"<<(strict_no?"true":"false")<<",\"profiles\":[";
  for(int k=0;k<4;++k){if(k)out<<',';out<<"{\"type\":"<<k<<",\"repairs_checked\":"<<checked_r[k]<<",\"legal_halfchoices_checked\":"<<halves[k]<<",\"maximum_base_hits\":"<<maxima[k]<<",\"base_plus_two_fullcuts_upper\":"<<maxima[k]+12<<",\"base_hit_histogram\":[";for(int j=0;j<28;++j){if(j)out<<',';out<<hist[k][j];}out<<"]}";}
  out<<"],\"first_new_failure_candidate_id\":"<<first_new_id<<",\"first_old_failure_candidate_id\":"<<first_old_id<<",\"frozen_first_type\":"<<bt<<",\"frozen_repair\":["<<ba<<','<<bb<<"],\"global_max_base_hits\":"<<best<<",\"first_max_halfchoice\":["<<bap<<','<<bbp<<"],\"first_max_base_mask\":"<<bestmask<<",\"selected_R_halfchoices\":"<<half_total<<",\"selected_R_completed_halfchoices\":"<<half_checked<<",\"selected_R_domain_complete\":"<<(selected_complete?"true":"false")<<",\"fullcut_firstedge_queries\":"<<firstedge_queries<<",\"necessary_joined_candidates\":"<<joined_pairs<<",\"actual_final_candidate_count\":"<<candidates<<",\"newroot_fail\":"<<new_fail<<",\"newroot_pass\":"<<new_pass<<",\"oldroot_fail_candidates\":"<<old_fail<<",\"oldroot_BFS_count\":"<<oldroot_bfs<<",\"newroot_BFS_count\":"<<candidates<<",\"full_hit\":"<<(hit?"true":"false")<<",\"candidate_cap_stop\":"<<(cap_stop?"true":"false")<<",\"time_cap_stop\":"<<(time_stop?"true":"false")<<",\"first_newroot_failure\":{\"root\":253,\"target\":"<<first_new_target<<",\"distance\":"<<first_new_dist<<",\"path\":";vectorjson(out,first_new_path);out<<"},\"first_oldroot_failure\":{\"root\":"<<first_old_root<<",\"target\":"<<first_old_target<<",\"distance\":"<<first_old_dist<<",\"path\":";vectorjson(out,first_old_path);out<<"},\"hit_deleted_edges\":[";for(size_t i=0;i<saved_cuts.size();++i){if(i)out<<',';out<<'['<<saved_cuts[i].first<<','<<saved_cuts[i].second<<']';}out<<"],\"native_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<"}\n";
  cout<<status<<"; maxbase="<<best<<"; frozen="<<bt<<','<<ba<<','<<bb<<"; candidates="<<candidates<<"; newpass="<<new_pass<<"; oldfail="<<old_fail<<'\n';
}
