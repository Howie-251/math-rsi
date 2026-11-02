#include <algorithm>
#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <stdexcept>
#include <string>
#include <vector>
#include "controller_input.h"
using namespace std;
using Bits=unsigned __int128;
array<Bits,78> neighborhoods{},compatible{};
vector<int>best,current,cutoff_path,cutoff_candidates;
unsigned long long nodes=0,colorings=0,pruned=0;
bool hit12=false,timed_out=false;
double deadline=0,start_cpu=0;
int root_color_upper=0;
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
int popcount(Bits b){return __builtin_popcountll((unsigned long long)b)+__builtin_popcountll((unsigned long long)(b>>64));}
int firstbit(Bits b){unsigned long long low=(unsigned long long)b;if(low)return __builtin_ctzll(low);return 64+__builtin_ctzll((unsigned long long)(b>>64));}
vector<int>vertices(Bits b){vector<int>v;while(b){int x=firstbit(b);b&=~(Bits(1)<<x);v.push_back(x);}return v;}
void emit_array(ostream&out,const vector<int>&v){out<<'[';for(size_t i=0;i<v.size();i++){if(i)out<<',';out<<v[i];}out<<']';}
void checkpoint(){
 ofstream out("BEST_PREFIX.json");out<<"{\"status\":\"SEARCH_PREFIX_WITNESS\",\"best_size\":"<<best.size()<<",\"best_U\":";emit_array(out,best);out<<",\"nodes\":"<<nodes<<",\"paper_upper_bound\":12,\"search_CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-start_cpu<<"}\n";
}
void update_best(){if(current.size()>best.size()){best=current;sort(best.begin(),best.end());checkpoint();if(best.size()==12)hit12=true;}}
void color_sort(Bits P,vector<int>&order,vector<int>&bounds){
 colorings++;int color=0;
 while(P){color++;Bits free=P;
  while(free){
   int v=firstbit(free);Bits bit=Bits(1)<<v;order.push_back(v);bounds.push_back(color);
   P&=~bit;free&=~bit;free&=~compatible[v];
  }
 }
}
void expand(Bits P){
 if(hit12||timed_out)return;
 nodes++;
 if((nodes&1023)==0&&double(clock())/CLOCKS_PER_SEC-start_cpu>deadline){timed_out=true;cutoff_path=current;cutoff_candidates=vertices(P);checkpoint();return;}
 if(current.size()+popcount(P)<=best.size()){pruned++;return;}
 vector<int>order,bounds;color_sort(P,order,bounds);
 if(current.empty())root_color_upper=bounds.empty()?0:bounds.back();
 for(int i=int(order.size())-1;i>=0;i--){
  if(hit12||timed_out)return;
  if(current.size()+bounds[i]<=best.size()){pruned++;return;}
  int v=order[i];Bits bit=Bits(1)<<v;current.push_back(v);
  Bits next=P&compatible[v];
  update_best();
  if(next&&!hit12)expand(next);
  current.pop_back();P&=~bit;
 }
}
int mod26(int g){return (g%26+26)%26;}
int label(int c,int g){return 26*c+mod26(g);}
int main(int argc,char**argv){try{
 need(argc==2,"CPU deadline argument");deadline=stod(argv[1]);start_cpu=double(clock())/CLOCKS_PER_SEC;
 for(int c=0;c<3;c++)for(int g=0;g<26;g++){
  int u=label(c,g);array<int,6>r;
  r[0]=c==0?label(0,g+2):c==1?label(2,g+6):label(1,g+17);
  r[1]=c==0?label(0,g-2):c==1?label(2,g-17):label(1,g-6);
  r[2]=label((c+1)%3,g);r[3]=label((c+2)%3,g);
  r[4]=c==0?label(1,g+5):c==1?label(0,g-5):label(2,g+13);
  r[5]=c==0?label(2,g+10):c==1?label(1,g+13):label(0,g-10);
  for(int p=0;p<6;p++){need(r[p]==literal_controller[u][p],"literal vs explicit controller rule");neighborhoods[u]|=Bits(1)<<r[p];}
  need(popcount(neighborhoods[u])==6&&!(neighborhoods[u]&(Bits(1)<<u)),"simple6neighbor input");
 }
 for(int u=0;u<78;u++)for(int v=0;v<78;v++){
  need(bool(neighborhoods[u]&(Bits(1)<<v))==bool(neighborhoods[v]&(Bits(1)<<u)),"symmetric input");
  if(u!=v&&!(neighborhoods[u]&neighborhoods[v]))compatible[u]|=Bits(1)<<v;
 }
 best={0,1,7,9,15,18,24};for(int u:best)for(int v:best)if(u!=v)need(bool(compatible[u]&(Bits(1)<<v)),"givenLB7 valid");checkpoint();
 Bits all=(Bits(1)<<78)-1;expand(all);checkpoint();
 Bits covered=0;ofstream pairs("PAIR_INTERSECTION_CERTIFICATE.tsv");pairs<<"u\tv\tcommon_open_neighbors\n";
 for(size_t i=0;i<best.size();i++){
  need(!(covered&neighborhoods[best[i]]),"final disjoint target certificate");covered|=neighborhoods[best[i]];
  for(size_t j=0;j<i;j++){int n=popcount(neighborhoods[best[i]]&neighborhoods[best[j]]);need(n==0,"final pair disjoint");pairs<<best[j]<<'\t'<<best[i]<<'\t'<<n<<'\n';}
 }
 ofstream nfile("SELECTED_OPEN_NEIGHBORHOODS.tsv");nfile<<"selected\tneighbor1\tneighbor2\tneighbor3\tneighbor4\tneighbor5\tneighbor6\n";for(int u:best){nfile<<u;for(int p=0;p<6;p++)nfile<<'\t'<<literal_controller[u][p];nfile<<'\n';}
 string status=hit12?"OPTIMUM12_PAPER_UPPER_MATCHED":timed_out?"UNKNOWN_TIME_LIMIT_WITH_WITNESS":"TRUE_OPTIMUM_COMPLETE_TREE";
 ofstream out("SEARCH_RESULT.json");out<<"{\"status\":\""<<status<<"\",\"best_size\":"<<best.size()<<",\"best_U\":";emit_array(out,best);out<<",\"lower_bound\":"<<best.size()<<",\"upper_bound\":"<<(timed_out?12:int(best.size()))<<",\"paper_upper_bound\":12,\"whole_tree_exhausted\":"<<(!hit12&&!timed_out?"true":"false")<<",\"stopped_at_attained_paper_bound\":"<<(hit12?"true":"false")<<",\"timed_out\":"<<(timed_out?"true":"false")<<",\"nodes\":"<<nodes<<",\"greedy_coloring_calls\":"<<colorings<<",\"color_or_cardinality_prunes\":"<<pruned<<",\"initial_root_color_bound\":"<<root_color_upper<<",\"distinct_covered_targets\":"<<popcount(covered)<<",\"covered_targets\":";emit_array(out,vertices(covered));out<<",\"uncovered_targets\":";emit_array(out,vertices(all&~covered));out<<",\"cutoff_path\":";emit_array(out,cutoff_path);out<<",\"cutoff_pending_candidates\":";emit_array(out,cutoff_candidates);out<<",\"search_CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-start_cpu<<",\"large_graphs_BFS_Lean_or_other_controllers\":0}\n";
 out.close();cout<<status<<" best="<<best.size()<<" nodes="<<nodes<<" CPU="<<double(clock())/CLOCKS_PER_SEC-start_cpu<<'\n';return 0;
}catch(const exception&e){cerr<<e.what()<<'\n';return 2;}}
