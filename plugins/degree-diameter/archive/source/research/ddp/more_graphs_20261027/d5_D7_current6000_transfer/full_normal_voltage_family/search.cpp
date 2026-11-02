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
uint8_t FA[9][9],FM[9][9],FN[9];
#include "actual_builder.hpp"
uint32_t r32(istream&f){uint32_t x;f.read((char*)&x,4);assert(f);return x;}
struct Model{int scalar;vector<vector<U>>forms;vector<int>priority;};
int main(int argc,char**argv){
 const clock_t start=clock();auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};string dir=argv[4];double budget=stod(argv[5]);
 ifstream field(argv[3],ios::binary);field.read((char*)FA,81);field.read((char*)FM,81);field.read((char*)FN,9);assert(field);
 ifstream in(argv[1],ios::binary);char magic[4];in.read(magic,4);assert(string(magic,4)=="NMF1");
 assert(r32(in)==1&&r32(in)==9&&r32(in)==2&&r32(in)==480&&r32(in)==12);
 vector<Model>models;for(int mi=0;mi<2;mi++){Model m;m.scalar=r32(in);assert(m.scalar==(mi==0?4:8));m.forms.resize(480);m.priority.resize(480);iota(m.priority.begin(),m.priority.end(),0);
  for(int j=0;j<480;j++){assert(r32(in)==uint32_t(j));int count=r32(in);m.forms[j].resize(count);in.read((char*)m.forms[j].data(),8*count);assert(in);}
  sort(m.priority.begin(),m.priority.end(),[&](int a,int b){return m.forms[a].size()!=m.forms[b].size()?m.forms[a].size()<m.forms[b].size():a<b;});models.push_back(move(m));}
 ifstream pf(argv[2],ios::binary);int count=r32(pf);assert(count==66349);vector<array<uint8_t,6>>points(count);pf.read((char*)points.data(),6*count);assert(pf);
 int processed=0,numeric=0,pruned=0,slotchecks=0,lastmodel=-1,lastcase=-1,lastslot=-1;bool hit=false,limited=false,inconsistent=false;
 vector<int>modeldone(2),modelnumeric(2),modelchecks(2),modelpruned(2);vector<vector<int>>failhist(2,vector<int>(480));
 for(int mi=0;mi<2;mi++){
  auto&m=models[mi];lastmodel=mi;
  if(m.forms[m.priority[0]].size()<81){processed+=count;pruned+=count;modeldone[mi]=modelpruned[mi]=count;failhist[mi][m.priority[0]]=count;lastcase=count-1;lastslot=m.priority[0];continue;}
  for(int ci=0;ci<count;ci++){
   lastcase=ci;auto t=points[ci];assert(!(t[0]==0&&t[1]==1&&t[4]==0&&t[5]==2));++processed;++numeric;++modeldone[mi];++modelnumeric[mi];bool full=true;
   uint8_t product[6][9];for(int j=0;j<6;j++)for(int x=0;x<9;x++)product[j][x]=FM[t[j]][x];
   for(int slot:m.priority){
    ++slotchecks;++modelchecks[mi];U low=0,high=0;bool covered=false;
    for(U packed:m.forms[slot]){
     int x=0,y=0;
     for(int j=0;j<6;j++){x=FA[x][product[j][(packed>>(4*j))&15]];y=FA[y][product[j][(packed>>(4*(j+6)))&15]];}
     int value=x+9*y;if(value<64)low|=U(1)<<value;else high|=U(1)<<(value-64);
     if(low==~U(0)&&high==((U(1)<<17)-1)){covered=true;break;}
    }
    if(!covered){full=false;lastslot=slot;failhist[mi][slot]++;break;}
   }
   if(full){array<int,6>tuple;copy(t.begin(),t.end(),tuple.begin());hit=verify_candidate(m.scalar,tuple,dir);inconsistent=!hit;
    ofstream params(dir+"/SURVIVOR_PARAMETERS.json");params<<"{\"scalar\":"<<m.scalar<<",\"new_case_ordinal\":"<<ci<<",\"normal_tuple\":[";
    for(int j=0;j<6;j++){if(j)params<<',';params<<int(t[j]);}params<<"],\"complete480slots\":true,\"actual_graph_matches\":"<<(hit?"true":"false")<<"}\n";goto terminal;}
   if((ci&127)==0&&cpu()>budget){limited=true;goto terminal;}
  }
  cout<<"MODEL_DONE scalar "<<m.scalar<<" newcases "<<modeldone[mi]<<" CPU "<<cpu()<<endl;
 }
terminal:
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(inconsistent?"INCONSISTENT_GENERIC_FORMS_VS_ACTUAL_GRAPH":hit?"FIRST_COMPLETE_D8_HIT":limited?"UNKNOWN_CPU_LIMIT":"ALL_NEW_NORMAL6_SETTINGS_COMPLETE_NO_HIT")
  <<"\",\"new_settings_scope\":132698,\"new_settings_processed\":"<<processed<<",\"numeric_settings\":"<<numeric<<",\"capacity_pruned_settings\":"<<pruned
  <<",\"slot_evaluations\":"<<slotchecks<<",\"hit\":"<<(hit?"true":"false")<<",\"CPU_limited\":"<<(limited?"true":"false")<<",\"cursor\":{\"model_index\":"<<lastmodel<<",\"scalar\":"<<models[lastmodel].scalar<<",\"new_case_ordinal\":"<<lastcase<<",\"last_failed_slot\":"<<lastslot<<"},\"models\":[";
 for(int mi=0;mi<2;mi++){if(mi)out<<',';out<<"{\"scalar\":"<<models[mi].scalar<<",\"new_settings_processed\":"<<modeldone[mi]<<",\"numeric_settings\":"<<modelnumeric[mi]<<",\"capacity_pruned_settings\":"<<modelpruned[mi]<<",\"slot_evaluations\":"<<modelchecks[mi]<<",\"minimum_forms\":"<<models[mi].forms[models[mi].priority[0]].size()<<'}';}
 out<<"],\"native_CPU_seconds\":"<<cpu()<<",\"actual_graphs_generated\":"<<(hit||inconsistent?1:0)<<",\"actual_graph_orbit_root_BFS\":"<<(hit||inconsistent?2:0)<<",\"inherited162_recomputed\":false,\"source_BFS\":0}\n";
 ofstream fh(dir+"/FIRST_FAIL_SLOT_COUNTS.json");fh<<"{\"models\":[";for(int mi=0;mi<2;mi++){if(mi)fh<<',';fh<<"{\"scalar\":"<<models[mi].scalar<<",\"counts\":[";for(int j=0;j<480;j++){if(j)fh<<',';fh<<failhist[mi][j];}fh<<"]}";}fh<<"]}\n";
 cout<<(hit?"HIT":inconsistent?"INCONSISTENT":limited?"UNKNOWN":"COMPLETE_NO_HIT")<<" newsettings "<<processed<<" CPU "<<cpu()<<endl;
 return inconsistent?2:0;
}
