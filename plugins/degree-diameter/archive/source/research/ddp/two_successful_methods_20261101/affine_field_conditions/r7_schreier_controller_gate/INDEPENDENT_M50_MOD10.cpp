#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using V=array<int,6>;using F=array<int,7>;
vector<V>read(const string&name){ifstream in(name);if(!in)throw runtime_error("missing inherited passing profiles");string line;getline(in,line);vector<V>rows;while(getline(in,line)){istringstream s(line);V v;for(int&x:v)s>>x;rows.push_back(v);}return rows;}
template<size_t N>void emit(ostream&out,const array<int,N>&x){out<<'[';for(size_t i=0;i<N;i++){if(i)out<<',';out<<x[i];}out<<']';}
int main(){try{
 double start=double(clock())/CLOCKS_PER_SEC;auto mod2=read("M50_MOD2_PASS_PROFILES.tsv"),mod5=read("M50_MOD5_PASS_PROFILES.tsv");
 if(mod2.size()!=16||mod5.size()!=1136)throw runtime_error("unexpected inherited profile counts");
 ifstream input("DISTINCT_FORMS.tsv");string line;getline(input,line);vector<F>forms;
 while(getline(input,line)){istringstream s(line);int root,target;s>>root>>target;F f;for(int&x:f)s>>x;if(root==0&&target==0)forms.push_back(f);}
 if(forms.size()!=50)throw runtime_error("expected50 saved source00 forms");
 set<F>formset(forms.begin(),forms.end());int fixed=0;for(auto f:forms){F minus=f;for(int j=0;j<6;j++)minus[j]=-minus[j];if(!formset.count(minus))throw runtime_error("negation-pair invariant");if(f==minus)fixed++;}
 if(fixed!=2)throw runtime_error("expectedonly0/half fixed forms");
 ofstream out("INDEPENDENT_M50_MOD10_PASS_PROFILES.tsv");out<<"normalized_alpha0\talpha0_mod10\talpha1\talpha2\tsigma\ttau\trho\n";
 array<int,2>tested{},passed{};V firstpass{},firstreject{};array<int,10>firstrejectcounts{};bool havepass=false,havereject=false;
 for(auto v5:mod5){if(v5[0]!=0&&v5[0]!=2)continue;int branch=v5[0]==2?0:1;
  for(auto v2:mod2){V v;for(int j=0;j<6;j++){int flip=(v2[j]-(v5[j]%2)+2)%2;v[j]=v5[j]+5*flip;}tested[branch]++;
   array<int,10>counts{};for(auto f:forms){int val=5*f[6];for(int j=0;j<6;j++)val+=f[j]*v[j];val%=10;if(val<0)val+=10;counts[val]++;}
   bool ok=true;for(int n:counts)ok&=n==5;
   if(ok){passed[branch]++;if(!havepass){firstpass=v;havepass=true;}out<<(branch==0?2:10);for(int x:v)out<<'\t'<<x;out<<'\n';}
   else if(!havereject){firstreject=v;firstrejectcounts=counts;havereject=true;}
  }
 }
 if(tested!=array<int,2>{4352,768})throw runtime_error("expected5120 normalized CRT combinations");
 cout<<"{\"status\":\"COMPLETE_NEW_MOD10_CHARACTER_NECESSARY_GATE\",\"saved_source00_forms\":50,\"inherited_parity_profiles\":16,\"inherited_mod5_profiles\":1136,\"marginal_profiles_reenumerated\":false,\"normalized_alpha0_branches\":[2,10],\"tested_per_branch\":";emit(cout,tested);cout<<",\"passing_per_branch\":";emit(cout,passed);cout<<",\"total_tested\":5120,\"total_passing\":"<<passed[0]+passed[1]<<",\"first_passing_mod10_profile\":";if(havepass)emit(cout,firstpass);else cout<<"null";cout<<",\"first_marginal_passing_joint_rejection\":";if(havereject){cout<<"{\"profile_mod10\":";emit(cout,firstreject);cout<<",\"counts_mod10\":";emit(cout,firstrejectcounts);cout<<'}';}else cout<<"null";cout<<",\"negation_fixed_forms\":2,\"first_and_odd_moment_condition\":\"automatic_from_negation_and0_half\",\"full_Z50_parameter_or_controller_search\":false,\"graphs_BFS_Lean_or_other_m\":0,\"CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-start<<"}\n";return 0;
 }catch(const exception&e){cerr<<e.what()<<'\n';return 2;}}
