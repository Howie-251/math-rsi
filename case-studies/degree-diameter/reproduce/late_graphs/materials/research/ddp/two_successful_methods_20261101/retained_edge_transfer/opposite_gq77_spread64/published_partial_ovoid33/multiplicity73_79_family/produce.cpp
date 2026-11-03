#include <algorithm>
#include <array>
#include <cstdio>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <vector>
struct Input{
  FILE*f;std::array<char,1<<20>b{};size_t at=0,size=0;
  explicit Input(const char*p):f(std::fopen(p,"rb")){}
  int get(){if(at==size){size=std::fread(b.data(),1,b.size(),f);at=0;if(!size)return -1;}return static_cast<unsigned char>(b[at++]);}
  bool number(uint32_t&x){int c;do{c=get();if(c<0)return false;}while(c<=32);x=0;do{x=10*x+c-'0';c=get();}while(c>32);return true;}
  ~Input(){if(f)std::fclose(f);}
};
struct Output{
  FILE*f;std::array<char,1<<20>b{};size_t size=0;
  explicit Output(const std::string&p):f(std::fopen(p.c_str(),"wb")){}
  void flush(){if(size){std::fwrite(b.data(),1,size,f);size=0;}}
  void ch(char c){if(size==b.size())flush();b[size++]=c;}
  void number(uint32_t x){char d[12];int n=0;do{d[n++]=char('0'+x%10);x/=10;}while(x);while(n)ch(d[--n]);}
  void pair(uint32_t u,uint32_t v){number(u);ch(' ');number(v);ch('\n');}
  bool close(){flush();bool ok=!std::ferror(f);ok=std::fclose(f)==0&&ok;f=nullptr;return ok;}
  ~Output(){if(f)close();}
};
struct Edge{uint32_t u,v;};
constexpr int SOURCE_N=160050,CENTERS=1650;constexpr uint32_t SOURCE_M=5121600;
int main(int argc,char**argv){
  if(argc!=3)return 2;double budget=std::stod(argv[2]),began=double(std::clock())/CLOCKS_PER_SEC;
  std::ifstream config("CENTERS_INPUT.txt");int centers;config>>centers;if(centers!=CENTERS)return 3;
  std::array<int,SOURCE_N>center_index,pin_owner;center_index.fill(-1);pin_owner.fill(-1);
  std::vector<int>labels(CENTERS);std::vector<std::vector<int>>pins(CENTERS),actual(CENTERS);
  for(int i=0;i<CENTERS;i++){
    int label,count;config>>label>>count;if(count!=64||label<0||label>=SOURCE_N||center_index[label]>=0)return 4;
    labels[i]=label;center_index[label]=i;
    for(int j=0;j<64;j++){int p;config>>p;if(p<0||p>=SOURCE_N||pin_owner[p]>=0)return 5;pin_owner[p]=i;pins[i].push_back(p);}
    std::sort(pins[i].begin(),pins[i].end());
  }
  if(!config)return 6;
  Input input(argv[1]);if(!input.f)return 7;uint32_t n,m;if(!input.number(n)||!input.number(m)||n!=SOURCE_N||m!=SOURCE_M)return 8;
  std::vector<Edge>old;old.reserve(m);std::array<int,SOURCE_N>source_degree{};Edge previous{0,0};
  for(uint32_t i=0;i<m;i++){
    uint32_t u,v;if(!input.number(u)||!input.number(v)||u>=v||v>=SOURCE_N)return 9;
    if(i&&(u<previous.u||(u==previous.u&&v<=previous.v)))return 10;
    old.push_back({u,v});previous={u,v};source_degree[u]++;source_degree[v]++;
    if(center_index[u]>=0)actual[center_index[u]].push_back(v);
    if(center_index[v]>=0)actual[center_index[v]].push_back(u);
  }
  uint32_t extra;if(input.number(extra))return 11;
  for(int i=0;i<CENTERS;i++){std::sort(actual[i].begin(),actual[i].end());if(actual[i]!=pins[i])return 12;}
  uint64_t pin_count=0;for(int x:pin_owner)pin_count+=x>=0;if(pin_count!=105600)return 13;
  std::cout<<std::setprecision(12)<<"{\"status\":\"PASS_PRODUCED_SEVEN_UPPER_ENDPOINTS_PENDING_FRESH_ACCEPTANCE\",\"source_literal_parses\":1,\"source_n\":160050,\"source_m\":5121600,\"immutable_fullN_bindings\":1650,\"immutable_pin_count\":105600,\"cases\":[";
  for(int k=9;k<=15;k++){
    if(double(std::clock())/CLOCKS_PER_SEC-began>=budget)return 14;
    uint32_t targetn=SOURCE_N+CENTERS*k,targetm=SOURCE_M+105600*k;
    std::string path="graphs/d"+std::to_string(64+k)+"_D3_n"+std::to_string(targetn)+".edges";
    Output out(path);if(!out.f)return 15;out.pair(targetn,targetm);
    std::vector<uint32_t>degree(targetn);uint64_t written=0,retained=0,added=0;size_t at=0;
    for(int u=0;u<SOURCE_N;u++){
      while(at<old.size()&&old[at].u==uint32_t(u)){auto e=old[at++];out.pair(e.u,e.v);degree[e.u]++;degree[e.v]++;written++;retained++;}
      if(pin_owner[u]>=0)for(int copy=0;copy<k;copy++){uint32_t v=SOURCE_N+CENTERS*copy+pin_owner[u];out.pair(u,v);degree[u]++;degree[v]++;written++;added++;}
    }
    if(!out.close()||at!=old.size()||retained!=SOURCE_M||added!=uint64_t(105600*k)||written!=targetm)return 16;
    std::map<uint32_t,uint32_t>hist;for(auto d:degree)hist[d]++;
    for(int v=SOURCE_N;v<int(targetn);v++)if(degree[v]!=64)return 17;
    if(hist.size()!=2||hist[64]!=uint32_t(54450+CENTERS*k)||hist[64+k]!=105600)return 18;
    if(k>9)std::cout<<',';
    std::cout<<"{\"copy_count\":"<<k<<",\"degree_cap\":"<<64+k<<",\"n\":"<<targetn<<",\"m\":"<<written
      <<",\"path\":\""<<path<<"\",\"header\":true,\"retained_source_edges\":"<<retained<<",\"new_old_source_edges\":"<<added
      <<",\"new_new_edges\":0,\"clone_count\":"<<CENTERS*k<<",\"actual_new_degrees_all64\":true,\"degree_histogram\":{\"64\":"<<hist[64]<<",\""<<64+k<<"\":"<<hist[64+k]<<"},\"strict_lex_body\":true}";
  }
  std::cout<<"],\"old_source_only_neighborhoods\":true,\"currentR2_checks\":0,\"BFS_runs\":0,\"Lean_compilations\":0,\"CPU_seconds\":"<<double(std::clock())/CLOCKS_PER_SEC-began<<"}\n";
}
