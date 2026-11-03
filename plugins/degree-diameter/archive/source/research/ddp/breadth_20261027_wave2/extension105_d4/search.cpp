#include <array>
#include <fstream>
#include <iostream>
#include <vector>
#include <cstdint>
#include <cassert>
#include <ctime>
using namespace std;
struct Bits { uint64_t a=0,b=0; void add(int v){if(v<64)a|=1ULL<<v;else b|=1ULL<<(v-64);} void join(Bits x){a|=x.a;b|=x.b;} int count()const{return __builtin_popcountll(a)+__builtin_popcountll(b);} };
int main(){
 double started=double(clock())/CLOCKS_PER_SEC;
 ifstream in("source.edges");int n,m;in>>n>>m;assert(n==104&&m==208);
 vector<pair<int,int>> edges(m);for(auto &e:edges)in>>e.first>>e.second;
 array<int,105> expected;ifstream calibration("first_expected.txt");for(auto &x:expected)calibration>>x;
 long long proposals=0,invalid=0,evaluated=0;int best=100000,best_i=-1,best_j=-1;bool first=true,hit=false;
 for(int i=0;i<m&&!hit;i++)for(int j=i+1;j<m&&!hit;j++){
  proposals++;auto [u,v]=edges[i];auto [w,z]=edges[j];
  if(u==w||u==z||v==w||v==z){invalid++;continue;}
  array<vector<int>,105> a;
  auto add=[&](int x,int y){a[x].push_back(y);a[y].push_back(x);};
  for(int k=0;k<m;k++)if(k!=i&&k!=j)add(edges[k].first,edges[k].second);
  for(int x:{u,v,w,z})add(104,x);
  array<Bits,105> b2;
  for(int x=0;x<105;x++){
   b2[x].add(x);
   for(int y:a[x]){b2[x].add(y);for(int q:a[y])b2[x].add(q);}
  }
  int total=0;
  for(int x=0;x<105;x++){
   Bits seen;auto take=[&](uint64_t bits,int offset){while(bits){int k=__builtin_ctzll(bits);bits&=bits-1;seen.join(b2[offset+k]);}};
   take(b2[x].a,0);take(b2[x].b,64);int miss=105-seen.count();
   if(first)assert(miss==expected[x]);total+=miss;
  }
  assert(total%2==0);int bad=total/2;evaluated++;first=false;
  if(bad<best){
   best=bad;best_i=i;best_j=j;ofstream out("best.edges");out<<105<<" "<<210<<"\n";
   for(int x=0;x<105;x++)for(int y:a[x])if(x<y)out<<x<<" "<<y<<"\n";
   ofstream meta("best.json");meta<<"{\"n\":105,\"m\":210,\"degree\":4,\"target_D\":4,\"bad_unordered_pairs\":"<<bad<<",\"deleted_edge_ids\":["<<i<<","<<j<<"],\"new_vertex\":104,\"new_neighbors\":["<<u<<","<<v<<","<<w<<","<<z<<"]}\n";
  }
  if(bad==0)hit=true;
 }
 ofstream out("production.json");out<<"{\"status\":\""<<(hit?"FOUND_D4_CANDIDATE":"COMPLETE_DISJOINT_EDGE_PAIRS_NO_D4")<<"\",\"running\":false,\"raw_pairs\":"<<proposals<<",\"overlapping_pairs\":"<<invalid<<",\"legal_candidates_scored\":"<<evaluated<<",\"best_bad_unordered_pairs\":"<<best<<",\"first_candidate_calibrated\":true,\"first_score_reused\":true,\"found_D4\":"<<(hit?"true":"false")<<",\"production_CPU_seconds\":"<<double(clock())/CLOCKS_PER_SEC-started<<",\"restarts\":0}\n";
 cout<<"scored="<<evaluated<<" best="<<best<<" hit="<<hit<<"\n";
}
