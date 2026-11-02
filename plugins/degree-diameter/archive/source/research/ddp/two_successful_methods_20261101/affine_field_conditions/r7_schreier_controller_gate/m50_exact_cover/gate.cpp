#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using Mask=uint64_t;
using Coeff=std::array<int,7>;
struct Form { Coeff c; std::array<int,3> word; };
struct Block { int d; Mask mask; };
constexpr Mask ALL=(Mask(1)<<50)-1;
int mod(int x) { x%=50; return x<0?x+50:x; }
bool insert(Mask &m,int x) { Mask b=Mask(1)<<mod(x); bool fresh=!(m&b); m|=b; return fresh; }
int evaluate(const Coeff &c,const Coeff &p) { int s=0;for(int i=0;i<7;i++)s+=c[i]*p[i];return mod(s); }
std::array<std::array<std::vector<Form>,3>,3> forms;
std::vector<std::pair<std::array<int,2>,Form>> words;
bool load() {
  std::ifstream in("../DISTINCT_FORMS.tsv");std::string line;std::getline(in,line);
  while(std::getline(in,line)) {
    std::istringstream s(line);int a,b;Form f{};s>>a>>b;
    for(int &x:f.c)s>>x;for(int &x:f.word)s>>x;
    if(!s)return false;forms[a][b].push_back(f);
  }
  std::ifstream iw("../ALL_WORD_FORMS.tsv");std::getline(iw,line);
  while(std::getline(iw,line)) {
    std::istringstream s(line);int a,b;Form f{};s>>a;for(int &x:f.word)s>>x;s>>b;for(int &x:f.c)s>>x;
    if(!s)return false;words.push_back({{a,b},f});
  }
  return forms[0][0].size()==50 && words.size()==1029;
}
std::pair<int,int> step(int b,int g,int port,const Coeff &v) {
  int a=v[0],a1=v[1],a2=v[2],s=v[3],t=v[4],r=v[5];
  switch(port) {
    case 0:return {b==0?0:3-b,mod(g+(b==0?a:(b==1?a1:a2)))};
    case 1:return {b==0?0:3-b,mod(g-(b==0?a:(b==1?a2:a1)))};
    case 2:return {(b+1)%3,g};
    case 3:return {(b+2)%3,g};
    case 4:return {b==2?2:1-b,mod(g+(b==2?25:(b==0?s:-s)))};
    case 5:return {b==1?1:2-b,mod(g+(b==1?25:(b==0?t:-t)))};
    default:return {b==0?0:3-b,mod(g+(b==0?25:(b==1?r:-r)))};
  }
}
bool export_solution(const Coeff &v) {
  std::array<std::array<int,7>,150> C{};const int reverse[7]={1,0,3,2,4,5,6};
  for(int u=0;u<150;u++) {
    Mask local[3]={0,0,0};
    for(int p=0;p<7;p++) {
      auto z=step(u/50,u%50,p,v);C[u][p]=50*z.first+z.second;
      if(C[u][p]==u || !insert(local[z.first],z.second))return false;
    }
  }
  for(int u=0;u<150;u++)for(int p=0;p<7;p++)if(C[C[u][p]][reverse[p]]!=u)return false;
  // Bind every saved symbolic word to the literal controller once.
  for(auto aw:words) {
    int u=50*aw.first[0];for(int p:aw.second.word)u=C[u][p];
    if(u!=50*aw.first[1]+evaluate(aw.second.c,v))return false;
  }
  std::array<std::array<std::array<std::array<int,3>,50>,3>,3> witness{};
  for(int a=0;a<3;a++)for(int b=0;b<3;b++) {
    std::array<bool,50> seen{};
    for(auto f:forms[a][b]) {int g=evaluate(f.c,v);if(!seen[g]){seen[g]=true;witness[a][b][g]=f.word;}}
    for(bool x:seen)if(!x)return false;
  }
  std::ofstream cp("controller150.porttable.tsv");cp<<"vertex\tbase\tcoordinate\tp0\tp1\tp2\tp3\tp4\tp5\tp6\n";
  for(int u=0;u<150;u++){cp<<u<<'\t'<<u/50<<'\t'<<u%50;for(int x:C[u])cp<<'\t'<<x;cp<<'\n';}
  std::ofstream ep("controller150.edges");
  for(int u=0;u<150;u++) {std::vector<int> ns(C[u].begin(),C[u].end());std::sort(ns.begin(),ns.end());for(int x:ns)if(u<x)ep<<u<<' '<<x<<'\n';}
  std::ofstream wp("EXACT_THREE_WORDS.tsv");wp<<"source\ttarget\tp0\tp1\tp2\n";
  for(int u=0;u<150;u++)for(int w=0;w<150;w++) {
    auto ps=witness[u/50][w/50][mod(w%50-u%50)];int end=u;for(int p:ps)end=C[end][p];
    if(end!=w)return false;wp<<u<<'\t'<<w;for(int p:ps)wp<<'\t'<<p;wp<<'\n';
  }
  return true;
}
int main(int argc,char **argv) {
  const double budget=argc>1?std::stod(argv[1]):0;
  if(budget<=0 || !load())return 2;
  const double begin=double(std::clock())/CLOCKS_PER_SEC;
  uint64_t outer=0,basepass=0,blocktested=0,blockpass=0,pairnodes=0,tilings=0,fullchecks=0;
  std::array<uint64_t,9> firstfails{};
  bool found=false,timed=false;Coeff solution{};
  for(int a:{2,10})for(int s=1;s<50;s++)for(int t=1;t<50;t++) {
    if((outer&31)==0 && double(std::clock())/CLOCKS_PER_SEC-begin>=budget){timed=true;goto finished;}
    outer++;Mask base=0;bool ok=true;
    for(int z:{a,-a,3*a,-3*a,25,25+2*a,25-2*a})ok=insert(base,z)&&ok;
    for(int v:{s,t}) {for(int e:{-1,1})for(int f:{-1,1})ok=insert(base,e*a+f*v)&&ok;for(int f:{-1,1})ok=insert(base,25+f*v)&&ok;}
    for(int z:{0,s,-s,t,-t,s-t,t-s})ok=insert(base,z)&&ok;
    if(!ok)continue;basepass++;
    std::vector<Block> blocks;
    for(int d=1;d<50;d++) {
      blocktested++;Mask m=0;bool good=true;
      for(int z:{d,d+s,d-t,d+s-t}) {good=insert(m,z)&&good;good=insert(m,-z)&&good;}
      if(good && !(m&base)){blocks.push_back({d,m});blockpass++;}
    }
    const Mask remaining=ALL^base;
    for(size_t i=0;i<blocks.size();i++)for(size_t j=i+1;j<blocks.size();j++) {
      pairnodes++;if(blocks[i].mask&blocks[j].mask)continue;
      Mask wanted=remaining^(blocks[i].mask|blocks[j].mask);
      for(size_t k=j+1;k<blocks.size();k++)if(blocks[k].mask==wanted) {
        tilings++;Coeff v={a,blocks[i].d,mod(-blocks[j].d),s,t,blocks[k].d,25};
        bool full=true;fullchecks++;
        for(int x=0;x<3 && full;x++)for(int y=0;y<3;y++) {
          Mask cover=0;for(auto f:forms[x][y])insert(cover,evaluate(f.c,v));
          if(cover!=ALL){firstfails[3*x+y]++;full=false;break;}
        }
        if(full) {if(!export_solution(v))return 3;solution=v;found=true;goto finished;}
      }
    }
  }
finished:
  const double cpu=double(std::clock())/CLOCKS_PER_SEC-begin;
  std::cout<<std::setprecision(12)<<"{\"status\":\""<<(found?"PASS_FIRST_ACTUAL_M50_CONTROLLER":(timed?"UNKNOWN_CPU_BUDGET_STOP":"COMPLETE_NO_M50_FIXED_FAMILY_CONTROLLER"))
    <<"\",\"search_complete\":"<<(!found&&!timed?"true":"false")<<",\"found\":"<<(found?"true":"false")
    <<",\"modulus\":50,\"normalized_alpha0_representatives\":[2,10],\"outer_pairs_total\":4802,\"outer_pairs_visited\":"<<outer
    <<",\"base26_distinct_pairs\":"<<basepass<<",\"blocks_tested\":"<<blocktested<<",\"blocks_admissible\":"<<blockpass
    <<",\"block_pair_nodes\":"<<pairnodes<<",\"root00_tilings\":"<<tilings<<",\"full_nine_support_checks\":"<<fullchecks
    <<",\"first_failure_by_basepair\":[";
  for(int i=0;i<9;i++){if(i)std::cout<<',';std::cout<<firstfails[i];}
  std::cout<<"],\"parameters_alpha0_alpha1_alpha2_sigma_tau_rho_half\":[";
  if(found)for(int i=0;i<7;i++){if(i)std::cout<<',';std::cout<<solution[i];}
  std::cout<<"],\"literal_portword_checks\":"<<(found?1029:0)<<",\"exported_controller_vertices\":"<<(found?150:0)
    <<",\"exported_controller_edges\":"<<(found?525:0)<<",\"exported_exact_three_walks\":"<<(found?22500:0)
    <<",\"fiber_graphs_generated\":0,\"BFS_runs\":0,\"Lean_compilations\":0,\"CPU_seconds\":"<<cpu<<"}\n";
}
