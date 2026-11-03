#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
#include <stdexcept>
#include <sstream>
#include <string>
#include <sys/resource.h>
using namespace std;
constexpr int N=6804,D=13,W=(N+63)/64;
using Bits=array<uint64_t,W>;
int main(int argc,char**argv){
 rlimit lim{2,2};setrlimit(RLIMIT_CPU,&lim);clock_t t=clock();
 try{
 ifstream f(argv[1]);int m=0;string line;vector<vector<int>>adj(N);
 while(getline(f,line)){if(line.empty()||line[0]=='#')continue;istringstream row(line);int u,v;if(!(row>>u>>v))throw runtime_error("source pair format");if(u<0||u>=N||v<0||v>=N||u==v)throw runtime_error("source label");adj[u].push_back(v);adj[v].push_back(u);m++;}if(m!=44226)throw runtime_error("source edge count binding");
 vector<Bits>r1(N),r2(N),r3(N);
 auto count=[](const Bits&b){int z=0;for(auto x:b)z+=__builtin_popcountll(x);return z;};
 for(int u=0;u<N;u++){if(adj[u].size()!=D)throw runtime_error("source degree binding");r1[u][u/64]|=1ULL<<(u%64);for(int v:adj[u])r1[u][v/64]|=1ULL<<(v%64);}
 int b2max=0,s2max=0,b3max=0,s3max=0;
 for(int u=0;u<N;u++){r2[u]=r1[u];for(int v:adj[u])for(int w=0;w<W;w++)r2[u][w]|=r1[v][w];b2max=max(b2max,count(r2[u]));s2max=max(s2max,count(r2[u])-count(r1[u]));}
 for(int u=0;u<N;u++){r3[u]=r2[u];for(int v:adj[u])for(int w=0;w<W;w++)r3[u][w]|=r2[v][w];b3max=max(b3max,count(r3[u]));s3max=max(s3max,count(r3[u])-count(r2[u]));}
 int upper=b3max+D*b2max+s2max*(D+1)+s3max;
 ofstream shell("OVERLAP_SHELL_PROFILES.tsv");shell<<"source_root\tB1\tB2\tB3\tS2\tS3\n";for(int u=0;u<N;u++)shell<<u<<'\t'<<count(r1[u])<<'\t'<<count(r2[u])<<'\t'<<count(r3[u])<<'\t'<<count(r2[u])-count(r1[u])<<'\t'<<count(r3[u])-count(r2[u])<<'\n';shell.close();
 ofstream hist("OVERLAP_ROOT_RESULTS.tsv");hist<<"source_root\tsum13smallest\tunion_upper\tchecked_other_centres\n";
 int witness=-1,best=-1,checked=0;vector<pair<int,int>>small;
 for(int y=0;y<81;y++){
  if(double(clock()-t)/CLOCKS_PER_SEC>1.7)break;
  vector<pair<int,int>>vals;vals.reserve(N-1);
  for(int z=0;z<N;z++)if(z!=y){int c=0;for(int w=0;w<W;w++)c+=__builtin_popcountll(r3[y][w]&r2[z][w]);vals.push_back({c,z});}
  sort(vals.begin(),vals.end());int L=0;for(int i=0;i<D;i++)L+=vals[i].first;
  checked++;hist<<y<<'\t'<<L<<'\t'<<upper-L<<'\t'<<N-1<<'\n';
  if(L>best){best=L;small.assign(vals.begin(),vals.begin()+D);}
  if(upper-L<N){witness=y;small.assign(vals.begin(),vals.begin()+D);break;}
 }
 hist.close();ofstream o("OVERLAP_CHILD_RESULT.json");
 o<<"{\"status\":\""<<(witness>=0?"PROVED_NO_ANY_PERFECT_MATCHING_TWO6804_D4":checked==81?"OVERLAP_OBSTRUCTION_NOT_SUPPORTED_COMPLETE81":"UNKNOWN_BUDGET")<<"\",\"source_parse_count\":1,\"sourceD4_validation_BFS\":0,\"B2max\":"<<b2max<<",\"S2max\":"<<s2max<<",\"B3max_all6804\":"<<b3max<<",\"S3max_all6804\":"<<s3max<<",\"raw_union_upper\":"<<upper<<",\"source_n\":6804,\"threshold_L\":"<<upper-N+1<<",\"root_centres_checked\":"<<checked<<",\"witness_y\":"<<witness<<",\"witness_L\":"<<best<<",\"witness_union_upper\":"<<upper-best<<",\"thirteen_smallest_pairs_overlap_then_label\":[";
 for(size_t i=0;i<small.size();i++){if(i)o<<',';o<<'['<<small[i].first<<','<<small[i].second<<']';}
 o<<"],\"native_CPU\":"<<double(clock()-t)/CLOCKS_PER_SEC<<",\"new_graph_parameter_Lean\":[0,0,0]}\n";
 cout<<"witness="<<witness<<" L="<<best<<" U="<<upper<<" crossupper="<<upper-best<<" CPU="<<double(clock()-t)/CLOCKS_PER_SEC<<'\n';
 }catch(const exception&e){cerr<<e.what()<<'\n';return 2;}
}
