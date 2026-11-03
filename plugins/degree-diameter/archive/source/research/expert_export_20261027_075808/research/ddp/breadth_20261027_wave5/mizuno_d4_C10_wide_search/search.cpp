#include <bits/stdc++.h>
using namespace std;
using V=array<int,9>;
vector<vector<V>> slots;
int score(const V& g, vector<int>* saved=nullptr){
 int miss=0;if(saved)saved->clear();
 for(auto& slot:slots){int mask=0;for(auto& f:slot){int v=0;for(int j=0;j<9;j++)v+=f[j]*g[j];mask|=1<<(v%10);}miss+=10-__builtin_popcount((unsigned)mask);if(saved)saved->push_back(mask);}
 return miss;
}
int main(){
 clock_t began=clock();int ns;cin>>ns;slots.resize(ns);for(auto& s:slots){int n;cin>>n;s.resize(n);for(auto& f:s)for(int& c:f)cin>>c;}
 int starts_count;cin>>starts_count;vector<V> starts(starts_count);for(auto& g:starts)for(int& c:g)cin>>c;
 mt19937_64 rng(20261027510ULL);int first=score(starts[0]);assert(first==44);V best=starts[0];int best_s=first;
 long long proposals=0,scored=0,accepted=0;int completed=0,cur_start=-1,cur_proposal=-1;bool hit=first==0,limited=false;vector<int> initial_scores,best_after;
 for(int s=0;s<starts_count&&!hit&&!limited;s++){
  V g=starts[s];int old=s==0?first:score(g);scored++;initial_scores.push_back(old);cur_start=s;
  if(old<best_s){best_s=old;best=g;}
  for(int p=0;p<25000&&!hit;p++){
   if((p&255)==0 && double(clock()-began)/CLOCKS_PER_SEC>=54.0){limited=true;break;}
   proposals++;cur_proposal=p;int j=rng()%9,oldv=g[j],offset=j<2?1:0,domain=j<2?9:10;
   int candidate=rng()%(domain-1);if(candidate>=oldv-offset)candidate++;g[j]=candidate+offset;
   int val=score(g);scored++;
   if(val<best_s){best_s=val;best=g;}
   if(val==0){hit=true;old=val;accepted++;break;}
   double frac=double(p)/25000,temp=0.15+2.5*(1-frac)*(1-frac);
   bool take=val<=old || generate_canonical<double,53>(rng)<exp(double(old-val)/temp);
   if(take){old=val;accepted++;}else g[j]=oldv;
  }
  best_after.push_back(best_s);if(!limited)completed++;
 }
 vector<int> masks;assert(score(best,&masks)==best_s);
 cout<<"{\"status\":\""<<(hit?"HIT_WIDE_CERTIFICATE":limited?"CPU_LIMIT_INCOMPLETE":"EIGHT_FIXED_STARTS_COMPLETE_NO_HIT")<<"\",\"first_score\":"<<first<<",\"best_score\":"<<best_s<<",\"best\":[";
 for(int i=0;i<9;i++){if(i)cout<<',';cout<<best[i];}cout<<"],\"initial_scores\":[";
 for(int i=0;i<(int)initial_scores.size();i++){if(i)cout<<',';cout<<initial_scores[i];}cout<<"],\"best_after_starts\":[";
 for(int i=0;i<(int)best_after.size();i++){if(i)cout<<',';cout<<best_after[i];}cout<<"],\"best_masks\":[";
 for(int i=0;i<(int)masks.size();i++){if(i)cout<<',';cout<<masks[i];}
 cout<<"],\"proposals\":"<<proposals<<",\"scored_candidates_including_starts\":"<<scored<<",\"accepted\":"<<accepted<<",\"completed_starts\":"<<completed<<",\"cursor_start_zero_based\":"<<cur_start<<",\"cursor_proposal_zero_based\":"<<cur_proposal<<",\"CPU_limit_reached\":"<<(limited?"true":"false")<<",\"search_CPU_seconds\":"<<double(clock()-began)/CLOCKS_PER_SEC<<"}\n";
}
