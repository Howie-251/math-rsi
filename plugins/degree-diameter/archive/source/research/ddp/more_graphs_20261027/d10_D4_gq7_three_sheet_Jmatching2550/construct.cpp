#include <algorithm>
#include <array>
#include <cassert>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;
using V=array<int,4>;
int md(int a){a%=7;return a<0?a+7:a;}
int inv(int a){for(int b=1;b<7;b++)if(a*b%7==1)return b;assert(false);return 0;}
V norm(V x){int i=0;while(x[i]==0)i++;int z=inv(x[i]);for(int &a:x)a=a*z%7;return x;}
int bil(V x,V y){return md(x[0]*y[2]-x[2]*y[0]+3*(x[1]*y[3]-x[3]*y[1]));}
int main(){
 double started=(double)clock()/CLOCKS_PER_SEC;
 vector<V> points;map<V,int> pid;
 for(int a=0;a<7;a++)for(int b=0;b<7;b++)for(int c=0;c<7;c++)for(int d=0;d<7;d++){
  V p={a,b,c,d};if(a||b||c||d)pid[norm(p)]=0;
 }
 for(auto &[p,id]:pid){id=points.size();points.push_back(p);}assert(points.size()==400);
 set<vector<int>> lset;
 for(int i=0;i<400;i++)for(int j=i+1;j<400;j++)if(bil(points[i],points[j])==0){
  vector<int> l={j};for(int t=0;t<7;t++){V p;for(int k=0;k<4;k++)p[k]=md(points[i][k]+t*points[j][k]);l.push_back(pid.at(norm(p)));}
  sort(l.begin(),l.end());lset.insert(l);
 }
 vector<vector<int>> lines(lset.begin(),lset.end());assert(lines.size()==400);
 map<vector<int>,int> lid;for(int i=0;i<400;i++)lid[lines[i]]=i;
 vector<array<V,2>> bases(400);vector<array<int,2>> pivots(400);
 for(int l=0;l<400;l++){
  array<V,2> b={points[lines[l][0]],points[lines[l][1]]};int row=0;
  for(int col=0;col<4&&row<2;col++){
   int r=row;while(r<2&&b[r][col]==0)r++;if(r==2)continue;swap(b[row],b[r]);int z=inv(b[row][col]);
   for(int k=0;k<4;k++)b[row][k]=b[row][k]*z%7;
   for(int s=0;s<2;s++)if(s!=row){int f=b[s][col];for(int k=0;k<4;k++)b[s][k]=md(b[s][k]-f*b[row][k]);}
   pivots[l][row]=col;row++;
  }assert(row==2);bases[l]=b;
 }
 set<int> spread;
 for(int ta=0;ta<7;ta++)for(int tb=0;tb<7;tb++){
  vector<int> line;for(int a=0;a<7;a++)for(int b=0;b<7;b++)if(a||b){V p={a,b,md(ta*a+3*tb*b),md(ta*b+tb*a)};line.push_back(pid.at(norm(p)));}
  sort(line.begin(),line.end());line.erase(unique(line.begin(),line.end()),line.end());assert(line.size()==8);spread.insert(lid.at(line));
 }
 {vector<int> line;for(int c=0;c<7;c++)for(int d=0;d<7;d++)if(c||d)line.push_back(pid.at(norm({0,0,c,d})));sort(line.begin(),line.end());line.erase(unique(line.begin(),line.end()),line.end());spread.insert(lid.at(line));}
 assert(spread.size()==50);vector<int> memberships(400);
 for(int l:spread)for(int p:lines[l])memberships[p]++;
 for(int a:memberships)assert(a==1);
 vector<int> J(400);for(int p=0;p<400;p++){V x=points[p];J[p]=pid.at(norm({md(3*x[1]),x[0],md(3*x[3]),x[2]}));assert(J[p]!=p);}
 for(int p=0;p<400;p++)assert(J[J[p]]==p);
 for(int l:spread)for(int p:lines[l])assert(binary_search(lines[l].begin(),lines[l].end(),J[p]));
 int chi[7]={-1,0,2,1,1,2,0};vector<vector<int>> adj(2550);set<pair<int,int>> edges;
 auto point=[](int p,int s){return 3*p+s;};auto line=[](int l,int s){return 1200+3*l+s;};
 auto edge=[&](int u,int v){assert(u!=v);if(u>v)swap(u,v);assert(edges.insert({u,v}).second);adj[u].push_back(v);adj[v].push_back(u);};
 vector<map<int,int>> tau(400);
 for(int l=0;l<400;l++){
  for(int p:lines[l]){
   int a=points[p][pivots[l][0]],b=points[p][pivots[l][1]];V recovered;
   for(int k=0;k<4;k++)recovered[k]=md(a*bases[l][0][k]+b*bases[l][1][k]);assert(recovered==points[p]);
   int q=md(a*a-3*b*b);assert(q!=0);tau[l][p]=chi[q];
   for(int s=0;s<3;s++)edge(point(p,s),line(l,(s+chi[q])%3));
  }
  for(int s=0;s<3;s++)for(int t=s+1;t<3;t++)edge(line(l,s),line(l,t));
 }
 int tindex=0;for(int l:spread){
  for(int s=0;s<3;s++)for(int p:lines[l])edge(2400+3*tindex+s,point(p,(s-tau[l][p]+6)%3));
  for(int s=0;s<3;s++)for(int t=s+1;t<3;t++)edge(2400+3*tindex+s,2400+3*tindex+t);
  tindex++;
 }
 for(int p=0;p<400;p++)if(p<J[p])for(int s=0;s<3;s++)edge(point(p,s),point(J[p],s));
 assert(edges.size()==12750);for(int v=0;v<2550;v++){assert(adj[v].size()==10);sort(adj[v].begin(),adj[v].end());}
 // Count the whole analytically repaired point-pair class, not a score for followup search.
 int classpairs=0;for(int p=0;p<400;p++)for(int r=p+1;r<400;r++)if(bil(points[p],points[r])&&bil(points[J[p]],points[r])==0)classpairs++;
 vector<int> dist(2550),queue(2550);int checked=0,failroot=-1,firstmiss=-1,misscount=0;array<int,5> shell={};
 for(int root=0;root<2550;root++){
  fill(dist.begin(),dist.end(),-1);int begin=0,end=1;queue[0]=root;dist[root]=0;
  while(begin<end){int u=queue[begin++];if(dist[u]==4)continue;for(int v:adj[u])if(dist[v]<0){dist[v]=dist[u]+1;queue[end++]=v;}}
  checked++;if(end<2550){failroot=root;misscount=2550-end;for(int v=0;v<2550;v++)if(dist[v]<0){if(firstmiss<0)firstmiss=v;}else shell[dist[v]]++;break;}
 }
 ofstream geometry("GEOMETRY.json");geometry<<"{\"q\":7,\"point_count\":400,\"line_count\":400,\"spread_line_count\":50,\"J_repaired_opposite_point_pairs_unordered\":"<<classpairs<<",\"point_coordinates\":[";
 for(int p=0;p<400;p++){if(p)geometry<<",";geometry<<"[";for(int k=0;k<4;k++){if(k)geometry<<",";geometry<<points[p][k];}geometry<<"]";}geometry<<"],\"spread_line_ids\":[";int c=0;for(int l:spread){if(c++)geometry<<",";geometry<<l;}geometry<<"]}\n";
 cout<<"{\"n\":2550,\"m\":12750,\"Delta\":10,\"simple\":true,\"undirected\":true,\"regular\":true,\"roots_checked\":"<<checked<<",\"first_failure_root\":"<<failroot<<",\"first_R4_missing_target\":"<<firstmiss<<",\"R4_missing_target_count\":"<<misscount<<",\"layer_counts\":[";
 for(int i=0;i<5;i++){if(i)cout<<",";cout<<shell[i];}cout<<"],\"global_diameter\":"<<(failroot>=0?5:4)<<",\"diameter_basis\":\"fixed_line_fibre_and_twins_universal_upper5; actual_R4_lower_or_allroots_upper4\",\"J_repaired_opposite_point_pairs_unordered\":"<<classpairs<<",\"native_CPU_seconds\":"<<((double)clock()/CLOCKS_PER_SEC-started)<<"}\n";
 if(failroot<0){ofstream out("graph2550.edges");out<<"2550 12750\n";for(auto [u,v]:edges)out<<u<<" "<<v<<"\n";}
}
