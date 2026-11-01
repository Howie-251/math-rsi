#include <algorithm>
#include <array>
#include <cassert>
#include <cstdint>
#include <ctime>
#include <fstream>
#include <iostream>
#include <map>
#include <sstream>
#include <string>
#include <vector>
using namespace std;using U32=uint32_t;using I64=int64_t;
vector<int> points;vector<int> extension;
map<int,array<vector<U32>,5>> targetCache;
I64 C;int N;
void targets(int at,int left,U32 mask,vector<U32>&out){if(!left){out.push_back(mask);return;}for(int p=at;p<=N-left;p++)targets(p+1,left-1,mask|(U32(1)<<p),out);}
void choose(int at,int left,U32 selected,int cover){
 if(!left){if(cover!=127)return;++C;for(U32 sub=selected;sub;sub=(sub-1)&selected){int s=__builtin_popcount(sub);if(s>=2&&s<=4)++extension[sub];}return;}
 for(int p=at;p<=N-left;p++)choose(p+1,left-1,selected|(U32(1)<<p),cover|points[p]);
}
struct Family{I64 count;array<I64,3>S;I64 h3,h4;};
Family family(int k){
 extension.assign(U32(1)<<N,0);C=0;choose(0,k,0,0);
 if(!targetCache.count(N)){auto &a=targetCache[N];for(int s=2;s<=4;s++)targets(0,s,0,a[s]);}
 auto &a=targetCache[N];I64 first=0,second=0,h3=0,h4=0;
 for(U32 f:a[2]){I64 v=extension[f];if(v>=first){second=first;first=v;}else if(v>second)second=v;}
 for(U32 f:a[3])h3=max<I64>(h3,extension[f]);for(U32 f:a[4])h4=max<I64>(h4,extension[f]);
 return {C,{0,first,first+second},h3,h4};
}
I64 field(const string&s,const string&name){auto p=s.find("\""+name+"\":");assert(p!=string::npos);p+=name.size()+3;return stoll(s.substr(p));}
int main(int argc,char**argv){
 assert(argc>=3);string input=argv[1],prefix=argv[2];int limit=argc>3?stoi(argv[3]):100;double cpuLimit=argc>4?stod(argv[4]):5;
 clock_t start=clock();ifstream in(input);ofstream out(prefix+"_ROWS.jsonl");string line;int processed=0,strict=0,failed=0;I64 labelsStrict=0,labelsFailed=0,minMargin=100000000;bool interrupted=false;map<int,int>byE;
 while(getline(in,line)){
  if((limit&&processed>=limit)||double(clock()-start)/CLOCKS_PER_SEC>=cpuLimit){interrupted=true;break;}
  auto pos=line.find("\"vector\":[");assert(pos!=string::npos);string nums=line.substr(pos+10);replace(nums.begin(),nums.end(),',',' ');istringstream ss(nums);array<int,21>g{};for(int&i:g){ss>>i;assert(ss);}
  int E=field(line,"E");I64 orbit=field(line,"orbit_size");points.clear();array<int,7>d{};int k=0;
  for(int i=0;i<7;i++)for(int j=i+1;j<7;j++,k++){assert(g[k]>=0);d[i]+=g[k];d[j]+=g[k];for(int m=0;m<g[k];m++)points.push_back((1<<i)|(1<<j));}
  for(int i=0;i<7;i++){assert(d[i]<=4);for(int m=d[i];m<4;m++)points.push_back(1<<i);}
  N=points.size();assert(N==28-E&&N<=17&&N>=14);
  Family f4=family(4),f5=family(5);assert(f4.h4<=1);assert(f4.count+f5.count>0);
  bool good=true;I64 bestMin=100000000;
  out<<"{\"E\":"<<E<<",\"orbit_size\":"<<orbit<<",\"vector\":[";for(int i=0;i<21;i++){if(i)out<<',';out<<g[i];}
  auto emit=[&](const char*name,const Family&f){out<<"],\""<<name<<"\":{\"count\":"<<f.count<<",\"pair_prefix\":["<<f.S[0]<<','<<f.S[1]<<','<<f.S[2]<<"],\"h3\":"<<f.h3<<",\"h4\":"<<f.h4<<"}";};
  // Close the graph vector once; family output below is written directly.
  out<<"],\"C4\":{\"count\":"<<f4.count<<",\"pair_prefix\":["<<f4.S[0]<<','<<f4.S[1]<<','<<f4.S[2]<<"],\"h3\":"<<f4.h3<<",\"h4\":"<<f4.h4<<"},\"C5\":{\"count\":"<<f5.count<<",\"pair_prefix\":["<<f5.S[0]<<','<<f5.S[1]<<','<<f5.S[2]<<"],\"h3\":"<<f5.h3<<",\"h4\":"<<f5.h4<<"},\"parameters\":[";
  bool first=true;for(int u=0;u<=2;u++)for(int v=0;v<=4-u;v++){
   I64 b4=f4.S[u]+(2-u+v)*f4.h3+(18-v)*f4.h4,b5=f5.S[u]+(2-u+v)*f5.h3+(18-v)*f5.h4;
   I64 margin=max(f4.count-b4,f5.count-b5);bestMin=min(bestMin,margin);if(margin<=0)good=false;
   if(!first)out<<',';first=false;out<<'['<<u<<','<<v<<','<<b4<<','<<b5<<','<<f4.count-b4<<','<<f5.count-b5<<']';
  }
  out<<"],\"raw_strict\":"<<(good?"true":"false")<<",\"minimum_best_margin\":"<<bestMin<<"}\n";
  processed++;byE[E]++;minMargin=min(minMargin,bestMin);if(good){strict++;labelsStrict+=orbit;}else{failed++;labelsFailed+=orbit;}
 }
 out.close();ofstream summary(prefix+"_SUMMARY.json");summary<<"{\"complete_representative_input\":"<<(interrupted?"false":"true")<<",\"representatives_processed\":"<<processed<<",\"raw_strict\":"<<strict<<",\"raw_failed\":"<<failed<<",\"labelled_strict\":"<<labelsStrict<<",\"labelled_failed\":"<<labelsFailed<<",\"minimum_best_margin\":"<<minMargin<<",\"cpu_seconds\":"<<double(clock()-start)/CLOCKS_PER_SEC<<",\"parameters_per_graph\":12,\"by_E\":[";bool first=true;for(auto[e,n]:byE){if(!first)summary<<',';first=false;summary<<'['<<e<<','<<n<<']';}summary<<"]}\n";
 cout<<"processed="<<processed<<" strict="<<strict<<" failed="<<failed<<" cpu="<<double(clock()-start)/CLOCKS_PER_SEC<<" complete="<<!interrupted<<"\n";
}
