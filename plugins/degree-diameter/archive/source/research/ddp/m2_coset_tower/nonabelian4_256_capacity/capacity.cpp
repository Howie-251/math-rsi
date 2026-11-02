#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;
using U64=uint64_t;
constexpr int E=16,F=13,Q=32,PATTERNS=1<<F;
const array<int,E> eu={0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2};
const array<int,E> ev={1,1,1,2,2,2,3,3,2,2,3,3,3,3,3,3};
const array<int,3> tree={0,3,6};
const array<int,F> free_edges={1,2,4,5,7,8,9,10,11,12,13,14,15};
array<int,E> variable;
array<vector<int>,4> adjacency;
struct Path {int source,target,length;array<int,3> darts;};
vector<Path> paths;
U64 zero_key=0;
constexpr U64 constant_flag=1ULL<<(3*F);
clock_t began;
double cpu(){return double(clock()-began)/CLOCKS_PER_SEC;}

void make_paths(int root,int vertex,int length,int last,array<int,3>&darts){
 paths.push_back({root,vertex,length,darts});
 if(length==3)return;
 for(int d:adjacency[vertex]){
  if(last>=0&&d==(last^1))continue;
  darts[length]=d;
  int e=d/2, target=(d&1)?eu[e]:ev[e];
  make_paths(root,target,length+1,d,darts);
 }
}

template<class T> void array_json(ostream&o,const T&a){
 o<<'[';bool first=true;for(auto x:a){if(!first)o<<',';first=false;o<<x;}o<<']';
}
void matrix_json(ostream&o,const array<int,32>&a){
 o<<'[';for(int root=0;root<4;root++){
  if(root)o<<',';o<<'[';
  for(int target=0;target<4;target++){
   if(target)o<<',';int k=(root*4+target)*2;o<<'['<<a[k]<<','<<a[k+1]<<']';
  }o<<']';
 }o<<']';
}
struct Case {
 int phase_mask,min_capacity,total_capacity;
 array<int,32> counts,raw;
};
void case_json(ostream&o,const Case&c){
 o<<"{\"phase_mask\":"<<c.phase_mask<<",\"minimum_capacity\":"<<c.min_capacity
  <<",\"total_capacity\":"<<c.total_capacity<<",\"capacity_pass\":"<<(c.min_capacity>=Q?"true":"false")
  <<",\"capacity_by_root_target_phase\":";matrix_json(o,c.counts);
 o<<",\"raw_walk_counts_by_root_target_phase\":";matrix_json(o,c.raw);o<<'}';
}
void form_json(ostream&o,U64 key){
 o<<"{\"constant\":"<<((key&constant_flag)?16:0)<<",\"coefficients\":[";
 for(int k=0;k<F;k++){if(k)o<<',';o<<(int((key>>(3*k))&7)-3);}o<<"]}";
}

int main(int argc,char**argv){
 assert(argc==4);string out=argv[1],group=argv[2];double budget=stod(argv[3]);
 assert(group=="D64"||group=="Q64");bool quaternion=group=="Q64";
 began=clock();filesystem::create_directories(out);
 variable.fill(-1);for(int k=0;k<F;k++){variable[free_edges[k]]=k;zero_key|=3ULL<<(3*k);}
 for(int e=0;e<E;e++){adjacency[eu[e]].push_back(2*e);adjacency[ev[e]].push_back(2*e+1);}
 for(int root=0;root<4;root++){
  assert(adjacency[root].size()==8);array<int,3>darts{};make_paths(root,root,0,-1,darts);
 }
 assert(paths.size()==4*(1+8+56+392));
 {ofstream f(out+"/paths.json");f<<'[';bool first=true;for(const auto&p:paths){
  if(!first)f<<',';first=false;f<<"{\"root\":"<<p.source<<",\"target\":"<<p.target<<",\"darts\":[";
  for(int k=0;k<p.length;k++){if(k)f<<',';f<<p.darts[k];}f<<"]}";
 }f<<"]\n";}
 ofstream all(out+"/all_patterns.jsonl"),tight(out+"/forms_tight.jsonl");
 vector<Case> survivors;array<vector<U64>,32> forms;
 map<int,int> histogram;int completed=0,tight_fibers=0;
 Case best{};best.min_capacity=-1;bool complete=true;
 for(int mask=0;mask<PATTERNS;mask++){
  if((mask&127)==0&&cpu()>=budget){complete=false;break;}
  array<int,E> bits{};for(int k=0;k<F;k++)bits[free_edges[k]]=(mask>>k)&1;
  array<int,32> raw{};for(auto&f:forms)f.clear();
  for(const auto&p:paths){
   int phase=0,constant=0;U64 key=zero_key;
   for(int j=0;j<p.length;j++){
    int dart=p.darts[j],e=dart/2,rev=dart&1,bit=bits[e],v=variable[e];
    int sign=rev?((phase^bit)?1:-1):(phase?-1:1);
    if(v>=0){U64 unit=1ULL<<(3*v);if(sign>0)key+=unit;else key-=unit;}
    if(quaternion)constant^=bit&(phase^rev);
    phase^=bit;
   }
   if(constant)key|=constant_flag;
   int slot=(p.source*4+p.target)*2+phase;raw[slot]++;forms[slot].push_back(key);
  }
  Case c{};c.phase_mask=mask;c.raw=raw;c.min_capacity=100000;
  for(int slot=0;slot<32;slot++){
   auto&f=forms[slot];sort(f.begin(),f.end());f.erase(unique(f.begin(),f.end()),f.end());
   c.counts[slot]=f.size();c.total_capacity+=f.size();c.min_capacity=min(c.min_capacity,int(f.size()));
  }
  for(int root=0;root<4;root++){
   int sum=0;for(int k=0;k<8;k++)sum+=raw[root*8+k];assert(sum==457);
  }
  histogram[c.min_capacity]++;
  if(c.min_capacity>best.min_capacity||(c.min_capacity==best.min_capacity&&c.total_capacity>best.total_capacity))best=c;
  case_json(all,c);all<<'\n';
  if(c.min_capacity>=Q){
   survivors.push_back(c);
   for(int slot=0;slot<32;slot++)if(c.counts[slot]==Q){
    tight_fibers++;
    tight<<"{\"phase_mask\":"<<mask<<",\"root\":"<<slot/8<<",\"target\":"<<(slot/2)%4
         <<",\"target_phase\":"<<slot%2<<",\"forms\":[";
    bool first=true;for(U64 form:forms[slot]){if(!first)tight<<',';first=false;form_json(tight,form);}tight<<"]}\n";
   }
  }
  completed=mask+1;
  if((completed&1023)==0){all.flush();tight.flush();ofstream p(out+"/progress.json");
   p<<"{\"running\":true,\"group\":\""<<group<<"\",\"completed_phase_masks\":"<<completed
    <<",\"capacity_pass_count\":"<<survivors.size()<<",\"CPU_seconds\":"<<cpu()<<"}\n";
  }
 }
 {ofstream f(out+"/survivors.json");f<<'[';bool first=true;for(const auto&c:survivors){if(!first)f<<',';first=false;case_json(f,c);}f<<"]\n";}
 string status=complete?"COMPLETE":"CPU_LIMIT_PREFIX_SAVED";
 {ofstream f(out+"/results.json");f.precision(12);
  f<<"{\"status\":\""<<status<<"\",\"running\":false,\"group\":\""<<group
   <<"\",\"completed_phase_masks\":"<<completed<<",\"next_phase_mask\":"<<completed
   <<",\"total_phase_masks\":8192,\"capacity_pass_count\":"<<survivors.size()
   <<",\"surviving_tight_fibers\":"<<tight_fibers<<",\"minimum_capacity_histogram\":{";
  bool first=true;for(auto[k,v]:histogram){if(!first)f<<',';first=false;f<<'"'<<k<<"\":"<<v;}f<<'}';
  f<<",\"best_capacity_pattern\":";case_json(f,best);
  f<<",\"CPU_seconds\":"<<cpu()<<",\"translation_assignments\":0,\"generated_graphs\":0,\"BFS_roots\":0}\n";
 }
 cout<<group<<' '<<status<<" completed="<<completed<<" pass="<<survivors.size()
     <<" minbest="<<best.min_capacity<<" tight="<<tight_fibers<<" CPU="<<cpu()<<endl;
}
