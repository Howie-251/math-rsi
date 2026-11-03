#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;using U=uint64_t;
struct Slot{int root,end,phase;vector<array<uint8_t,3>>f;};
struct Action{int r;vector<Slot>slots;vector<int>priority;};
struct Dart{int to,a,h;};
uint32_t read32(istream&f){uint32_t x;f.read((char*)&x,4);assert(f);return x;}
int main(int argc,char**argv){
 clock_t started=clock();string dir=argv[2];double budget=stod(argv[3]);auto cpu=[&](){return double(clock()-started)/CLOCKS_PER_SEC;};
 ifstream in(argv[1],ios::binary);char magic[4];in.read(magic,4);assert(string(magic,4)=="ABF1");
 assert(read32(in)==1&&read32(in)==109&&read32(in)==6&&read32(in)==324);
 vector<Action>actions;for(int ai=0;ai<6;ai++){Action a;a.r=read32(in);
  for(int k=0;k<324;k++){Slot s;s.root=read32(in);s.end=read32(in);s.phase=read32(in);int count=read32(in);
   assert(108*s.root+36*s.end+s.phase==k);s.f.resize(count);in.read((char*)s.f.data(),size_t(count)*3);assert(in);a.slots.push_back(move(s));}
  a.priority.resize(324);iota(a.priority.begin(),a.priority.end(),0);
  sort(a.priority.begin(),a.priority.end(),[&](int i,int j){auto x=a.slots[i].f.size(),y=a.slots[j].f.size();return x!=y?x<y:i<j;});actions.push_back(move(a));
 }
 const int P=109,M=36,G=P*M,N=3*G;int products[P][P];for(int a=0;a<P;a++)for(int x=0;x<P;x++)products[a][x]=a*x%P;
 long long visited=0,numeric=0,capacity=0,slotchecks=0;int ai=-1,A=-1,B=-1,failedslot=-1;bool hit=false,limited=false,inconsistent=false;
 vector<int>action_counts(6),action_slotchecks(6);vector<vector<long long>>failhist(6,vector<long long>(324));
 auto cover=[&](const Slot&s,int a,int b){U low=0,high=0;for(auto c:s.f){int v=products[a][c[0]]+products[b][c[1]]+c[2];if(v>=218)v-=218;else if(v>=109)v-=109;
   if(v<64)low|=U(1)<<v;else high|=U(1)<<(v-64);
   if(low==~U(0)&&high==((U(1)<<45)-1))return true;}return false;};
 auto build_hit=[&](int R,int av,int bv){
  int rp[M];rp[0]=1;for(int j=1;j<M;j++)rp[j]=rp[j-1]*R%P;assert(rp[35]*R%P==1);
  array<vector<Dart>,3>base;auto link=[&](int u,int v,int x,int h){base[u].push_back({v,x,h});base[v].push_back({u,(P-rp[(M-h)%M]*x%P)%P,(M-h)%M});};
  link(0,1,0,0);link(0,2,0,0);link(1,2,1,6);link(0,1,av,10);link(0,1,bv,14);base[2].push_back({2,0,3});base[2].push_back({2,0,33});
  vector<array<int,4>>adj(N);for(int v=0;v<3;v++)for(int j=0;j<M;j++)for(int i=0;i<P;i++){int u=v*G+j*P+i;
   for(int k=0;k<4;k++){auto e=base[v][k];adj[u][k]=e.to*G+((j+e.h)%M)*P+(i+rp[j]*e.a)%P;}
   auto row=adj[u];sort(row.begin(),row.end());assert(adjacent_find(row.begin(),row.end())==row.end()&&find(row.begin(),row.end(),u)==row.end());}
  for(int u=0;u<N;u++)for(int v:adj[u])assert(find(adj[v].begin(),adj[v].end(),u)!=adj[v].end());
  vector<int>eccs;
  for(int rootbase=0;rootbase<3;rootbase++){vector<int>d(N,-1),q(N);int h=0,t=0,root=rootbase*G;d[root]=0;q[t++]=root;
   while(h<t){int u=q[h++];for(int v:adj[u])if(d[v]<0){d[v]=d[u]+1;q[t++]=v;}}
   int ecc=*max_element(d.begin(),d.end());eccs.push_back(ecc);
   if(t!=N||ecc>9){inconsistent=true;return;}
  }
  ofstream edgefile(dir+"/graph_d4_D9_n11772.edges");edgefile<<N<<' '<<2*N<<'\n';for(int u=0;u<N;u++)for(int v:adj[u])if(u<v)edgefile<<u<<' '<<v<<'\n';
  ofstream params(dir+"/FIRST_HIT.json");params<<"{\"N\":109,\"M\":36,\"r\":"<<R<<",\"A\":"<<av<<",\"B\":"<<bv<<",\"C\":1,\"n\":11772,\"m\":23544,\"degree\":4,\"simple\":true,\"connected\":true,\"root_eccentricities\":[";
  for(int k=0;k<3;k++){if(k)params<<',';params<<eccs[k];}
  params<<"],\"actual_global_D\":"<<*max_element(eccs.begin(),eccs.end())<<",\"ordinary_bad_unordered_pairs_targetD9\":0,\"complete_orbit_roots\":3,\"independent_root_acceptance_pending\":true}\n";
 };
 for(ai=0;ai<6;ai++){
  auto&act=actions[ai];
  if(act.slots[act.priority[0]].f.size()<109){capacity+=11881;visited+=11881;action_counts[ai]=11881;failedslot=act.priority[0];failhist[ai][failedslot]=11881;A=B=108;continue;}
  for(A=0;A<109;A++)for(B=0;B<109;B++){
   ++visited;++numeric;++action_counts[ai];bool full=true;
   for(int slotid:act.priority){++slotchecks;++action_slotchecks[ai];if(!cover(act.slots[slotid],A,B)){failedslot=slotid;++failhist[ai][slotid];full=false;break;}}
   if(full){build_hit(act.r,A,B);hit=!inconsistent;goto terminal;}
   if((visited&255)==0&&cpu()>budget){limited=true;goto terminal;}
  }
  cout<<"ACTION_DONE "<<act.r<<" cases "<<action_counts[ai]<<" CPU "<<cpu()<<endl;
 }
 ai=5;A=B=108;
terminal:
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(inconsistent?"INCONSISTENT_FORMS_VS_ACTUAL_GRAPH":hit?"FIRST_COMPLETE_HIT":limited?"UNKNOWN_CPU_LIMIT":"COMPLETE_FIXED_FAMILY_NO_HIT")
  <<"\",\"scope_cases\":71286,\"cases_processed\":"<<visited<<",\"numeric_cases\":"<<numeric<<",\"capacity_pruned_cases\":"<<capacity
  <<",\"slot_evaluations\":"<<slotchecks<<",\"hit\":"<<(hit?"true":"false")<<",\"CPU_limited\":"<<(limited?"true":"false")
  <<",\"cursor\":{\"action_index\":"<<ai<<",\"r\":"<<actions[ai].r<<",\"A\":"<<A<<",\"B\":"<<B<<",\"last_failed_slot\":"<<failedslot
  <<"},\"actions\":[";
 for(int k=0;k<6;k++){if(k)out<<',';out<<"{\"r\":"<<actions[k].r<<",\"cases_processed\":"<<action_counts[k]<<",\"slot_evaluations\":"<<action_slotchecks[k]<<'}';}
 out<<"],\"native_CPU_seconds\":"<<cpu()<<",\"source_BFS\":0,\"actual_graphs_generated\":"<<(hit||inconsistent?1:0)<<",\"actual_graph_orbit_BFS\":"<<(hit?3:inconsistent?1:0)<<"}\n";
 ofstream histogram(dir+"/FIRST_FAIL_SLOT_COUNTS.json");histogram<<"{\"actions\":[";
 for(int k=0;k<6;k++){if(k)histogram<<',';histogram<<"{\"r\":"<<actions[k].r<<",\"counts\":[";for(int j=0;j<324;j++){if(j)histogram<<',';histogram<<failhist[k][j];}histogram<<"]}";}histogram<<"]}\n";
 cout<<(hit?"HIT":inconsistent?"INCONSISTENT":limited?"UNKNOWN":"COMPLETE_NO_HIT")<<" cases "<<visited<<" CPU "<<cpu()<<endl;
 return inconsistent?2:0;
}
