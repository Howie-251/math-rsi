#include "/tmp/n62_sms_install/include/sms/cadical.hpp"
#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
struct Timer:CaDiCaL::Terminator{double deadline;bool terminate()override{return cpu()>=deadline;}};
template<class Emit>void atmost(const vector<int>&xs,int cap,int&next,Emit emit){
 vector<array<int,13>>pref(xs.size());assert(cap==12);
 for(auto&r:pref)for(int&v:r)v=++next;
 for(size_t i=0;i<xs.size();i++){
  emit(vector<int>{-xs[i],pref[i][0]});
  if(i)for(int j=0;j<=cap;j++)emit(vector<int>{-pref[i-1][j],pref[i][j]});
  if(i)for(int j=1;j<=cap;j++)emit(vector<int>{-xs[i],-pref[i-1][j-1],pref[i][j]});
 }
 emit(vector<int>{-pref.back()[cap]});
}
template<class T>vector<T>binary(const string&path,size_t count){
 ifstream f(path,ios::binary|ios::ate);if(!f||f.tellg()!=streampos(count*sizeof(T)))throw runtime_error("size mismatch "+path);
 vector<T>v(count);f.seekg(0);f.read(reinterpret_cast<char*>(v.data()),count*sizeof(T));if(!f)throw runtime_error("short read "+path);return v;
}
string ints(const vector<int>&v){ostringstream o;o<<'[';for(size_t i=0;i<v.size();i++){if(i)o<<',';o<<v[i];}o<<']';return o.str();}
struct Input{int np=0,nf=0;vector<int>pids;vector<vector<vector<int>>>planes;vector<uint64_t>periphery;
 Input(const string&out,const string&data){ifstream f(out+"/planes.txt");f>>np>>nf;assert(f&&np==754&&nf==13857);planes.resize(np);
  for(int j=0;j<np;j++){int pid;f>>pid;pids.push_back(pid);planes[j].resize(91);
   for(auto&r:planes[j]){int n;f>>n;assert(n>0&&n<=nf);r.resize(n);for(int&v:r){f>>v;assert(v>=1&&v<=nf);}assert(f);}}
  periphery=binary<uint64_t>(data+"/PERIPHERY_R4_FREE.u64le.bin",1046*217);
  for(int i=0;i<1046;i++)if(periphery[size_t(i)*217+216]>>33)throw runtime_error("provider padding");
 }
};
void selftest(){
 int cases=0;
 for(int positive:{12,13,0}){CaDiCaL::Solver q;q.set("quiet",1);int next=13;vector<int>xs;for(int i=1;i<=13;i++)xs.push_back(i);
  atmost(xs,12,next,[&](const vector<int>&r){for(int x:r)q.add(x);q.add(0);});
  for(int i=1;i<=13;i++)q.assume(i<=positive?i:-i);
  if(q.solve()!=(positive==13?20:10))throw runtime_error("atmost12 boundary selftest");cases++;
 }
 for(int test=0;test<3;test++){CaDiCaL::Solver q;q.set("quiet",1);
  for(vector<int>r:vector<vector<int>>{{4,5},{-4,1},{-4,2,3},{-5,2},{-5,3}}){for(int x:r)q.add(x);q.add(0);}
  vector<int>a=test==0?vector<int>{1,-2,3}:test==1?vector<int>{-1,2,-3}:vector<int>{-1,2,3};for(int x:a)q.assume(x);
  if(q.solve()!=(test==1?20:10))throw runtime_error("small conditional plane selftest");cases++;
 }
 cout<<"ENCODING_CONTROL_PASS cases="<<cases<<" mathematical_solver_calls=0"<<endl;
}
void prepare(const string&out,const string&data){
 double start=cpu();Input in(out,data);int variables=in.nf+in.np;long long clauses=0,literals=0;
 fstream f(out+"/model.cnf",ios::out|ios::trunc);f<<"p cnf "<<setw(10)<<0<<' '<<setw(10)<<0<<'\n';
 auto emit=[&](const vector<int>&r){for(int v:r){f<<v<<' ';literals++;}f<<"0\n";clauses++;};
 vector<int>selectors,open;for(int i=1;i<=in.nf;i++)selectors.push_back(i);for(int i=0;i<in.np;i++)open.push_back(in.nf+i+1);
 emit(open);atmost(selectors,12,variables,emit);
 for(int p=0;p<in.np;p++)for(auto&r:in.planes[p]){vector<int>c{-in.nf-p-1};c.insert(c.end(),r.begin(),r.end());emit(c);}
 for(int t=0;t<1046;t++){vector<int>r;for(int w=0;w<217;w++){uint64_t bits=in.periphery[size_t(t)*217+w];while(bits){int v=64*w+__builtin_ctzll(bits)+1;assert(v<=in.nf);r.push_back(v);bits&=bits-1;}}assert(!r.empty());emit(r);}
 f.seekp(0);f<<"p cnf "<<setw(10)<<variables<<' '<<setw(10)<<clauses<<'\n';f.close();
 ofstream(out+"/MODEL.json")<<"{\"status\":\"PREPARED_NOT_SOLVED\",\"variables\":"<<variables<<",\"selectors\":"<<in.nf<<",\"planes\":"<<in.np<<",\"clauses\":"<<clauses<<",\"literals\":"<<literals<<",\"cardinality_cap\":12,\"conditional_plane_line_clauses\":"<<91*in.np<<",\"periphery_clauses\":1046,\"solve_entered\":false,\"SAT_models\":0,\"fullchecks\":0,\"prep_native_CPU\":"<<cpu()-start<<"}\n";
 cout<<"MODEL_READY variables="<<variables<<" actual_clauses="<<clauses<<" solve_entered=0 SAT_models=0 fullchecks=0 CPU="<<cpu()-start<<endl;
}
void solve(const string&out,const string&data,double limit){
 double start=cpu();CaDiCaL::Solver s;s.set("quiet",1);ifstream f(out+"/model.cnf");string p,cnf;int variables;long long expected;f>>p>>cnf>>variables>>expected;if(p!="p"||cnf!="cnf")throw runtime_error("CNF header");
 int lit;long long clauses=0,literals=0;while(f>>lit){s.add(lit);if(lit)literals++;else clauses++;}if(clauses!=expected)throw runtime_error("actual CNF clause count");
 Timer timer;timer.deadline=cpu()+limit;s.connect_terminator(&timer);
 ofstream(out+"/SOLVE_PROGRESS.json")<<"{\"status\":\"SOLVING\",\"solve_entered\":true,\"actual_clauses\":"<<clauses<<",\"SAT_models\":0,\"fullchecks\":0,\"solver_CPU_limit\":"<<limit<<"}\n";
 cout<<"SOLVE_ENTERED actual_clauses="<<clauses<<" actual_literals="<<literals<<" solver_CPU_limit="<<limit<<endl;
 double before=cpu();int code=s.solve();double used=cpu()-before;vector<int>indices,pins,planes;string status=code==10?"SAT_PROVIDER_VERIFICATION_PENDING":code==20?"RAW_UNSAT_UNCERTIFIED_SUFFICIENT_PLANE_FAMILY":"UNKNOWN_LIMIT";
 if(code==10){auto free=binary<uint32_t>(data+"/FREE_IDS.u32le.bin",13857);ifstream pf(out+"/planes.txt");int np,nf;pf>>np>>nf;
  for(int i=1;i<=nf;i++)if(s.val(i)>0){indices.push_back(i-1);pins.push_back(free[i-1]);}assert(pins.size()<=12);
  for(int j=0;j<np;j++){int pid;pf>>pid;if(s.val(nf+j+1)>0)planes.push_back(pid);for(int k=0;k<91;k++){int n,v;pf>>n;while(n--)pf>>v;}}
  assert(!planes.empty());ofstream(out+"/CANDIDATE.json")<<"{\"source_n\":42402,\"selected_indices\":"<<ints(indices)<<",\"pins\":"<<ints(pins)<<",\"open_plane_ids\":"<<ints(planes)<<",\"status\":\"SAT_NOT_YET_ORIGINAL_PROVIDER_OR_BFS_CHECKED\"}\n";
 }
 ofstream(out+"/NATIVE_RESULT.json")<<"{\"status\":\""<<status<<"\",\"running\":false,\"solve_entered\":true,\"solver_calls\":1,\"solver_return_code\":"<<code<<",\"actual_clauses\":"<<clauses<<",\"SAT_models\":"<<(code==10?1:0)<<",\"fullchecks\":0,\"solver_CPU\":"<<used<<",\"native_CPU\":"<<cpu()-start<<",\"proof_checked\":false}\n";
 cout<<"FINAL "<<status<<" SAT_models="<<(code==10)<<" fullchecks=0 solver_CPU="<<used<<endl;
}
int main(int argc,char**argv){try{if(argc==2&&string(argv[1])=="--selftest"){selftest();return 0;}
 if(argc<4)return 2;string mode=argv[1],out=argv[2],data=argv[3];if(mode=="--prepare"){prepare(out,data);return 0;}if(mode=="--solve"&&argc==5){solve(out,data,stod(argv[4]));return 0;}return 2;
 }catch(const exception&e){cerr<<"ERROR "<<e.what()<<endl;return 1;}}
