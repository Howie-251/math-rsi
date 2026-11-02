#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Mask=array<uint64_t,6>;
struct Triple {array<int,3> vertices;uint32_t bits;Mask r3{},r4{};};
template<class C>void ints(ostream&f,const C&v){f<<'[';bool first=true;for(auto x:v){if(!first)f<<',';first=false;f<<x;}f<<']';}
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
int main(int argc,char**argv){
 need(argc==5,"usage: scan SOURCE MASKBIN OUTDIR CPUbudget");
 clock_t start=clock();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
 filesystem::path output=argv[3];double budget=stod(argv[4]);filesystem::create_directories(output);
 try{
  ifstream f(argv[1]);int n,m;f>>n>>m;need(n==364&&m==714,"unexpected hostbinding");
  vector<pair<int,int>>edges;vector<int>deg(n);
  for(int j=0;j<m;++j){int u,v;f>>u>>v;need(bool(f)&&u>=0&&u<n&&v>=0&&v<n&&u!=v,"bad hostedge");edges.emplace_back(u,v);++deg[u];++deg[v];}
  vector<int>actualports;for(int u=0;u<n;++u){need(deg[u]==3||deg[u]==4,"hostdegree outside3/4");if(deg[u]==3)actualports.push_back(u);}
  need(actualports.size()==28,"naturalhost musthave28degree3ports");
  ifstream bin(argv[2],ios::binary);uint32_t count,bn,bw;bin.read((char*)&count,4);bin.read((char*)&bn,4);bin.read((char*)&bw,4);
  need(count==28&&bn==364&&bw==6,"bad maskheader");
  vector<int>ports;vector<Mask>r3(count),r4(count);
  for(unsigned j=0;j<count;++j){uint32_t v;bin.read((char*)&v,4);ports.push_back(v);bin.read((char*)r3[j].data(),48);bin.read((char*)r4[j].data(),48);}
  need(bool(bin)&&ports==actualports,"maskports do notmatch actualhost");
  const Mask full={~uint64_t(0),~uint64_t(0),~uint64_t(0),~uint64_t(0),~uint64_t(0),(uint64_t(1)<<44)-1};
  vector<Triple>triples;
  for(int a=0;a<28;++a)for(int b=a+1;b<28;++b)for(int c=b+1;c<28;++c){
   Triple t;t.vertices={ports[a],ports[b],ports[c]};t.bits=(uint32_t(1)<<a)|(uint32_t(1)<<b)|(uint32_t(1)<<c);
   for(int w=0;w<6;++w){t.r3[w]=r3[a][w]|r3[b][w]|r3[c][w];t.r4[w]=r4[a][w]|r4[b][w]|r4[c][w];}
   triples.push_back(t);
  }
  need(triples.size()==3276,"triplecount mismatch");
  uint64_t checked=0,overlap=0,fail1=0,fail2=0;bool stop=false,hit=false;string status="RUNNING",firstfailure="null";
  double prep=cpu(),profile=0,forecast=0;int ai=-1,bi=-1;
  for(size_t a=0;a<triples.size()&&!stop;++a)for(size_t b=a+1;b<triples.size()&&!stop;++b){
   if(triples[a].bits&triples[b].bits){++overlap;continue;}
   if((checked&1023)==0&&cpu()>=budget){status="BUDGET_UNKNOWN";stop=true;break;}
   ++checked;int failed=0,missing=-1;
   for(int w=0;w<6;++w){uint64_t absent=full[w]&~(triples[a].r4[w]|triples[b].r3[w]);if(absent){failed=1;missing=64*w+__builtin_ctzll(absent);break;}}
   if(!failed)for(int w=0;w<6;++w){uint64_t absent=full[w]&~(triples[a].r3[w]|triples[b].r4[w]);if(absent){failed=2;missing=64*w+__builtin_ctzll(absent);break;}}
   if(failed==1)++fail1;else if(failed==2)++fail2;
   else{hit=true;ai=a;bi=b;status="FIRST_COMPLETE_HIT_STOP";stop=true;}
   if(failed&&firstfailure=="null"){
    ostringstream s;s<<"{\"triple_indices\":["<<a<<','<<b<<"],\"Na\":";ints(s,triples[a].vertices);s<<",\"Nb\":";ints(s,triples[b].vertices);s<<",\"failed_condition\":"<<failed<<",\"first_missing_old_vertex\":"<<missing<<'}';firstfailure=s.str();
   }
   if(checked==1000&&!stop){
    profile=cpu()-prep;forecast=prep+profile*3767400.0/1000.0;
    ofstream p(output/"profile1000.json");p<<"{\"eligiblepairs\":1000,\"scan_CPU_seconds\":"<<profile<<",\"preparation_CPU_seconds\":"<<prep<<",\"projected_allpairs_native_CPU_seconds\":"<<forecast<<",\"native_budget\":"<<budget<<"}\n";
    cout<<"PROFILE1000 CPU="<<profile<<" forecast="<<forecast<<endl;
    if(forecast>budget-0.2){status="PROFILE_UNKNOWN";stop=true;}
   }
  }
  if(hit){
   auto&a=triples[ai];auto&b=triples[bi];
   ofstream g(output/"graph_d4_D5_n366.edges");g<<366<<' '<<m+7<<'\n';for(auto[u,v]:edges)g<<u<<' '<<v<<'\n';for(int u:a.vertices)g<<u<<" 364\n";for(int v:b.vertices)g<<v<<" 365\n";g<<"364 365\n";
   ofstream p(output/"first_hit.json");
   p<<"{\"status\":\"PRODUCER_COMPLETE_ROOT_CHECK_PENDING\",\"source_n\":364,\"source_m\":714,\"new_n\":366,\"new_m\":721,\"degree_cap\":4,\"target_D\":5,\"actual_all_source_D\":null,\"new_vertices\":[364,365],\"interedge\":[364,365],\"Na\":";ints(p,a.vertices);p<<",\"Nb\":";ints(p,b.vertices);
   p<<",\"old_pin_degrees_A\":[3,3,3],\"old_pin_degrees_B\":[3,3,3],\"new_degrees\":[4,4],\"Na_Nb_disjoint\":true,\"old_edges_retained\":true,\"condition1_missing\":0,\"condition2_missing\":0,\"triple_indices\":["<<ai<<','<<bi<<"],\"eligiblepair_ordinal\":"<<checked<<",\"R3_Na\":";ints(p,a.r3);p<<",\"R4_Na\":";ints(p,a.r4);p<<",\"R3_Nb\":";ints(p,b.r3);p<<",\"R4_Nb\":";ints(p,b.r4);p<<",\"full364mask\":";ints(p,full);p<<",\"graph_file\":\"graph_d4_D5_n366.edges\"}\n";
  }else if(checked==3767400){status="COMPLETE_NO_HIT";need(fail1+fail2==checked,"counter mismatch");}
  ofstream t(output/"native_terminal.json");t<<"{\"status\":\""<<status<<"\",\"source_n\":364,\"source_m\":714,\"triples\":3276,\"complete_pairspace\":"<<((checked==3767400)?"true":"false")<<",\"eligiblepairs_total\":3767400,\"eligiblepairs_checked\":"<<checked<<",\"eligiblepairs_untested\":"<<3767400-checked<<",\"overlapping_pairs_skipped\":"<<overlap<<",\"first_condition_failures\":"<<fail1<<",\"second_condition_failures\":"<<fail2<<",\"full_hits\":"<<(hit?1:0)<<",\"first_failure\":"<<firstfailure<<",\"native_CPU_seconds\":"<<cpu()<<",\"native_budget\":"<<budget<<",\"preparation_CPU_seconds\":"<<prep<<",\"profile1000_scan_CPU_seconds\":"<<profile<<",\"projected_allpairs_CPU_seconds\":"<<forecast<<",\"source_allroot_BFS\":0,\"port_balls_reused\":true}\n";
  cout<<status<<" checked="<<checked<<" CPU="<<cpu()<<endl;
 }catch(const exception&e){ofstream f(output/"error.txt");f<<e.what()<<'\n';cerr<<e.what()<<'\n';return 1;}
}
