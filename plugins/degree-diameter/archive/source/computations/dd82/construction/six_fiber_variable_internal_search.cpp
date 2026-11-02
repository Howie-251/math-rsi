// Complete necessary quotient enumeration for nonuniform equitable 6 x 10 fibers.
#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using Row = std::array<int,6>;
using Pattern = std::array<int,5>;
using Matrix = std::array<Row,6>;
struct Result {
 Row d{}; std::string status="not_started";
 long long nodes=0, complete_matrices=0, survivors=0;
 std::map<int,long long> minimum_capacity_histogram;
};
std::array<std::vector<Pattern>,4> patterns;
std::array<std::array<std::vector<std::vector<Row>>,6>,4> options;
std::vector<Result> results;
Matrix q{},bestq{}; Row bestd{};
long long nodes=0, matrices=0, survivors=0;
clock_t started; bool capped=false,have_best=false;
std::array<int,19> bestkey{};
std::ofstream survivor_output;

template<class T> void array_json(std::ostream&out,const T&a) {
 out<<'['; for(size_t i=0;i<a.size();i++){if(i)out<<',';out<<a[i];}out<<']';
}
void matrix_json(std::ostream&out,const Matrix&a) {
 out<<'[';for(int i=0;i<6;i++){if(i)out<<',';array_json(out,a[i]);}out<<']';
}
void generate_patterns(int d,int position,int remaining,Pattern&row) {
 if(position==5){
  if(remaining)return;
  int square=0;for(int x:row)square+=x*x;
  if(square>=17-d-d*d&&square<=22-d-d*d)patterns[d].push_back(row);
  return;
 }
 for(int x=0;x<=remaining;x++){row[position]=x;generate_patterns(d,position+1,remaining-x,row);}
}
void generate_degrees(int position,int lower,Row&d) {
 if(position==6){
  if(d.front()==d.back())return;
  int sum=0;for(int x:d)sum+=x;
  Result r;r.d=d;if(sum%2)r.status="excluded_by_parity";results.push_back(r);return;
 }
 for(int x=lower;x<=3;x++){d[position]=x;generate_degrees(position+1,x,d);}
}
Matrix quotient_defect(const Row&d,const Matrix&q) {
 Matrix r=q,b{};for(int i=0;i<6;i++)r[i][i]=d[i];
 for(int i=0;i<6;i++)for(int j=0;j<6;j++){
  b[i][j]=r[i][j]-10-7*(i==j);
  for(int k=0;k<6;k++)b[i][j]+=r[i][k]*r[k][j];
 }
 return b;
}
void record_survivor(Result&r) {
 r.survivors++;survivors++;
 survivor_output<<"{\"d\":";array_json(survivor_output,r.d);
 survivor_output<<",\"Q\":";matrix_json(survivor_output,q);survivor_output<<"}\n";
 // An explicit representative: minimize maximum cross-degree, then support,
 // then total internal degree, followed by the 15 upper-triangle entries.
 std::array<int,19> key{};int p=4;
 for(int x:r.d)key[2]+=x;
 for(int i=0;i<6;i++)for(int j=i+1;j<6;j++){
  key[0]=std::max(key[0],q[i][j]);key[1]+=q[i][j]>0;key[p++]=q[i][j];
 }
 key[3]=0;for(int x:r.d)key[3]=4*key[3]+x;
 if(!have_best||key<bestkey){have_best=true;bestkey=key;bestq=q;bestd=r.d;}
}
void visit(int i,Result&r) {
 if(capped)return;
 nodes++;r.nodes++;
 if((nodes&1023)==0&&double(clock()-started)/CLOCKS_PER_SEC>=10){capped=true;return;}
 if(i==6){
  matrices++;r.complete_matrices++;
  int minimum=1000;
  for(int a=0;a<6;a++)for(int b=a+1;b<6;b++){
   int h=(1+r.d[a]+r.d[b])*q[a][b];
   for(int k=0;k<6;k++)h+=q[a][k]*q[k][b];
   minimum=std::min(minimum,h);
  }
  r.minimum_capacity_histogram[minimum]++;
  if(minimum>=10)record_survivor(r);
  return;
 }
 int prefix=0,power=1;
 for(int j=0;j<i;j++){prefix+=power*q[i][j];power*=5;}
 for(const Row&row:options[r.d[i]][i][prefix]){
  for(int j=i+1;j<6;j++)q[i][j]=q[j][i]=row[j];
  visit(i+1,r);if(capped)break;
 }
 for(int j=i+1;j<6;j++)q[i][j]=q[j][i]=0;
}
int main(int argc,char**argv) {
 assert(argc==2);started=clock();const std::string prefix=argv[1];
 for(int d=0;d<4;d++){
  Pattern p{};generate_patterns(d,0,8-d,p);
  int power=1;
  for(int i=0;i<6;i++){
   options[d][i].resize(power);
   for(const Pattern&p:patterns[d]){
    Row row{};for(int j=0;j<6;j++)if(j!=i)row[j]=p[j-(j>i)];
    int code=0,mult=1;for(int j=0;j<i;j++){assert(row[j]<=4);code+=mult*row[j];mult*=5;}
    options[d][i][code].push_back(row);
   }
   power*=5;
  }
 }
 assert(patterns[0].size()==185&&patterns[1].size()==140&&patterns[2].size()==90&&patterns[3].size()==51);
 Row d{};generate_degrees(0,0,d);assert(results.size()==80);
 survivor_output.open(prefix+".survivors.jsonl");
 int even_cases=0,completed_cases=0;
 for(Result&r:results)if(r.status!="excluded_by_parity"){
  even_cases++;
  if(capped)continue;
  r.status="running";visit(0,r);
  r.status=capped?"cpu_cap":"complete";
  if(!capped)completed_cases++;
 }
 survivor_output.close();assert(even_cases==40);
 if(have_best){
  std::ofstream b(prefix+".representative.json");b<<"{\"d\":";array_json(b,bestd);
  b<<",\"Q\":";matrix_json(b,bestq);Matrix r=bestq;for(int i=0;i<6;i++)r[i][i]=bestd[i];
  b<<",\"R\":";matrix_json(b,r);b<<",\"defect_quotient\":";matrix_json(b,quotient_defect(bestd,bestq));b<<"}\n";
 }
 std::ofstream out(prefix+".json");
 out<<"{\"scope\":\"Sorted nonuniform internal degrees, all compatible symmetric Q in proved row bounds, then all fifteen cross capacities\",\"complete\":"<<(capped?"false":"true")
    <<",\"stop_reason\":\""<<(capped?"cpu_cap":"complete_domain")<<"\",\"sorted_nonuniform_degree_tuples\":80,\"excluded_by_parity\":40,\"eligible_degree_tuples\":40,\"completed_eligible_tuples\":"<<completed_cases
    <<",\"row_pattern_counts\":[185,140,90,51],\"nodes\":"<<nodes<<",\"row_compatible_matrices\":"<<matrices<<",\"survivors\":"<<survivors<<",\"all_survivors_saved\":true,\"uniform_cases_enumerated\":0,\"cpu_budget_seconds\":10,\"threads\":1,\"cpu_seconds\":"<<double(clock()-started)/CLOCKS_PER_SEC<<",\"degree_tuples\":[";
 bool comma=false;
 for(const Result&r:results){if(comma)out<<',';comma=true;out<<"{\"d\":";array_json(out,r.d);
  out<<",\"status\":\""<<r.status<<"\",\"nodes\":"<<r.nodes<<",\"row_compatible_matrices\":"<<r.complete_matrices<<",\"survivors\":"<<r.survivors<<",\"minimum_capacity_histogram\":{";bool c=false;
  for(auto [k,v]:r.minimum_capacity_histogram){if(c)out<<',';c=true;out<<'"'<<k<<"\":"<<v;}out<<"}}";
 }
 out<<"]}\n";
 std::cout<<"eligible "<<completed_cases<<"/40 matrices "<<matrices<<" survivors "<<survivors<<" nodes "<<nodes<<" CPU "<<double(clock()-started)/CLOCKS_PER_SEC<<" status "<<(capped?"CPU_CAP":"COMPLETE")<<'\n';
}
