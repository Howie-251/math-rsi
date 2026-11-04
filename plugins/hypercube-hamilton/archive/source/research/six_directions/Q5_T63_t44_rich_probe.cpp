#include <array>
#include <vector>
#include <fstream>
#include <iostream>
#include <cstdint>
#include <algorithm>
using namespace std;
array<array<int,16>,16> ei;
vector<vector<int>> unit;
vector<int> path;
vector<vector<int>> witnessed;
uint32_t unionmask;
int cycles;
bool stopped;
int stopat=18;
void dfs(int used,int last,uint32_t links){
 if(stopped)return;
 if(used==(1<<unit.size())-1){
  int ix=ei[last][path[0]];if(ix<0)return;
  uint32_t mask=links|(uint32_t(1)<<ix);
  if(mask&~unionmask)witnessed.push_back(path);
  unionmask|=mask;++cycles;
  if(__builtin_popcount(unionmask)>=stopat)stopped=true;
  return;
 }
 for(int j=1;j<(int)unit.size();++j)if(!(used>>j&1)){
  for(int rev=0;rev<(int)unit[j].size();++rev){
   int a=unit[j][rev],b=unit[j].back();
   if(unit[j].size()==2)b=unit[j][1-rev];
   int ix=ei[last][a];if(ix<0)continue;
   path.push_back(a);if(unit[j].size()==2)path.push_back(b);
   dfs(used|(1<<j),b,links|(uint32_t(1)<<ix));
   if(unit[j].size()==2)path.pop_back();path.pop_back();
  }
 }
}
int main(int argc,char**argv){
 if(argc>3)stopat=stoi(argv[3]);
 for(auto&row:ei)row.fill(-1);int k=0;
 for(int a=0;a<16;++a)for(int b=a+1;b<16;++b)if(__builtin_popcount(unsigned(a^b))==1)ei[a][b]=ei[b][a]=k++;
 ifstream in(argv[1],ios::binary);ofstream out(argv[2]);
 ofstream binary;if(argc>4)binary.open(argv[4],ios::binary);
 ofstream certificates;if(argc>5)certificates.open(argv[5],ios::binary);
 array<unsigned char,18> rec;array<long long,33> hist{};int n=0,low=0;
 out<<"{\"low\":[";bool comma=false;
 while(in.read((char*)rec.data(),18)){
  unit.clear();for(int a=0;a<16;++a)if(rec[a]!=255&&a<rec[a])unit.push_back({a,rec[a]});
  for(int a=0;a<16;++a)if(rec[a]==255&&a!=rec[16]&&a!=rec[17])unit.push_back({a});
  if(unit.size()!=8)return 2;
  path=unit[0];unionmask=0;cycles=0;stopped=false;witnessed.clear();dfs(1,path.back(),0);
  int width=__builtin_popcount(unionmask);if(!cycles)return 3;
  if(binary.is_open())binary.write((char*)&unionmask,4);
  if(certificates.is_open()){
   certificates.write((char*)rec.data(),18);unsigned char n=witnessed.size();certificates.write((char*)&n,1);
   for(auto&c:witnessed)for(int x:c){unsigned char y=x;certificates.write((char*)&y,1);}
  }
  ++hist[width];++n;
  if(width<18 || (stopat>32&&!binary.is_open())){++low;if(comma)out<<",";comma=true;
   out<<"{\"record\":"<<n-1<<",\"mate\":[";
   for(int a=0;a<16;++a){if(a)out<<",";out<<int(rec[a]);}
   out<<"],\"omitted\":["<<int(rec[16])<<","<<int(rec[17])<<"],\"union_mask\":"<<unionmask<<",\"cycles_enumerated\":"<<cycles<<"}";
  }
 }
 out<<"],\"records\":"<<n<<",\"below18\":"<<low<<",\"hist\":{";comma=false;
 for(int i=0;i<=32;++i)if(hist[i]){if(comma)out<<",";comma=true;out<<"\""<<i<<"\":"<<hist[i];}
 out<<"}}\n";cout<<n<<" samples; "<<low<<" below18\n";
}
