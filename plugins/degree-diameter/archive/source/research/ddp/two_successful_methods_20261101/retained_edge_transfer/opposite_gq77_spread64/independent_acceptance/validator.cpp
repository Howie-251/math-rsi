#include <algorithm>
#include <array>
#include <chrono>
#include <ctime>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
using Vec = array<int,4>;
using Line = array<int,8>;
const int NP=400, OLD=160000, N=160050, DEG=64;
const long long M=5121600;
int mod(int a) {a%=7;return a<0?a+7:a;}
void require(bool b,const string& s) {if(!b) throw runtime_error(s);}
int inv(int a) {for(int b=1;b<7;b++)if(a*b%7==1)return b;throw runtime_error("zero inverse");}
Vec canonical(Vec v) {for(int a:v)if(a){int k=inv(a);for(int& b:v)b=b*k%7;return v;}throw runtime_error("zero vector canonicalization");}
int B(const Vec&a,const Vec&b) {return mod(a[0]*b[2]+3*a[1]*b[3]-a[2]*b[0]-3*a[3]*b[1]);}
double cpu() {return double(clock())/CLOCKS_PER_SEC;}
struct Geometry {
 vector<Vec> pts; map<Vec,int> pointID; vector<Line> lines;
 array<vector<int>,400> through;
 bool inc[400][400]{};
 int common[400][400];
 array<int,50> spread{}; array<int,400> owner{};
 int rref=0, flags=0, projection=0, incidentProjection=0, uniqueProjection=0;
 int linePairDisjoint=0,linePairMeet=0;
 double seconds=0;
 Geometry() {
  double t=cpu();
  // A fresh enumeration of all canonical projective points.
  for(int a=0;a<7;a++)for(int b=0;b<7;b++)for(int c=0;c<7;c++)for(int d=0;d<7;d++){
   Vec v={a,b,c,d}; bool seen=false,good=false;
   for(int z:v)if(z){seen=true;good=z==1;break;}
   if(seen&&good)pts.push_back(v);
  }
  require(pts.size()==400,"projective point count");
  require(is_sorted(pts.begin(),pts.end()),"point ordering");
  for(int i=0;i<400;i++)pointID[pts[i]]=i;
  // Every rank-two subspace has exactly one 2x4 reduced row-echelon matrix.
  for(int p=0;p<4;p++)for(int q=p+1;q<4;q++){
   array<Vec,2> rows{};rows[0][p]=1;rows[1][q]=1;
   vector<pair<int,int>> freeCells;
   for(int c=p+1;c<4;c++)if(c!=q)freeCells.push_back({0,c});
   for(int c=q+1;c<4;c++)freeCells.push_back({1,c});
   function<void(int)> rec=[&](int k){
    if(k<(int)freeCells.size()) {auto [r,c]=freeCells[k];for(int x=0;x<7;x++){rows[r][c]=x;rec(k+1);}return;}
    rref++;
    if(B(rows[0],rows[1])!=0)return;
    Line line{};
    for(int s=0;s<8;s++){
     Vec v{};int a=s==7?0:1,b=s==7?1:s;
     for(int c=0;c<4;c++)v[c]=mod(a*rows[0][c]+b*rows[1][c]);
     line[s]=pointID.at(canonical(v));
    }
    sort(line.begin(),line.end());
    require(adjacent_find(line.begin(),line.end())==line.end(),"line repeats point");
    // Independent pairwise total isotropy of the resulting point set.
    for(int a:line)for(int b:line)require(B(pts[a],pts[b])==0,"nonisotropic retained line");
    lines.push_back(line);
   };rec(0);
  }
  require(rref==2850,"all RREF rank-two subspaces count");
  sort(lines.begin(),lines.end());
  require(lines.size()==400,"isotropic line count");
  require(adjacent_find(lines.begin(),lines.end())==lines.end(),"repeated isotropic line");
  for(auto &row:common)fill(begin(row),end(row),-1);
  for(int l=0;l<400;l++)for(int p:lines[l]){inc[p][l]=true;through[p].push_back(l);flags++;}
  require(flags==3200,"flag count");
  for(int p=0;p<400;p++)require(through[p].size()==8,"through-point line count");
  for(int l=0;l<400;l++)for(int p:lines[l])for(int q:lines[l])if(p!=q){
   require(common[p][q]<0,"two points on multiple lines");common[p][q]=l;
  }
  for(int l=0;l<400;l++)for(int m=l+1;m<400;m++){
   int k=0;for(int p:lines[l])k+=inc[p][m];
   require(k<=1,"distinct lines meet twice");
   if(k)linePairMeet++;else linePairDisjoint++;
  }
  // Full finite project premise, with uniqueness checked as an extra GQ condition.
  for(int p=0;p<400;p++)for(int l=0;l<400;l++){
   int qCount=0;
   for(int q:lines[l]){
    int m=p==q?through[p][0]:common[p][q];
    if(m>=0){require(inc[q][l]&&inc[p][m]&&inc[q][m],"projection witness");qCount++;}
   }
   require(qCount>0,"missing point-line projection");projection++;
   if(inc[p][l]){require(qCount==8,"incident projection witness count");incidentProjection++;}
   else {require(qCount==1,"nonincident projection is not unique");uniqueProjection++;}
  }
  // Desarguesian spread computed independently by GF49 multiplication, beta^2=3.
  map<Line,int> lineID;for(int l=0;l<400;l++)lineID[lines[l]]=l;
  owner.fill(-1);
  for(int j=0;j<50;j++){
   vector<int> lp;
   for(int p=0;p<400;p++){
    auto v=pts[p];bool on;
    if(j==49)on=v[0]==0&&v[1]==0;
    else {int a=j%7,b=j/7;on=v[2]==mod(a*v[0]+3*b*v[1])&&v[3]==mod(b*v[0]+a*v[1]);}
    if(on)lp.push_back(p);
   }
   require(lp.size()==8,"spread line has wrong point count");Line key{};copy(lp.begin(),lp.end(),key.begin());
   require(lineID.count(key)==1,"spread line absent from isotropic geometry");spread[j]=lineID.at(key);
   for(int p:lp){require(owner[p]==-1,"spread points overlap");owner[p]=j;}
  }
  for(int p=0;p<400;p++)require(owner[p]>=0,"spread fails to cover point");
  // Formula-degree computation covers every old vertex; every pair (q,m) is distinct.
  long long oldDegreeSum=0,oldFormulaEdgesTwice=0,newDegreeSum=0;
  for(int p=0;p<400;p++)for(int l=0;l<400;l++){
   int d=0;for(int q:lines[l])for(int m:through[p])if(q!=p||m!=l)d++;
   require(d==64-int(inc[p][l]),"old formula degree");oldFormulaEdgesTwice+=d;
   if(inc[p][l]){require(inc[p][spread[owner[p]]],"spread owner incidence");d++;}
   require(d==64,"augmented old formula degree");oldDegreeSum+=d;
  }
  for(int j=0;j<50;j++){
   int d=0;for(int p:lines[spread[j]])for(int l:through[p]){require(inc[p][l],"pin flag");d++;}
   require(d==64,"new formula degree");newDegreeSum+=d;
  }
  require(oldFormulaEdgesTwice/2==5118400,"source edge count");
  require(oldDegreeSum+newDegreeSum==2*M,"formula augmented edge count");
  seconds=cpu()-t;
 }
 bool allowed(int u,int v)const{
  if(u<OLD&&v<OLD){int p=u/400,l=u%400,q=v/400,m=v%400;return u!=v&&inc[p][m]&&inc[q][l];}
  if(u>=OLD&&v>=OLD)return false;
  int x=u<OLD?u:v,j=(u>=OLD?u:v)-OLD,p=x/400,l=x%400;
  return inc[p][l]&&owner[p]==j;
 }
 void save(const string&path)const{
  ofstream f(path);require(bool(f),"open geometry record");
  f<<"Independent canonical PG(3,7) points, coordinates u0 u1 v0 v1\n";
  for(int i=0;i<400;i++)f<<"P "<<i<<" "<<pts[i][0]<<" "<<pts[i][1]<<" "<<pts[i][2]<<" "<<pts[i][3]<<"\n";
  f<<"Independent lexicographically sorted isotropic line point IDs\n";
  for(int l=0;l<400;l++){f<<"L "<<l;for(int p:lines[l])f<<" "<<p;f<<"\n";}
  f<<"Ordered GF49 slopes 0..48 and infinity 49 mapped to line IDs\n";
  for(int j=0;j<50;j++)f<<"S "<<j<<" "<<spread[j]<<"\n";
 }
};
int main(int argc,char**argv){
 double start=cpu();
 try{
  require(argc==3||argc==4,"usage: validator --geometry-only geometry.txt OR validator edgefile geometry.txt bfs.csv");
  Geometry g;g.save(argv[2]);
  if(string(argv[1])=="--geometry-only"){
   cout<<"{\"status\":\"GEOMETRY_PREMISES_PASS_LITERAL_PENDING\",\"points\":400,\"RREF_subspaces\":"<<g.rref<<",\"lines\":400,\"flags\":"<<g.flags<<",\"projection_obligations\":"<<g.projection<<",\"nonincident_unique_projections\":"<<g.uniqueProjection<<",\"incident_projection_obligations\":"<<g.incidentProjection<<",\"spread_lines\":50,\"formula_degree\":64,\"CPU_seconds\":"<<cpu()-start<<"}\n";return 0;
  }
  require(argc==4,"missing BFS output");
  ifstream f(argv[1]);require(bool(f),"edge file is unavailable");
  string header;require(bool(getline(f,header)),"missing header");
  // The literal graph contract is a numeric n m header, optionally prefixed '#'.
  string numeric=header;if(!numeric.empty()&&numeric[0]=='#')numeric=numeric.substr(1);
  istringstream hs(numeric);long long hn,hm;string extra;
  require(bool(hs>>hn>>hm)&&!(hs>>extra)&&hn==N&&hm==M,"header must declare 160050 5121600");
  vector<array<int,64>> adj(N);vector<int> deg(N,0);
  long long edges=0,oldEdges=0,pinEdges=0;int pu=-1,pv=-1,u,v;
  double parseStart=cpu();
  string edgeLine;
  while(getline(f,edgeLine)){
   istringstream row(edgeLine);string trailing;
   require(bool(row>>u>>v)&&!(row>>trailing),"each edge line must contain exactly two integer endpoints");
   require(0<=u&&u<v&&v<N,"invalid endpoint, ordering, or loop");
   require(u>pu||(u==pu&&v>pv),"edge order not strict lexicographic; duplicate or out-of-order edge");
   require(g.allowed(u,v),"literal edge violates independent formula");
   require(deg[u]<64&&deg[v]<64,"literal degree exceeds 64");
   adj[u][deg[u]++]=v;adj[v][deg[v]++]=u;pu=u;pv=v;edges++;
   if(v<OLD)oldEdges++;else pinEdges++;
  }
  require(f.eof(),"nonnumeric trailing edge data");
  require(edges==M&&oldEdges==5118400&&pinEdges==3200,"literal edge counts");
  for(int x=0;x<N;x++)require(deg[x]==64,"literal degree is not 64");
  double parseSeconds=cpu()-parseStart;
  // Formula graph has degree exactly 64 everywhere.  A literal allowed subset
  // of equal degree at each vertex is therefore exactly that formula graph.
  ofstream bfs(argv[3]);require(bool(bfs),"open BFS record");bfs<<"root,reach_R3,d0,d1,d2,d3,eccentricity\n";
  vector<int> seen(N,0),queue(N),depth(N);double bfsStart=cpu();int roots=0;
  int mind2=N,maxd2=0;
  for(int r=OLD;r<N;r++){
   int stamp=r-OLD+1,head=0,tail=1;queue[0]=r;seen[r]=stamp;depth[r]=0;array<int,4> hist{};hist[0]=1;
   while(head<tail){int x=queue[head++];if(depth[x]==3)continue;
    for(int y:adj[x])if(seen[y]!=stamp){seen[y]=stamp;depth[y]=depth[x]+1;hist[depth[y]]++;queue[tail++]=y;}
   }
   require(tail==N,"new-root literal R3 misses vertices");require(hist[3]>0,"new-root eccentricity unexpectedly at most 2");
   bfs<<r<<","<<tail;for(int k:hist)bfs<<","<<k;bfs<<",3\n";
   mind2=min(mind2,hist[2]);maxd2=max(maxd2,hist[2]);roots++;
  }
  double bfsSeconds=cpu()-bfsStart;
  require(N>1+64+64*64,"diameter lower bound capacity");
  cout<<"{\n  \"status\": \"PASS\",\n  \"validation_kind\": \"fresh independent finite geometry, exact literal formula binding, conditional general short-walk proof instantiated mathematically, and all new-root literal BFS\",\n";
  cout<<"  \"vertices\": "<<N<<",\n  \"edges\": "<<edges<<",\n  \"old_edges\": "<<oldEdges<<",\n  \"pin_edges\": "<<pinEdges<<",\n  \"degree_min\": 64,\n  \"degree_max\": 64,\n  \"points\": 400,\n  \"RREF_subspaces\": "<<g.rref<<",\n  \"isotropic_lines\": 400,\n  \"points_per_line\": 8,\n  \"lines_per_point\": 8,\n  \"flags\": "<<g.flags<<",\n";
  cout<<"  \"line_pairs_meeting_once\": "<<g.linePairMeet<<",\n  \"line_pairs_disjoint\": "<<g.linePairDisjoint<<",\n  \"projection_obligations\": "<<g.projection<<",\n  \"nonincident_unique_projections\": "<<g.uniqueProjection<<",\n  \"incident_projection_obligations\": "<<g.incidentProjection<<",\n  \"spread_lines\": 50,\n  \"spread_owners_per_point\": 1,\n  \"formula_degree_every_vertex\": 64,\n  \"literal_formula_equality\": true,\n";
  cout<<"  \"literal_BFS_roots\": "<<roots<<",\n  \"literal_BFS_scope\": \"new vertices 160000 through 160049 only; no old-root BFS\",\n  \"literal_BFS_reach_each\": 160050,\n  \"literal_BFS_d2_min\": "<<mind2<<",\n  \"literal_BFS_d2_max\": "<<maxd2<<",\n  \"all_pairs_D3_upper_bound\": \"independent full finite geometry premises plus reusable general old-old/old-new/new-new short walks, not inferred from 50 BFS roots\",\n  \"diameter_exact\": 3,\n  \"radius_two_capacity_upper_bound\": 4161,\n  \"concrete_Lean_build_performed\": false,\n  \"public_priority_or_world_record_claimed\": false,\n";
  cout<<"  \"CPU_seconds\": {\"geometry\": "<<g.seconds<<", \"literal_parse_and_binding\": "<<parseSeconds<<", \"new_root_BFS\": "<<bfsSeconds<<", \"whole_validator\": "<<cpu()-start<<"}\n}\n";
 }catch(const exception&e){cerr<<"FAIL: "<<e.what()<<"; CPU="<<cpu()-start<<"\n";return 1;}
}
