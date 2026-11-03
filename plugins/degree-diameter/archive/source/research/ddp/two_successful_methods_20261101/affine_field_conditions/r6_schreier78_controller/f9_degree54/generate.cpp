#include <algorithm>
#include <array>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <stdexcept>
#include "actual_parameters.hpp"

constexpr int N=56862,F=729;
int ADD[9][9],MUL[9][9],NEG[9];
int TRANS[8][729][9];
int add(int a,int b){return ADD[a][b];}
int mul(int a,int b){return MUL[a][b];}
using Vec=std::array<int,3>;
Vec direction(int p){return {DIR[p][0],DIR[p][1],DIR[p][2]};}
Vec decode(int x){return {x%9,x/9%9,x/81};}
int encode(const Vec&v){return v[0]+9*v[1]+81*v[2];}
Vec mv(int c,const Vec&v){Vec r{};for(int i=0;i<3;i++)for(int j=0;j<3;j++)r[i]=add(r[i],mul(MAT[c][i][j],v[j]));return r;}
int det(const Vec&a,const Vec&b,const Vec&c){
  int plus=add(add(mul(a[0],mul(b[1],c[2])),mul(a[1],mul(b[2],c[0]))),mul(a[2],mul(b[0],c[1])));
  int minus=add(add(mul(a[0],mul(b[2],c[1])),mul(a[1],mul(b[0],c[2]))),mul(a[2],mul(b[1],c[0])));
  return add(plus,NEG[minus]);
}
void require(bool x,const char*message){if(!x)throw std::runtime_error(message);}
int main(){
 try{
  const auto started=std::clock();
  for(int a=0;a<9;a++){
    NEG[a]=(3-a%3)%3+3*((3-a/3)%3);
    for(int b=0;b<9;b++){
      ADD[a][b]=(a%3+b%3)%3+3*((a/3+b/3)%3);
      MUL[a][b]=((a%3*(b%3)-a/3*(b/3))%3+3)%3+3*((a%3*(b/3)+a/3*(b%3))%3);
    }
  }
  for(int c=0;c<8;c++)for(int x=0;x<F;x++){
    Vec center=mv(c,decode(x));
    for(int t=0;t<9;t++){
      Vec y=center;for(int i=0;i<3;i++)y[i]=add(y[i],mul(t,DIR[TARGETPORT[c]][i]));
      TRANS[c][x][t]=encode(y);
    }
  }
  int inverse_noise_checks=0,actual_dart_bindings=0;
  for(int c=0;c<8;c++)for(int x=0;x<F;x++)for(int t=0;t<9;t++){
    require(TRANS[CHARTINV[c]][TRANS[c][x][t]][NEG[t]]==x,"chart noise inverse failed");
    inverse_noise_checks++;
  }
  for(int u=0;u<78;u++)for(int p=0;p<6;p++){
    int v=CTRL[u][p],q=INV[p],c=DARTCHART[u][p];
    require(CTRL[v][q]==u,"controller inverse failed");
    require(SOURCEPORT[c]==p && TARGETPORT[c]==q,"chart endpoint ports failed");
    require(DARTCHART[v][q]==CHARTINV[c],"actual dart chart inverse failed");
    actual_dart_bindings++;
  }
  int nb_routes=0,adjacent_pairs=0;
  for(int u=0;u<78;u++)for(int v=0;v<78;v++){
    bool adj=false;for(int p=0;p<6;p++)if(CTRL[u][p]==v)adj=true;
    if(adj){adjacent_pairs++;continue;}
    int representative=26*(v/26)+(v%26-u%26+26)%26;
    const int*word=ROUTES[u/26][representative];
    require(word[1]!=INV[word[0]] && word[2]!=INV[word[1]],"actual same/nonadj word not NB3");
    int u1=CTRL[u][word[0]],u2=CTRL[u1][word[1]],u3=CTRL[u2][word[2]];
    require(u3==v,"actual translated word endpoint failed");
    int center_chart=DARTCHART[u1][word[1]];
    require(det(mv(center_chart,direction(INV[word[0]])),direction(INV[word[1]]),direction(word[2]))!=0,"actual NB3 rank failed");
    nb_routes++;
  }
  require(nb_routes==5616 && adjacent_pairs==468,"actual route class count failed");
  std::ofstream output("graph_d54_D3_n56862.edges");
  require(bool(output),"edge output open failed");
  std::array<int,N> literal_degree{};
  uint64_t edges=0,darts=0;
  for(int u=0;u<78;u++)for(int x=0;x<F;x++){
    int source=F*u+x;
    std::array<int,54> neighbors{};int k=0;
    for(int p=0;p<6;p++)for(int t=0;t<9;t++)
      neighbors[k++]=F*CTRL[u][p]+TRANS[DARTCHART[u][p]][x][t];
    std::sort(neighbors.begin(),neighbors.end());
    for(int i=0;i<54;i++){
      int target=neighbors[i];
      require(target!=source && target>=0 && target<N,"loop or label range failed");
      require(i==0||target!=neighbors[i-1],"repeated neighbor failed");
      if(source<target){output<<source<<' '<<target<<'\n';literal_degree[source]++;literal_degree[target]++;edges++;}
      darts++;
    }
  }
  output.close();require(bool(output),"edge output write failed");
  require(edges==1535274 && darts==3070548,"edge count failed");
  for(int degree:literal_degree)require(degree==54,"literal degree failed");
  double cpu=double(std::clock()-started)/CLOCKS_PER_SEC;
  std::ofstream result("GENERATION_RESULT.json");
  result<<std::setprecision(12)<<"{\n  \"status\": \"PRODUCTION_PASS\",\n  \"order\": "<<N<<",\n  \"edges\": "<<edges<<",\n  \"degree_min\": 54,\n  \"degree_max\": 54,\n  \"all_vertices_checked\": "<<N<<",\n  \"darts_checked\": "<<darts<<",\n  \"actual_chart_noise_inverse_checks\": "<<inverse_noise_checks<<",\n  \"actual_controller_dart_bindings\": "<<actual_dart_bindings<<",\n  \"actual_same_nonadjacent_rank_routes\": "<<nb_routes<<",\n  \"actual_adjacent_pencil_pairs\": "<<adjacent_pairs<<",\n  \"sorted_literal_edges\": true,\n  \"generation_cpu_seconds\": "<<cpu<<",\n  \"BFS_runs\": 0,\n  \"solver_Lean_runs\": 0\n}\n";
  std::cout<<"PRODUCTION_PASS n="<<N<<" edges="<<edges<<" all54regular NB3="<<nb_routes<<" pencil="<<adjacent_pairs<<" cpu="<<cpu<<'\n';
  return 0;
 }catch(const std::exception&e){std::cerr<<e.what()<<'\n';return 2;}
}
