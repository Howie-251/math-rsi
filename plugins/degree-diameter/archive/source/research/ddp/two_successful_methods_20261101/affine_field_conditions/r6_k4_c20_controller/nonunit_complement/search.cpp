#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
struct Word { array<int,3> p; array<int,6> c; };
static const int edgeindex[4][4]={{-1,0,1,2},{0,-1,3,4},{1,3,-1,5},{2,4,5,-1}};
static int mod20(int x) { x%=20;return x<0?x+20:x; }
static int eval(const Word&w,const array<int,6>&g) {
  return mod20(w.c[0]*g[0]+w.c[1]*g[1]+w.c[2]*g[2]+w.c[3]*g[3]+w.c[4]*g[4]+w.c[5]*g[5]);
}
int main(int argc,char**argv) {
  const double limit=stod(argv[1]);const clock_t start=clock();
  vector<Word> words[4][4];ifstream input("../WORD_COEFFICIENTS.tsv");string line;
  getline(input,line);int loaded=0;
  while(getline(input,line)) {istringstream row(line);int i,j;Word w;
    row>>i>>j;for(int&p:w.p)row>>p;for(int&c:w.c)row>>c;if(!row)return 2;
    words[i][j].push_back(w);++loaded;
  }
  if(loaded!=600)return 3;
  const array<int,11> U{2,4,5,6,8,10,12,14,15,16,18};
  const uint32_t full=(1u<<20)-1;array<int,6> g{5,2,2,2,2,2},last=g;
  uint64_t considered=0,tested=0,skipped=0,failures[4][4]={};bool found=false,timed_out=false;
  for(int a:U) {if(found||timed_out)break;for(int b:U) {if(found||timed_out)break;
    for(int c:U) {if(found||timed_out)break;for(int d:U) {if(found||timed_out)break;
      for(int e:U) {
        if((considered&255)==0&&double(clock()-start)/CLOCKS_PER_SEC>=limit) {timed_out=true;break;}
        ++considered;g={5,a,b,c,d,e};last=g;
        if(a%5==0&&b%5==0&&c%5==0&&d%5==0&&e%5==0) {++skipped;continue;}
        ++tested;bool ok=true;
        for(int i=0;i<4&&ok;i++)for(int j=0;j<4&&ok;j++) {
          uint32_t mask=0;for(const Word&w:words[i][j])mask|=1u<<eval(w,g);
          uint32_t required=full;if(i!=j)required&=~(1u|(1u<<mod20((i<j?1:-1)*g[edgeindex[i][j]])));
          if((mask&required)!=required) {++failures[i][j];ok=false;}
        }
        if(ok) {found=true;break;}
      }
    }}
  }}
  if(found) {
    ofstream witnesses("CLASS_WITNESSES.tsv");witnesses<<"root_base\ttarget_base\tresidue\tp1\tp2\tp3\n";
    for(int i=0;i<4;i++)for(int j=0;j<4;j++) {
      uint32_t required=full;if(i!=j)required&=~(1u|(1u<<mod20((i<j?1:-1)*g[edgeindex[i][j]])));
      for(int r=0;r<20;r++)if(required&(1u<<r))for(const Word&w:words[i][j])if(eval(w,g)==r) {
        witnesses<<i<<'\t'<<j<<'\t'<<r;for(int p:w.p)witnesses<<'\t'<<p;witnesses<<'\n';break;
      }
    }
  }
  ofstream out("RAW_RESULT.json");out<<setprecision(12);
  out<<"{\n\"status\":\""<<(found?"PASS":timed_out?"UNKNOWN_BUDGET":"STOP_EXHAUSTED_NONUNIT_COMPLEMENT")<<"\",\n";
  out<<"\"domain_size_including_disconnected\":161051,\n\"connected_domain_size\":160808,\n\"assignments_considered\":"<<considered<<",\n\"connected_assignments_tested\":"<<tested<<",\n\"disconnected_assignments_skipped\":"<<skipped<<",\n\"loaded_word_coefficient_rows\":"<<loaded<<",\n\"last_considered_shifts\":[";
  for(int k=0;k<6;k++)out<<(k?",":"")<<last[k];out<<"],\n\"first_failure_group_counts\":[";
  for(int i=0;i<4;i++)for(int j=0;j<4;j++)out<<((i||j)?",":"")<<failures[i][j];
  out<<"],\n\"search_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\n\"search_CPU_limit_seconds\":"<<limit<<"\n}\n";
  cout<<(found?"PASS":timed_out?"UNKNOWN_BUDGET":"STOP_EXHAUSTED_NONUNIT_COMPLEMENT")<<" considered="<<considered<<" tested="<<tested<<" skipped="<<skipped<<'\n';
}
