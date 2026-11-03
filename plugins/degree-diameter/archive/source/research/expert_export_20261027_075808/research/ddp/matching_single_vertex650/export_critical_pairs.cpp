// Export existing 650-source single-edge damage pairs; no construction or search.
#include <algorithm>
#include <array>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <stdexcept>
#include <string>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 try{
  if(argc!=4)throw runtime_error("usage: SOURCE_EDGES OUTPUT_DIRECTORY CPU_LIMIT");
  auto start=chrono::steady_clock::now();clock_t cpu_start=clock();
  auto cpu=[&](){return double(clock()-cpu_start)/CLOCKS_PER_SEC;};double limit=stod(argv[3]);
  ifstream input(argv[1]);int n,m;if(!(input>>n>>m)||n!=650||m!=1625)throw runtime_error("expected source header 650 1625");
  vector<pair<int,int>>edges(m);vector<vector<pair<int,int>>>adj(n);set<pair<int,int>>unique;
  for(int e=0;e<m;++e){auto&[u,v]=edges[e];if(!(input>>u>>v)||u<0||u>=v||v>=n||!unique.insert({u,v}).second)throw runtime_error("invalid edge");
   adj[u].emplace_back(v,e);adj[v].emplace_back(u,e);}
  string extra;if(input>>extra)throw runtime_error("extra edge input");for(auto&row:adj)if(row.size()!=5)throw runtime_error("not regular five");
  vector<unsigned char>matrix(size_t(n)*n);vector<int>queue(n),ball3(n),ball4(n);
  vector<vector<int>>critical(m);vector<long long>damage(m);vector<array<long long,6>>by_distance(m);
  vector<array<int,5>>prev(n),next(n);vector<int>ps(n),ns(n);
  int diameter=0;
  for(int root=0;root<n;++root){
   if(cpu()>limit)throw runtime_error("CPU_LIMIT before completion");
   auto*d=matrix.data()+size_t(root)*n;fill(d,d+n,255);int head=0,end=1;queue[0]=root;d[root]=0;
   while(head<end){int u=queue[head++];for(auto[v,e]:adj[u])if(d[v]==255){d[v]=d[u]+1;queue[end++]=v;}}
   if(end!=n)throw runtime_error("source disconnected");
   for(int v=0;v<n;++v){if(d[v]>5)throw runtime_error("source diameter exceeds five");diameter=max(diameter,int(d[v]));ball3[root]+=d[v]<=3;ball4[root]+=d[v]<=4;}
   fill(ps.begin(),ps.end(),0);
   for(int k=1;k<=5;++k){
    for(int v=0;v<n;++v){
     if(d[v]>k){ns[v]=0;continue;}bool first=d[v]>k-1;
     if(!first){ns[v]=ps[v];copy_n(prev[v].begin(),ps[v],next[v].begin());if(ns[v]==0)continue;}
     for(auto[u,eid]:adj[v])if(d[u]<=k-1){
      if(first){ns[v]=ps[u];copy_n(prev[u].begin(),ps[u],next[v].begin());
       bool present=false;for(int j=0;j<ns[v];++j)present|=next[v][j]==eid;if(!present)next[v][ns[v]++]=eid;first=false;
      }else{int keep=0;for(int j=0;j<ns[v];++j){int e=next[v][j];bool present=e==eid;
        for(int t=0;t<ps[u]&&!present;++t)present=prev[u][t]==e;if(present)next[v][keep++]=e;}ns[v]=keep;}
      if(ns[v]==0)break;
     }
     if(first)throw runtime_error("no reachable predecessor");
    }prev.swap(next);ps.swap(ns);
   }
   for(int v=root+1;v<n;++v)for(int j=0;j<ps[v];++j){int e=prev[v][j];damage[e]++;critical[e].push_back(root*n+v);by_distance[e][d[v]]++;}
  }
  string directory=argv[2];long long total=0;for(auto&row:critical)total+=row.size();
  ofstream output(directory+"/critical_upto5_pairs.txt");output<<n<<" "<<m<<" "<<total<<"\n";
  for(int eid=0;eid<m;++eid){
   if(!is_sorted(critical[eid].begin(),critical[eid].end())||adjacent_find(critical[eid].begin(),critical[eid].end())!=critical[eid].end())throw runtime_error("pair list order");
   output<<eid<<" "<<critical[eid].size();for(int code:critical[eid])output<<" "<<code;output<<"\n";
  }output.close();
  double used=cpu(),wall=chrono::duration<double>(chrono::steady_clock::now()-start).count();
  ofstream summary(directory+"/critical_export.json");summary<<"{\"status\":\"COMPLETE\",\"n\":"<<n<<",\"m\":"<<m
   <<",\"total_incidences\":"<<total<<",\"all_lists_sorted_unique\":true,\"cpu_seconds\":"<<used<<",\"wall_seconds\":"<<wall<<"}\n";
  cout<<"COMPLETE total_incidences="<<total<<" cpu="<<used<<" wall="<<wall<<endl;
 }catch(const exception&e){cerr<<e.what()<<"\n";return 2;}
 return 0;
}
