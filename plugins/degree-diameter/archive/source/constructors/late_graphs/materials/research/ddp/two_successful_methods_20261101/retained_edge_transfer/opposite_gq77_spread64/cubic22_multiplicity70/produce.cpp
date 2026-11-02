#include <algorithm>
#include <array>
#include <charconv>
#include <cstdio>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <utility>
#include <vector>
using namespace std;
constexpr int P=400,K=8,J=50,C=1100,COPIES=6,NC=C*COPIES,SN=160050,FN=166650;
constexpr long long SM=5121600,BASELOAD=70400,NM=422400,FM=5544000;
void need(bool x,const string&s){if(!x)throw runtime_error(s);}
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
struct Input{
  FILE*f;array<unsigned char,1<<20>b{};size_t at=0,n=0;
  explicit Input(const char*p):f(fopen(p,"rb")){need(f!=nullptr,"inputopen");}
  ~Input(){if(f)fclose(f);}
  int get(){if(at==n){n=fread(b.data(),1,b.size(),f);at=0;if(!n)return EOF;}return b[at++];}
  bool next(int&v){int c;do{c=get();}while(c!=EOF&&c<=32);if(c==EOF)return false;
    need(c>='0'&&c<='9',"inputnondigit");v=0;
    do{v=v*10+c-'0';c=get();}while(c>='0'&&c<='9');
    need(c==EOF||c<=32,"inputbadseparator");return true;}
  int integer(){int v;need(next(v),"inputtruncated");return v;}
};
struct Output{
  FILE*f;array<char,1<<20>b{};size_t n=0;long long lines=0;
  explicit Output(const char*p):f(fopen(p,"wb")){need(f!=nullptr,"outputopen");}
  void flush(){need(fwrite(b.data(),1,n,f)==n,"outputwrite");n=0;}
  void integer(int x,char sep){if(n+24>=b.size())flush();auto r=to_chars(b.data()+n,b.data()+b.size(),x);n=r.ptr-b.data();b[n++]=sep;}
  void pair(int u,int v){integer(u,' ');integer(v,'\n');++lines;}
  void close(){flush();need(fclose(f)==0,"outputclose");f=nullptr;}
  ~Output(){if(f)fclose(f);}
};
int main(){
  const double start=cpu();
  try{
    need(filesystem::exists("PRED.json"),"missingprediction");
    need(!filesystem::exists("graph_d70_D3_n166650.edges")&&!filesystem::exists("graph_d70_D3_n166650.edges.tmp"),"fixedproductionalreadyexists");
    ifstream table("PRODUCTION_INPUT.txt");int p,k,j,c,copies;table>>p>>k>>j>>c>>copies;
    need(p==P&&k==K&&j==J&&c==C&&copies==COPIES,"inputheader");
    array<array<int,K>,P>LP{},PL{};array<int,J>spread{};array<int,P>owner{};
    for(auto&r:LP)for(int&x:r)table>>x;
    for(auto&r:PL)for(int&x:r)table>>x;
    for(int&x:spread)table>>x;for(int&x:owner)table>>x;
    array<int,C>center{},point{},line{},spreadindex{};array<vector<int>,C>formula,literal;
    vector<int>centerindex(SN,-1);
    for(int i=0;i<C;++i){
      int index,pi;table>>index>>pi>>point[i]>>spreadindex[i]>>line[i]>>center[i];
      need(index==i&&pi==i/J&&spreadindex[i]==i%J,"basecenterorder");
      need(point[i]>=0&&point[i]<P&&line[i]==spread[i%J]&&center[i]==P*point[i]+line[i],"basecenterbinding");
      need(centerindex[center[i]]==-1,"duplicatebasecenter");centerindex[center[i]]=i;
      for(int q:LP[line[i]])for(int m:PL[point[i]]){int v=P*q+m;if(v!=center[i])formula[i].push_back(v);}
      bool flag=binary_search(PL[point[i]].begin(),PL[point[i]].end(),line[i]);
      if(flag){need(owner[point[i]]==i%J,"bonusowner");formula[i].push_back(160000+owner[point[i]]);}
      sort(formula[i].begin(),formula[i].end());
      need(formula[i].size()==64&&adjacent_find(formula[i].begin(),formula[i].end())==formula[i].end(),"formulaneighbors");
      literal[i].reserve(64);
    }
    need(bool(table),"productioninputtruncated");
    vector<int>source_degree(SN,0);
    {
      Input source("../graph_d64_D3_n160050.edges");
      need(source.integer()==SN&&source.integer()==SM,"sourceheader");
      pair<int,int>last{-1,-1};
      for(long long z=0;z<SM;++z){
        int u=source.integer(),v=source.integer();
        need(u>=0&&u<v&&v<SN&&last<pair<int,int>{u,v},"sourcesimpleorder");last={u,v};
        ++source_degree[u];++source_degree[v];
        if(centerindex[u]>=0)literal[centerindex[u]].push_back(v);
        if(centerindex[v]>=0)literal[centerindex[v]].push_back(u);
      }
      int extra;need(!source.next(extra),"sourceextraedge");
    }
    for(int d:source_degree)need(d==64,"sourceregular64");
    vector<int>base_load(SN,0),load(SN,0);
    for(int i=0;i<C;++i){
      sort(literal[i].begin(),literal[i].end());
      need(literal[i]==formula[i],"literal_source_neighborhood_binding_at_basecenter"+to_string(i));
      for(int v:literal[i])need(++base_load[v]<=1,"basepackloadgreaterthanone");
    }
    need(count(base_load.begin(),base_load.end(),1)==BASELOAD,"basepackunion");
    vector<pair<int,int>>added;added.reserve(NM);
    ofstream prefix("PREFIX_LOADS.csv");
    prefix<<"clone_index,copy,base_index,point_index,spread_index,source_center,new_vertex,current_n_after,pin_degree_before,pin_degree_after,new_vertex_degree,new_edges_so_far\n";
    for(int copy=0;copy<COPIES;++copy)for(int i=0;i<C;++i){
      const int index=C*copy+i,label=SN+index;
      for(int v:literal[i]){
        need(base_load[v]==1&&load[v]==copy,"prefixpinloadbefore");
        ++load[v];need(load[v]<=COPIES,"prefixdegreecap");
        added.emplace_back(v,label);
      }
      prefix<<index<<','<<copy<<','<<i<<','<<i/J<<','<<i%J<<','<<center[i]<<','<<label<<','<<label+1<<','<<64+copy<<','<<65+copy<<",64,"<<added.size()<<'\n';
    }
    prefix.close();need(bool(prefix),"prefixwrite");
    need(added.size()==NM,"addededgecount");
    for(int v=0;v<SN;++v)need(load[v]==COPIES*base_load[v],"finalpinload");
    need(count(load.begin(),load.end(),6)==BASELOAD&&count(load.begin(),load.end(),0)==89650,"loadhistogram");
    sort(added.begin(),added.end());
    need(adjacent_find(added.begin(),added.end())==added.end(),"addedduplicate");
    const double binding_cpu=cpu()-start;
    Input source("../graph_d64_D3_n160050.edges");
    need(source.integer()==SN&&source.integer()==SM,"secondsourceheader");
    Output output("graph_d70_D3_n166650.edges.tmp");
    output.integer(FN,' ');output.integer(FM,'\n');
    size_t ni=0;long long retained=0;pair<int,int>last{-1,-1};
    auto emit=[&](pair<int,int>e){need(e.first>=0&&e.first<e.second&&e.second<FN&&last<e,"finalsimpleorder");output.pair(e.first,e.second);last=e;};
    for(long long z=0;z<SM;++z){
      pair<int,int>old{source.integer(),source.integer()};
      need(old.first>=0&&old.first<old.second&&old.second<SN,"secondsourceedge");
      while(ni<added.size()&&added[ni]<old)emit(added[ni++]);
      emit(old);++retained;
    }
    int extra;need(!source.next(extra),"secondsourceextraedge");
    while(ni<added.size())emit(added[ni++]);
    need(retained==SM&&output.lines==FM,"finaledgecounts");output.close();
    need(rename("graph_d70_D3_n166650.edges.tmp","graph_d70_D3_n166650.edges")==0,"outputrename");
    const double total=cpu()-start,write_cpu=total-binding_cpu;
    ofstream result("PRODUCER_RESULT.json");
    result<<"{\"status\":\"PRODUCER_PASS_FIXED166650_AWAIT_FRESH_INDEPENDENT_ACCEPTANCE\",\"n\":166650,\"m\":5544000,\"source_n\":160050,\"source_m\":5121600,\"old_edges_retained\":5121600,\"new_vertices\":6600,\"new_edges\":422400,\"new_to_new_edges\":0,\"literal_base_source_neighborhoods_bound\":1100,\"source_neighbor_size\":64,\"basepack_maximum_load\":1,\"basepack_union\":70400,\"multiplicity\":6,\"source_load_histogram\":{\"0\":89650,\"6\":70400},\"old_vertices_degree70\":70400,\"old_vertices_degree64\":89650,\"new_vertices_degree64\":6600,\"degree_histogram\":{\"64\":96250,\"70\":70400},\"max_degree\":70,\"prefix_degree_checks\":6600,\"prefix_currentR2_checks\":0,\"prefix_BFS_checks\":0,\"prefix_D3_basis\":\"actual immutable source full-neighborhood clone Walk argument covers every previous clone\",\"source_full_edges_parsed\":5121600,\"source_all64regular_checked\":true,\"source_edgefile_read\":true,\"accepted65_edgefile_read\":false,\"simple\":true,\"strict_lexicographic_u_lt_v\":true,\"edgefile_closed\":true,\"candidate_graphs_generated\":1,\"BFS_calls\":0,\"solver_calls\":0,\"Lean_compilations\":0,\"workers\":1,\"literal_binding_and_repeat_CPU_seconds\":"<<binding_cpu<<",\"streammerge_write_CPU_seconds\":"<<write_cpu<<",\"production_CPU_seconds\":"<<total<<",\"edgefile\":\"graph_d70_D3_n166650.edges\",\"independent_acceptance\":\"PENDING_ROOT_FRESH_READBACK\",\"newroot_histograms\":\"UNTESTED_PREDICTION_ONLY_IN_PRED\",\"public_global_record_or_priority\":\"NOT_CERTIFIED\"}\n";
    result.close();need(bool(result),"resultwrite");
    cout<<"PRODUCER_PASS n="<<FN<<" m="<<FM<<" literalBaseN="<<C<<" multiplicity=6 loadmax=6 degree64=96250 degree70=70400 oldretained="<<retained<<" productionCPU="<<total<<" fileclosed=1\n";
  }catch(const exception&e){ofstream failure("PRODUCTION_FAILURE.txt");failure<<e.what()<<'\n';cerr<<"PRODUCTION_FAILURE "<<e.what()<<'\n';return 2;}
}
