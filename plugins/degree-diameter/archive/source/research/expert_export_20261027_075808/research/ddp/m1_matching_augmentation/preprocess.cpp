// Baseline distances and exact distance-5 pairs spoiled by deleting one old edge.
#include <algorithm>
#include <array>
#include <chrono>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>
using namespace std;
int main(int argc,char**argv){
 if(argc!=3)return 2;auto start=chrono::steady_clock::now();clock_t cpu_start=clock();
 ifstream in(argv[1]);int n,m;in>>n>>m;if(n!=2810||m!=9835)return 2;
 vector<pair<int,int>>edges(m);vector<vector<pair<int,int>>>adj(n);
 for(int eid=0;eid<m;eid++){auto&[u,v]=edges[eid];in>>u>>v;adj[u].emplace_back(v,eid);adj[v].emplace_back(u,eid);}
 for(auto&a:adj)if(a.size()!=7)return 2;
 vector<unsigned char>matrix(n*n);vector<int>queue(n);vector<long long>critical(m);
 vector<array<int,5>>common(n);vector<int>size(n);long long distance5=0;
 for(int root=0;root<n;root++){
  auto*d=&matrix[root*n];fill(d,d+n,255);int head=0,end=1;queue[0]=root;d[root]=0;size[root]=0;
  while(head<end){int u=queue[head++];for(auto[v,eid]:adj[u])if(d[v]==255){d[v]=d[u]+1;queue[end++]=v;}}
  if(end!=n||*max_element(d,d+n)!=5)return 2;
  for(int j=1;j<n;j++){
   int v=queue[j];bool first=true;
   for(auto[u,eid]:adj[v])if(d[u]+1==d[v]){
    if(first){size[v]=size[u];copy_n(common[u].begin(),size[u],common[v].begin());common[v][size[v]++]=eid;first=false;}
    else{
     int count=0;for(int k=0;k<size[v];k++){
      int e=common[v][k];bool present=e==eid;
      for(int t=0;t<size[u]&&!present;t++)present=common[u][t]==e;
      if(present)common[v][count++]=e;
     }size[v]=count;
    }
   }
   if(d[v]==5){distance5++;for(int k=0;k<size[v];k++)critical[common[v][k]]++;}
  }
 }
 string prefix=argv[2];ofstream raw(prefix+".distances.u8",ios::binary);raw.write((char*)matrix.data(),matrix.size());raw.close();
 ofstream edgeout(prefix+".edge_critical5.txt");map<long long,int>hist;
 for(int eid=0;eid<m;eid++){
  if(critical[eid]%2)return 2;critical[eid]/=2;hist[critical[eid]]++;
  edgeout<<edges[eid].first<<" "<<edges[eid].second<<" "<<critical[eid]<<"\n";
 }
 double cpu=double(clock()-cpu_start)/CLOCKS_PER_SEC;
 double wall=chrono::duration<double>(chrono::steady_clock::now()-start).count();
 ofstream out(prefix+".preprocess.json");out<<"{\"n\":"<<n<<",\"edges\":"<<m<<",\"distance5_unordered_pairs\":"<<distance5/2<<",\"critical5_count_histogram\":{";
 bool comma=false;for(auto[c,count]:hist){out<<(comma?",":"")<<"\""<<c<<"\":"<<count;comma=true;}
 out<<"},\"cpu_seconds\":"<<cpu<<",\"wall_seconds\":"<<wall<<"}\n";
 cout<<"baseline distances complete; critical5 min "<<hist.begin()->first<<" max "<<hist.rbegin()->first<<" cpu "<<cpu<<" wall "<<wall<<endl;
}
