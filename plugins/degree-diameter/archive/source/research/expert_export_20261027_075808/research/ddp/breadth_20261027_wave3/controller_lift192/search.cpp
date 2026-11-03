#include <bits/stdc++.h>
using namespace std;
struct F {array<int,7> c;};
vector<vector<F>> fs;
int score(const array<int,7>& g) {
 int score=0;
 for(auto& slot:fs){uint32_t seen=0;
  for(auto& w:slot){int x=0,y=0;for(int j=0;j<7;j++){x+=w.c[j]*(g[j]&3);y+=w.c[j]*(g[j]>>2);}seen|=uint32_t(1)<<((x&3)+4*(y&7));}
  score+=32-__builtin_popcount(seen);
 }
 return score;
}
int main(){
 int n;cin>>n;fs.resize(n);for(auto& s:fs){int m;cin>>m;s.resize(m);for(auto& w:s)for(auto& c:w.c)cin>>c;}
 int ns;cin>>ns;vector<array<int,7>> starts(ns);for(auto& g:starts)for(int& x:g)cin>>x;
 mt19937_64 rng(20261027192ULL);const int per_start=25000;const double hard_cpu=445.0;
 clock_t began=clock();array<int,7> best=starts[0];int first=score(best),best_s=first;
 long long proposals=0,evaluated=0,accepted=0;int completed=0,cur_start=-1,cur_proposal=-1;
 vector<int> startscores,best_after_start;bool hit=best_s==0,limit=false;
 for(int s=0;s<ns&&!hit&&!limit;s++){
  auto g=starts[s];int old=s==0?first:score(g);evaluated++;startscores.push_back(old);
  if(old<best_s){best=g;best_s=old;}cur_start=s;
  for(int p=0;p<per_start&&!hit;p++){
   if((p&255)==0 && double(clock()-began)/CLOCKS_PER_SEC>=hard_cpu){limit=true;break;}
   proposals++;cur_proposal=p;int j=rng()%7,oldv=g[j];int v=rng()%31;if(v>=oldv)v++;
   if((j==0||j==2)&&v==0)continue;
   g[j]=v;int val=score(g);evaluated++;
   if(val<best_s){best_s=val;best=g;}
   if(val==0){hit=true;old=val;accepted++;break;}
   double frac=double(p)/per_start,temp=0.35+6.0*pow(1.0-frac,2.0);
   bool take=val<=old || generate_canonical<double,53>(rng)<exp(double(old-val)/temp);
   if(take){old=val;accepted++;}else g[j]=oldv;
  }
  best_after_start.push_back(best_s);if(!limit)completed++;
 }
 cout<<"{\"scope\":\"8 fixed starts times 25000 single-coordinate proposals; original transplantation first\",\"seed\":20261027192,\"first_score\":"<<first<<",\"best_score\":"<<best_s<<",\"best\":[";
 for(int j=0;j<7;j++){if(j)cout<<',';cout<<best[j];}
 cout<<"],\"startscores\":[";for(int i=0;i<(int)startscores.size();i++){if(i)cout<<',';cout<<startscores[i];}
 cout<<"],\"best_after_start\":[";for(int i=0;i<(int)best_after_start.size();i++){if(i)cout<<',';cout<<best_after_start[i];}
 cout<<"],\"proposals\":"<<proposals<<",\"scored_candidates_including_starts\":"<<evaluated<<",\"accepted\":"<<accepted<<",\"completed_starts\":"<<completed<<",\"cursor_start_zero_based\":"<<cur_start<<",\"cursor_proposal_zero_based\":"<<cur_proposal<<",\"CPU_limit_reached\":"<<(limit?"true":"false")<<",\"search_CPU_seconds\":"<<double(clock()-began)/CLOCKS_PER_SEC<<"}\n";
}
