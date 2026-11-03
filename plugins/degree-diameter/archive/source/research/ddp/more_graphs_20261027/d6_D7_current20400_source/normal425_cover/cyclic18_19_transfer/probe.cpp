#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
struct Dart{int to,a,b,c,reverse;};
int main(int argc,char**argv){
 clock_t begin=clock();string dir=argv[2];ifstream ports(argv[1]);array<array<Dart,6>,48>base;
 for(int v=0;v<48;v++)for(int k=0;k<6;k++){auto&d=base[v][k];ports>>d.to>>d.a>>d.b>>d.c>>d.reverse;assert(ports);assert(0<=d.to&&d.to<48&&0<=d.a&&d.a<5&&0<=d.b&&d.b<5&&-8<=d.c&&d.c<=8);}
 for(int v=0;v<48;v++)for(int k=0;k<6;k++){auto d=base[v][k],e=base[d.to][d.reverse];assert(e.to==v&&(d.a+e.a)%5==0&&(d.b+e.b)%5==0&&d.c+e.c==0);}
 vector<int>ms;for(int i=3;i<argc;i++)ms.push_back(stoi(argv[i]));
 vector<string>rows;bool hit=false;
 for(int m:ms){
  const clock_t one=clock();assert(m==18||m==19);int order=25*m,n=48*order;
  vector<array<int,6>>adj(n);for(int v=0;v<48;v++)for(int z=0;z<m;z++)for(int y=0;y<5;y++)for(int x=0;x<5;x++){
   int u=v*order+x+5*y+25*z;for(int k=0;k<6;k++){auto d=base[v][k];adj[u][k]=d.to*order+(x+d.a)%5+5*((y+d.b)%5)+25*((z+d.c+m)%m);}
   auto a=adj[u];sort(a.begin(),a.end());assert(adjacent_find(a.begin(),a.end())==a.end()&&find(a.begin(),a.end(),u)==a.end());}
  for(int u=0;u<n;u++)for(int v:adj[u])assert(find(adj[v].begin(),adj[v].end(),u)!=adj[v].end());
  int checked=0,failed=-1,missing=0,visited=0;vector<int>eccs;
  for(int rb=0;rb<48;rb++){
   vector<int>d(n,-1),parent(n,-1),q(n);int lo=0,hi=0,root=rb*order;d[root]=0;q[hi++]=root;
   while(lo<hi){int u=q[lo++];for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;parent[v]=u;q[hi++]=v;}}
   ++checked;visited=hi;int ecc=*max_element(d.begin(),d.end());eccs.push_back(ecc);missing=count_if(d.begin(),d.end(),[](int z){return z<0||z>7;});
   if(missing){
    failed=rb;ofstream witness(dir+"/m"+to_string(m)+"_first_failed_root.json");
    witness<<"{\"m\":"<<m<<",\"root_base\":"<<rb<<",\"root\":"<<root<<",\"visited\":"<<hi<<",\"eccentricity\":"<<ecc<<",\"radius7_missing\":"<<missing<<",\"missing_by_end_base\":[";
    for(int vb=0;vb<48;vb++){if(vb)witness<<',';int count=0;for(int j=0;j<order;j++)count+=d[vb*order+j]<0||d[vb*order+j]>7;witness<<count;}
    int target=-1;for(int u=0;u<n;u++)if(d[u]>7){target=u;break;}
    witness<<"],\"first_reachable_failed_target\":"<<target;
    if(target>=0){vector<int>path;for(int u=target;u>=0;u=parent[u])path.push_back(u);reverse(path.begin(),path.end());witness<<",\"exact_distance\":"<<d[target]<<",\"exact_path\":[";for(size_t i=0;i<path.size();i++){if(i)witness<<',';witness<<path[i];}witness<<']';}
    witness<<"}\n";break;
   }
  }
  hit=checked==48&&failed<0;
  ofstream out(dir+"/m"+to_string(m)+"_RESULT.json");out<<"{\"m\":"<<m<<",\"n\":"<<n<<",\"edges\":"<<3*n<<",\"degree\":6,\"simple\":true,\"undirected\":true,\"connected\":"<<(visited==n?"true":"false")<<",\"root_representatives_checked\":"<<checked<<",\"root_eccentricities\":[";
  for(size_t i=0;i<eccs.size();i++){if(i)out<<',';out<<eccs[i];}
  out<<"],\"failed_root_base\":"<<failed<<",\"failed_root_R7_missing\":"<<(hit?0:missing)<<",\"complete_D7\":"<<(hit?"true":"false")<<",\"actual_global_D\":";
  if(hit)out<<*max_element(eccs.begin(),eccs.end());else out<<"null";
  out<<",\"ordinary_bad_unordered_pairs\":"<<(hit?"0":"null")<<",\"edgefile_exported\":"<<(hit?"true":"false")<<",\"native_CPU_seconds\":"<<double(clock()-one)/CLOCKS_PER_SEC<<"}\n";
  rows.push_back("m"+to_string(m)+"_RESULT.json");cout<<"m "<<m<<" hit "<<hit<<" roots "<<checked<<" missing "<<missing<<endl;
  if(hit){ofstream edges(dir+"/graph_d6_D7_n"+to_string(n)+".edges");edges<<n<<' '<<3*n<<'\n';for(int u=0;u<n;u++)for(int v:adj[u])if(u<v)edges<<u<<' '<<v<<'\n';break;}
 }
 ofstream done(dir+"/NATIVE_RESULT.json");done<<"{\"hit\":"<<(hit?"true":"false")<<",\"case_result_files\":[";
 for(size_t i=0;i<rows.size();i++){if(i)done<<',';done<<'\"'<<rows[i]<<'\"';}
 done<<"],\"native_CPU_seconds\":"<<double(clock()-begin)/CLOCKS_PER_SEC<<",\"source_BFS\":0}\n";
}
