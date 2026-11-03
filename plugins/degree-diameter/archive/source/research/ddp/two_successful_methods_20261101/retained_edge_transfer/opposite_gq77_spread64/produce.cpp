#include <algorithm>
#include <array>
#include <cassert>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <memory>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
constexpr int P=400,K=8,J=50,OLD=P*P,FINAL=OLD+J,CAP=64;
using NRow=array<int,CAP>;
void need(bool ok,const string&message){if(!ok)throw runtime_error(message);}
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
int main(int argc,char**argv){
  const double start=cpu();
  const double geometry_cpu=argc>1?atof(argv[1]):0,compile_cpu=argc>2?atof(argv[2]):0;
  try{
    need(!filesystem::exists("graph_d64_D3_n160050.edges"),"fixedcandidatealreadyexists;do notregenerate");
    ifstream input("TABLES_INPUT.txt");int p,k,j;input>>p>>k>>j;need(p==P&&k==K&&j==J,"tableheader");
    array<array<int,K>,P>LP{},PL{};array<int,J>spread{};array<int,P>owner{};
    for(auto&row:LP)for(auto&v:row)input>>v;
    for(auto&row:PL)for(auto&v:row)input>>v;
    for(auto&v:spread)input>>v;for(auto&v:owner)input>>v;
    need(bool(input),"tabletruncated");
    for(auto&row:LP)need(is_sorted(row.begin(),row.end())&&adjacent_find(row.begin(),row.end())==row.end(),"LPorder");
    for(auto&row:PL)need(is_sorted(row.begin(),row.end())&&adjacent_find(row.begin(),row.end())==row.end(),"PLorder");
    vector<NRow>N(FINAL);vector<int>degree(FINAL,0),old_degree(OLD);vector<unsigned char>used(OLD,0);
    long long source_directed=0,flags=0;
    for(int point=0;point<P;++point)for(int line=0;line<P;++line){
      int u=P*point+line;
      for(int q:LP[line])for(int m:PL[point]){int v=P*q+m;if(v!=u)N[u][degree[u]++]=v;}
      bool flag=binary_search(PL[point].begin(),PL[point].end(),line);
      need(degree[u]==CAP-int(flag),"sourcedegree");
      need(is_sorted(N[u].begin(),N[u].begin()+degree[u]),"sourceneighbororder");
      need(adjacent_find(N[u].begin(),N[u].begin()+degree[u])==N[u].begin()+degree[u],"sourceduplicate");
      source_directed+=degree[u];flags+=flag;old_degree[u]=degree[u];
    }
    need(flags==3200&&source_directed==10236800,"sourcecounts");
    double source_cpu=cpu()-start;
    ofstream source("SOURCE_CHECK.json");
    source<<"{\"status\":\"PASS_LITERAL_SOURCE_GENERATED_ONCE_NO_SOURCE_BFS\",\"n\":160000,\"m\":5118400,\"degree_histogram\":{\"63\":3200,\"64\":156800},\"flags\":3200,\"source_BFS_runs\":0,\"source_CPU_seconds\":"<<source_cpu<<",\"rule\":\"distinct400*p+l~400*q+m iff qinLP[l],minPL[p]\"}\n";source.close();
    vector<unsigned char>dist(FINAL,255);vector<int>queue;queue.reserve(FINAL);
    ostringstream steps;steps<<"[";int used_count=0;
    double prefix_start=cpu();
    for(int index=0;index<J;++index){
      const int current=OLD+index;vector<int>pins;pins.reserve(CAP);
      for(int point:LP[spread[index]]){
        need(owner[point]==index,"frozenowner");
        for(int line:PL[point])pins.push_back(P*point+line);
      }
      need(pins.size()==CAP&&is_sorted(pins.begin(),pins.end()),"pinsizeorder");
      need(adjacent_find(pins.begin(),pins.end())==pins.end(),"pinduplicate");
      for(int pin:pins)need(!used[pin]&&degree[pin]==63,"pinspare");
      fill(dist.begin(),dist.begin()+current,255);queue.clear();
      for(int pin:pins){dist[pin]=0;queue.push_back(pin);}
      for(size_t pos=0;pos<queue.size();++pos){
        int u=queue[pos];if(dist[u]==2)continue;
        for(int z=0;z<degree[u];++z){int v=N[u][z];need(v<current,"currentprefixneighbor");if(dist[v]==255){dist[v]=dist[u]+1;queue.push_back(v);}}
      }
      need(int(queue.size())==current,"completecurrentR2coveragefailure_at_step"+to_string(index));
      array<int,3>hist{};for(int u=0;u<current;++u){need(dist[u]<=2,"R2uncovered");hist[dist[u]]++;}
      for(int u=OLD;u<current;++u)need(dist[u]==2,"priorbonusdistance");
      need(hist[0]==64,"R2rootpins");
      for(int pin:pins){N[pin][degree[pin]++]=current;used[pin]=1;++used_count;need(degree[pin]==64,"pinfinaldegree");}
      for(int pin:pins)N[current][degree[current]++]=pin;
      need(degree[current]==64,"bonusdegree");
      if(index)steps<<',';
      steps<<"{\"step\":"<<index<<",\"new_vertex\":"<<current<<",\"spread_line\":"<<spread[index]<<",\"slope_code\":";
      if(index<49)steps<<index;else steps<<"\"infinity\"";
      steps<<",\"pins\":[";for(int z=0;z<CAP;++z){if(z)steps<<',';steps<<pins[z];}
      steps<<"],\"pins_count\":64,\"pin_degree_before\":{\"63\":64},\"current_n_before\":"<<current<<",\"full_current_R2_covered\":"<<queue.size()<<",\"R2_uncovered_count\":0,\"R2_distance_histogram\":{\"0\":"<<hist[0]<<",\"1\":"<<hist[1]<<",\"2\":"<<hist[2]<<"},\"earlier_bonus_distance2_count\":"<<index<<",\"degree_cap_after\":64}";
    }
    steps<<']';double prefix_cpu=cpu()-prefix_start;
    need(used_count==3200,"allflagsusedonce");
    long long oldold=0,oldnew=0,newnew=0;
    for(int u=0;u<FINAL;++u){
      need(degree[u]==64,"finaldegree");
      need(is_sorted(N[u].begin(),N[u].end()),"finalneighbororder");
      need(adjacent_find(N[u].begin(),N[u].end())==N[u].end(),"finalduplicate");
      for(int v:N[u]){
        need(v!=u&&v>=0&&v<FINAL,"finalsimple");
        need(binary_search(N[v].begin(),N[v].end(),u),"finalreciprocity");
        if(u<v){if(v<OLD)++oldold;else if(u<OLD)++oldnew;else ++newnew;}
      }
      if(u<OLD){int count=0;for(int v:N[u])count+=v<OLD;need(count==old_degree[u],"oldedgeprefixretention");}
    }
    need(oldold==5118400&&oldnew==3200&&newnew==0,"finaledgepartition");
    double before_write=cpu();
    FILE*out=fopen("graph_d64_D3_n160050.edges.tmp","w");need(out!=nullptr,"outputopen");
    auto buffer=make_unique<char[]>(4*1024*1024);setvbuf(out,buffer.get(),_IOFBF,4*1024*1024);
    fprintf(out,"160050 5121600\n");long long written=0;
    for(int u=0;u<FINAL;++u)for(int v:N[u])if(u<v){fprintf(out,"%d %d\n",u,v);++written;}
    need(written==5121600,"writtenedgecount");need(fclose(out)==0,"outputclose");
    need(rename("graph_d64_D3_n160050.edges.tmp","graph_d64_D3_n160050.edges")==0,"outputrename");
    double write_cpu=cpu()-before_write,total=cpu()-start;
    ofstream extension("EXTENSION_STEPS.json");
    extension<<"{\"status\":\"ALL50_COMPLETE_CURRENT_R2_CHECKS_PASS\",\"source_vertices\":160000,\"final_vertices\":160050,\"final_edges\":5121600,\"all3200_flags_used_once\":true,\"all_old_edges_retained\":5118400,\"steps\":"<<steps.str()<<"}\n";extension.close();
    ofstream result("RESULT.json");
    result<<"{\"status\":\"PRODUCER_PASS_FIXED160050_CANDIDATE_AWAIT_INDEPENDENT_ACCEPTANCE\",\"target_Delta\":64,\"target_D\":3,\"n\":160050,\"m\":5121600,\"source_n\":160000,\"source_m\":5118400,\"source_degree_histogram\":{\"63\":3200,\"64\":156800},\"degree_histogram\":{\"64\":160050},\"geometry_points\":400,\"geometry_lines\":400,\"geometry_unique_projections\":156800,\"spread_lines\":50,\"new_vertices\":50,\"pins_each\":64,\"new_edges\":3200,\"old_edges_retained\":5118400,\"new_new_edges\":0,\"simple\":true,\"reciprocal\":true,\"current_complete_R2_checks\":50,\"R2_uncovered_count\":0,\"includes_previous_bonus_vertices\":true,\"source_BFS_runs\":0,\"final_allroot_BFS_runs\":0,\"geometry_CPU_seconds\":"<<geometry_cpu<<",\"compile_CPU_seconds\":"<<compile_cpu<<",\"production_CPU_seconds\":"<<total<<",\"source_adjacency_CPU_seconds\":"<<source_cpu<<",\"all50_prefix_R2_CPU_seconds\":"<<prefix_cpu<<",\"edgefile_write_CPU_seconds\":"<<write_cpu<<",\"total_measured_CPU_seconds\":"<<(geometry_cpu+compile_cpu+total)<<",\"total_CPU_budget_seconds\":300,\"workers\":1,\"solver_calls\":0,\"actual_candidate_graphs_generated\":1,\"source_reproduction_counted_new\":false,\"independent_acceptance\":\"PENDING_ROOT_SEPARATE_LITERAL_CHECK\",\"concrete_Lean\":\"SEPARATE_TASK\",\"public_global_record_or_priority\":\"NOT_CERTIFIED\",\"edgefile\":\"graph_d64_D3_n160050.edges\",\"edgefile_closed_and_sorted\":true}\n";result.close();
    ofstream terminal("TERMINAL.json");terminal<<"{\"status\":\"PRODUCER_FIXED160050_LOCAL_TERMINAL\",\"running\":false,\"graph_file_complete\":true,\"independent_acceptance_pending\":true,\"next\":\"Returnliteralgraph;noq/degree65/ovoid/clonecontinuation\"}\n";terminal.close();
    cout<<"PRODUCER_PASS n=160050 m=5121600 regular=64 source_m=5118400 prefixR2=50 productionCPU="<<total<<" totalCPU="<<(geometry_cpu+compile_cpu+total)<<" fileclosed=1\n";
  }catch(const exception&e){
    ofstream failure("PRODUCTION_FAILURE.txt");failure<<e.what()<<'\n';cerr<<"PRODUCTION_FAILURE "<<e.what()<<'\n';return 2;
  }
}
