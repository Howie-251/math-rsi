#include <array>
#include <cassert>
#include <cstdio>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using V=array<int,3>;
using M=array<V,3>;
#include "literal_inputs.h"
const int N=56862, Q=729;
int A[9][9],P[9][9],neg9[9],inv9[9];
array<array<int,6>,78> C{};
const array<int,6> reversep={1,0,3,2,4,5};
vector<V> vecs;
array<array<int,729>,8> mapped{};
array<array<array<int,9>,729>,8> images{};
int add9(int a,int b){return ((a%3+b%3)%3)+3*((a/3+b/3)%3);}
int mul9(int a,int b){return ((a%3*(b%3)+2*(a/3)*(b/3))%3)+3*((a%3*(b/3)+a/3*(b%3))%3);}
void need(bool b,const string&s){if(!b)throw runtime_error(s);}
V addv(V a,V b){for(int i=0;i<3;i++)a[i]=A[a[i]][b[i]];return a;}
V subv(V a,V b){for(int i=0;i<3;i++)a[i]=A[a[i]][neg9[b[i]]];return a;}
V scale(int t,V a){for(int&i:a)i=P[t][i];return a;}
V act(const M&m,V x){V y{};for(int i=0;i<3;i++)for(int j=0;j<3;j++)y[i]=A[y[i]][P[m[i][j]][x[j]]];return y;}
int enc(V x){return x[0]+9*x[1]+81*x[2];}
int det(V a,V b,V c){
 int s=0;
 s=A[s][P[a[0]][P[b[1]][c[2]]]];s=A[s][P[a[1]][P[b[2]][c[0]]]];s=A[s][P[a[2]][P[b[0]][c[1]]]];
 s=A[s][neg9[P[a[0]][P[b[2]][c[1]]]]];s=A[s][neg9[P[a[1]][P[b[0]][c[2]]]]];s=A[s][neg9[P[a[2]][P[b[1]][c[0]]]]];return s;
}
int mod26(int x){return (x%26+26)%26;}
int label(int c,int g){return c*26+mod26(g);}
int chart(int u,int p){int v=C[u][p];if(p<4)return p;return p==4?(u<v?4:5):(u<v?6:7);}
int outq(int k){return k<4?reversep[k]:(k<6?4:5);}
int inp(int k){return k<4?k:(k<6?4:5);}
int otherchart(int k){return k^1;}
vector<int> neighbors_formula(int vertex){
 int u=vertex/Q,x=vertex%Q;vector<int> ns;ns.reserve(54);
 for(int p=0;p<6;p++){int k=chart(u,p),v=C[u][p];for(int t=0;t<9;t++)ns.push_back(Q*v+images[k][x][t]);}
 return ns;
}
int main(int argc,char**argv){
 try{
 need(argc==2,"edge file argument required");double start=double(clock())/CLOCKS_PER_SEC;
 for(int a=0;a<9;a++)for(int b=0;b<9;b++){A[a][b]=add9(a,b);P[a][b]=mul9(a,b);}
 for(int a=0;a<9;a++){neg9[a]=-1;for(int b=0;b<9;b++){if(A[a][b]==0)neg9[a]=b;if(P[a][b]==1)inv9[a]=b;}need(neg9[a]>=0,"additive inverse");if(a)need(P[a][inv9[a]]==1,"nonzero multiplicative inverse");}
 for(int a=0;a<9;a++)for(int b=0;b<9;b++){
  need(A[a][b]==A[b][a]&&P[a][b]==P[b][a],"commutative field operations");
  need(A[a][0]==a&&P[a][1]==a&&P[a][0]==0,"identity laws");
  for(int c=0;c<9;c++)need(A[A[a][b]][c]==A[a][A[b][c]]&&P[P[a][b]][c]==P[a][P[b][c]]&&P[a][A[b][c]]==A[P[a][b]][P[a][c]],"field axioms");
 }
 for(int c=0;c<3;c++)for(int g=0;g<26;g++){
  int u=label(c,g);
  C[u][0]=c==0?label(0,g+2):c==1?label(2,g+6):label(1,g+17);
  C[u][1]=c==0?label(0,g-2):c==1?label(2,g-17):label(1,g-6);
  C[u][2]=label((c+1)%3,g);C[u][3]=label((c+2)%3,g);
  C[u][4]=c==0?label(1,g+5):c==1?label(0,g-5):label(2,g+13);
  C[u][5]=c==0?label(2,g+10):c==1?label(1,g+13):label(0,g-10);
 }
 int controller_edges=0;
 for(int u=0;u<78;u++){
  set<int>distinct(C[u].begin(),C[u].end());need(distinct.size()==6&&!distinct.count(u),"simple controller");
  for(int p=0;p<6;p++){need(C[u][p]==declared_controller[u][p],"explicit rule/controller literal binding");need(C[C[u][p]][reversep[p]]==u,"true inverse port");if(u<C[u][p])controller_edges++;}
  need(C[C[C[u][2]][2]][2]==u,"b-cube triangle");
 }
 need(controller_edges==234,"controller edge count");
 for(int x=0;x<Q;x++)vecs.push_back({x%9,(x/9)%9,x/81});
 for(int k=0;k<8;k++){
  int p=inp(k),q=outq(k);need(act(matrices[k],directions[p])==directions[q],"port exact compatibility");
  for(int i=0;i<3;i++){V e{};e[i]=1;need(act(matrices[otherchart(k)],act(matrices[k],e))==e,"actual matrix inverse");}
  for(int x=0;x<Q;x++){
   V y=act(matrices[k],vecs[x]);mapped[k][x]=enc(y);
   for(int t=0;t<9;t++)images[k][x][t]=enc(addv(y,scale(t,directions[q])));
  }
 }
 int turns=0,pencils=0;
 ofstream turnfile("TURN_DETERMINANTS.tsv");turnfile<<"chart\tprevious_reverse_port\tnext_port\tdeterminant\n";
 for(int k=0;k<8;k++){
  int p=inp(k),q=outq(k);
  for(int a=0;a<6;a++)if(a!=p)for(int b=0;b<6;b++)if(b!=q){
   int d=det(act(matrices[k],directions[a]),directions[q],directions[b]);need(d!=0,"NB3 central rank");turnfile<<k<<'\t'<<a<<'\t'<<b<<'\t'<<d<<'\n';turns++;
  }
  array<bool,729>covered{};int planes=0;
  for(int a=0;a<6;a++)if(a!=p){V e=act(matrices[k],directions[a]);for(int t=0;t<9;t++)for(int s=0;s<9;s++)covered[enc(addv(scale(t,e),scale(s,directions[q])))]=true;planes++;}
  for(int b=0;b<6;b++)if(b!=q){for(int t=0;t<9;t++)for(int s=0;s<9;s++)covered[enc(addv(scale(t,directions[q]),scale(s,directions[b])))]=true;planes++;}
  need(planes==10,"ten pencil planes");for(bool b:covered)need(b,"adjacent pencil misses offset");pencils++;
 }
 ofstream routefile("CONTROLLER_ACTUAL_ROUTES.tsv");routefile<<"source\ttarget\tp1\tp2\tp3\tNB_required\n";
 int paircount=0,nbcount=0,adjcount=0;
 for(int u=0;u<78;u++){
  array<array<int,3>,78>witness{};array<bool,78>found{};
  for(int p1=0;p1<6;p1++)for(int p2=0;p2<6;p2++)for(int p3=0;p3<6;p3++){
   int u1=C[u][p1],u2=C[u1][p2],v=C[u2][p3];bool adjacent=false;for(int p=0;p<6;p++)adjacent|=C[u][p]==v;
   bool nb=p2!=reversep[p1]&&p3!=reversep[p2];
   if((adjacent||nb)&&!found[v]){witness[v]={p1,p2,p3};found[v]=true;}
  }
  for(int v=0;v<78;v++){
   need(found[v],"controller pair has no required actual walk");bool adjacent=false;for(int p=0;p<6;p++)adjacent|=C[u][p]==v;
   auto w=witness[v];int u1=C[u][w[0]],u2=C[u1][w[1]];need(C[u2][w[2]]==v,"witness endpoint");
   if(!adjacent){need(w[1]!=reversep[w[0]]&&w[2]!=reversep[w[1]],"NB witness");need(det(act(matrices[chart(u1,w[1])],directions[reversep[w[0]]]),directions[reversep[w[1]]],directions[w[2]])!=0,"actual route rank");nbcount++;}else adjcount++;
   routefile<<u<<'\t'<<v<<'\t'<<w[0]<<'\t'<<w[1]<<'\t'<<w[2]<<'\t'<<!adjacent<<'\n';paircount++;
  }
 }
 double finite_cpu=double(clock())/CLOCKS_PER_SEC-start;
 vector<vector<int>>adj(N);for(auto&ns:adj)ns.reserve(54);
 ifstream input(argv[1]);need(bool(input),"full edge file available");int a,b;pair<int,int>prev={-1,-1};long long edges=0;
 while(input>>a>>b){
  need(0<=a&&a<b&&b<N,"literal edge labels/order");need(prev<pair<int,int>{a,b},"strict global literal ordering/simple");prev={a,b};
  int u=a/Q,v=b/Q,x=a%Q,y=b%Q,p=-1;for(int k=0;k<6;k++)if(C[u][k]==v)p=k;
  need(p>=0,"literal edge controller relation");int k=chart(u,p),q=reversep[p];V diff=subv(vecs[y],vecs[mapped[k][x]]);
  int h=0;while(directions[q][h]==0)h++;int t=P[diff[h]][inv9[directions[q][h]]];need(diff==scale(t,directions[q]),"literal edge affine relation");
  adj[a].push_back(b);adj[b].push_back(a);edges++;
 }
 need(input.eof(),"edge file parse completed");need(edges==1535274,"full edge count");
 for(int u=0;u<N;u++)need(adj[u].size()==54,"literal degree exact54");
 double literal_cpu=double(clock())/CLOCKS_PER_SEC-start-finite_cpu;
 vector<int>roots;for(int x=0;x<729;x++)roots.push_back(x);for(int u=1;u<78;u++)roots.push_back(u*Q);
 vector<int>mark(N,0),queue(N),dist(N);int stamp=0;
 ofstream csv("BFS_PREDICTION_VS_ACTUAL.csv");csv<<"root,pred_R0,pred_R1,pred_R2,pred_R3,actual_R0,actual_R1,actual_R2,actual_R3,reachable,max_distance\n";
 map<array<int,4>,int>histogram_counts;
 for(int root:roots){
  stamp++;int b2=1;mark[root]=stamp;auto ns=neighbors_formula(root);need(set<int>(ns.begin(),ns.end()).size()==54,"formula distinct54");
  for(int v:ns)if(mark[v]!=stamp){mark[v]=stamp;b2++;}
  for(int v:ns)for(int w:neighbors_formula(v))if(mark[w]!=stamp){mark[w]=stamp;b2++;}
  array<int,4>pred={1,54,b2-55,N-b2};
  stamp++;int head=0,tail=1;queue[0]=root;dist[root]=0;mark[root]=stamp;array<int,4>actual={1,0,0,0};
  while(head<tail){int v=queue[head++],d=dist[v];if(d==3)continue;for(int w:adj[v])if(mark[w]!=stamp){mark[w]=stamp;dist[w]=d+1;queue[tail++]=w;actual[d+1]++;}}
  need(tail==N,"literal BFS missing vertices");need(actual==pred,"predicted/actual distance classes");histogram_counts[actual]++;
  csv<<root;for(int z:pred)csv<<','<<z;for(int z:actual)csv<<','<<z;csv<<','<<tail<<",3\n";
 }
 double bfs_cpu=double(clock())/CLOCKS_PER_SEC-start-finite_cpu-literal_cpu;
 ofstream hist("BFS_HISTOGRAMS.tsv");hist<<"R0\tR1\tR2\tR3\troots\n";for(auto [h,c]:histogram_counts){for(int z:h)hist<<z<<'\t';hist<<c<<'\n';}
 cout<<"{\"status\":\"PASS\",\"n\":56862,\"m\":"<<edges<<",\"all_literal_degrees\":54,\"literal_edge_formula_binding\":true,\"global_strict_order\":true,\"simple\":true,\"independent_field\":true,\"used_charts\":8,\"turn_determinants\":"<<turns<<",\"adjacent_pencils\":"<<pencils<<",\"pencil_offsets_each\":729,\"controller_pairs\":"<<paircount<<",\"same_nonadjacent_NB3_pairs\":"<<nbcount<<",\"adjacent_pairs\":"<<adjcount<<",\"literal_BFS_roots\":"<<roots.size()<<",\"full_graph_all_pairs_BFS\":false,\"actualWalk_all_pairs_proof\":true,\"exact_diameter\":3,\"finite_premise_cpu\":"<<finite_cpu<<",\"literal_binding_cpu\":"<<literal_cpu<<",\"BFS_prediction_cpu\":"<<bfs_cpu<<",\"validator_cpu\":"<<double(clock())/CLOCKS_PER_SEC-start<<"}\n";
 return 0;
 }catch(const exception&e){cerr<<"VALIDATION_FAIL: "<<e.what()<<'\n';return 2;}
}
