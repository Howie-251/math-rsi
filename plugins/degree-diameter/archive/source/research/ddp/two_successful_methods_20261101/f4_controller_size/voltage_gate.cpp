#include <array>
#include <ctime>
#include <fstream>
#include <iostream>
#include <vector>
using Ctl=std::array<std::array<int,5>,66>;
int mod22(int x){x%=22;return x<0?x+22:x;}
Ctl build(int a,int b,int c,int t){
 Ctl C{};int perm[3]={0,2,1},v[3]={a,b,c};
 for(int k=0;k<3;k++)for(int g=0;g<22;g++){
  int u=22*k+g,w=22*perm[k]+mod22(g+v[k]);C[u][0]=w;C[w][1]=u;
  w=22*((k+1)%3)+g;C[u][2]=w;C[w][3]=u;
 }
 for(int g=0;g<22;g++){
  int w=22+mod22(g+t);C[g][4]=w;C[w][4]=g;C[44+g][4]=44+mod22(g+11);
 }
 return C;
}
bool cover3(const Ctl&C,int u){
 std::array<bool,66> seen{};seen[u]=true;
 for(int a:C[u]){seen[a]=true;for(int b:C[a]){seen[b]=true;for(int c:C[b])seen[c]=true;}}
 for(bool x:seen)if(!x)return false;
 return true;
}
bool nb3(const Ctl&C,int u){
 int inv[5]={1,0,3,2,4};std::array<bool,66> seen{};
 for(int p=0;p<5;p++)for(int q=0;q<5;q++)if(q!=inv[p])
  for(int r=0;r<5;r++)if(r!=inv[q])seen[C[C[C[u][p]][q]][r]]=true;
 for(int v=0;v<66;v++){
  bool adj=false;for(int w:C[u])if(v==w)adj=true;
  if(!adj&&!seen[v])return false;
 }
 return true;
}
int main(int argc,char**argv){
 if(argc!=2)return 2;
 std::clock_t start=std::clock();long total=0,pass0=0,pass01=0,passall=0,rank=0;
 std::ofstream out(std::string(argv[1])+"/PASSING_VOLTAGES.json");out<<"[\n";
 bool first=true;
 for(int a=1;a<22;a++)if(a!=11)for(int b=1;b<22;b++)for(int c=1;c<22;c++)if(mod22(b+c))for(int t=1;t<22;t++){
  total++;Ctl C=build(a,b,c,t);
  if(!cover3(C,0))continue;pass0++;
  if(!cover3(C,22))continue;pass01++;
  if(!cover3(C,44))continue;passall++;
  bool ok=nb3(C,0)&&nb3(C,22)&&nb3(C,44);if(ok)rank++;
  if(!first)out<<",\n";first=false;
  out<<"{\"a\":["<<a<<","<<b<<","<<c<<"],\"matching_offset\":"<<t<<",\"required_NB3_gate\":"<<(ok?"true":"false")<<"}";
 }
 out<<"\n]\n";out.close();
 double cpu=double(std::clock()-start)/CLOCKS_PER_SEC;
 std::ofstream res(std::string(argv[1])+"/VOLTAGE_RESULT.json");
 res<<"{\"status\":\""<<(passall?"CONTROLLER_PASS_NOT_FIBER_GRAPH":"COMPLETE_CONTROLLER_DOMAIN_FAIL")<<"\",\"assignments\":"<<total<<",\"root0_pass\":"<<pass0<<",\"roots01_pass\":"<<pass01<<",\"all_three_classes_pass\":"<<passall<<",\"required_NB3_pass\":"<<rank<<",\"CPU_seconds\":"<<cpu<<",\"fiber_graphs_generated\":0,\"solver_calls\":0,\"complete_fixed_domain\":true,\"global_controller_class_excluded\":false}\n";
 std::cout<<"assignments="<<total<<" root0="<<pass0<<" roots01="<<pass01<<" all3="<<passall<<" NB3="<<rank<<" CPU="<<cpu<<"\n";
}
