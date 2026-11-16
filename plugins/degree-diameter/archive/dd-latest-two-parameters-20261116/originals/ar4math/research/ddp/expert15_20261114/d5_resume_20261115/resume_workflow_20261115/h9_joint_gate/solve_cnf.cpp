#include "/tmp/n62_sms_install/include/sms/cadical.hpp"
#include <ctime>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
using namespace std;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
struct Timer:CaDiCaL::Terminator{double end;bool terminate()override{return cpu()>=end;}};
int main(int argc,char**argv){try{
 if(argc!=4)return 2;
 string model=argv[1],out=argv[2];double start=cpu(),limit=stod(argv[3]);
 CaDiCaL::Solver s;s.set("quiet",1);Timer timer;timer.end=start+limit;s.connect_terminator(&timer);
 ifstream f(model);string p,cnf;int variables;long long expected;
 f>>p>>cnf>>variables>>expected;if(p!="p"||cnf!="cnf")throw runtime_error("bad DIMACS header");
 int lit;long long clauses=0;while(f>>lit){s.add(lit);if(!lit)clauses++;}
 if(clauses!=expected)throw runtime_error("clause count mismatch");
 ofstream(out+"/SOLVE_PROGRESS.json")<<"{\"status\":\"SOLVING\",\"solver_calls\":1,\"SAT_models\":0,\"running\":true}\n";
 double before=cpu();int code=s.solve();double solver_cpu=cpu()-before;
 if(code==10){ofstream vals(out+"/ASSIGNMENT.txt");for(int i=1;i<=variables;i++)vals<<(s.val(i)>0?i:-i)<<' ';vals<<"0\n";}
 string status=code==10?"SAT_PENDING_DIRECT_CHECK":code==20?"RAW_UNSAT_UNCHECKED":"UNKNOWN_LIMIT";
 ofstream(out+"/NATIVE_RESULT.json")<<"{\"status\":\""<<status<<"\",\"running\":false,\"solver_calls\":1,\"solver_return_code\":"<<code<<",\"SAT_models\":"<<(code==10)<<",\"fully_checked_assignments\":0,\"variables\":"<<variables<<",\"clauses\":"<<clauses<<",\"solver_CPU\":"<<solver_cpu<<",\"native_CPU\":"<<cpu()-start<<",\"proof_checked\":false}\n";
 cout<<status<<" code="<<code<<" solver_CPU="<<solver_cpu<<endl;return 0;
 }catch(const exception&e){cerr<<e.what()<<endl;return 1;}}
