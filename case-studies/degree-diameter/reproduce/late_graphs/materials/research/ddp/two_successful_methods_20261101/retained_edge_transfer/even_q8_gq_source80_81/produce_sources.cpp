#include <algorithm>
#include <cstdio>
#include <cstdint>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>
struct Output{
  FILE*f;std::vector<char>b;size_t at=0;
  explicit Output(const std::string&p):f(std::fopen(p.c_str(),"wb")),b(1<<20){}
  void flush(){if(at){std::fwrite(b.data(),1,at,f);at=0;}}
  void ch(char c){if(at==b.size())flush();b[at++]=c;}
  void number(uint32_t x){char d[12];int n=0;do{d[n++]=char('0'+x%10);x/=10;}while(x);while(n)ch(d[--n]);}
  void pair(uint32_t a,uint32_t b){number(a);ch(' ');number(b);ch('\n');}
  bool close(){flush();bool ok=!std::ferror(f);ok=std::fclose(f)==0&&ok;f=nullptr;return ok;}
  ~Output(){if(f)close();}
};
int main(int argc,char**argv){
  if(argc!=5)return 2;std::string mode=argv[1];double began=double(std::clock())/CLOCKS_PER_SEC,budget=std::stod(argv[4]);
  std::ifstream in(argv[2]);uint32_t np,nl,a,b,j,oldn,oldm,n,m,delta;
  in>>np>>nl>>a>>b>>j>>oldn>>oldm>>n>>m>>delta;
  if(!in||oldn!=np*nl||n!=oldn+j||delta!=a*b)return 3;
  if(mode=="derived"){if(np!=512||nl!=640||a!=8||b!=10||j!=64)return 4;}
  else if(mode=="balanced"){if(np!=585||nl!=585||a!=9||b!=9||j!=65)return 5;}else return 6;
  std::vector<std::vector<uint32_t>>lp(nl,std::vector<uint32_t>(a)),pl(np,std::vector<uint32_t>(b));
  std::vector<uint32_t>spread(j),owner(np);
  for(auto&row:lp)for(auto&x:row)in>>x;
  for(auto&row:pl)for(auto&x:row)in>>x;
  for(auto&x:spread)in>>x;for(auto&x:owner)in>>x;if(!in)return 7;
  std::string out=argv[3];std::filesystem::create_directories(out);
  std::string unfilled=out+"/classical_unfilled_d"+std::to_string(delta)+"_n"+std::to_string(oldn)+".edges";
  std::string filled=out+"/graph_d"+std::to_string(delta)+"_D3_n"+std::to_string(n)+".edges";
  if(std::filesystem::exists(unfilled)||std::filesystem::exists(filled))return 8;
  Output oldout(unfilled),newout(filled);if(!oldout.f||!newout.f)return 9;
  oldout.pair(oldn,oldm);newout.pair(n,m);
  uint64_t old_written=0,new_written=0,flags=0;std::vector<std::vector<uint32_t>>pins(j);
  std::vector<uint32_t>ns;ns.reserve(delta);
  for(uint32_t p=0;p<np;p++)for(uint32_t l=0;l<nl;l++){
    if((l&127)==0&&double(std::clock())/CLOCKS_PER_SEC-began>budget)return 10;
    uint32_t u=p*nl+l;ns.clear();
    for(uint32_t q:lp[l])for(uint32_t M:pl[p]){uint32_t v=q*nl+M;if(v!=u)ns.push_back(v);}
    std::sort(ns.begin(),ns.end());bool flag=std::binary_search(pl[p].begin(),pl[p].end(),l);
    if(ns.size()!=delta-uint32_t(flag)||std::adjacent_find(ns.begin(),ns.end())!=ns.end())return 11;
    for(uint32_t v:ns)if(u<v){oldout.pair(u,v);newout.pair(u,v);old_written++;new_written++;}
    if(flag){
      if(owner[p]>=j)return 12;
      newout.pair(u,oldn+owner[p]);new_written++;flags++;pins[owner[p]].push_back(u);
    }
  }
  if(!oldout.close()||!newout.close()||old_written!=oldm||new_written!=m||flags!=np*b||flags!=j*delta)return 13;
  for(uint32_t k=0;k<j;k++)if(pins[k].size()!=delta)return 14;
  std::ofstream pinfile(out+"/FILL_PINS.tsv");pinfile<<"fill_index\tnew_label\told_flag_label\n";
  for(uint32_t k=0;k<j;k++)for(uint32_t u:pins[k])pinfile<<k<<'\t'<<oldn+k<<'\t'<<u<<'\n';
  std::ofstream prefix(out+"/PREFIX_DEGREES.csv");prefix<<"prefix,current_n,flags_consumed,old_flags_remaining,degree_low,degree_low_count,degree_cap,degree_cap_count\n";
  uint64_t consumed=0;
  for(uint32_t k=0;k<=j;k++){
    if(k)consumed+=pins[k-1].size();uint64_t remaining=flags-consumed;
    prefix<<k<<','<<oldn+k<<','<<consumed<<','<<remaining<<','<<delta-1<<','<<remaining<<','<<delta<<','<<oldn+k-remaining<<'\n';
  }
  std::cout<<std::setprecision(12)<<"{\"status\":\"PASS_LITERAL_FILLED_SOURCE_PENDING_FRESH_ACCEPTANCE\",\"case\":\""<<mode
    <<"\",\"np\":"<<np<<",\"nl\":"<<nl<<",\"line_size\":"<<a<<",\"point_degree\":"<<b<<",\"spread_size\":"<<j
    <<",\"old_label\":\"p*nl+l\",\"old_n\":"<<oldn<<",\"old_m\":"<<old_written<<",\"n\":"<<n<<",\"m\":"<<new_written
    <<",\"degree\":"<<delta<<",\"flag_count\":"<<flags<<",\"fill_count\":"<<j<<",\"added_edges\":"<<flags
    <<",\"unfilled_path\":\""<<unfilled<<"\",\"filled_path\":\""<<filled<<"\",\"header\":true,\"strict_lex_body\":true,\"all_old_edges_retained\":true,\"fill_fill_edges\":0"
    <<",\"unfilled_degree_histogram\":{\""<<delta-1<<"\":"<<flags<<",\""<<delta<<"\":"<<oldn-flags<<"},\"filled_degree_histogram\":{\""<<delta<<"\":"<<n<<"}"
    <<",\"prefix_rows_including_zero\":"<<j+1<<",\"fresh_geometry_or_field_checks_repeated\":false,\"BFS_runs\":0,\"Lean_compilations\":0,\"new_graphs_accepted_by_producer\":0,\"CPU_seconds\":"<<double(std::clock())/CLOCKS_PER_SEC-began<<"}\n";
}
