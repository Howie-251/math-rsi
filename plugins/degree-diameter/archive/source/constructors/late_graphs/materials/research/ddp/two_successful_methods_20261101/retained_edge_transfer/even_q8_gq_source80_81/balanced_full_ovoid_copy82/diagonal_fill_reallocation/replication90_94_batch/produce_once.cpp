#include <algorithm>
#include <array>
#include <cassert>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <map>
#include <vector>

constexpr int sourceN=346516, oldH=342290, roles=4226;
constexpr long long sourceM=14204970;
struct Case {
  int r,n,cap; long long expectedM,count=0,added=0;
  int lastU=-1,lastV=-1;
  std::ofstream out;
  std::vector<int> degree;
  std::filesystem::path dir;
  Case(int copies,int d,const char* path):r(copies),n(sourceN+copies*roles),cap(d),
      expectedM(sourceM+342225LL*copies),out(path),degree(n),
      dir(std::filesystem::path(path).parent_path()) {
    assert(out.good());out<<n<<' '<<expectedM<<'\n';
  }
  void write(int u,int v,bool isNew) {
    assert(0<=u&&u<v&&v<n);
    assert(u>lastU||(u==lastU&&v>lastV));
    out<<u<<' '<<v<<'\n';++count;++degree[u];++degree[v];
    added+=isNew;lastU=u;lastV=v;
  }
};
int main(int argc,char** argv) {
  assert(argc==4);
  std::ifstream in(argv[1]);assert(in.good());
  int inputN;long long inputM;in>>inputN>>inputM;
  assert(inputN==sourceN&&inputM==sourceM);
  Case c90(8,90,argv[2]),c94(12,94,argv[3]);
  std::array<Case*,2> cases{&c90,&c94};
  std::vector<int> oldDegree(sourceN),rolePins(roles),pinOwner(oldH,-1);
  int row=-1,role=-1,previousU=-1,previousV=-1;
  long long readEdges=0;
  auto flush=[&]() {
    if(row<0||role<0)return;
    assert(row<oldH&&pinOwner[row]<0);pinOwner[row]=role;++rolePins[role];
    for(Case* c:cases)for(int b=0;b<c->r;++b)
      c->write(row,sourceN+roles*b+role,true);
    role=-1;
  };
  int u,v;
  while(in>>u>>v) {
    assert(0<=u&&u<v&&v<sourceN);
    assert(u>previousU||(u==previousU&&v>previousV));
    if(u!=row){flush();row=u;}
    if(u<oldH&&v>=oldH){assert(role<0);role=v-oldH;}
    for(Case* c:cases)c->write(u,v,false);
    ++oldDegree[u];++oldDegree[v];++readEdges;previousU=u;previousV=v;
  }
  assert(in.eof());flush();assert(readEdges==sourceM);
  std::map<int,int> sourceHist,roleHist;
  for(int d:oldDegree)++sourceHist[d];
  assert((sourceHist==std::map<int,int>{{65,1},{80,65},{81,4225},{82,342225}}));
  int pins=0;
  for(int u=0;u<oldH;++u)if(pinOwner[u]>=0){++pins;assert(oldDegree[u]==82);}
  assert(pins==342225);
  for(int h=0;h<roles;++h){assert(rolePins[h]==oldDegree[oldH+h]);++roleHist[rolePins[h]];}
  assert((roleHist==std::map<int,int>{{65,1},{80,65},{81,4160}}));
  for(Case* c:cases) {
    c->out.close();assert(c->out.good());
    assert(c->count==c->expectedM&&c->added==342225LL*c->r);
    for(int u=0;u<sourceN;++u)
      assert(c->degree[u]==oldDegree[u]+(u<oldH&&pinOwner[u]>=0?c->r:0));
    for(int b=0;b<c->r;++b)for(int h=0;h<roles;++h)
      assert(c->degree[sourceN+roles*b+h]==rolePins[h]);
    std::map<int,int> hist;
    for(int d:c->degree){assert(d<=c->cap);++hist[d];}
    std::map<int,int> expected{{65,c->r+1},{80,65*(c->r+1)},
      {81,4160*(c->r+1)+65},{c->cap,342225}};
    assert(hist==expected);
    std::ofstream recipe(c->dir/"ORDERED_NEW_ROLE_RECIPE.tsv");
    std::ofstream prefix(c->dir/"PREFIX_LOAD_CHECKS.tsv");
    recipe<<"j\tcopy\trole\tsource_center_label\tnew_label\tliteral_N_size\n";
    prefix<<"j\tcopy\trole\tpins\told_load_before\told_load_after\told_pin_degree_after\n";
    for(int b=0;b<c->r;++b)for(int h=0;h<roles;++h) {
      int j=roles*b+h;
      recipe<<j<<'\t'<<b<<'\t'<<h<<'\t'<<oldH+h<<'\t'<<sourceN+j<<'\t'<<rolePins[h]<<'\n';
      prefix<<j<<'\t'<<b<<'\t'<<h<<'\t'<<rolePins[h]<<'\t'<<b<<'\t'<<b+1<<'\t'<<83+b<<'\n';
    }
    recipe.close();prefix.close();assert(recipe.good()&&prefix.good());
  }
  std::cout<<"{\"status\":\"PRODUCTION_PASS_PENDING_FRESH_ACCEPTANCE\",\"source_parse\":1,"
    <<"\"source_n\":346516,\"source_m\":14204970,\"source_pin_union\":342225,"
    <<"\"all4226_role_fullN_sizes_bound_to_source_stream\":true,\"new_new_edges\":0,"
    <<"\"all_old_body_edges_streamed_unchanged\":true,\"all_final_vertex_degrees_checked\":true,"
    <<"\"strictlex_headers_simple\":true,\"BFS_runs\":0,\"cases\":[";
  for(int i=0;i<2;++i) {
    Case* c=cases[i];if(i)std::cout<<',';
    std::cout<<"{\"degree\":"<<c->cap<<",\"r\":"<<c->r<<",\"n\":"<<c->n
      <<",\"m\":"<<c->expectedM<<",\"new_roles\":"<<c->r*roles
      <<",\"old_edges_retained\":"<<readEdges<<",\"new_edges\":"<<c->added
      <<",\"degree_histogram\":{\"65\":"<<c->r+1<<",\"80\":"<<65*(c->r+1)
      <<",\"81\":"<<4160*(c->r+1)+65<<",\""<<c->cap<<"\":342225}}";
  }
  std::cout<<"]}\n";
}
