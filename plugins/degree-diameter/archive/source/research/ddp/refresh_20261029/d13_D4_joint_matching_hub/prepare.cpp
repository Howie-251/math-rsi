#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <queue>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
constexpr int N=6804,E=3402;
struct CNF {
  ofstream f; long long clauses=0,literals=0; int vars=E+N;
  CNF():f("base.cnf"){f<<string(127,' ')<<'\n';}
  void add(const vector<int>&c){for(int x:c)f<<x<<' ';f<<"0\n";++clauses;literals+=c.size();}
  void finish(){f.seekp(0);f<<"p cnf "<<vars<<' '<<clauses<<'\n';f.close();}
};
int main(int argc,char**argv){
  clock_t started=clock();assert(argc==2);
  vector<vector<int>> adj(N);vector<pair<int,int>> edges,matching;
  ifstream input(argv[1]);string line;
  while(getline(input,line)){if(line.empty()||line[0]=='#')continue;istringstream s(line);int u,v;assert(bool(s>>u>>v));if(u>v)swap(u,v);edges.push_back({u,v});adj[u].push_back(v);adj[v].push_back(u);}
  assert(edges.size()==44226);sort(edges.begin(),edges.end());
  vector<int> eid(N),partner(N,-1);
  for(auto [u,v]:edges)if(v/81==(u/81+42)%84){matching.push_back({u,v});int id=matching.size();eid[u]=eid[v]=id;partner[u]=v;partner[v]=u;}
  assert(matching.size()==E);for(int u=0;u<N;++u){assert(partner[u]>=0);sort(adj[u].begin(),adj[u].end());assert(adj[u].size()==13);}
  ofstream ids("SELECTORS.tsv");for(int e=0;e<E;++e)ids<<e+1<<' '<<matching[e].first<<' '<<matching[e].second<<'\n';ids.close();
  int pow2[12];pow2[0]=1;for(int j=1;j<12;++j)pow2[j]=2*pow2[j-1]%7;
  int mul[84][84];for(int h=0;h<84;++h)for(int g=0;g<84;++g)mul[h][g]=(h%7+pow2[h/7]*(g%7))%7+7*((h/7+g/7)%12);
  auto move=[&](int h,int v){return 81*mul[h][v/81]+v%81;};
  array<vector<int>,81>b2,b3,critical;
  long long representative_critical=0;
  for(int root=0;root<81;++root){
    vector<int>d(N,-1),support(N),q(N);int head=0,tail=0;d[root]=0;q[tail++]=root;
    int centralbit=1<<int(find(adj[root].begin(),adj[root].end(),partner[root])-adj[root].begin());
    while(head<tail){int u=q[head++];if(d[u]==4)continue;for(int j=0;j<int(adj[u].size());++j){int v=adj[u][j],mask=u==root?(1<<j):support[u];if(d[v]<0){d[v]=d[u]+1;support[v]=mask;q[tail++]=v;}else if(d[v]==d[u]+1)support[v]|=mask;}}
    assert(tail==N);for(int v=0;v<N;++v){if(d[v]<=2)b2[root].push_back(v);if(d[v]<=3)b3[root].push_back(v);if(d[v]==4&&support[v]==centralbit)critical[root].push_back(v);}
    representative_critical+=critical[root].size();
  }
  assert(representative_critical==13230);
  CNF cnf;vector<vector<int>> c2(N);vector<int> mark(E+1),coverage;int epoch=0;
  auto selector_ball=[&](int h,const vector<int>&ball){vector<int> out;++epoch;for(int x:ball){int id=eid[move(h,x)];if(mark[id]!=epoch){mark[id]=epoch;out.push_back(id);}}sort(out.begin(),out.end());return out;};
  long long cover_literals=0,c2_incidence=0;
  for(int h=0;h<84;++h)for(int x=0;x<81;++x){int t=81*h+x;coverage=selector_ball(h,b3[x]);cover_literals+=coverage.size();cnf.add(coverage);c2[t]=selector_ball(h,b2[x]);c2_incidence+=c2[t].size();int cvar=E+t+1;vector<int> clause={-cvar};clause.insert(clause.end(),c2[t].begin(),c2[t].end());cnf.add(clause);for(int s:c2[t])cnf.add({-s,cvar});}
  long long critical_cuts=0;
  for(int h=0;h<84;++h)for(int x=0;x<81;++x){int u=81*h+x;for(int raw:critical[x]){int t=move(h,raw);assert(!binary_search(c2[t].begin(),c2[t].end(),eid[u]));cnf.add({-eid[u],E+t+1});++critical_cuts;}}
  vector<int> symmetry;for(int x=0;x<81;++x)symmetry.push_back(eid[x]);sort(symmetry.begin(),symmetry.end());symmetry.erase(unique(symmetry.begin(),symmetry.end()),symmetry.end());assert(symmetry.size()==81);cnf.add(symmetry);
  vector<array<int,6>> sc(E);for(auto&r:sc)for(int&v:r)v=++cnf.vars;
  for(int i=0;i<E;++i){int x=i+1;cnf.add({-x,sc[i][0]});if(i){for(int j=0;j<6;++j)cnf.add({-sc[i-1][j],sc[i][j]});for(int j=1;j<6;++j)cnf.add({-x,-sc[i-1][j-1],sc[i][j]});cnf.add({-x,-sc[i-1][5]});}}
  cnf.finish();double cpu=double(clock()-started)/CLOCKS_PER_SEC;
  ofstream meta("MODEL.json");meta<<"{\n\"source_order\":6804,\"matching_selectors\":3402,\"variables\":"<<cnf.vars<<",\"clauses\":"<<cnf.clauses<<",\"literals\":"<<cnf.literals<<",\"r3_cover_clauses\":6804,\"r3_cover_literals\":"<<cover_literals<<",\"shared_c2_variables\":6804,\"c2_full_iff_selector_incidence\":"<<c2_incidence<<",\"representative_support_bfs\":81,\"representative_critical_pairs\":"<<representative_critical<<",\"expanded_endpoint_critical_cuts\":"<<critical_cuts<<",\"symmetry_or_size\":81,\"cardinality_limit\":6,\"prepare_cpu_seconds\":"<<cpu<<"}\n";
  cout<<"prepared vars="<<cnf.vars<<" clauses="<<cnf.clauses<<" CPU="<<cpu<<endl;
}
