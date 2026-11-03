#include <bits/stdc++.h>
using namespace std;
constexpr int N=504,BN=252,W=8;
using Graph=array<array<int,6>,N>;using Matrix=array<array<uint64_t,W>,N>;
Graph base;int basedeg[N]{};vector<array<int,3>>lines;vector<pair<int,int>>labels;vector<array<int,3>>groups;
int pairid[7][7];
void addbase(int u,int v){base[u][basedeg[u]++]=v;base[v][basedeg[v]++]=u;}
bool disjoint(int e,int f){auto[a,b]=labels[e];auto[c,d]=labels[f];return a!=c&&a!=d&&b!=c&&b!=d;}
int score(const Graph&g,Matrix*out=nullptr){
 Matrix r2{};for(int u=0;u<N;u++){
  r2[u][u>>6]|=1ULL<<(u&63);
  for(int v:g[u]){r2[u][v>>6]|=1ULL<<(v&63);for(int x:g[v])r2[u][x>>6]|=1ULL<<(x&63);}
 }
 int missing=0;
 for(int u=0;u<N;u++){
  array<uint64_t,W>r{};
  for(int word=0;word<W;word++){uint64_t bits=r2[u][word];while(bits){int v=64*word+__builtin_ctzll(bits);bits&=bits-1;for(int k=0;k<W;k++)r[k]|=r2[v][k];}}
  int count=0;for(auto bits:r)count+=__builtin_popcountll(bits);missing+=N-count;if(out)(*out)[u]=r;
 }assert(missing%2==0);return missing/2;
}
void rawwalk(const Graph&g,int root,int u,int depth,Matrix&seen){
 seen[root][u>>6]|=1ULL<<(u&63);if(depth==4)return;for(int v:g[u])rawwalk(g,root,v,depth+1,seen);
}
pair<int,int> relevant(const Graph&g,const vector<pair<int,int>>&edges){
 int walks=0;for(auto[u,v]:edges)walks+=disjoint(u%21,v%21);
 bool reachable[BN][BN]{};
 for(int u=0;u<BN;u++){
  int ns[3];for(int j=0;j<3;j++)ns[j]=g[252+u][3+j]-252;
  for(int i=0;i<3;i++)for(int j=i+1;j<3;j++)walks+=disjoint(ns[i]%21,ns[j]%21);
  for(int v:ns){if(disjoint(u%21,v%21))reachable[u][v]=true;for(int j=3;j<6;j++){int x=g[252+v][j]-252;if(disjoint(u%21,x%21))reachable[u][x]=true;}}
 }
 int distinct=0;for(int u=0;u<BN;u++)for(int v=u+1;v<BN;v++)distinct+=reachable[u][v];return {walks,distinct};
}
void setup(const string&dir){
 for(int m=0;m<3;m++)for(int c=0;c<3;c++){array<int,3>l;for(int x=0;x<3;x++)l[x]=3*x+(m*x+c)%3;lines.push_back(l);}
 for(int x=0;x<3;x++)lines.push_back({3*x,3*x+1,3*x+2});
 for(int i=0;i<7;i++)for(int j=i+1;j<7;j++){pairid[i][j]=pairid[j][i]=labels.size();labels.push_back({i,j});}
 for(int r=0;r<7;r++){array<int,3>group;for(int k=1;k<=3;k++)group[k-1]=pairid[(r+k)%7][(r-k+7)%7];sort(group.begin(),group.end());groups.push_back(group);}
 for(int u=0;u<9;u++){
  int incidence=0;for(auto l:lines)incidence+=find(l.begin(),l.end(),u)!=l.end();assert(incidence==4);
  for(int e=0;e<21;e++){auto[i,j]=labels[e];addbase(7*u+i,63+21*u+e);addbase(7*u+j,63+21*u+e);}
 }
 for(int L=0;L<12;L++)for(int e=0;e<21;e++)for(int u:lines[L])addbase(63+21*u+e,252+21*L+e);
 for(int u=0;u<9;u++)for(int v=u+1;v<9;v++){int common=0;for(auto l:lines)common+=(find(l.begin(),l.end(),u)!=l.end()&&find(l.begin(),l.end(),v)!=l.end());assert(common==1);}
 for(int v=0;v<N;v++)assert(basedeg[v]==(v<252?6:3));
 ofstream o(dir+"/structure.json");o<<"{\"points\":9,\"lines\":[";
 for(int i=0;i<12;i++){if(i)o<<',';auto l=lines[i];o<<'['<<l[0]<<','<<l[1]<<','<<l[2]<<']';}
 o<<"],\"K7_edge_labels\":[";for(int e=0;e<21;e++){if(e)o<<',';o<<'['<<labels[e].first<<','<<labels[e].second<<']';}
 o<<"],\"initial_round_robin_label_groups\":[";for(int i=0;i<7;i++){if(i)o<<',';auto t=groups[i];o<<'['<<t[0]<<','<<t[1]<<','<<t[2]<<']';}
 o<<"],\"encoding\":{\"point\":\"u=3*x+y, AG(2,3)\",\"A\":\"7*u+i,0..62\",\"C\":\"63+21*u+edge_id,63..251\",\"B\":\"252+21*line_id+edge_id,252..503\"},\"layer_sizes\":[63,189,252],\"fixed_edges_AC\":378,\"fixed_edges_CB\":756,\"cubic_H_edges\":378,\"total_vertices\":504,\"total_edges\":1512,\"regular_degree\":6}\n";
}
int main(int argc,char**argv){
 assert(argc==3);string dir=argv[1];double limit=stod(argv[2]);clock_t started=clock();auto cpu=[&](){return double(clock()-started)/CLOCKS_PER_SEC;};setup(dir);
 const uint64_t seeds[2]={2026102765041ULL,2026102765042ULL};Graph bestg;vector<pair<int,int>>bestH;int best=INT_MAX,totallegal=0,totalillegal=0,completed=0;bool limited=false,hit=false,calibrated=false;
 struct Stat{uint64_t seed;int initial,best,final,legal=0,illegal=0,accepted=0,relatedwalks,relatedpairs,minAmissing;};vector<Stat>stats;
 for(int st=0;st<2&&!limited&&!hit;st++){
  mt19937_64 rng(seeds[st]);uniform_real_distribution<double>unit(0,1);uniform_int_distribution<int>edgepick(0,377);
  Graph g=base;int deg[N];copy(basedeg,basedeg+N,deg);bool h[BN][BN]{};vector<pair<int,int>>he;
  auto addH=[&](int u,int v){assert(u!=v&&!h[u][v]);h[u][v]=h[v][u]=true;he.push_back(minmax(u,v));g[252+u][deg[252+u]++]=252+v;g[252+v][deg[252+v]++]=252+u;};
  for(auto group:groups){vector<int>cycle;for(int L=0;L<12;L++)for(int e:group)cycle.push_back(21*L+e);for(int j=0;j<36;j++)addH(cycle[j],cycle[(j+1)%36]);}
  for(int e=0;e<21;e++){array<int,12>ls; iota(ls.begin(),ls.end(),0);shuffle(ls.begin(),ls.end(),rng);for(int j=0;j<12;j+=2)addH(21*ls[j]+e,21*ls[j+1]+e);}
  assert(he.size()==378);for(int d:deg)assert(d==6);
  Matrix initialreach;int current=score(g,&initialreach);auto rel=relevant(g,he);assert(rel.first==1008);
  Stat ss;ss.seed=seeds[st];ss.initial=ss.best=current;ss.relatedwalks=rel.first;ss.relatedpairs=rel.second;ss.minAmissing=N;
  for(int u=0;u<63;u++){int c=0;for(auto w:initialreach[u])c+=__builtin_popcountll(w);ss.minAmissing=min(ss.minAmissing,N-c);}assert(ss.minAmissing>=48);
  if(current<best){best=current;bestg=g;bestH=he;}
  auto replace=[&](int u,int oldv,int newv){for(int j=3;j<6;j++)if(g[252+u][j]==252+oldv){g[252+u][j]=252+newv;return;}assert(false);};
  while(ss.legal<2000){
   if((ss.legal&15)==0&&cpu()>=limit){limited=true;break;}
   int i=edgepick(rng),j=edgepick(rng);if(i==j){ss.illegal++;continue;}
   auto[a,b]=he[i];auto[c,d]=he[j];if(a==c||a==d||b==c||b==d){ss.illegal++;continue;}
   if(rng()&1)swap(c,d);
   if(h[a][c]||h[b][d]){ss.illegal++;continue;}
   replace(a,b,c);replace(b,a,d);replace(c,d,a);replace(d,c,b);
   h[a][b]=h[b][a]=h[c][d]=h[d][c]=false;h[a][c]=h[c][a]=h[b][d]=h[d][b]=true;
   he[i]=minmax(a,c);he[j]=minmax(b,d);ss.legal++;totallegal++;
   Matrix formal;int next=score(g,calibrated?nullptr:&formal);
   if(!calibrated){Matrix walks{};for(int u=0;u<N;u++)rawwalk(g,u,u,0,walks);assert(walks==formal);
    ofstream o(dir+"/first_proposal_calibration.json");o<<"{\"status\":\"MATCH\",\"formal_proposal\":1,\"all504_rows_match\":true,\"walks_per_root\":1555,\"raw_walks_enumerated\":783720,\"boolean_R2_squared_bad_unordered_pairs\":"<<next<<",\"method\":\"Direct recursive enumeration of every walk length0..4; compare every504x504 bit to Boolean R2 squared. No graph BFS.\"}\n";calibrated=true;
   }
   ss.best=min(ss.best,next);if(next<best){best=next;bestg=g;bestH=he;}
   if(!next){current=next;ss.accepted++;hit=true;break;}
   double temperature=200.0*pow(2.0/200.0,double(ss.legal-1)/1999.0);
   if(next<=current||unit(rng)<exp(-double(next-current)/temperature)){current=next;ss.accepted++;}
   else{
    replace(a,c,b);replace(b,d,a);replace(c,a,d);replace(d,b,c);
    h[a][c]=h[c][a]=h[b][d]=h[d][b]=false;h[a][b]=h[b][a]=h[c][d]=h[d][c]=true;
    he[i]=minmax(a,b);he[j]=minmax(c,d);
   }
  }
  ss.final=current;stats.push_back(ss);totalillegal+=ss.illegal;if(ss.legal==2000)completed++;
  cout<<"PROFILE "<<st<<" legal="<<ss.legal<<" best_bad="<<ss.best<<" CPU="<<cpu()<<endl;
 }
 set<pair<int,int>>all;for(int u=0;u<N;u++){set<int>ns(bestg[u].begin(),bestg[u].end());assert(ns.size()==6&&!ns.count(u));for(int v:ns)all.insert(minmax(u,v));}assert(all.size()==1512);
 ofstream ef(dir+"/best.edges");ef<<"504 1512\n";for(auto[u,v]:all)ef<<u<<' '<<v<<'\n';
 ofstream hf(dir+"/best_H.edges");hf<<"252 378\n";for(auto[u,v]:bestH)hf<<u<<' '<<v<<'\n';
 Matrix finalreach;assert(score(bestg,&finalreach)==best);int categories[3][3]{};auto type=[](int u){return u<63?0:u<252?1:2;};
 ofstream bf(dir+"/best_score.json");bf<<"{\"n\":504,\"m\":1512,\"degree\":6,\"bad_unordered_pairs_gt4\":"<<best<<",\"missing_pairs\":[";bool comma=false;
 for(int u=0;u<N;u++)for(int v=u+1;v<N;v++)if(!(finalreach[u][v>>6]>>(v&63)&1)){categories[type(u)][type(v)]++;if(comma)bf<<',';comma=true;bf<<'['<<u<<','<<v<<']';}
 auto rel=relevant(bestg,bestH);bf<<"],\"best_H_relevant_short_walks\":"<<rel.first<<",\"best_H_distinct_relevant_endpoint_pairs\":"<<rel.second<<",\"bad_pair_categories\":{\"AA\":"<<categories[0][0]<<",\"AC\":"<<categories[0][1]<<",\"AB\":"<<categories[0][2]<<",\"CC\":"<<categories[1][1]<<",\"CB\":"<<categories[1][2]<<",\"BB\":"<<categories[2][2]<<"}}\n";
 ofstream t(dir+"/search_result.json");t<<"{\"status\":\""<<(hit?"HIT_FULL504_DIAMETER_AT_MOST4":limited?"CPU_LIMIT_PARTIAL_PROFILE":"TWO_FIXED_GLOBAL_H_PROFILES_FAILED")<<"\",\"starts_planned\":2,\"starts_started\":"<<stats.size()<<",\"starts_completed\":"<<completed<<",\"legal_proposals_per_start_limit\":2000,\"legal_proposals_actual\":"<<totallegal<<",\"illegal_swap_draws\":"<<totalillegal<<",\"best_bad_unordered_pairs_gt4\":"<<best<<",\"score\":\"Exact all504 ordered relation (I+A+A^2)^2, then divide offdiagonal missing count by2\",\"first_formal_proposal_calibration\":"<<(calibrated?"true":"false")<<",\"full_graph_generated\":true,\"n\":504,\"m\":1512,\"degree\":6,\"BFS_performed\":false,\"CPU_seconds\":"<<cpu()<<",\"CPU_internal_limit_seconds\":"<<limit<<",\"profiles\":[";
 for(int i=0;i<(int)stats.size();i++){auto s=stats[i];if(i)t<<',';t<<"{\"seed\":"<<s.seed<<",\"initial_bad\":"<<s.initial<<",\"best_bad\":"<<s.best<<",\"final_bad\":"<<s.final<<",\"legal_proposals\":"<<s.legal<<",\"illegal_draws\":"<<s.illegal<<",\"accepted\":"<<s.accepted<<",\"initial_relevant_short_walks\":"<<s.relatedwalks<<",\"initial_distinct_relevant_endpoint_pairs\":"<<s.relatedpairs<<",\"initial_minimum_A_root_missing\":"<<s.minAmissing<<'}';}t<<"]}\n";
 if(hit)cout<<"HIT_SAVED best.edges"<<endl;
}
