#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <set>
#include <string>
#include <vector>
#include <sys/resource.h>
using namespace std;
using Row=array<uint64_t,11>;
double cpu(){return double(clock())/CLOCKS_PER_SEC;}
int main(int argc,char**argv){
 rlimit lim{3,3};assert(setrlimit(RLIMIT_CPU,&lim)==0);
 assert(argc==3);string base=argv[1],out=argv[2];double start=cpu();
 ifstream csc(base+"/single_vertex_R3_cover/COVER_CSC.bin",ios::binary);uint32_t h[3];csc.read((char*)h,12);int N=h[0],C=h[1],nnz=h[2];assert(N==15552&&C==648&&nnz==1496880);
 vector<int32_t>ptr(C+1),indices(nnz);csc.read((char*)ptr.data(),4*ptr.size());csc.read((char*)indices.data(),4*indices.size());assert(csc.good()&&ptr.front()==0&&ptr.back()==nnz);
 vector<Row>rows(N);for(int j=0;j<C;j++)for(int k=ptr[j];k<ptr[j+1];k++){assert(indices[k]>=0&&indices[k]<N);rows[indices[k]][j/64]|=1ULL<<(j%64);}
 map<Row,vector<int>>groups;for(int i=0;i<N;i++)groups[rows[i]].push_back(i);
 int duplicate_groups=0,duplicate_excess=0,collapsed_nnz=0,largest_group=0;map<int,int>mults;ofstream gf(out+"/EXACT_ROW_GROUPS.jsonl");vector<int32_t>representatives;
 for(auto&[row,targets]:groups){int size=0;for(uint64_t w:row)size+=__builtin_popcountll(w);collapsed_nnz+=size;int q=targets.size();mults[q]++;largest_group=max(largest_group,q);if(q>1){duplicate_groups++;duplicate_excess+=q-1;}
  representatives.push_back(targets.front());gf<<"{\"representative\":"<<targets.front()<<",\"multiplicity\":"<<q<<",\"support_size\":"<<size<<",\"target_ids\":[";for(int k=0;k<q;k++){if(k)gf<<',';gf<<targets[k];}gf<<"]}\n";
 }
 sort(representatives.begin(),representatives.end());ofstream rf(out+"/UNIQUE_ROW_REPRESENTATIVES.i32le.bin",ios::binary);rf.write((char*)representatives.data(),4*representatives.size());
 ifstream mask(base+"/single_vertex_R3_cover/R3_MASKS.bin",ios::binary);uint32_t mh[3];mask.read((char*)mh,12);assert(mh[0]==648&&mh[1]==15552&&mh[2]==243);
 vector<int>free;for(int i=0;i<C;i++){uint32_t v;mask.read((char*)&v,4);free.push_back(v);mask.seekg(243*8,ios::cur);}assert(is_sorted(free.begin(),free.end())&&adjacent_find(free.begin(),free.end())==free.end());
 vector<bool>isfree(N);for(int v:free)isfree[v]=true;vector<vector<int>>Fadj(N);vector<int>degree(N);ifstream s(base+"/source15552.header.edges");int n,m;s>>n>>m;assert(n==N&&m==116316);
 int Fm=0;for(int i=0,u,v;i<m;i++){s>>u>>v;degree[u]++;degree[v]++;if(isfree[u]&&isfree[v]){Fadj[u].push_back(v);Fadj[v].push_back(u);Fm++;}}
 for(int v:free)assert(degree[v]==14);map<int,int>Fd,types_by_size;for(int v:free)Fd[Fadj[v].size()]++;
 vector<bool>seen(N);struct Comp{vector<int>vs;int m;map<int,int>ds;string typ;};vector<Comp>components;map<string,int>types;
 for(int root:free)if(!seen[root]){vector<int>stack{root},vs;seen[root]=true;int sum=0;map<int,int>d;
  while(!stack.empty()){int u=stack.back();stack.pop_back();vs.push_back(u);sum+=Fadj[u].size();d[Fadj[u].size()]++;for(int v:Fadj[u])if(!seen[v]){seen[v]=true;stack.push_back(v);}}
  sort(vs.begin(),vs.end());int sz=vs.size(),e=sum/2;string typ;
  if(sz==1&&e==0)typ="P1";else if(e==sz&&d.size()==1&&d.count(2))typ="C"+to_string(sz);else if(e==sz-1&&d.rbegin()->first<=2)typ="P"+to_string(sz);else typ="GENERAL";
  components.push_back({vs,e,d,typ});types[typ]++;types_by_size[sz]++;
 }
 ofstream F(out+"/FREE_COMPONENTS.json");F<<"{\"free_vertices\":648,\"free_edges\":"<<Fm<<",\"degree_histogram\":{";bool first=true;for(auto[a,b]:Fd){if(!first)F<<',';first=false;F<<'\"'<<a<<"\":"<<b;}F<<"},\"component_count\":"<<components.size()<<",\"component_type_histogram\":{";first=true;for(auto[a,b]:types){if(!first)F<<',';first=false;F<<'\"'<<a<<"\":"<<b;}F<<"},\"components\":[";
 for(int k=0;k<(int)components.size();k++){auto&c=components[k];if(k)F<<',';F<<"{\"type\":\""<<c.typ<<"\",\"n\":"<<c.vs.size()<<",\"m\":"<<c.m<<",\"vertices\":[";for(int j=0;j<(int)c.vs.size();j++){if(j)F<<',';F<<c.vs[j];}F<<"]}";}
 F<<"],\"free_adjacency\":{";first=true;for(int u:free){if(!first)F<<',';first=false;sort(Fadj[u].begin(),Fadj[u].end());F<<'\"'<<u<<"\":[";for(int j=0;j<(int)Fadj[u].size();j++){if(j)F<<',';F<<Fadj[u][j];}F<<']';}F<<"},\"ordinary_BFS\":0,\"DFS_component_scans\":1}\n";
 ofstream r(out+"/NATIVE_RESULT.json");r<<"{\"status\":\"EXACT_CACHED_SUPPORT_AND_FREE_STRUCTURE_COMPLETE\",\"source_n\":"<<N<<",\"columns\":"<<C<<",\"original_rows\":"<<N<<",\"original_nnz\":"<<nnz<<",\"unique_support_rows\":"<<groups.size()<<",\"duplicate_groups\":"<<duplicate_groups<<",\"duplicate_excess_rows\":"<<duplicate_excess<<",\"largest_equal_row_group\":"<<largest_group<<",\"collapsed_nnz\":"<<collapsed_nnz<<",\"row_multiplicity_histogram\":{";first=true;for(auto[a,b]:mults){if(!first)r<<',';first=false;r<<'\"'<<a<<"\":"<<b;}r<<"},\"free_vertices\":648,\"free_induced_edges\":"<<Fm<<",\"free_degree_histogram\":{";first=true;for(auto[a,b]:Fd){if(!first)r<<',';first=false;r<<'\"'<<a<<"\":"<<b;}r<<"},\"free_component_count\":"<<components.size()<<",\"free_component_types\":{";first=true;for(auto[a,b]:types){if(!first)r<<',';first=false;r<<'\"'<<a<<"\":"<<b;}r<<"},\"native_CPU_seconds\":"<<cpu()-start<<",\"ordinary_BFS\":0,\"new_R3_balls\":0,\"solver_runs\":0,\"candidate_graphs\":0,\"hard_RLIMIT_CPU_seconds\":3,\"exact_row_equality_method\":\"Lexicographicbalancedtreeover648-bitrowarrays; nohashkeys/digests.\"}\n";
 cerr<<"DONE unique "<<groups.size()<<"/"<<N<<" duplicateexcess "<<duplicate_excess<<" Fcomps "<<components.size()<<" CPU "<<cpu()-start<<'\n';
}
