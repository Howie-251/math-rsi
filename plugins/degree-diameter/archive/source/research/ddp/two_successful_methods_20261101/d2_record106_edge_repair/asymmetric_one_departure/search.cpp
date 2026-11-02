#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using U64=std::uint64_t;
struct Mask {
  U64 lo=0,hi=0;
  void set(int u){ if(u<64)lo|=U64(1)<<u;else hi|=U64(1)<<(u-64); }
  bool has(int u)const{return u<64?((lo>>u)&1):((hi>>(u-64))&1);}
  bool any()const{return lo||hi;}
};
static int pc(U64 x){return __builtin_popcountll(x);}
static int pc(Mask x){return pc(x.lo)+pc(x.hi);}
static Mask meet(Mask a,Mask b){return{a.lo&b.lo,a.hi&b.hi};}
static Mask outside(Mask a,Mask s){return{a.lo&~s.lo,a.hi&~s.hi};}
static int first(Mask a){return a.lo?__builtin_ctzll(a.lo):64+__builtin_ctzll(a.hi);}

struct State{U64 on=0,off=0;};
struct Search {
  std::array<Mask,106>A;
  std::array<int,106>degree;
  std::vector<int>fixed;
  std::vector<std::vector<int>>orbits;
  std::vector<int>S;
  std::array<int,11>L,U;
  std::array<U64,11>rowMask;
  std::array<std::array<int,11>,11>var;
  std::vector<U64>clauses;
  std::array<int,55>vi,vj;
  U64 all=(U64(1)<<55)-1,solution=0;
  std::clock_t start;
  double seconds=0;
  long visited=0,patternVisited[2]={0,0},domReject=0,crossReject=0,emptyReject=0;
  long propReject=0,dfsUnsat=0,nodes=0,propCalls=0,fullModelCount=0;
  long failUpper=0,failLower=0,failCover=0,failConflict=0;
  bool stopped=false,sat=false;
  std::string stopReason,pattern;
  int currentO=-1,currentQ=-1;
  long passingNecessary=0;
  static constexpr long nodeLimit=200000;

  double elapsed()const{return double(std::clock()-start)/CLOCKS_PER_SEC;}
  bool timeout(){
    if(elapsed()>=seconds){stopped=true;stopReason="CPU_CAP";return true;}
    return false;
  }
  bool propagate(State&s){
    ++propCalls;
    for(;;){
      if(s.on&s.off){++failConflict;return false;}
      U64 oldOn=s.on,oldOff=s.off;
      for(U64 c:clauses){
        if(c&s.on)continue;
        U64 a=c&~s.off;
        if(!a){++failCover;return false;}
        if(!(a&(a-1)))s.on|=a;
      }
      for(int i=0;i<11;++i){
        int n=pc(rowMask[i]&s.on);
        U64 avail=rowMask[i]&~(s.on|s.off);
        int count=pc(avail);
        if(n>U[i]){++failUpper;return false;}
        if(n+count<L[i]){++failLower;return false;}
        if(n==U[i])s.off|=avail;
        if(n+count==L[i])s.on|=avail;
      }
      if(oldOn==s.on&&oldOff==s.off)return true;
    }
  }
  // 1 SAT,0 exact UNSAT,-1 budget UNKNOWN. All branching is on actual y edges.
  int dfs(State s,bool alreadyPropagated=false){
    if(nodes>=nodeLimit){stopped=true;stopReason="GLOBAL_DFS_NODE_CAP";return-1;}
    ++nodes;
    if((nodes&63)==0&&timeout())return-1;
    if(!alreadyPropagated&&!propagate(s))return 0;
    U64 choice=0;
    int best=56;
    for(U64 c:clauses){
      if(c&s.on)continue;
      U64 a=c&~s.off;
      int n=pc(a);
      if(n<best){best=n;choice=a;}
    }
    if(!choice){
      for(int i=0;i<11;++i){
        int n=pc(rowMask[i]&s.on);
        if(n>=L[i])continue;
        U64 a=rowMask[i]&~(s.on|s.off);
        int count=pc(a);
        if(count<best){best=count;choice=a;}
      }
      if(!choice){solution=s.on;return 1;}
    }
    U64 b=choice&(~choice+1);
    State yes=s;yes.on|=b;
    int r=dfs(yes);
    if(r)return r;
    State no=s;no.off|=b;
    return dfs(no);
  }
  bool process(std::vector<int>s,int kind,int oi,int qi){
    if(timeout())return false;
    ++visited;++patternVisited[kind];
    std::sort(s.begin(),s.end());S=s;
    Mask sm;
    for(int u:S)sm.set(u);
    for(int u=0;u<106;++u){
      if(!sm.has(u)&&!meet(A[u],sm).any()){++domReject;return true;}
    }
    for(int i=0;i<11;++i){
      int a=degree[S[i]]-pc(meet(A[S[i]],sm));
      L[i]=std::max(0,9-a);U[i]=10-a;
      if(U[i]<0||L[i]>10){++crossReject;return true;}
    }
    ++passingNecessary;
    for(int i=0;i<11;++i)rowMask[i]=0;
    int e=0;
    for(int i=0;i<11;++i)for(int j=i+1;j<11;++j){
      var[i][j]=var[j][i]=e;vi[e]=i;vj[e]=j;
      rowMask[i]|=U64(1)<<e;rowMask[j]|=U64(1)<<e;++e;
    }
    clauses.clear();
    for(int i=0;i<11;++i){
      int v=S[i];
      for(int u=0;u<106;++u){
        if(sm.has(u)||A[v].has(u))continue;
        if(outside(meet(A[v],A[u]),sm).any())continue;
        U64 c=0;
        for(int j=0;j<11;++j)if(j!=i&&A[u].has(S[j]))c|=U64(1)<<var[i][j];
        if(!c){++emptyReject;return true;}
        clauses.push_back(c);
      }
    }
    std::sort(clauses.begin(),clauses.end());
    clauses.erase(std::unique(clauses.begin(),clauses.end()),clauses.end());
    ++fullModelCount;
    State state;
    if(!propagate(state)){++propReject;return true;}
    int result=dfs(state,true);
    if(result==0){++dfsUnsat;return true;}
    pattern=kind==0?"A_six_from_orbit_plus_five_fixed":"B_seven_from_orbit_plus_three_fixed_plus_one_external";
    currentO=oi;currentQ=qi;
    if(result==1){sat=true;return false;}
    return false;
  }
  void combinations(int choose,int at,std::vector<int>&p,std::vector<std::vector<int>>&out){
    if(int(p.size())==choose){out.push_back(p);return;}
    for(int i=at;i<=8-(choose-int(p.size()));++i){
      p.push_back(fixed[i]);combinations(choose,i+1,p,out);p.pop_back();
    }
  }
  void run(){
    std::vector<std::vector<int>>c5,c3;
    std::vector<int>p;
    combinations(5,0,p,c5);combinations(3,0,p,c3);
    for(int oi=0;oi<14;++oi)for(const auto&k:c5){
      std::vector<int>s=k;
      int omitted=*std::min_element(orbits[oi].begin(),orbits[oi].end());
      for(int u:orbits[oi])if(u!=omitted)s.push_back(u);
      if(!process(s,0,oi,-1))return;
    }
    for(int oi=0;oi<14;++oi)for(const auto&k:c3)for(int qi=0;qi<14;++qi){
      if(oi==qi)continue;
      std::vector<int>s=k;
      s.insert(s.end(),orbits[oi].begin(),orbits[oi].end());
      s.push_back(*std::min_element(orbits[qi].begin(),orbits[qi].end()));
      if(!process(s,1,oi,qi))return;
    }
  }
  static void list(std::ostream&out,const std::vector<int>&v){
    out<<'[';for(unsigned i=0;i<v.size();++i){if(i)out<<',';out<<v[i];}out<<']';
  }
  void emitCandidate(){
    std::array<int,106>index;index.fill(-1);
    for(int i=0;i<11;++i)index[S[i]]=i;
    std::vector<std::pair<int,int>>oldDeleted,oldAdded,body,internal;
    std::array<int,107>deg{};
    for(int u=0;u<106;++u)for(int v=u+1;v<106;++v){
      bool before=A[u].has(v),after=before;
      if(index[u]>=0&&index[v]>=0)
        after=(solution>>var[index[u]][index[v]])&1;
      if(before&&!after)oldDeleted.push_back({u,v});
      if(!before&&after)oldAdded.push_back({u,v});
      if(after){body.push_back({u,v});++deg[u];++deg[v];}
      if(after&&index[u]>=0&&index[v]>=0)internal.push_back({u,v});
    }
    for(int u:S){body.push_back({u,106});++deg[u];++deg[106];}
    std::sort(body.begin(),body.end());
    std::ofstream graph("graph_d11_D2_n107_CANDIDATE.edges");
    graph<<107<<' '<<body.size()<<'\n';
    for(auto e:body)graph<<e.first<<' '<<e.second<<'\n';
    auto pairlist=[](std::ostream&o,const std::vector<std::pair<int,int>>&es){
      o<<'[';for(unsigned i=0;i<es.size();++i){if(i)o<<',';o<<'['<<es[i].first<<','<<es[i].second<<']';}o<<']';
    };
    std::ofstream delta("CANDIDATE_EDGE_DELTA.json");
    delta<<"{\"selected_S\":";list(delta,S);
    delta<<",\"old_deleted\":";pairlist(delta,oldDeleted);
    delta<<",\"old_added\":";pairlist(delta,oldAdded);
    delta<<",\"new_vertex\":106,\"new_neighbors\":";list(delta,S);
    delta<<",\"final_internal_edges\":";pairlist(delta,internal);
    delta<<",\"n\":107,\"m\":"<<body.size()<<",\"degree_by_label\":[";
    for(int u=0;u<107;++u){if(u)delta<<',';delta<<deg[u];}
    delta<<"],\"pending_fresh_root_acceptance\":true}\n";
    std::ofstream routes("MIXED_AND_NEW_ROOT_ROUTES.csv");
    routes<<"from,to,type,middle\n";
    Mask sm;for(int u:S)sm.set(u);
    for(int i=0;i<11;++i){int v=S[i];
      routes<<106<<','<<v<<",new_direct,-1\n";
      for(int u=0;u<106;++u){
        if(sm.has(u))continue;
        if(A[v].has(u)){routes<<v<<','<<u<<",frozen_direct,-1\n";continue;}
        Mask common=outside(meet(A[v],A[u]),sm);
        if(common.any()){routes<<v<<','<<u<<",outside_middle,"<<first(common)<<'\n';continue;}
        int middle=-1;
        for(int j=0;j<11;++j)if(i!=j&&A[u].has(S[j])&&((solution>>var[i][j])&1)){middle=S[j];break;}
        routes<<v<<','<<u<<",chosen_internal_middle,"<<middle<<'\n';
      }
    }
    for(int u=0;u<106;++u)if(!sm.has(u)){
      int middle=-1;for(int v:S)if(A[u].has(v)){middle=v;break;}
      routes<<106<<','<<u<<",frozen_pin_middle,"<<middle<<'\n';
    }
  }
  void result(){
    std::ofstream out("SEARCH_RESULT.json");
    std::string status=sat?"SAT_COMPLETE_CANDIDATE_PENDING_FRESH_ACCEPTANCE":stopped?"UNKNOWN_BUDGET_STOP":"EXACT_NO_IN_TWO_FIXED_PATTERNS";
    out<<"{\"status\":\""<<status<<"\",\"stop_reason\":\""<<stopReason<<"\","
       <<"\"expected_representatives\":10976,\"visited_representatives\":"<<visited
       <<",\"unvisited_representatives\":"<<10976-visited
       <<",\"pattern_A_visited\":"<<patternVisited[0]<<",\"pattern_B_visited\":"<<patternVisited[1]
       <<",\"closed_domination_reject\":"<<domReject<<",\"frozen_cross_degree_reject\":"<<crossReject
       <<",\"passing_both_necessary_gates\":"<<passingNecessary<<",\"mixed_clause_empty_reject\":"<<emptyReject
       <<",\"exact_models_constructed\":"<<fullModelCount<<",\"initial_propagation_reject\":"<<propReject
       <<",\"DFS_exact_unsat\":"<<dfsUnsat<<",\"DFS_nodes\":"<<nodes<<",\"DFS_node_cap\":200000"
       <<",\"propagation_calls\":"<<propCalls<<",\"propagation_failures_by_event\":{\"upper_degree\":"<<failUpper
       <<",\"lower_degree\":"<<failLower<<",\"coverage\":"<<failCover<<",\"on_off_conflict\":"<<failConflict<<'}'
       <<",\"all_representatives_resolved\":"<<((!sat&&!stopped&&visited==10976)?"true":"false")
       <<",\"unresolved_current_representative\":"<<(stopped?"true":"false")
       <<",\"search_CPU_seconds\":"<<elapsed()<<",\"search_CPU_limit_seconds\":"<<seconds
       <<",\"source_D2_BFS_rechecks\":0,\"solver_runs\":0,\"source_automorphism_rechecks\":0";
    if(sat){out<<",\"candidate_pattern\":\""<<pattern<<"\",\"orbit_index\":"<<currentO
       <<",\"external_orbit_index\":"<<currentQ<<",\"selected_S\":";list(out,S);}
    if(stopped){out<<",\"last_visited_pattern\":\""<<pattern<<"\",\"selected_S\":";list(out,S);}
    out<<"}\n";
    std::cout<<status<<" visited="<<visited<<" nodes="<<nodes<<" cpu="<<elapsed()<<'\n';
  }
};

int main(int argc,char**argv){
  Search s;s.start=std::clock();s.seconds=std::stod(argv[1]);
  std::ifstream in("INPUT.txt");
  for(int u=0;u<106;++u){int label,n;in>>label>>n;s.degree[label]=n;for(int j=0;j<n;++j){int v;in>>v;s.A[label].set(v);}}
  int n;in>>n;for(int i=0;i<n;++i){int v;in>>v;s.fixed.push_back(v);}
  in>>n;for(int i=0;i<n;++i){std::vector<int>row(7);for(int&v:row)in>>v;s.orbits.push_back(row);}
  s.run();if(s.sat)s.emitCandidate();s.result();
}
