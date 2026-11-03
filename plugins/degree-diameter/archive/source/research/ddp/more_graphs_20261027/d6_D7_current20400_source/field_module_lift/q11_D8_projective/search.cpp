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
#include "actual_builder.hpp"
using namespace std;using U=uint64_t;
uint32_t r32(istream&f){uint32_t x;f.read((char*)&x,4);assert(f);return x;}
int main(int argc,char**argv){
 clock_t start=clock();string dir=argv[3];double budget=stod(argv[4]);auto cpu=[&](){return double(clock()-start)/CLOCKS_PER_SEC;};
 ifstream in(argv[1],ios::binary);char magic[4];in.read(magic,4);assert(string(magic,4)=="QMF1");
 assert(r32(in)==1&&r32(in)==11&&r32(in)==816&&r32(in)==2&&r32(in)==4);
 vector<vector<uint32_t>>forms(816);for(int i=0;i<816;i++){assert(r32(in)==uint32_t(i));int n=r32(in);forms[i].resize(n);in.read((char*)forms[i].data(),4*n);assert(in);}
 vector<int>priority(816);iota(priority.begin(),priority.end(),0);sort(priority.begin(),priority.end(),[&](int a,int b){return forms[a].size()!=forms[b].size()?forms[a].size()<forms[b].size():a<b;});
 vector<array<int,4>>points;ifstream params(argv[2]);for(array<int,4>t;params>>t[0]>>t[1]>>t[2]>>t[3];){assert((t!=array<int,4>{0,1,0,2}));points.push_back(t);}assert(points.size()==1463);
 int products[11][11];for(int a=0;a<11;a++)for(int b=0;b<11;b++)products[a][b]=a*b%11;
 int processed=0,numeric=0,pruned=0,slotchecks=0,lastcase=-1,lastslot=-1;bool hit=false,limited=false,inconsistent=false;
 vector<int>failcount(816);
 if(forms[priority[0]].size()<121){processed=pruned=1463;lastcase=1462;lastslot=priority[0];failcount[lastslot]=1463;}
 else for(int ci=0;ci<1463;ci++){
  ++processed;++numeric;lastcase=ci;auto t=points[ci];bool all=true;
  for(int slot:priority){
   ++slotchecks;U low=0,high=0;bool full=false;
   for(uint32_t packed:forms[slot]){
    int x=0,y=0;for(int k=0;k<4;k++){x+=products[t[k]][(packed>>(4*k))&15];y+=products[t[k]][(packed>>(4*(k+4)))&15];}
    int value=(x%11)+11*(y%11);if(value<64)low|=U(1)<<value;else high|=U(1)<<(value-64);
    if(low==~U(0)&&high==((U(1)<<57)-1)){full=true;break;}
   }
   if(!full){all=false;lastslot=slot;failcount[slot]++;break;}
  }
  if(all){
   hit=verify_candidate(dir,t);inconsistent=!hit;
   ofstream h(dir+"/SURVIVOR_PARAMETERS.json");h<<"{\"case_ordinal\":"<<ci<<",\"normal_tuple\":[";
   for(int k=0;k<4;k++){if(k)h<<',';h<<t[k];}h<<"],\"complete816slots\":true,\"actual_graph_matches\":"<<(hit?"true":"false")<<"}\n";break;
  }
  if(cpu()>budget){limited=true;break;}
 }
 ofstream out(dir+"/NATIVE_RESULT.json");out<<"{\"status\":\""<<(inconsistent?"INCONSISTENT_GENERIC_FORMS_VS_ACTUAL_GRAPH":hit?"FIRST_COMPLETE_D8_HIT":limited?"UNKNOWN_CPU_LIMIT":"ALL_NEW_Q11_PROJECTIVE_SETTINGS_COMPLETE_NO_HIT")
  <<"\",\"new_settings_scope\":1463,\"new_settings_processed\":"<<processed<<",\"numeric_settings\":"<<numeric<<",\"capacity_pruned_settings\":"<<pruned
  <<",\"slot_evaluations\":"<<slotchecks<<",\"cursor\":{\"case_ordinal\":"<<lastcase<<",\"last_failed_slot\":"<<lastslot
  <<"},\"minimum_generic_form_count\":"<<forms[priority[0]].size()<<",\"minimum_generic_slot\":"<<priority[0]<<",\"hit\":"<<(hit?"true":"false")<<",\"CPU_limited\":"<<(limited?"true":"false")
  <<",\"actual_graphs_generated\":"<<(hit||inconsistent?1:0)<<",\"actual_graph_root_BFS\":"<<(hit||inconsistent?1:0)<<",\"native_CPU_seconds\":"<<cpu()<<",\"inherited_control_recomputed\":false}\n";
 ofstream f(dir+"/FIRST_FAIL_SLOT_COUNTS.json");f<<"{\"counts\":[";for(int i=0;i<816;i++){if(i)f<<',';f<<failcount[i];}f<<"]}\n";
 cout<<(hit?"HIT":inconsistent?"INCONSISTENT":limited?"UNKNOWN":"COMPLETE_NO_HIT")<<" newsettings "<<processed<<" CPU "<<cpu()<<endl;
 return inconsistent?2:0;
}
