#include <algorithm>
#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
int main(int argc,char**argv){
  const clock_t begun=clock();
  vector<vector<int>> g(200);
  vector<pair<int,int>> edges;
  string line; ifstream input(argv[1]);
  while(getline(input,line)){
    if(line.empty()||line[0]=='#')continue;
    istringstream ss(line);int a,b;if(!(ss>>a>>b))continue;
    if(a<0||b<0||a>=200||b>=200||a==b)return 2;
    if(a>b)swap(a,b);edges.emplace_back(a,b);
    g[a].push_back(b);g[b].push_back(a);
  }
  sort(edges.begin(),edges.end());
  if(edges.size()!=300||adjacent_find(edges.begin(),edges.end())!=edges.end())return 3;
  for(auto&v:g){sort(v.begin(),v.end());if(v.size()!=3)return 4;}
  vector<vector<int>> radius3(200);
  for(int v=0;v<200;v++){
    int d[201],q[201],lo=0,hi=0;fill(d,d+201,-1);d[v]=0;q[hi++]=v;
    while(lo<hi){int x=q[lo++];if(d[x]==3)continue;for(int y:g[x])if(d[y]<0){d[y]=d[x]+1;q[hi++]=y;}}
    for(int x=0;x<200;x++)if(d[x]>=0)radius3[v].push_back(x);
  }
  ofstream rows(string(argv[2])+"/cases.tsv");
  rows<<"ordinal\tvertex\tsingleton\tnewroot_missing\tchecked_roots\tfirst_bad_root\tfirst_bad_target\n";
  int cases=0,newpass=0,oldfail=0,bfses=0,hit=-1,hitv=-1,hits=-1;
  int firstv=-1,firsts=-1,firstbadroot=-1,firstbadtarget=-1,firstnewmiss=-1;
  for(int v=0;v<200 && hit<0;v++)for(int singleton:g[v]){
    vector<vector<int>> h=g;h.resize(201);
    for(int y:g[v])if(y!=singleton){
      auto& a=h[v];a.erase(find(a.begin(),a.end(),y));
      auto& b=h[y];b.erase(find(b.begin(),b.end(),v));
      h[y].push_back(200);h[200].push_back(y);
    }
    h[v].push_back(200);h[200].push_back(v);
    if(h[v].size()!=2||h[200].size()!=3)return 5;
    int checked=0,br=-1,bt=-1;
    auto check=[&](int r){
      int d[201],q[201],lo=0,hi=0;fill(d,d+201,-1);d[r]=0;q[hi++]=r;
      while(lo<hi){int x=q[lo++];if(d[x]==7)continue;for(int y:h[x])if(d[y]<0){d[y]=d[x]+1;q[hi++]=y;}}
      ++bfses;++checked;int miss=0;
      for(int x=0;x<=200;x++)if(d[x]<0){++miss;if(bt<0){br=r;bt=x;}}
      return miss;
    };
    int newmiss=check(200);
    if(newmiss==0){
      ++newpass;
      for(int r:radius3[v])if(check(r)>0)break;
      if(br>=0)++oldfail;
    }
    if(cases==0){firstv=v;firsts=singleton;firstbadroot=br;firstbadtarget=bt;firstnewmiss=newmiss;}
    rows<<cases<<'\t'<<v<<'\t'<<singleton<<'\t'<<newmiss<<'\t'<<checked<<'\t'<<br<<'\t'<<bt<<'\n';
    if(br<0){
      hit=cases;hitv=v;hits=singleton;
      ofstream out(string(argv[2])+"/first_hit.edges");out<<"201 301\n";
      for(int x=0;x<=200;x++)for(int y:h[x])if(x<y)out<<x<<" "<<y<<"\n";
    }
    ++cases;
    if(double(clock()-begun)/CLOCKS_PER_SEC>25.0)goto finished;
  }
finished:
  ofstream out(string(argv[2])+"/NATIVE_RESULT.json");
  out<<"{\"source_n\":200,\"source_m\":300,\"source_degree_histogram\":{\"3\":200},"
     <<"\"source_R3_search_roots\":200,\"source_full_diameter_BFS\":0,"
     <<"\"scope_size\":600,\"visited\":"<<cases<<",\"unattempted\":"<<(600-cases)
     <<",\"newroot_pass\":"<<newpass<<",\"newroot_pass_oldpair_fail\":"<<oldfail
     <<",\"modified_graph_root_BFS\":"<<bfses<<",\"hit_ordinal\":"<<hit
     <<",\"hit_vertex\":"<<hitv<<",\"hit_singleton\":"<<hits
     <<",\"first_case\":{\"vertex\":"<<firstv<<",\"singleton\":"<<firsts
     <<",\"newroot_missing\":"<<firstnewmiss<<",\"first_bad_root\":"<<firstbadroot
     <<",\"first_bad_target\":"<<firstbadtarget<<"},\"native_CPU_seconds\":"
     <<double(clock()-begun)/CLOCKS_PER_SEC<<"}\n";
  return 0;
}
