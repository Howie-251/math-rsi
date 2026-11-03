#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <sys/resource.h>
using namespace std;
int F[64][64],lg64[64],iv[64];vector<int>sf;string folder;
int power(int a,int n){int r=1;while(n){if(n&1)r=F[r][a];a=F[a][a];n>>=1;}return r;}
int trace(int a){return a^power(a,8);}
int mod3(int a){a%=3;return a<0?a+3:a;}
struct Point{array<int,4>q;int x,y;};
struct Line{array<int,9>p,tau;int spread=-1,t0=-1,centre=-1,wx=-1,wy=-1;};
int main(int argc,char**argv){
 assert(argc==2);folder=argv[1];clock_t begin=clock();rlimit limit{10,10};setrlimit(RLIMIT_CPU,&limit);
 for(int a=0;a<64;a++)for(int b=0;b<64;b++){int x=a,y=b,r=0;while(y){if(y&1)r^=x;x<<=1;if(x&64)x^=67;y>>=1;}F[a][b]=r;}
 fill(lg64,lg64+64,-1);int z=1;for(int e=0;e<63;e++){assert(lg64[z]<0);lg64[z]=e;z=F[z][2];}assert(z==1);
 assert(power(2,21)!=1&&power(2,9)!=1);for(int a=1;a<64;a++)iv[a]=power(a,62);
 for(int a=0;a<64;a++)if(power(a,8)==a)sf.push_back(a);assert(sf.size()==8);
 array<array<int,2>,64>decomp;array<int,64>found{};
 for(int a:sf)for(int b:sf){int x=a^F[2][b];assert(!found[x]++);decomp[x]={a,b};}
 vector<array<int,4>>quads;
 for(int a:sf)for(int b:sf)for(int c:sf)for(int d:sf){array<int,4>q={a,b,c,d};int first=0;for(int v:q)if(v){first=v;break;}if(first==1)quads.push_back(q);}
 sort(quads.begin(),quads.end());assert(quads.size()==585);vector<Point>pts;
 int pid[64][64];for(auto&row:pid)fill(row,row+64,-1);
 for(auto q:quads){int x=q[0]^F[2][q[1]],y=q[2]^F[2][q[3]];assert(pid[x][y]<0);pid[x][y]=pts.size();pts.push_back({q,x,y});}
 int normalized[64][64];for(int x=0;x<64;x++)for(int y=0;y<64;y++){
  if(!x&&!y){normalized[x][y]=-1;continue;}array<int,4>q={decomp[x][0],decomp[x][1],decomp[y][0],decomp[y][1]};int first=0;for(int v:q)if(v){first=v;break;}int s=iv[first];normalized[x][y]=pid[F[s][x]][F[s][y]];assert(normalized[x][y]>=0);
 }
 auto det=[&](const Point&a,const Point&b){return F[a.x][b.y]^F[a.y][b.x];};
 set<array<int,9>>lineSet;
 for(int a=0;a<585;a++)for(int b=a+1;b<585;b++)if(trace(det(pts[a],pts[b]))==0){
  array<int,9>row;int at=0;for(int l:sf)row[at++]=normalized[pts[a].x^F[l][pts[b].x]][pts[a].y^F[l][pts[b].y]];row[8]=b;sort(row.begin(),row.end());assert(adjacent_find(row.begin(),row.end())==row.end());lineSet.insert(row);
 }
 assert(lineSet.size()==585);vector<Line>lines;array<int,65>spreadLine;spreadLine.fill(-1);array<int,585>incidence{};
 vector<vector<int>>pairline(585,vector<int>(585,-1));
 for(auto row:lineSet){
  Line line;line.p=row;set<int>labels;
  for(int p:row){incidence[p]++;labels.insert(pts[p].x?F[pts[p].y][iv[pts[p].x]]:64);}
  if(labels.size()==1){
   line.spread=*labels.begin();assert(spreadLine[line.spread]<0);spreadLine[line.spread]=lines.size();
   line.wx=line.spread==64?1:0;line.wy=line.spread==64?0:1;
  }else{
   assert(labels.size()==9);vector<int>finite;
   if(!labels.count(64)){finite.assign(labels.begin(),labels.end());}
   else{
    for(int t=0;t<64;t++)if(!labels.count(t)){line.t0=t;break;}assert(line.t0>=0);
    for(int t:labels){if(t==64)finite.push_back(0);else finite.push_back(iv[t^line.t0]);}
   }
   int centres=0;
   for(int c=0;c<64;c++){int radius=power(finite[0]^c,9);if(!radius)continue;bool same=true;for(int t:finite)if(power(t^c,9)!=radius){same=false;break;}if(same){line.centre=c;centres++;}}
   assert(centres==1);
   if(line.t0<0){line.wx=1;line.wy=line.centre;}else{line.wx=line.centre;line.wy=1^F[line.t0][line.centre];}
  }
  for(int j=0;j<9;j++){
   auto p=pts[row[j]];int d=F[p.x][line.wy]^F[p.y][line.wx];assert(d);line.tau[j]=lg64[d]%3;
   for(int s:sf)if(s)assert(lg64[F[s][d]]%3==line.tau[j]);
  }
  for(int a:row)for(int b:row)if(a!=b){assert(pairline[a][b]<0);pairline[a][b]=lines.size();}
  lines.push_back(line);
 }
 for(int n:incidence)assert(n==9);for(int l:spreadLine)assert(l>=0);
 auto tau=[&](int p,int l){auto&line=lines[l];int j=lower_bound(line.p.begin(),line.p.end(),p)-line.p.begin();assert(j<9&&line.p[j]==p);return line.tau[j];};
 int l0=spreadLine[0],linf=spreadLine[64];array<int,3>hist{};vector<array<int,4>>geodesics;
 for(int p:lines[l0].p){
  int q=-1,mid=-1;for(int candidate:lines[linf].p)if(pairline[p][candidate]>=0){assert(q<0);q=candidate;mid=pairline[p][candidate];}assert(q>=0);
  int phase=mod3(-tau(p,l0)+tau(p,mid)-tau(q,mid)+tau(q,linf));hist[phase]++;geodesics.push_back({p,mid,q,phase});
 }
 ofstream geo(folder+"/GEOMETRY.json");geo<<"{\"field_polynomial\":67,\"j\":2,\"F8\":[";for(int i=0;i<8;i++){if(i)geo<<',';geo<<sf[i];}geo<<"],\"point_order\":\"Lexicographic normalized F8 quadruple, embeddedF64 valuesnumeric\",\"points\":[";
 for(int i=0;i<585;i++){if(i)geo<<',';auto p=pts[i];geo<<"{\"q\":[";for(int j=0;j<4;j++){if(j)geo<<',';geo<<p.q[j];}geo<<"],\"x\":"<<p.x<<",\"y\":"<<p.y<<'}';}
 geo<<"],\"lines\":[";
 for(int i=0;i<585;i++){if(i)geo<<',';auto l=lines[i];geo<<"{\"points\":[";for(int j=0;j<9;j++){if(j)geo<<',';geo<<l.p[j];}geo<<"],\"tau\":[";for(int j=0;j<9;j++){if(j)geo<<',';geo<<l.tau[j];}geo<<"],\"spread_label\":"<<l.spread<<",\"t0\":"<<l.t0<<",\"centre\":"<<l.centre<<",\"pole\":["<<l.wx<<','<<l.wy<<"]}";}
 geo<<"]}\n";geo.close();
 ofstream phaseout(folder+"/PHASE_PREFLIGHT.json");phaseout<<"{\"histogram\":["<<hist[0]<<','<<hist[1]<<','<<hist[2]<<"],\"all_three_colours\":"<<(hist[0]&&hist[1]&&hist[2]?"true":"false")<<",\"balanced_prediction\":"<<(hist[0]==3&&hist[1]==3&&hist[2]==3?"true":"false")<<",\"S0_line\":"<<l0<<",\"Sinfinity_line\":"<<linf<<",\"routes\":[";
 for(int i=0;i<9;i++){if(i)phaseout<<',';auto g=geodesics[i];phaseout<<"{\"p\":"<<g[0]<<",\"middle_line\":"<<g[1]<<",\"q\":"<<g[2]<<",\"phase\":"<<g[3]<<'}';}phaseout<<"],\"CPU_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC<<"}\n";phaseout.close();
 if(!hist[0]||!hist[1]||!hist[2]){
  ofstream out(folder+"/NATIVE_RESULT.json");out<<"{\"status\":\"CANONICAL_PHASE_GATE_MISSING_COLOUR_NO_GRAPH\",\"actual_graphs\":0,\"actual_D\":null,\"native_CPU_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC<<"}\n";return 0;
 }
 constexpr int N=3705;vector<vector<int>>adj(N);auto edge=[&](int u,int v){assert(u!=v);adj[u].push_back(v);adj[v].push_back(u);};
 auto P=[](int p,int s){return 3*p+s;};auto L=[](int l,int s){return 1755+3*l+s;};auto T=[](int l,int s){return 3510+3*l+s;};
 for(int l=0;l<585;l++){
  for(int j=0;j<9;j++)for(int s=0;s<3;s++)edge(P(lines[l].p[j],s),L(l,(s+lines[l].tau[j])%3));
  for(int s=0;s<3;s++)edge(L(l,s),L(l,(s+1)%3));
 }
 for(int k=0;k<65;k++){int l=spreadLine[k];for(int j=0;j<9;j++)for(int s=0;s<3;s++)edge(P(lines[l].p[j],s),T(k,(s+lines[l].tau[j])%3));for(int s=0;s<3;s++)edge(T(k,s),T(k,(s+1)%3));}
 long long arcs=0;int d10=0,d11=0;
 for(int u=0;u<N;u++){sort(adj[u].begin(),adj[u].end());assert(adjacent_find(adj[u].begin(),adj[u].end())==adj[u].end());assert(adj[u].size()==size_t(u<1755?10:11));arcs+=adj[u].size();if(adj[u].size()==10)d10++;else d11++;for(int v:adj[u])assert(find(adj[v].begin(),adj[v].end(),u)!=adj[v].end());}assert(arcs==39000&&d10==1755&&d11==1950);
 vector<int>dist(N),queue(N);int roots=0,fail=-1,first=-1,missing=0;array<int,5>layers{};bool timeout=false;
 for(int root=0;root<N;root++){
  if(double(clock()-begin)/CLOCKS_PER_SEC>9.8){timeout=true;break;}fill(dist.begin(),dist.end(),-1);int lo=0,hi=1;queue[0]=root;dist[root]=0;layers={1,0,0,0,0};
  for(int dep=0;dep<4;dep++){int end=hi;while(lo<end){int u=queue[lo++];for(int v:adj[u])if(dist[v]<0){dist[v]=dep+1;queue[hi++]=v;}}layers[dep+1]=hi-end;}roots++;
  if(hi<N){fail=root;missing=N-hi;first=find(dist.begin(),dist.end(),-1)-dist.begin();break;}
 }
 bool hit=!timeout&&fail<0&&roots==N;
 ofstream out(folder+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(hit?"COMPLETE_D4_REQUIRES_PARENT_CHECK":timeout?"UNKNOWN_CPU_LIMIT":"CANONICAL_GRAPH_FIRST_R4_FAILURE")<<"\",\"actual_graphs\":1,\"n\":3705,\"m\":19500,\"Delta\":11,\"simple\":true,\"undirected\":true,\"degree_histogram\":{\"10\":1755,\"11\":1950},\"R4_roots_checked\":"<<roots<<",\"failed_source\":"<<fail<<",\"first_missing_target\":"<<first<<",\"failed_root_R4_missing\":"<<missing<<",\"layers\":[";for(int i=0;i<5;i++){if(i)out<<',';out<<layers[i];}out<<"],\"actual_D\":";if(timeout)out<<"null";else out<<(hit?4:5);out<<",\"diameter_scope\":\""<<(hit?"All3705actualrootsR4":"FirstactualR4counterexampleplusuniversalupper5")<<"\",\"ordinary_bad_unordered_pairs\":null,\"native_CPU_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC<<"}\n";
 if(fail>=0){ofstream misses(folder+"/FIRST_FAILURE.json");misses<<"{\"source\":"<<fail<<",\"source_type\":\""<<(fail<1755?"point":fail<3510?"line":"twin")<<"\",\"first_target\":"<<first<<",\"target_type\":\""<<(first<1755?"point":first<3510?"line":"twin")<<"\",\"missing_vertices\":[";bool comma=false;for(int v=0;v<N;v++)if(dist[v]<0){if(comma)misses<<',';comma=true;misses<<v;}misses<<"]}\n";}
 if(hit){ofstream e(folder+"/graph_d11_D4_n3705.edges");e<<N<<" 19500\n";int count=0;for(int u=0;u<N;u++)for(int v:adj[u])if(u<v){e<<u<<' '<<v<<'\n';count++;}assert(count==19500);}
 cout<<"phasehist="<<hist[0]<<','<<hist[1]<<','<<hist[2]<<" roots="<<roots<<" missing="<<missing<<" hit="<<hit<<" nativeCPU="<<double(clock()-begin)/CLOCKS_PER_SEC<<endl;
}
