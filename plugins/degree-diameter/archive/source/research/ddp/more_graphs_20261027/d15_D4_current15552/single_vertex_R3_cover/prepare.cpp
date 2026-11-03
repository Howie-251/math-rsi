#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
int main(int argc,char**argv){assert(argc==3);double start=cpu();string source=argv[1],out=argv[2];ifstream f(source);int n,m;f>>n>>m;assert(n==15552&&m==116316);
 vector<vector<int>>adj(n);for(int i=0,u,v;i<m;i++){f>>u>>v;adj[u].push_back(v);adj[v].push_back(u);}
 vector<int>free;for(int v=0;v<n;v++)if(adj[v].size()<15){assert(adj[v].size()==14);free.push_back(v);}assert(free.size()==648);
 int W=(n+63)/64;assert(W==243);ofstream mask(out+"/R3_MASKS.bin",ios::binary);uint32_t h[3]={(uint32_t)free.size(),(uint32_t)n,(uint32_t)W};mask.write((char*)h,sizeof h);
 vector<int>stamp(n),depth(n),queue(n),support(n),ptr={0},indices;indices.reserve(2000000);map<int,int>sizes;bool limited=false;int done=0;
 for(int root:free){if(cpu()-start>2.8){limited=true;break;}int gen=done+1,lo=0,hi=0;vector<uint64_t>ball(W);stamp[root]=gen;depth[root]=0;queue[hi++]=root;ball[root/64]|=1ULL<<(root%64);
  while(lo<hi){int u=queue[lo++];if(depth[u]==3)continue;for(int v:adj[u])if(stamp[v]!=gen){stamp[v]=gen;depth[v]=depth[u]+1;queue[hi++]=v;ball[v/64]|=1ULL<<(v%64);}}
  sizes[hi]++;for(int i=0;i<hi;i++)support[queue[i]]++;
  uint32_t vertex=root;mask.write((char*)&vertex,4);mask.write((char*)ball.data(),W*8);
  for(int w=0;w<W;w++){uint64_t bits=ball[w];while(bits){int b=__builtin_ctzll(bits);indices.push_back(64*w+b);bits&=bits-1;}}ptr.push_back(indices.size());++done;
 }
 mask.close();if(!limited){ofstream csc(out+"/COVER_CSC.bin",ios::binary);uint32_t hdr[3]={(uint32_t)n,(uint32_t)free.size(),(uint32_t)indices.size()};csc.write((char*)hdr,12);csc.write((char*)ptr.data(),ptr.size()*4);csc.write((char*)indices.data(),indices.size()*4);}
 ofstream r(out+"/PREPARATION_RESULT.json");int covered=count_if(support.begin(),support.end(),[](int x){return x>0;});int mins=*min_element(support.begin(),support.end()),maxs=*max_element(support.begin(),support.end());
 r<<"{\"status\":\""<<(limited?"CPU_LIMITED_PARTIAL":"ALL648_SOURCE_R3_COMPLETE")<<"\",\"source_n\":"<<n<<",\"source_m\":"<<m<<",\"eligible_count\":648,\"balls_prepared\":"<<done<<",\"allfree_union_covered\":"<<covered<<",\"allfree_union_missing\":"<<n-covered<<",\"minimum_target_support\":"<<mins<<",\"maximum_target_support\":"<<maxs<<",\"matrix_nonzeros\":"<<indices.size()<<",\"CPU_seconds\":"<<cpu()-start<<",\"CPU_limited\":"<<(limited?"true":"false")<<",\"ball_size_histogram\":{";bool first=true;for(auto[a,b]:sizes){if(!first)r<<',';first=false;r<<'\"'<<a<<"\":"<<b;}r<<"},\"missing_vertices\":[";first=true;for(int v=0;v<n;v++)if(!support[v]){if(!first)r<<',';first=false;r<<v;}r<<"],\"eligible_vertices\":[";for(int k=0;k<(int)free.size();k++){if(k)r<<',';r<<free[k];}r<<"],\"target_support\":[";for(int v=0;v<n;v++){if(v)r<<',';r<<support[v];}r<<"]}\n";
 cerr<<"PREP done "<<done<<" union "<<covered<<"/"<<n<<" nnz "<<indices.size()<<" support "<<mins<<".."<<maxs<<" CPU "<<cpu()-start<<'\n';
}
