#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <string>
#include <vector>

using namespace std;
struct Word { array<int,3> p; array<int,6> c; int target; };
static const int edgeindex[4][4]={{-1,0,1,2},{0,-1,3,4},{1,3,-1,5},{2,4,5,-1}};
static int mod20(int x) { x%=20; return x<0?x+20:x; }
static int eval(const Word& w,const array<int,6>& g) {
  return mod20(w.c[0]*g[0]+w.c[1]*g[1]+w.c[2]*g[2]+w.c[3]*g[3]+w.c[4]*g[4]+w.c[5]*g[5]);
}
static int step(int v,int p,const array<int,6>& g) {
  int i=v/20,z=v%20,k=p%3+1,j=i^k;
  if(p>=3) z=mod20(z+(i<j?1:-1)*g[edgeindex[i][j]]);
  return 20*j+z;
}
int main(int argc,char** argv) {
  const double cpu_limit=stod(argv[1]);
  const clock_t start=clock();
  vector<Word> words[4][4];
  for(int i=0;i<4;i++) for(int a=0;a<6;a++) for(int b=0;b<6;b++) if(b!=a)
    for(int c=0;c<6;c++) if(c!=b) {
      Word w{{a,b,c},{0,0,0,0,0,0},0}; int at=i;
      for(int p:w.p) { int j=at^(p%3+1); if(p>=3) w.c[edgeindex[at][j]]+=(at<j?1:-1); at=j; }
      w.target=at; words[i][at].push_back(w);
    }
  { ofstream f("WORD_COEFFICIENTS.tsv");
    f<<"root_base\ttarget_base\tp1\tp2\tp3\tc01\tc02\tc03\tc12\tc13\tc23\n";
    for(int i=0;i<4;i++) for(int j=0;j<4;j++) for(const Word&w:words[i][j]) {
      f<<i<<'\t'<<j; for(int p:w.p) f<<'\t'<<p; for(int c:w.c) f<<'\t'<<c; f<<'\n';
    }
  }
  uint64_t tried=0, failures[4][4]={}; bool found=false,timed_out=false;
  array<int,6> g{1,1,1,1,1,1},last=g;
  const uint32_t full=(1u<<20)-1;
  for(int a=1;a<=19&&!found&&!timed_out;a++) for(int b=1;b<=19&&!found&&!timed_out;b++)
    for(int c=1;c<=19&&!found&&!timed_out;c++) for(int d=1;d<=19&&!found&&!timed_out;d++)
      for(int e=1;e<=19&&!found&&!timed_out;e++) {
        if((tried&511)==0 && double(clock()-start)/CLOCKS_PER_SEC>=cpu_limit) {timed_out=true;break;}
        g={1,a,b,c,d,e}; last=g; ++tried; bool ok=true;
        for(int i=0;i<4&&ok;i++) for(int j=0;j<4&&ok;j++) {
          uint32_t mask=0; for(const Word& w:words[i][j]) mask|=1u<<eval(w,g);
          uint32_t required=full;
          if(i!=j) {int shift=mod20((i<j?1:-1)*g[edgeindex[i][j]]); required &=~((1u<<0)|(1u<<shift));}
          if((mask&required)!=required) {++failures[i][j];ok=false;}
        }
        found=ok;
      }
  if(found) {
    ofstream edges("controller.edges"), ports("PORT_TABLE.tsv"), witnesses("NB3_WITNESSES.tsv"),
      triangles("TRIANGLES.tsv"), masks("COVERAGE_MASKS.tsv");
    ports<<"vertex\tbase\tdeck\tp0\tp1\tp2\tp3\tp4\tp5\n";
    for(int u=0;u<80;u++) {ports<<u<<'\t'<<u/20<<'\t'<<u%20;
      for(int p=0;p<6;p++) {int v=step(u,p,g);ports<<'\t'<<v;if(u<v)edges<<u<<' '<<v<<'\n';} ports<<'\n';}
    int adj[80][80]={}; for(int u=0;u<80;u++) for(int p=0;p<6;p++) adj[u][step(u,p,g)]=1;
    triangles<<"a\tb\tc\n";
    for(int a=0;a<80;a++)for(int b=a+1;b<80;b++)if(adj[a][b])for(int c=b+1;c<80;c++)if(adj[a][c]&&adj[b][c])triangles<<a<<'\t'<<b<<'\t'<<c<<'\n';
    witnesses<<"source\ttarget\tp1\tp2\tp3\tv1\tv2\tv3\n";
    masks<<"root_base\ttarget_base\tendpoint_mask_decimal\trequired_mask_decimal\trequired_classes\tcovered_required_classes\n";
    for(int i=0;i<4;i++)for(int j=0;j<4;j++) {
      int first[20];for(int&r:first)r=-1;uint32_t mask=0;
      for(int k=0;k<(int)words[i][j].size();k++) {int r=eval(words[i][j][k],g);mask|=1u<<r;if(first[r]<0)first[r]=k;}
      uint32_t required=full;if(i!=j)required&=~(1u|(1u<<mod20((i<j?1:-1)*g[edgeindex[i][j]])));
      masks<<i<<'\t'<<j<<'\t'<<mask<<'\t'<<required<<'\t'<<__builtin_popcount(required)<<'\t'<<__builtin_popcount(mask&required)<<'\n';
      for(int r=0;r<20;r++)if(required&(1u<<r))for(int z=0;z<20;z++) {
        const Word&w=words[i][j][first[r]];int u=20*i+z,v=20*j+mod20(z+r),v1=step(u,w.p[0],g),v2=step(v1,w.p[1],g),v3=step(v2,w.p[2],g);
        if(v3!=v) return 2;
        witnesses<<u<<'\t'<<v;for(int p:w.p)witnesses<<'\t'<<p;witnesses<<'\t'<<v1<<'\t'<<v2<<'\t'<<v3<<'\n';
      }
    }
  }
  ofstream out("SEARCH_RESULT.json");out<<setprecision(12);
  out<<"{\n\"status\":\""<<(found?"PASS":timed_out?"UNKNOWN_BUDGET":"STOP_EXHAUSTED_ANCHORED_FAMILY")<<"\",\n";
  out<<"\"assignments_tried\":"<<tried<<",\n\"domain_size\":2476099,\n\"g_order\":[\"01\",\"02\",\"03\",\"12\",\"13\",\"23\"],\n\"last_tried_shifts\":[";
  for(int k=0;k<6;k++)out<<(k?",":"")<<last[k];out<<"],\n\"first_failure_group_counts\":[";
  for(int i=0;i<4;i++)for(int j=0;j<4;j++)out<<((i||j)?",":"")<<failures[i][j];
  out<<"],\n\"search_and_certificate_CPU_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\n\"search_CPU_limit_seconds\":"<<cpu_limit<<"\n}\n";
  cout<<(found?"PASS":timed_out?"UNKNOWN_BUDGET":"STOP_EXHAUSTED_ANCHORED_FAMILY")<<" tried="<<tried<<" g=";
  for(int v:last)cout<<v<<',';cout<<" CPU="<<double(clock()-start)/CLOCKS_PER_SEC<<'\n';
}
