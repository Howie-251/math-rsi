#include <array>
#include <cstdint>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

struct Word {
  int target;
  std::array<int,6> coeff{}; // alpha0,alpha1,alpha2,sigma,tau,half
  std::array<int,3> ports{};
};
int mod26(int n) { n %= 26; return n < 0 ? n+26 : n; }
int step(int c, int p, std::array<int,6>& f) {
  if(p==0) { f[c]++; return c==0?0:3-c; }
  if(p==1) { f[c==0?0:3-c]--; return c==0?0:3-c; }
  if(p==2) return (c+1)%3;
  if(p==3) return (c+2)%3;
  if(p==4) { if(c==2) {f[5]++; return 2;} f[3]+=c==0?1:-1; return 1-c; }
  if(c==1) {f[5]++; return 1;} f[4]+=c==0?1:-1; return 2-c;
}
int neighbor(int v,int p,const std::array<int,6>& pars) {
  int c=v/26,g=v%26; std::array<int,6> f{};
  c=step(c,p,f); for(int i=0;i<6;i++)g+=f[i]*pars[i];
  return 26*c+mod26(g);
}
int main(int argc,char**argv) {
  const double limit=argc>1?std::atof(argv[1]):8.0;
  const std::clock_t started=std::clock();
  const std::array<int,6> inv={1,0,3,2,4,5};
  std::array<std::vector<Word>,3> words;
  std::ofstream pre("WALK_LINEAR_FORMS.tsv");
  pre<<"root_base\tp0\tp1\tp2\ttarget_base\talpha0\talpha1\talpha2\tsigma\ttau\thalf\n";
  for(int c=0;c<3;c++)for(int p=0;p<6;p++)for(int q=0;q<6;q++)for(int r=0;r<6;r++) {
    Word w; w.ports={p,q,r}; int d=c;
    for(int port:w.ports)d=step(d,port,w.coeff);
    w.target=d; words[c].push_back(w); pre<<c<<'\t'<<p<<'\t'<<q<<'\t'<<r<<'\t'<<d;
    for(int v:w.coeff)pre<<'\t'<<v; pre<<'\n';
  }
  pre.close();
  int residue[512];for(int i=0;i<512;i++)residue[i]=mod26(i-208);
  // Fixed alpha0,a1,a2,sigma contributions, then the innermost tau is one lookup.
  std::array<std::array<int,216>,3> base{},pref{};
  const uint32_t full=(1u<<26)-1;
  uint64_t tested=0,raw=0,skipped=0,root_checks=0;
  std::array<uint64_t,2> branch_tested{};
  std::array<int,6> solution{};
  std::array<int,5> last{};
  bool found=false,budget=false;
  for(int a0=1;a0<=2 && !found && !budget;a0++) {
    for(int a1=1;a1<=25 && !found && !budget;a1++)for(int a2=1;a2<=25 && !found && !budget;a2++) {
      if((a1+a2)%26==0) {raw+=625;skipped+=625;continue;}
      for(int c=0;c<3;c++)for(int i=0;i<216;i++) {
        const auto& f=words[c][i].coeff;
        base[c][i]=f[0]*a0+f[1]*a1+f[2]*a2+f[5]*13;
      }
      for(int s=1;s<=25 && !found && !budget;s++) {
        for(int c=0;c<3;c++)for(int i=0;i<216;i++)
          pref[c][i]=mod26(base[c][i]+words[c][i].coeff[3]*s);
        for(int t=1;t<=25;t++) {
          ++raw;++tested;++branch_tested[a0-1];last={a0,a1,a2,s,t};
          bool pass=true;
          for(int c=0;c<3;c++) {
            ++root_checks;uint32_t mask[3]={0,0,0};
            for(int i=0;i<216;i++) {
              const auto& w=words[c][i];
              int g=residue[208+pref[c][i]+w.coeff[4]*t];
              mask[w.target]|=1u<<g;
            }
            if(mask[0]!=full||mask[1]!=full||mask[2]!=full) {pass=false;break;}
          }
          if(pass) {solution={a0,a1,a2,s,t,13};found=true;break;}
          if((tested&255)==0 && double(std::clock()-started)/CLOCKS_PER_SEC>=limit) {budget=true;break;}
        }
      }
    }
  }
  bool actual_ok=true;
  int edges_count=0;
  if(found) {
    std::array<std::array<int,6>,78> table{};
    std::ofstream ports("controller78.porttable.tsv"),edges("controller78.edges"),wit("THREE_PORT_WITNESSES.tsv");
    ports<<"vertex\ta_plus\ta_minus\tb_plus\tb_minus\ts\tt\n";
    for(int v=0;v<78;v++) {
      ports<<v;for(int p=0;p<6;p++){table[v][p]=neighbor(v,p,solution);ports<<'\t'<<table[v][p];}ports<<'\n';
    }
    for(int v=0;v<78;v++) {
      uint64_t lo=0,hi=0;
      for(int p=0;p<6;p++) {
        int u=table[v][p];if(u==v||table[u][inv[p]]!=v)actual_ok=false;
        if(u<64) {if(lo&(uint64_t(1)<<u))actual_ok=false;lo|=uint64_t(1)<<u;}
        else {if(hi&(uint64_t(1)<<(u-64)))actual_ok=false;hi|=uint64_t(1)<<(u-64);}
        if(v<u){edges<<v<<' '<<u<<'\n';edges_count++;}
      }
      if(table[table[table[v][2]][2]][2]!=v)actual_ok=false;
    }
    wit<<"root_base\ttarget_vertex\tp0\tp1\tp2\tv1\tv2\tv3\tnonbacktracking\n";
    for(int c=0;c<3;c++)for(int target=0;target<78;target++) {
      bool got=false;
      for(const auto&w:words[c]) {
        int v=26*c;std::array<int,3> path{};
        for(int k=0;k<3;k++){v=table[v][w.ports[k]];path[k]=v;}
        if(v!=target)continue;
        bool nb=w.ports[1]!=inv[w.ports[0]]&&w.ports[2]!=inv[w.ports[1]];
        bool adjacent=false;for(int p=0;p<6;p++)if(table[26*c][p]==target)adjacent=true;
        if(!adjacent&&!nb)actual_ok=false;
        wit<<c<<'\t'<<target;for(int p:w.ports)wit<<'\t'<<p;for(int u:path)wit<<'\t'<<u;wit<<'\t'<<nb<<'\n';
        // Literal verification of all 26 translates; not a BFS.
        for(int g=0;g<26;g++) {
          int x=26*c+g;for(int p:w.ports)x=table[x][p];
          if(x!=26*(target/26)+(target%26+g)%26)actual_ok=false;
        }
        got=true;break;
      }
      if(!got)actual_ok=false;
    }
    if(edges_count!=234)actual_ok=false;
  }
  double cpu=double(std::clock()-started)/CLOCKS_PER_SEC;
  std::ofstream result("SEARCH_RESULT.json");
  result<<std::setprecision(12)<<"{\n  \"status\": \""<<(found?(actual_ok?"WITNESS_PASS":"ACTUAL_CHECK_FAIL"):(budget?"UNKNOWN_BUDGET":"EXHAUSTED_FIXED_FAMILY"))<<"\",\n  \"tested_simple_candidates\": "<<tested<<",\n  \"raw_prefix_candidates\": "<<raw<<",\n  \"skipped_nonsimple_prefix\": "<<skipped<<",\n  \"branch_tested\": ["<<branch_tested[0]<<", "<<branch_tested[1]<<"],\n  \"root_mask_checks\": "<<root_checks<<",\n  \"last_lex_candidate\": [";
  for(int i=0;i<5;i++){if(i)result<<", ";result<<last[i];}result<<"],\n  \"search_export_cpu_seconds\": "<<cpu<<",\n  \"actual_controller_checks\": "<<(found?(actual_ok?"true":"false"):"null")<<",\n  \"solution_parameters\": ";
  if(found){result<<'[';for(int i=0;i<6;i++){if(i)result<<", ";result<<solution[i];}result<<']';}else result<<"null";
  result<<",\n  \"fiber_graphs_generated\": 0,\n  \"BFS_solver_Lean_runs\": 0\n}\n";
  std::cout<<(found?(actual_ok?"WITNESS_PASS":"ACTUAL_CHECK_FAIL"):(budget?"UNKNOWN_BUDGET":"EXHAUSTED_FIXED_FAMILY"))<<" tested="<<tested<<" branches="<<branch_tested[0]<<','<<branch_tested[1]<<" cpu="<<cpu<<'\n';
  if(found) {std::cout<<"PARAMS";for(int p:solution)std::cout<<' '<<p;std::cout<<'\n';}
  return actual_ok?0:2;
}
