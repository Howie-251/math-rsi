#include <algorithm>
#include <array>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <vector>
constexpr int N=400,K=33;
std::array<std::array<unsigned char,N>,N>A{};
std::array<std::vector<int>,N>neighbors;
std::mt19937_64 rng(2026110133ULL);
int pick(int n){return rng()%n;}
std::vector<int>bestvalid;
int bestconflicts=10000;uint64_t totalmoves=0,restarts=0;
std::ofstream events("BEST_EVENTS.csv");
double began=0,budget=0;
double cpu(){return double(std::clock())/CLOCKS_PER_SEC-began;}
bool expired(){return cpu()>=budget;}
void observe(std::vector<int> s){
  while(true){int largest=0,index=-1;for(size_t i=0;i<s.size();i++){int c=0;for(int v:s)c+=A[s[i]][v];if(c>largest){largest=c;index=i;}}if(index<0)break;s.erase(s.begin()+index);}
  if(s.size()>bestvalid.size()){
    bestvalid=s;std::sort(bestvalid.begin(),bestvalid.end());events<<cpu()<<','<<restarts<<','<<totalmoves<<','<<bestvalid.size()<<'\n';events.flush();
  }else if(s.size()==bestvalid.size() && pick(8)==0)bestvalid=s;
}
std::vector<int> greedy(std::vector<int> s){
  std::array<bool,N>active{};active.fill(true);for(int u:s){active[u]=false;for(int v:neighbors[u])active[v]=false;}
  while(true){int best=10000,chosen=-1,ties=0;for(int u=0;u<N;u++)if(active[u]){int degree=0;for(int v:neighbors[u])degree+=active[v];if(degree<best){best=degree;chosen=u;ties=1;}else if(degree==best && pick(++ties)==0)chosen=u;}
    if(chosen<0)break;s.push_back(chosen);active[chosen]=false;for(int v:neighbors[chosen])active[v]=false;if(s.size()>=K)break;
  }return s;
}
int main(int argc,char **argv){
  budget=argc==2?std::stod(argv[1]):0;if(budget<=0)return 2;began=double(std::clock())/CLOCKS_PER_SEC;
  std::ifstream input("INPUT.txt");int n,l,seedcount;input>>n>>l>>seedcount;if(n!=400||l!=400||seedcount!=22)return 3;
  for(int i=0;i<l;i++){std::array<int,8>line{};for(int &u:line)input>>u;for(int u:line)for(int v:line)if(u!=v)A[u][v]=1;}
  for(int u=0;u<N;u++)for(int v=0;v<N;v++)if(A[u][v])neighbors[u].push_back(v);
  std::vector<int>old22(seedcount);for(int &v:old22)input>>v;if(!input)return 4;bestvalid=old22;
  events<<"CPU_seconds,restart,total_moves,valid_size\n";events<<cpu()<<",0,0,22\n";
  bool found=false,timed=false;
  for(int restart=0;restart<1000;restart++){
    if(expired()){timed=true;break;}restarts++;
    std::vector<int>s;
    if(restart==0)s=old22;
    else if(restart%2==0){s=bestvalid;for(int q=0;q<4&&!s.empty();q++)s.erase(s.begin()+pick(s.size()));s=greedy(s);}
    else s=greedy({});
    observe(s);if(bestvalid.size()>=K){bestconflicts=0;found=true;break;}
    std::array<bool,N>inside{};std::array<int,N>count{},tabu{};
    for(int u:s){inside[u]=true;for(int v:neighbors[u])count[v]++;}
    while(s.size()<K){int minimum=10000,chosen=-1,ties=0;for(int v=0;v<N;v++)if(!inside[v]){if(count[v]<minimum){minimum=count[v];chosen=v;ties=1;}else if(count[v]==minimum&&pick(++ties)==0)chosen=v;}s.push_back(chosen);inside[chosen]=true;for(int v:neighbors[chosen])count[v]++;}
    int conflicts=0;for(int u:s)conflicts+=count[u];conflicts/=2;
    if(conflicts<bestconflicts){bestconflicts=conflicts;observe(s);}
    if(conflicts==0){observe(s);found=true;break;}
    for(int move=1;move<=20000;move++){
      if((move&63)==0&&expired()){timed=true;break;}
      int maxselected=0;for(int u:s)maxselected=std::max(maxselected,count[u]);
      int bestdelta=10000,removeindex=-1,addvertex=-1,ties=0;
      for(int v=0;v<N;v++)if(!inside[v]){
        if(count[v]-maxselected-1>bestdelta)continue;
        if(tabu[v]>move && conflicts+count[v]-maxselected-1>=bestconflicts)continue;
        for(int i=0;i<K;i++){
          int u=s[i],delta=count[v]-count[u]-A[u][v];
          if(tabu[v]>move&&conflicts+delta>=bestconflicts)continue;
          if(delta<bestdelta){bestdelta=delta;removeindex=i;addvertex=v;ties=1;}
          else if(delta==bestdelta&&pick(++ties)==0){removeindex=i;addvertex=v;}
        }
      }
      if(removeindex<0)break;
      int removed=s[removeindex];inside[removed]=false;for(int v:neighbors[removed])count[v]--;
      inside[addvertex]=true;for(int v:neighbors[addvertex])count[v]++;s[removeindex]=addvertex;
      conflicts+=bestdelta;tabu[removed]=move+7+pick(7)+conflicts;totalmoves++;
      if(conflicts<bestconflicts){bestconflicts=conflicts;observe(s);}
      if(conflicts==0){observe(s);found=true;break;}
    }
    if(found||timed)break;
  }
  std::sort(bestvalid.begin(),bestvalid.end());
  std::ofstream ids("BEST_POINT_IDS.txt");for(int u:bestvalid)ids<<u<<'\n';
  std::cout<<std::setprecision(12)<<"{\"status\":\""<<(found?"FOUND_PUBLISHED_SIZE33_PENDING_SELECTED_PAIR_CHECK":"UNKNOWN_BOUNDED_REPRODUCTION_ATTEMPT")
    <<"\",\"found33\":"<<(found?"true":"false")<<",\"best_valid_size\":"<<bestvalid.size()<<",\"best_target33_conflict_count\":"<<bestconflicts
    <<",\"point_ids\":[";for(size_t i=0;i<bestvalid.size();i++){if(i)std::cout<<',';std::cout<<bestvalid[i];}
  std::cout<<"],\"seed\":2026110133,\"restarts\":"<<restarts<<",\"maximum_restarts\":1000,\"moves\":"<<totalmoves<<",\"maximum_moves_per_restart\":20000,\"CPU_stop\":"<<(timed?"true":"false")
    <<",\"maximum_proved\":false,\"public_object_reproduction_only\":true,\"source_edgefile_read\":false,\"graph_generated\":false,\"BFS_runs\":0,\"Lean_compilations\":0,\"CPU_seconds\":"<<cpu()<<"}\n";
}
