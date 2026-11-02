#include <algorithm>
#include <fstream>
#include <iostream>
#include <limits>
#include <string>
#include <vector>
struct Option { int i,e,a,s,c; };
constexpr int NI=37, NE=46, NA=21, NK=6;
constexpr int N=NI*NE*NA*NK, BAD=-1000000;
int index_of(int i,int e,int a,int k) {
  return (((i*NE+e)*NA+a)*NK+k);
}
int main(int argc,char** argv) {
  bool excess=argc>2 && std::string(argv[2])=="excess";
  std::ifstream in(argv[1]);
  std::vector<Option> op;
  Option o;
  while(in>>o.i>>o.e>>o.a>>o.s>>o.c) op.push_back(o);
  std::vector<int> dp(N,BAD),next(N,BAD),parent(17*N,-1);
  dp[0]=0;
  for(int h=1;h<=16;++h) {
    std::fill(next.begin(),next.end(),BAD);
    for(int i=0;i<NI;++i) for(int e=0;e<NE;++e)
      for(int a=0;a<NA;++a) for(int k=0;k<NK;++k) {
        int previous=index_of(i,e,a,k),value=dp[previous];
        if(value==BAD) continue;
        for(int t=0;t<(int)op.size();++t) {
          const auto& p=op[t];
          int ii=i+p.i,ee=e+p.e,aa=a+p.a;
          if(ii>=NI||ee>=NE||aa>=NA) continue;
          int kk=std::min(5,k+(p.s<=5?p.a:0));
          int target=index_of(ii,ee,aa,kk);
          int contribution=p.c+p.s*(11-p.s);
          if(excess) contribution=std::max(0,p.s-6)*(11-p.s)
            -std::max(0,91-p.c-6*(11-p.s));
          int score=value+contribution;
          if(score>next[target]) {
            next[target]=score;
            parent[h*N+target]=t*N+previous;
          }
        }
      }
    dp.swap(next);
  }
  for(int a=15;a<=20;++a) {
    int state=-1,score=BAD;
    for(int k=20-a;k<6;++k) {
      int x=index_of(36,45,a,k);
      if(dp[x]>score) { score=dp[x];state=x; }
    }
    std::cout<<"CASE "<<a<<" "<<score<<"\n";
    if(state<0||score==BAD) continue;
    for(int h=16;h>0;--h) {
      int code=parent[h*N+state];
      if(code<0) return 3;
      int t=code/N;
      std::cout<<t<<(h==1?'\n':' ');
      state=code%N;
    }
  }
}
