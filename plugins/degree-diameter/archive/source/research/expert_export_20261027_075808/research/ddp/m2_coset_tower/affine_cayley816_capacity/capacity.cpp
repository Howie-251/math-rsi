#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
using U=uint64_t;
constexpr int Q=17,M=48,R=3,H=M/2;
static_assert(12*5<=64,"All component coefficients fit uint64_t");
int pw[M];
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
template<class T>void list(ostream&o,const T&v){o<<'[';bool comma=false;for(auto x:v){if(comma)o<<',';comma=true;o<<x;}o<<']';}
U projective(int variables){U power=1,sum=0;for(int i=0;i<variables-1;i++){sum+=power;power*=Q;}return sum;}
U choose(int n,int k){U result=1;for(int i=1;i<=k;i++)result=result*(n-k+i)/i;return result;}
struct Letter{int phase,coefficient,variable,inverse;};
vector<Letter> alphabet(int d,const vector<int>&phase){
 vector<Letter> letters;int p=phase.size(),involutions=d-2*p;
 for(int i=0;i<p;i++){int j=phase[i],at=letters.size();letters.push_back({j,1,i,at+1});letters.push_back({(M-j)%M,(Q-pw[(M-j)%M])%Q,i,at});}
 for(int i=0;i<involutions;i++){int at=letters.size();letters.push_back({H,1,p+i,at});}
 assert(d<=12&&p<=6&&d-p<=12);assert(int(letters.size())==d);return letters;
}
array<int,M> plain(int d,const vector<Letter>&letters){
 array<int,M>a{},a2{},a3{},result{};for(auto s:letters)a[s.phase]++;
 vector<int>support;for(int j=0;j<M;j++)if(a[j])support.push_back(j);
 for(int j:support)for(int k:support)a2[(j+k)%M]+=a[j]*a[k];
 for(int j=0;j<M;j++)if(a2[j])for(int k:support)a3[(j+k)%M]+=a2[j]*a[k];
 for(int j=0;j<M;j++){result[j]=a3[j]+a2[j]+(2-2*d)*a[j]+(j==0?1-d:0);assert(result[j]>=0);}
 assert(accumulate(result.begin(),result.end(),0)==1+d+d*(d-1)+d*(d-1)*(d-1));return result;
}
struct Symbolic{array<vector<U>,M> forms;array<int,M>raw{},counts{};};
struct Node{int phase,last;U coeff;};
Symbolic symbolic(const vector<Letter>&letters){
 Symbolic result;vector<Node>level{{0,-1,0}},next;result.forms[0].push_back(0);result.raw[0]=1;
 int d=letters.size(),new_phase[M][12],add[M][12];
 for(int j=0;j<M;j++)for(int k=0;k<d;k++){new_phase[j][k]=(j+letters[k].phase)%M;add[j][k]=pw[j]*letters[k].coefficient%Q;}
 for(int length=1;length<=3;length++){
  next.clear();next.reserve(level.size()*d);
  for(auto node:level)for(int k=0;k<d;k++){
   if(node.last>=0&&k==letters[node.last].inverse)continue;
   int shift=5*letters[k].variable,old=(node.coeff>>shift)&31;
   U coeff=(node.coeff&~(U(31)<<shift))|(U((old+add[node.phase][k])%Q)<<shift);
   int phase=new_phase[node.phase][k];result.forms[phase].push_back(coeff);result.raw[phase]++;next.push_back({phase,k,coeff});
  }
  level.swap(next);
 }
 for(int j=0;j<M;j++){auto&v=result.forms[j];sort(v.begin(),v.end());v.erase(unique(v.begin(),v.end()),v.end());result.counts[j]=v.size();}
 return result;
}
struct Branch{int degree,pairs,involutions,variables;U expected=0,completed=0,rawpass=0,sympass=0,rawmarked=0,symmarked=0;int maximum_min_symbolic=-1;};
void branchout(ostream&o,const Branch&b){o<<"{\"degree\":"<<b.degree<<",\"pairs\":"<<b.pairs<<",\"involutions\":"<<b.involutions<<",\"variables\":"<<b.variables<<",\"patterns_expected\":"<<b.expected<<",\"patterns_completed\":"<<b.completed<<",\"plain_pass\":"<<b.rawpass<<",\"symbolic_pass\":"<<b.sympass<<",\"projective_marked_inputs_per_pattern\":"<<projective(b.variables)<<",\"plain_projective_marked_inputs\":"<<b.rawmarked<<",\"symbolic_projective_marked_inputs\":"<<b.symmarked<<",\"maximum_minimum_symbolic_capacity\":";if(b.maximum_min_symbolic<0)o<<"null";else o<<b.maximum_min_symbolic;o<<'}';}
void rowhead(ostream&o,U cursor,int d,const vector<int>&phase){o<<"{\"cursor\":"<<cursor<<",\"degree\":"<<d<<",\"pair_count\":"<<phase.size()<<",\"involution_count\":"<<d-2*phase.size()<<",\"pair_phases\":";list(o,phase);}
int main(int argc,char**argv){
 assert(argc==4);string mode=argv[1],base=argv[2];double limit=stod(argv[3]),start=cpu();pw[0]=1;for(int j=1;j<M;j++)pw[j]=R*pw[j-1]%Q;
 assert(pw[16]==1&&pw[8]==16&&pw[24]==16&&pw[47]*R%Q==1);
 if(mode=="calibrate"){
  vector<pair<int,vector<int>>>cases{{12,{}},{12,{0,1,7,16,16,23}}};ofstream out(base+"/calibration.cpp.json");out<<'[';
  for(int ci=0;ci<int(cases.size());ci++){if(ci)out<<',';auto[d,phase]=cases[ci];auto letters=alphabet(d,phase);auto raw=plain(d,letters);auto s=symbolic(letters);assert(raw==s.raw);rowhead(out,ci,d,phase);out<<",\"raw_capacity\":";list(out,raw);out<<",\"form_counts\":";list(out,s.counts);out<<",\"packed_forms\":[";for(int j=0;j<M;j++){if(j)out<<',';list(out,s.forms[j]);}out<<"]}";}
  out<<"]\n";cout<<"CALIBRATION_SYMBOLIC_OUTPUT_COMPLETE CPU="<<cpu()-start<<endl;return 0;
 }
 assert(mode=="run");vector<Branch>branches;U cursor=0,rawpass=0,sympass=0;bool timeout=false;
 int next_degree=12,next_pairs=0;vector<int>next_phases;double plain_cpu=0,symbolic_cpu=0;
 ofstream rows(base+"/patterns.jsonl"),survivors(base+"/survivors.jsonl");
 for(int d:{12})for(int p=0;p<=d/2;p++){
  Branch b{d,p,d-2*p,d-p};b.expected=choose(p+H-1,p);branches.push_back(b);auto&current=branches.back();vector<int>phase;
  function<void(int)>visit=[&](int low){
   if(timeout)return;
   if(int(phase.size())<p){for(int j=low;j<H&&!timeout;j++){phase.push_back(j);visit(j);phase.pop_back();}return;}
   next_degree=d;next_pairs=p;next_phases=phase;
   if(cpu()-start>=limit){timeout=true;return;}
   auto letters=alphabet(d,phase);double timer=cpu();auto capacity=plain(d,letters);plain_cpu+=cpu()-timer;
   bool raw_ok=*min_element(capacity.begin(),capacity.end())>=Q;
   rowhead(rows,cursor,d,phase);rows<<",\"plain_capacity\":";list(rows,capacity);rows<<",\"plain_pass\":"<<(raw_ok?"true":"false");
   if(raw_ok){
    rawpass++;current.rawpass++;U marked=projective(d-p);current.rawmarked+=marked;
    timer=cpu();auto s=symbolic(letters);symbolic_cpu+=cpu()-timer;assert(s.raw==capacity);
    int tight=*min_element(s.counts.begin(),s.counts.end()),critical=min_element(s.counts.begin(),s.counts.end())-s.counts.begin();
    current.maximum_min_symbolic=max(current.maximum_min_symbolic,tight);bool symbolic_ok=tight>=Q;
    int anchor=0;while(anchor<p&&pw[phase[anchor]]==1)anchor++;assert(anchor<p||d-2*p>0);
    rows<<",\"symbolic_capacity\":";list(rows,s.counts);rows<<",\"symbolic_pass\":"<<(symbolic_ok?"true":"false")<<",\"minimum_symbolic_capacity\":"<<tight<<",\"field_variables\":"<<d-p<<",\"anchor_component\":"<<anchor<<",\"projective_marked_inputs\":"<<marked<<",\"witness_phase\":"<<critical<<",\"witness_packed_forms\":";list(rows,s.forms[critical]);
    if(symbolic_ok){
     sympass++;current.sympass++;current.symmarked+=marked;rowhead(survivors,cursor,d,phase);survivors<<",\"field_variables\":"<<d-p<<",\"anchor_component\":"<<anchor<<",\"projective_marked_inputs\":"<<marked<<",\"symbolic_capacity\":";list(survivors,s.counts);survivors<<",\"minimum_symbolic_capacity\":"<<tight<<",\"tightest_phases\":[";bool comma=false;for(int j=0;j<M;j++)if(s.counts[j]==tight){if(comma)survivors<<',';comma=true;survivors<<j;}survivors<<"]}\n";
    }
   }
   rows<<"}\n";cursor++;current.completed++;
   if(cursor==1000||cursor%10000==0)cout<<"PROGRESS cursor="<<cursor<<" CPU="<<cpu()-start<<" plainpass="<<rawpass<<" symbolicpass="<<sympass<<endl;
  };visit(0);
  cout<<"BRANCH degree="<<d<<" pairs="<<p<<" checked="<<current.completed<<'/'<<current.expected<<" plainpass="<<current.rawpass<<" symbolicpass="<<current.sympass<<" CPU="<<cpu()-start<<endl;
  if(timeout)goto done;
  assert(current.completed==current.expected);
 }
done:
 rows.close();survivors.close();string status=timeout?"CPU_LIMIT_INCOMPLETE":"COMPLETE_CAPACITY_ONLY";if(!timeout)assert(cursor==593775);
 ofstream terminal(base+"/capacity.terminal.json");terminal<<setprecision(12)<<"{\"status\":\""<<status<<"\",\"total_phase_patterns\":593775,\"completed_phase_patterns\":"<<cursor<<",\"plain_pass\":"<<rawpass<<",\"symbolic_pass\":"<<sympass<<",\"next_cursor\":"<<cursor<<",\"next_pattern\":";
 if(timeout){terminal<<"{\"degree\":"<<next_degree<<",\"pairs\":"<<next_pairs<<",\"pair_phases\":";list(terminal,next_phases);terminal<<'}';}else terminal<<"null";
 terminal<<",\"CPU_seconds\":"<<cpu()-start<<",\"plain_CPU_seconds\":"<<plain_cpu<<",\"symbolic_CPU_seconds\":"<<symbolic_cpu<<",\"branches\":[";for(int i=0;i<int(branches.size());i++){if(i)terminal<<',';branchout(terminal,branches[i]);}terminal<<"],\"field_assignments_tested\":0,\"graphs_generated\":0,\"BFS_runs\":0,\"running\":false}\n";
 cout<<status<<" cursor="<<cursor<<" CPU="<<cpu()-start<<" plainpass="<<rawpass<<" symbolicpass="<<sympass<<endl;
}
