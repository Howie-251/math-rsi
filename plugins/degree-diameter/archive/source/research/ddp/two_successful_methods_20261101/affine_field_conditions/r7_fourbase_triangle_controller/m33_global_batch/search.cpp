#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <random>
#include <sstream>
#include <string>
#include <vector>
using Mask=uint64_t;
using Values=std::array<int,10>;
struct Form {std::array<int,11> c{};std::array<int,3> word{};std::vector<std::pair<int,int>> terms;int constant=0;};
struct Word {int source,target;Form f;};
std::array<std::vector<Form>,16> forms;
std::vector<Word> allwords;
constexpr Mask ALL=(Mask(1)<<33)-1;
constexpr uint64_t SEED=2026110107ULL, MAXIMUM=2000000;
int mod(int x){x%=33;return x<0?x+33:x;}
int evaluate(const Form &f,const Values &v){int n=f.constant;for(auto ix:f.terms)n+=ix.second*v[ix.first];return mod(n);}
void compile_form(Form &f){f.constant=11*f.c[10];for(int i=0;i<10;i++)if(f.c[i])f.terms.push_back({i,f.c[i]});}
bool load(){
  std::ifstream f("../DISTINCT_FORMS.tsv");std::string line;std::getline(f,line);
  while(std::getline(f,line)){std::istringstream s(line);int a,b;Form x;s>>a>>b;for(int &c:x.c)s>>c;for(int &p:x.word)s>>p;if(!s)return false;compile_form(x);forms[4*a+b].push_back(x);}
  std::ifstream w("../ALL_WORD_FORMS.tsv");std::getline(w,line);
  while(std::getline(w,line)){std::istringstream s(line);Word x;s>>x.source;for(int &p:x.f.word)s>>p;s>>x.target;for(int &c:x.f.c)s>>c;if(!s)return false;compile_form(x.f);allwords.push_back(x);}
  return forms[15].size()==51 && allwords.size()==1372;
}
Mask support(int cl,const Values &v){Mask m=0;for(auto &f:forms[cl])m|=Mask(1)<<evaluate(f,v);return m;}
std::pair<int,int> literal_step(int b,int g,int p,const Values &v){
  switch(p){
    case 0:return {(b+1)%4,mod(g+v[b])};
    case 1:return {(b+3)%4,mod(g-v[(b+3)%4])};
    case 2:return b<3?std::make_pair((b+1)%3,g):std::make_pair(3,mod(g+11));
    case 3:return b<3?std::make_pair((b+2)%3,g):std::make_pair(3,mod(g-11));
    case 4:if(b==0)return {1,mod(g+v[4])};if(b==1)return {0,mod(g-v[4])};if(b==2)return {3,mod(g+v[5])};return {2,mod(g-v[5])};
    case 5:if(b==0)return {2,mod(g+v[6])};if(b==2)return {0,mod(g-v[6])};if(b==1)return {3,mod(g+v[7])};return {1,mod(g-v[7])};
    default:if(b==0)return {3,mod(g+v[8])};if(b==3)return {0,mod(g-v[8])};if(b==1)return {2,mod(g+v[9])};return {1,mod(g-v[9])};
  }
}
void values_json(std::ostream &o,const Values &v){o<<'[';for(int i=0;i<10;i++){if(i)o<<',';o<<v[i];}o<<']';}
void example(const Values &v,int passed){
  std::ofstream o("EXAMPLE_COVERAGE.json");o<<"{\"parameters\":";values_json(o,v);o<<",\"completed_classes_in_check_order\":"<<passed<<",\"classes\":[";
  for(int c=0;c<16;c++){if(c)o<<',';Mask m=support(c,v);o<<"{\"source\":"<<c/4<<",\"target\":"<<c%4<<",\"support_size\":"<<__builtin_popcountll(m)<<",\"missing\":[";bool first=true;for(int g=0;g<33;g++)if(!(m&(Mask(1)<<g))){if(!first)o<<',';first=false;o<<g;}o<<"]}";}
  o<<"]}\n";
}
bool export_controller(const Values &v){
  std::array<std::array<int,7>,132>C{};const int reverse[7]={1,0,3,2,4,5,6};
  for(int u=0;u<132;u++){
    for(int p=0;p<7;p++){auto z=literal_step(u/33,u%33,p,v);C[u][p]=33*z.first+z.second;if(C[u][p]==u)return false;for(int q=0;q<p;q++)if(C[u][q]==C[u][p])return false;}
  }
  for(int u=0;u<132;u++){for(int p=0;p<7;p++)if(C[C[u][p]][reverse[p]]!=u)return false;int b=C[u][2],c=C[b][2];if(u==b||u==c||b==c||C[c][2]!=u)return false;}
  for(auto &w:allwords){int end=33*w.source;for(int p:w.f.word)end=C[end][p];if(end!=33*w.target+evaluate(w.f,v))return false;}
  std::array<std::array<std::array<int,3>,33>,16>witness{};
  for(int c=0;c<16;c++){std::array<bool,33>seen{};for(auto &f:forms[c]){int g=evaluate(f,v);if(!seen[g]){seen[g]=true;witness[c][g]=f.word;}}for(bool x:seen)if(!x)return false;}
  std::ofstream cp("controller132.porttable.tsv");cp<<"vertex\tbase\tcoordinate\tp0\tp1\tp2\tp3\tp4\tp5\tp6\n";
  for(int u=0;u<132;u++){cp<<u<<'\t'<<u/33<<'\t'<<u%33;for(int x:C[u])cp<<'\t'<<x;cp<<'\n';}
  std::ofstream ep("controller132.edges");for(int u=0;u<132;u++){auto ns=C[u];std::sort(ns.begin(),ns.end());for(int x:ns)if(u<x)ep<<u<<' '<<x<<'\n';}
  std::ofstream wp("EXACT_THREE_WORDS.tsv");wp<<"source\ttarget\tp0\tp1\tp2\n";
  for(int u=0;u<132;u++)for(int vtx=0;vtx<132;vtx++){auto ps=witness[4*(u/33)+vtx/33][mod(vtx%33-u%33)];int end=u;for(int p:ps)end=C[end][p];if(end!=vtx)return false;wp<<u<<'\t'<<vtx;for(int p:ps)wp<<'\t'<<p;wp<<'\n';}
  return true;
}
int main(int argc,char **argv){
  const double budget=argc==2?std::stod(argv[1]):0;if(budget<=0||!load())return 2;
  double begin=double(std::clock())/CLOCKS_PER_SEC;
  std::mt19937_64 rng(SEED);uint64_t rawdraws=0;
  auto draw=[&](uint64_t n){uint64_t threshold=uint64_t(-n)%n,x;do{x=rng();rawdraws++;}while(x<threshold);return int(x%n);};
  std::array<int,16>order{};std::iota(order.begin(),order.end(),0);std::stable_sort(order.begin(),order.end(),[](int a,int b){return forms[a].size()<forms[b].size();});
  const int reps[5]={1,2,3,11,22};std::array<uint64_t,5>branches{};std::array<uint64_t,16>fails{};std::array<uint64_t,34>firsthist{};
  uint64_t attempted=0;bool found=false,timed=false;Values best{},solution{};int bestpassed=-1,bestcount=-1;
  std::ofstream attempts("ATTEMPTS.bin",std::ios::binary);
  while(attempted<MAXIMUM){
    if((attempted&4095)==0 && double(std::clock())/CLOCKS_PER_SEC-begin>=budget){timed=true;break;}
    int branch=attempted%5;Values v{};v[0]=reps[branch];v[3]=0;
    v[1]=1+draw(32);v[2]=draw(33);do{v[4]=1+draw(32);}while(v[4]==v[0]);
    do{v[5]=draw(33);}while(v[5]==v[2]);v[6]=1+draw(32);v[7]=draw(33);v[8]=1+draw(32);
    do{v[9]=1+draw(32);}while(v[9]==v[1]);
    int failed=255,count=33,passed=0,firstcount=0;
    for(int ix=0;ix<16;ix++){int c=order[ix];Mask m=support(c,v);int n=__builtin_popcountll(m);if(ix==0)firstcount=n;if(m!=ALL){failed=c;count=n;break;}passed++;}
    attempted++;branches[branch]++;firsthist[firstcount]++;
    std::array<unsigned char,12>record{};for(int i=0;i<10;i++)record[i]=v[i];record[10]=failed;record[11]=count;attempts.write(reinterpret_cast<const char*>(record.data()),record.size());
    if(failed!=255)fails[failed]++;
    if(passed>bestpassed||(passed==bestpassed&&count>bestcount)){best=v;bestpassed=passed;bestcount=count;}
    if(failed==255){if(!export_controller(v))return 3;solution=v;found=true;break;}
  }
  attempts.close();if(attempted)example(best,bestpassed);
  double cpu=double(std::clock())/CLOCKS_PER_SEC-begin;
  std::cout<<std::setprecision(12)<<"{\"status\":\""<<(found?"PASS_FIRST_ACTUAL_M33_CONTROLLER":(timed?"UNKNOWN_CPU_BUDGET_STOP":"UNKNOWN_SAMPLE_CAP_REACHED"))
    <<"\",\"found\":"<<(found?"true":"false")<<",\"family_exclusion\":false,\"search_complete\":false,\"modulus\":33,\"third\":11,\"seed\":"<<SEED
    <<",\"PRNG\":\"std::mt19937_64 with unbiased bounded rejection\",\"raw_PRNG_draws\":"<<rawdraws<<",\"maximum_legal_candidates\":"<<MAXIMUM
    <<",\"legal_candidates_tested\":"<<attempted<<",\"branch_representatives\":[1,2,3,11,22],\"branch_counts\":[";
  for(int i=0;i<5;i++){if(i)std::cout<<',';std::cout<<branches[i];}std::cout<<"],\"check_order\":[";
  for(int i=0;i<16;i++){if(i)std::cout<<',';std::cout<<order[i];}std::cout<<"],\"first_failure_counts_by_source_times4_plus_target\":[";
  for(int i=0;i<16;i++){if(i)std::cout<<',';std::cout<<fails[i];}std::cout<<"],\"first_class_support_histogram_0_through33\":[";
  for(int i=0;i<34;i++){if(i)std::cout<<',';std::cout<<firsthist[i];}
  std::cout<<"],\"representative_completed_classes\":"<<bestpassed<<",\"representative_parameters\":";values_json(std::cout,best);
  std::cout<<",\"solution_parameters\":";if(found)values_json(std::cout,solution);else std::cout<<"[]";
  std::cout<<",\"attempt_record_bytes\":12,\"recorded_attempt_bytes\":"<<attempted*12<<",\"literal_inverse_checks\":"<<(found?924:0)
    <<",\"literal_B_triangles_checked\":"<<(found?132:0)<<",\"symbolic_word_bindings_checked\":"<<(found?1372:0)
    <<",\"exported_controller_vertices\":"<<(found?132:0)<<",\"exported_controller_edges\":"<<(found?462:0)
    <<",\"exported_ordered_three_walks\":"<<(found?17424:0)<<",\"fiber_graphs_generated\":0,\"BFS_runs\":0,\"Lean_compilations\":0,\"CPU_seconds\":"<<cpu<<"}\n";
}
